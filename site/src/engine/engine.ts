// The engine: PixiJS stage + a d3-force simulation that never cools. Plain TypeScript, no Svelte.
// Float = random-walk drift + soft collisions + cursor push + soft walls. A Lens sets per-dot
// targets the simulation pulls toward (none for Float).
import { Application, Assets, Circle, Container, Graphics, Rectangle, Sprite, Text, Texture } from "pixi.js";
import { forceCollide, forceSimulation, type Simulation, type SimulationNodeDatum } from "d3-force";
import { dot, physics, tokens } from "./config";
import { drawIcon } from "./icons";
import { deviceOf, layoutLens, type Decoration, type Insets, type LensId, type Point, type Viewport } from "./lens";

export type EngineCompany = { slug: string; name: string; logoUrl: string; fund: string; sector: string };

type Node = SimulationNodeDatum & {
  company: EngineCompany;
  heading: number;
  home?: Point; // Float position before the last Lens switch
  target?: Point;
  delay: number;
  view: Container;
  art: Sprite; // the logo already clipped to a circle (baked once, so every dot is one cheap sprite)
  ring: Graphics;
  source: Texture; // the raw logo
  baked?: Texture;
};

const ease = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - (-2 * t + 2) ** 3 / 2);
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
const clamp = (v: number, lo: number, hi: number) => Math.max(lo, Math.min(hi, v));

export class Engine {
  private app = new Application();
  private sim!: Simulation<Node, undefined>;
  private nodes: Node[] = [];
  private pointer: Point | null = null;
  private lens: LensId = "float";
  private lensStart = 0;
  private paused: Node | null = null;
  private viewport: Viewport = { width: 1, height: 1, insets: { top: 0, right: 0, bottom: 0, left: 0 } };
  private stageHeightPx = 1;
  private radius: number = dot.radiusDesktop;
  private dots = new Container();
  private titles = new Container(); // Lens decorations, above the dots
  private host!: HTMLElement;
  private shrinkTimer = 0;

  /** Called when a Logo dot is clicked (the dot has already been paused). */
  onDotClick: (slug: string) => void = () => {};

  async init(host: HTMLElement) {
    await this.app.init({
      width: host.clientWidth || 1,
      height: host.clientHeight || 1,
      background: tokens.cream,
      antialias: true,
      resolution: Math.min(2, window.devicePixelRatio || 1),
      autoDensity: true,
    });
    this.host = host;
    host.appendChild(this.app.canvas);
    // Pixi blocks touch scrolling on its canvas; allow vertical panning so a tall stage can scroll on phones.
    this.app.canvas.style.touchAction = "pan-y";
    this.app.stage.addChild(this.dots, this.titles);

    this.sim = forceSimulation<Node>([])
      .alpha(1)
      .alphaDecay(0) // never cools down
      .alphaMin(0)
      .velocityDecay(physics.damping)
      .force("collide", forceCollide<Node>(() => this.radius + physics.collidePad).strength(physics.collideStrength).iterations(2))
      .force("drift", () => this.drift())
      .force("lens", () => this.lensPull())
      .force("cursor", () => this.cursor())
      .force("walls", () => this.walls())
      .stop();

    this.setViewport(host.clientWidth, host.clientHeight, this.viewport.insets);

    const canvas = this.app.canvas;
    canvas.addEventListener("pointermove", (e) => {
      if (e.pointerType === "mouse") this.pointer = { x: e.offsetX, y: e.offsetY };
    });
    canvas.addEventListener("pointerleave", () => (this.pointer = null));
    // A tap on empty canvas gives a brief push at that point, so touch has a reaction too.
    canvas.addEventListener("pointerdown", (e) => {
      if (e.pointerType === "mouse") return;
      const hit = this.app.renderer.events.rootBoundary.hitTest(e.offsetX, e.offsetY);
      if (!hit || hit.parent !== this.dots) {
        this.pointer = { x: e.offsetX, y: e.offsetY };
        setTimeout(() => (this.pointer = null), 350);
      }
    });

    // Fixed 60 Hz physics step (accumulator), so the feel is the same on 60/120/144 Hz screens.
    let acc = 0;
    this.app.ticker.add((t) => {
      acc = Math.min(acc + t.deltaMS, physics.stepMs * 4);
      while (acc >= physics.stepMs) {
        this.sim.tick();
        acc -= physics.stepMs;
      }
      for (const n of this.nodes) n.view.position.set(n.x!, n.y!);
    });
  }

  /** Create one Logo dot per company. Replaces any dots already there. */
  async load(companies: EngineCompany[]) {
    this.resume();
    this.dots.removeChildren().forEach((c) => c.destroy({ children: true }));
    const textures = await Promise.all(
      companies.map((c) =>
        Assets.load<Texture>(c.logoUrl.endsWith(".svg") ? { src: c.logoUrl, data: { resolution: 3 } } : c.logoUrl).catch(
          () => Texture.WHITE,
        ),
      ),
    );
    const { width, height } = this.viewport;
    this.nodes = companies.map((company, i) => {
      const view = new Container();
      const art = new Sprite();
      art.anchor.set(0.5);
      const ring = new Graphics();
      view.addChild(art, ring);
      view.eventMode = "static";
      view.cursor = "pointer";
      const node: Node = {
        company,
        heading: Math.random() * Math.PI * 2,
        x: Math.random() * width,
        y: Math.random() * height,
        delay: 0,
        view,
        art,
        ring,
        source: textures[i],
      };
      view.on("pointertap", (e) => {
        e.stopPropagation();
        this.pause(company.slug);
        this.onDotClick(company.slug);
      });
      view.on("pointerover", () => view.scale.set(1.12));
      view.on("pointerout", () => view.scale.set(1));
      this.dots.addChild(view);
      return node;
    });
    this.sim.nodes(this.nodes);
    this.redraw();
    this.setLens(this.lens, true);
  }

  /** Size of the visible area and the space the shell's bars take at its edges. */
  setViewport(width: number, height: number, insets: Insets) {
    this.viewport = { width, height, insets };
    if (this.updateRadius() && this.nodes.length) this.redraw();
    this.setLens(this.lens, true);
  }

  /** Re-read the config object after it was changed (the tuning panel does this). */
  applyConfig() {
    this.sim.velocityDecay(physics.damping);
    this.updateRadius();
    if (this.nodes.length) this.redraw();
  }

  /** Frames per second the renderer is reaching. */
  fps() {
    return this.app.ticker.FPS;
  }

  private updateRadius() {
    const radius = deviceOf(this.viewport) === "phone" ? dot.radiusPhone : dot.radiusDesktop;
    const changed = radius !== this.radius;
    this.radius = radius;
    this.refreshCollide();
    return changed;
  }

  /** d3's collide force caches each node's radius when its radius function is set, so set it again. */
  private refreshCollide() {
    (this.sim?.force("collide") as ReturnType<typeof forceCollide<Node>> | undefined)
      ?.radius(() => this.radius + physics.collidePad)
      .strength(physics.collideStrength);
  }

  /** Switch Lens. Float releases the dots back to where they were; a grouped Lens pulls them to targets. */
  setLens(lens: LensId, relayout = false) {
    if (lens === this.lens && !relayout) return;
    const layout = layoutLens(lens, this.nodes.map((n) => n.company), this.viewport);
    this.setStageHeight(layout.stageHeight, !relayout);
    if (!relayout) {
      this.lensStart = performance.now();
      if (this.lens === "float") for (const n of this.nodes) n.home = { x: n.x!, y: n.y! };
      for (const n of this.nodes) n.delay = Math.random() * physics.staggerMs;
    }
    this.nodes.forEach((n, i) => {
      if (lens === "float") {
        if (!relayout) n.target = n.home;
      } else {
        n.target = layout.targets[i] ?? undefined;
      }
    });
    this.lens = lens;
    this.drawTitles(layout.decorations, relayout);
  }

  /**
   * Grow or shrink the canvas (and with it the scroll range). When leaving a grouped Lens the shrink waits
   * until the dots are back, so they are not squashed against the new bottom edge on the way.
   */
  private setStageHeight(height: number, delayShrink: boolean) {
    clearTimeout(this.shrinkTimer);
    const apply = (h: number) => {
      this.stageHeightPx = h;
      this.app.renderer.resize(this.viewport.width, h);
    };
    if (delayShrink && height < this.stageHeightPx) {
      this.host.scrollTo({ top: 0, behavior: "smooth" });
      this.shrinkTimer = window.setTimeout(() => apply(height), physics.transitionMs * 1.6 + physics.staggerMs);
    } else apply(height);
  }

  /** Ball titles fade in once the dots have mostly arrived (immediately when only re-laying out). */
  private drawTitles(decorations: Decoration[], relayout: boolean) {
    for (const old of this.titles.removeChildren()) old.destroy();
    const start = performance.now() + (relayout ? -Infinity : physics.transitionMs * 0.5);
    for (const d of decorations) {
      const text = new Text({
        text: d.text,
        style: { fontFamily: "Bricolage Grotesque", fontSize: 15, fontWeight: "600", fill: tokens.brown },
      });
      text.anchor.set(0.5, 1);
      text.position.set(d.x, d.y);
      text.alpha = 0;
      const parts: Container[] = [text];
      if (d.icon) {
        const icon = new Graphics();
        drawIcon(icon, d.icon, tokens.brown);
        icon.position.set(d.x, d.y - 33);
        icon.alpha = 0;
        parts.push(icon);
      }
      this.titles.addChild(...parts);
      const fade = () => {
        if (text.destroyed) return;
        const alpha = clamp((performance.now() - start) / 400, 0, 1);
        for (const part of parts) part.alpha = alpha;
        if (alpha < 1) requestAnimationFrame(fade);
      };
      fade();
    }
  }

  /** Stop one dot where it is and mark it selected. */
  pause(slug: string) {
    const node = this.nodes.find((n) => n.company.slug === slug);
    if (!node) return;
    this.resume();
    this.paused = node;
    node.fx = node.x;
    node.fy = node.y;
    node.ring.clear().circle(0, 0, this.radius).stroke({ width: 2, color: tokens.yellow, alpha: 1, alignment: 0 });
  }

  /** Let the paused dot drift again. */
  resume() {
    const node = this.paused;
    if (!node) return;
    node.fx = node.fy = null;
    this.paused = null;
    this.drawRing(node);
  }

  /** Height of the stage in px (the viewport height for Float). */
  stageHeight() {
    return this.stageHeightPx;
  }

  // ---- drawing ---------------------------------------------------------------------------

  /**
   * Bake every logo into a circle texture. A mask per dot would break the GPU batch 130 times a frame
   * (the cause of the lag); one pre-clipped sprite per dot batches into a few draw calls.
   */
  private redraw() {
    const r = this.radius;
    const resolution = Math.min(2, window.devicePixelRatio || 1);
    for (const n of this.nodes) {
      n.baked?.destroy(true);
      n.baked = this.bake(n.source, r, resolution);
      n.art.texture = n.baked;
      n.view.hitArea = new Circle(0, 0, r);
      if (n === this.paused) n.ring.clear().circle(0, 0, r).stroke({ width: 2, color: tokens.yellow, alpha: 1, alignment: 0 });
      else this.drawRing(n);
    }
  }

  private bake(source: Texture, r: number, resolution: number) {
    const { width: tw, height: th } = source;
    // Squarish marks cover the circle; wide wordmarks are fitted inside it so they stay readable.
    const aspect = Math.max(tw, th) / Math.min(tw, th);
    const sprite = new Sprite(source);
    sprite.anchor.set(0.5);
    sprite.scale.set(aspect < 1.25 ? (2 * r) / Math.min(tw, th) : (1.7 * r) / Math.max(tw, th));
    const disc = new Graphics().circle(0, 0, r).fill(0xffffff);
    const mask = new Graphics().circle(0, 0, r).fill(0xffffff);
    sprite.mask = mask;
    const holder = new Container();
    holder.addChild(disc, sprite, mask);
    const texture = this.app.renderer.generateTexture({
      target: holder,
      frame: new Rectangle(-r, -r, 2 * r, 2 * r),
      resolution,
      antialias: true,
    });
    holder.destroy({ children: true });
    return texture;
  }

  /** The ring is drawn by the renderer, never baked into the image. */
  private drawRing(n: Node) {
    n.ring.clear().circle(0, 0, this.radius).stroke({ width: 1, color: tokens.brown, alpha: dot.ringOpacity, alignment: 0 });
  }

  // ---- forces ----------------------------------------------------------------------------

  private drift() {
    const t = performance.now() - this.lensStart;
    const k = this.lens === "float" ? 1 : lerp(1, physics.lensDrift, ease(Math.min(1, t / physics.transitionMs)));
    for (const n of this.nodes) {
      n.heading += (Math.random() - 0.5) * physics.wander;
      n.vx! += Math.cos(n.heading) * physics.drift * k;
      n.vy! += Math.sin(n.heading) * physics.drift * k;
    }
  }

  /** Pull toward the Lens target; back in Float, pull home for the transition, then let go. */
  private lensPull() {
    const now = performance.now();
    for (const n of this.nodes) {
      if (!n.target) continue;
      const t = (now - this.lensStart - n.delay) / physics.transitionMs;
      if (t <= 0) continue;
      let s: number;
      if (this.lens !== "float") s = physics.lensPull * ease(Math.min(1, t));
      else {
        if (t >= 1.6) {
          n.target = undefined;
          continue;
        }
        s = physics.lensPull * Math.sin(Math.min(1, t / 1.6) * Math.PI);
      }
      n.vx! += (n.target.x - n.x!) * s;
      n.vy! += (n.target.y - n.y!) * s;
    }
  }

  private cursor() {
    const ptr = this.pointer;
    if (!ptr) return;
    const R = physics.cursorRadius;
    for (const n of this.nodes) {
      const dx = n.x! - ptr.x;
      const dy = n.y! - ptr.y;
      const d = Math.hypot(dx, dy) || 1;
      if (d > R) continue;
      const f = physics.cursorForce * (1 - d / R) ** 2;
      n.vx! += (dx / d) * f;
      n.vy! += (dy / d) * f;
    }
  }

  /** Soft walls inset from the shell's bars: a gentle push one radius early, a hard clamp at the edge. */
  private walls() {
    const { width, insets } = this.viewport;
    const r = this.radius;
    const L = insets.left + r, T = insets.top + r;
    const R = width - insets.right - r, B = this.stageHeightPx - insets.bottom - r;
    const k = 0.01;
    for (const n of this.nodes) {
      if (n.x! < L + r) n.vx! += (L + r - n.x!) * k;
      if (n.x! > R - r) n.vx! -= (n.x! - R + r) * k;
      if (n.y! < T + r) n.vy! += (T + r - n.y!) * k;
      if (n.y! > B - r) n.vy! -= (n.y! - B + r) * k;
      if (n.x! < L || n.x! > R) (n.x = clamp(n.x!, L, R)), (n.vx! *= -0.3);
      if (n.y! < T || n.y! > B) (n.y = clamp(n.y!, T, B)), (n.vy! *= -0.3);
    }
  }
}
