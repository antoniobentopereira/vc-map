// PROTOTYPE, throwaway. Dot engine: PixiJS stage + a d3-force simulation that never cools.
// Float = drift + soft collisions + cursor push. A Lens = per-dot targets the sim pulls toward.
import { Application, Assets, Container, Graphics, Sprite, Text, Texture, Circle } from "pixi.js";
import { forceSimulation, forceCollide, type Simulation, type SimulationNodeDatum } from "d3-force";

export type Company = { name: string; logo: string; fund: string; bg: string };

export type Params = {
  drift: number; // velocity added per tick by the random walk
  wander: number; // how fast each dot's drift heading turns
  damping: number; // d3 velocityDecay: share of velocity lost per tick
  collidePad: number; // px of empty space kept between dots
  collideStrength: number; // 0..1, how hard overlaps are resolved (soft = low)
  cursorForce: number; // push strength at the cursor
  cursorRadius: number; // px reach of the push
  size: number; // dot radius in px
  ring: number; // ring opacity
  lensPull: number; // pull toward the Lens target once fully ramped
  lensDrift: number; // drift multiplier while grouped (keeps balls alive)
  transitionMs: number; // pull ramp duration
  staggerMs: number; // max random start delay per dot
};

export const defaults = (w: number, h: number): Params => ({
  drift: 0.02,
  wander: 0.25,
  damping: 0.06,
  collidePad: 4,
  collideStrength: 0.7,
  cursorForce: 0.6,
  cursorRadius: 120,
  size: autoSize(w, h),
  ring: 0.35,
  lensPull: 0.035,
  lensDrift: 0.25,
  transitionMs: 1400,
  staggerMs: 350,
});

/** Radius so 130 dots cover ~16% of the viewport, clamped to a readable range. */
export function autoSize(w: number, h: number) {
  return Math.round(Math.max(11, Math.min(30, Math.sqrt((0.16 * w * h) / (130 * Math.PI)))));
}

type Node = SimulationNodeDatum & {
  i: number;
  c: Company;
  heading: number;
  home?: { x: number; y: number }; // Float position before the last Lens switch
  target?: { x: number; y: number };
  delay: number;
  view: Container;
  sprite: Sprite;
  disc: Graphics;
  mask: Graphics;
  ringG: Graphics;
  tex: Texture;
};

type Group = { key: string; label: string; ids: number[] };

export class Engine {
  app = new Application();
  sim!: Simulation<Node, undefined>;
  nodes: Node[] = [];
  p!: Params;
  pointer: { x: number; y: number } | null = null;
  lens: "float" | "fund" = "float";
  lensStart = 0; // performance.now() of the last switch
  paused: Node | null = null;
  labels = new Container();
  onDotTap: (c: Company) => void = () => {};
  onTick: () => void = () => {};
  // Space the shell takes at screen edges, so balls and walls avoid it.
  insets = { top: 0, right: 0, bottom: 0, left: 0 };

  async init(host: HTMLElement, companies: Company[]) {
    await this.app.init({
      resizeTo: host,
      background: "#FAF6E4",
      antialias: true,
      resolution: Math.min(2, window.devicePixelRatio || 1),
      autoDensity: true,
    });
    host.appendChild(this.app.canvas);
    const { width: w, height: h } = this.app.screen;
    this.p = defaults(w, h);

    const textures = await Promise.all(
      companies.map((c) =>
        Assets.load<Texture>(c.logo.endsWith(".svg") ? { src: c.logo, data: { resolution: 3 } } : c.logo).catch(
          () => Texture.WHITE,
        ),
      ),
    );

    const stage = new Container();
    this.app.stage.addChild(stage, this.labels);

    this.nodes = companies.map((c, i) => {
      const view = new Container();
      const disc = new Graphics();
      const sprite = new Sprite(textures[i]);
      sprite.anchor.set(0.5);
      const mask = new Graphics();
      const ringG = new Graphics();
      view.addChild(disc, sprite, mask, ringG);
      sprite.mask = mask;
      view.eventMode = "static";
      view.cursor = "pointer";
      const n: Node = {
        i,
        c,
        heading: Math.random() * Math.PI * 2,
        x: this.insets.left + Math.random() * w,
        y: Math.random() * h,
        delay: 0,
        view,
        sprite,
        disc,
        mask,
        ringG,
        tex: textures[i],
      };
      view.on("pointertap", (e) => {
        e.stopPropagation();
        this.pause(n);
      });
      view.on("pointerover", () => view.scale.set(1.12));
      view.on("pointerout", () => view.scale.set(1));
      stage.addChild(view);
      return n;
    });
    this.redraw();

    this.sim = forceSimulation(this.nodes)
      .alpha(1)
      .alphaDecay(0)
      .alphaMin(0)
      .velocityDecay(this.p.damping)
      .force("collide", forceCollide<Node>(() => this.p.size + this.p.collidePad).strength(this.p.collideStrength).iterations(2))
      .force("drift", () => this.drift())
      .force("lens", () => this.lensPull())
      .force("cursor", () => this.cursor())
      .force("walls", () => this.walls())
      .stop();

    const canvas = this.app.canvas;
    canvas.addEventListener("pointermove", (e) => {
      if (e.pointerType === "mouse") this.pointer = { x: e.offsetX, y: e.offsetY };
    });
    canvas.addEventListener("pointerleave", () => (this.pointer = null));
    // Tap on empty canvas (touch or mouse) gives a one-off push, so phones feel the "cursor" too.
    canvas.addEventListener("pointerdown", (e) => {
      if (e.pointerType !== "mouse") {
        this.pointer = { x: e.offsetX, y: e.offsetY };
        setTimeout(() => (this.pointer = null), 350);
      }
    });

    // Fixed 60 Hz physics step, so tuned values feel the same on 60/120/144 Hz screens.
    let acc = 0;
    this.app.ticker.add((t) => {
      acc = Math.min(acc + t.deltaMS, 1000 / 15);
      while (acc >= 1000 / 60) {
        this.sim.tick();
        acc -= 1000 / 60;
      }
      for (const n of this.nodes) n.view.position.set(n.x!, n.y!);
      this.onTick();
    });
    this.app.renderer.on("resize", () => this.lens === "fund" && this.setLens("fund", true));
  }

  /** Apply changed params. Size and ring need a redraw; the rest are read live. */
  set(p: Partial<Params>) {
    Object.assign(this.p, p);
    this.sim.velocityDecay(this.p.damping);
    (this.sim.force("collide") as ReturnType<typeof forceCollide<Node>>)
      .radius(() => this.p.size + this.p.collidePad)
      .strength(this.p.collideStrength);
    if ("size" in p || "ring" in p) this.redraw();
    if ("size" in p && this.lens === "fund") this.setLens("fund", true);
  }

  redraw() {
    const r = this.p.size;
    for (const n of this.nodes) {
      const { width: tw, height: th } = n.tex;
      // Squarish marks cover the circle; wide wordmarks are fitted inside it so they stay readable.
      const aspect = Math.max(tw, th) / Math.min(tw, th);
      n.sprite.scale.set(aspect < 1.25 ? (2 * r) / Math.min(tw, th) : (1.7 * r) / Math.max(tw, th));
      n.mask.clear().circle(0, 0, r).fill(0xffffff);
      n.disc.clear().circle(0, 0, r).fill(discColor(n.c.bg));
      n.ringG.clear().circle(0, 0, r).stroke({ width: 1, color: 0x462500, alpha: this.p.ring, alignment: 0 });
      n.view.hitArea = new Circle(0, 0, r);
    }
  }

  pause(n: Node) {
    this.resume();
    this.paused = n;
    n.fx = n.x;
    n.fy = n.y;
    n.ringG.clear().circle(0, 0, this.p.size).stroke({ width: 2, color: 0xfbcf00, alpha: 1, alignment: 0 });
    this.onDotTap(n.c);
  }

  resume() {
    const n = this.paused;
    if (!n) return;
    n.fx = n.fy = null;
    this.paused = null;
    this.redraw();
  }

  // ---- forces ----------------------------------------------------------------------------

  private drift() {
    const t = performance.now() - this.lensStart;
    const k = this.lens === "float" ? 1 : lerp(1, this.p.lensDrift, ease(Math.min(1, t / this.p.transitionMs)));
    for (const n of this.nodes) {
      n.heading += (Math.random() - 0.5) * this.p.wander;
      n.vx! += Math.cos(n.heading) * this.p.drift * k;
      n.vy! += Math.sin(n.heading) * this.p.drift * k;
    }
  }

  /** Pull toward the Lens target. Ramps up with easing; on return to Float it ramps up then lets go. */
  private lensPull() {
    const now = performance.now();
    for (const n of this.nodes) {
      if (!n.target) continue;
      const t = (now - this.lensStart - n.delay) / this.p.transitionMs;
      if (t <= 0) continue;
      let s: number;
      if (this.lens === "fund") s = this.p.lensPull * ease(Math.min(1, t));
      else {
        // Back to Float: pull home for the transition, then release so drift takes over.
        if (t >= 1.6) {
          n.target = undefined;
          continue;
        }
        s = this.p.lensPull * Math.sin(Math.min(1, t / 1.6) * Math.PI);
      }
      n.vx! += (n.target.x - n.x!) * s;
      n.vy! += (n.target.y - n.y!) * s;
    }
  }

  private cursor() {
    const ptr = this.pointer;
    if (!ptr) return;
    const R = this.p.cursorRadius;
    for (const n of this.nodes) {
      const dx = n.x! - ptr.x;
      const dy = n.y! - ptr.y;
      const d = Math.hypot(dx, dy) || 1;
      if (d > R) continue;
      const f = this.p.cursorForce * (1 - d / R) ** 2;
      n.vx! += (dx / d) * f;
      n.vy! += (dy / d) * f;
    }
  }

  private walls() {
    const { width: w, height: h } = this.app.screen;
    const r = this.p.size;
    // Hard edge: the whole dot stays clear of the shell. Soft zone: a gentle push starts one radius earlier.
    const L = this.insets.left + r, T = this.insets.top + r;
    const R = w - this.insets.right - r, B = h - this.insets.bottom - r;
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

  // ---- lenses ----------------------------------------------------------------------------

  /** Switch Lens. `fund` is a STAND-IN grouping (Fund I / II) for judging the transition only. */
  setLens(lens: "float" | "fund", relayout = false) {
    if (lens === this.lens && !relayout) return;
    if (!relayout) this.lensStart = performance.now();
    this.labels.removeChildren();
    if (lens === "fund") {
      if (this.lens === "float") for (const n of this.nodes) n.home = { x: n.x!, y: n.y! };
      const groups = groupBy(this.nodes, (n) => n.c.fund).map(([key, ns]) => ({
        key,
        label: `Fund ${key}`,
        ids: ns.map((n) => n.i),
      }));
      this.layoutBalls(groups);
    } else {
      for (const n of this.nodes) n.target = n.home;
    }
    if (!relayout) for (const n of this.nodes) n.delay = Math.random() * this.p.staggerMs;
    this.lens = lens;
  }

  private layoutBalls(groups: Group[]) {
    const { width: w, height: h } = this.app.screen;
    const { top, right, bottom, left } = this.insets;
    const W = w - left - right, H = h - top - bottom;
    const horizontal = W >= H;
    const cell = this.p.size + this.p.collidePad;
    groups.forEach((g, gi) => {
      const frac = (gi + 0.5) / groups.length;
      const cx = left + (horizontal ? W * frac : W / 2);
      const cy = top + (horizontal ? H / 2 + 14 : H * frac + 14);
      // Sunflower spiral targets: a packed disc without everyone aiming at one point.
      const ballR = cell * Math.sqrt(g.ids.length) * 1.05;
      g.ids.forEach((id, k) => {
        const a = k * 2.39996;
        const rr = cell * 1.05 * Math.sqrt(k + 0.5);
        this.nodes[id].target = { x: cx + Math.cos(a) * rr, y: cy + Math.sin(a) * rr };
      });
      const t = new Text({
        text: `${g.label} · ${g.ids.length}`,
        style: { fontFamily: "Bricolage Grotesque", fontSize: 15, fontWeight: "600", fill: 0x462500 },
      });
      t.anchor.set(0.5, 1);
      t.position.set(cx, cy - ballR - 10);
      t.alpha = 0;
      this.labels.addChild(t);
      const t0 = performance.now();
      const fade = () => {
        t.alpha = Math.min(1, (performance.now() - t0 - this.p.transitionMs * 0.5) / 400);
        if (t.alpha < 1 && !t.destroyed) requestAnimationFrame(fade);
      };
      fade();
    });
  }

  /** Mean distance (px) from dots to their Lens targets: shows when the switch has settled. */
  spread() {
    let s = 0, k = 0;
    for (const n of this.nodes)
      if (n.target) {
        s += Math.hypot(n.target.x - n.x!, n.target.y - n.y!);
        k++;
      }
    return k ? s / k : 0;
  }
}

function discColor(bg: string) {
  if (bg.startsWith("#")) return parseInt(bg.slice(1), 16);
  return bg === "dark" ? 0x2a2a2a : 0xffffff;
}
const ease = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - (-2 * t + 2) ** 3 / 2);
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
const clamp = (v: number, a: number, b: number) => Math.max(a, Math.min(b, v));
function groupBy<T>(xs: T[], f: (x: T) => string): [string, T[]][] {
  const m = new Map<string, T[]>();
  for (const x of xs) m.set(f(x), [...(m.get(f(x)) ?? []), x]);
  return [...m.entries()].sort(([a], [b]) => a.localeCompare(b));
}
