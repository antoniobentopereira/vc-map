// PROTOTYPE, throwaway.
// Question: how should Float feel, how should a Lens switch move, and which shell layout wins?
// Plan: one canvas, three shells switchable via ?variant=A|B|C, live physics sliders.
import "./style.css";
import { Engine, defaults, autoSize, type Params } from "./engine";
import { SHELLS, LENSES } from "./shells";
import companies from "./companies.json";

const params = new URLSearchParams(location.search);
const keys = Object.keys(SHELLS);
let variant = keys.includes(params.get("variant") ?? "") ? params.get("variant")! : "A";

const stageEl = document.getElementById("stage")!;
const shellEl = document.getElementById("shell")!;
const engine = new Engine();

await document.fonts.load('600 15px "Bricolage Grotesque"');
await engine.init(stageEl, companies);

// ---- shell -------------------------------------------------------------------------------

let shell = mountShell();
function mountShell() {
  const s = SHELLS[variant];
  const h = s.mount(shellEl, {
    lens: () => engine.lens,
    setLens: (id) => go(id),
    about: () => openPanel(aboutHtml()),
  });
  applyInsets();
  h.refresh();
  return h;
}
function applyInsets() {
  engine.insets = SHELLS[variant].insets(window.innerWidth);
}
window.addEventListener("resize", applyInsets);

// Hash URL per Lens: #/lens/float, #/lens/fund
function go(id: string) {
  if (!LENSES.find((l) => l.id === id && l.built)) return;
  location.hash = `#/lens/${id}`;
}
function fromHash() {
  const id = location.hash.match(/^#\/lens\/(\w+)/)?.[1] ?? "float";
  engine.setLens(id === "fund" ? "fund" : "float");
  shell.refresh();
}
window.addEventListener("hashchange", fromHash);
fromHash();

// ---- placeholder Company card and About ---------------------------------------------------

const panel = document.getElementById("panel")!;
engine.onDotTap = (c) =>
  openPanel(`<div class="card-logo" style="background-image:url('${c.logo}')"></div>
    <h2>${c.name}</h2><p class="muted">Fund ${c.fund} · placeholder card (prototype)</p>`);
function openPanel(html: string) {
  panel.innerHTML = `<div class="card" role="dialog">${html}<button class="btn close">Close</button></div>`;
  panel.hidden = false;
  panel.querySelector(".close")!.addEventListener("click", closePanel);
}
function closePanel() {
  panel.hidden = true;
  engine.resume();
}
panel.addEventListener("click", (e) => e.target === panel && closePanel());
const aboutHtml = () => `<h2>About</h2>
  <p>An unofficial, static, visual exploration of Norte Ventures and the companies it has backed.</p>
  <p class="muted">Placeholder: the real About panel explains Estimated values and sources.</p>`;

// ---- PROTOTYPE chrome: tuning panel + variant switcher -----------------------------------

type Slider = [keyof Params, string, number, number, number];
const SLIDERS: Slider[] = [
  ["drift", "Drift strength", 0, 0.1, 0.001],
  ["wander", "Drift wander", 0, 1, 0.01],
  ["damping", "Damping", 0.01, 0.4, 0.005],
  ["collidePad", "Collision padding px", 0, 30, 1],
  ["collideStrength", "Collision firmness", 0.05, 1, 0.05],
  ["cursorForce", "Cursor force", 0, 3, 0.05],
  ["cursorRadius", "Cursor radius px", 20, 300, 5],
  ["size", "Dot radius px", 6, 48, 1],
  ["ring", "Ring opacity", 0, 1, 0.05],
  ["lensPull", "Lens pull", 0.002, 0.15, 0.001],
  ["lensDrift", "Drift while grouped", 0, 1, 0.05],
  ["transitionMs", "Transition ms", 200, 4000, 50],
  ["staggerMs", "Stagger ms", 0, 2000, 25],
];

const tune = document.getElementById("tune")!;
tune.innerHTML = `
  <div class="proto-bar">
    <button data-prev aria-label="Previous variant">←</button>
    <span class="proto-label"></span>
    <button data-next aria-label="Next variant">→</button>
    <button data-tune>Tune</button>
    <button data-lens-toggle title="Switch Float ⇄ Fund (key L)">Lens ⇄</button>
  </div>
  <div class="proto-panel" hidden>
    <div class="proto-head">PROTOTYPE · physics <span class="proto-stats"></span></div>
    ${SLIDERS.map(
      ([k, label, min, max, step]) => `<label><span>${label}</span>
        <input type="range" data-k="${k}" min="${min}" max="${max}" step="${step}" />
        <output data-o="${k}"></output></label>`,
    ).join("")}
    <div class="proto-actions">
      <button data-copy>Copy values</button><button data-reset>Reset</button>
    </div>
    <pre class="proto-json"></pre>
  </div>`;

const pnl = tune.querySelector<HTMLElement>(".proto-panel")!;
const label = tune.querySelector<HTMLElement>(".proto-label")!;
const json = tune.querySelector<HTMLElement>(".proto-json")!;
const stats = tune.querySelector<HTMLElement>(".proto-stats")!;

// Saved slider values survive reloads, so a variant switch (full reload) keeps the tuning.
try {
  const saved = JSON.parse(localStorage.getItem("proto-float-params") ?? "null");
  if (saved) engine.set(saved);
} catch {}

function syncSliders() {
  for (const [k] of SLIDERS) {
    tune.querySelector<HTMLInputElement>(`[data-k=${k}]`)!.value = String(engine.p[k]);
    tune.querySelector<HTMLElement>(`[data-o=${k}]`)!.textContent = String(engine.p[k]);
  }
  json.textContent = JSON.stringify(engine.p, null, 1);
  label.textContent = `${variant} (${SHELLS[variant].name})`;
  try {
    localStorage.setItem("proto-float-params", JSON.stringify(engine.p));
  } catch {}
}
syncSliders();

tune.querySelectorAll<HTMLInputElement>("input[type=range]").forEach((inp) =>
  inp.addEventListener("input", () => {
    engine.set({ [inp.dataset.k!]: Number(inp.value) });
    syncSliders();
  }),
);
tune.querySelector("[data-tune]")!.addEventListener("click", () => (pnl.hidden = !pnl.hidden));
tune.querySelector("[data-reset]")!.addEventListener("click", () => {
  engine.set(defaults(window.innerWidth, window.innerHeight));
  syncSliders();
});
tune.querySelector("[data-copy]")!.addEventListener("click", () =>
  navigator.clipboard?.writeText(JSON.stringify({ variant, width: innerWidth, ...engine.p }, null, 1)),
);
const toggleLens = () => go(engine.lens === "float" ? "fund" : "float");
tune.querySelector("[data-lens-toggle]")!.addEventListener("click", toggleLens);

function cycle(d: number) {
  variant = keys[(keys.indexOf(variant) + d + keys.length) % keys.length];
  const u = new URL(location.href);
  u.searchParams.set("variant", variant);
  history.replaceState(null, "", u);
  shell = mountShell();
  syncSliders();
}
tune.querySelector("[data-prev]")!.addEventListener("click", () => cycle(-1));
tune.querySelector("[data-next]")!.addEventListener("click", () => cycle(1));
window.addEventListener("keydown", (e) => {
  const t = e.target as HTMLElement;
  if (t.matches("input, textarea, select, [contenteditable]")) return;
  if (e.key === "ArrowLeft") cycle(-1);
  if (e.key === "ArrowRight") cycle(1);
  if (e.key === "l" || e.key === "L") toggleLens();
  if (e.key === "t" || e.key === "T") pnl.hidden = !pnl.hidden;
  if (e.key === "h" || e.key === "H") tune.classList.toggle("gone");
  if (e.key === "Escape") closePanel();
});

// Live readout: fps, Lens, time since switch, mean distance to targets.
let last = 0;
engine.onTick = () => {
  const now = performance.now();
  if (now - last < 250) return;
  last = now;
  const since = ((now - engine.lensStart) / 1000).toFixed(1);
  stats.textContent = `${Math.round(engine.app.ticker.FPS)} fps · ${engine.lens} · ${since}s · spread ${engine
    .spread()
    .toFixed(0)}px · auto size ${autoSize(innerWidth, innerHeight)}`;
};

if (import.meta.env.PROD) tune.remove(); // the prototype bar never ships
