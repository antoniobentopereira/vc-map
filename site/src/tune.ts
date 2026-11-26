// TEMPORARY tuning panel (dev server only, never in the build): sliders for the physics and dot
// values, like the prototype's. Delete this file and its import in main.ts when tuning is done.
import { dot, dotDefaults, physics, physicsDefaults } from "./engine/config";
import type { Engine } from "./engine/engine";

type Group = "physics" | "dot";
const SLIDERS: [Group, string, string, number, number, number, string][] = [
  ["physics", "drift", "Drift strength", 0, 0.2, 0.001, "How hard each dot is nudged along its wandering heading every tick. Higher = livelier floating."],
  ["physics", "wander", "Drift wander", 0, 1, 0.01, "How fast a dot's heading turns. Low = long smooth curves, high = jittery."],
  ["physics", "damping", "Damping", 0.01, 0.6, 0.005, "Share of velocity lost per tick (friction). Higher = dots slow down quickly, lower = they glide."],
  ["physics", "collidePad", "Collision padding px", 0, 30, 1, "Empty space in px kept between neighbouring dots."],
  ["physics", "collideStrength", "Collision firmness", 0.05, 1, 0.05, "How firmly overlaps are pushed apart. Low = soft, squishy bumps."],
  ["physics", "cursorForce", "Cursor force", 0, 3, 0.05, "How strongly the cursor (or a tap) pushes dots away."],
  ["physics", "cursorRadius", "Cursor radius px", 20, 300, 5, "How far from the cursor, in px, dots feel the push."],
  ["physics", "lensPull", "Lens pull", 0.002, 0.15, 0.001, "How strongly dots are pulled toward their Lens target once fully ramped up."],
  ["physics", "lensDrift", "Drift while grouped", 0, 1, 0.05, "Share of the Float drift dots keep while grouped. 0 = still, 1 = full drift."],
  ["physics", "transitionMs", "Transition ms", 200, 4000, 50, "How long the pull toward a Lens takes to ramp up, in ms."],
  ["physics", "staggerMs", "Stagger ms", 0, 2000, 25, "Maximum random start delay per dot when switching Lens, in ms."],
  ["dot", "radiusDesktop", "Dot radius desktop px", 6, 48, 1, "Dot radius in px on screens 640px wide or more."],
  ["dot", "radiusPhone", "Dot radius phone px", 6, 30, 1, "Dot radius in px on screens under 640px wide."],
  ["dot", "ringOpacity", "Ring opacity", 0, 1, 0.05, "Opacity of the thin brown ring drawn around each dot."],
];
const target = (g: Group): Record<string, number> => (g === "physics" ? physics : dot);
const KEY = "vc-map-tune";

export function mountTune(engine: Engine) {
  try {
    const saved = JSON.parse(localStorage.getItem(KEY) ?? "null");
    if (saved) {
      Object.assign(physics, saved.physics);
      Object.assign(dot, saved.dot);
      engine.applyConfig();
    }
  } catch {}

  const root = document.createElement("div");
  root.id = "tune";
  root.innerHTML = `
    <button data-toggle>Tune (T)</button>
    <div class="tune-panel" hidden>
      <div class="tune-head">TEMPORARY · physics <span class="tune-fps"></span></div>
      ${SLIDERS.map(
        ([g, k, label, min, max, step, tip]) => `<label><span data-tip="${tip.replace(/"/g, "&quot;")}">${label}</span>
          <input type="range" data-g="${g}" data-k="${k}" min="${min}" max="${max}" step="${step}" />
          <output data-o="${g}.${k}"></output></label>`,
      ).join("")}
      <div class="tune-actions"><button data-copy>Copy values</button><button data-reset>Reset</button><button data-default>Make default</button></div>
      <pre class="tune-json"></pre>
    </div>`;
  document.body.appendChild(root);
  const panel = root.querySelector<HTMLElement>(".tune-panel")!;
  const json = root.querySelector<HTMLElement>(".tune-json")!;
  const fps = root.querySelector<HTMLElement>(".tune-fps")!;
  const values = () => JSON.stringify({ physics, dot }, null, 1);

  const sync = () => {
    for (const [g, k] of SLIDERS) {
      root.querySelector<HTMLInputElement>(`[data-g=${g}][data-k=${k}]`)!.value = String(target(g)[k]);
      root.querySelector<HTMLElement>(`[data-o="${g}.${k}"]`)!.textContent = String(target(g)[k]);
    }
    json.textContent = values();
    try {
      localStorage.setItem(KEY, values());
    } catch {}
  };
  sync();

  root.querySelectorAll<HTMLInputElement>("input[type=range]").forEach((input) =>
    input.addEventListener("input", () => {
      target(input.dataset.g as Group)[input.dataset.k!] = Number(input.value);
      engine.applyConfig();
      sync();
    }),
  );
  root.querySelector("[data-reset]")!.addEventListener("click", () => {
    Object.assign(physics, physicsDefaults);
    Object.assign(dot, dotDefaults);
    engine.applyConfig();
    sync();
  });
  root.querySelector<HTMLButtonElement>("[data-default]")!.addEventListener("click", async (e) => {
    const button = e.currentTarget as HTMLButtonElement;
    const body: Record<string, Record<string, number>> = { physics: {}, dot: {} };
    for (const [g, k] of SLIDERS) body[g][k] = target(g)[k];
    const res = await fetch("/__tune/defaults", { method: "POST", body: JSON.stringify(body) });
    button.textContent = res.ok ? "Saved to config.ts" : "Failed";
    // config.ts changed, so the dev server reloads the page with these as the defaults.
  });
  root.querySelector("[data-copy]")!.addEventListener("click", () =>
    navigator.clipboard?.writeText(JSON.stringify({ width: innerWidth, ...JSON.parse(values()) }, null, 1)),
  );
  // Hover pop-up describing a variable. Fixed-position so the panel's scrolling never clips it.
  const tip = document.createElement("div");
  tip.className = "tune-tip";
  tip.hidden = true;
  root.appendChild(tip);
  panel.addEventListener("mouseover", (e) => {
    const label = (e.target as HTMLElement).closest<HTMLElement>("[data-tip]");
    if (!label) return (tip.hidden = true);
    tip.textContent = label.dataset.tip!;
    const box = label.getBoundingClientRect();
    tip.style.left = `${box.left}px`;
    tip.style.top = `${box.bottom + 4}px`;
    tip.hidden = false;
  });
  panel.addEventListener("mouseleave", () => (tip.hidden = true));
  const toggle = () => (panel.hidden = !panel.hidden);
  root.querySelector("[data-toggle]")!.addEventListener("click", toggle);
  window.addEventListener("keydown", (e) => {
    if ((e.target as HTMLElement).matches("input, textarea")) return;
    if (e.key === "t" || e.key === "T") toggle();
    if (e.key === "h" || e.key === "H") root.classList.toggle("gone");
  });
  setInterval(() => (fps.textContent = `${Math.round(engine.fps())} fps`), 500);
}
