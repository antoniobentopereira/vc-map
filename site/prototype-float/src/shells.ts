// PROTOTYPE, throwaway. Three structurally different navigation shells over the same canvas.
// Every shell lists every Lens and View from IDEAS.md; unbuilt ones are greyed out.

export type Item = { id: string; label: string; built: boolean; note?: string };

// "fund" is a STAND-IN Lens for the prototype (Sector mapping is still empty).
export const LENSES: Item[] = [
  { id: "float", label: "Float", built: true },
  { id: "fund", label: "Fund (stand-in)", built: true, note: "prototype stand-in for Sector" },
  { id: "sector", label: "Sector", built: false },
  { id: "country", label: "Country", built: false },
  { id: "year", label: "Founding year", built: false },
  { id: "money", label: "Money raised", built: false },
  { id: "status", label: "Status", built: false },
  { id: "employees", label: "Employees", built: false },
  { id: "model", label: "Business model", built: false },
];

export const VIEWS: Item[] = [
  { id: "timeline", label: "Norte Timeline", built: false },
  { id: "orbit", label: "Investors: Orbit", built: false },
  { id: "leaders", label: "Investors: Leaders and followers", built: false },
  { id: "pairings", label: "Investors: Top pairings", built: false },
  { id: "themes", label: "Theme Explorer", built: false },
  { id: "early", label: "How early does Norte get in?", built: false },
  { id: "exits", label: "Exit Wall", built: false },
  { id: "founders", label: "Founder graph", built: false },
];

export const FOOTER = "Unofficial project · not affiliated with Norte Ventures";

export type Ctx = {
  lens: () => string;
  setLens: (id: string) => void;
  about: () => void;
};

export type Shell = {
  name: string;
  insets: (w: number) => { top: number; right: number; bottom: number; left: number };
  mount: (root: HTMLElement, ctx: Ctx) => { refresh: () => void };
};

const soon = (i: Item) => (i.built ? "" : ` disabled title="Coming later"`);
const tag = (i: Item) => (i.built ? "" : `<span class="soon">soon</span>`);

// ---------------------------------------------------------------------------------------
// A. Bottom pill bar for Lenses; Views menu, Receipts and Play top-right.
// ---------------------------------------------------------------------------------------
const pills: Shell = {
  name: "Pill bar",
  insets: (w) => ({ top: 64, right: 0, bottom: w < 640 ? 110 : 96, left: 0 }),
  mount(root, ctx) {
    root.innerHTML = `
      <div class="shA">
        <header class="shA-top">
          <div class="mark">VC Map <span class="sub">Norte portfolio</span></div>
          <div class="shA-actions">
            <div class="menu-wrap">
              <button class="btn" data-menu>Views ▾</button>
              <div class="menu" hidden>
                ${VIEWS.map((v) => `<button class="menu-item"${soon(v)}>${v.label}${tag(v)}</button>`).join("")}
              </div>
            </div>
            <label class="toggle" title="Coming later"><input type="checkbox" disabled /> Receipts</label>
            <button class="btn play" disabled title="Quiz coming later">▶ Play</button>
            <button class="btn icon" data-about aria-label="About">?</button>
          </div>
        </header>
        <nav class="shA-pills" aria-label="Lenses">
          ${LENSES.map((l) => `<button class="pill" data-lens="${l.id}"${soon(l)}>${l.label}</button>`).join("")}
        </nav>
        <footer class="shA-foot">${FOOTER}</footer>
      </div>`;
    wireCommon(root, ctx);
    return { refresh: () => markActive(root, ctx.lens()) };
  },
};

// ---------------------------------------------------------------------------------------
// B. Left rail: everything in one column; becomes a drawer on narrow screens.
// ---------------------------------------------------------------------------------------
const rail: Shell = {
  name: "Left rail",
  insets: (w) => (w < 720 ? { top: 52, right: 0, bottom: 0, left: 0 } : { top: 0, right: 0, bottom: 0, left: 240 }),
  mount(root, ctx) {
    root.innerHTML = `
      <div class="shB">
        <button class="shB-burger btn" aria-label="Menu">☰ <span class="cur"></span></button>
        <aside class="shB-rail">
          <div class="mark">VC Map</div>
          <p class="shB-lede">Every company Norte Ventures has backed.</p>
          <button class="btn play wide" disabled title="Quiz coming later">▶ Play the quiz</button>
          <h3>Lenses</h3>
          <ul>${LENSES.map((l) => `<li><button class="row" data-lens="${l.id}"${soon(l)}>${l.label}${tag(l)}</button></li>`).join("")}</ul>
          <h3>Views</h3>
          <ul>${VIEWS.map((v) => `<li><button class="row"${soon(v)}>${v.label}${tag(v)}</button></li>`).join("")}</ul>
          <div class="shB-bottom">
            <label class="toggle" title="Coming later"><input type="checkbox" disabled /> Receipts</label>
            <button class="link" data-about>About</button>
            <p class="foot">${FOOTER}</p>
          </div>
        </aside>
      </div>`;
    const el = root.querySelector(".shB")!;
    root.querySelector(".shB-burger")!.addEventListener("click", () => el.classList.toggle("open"));
    wireCommon(root, ctx, () => el.classList.remove("open"));
    return {
      refresh: () => {
        markActive(root, ctx.lens());
        root.querySelector(".cur")!.textContent = LENSES.find((l) => l.id === ctx.lens())?.label ?? "";
      },
    };
  },
};

// ---------------------------------------------------------------------------------------
// C. Minimal top bar: the current Lens name IS the selector; everything else behind "Menu".
// ---------------------------------------------------------------------------------------
const minimal: Shell = {
  name: "Minimal top bar",
  insets: () => ({ top: 56, right: 0, bottom: 28, left: 0 }),
  mount(root, ctx) {
    root.innerHTML = `
      <div class="shC">
        <header class="shC-top">
          <div class="mark">VC Map</div>
          <div class="menu-wrap center">
            <button class="shC-lens" data-menu><span class="seen">Seen by </span><b class="cur"></b> ▾</button>
            <div class="menu sheet" hidden>
              <div class="menu-h">Lenses</div>
              ${LENSES.map((l) => `<button class="menu-item" data-lens="${l.id}"${soon(l)}>${l.label}${tag(l)}</button>`).join("")}
            </div>
          </div>
          <div class="shC-right">
            <button class="btn play" disabled title="Quiz coming later">▶ Play</button>
            <div class="menu-wrap">
              <button class="btn" data-menu>Menu</button>
              <div class="menu right" hidden>
                <div class="menu-h">Views</div>
                ${VIEWS.map((v) => `<button class="menu-item"${soon(v)}>${v.label}${tag(v)}</button>`).join("")}
                <hr />
                <label class="toggle menu-item" title="Coming later"><input type="checkbox" disabled /> Receipts</label>
                <button class="menu-item" data-about>About</button>
              </div>
            </div>
          </div>
        </header>
        <footer class="shC-foot">${FOOTER}</footer>
      </div>`;
    wireCommon(root, ctx);
    return {
      refresh: () => {
        markActive(root, ctx.lens());
        root.querySelector(".cur")!.textContent = LENSES.find((l) => l.id === ctx.lens())?.label ?? "";
      },
    };
  },
};

export const SHELLS: Record<string, Shell> = { A: pills, B: rail, C: minimal };

// ---------------------------------------------------------------------------------------

function wireCommon(root: HTMLElement, ctx: Ctx, after = () => {}) {
  root.querySelectorAll<HTMLButtonElement>("[data-lens]").forEach((b) =>
    b.addEventListener("click", () => {
      ctx.setLens(b.dataset.lens!);
      closeMenus(root);
      after();
    }),
  );
  root.querySelectorAll<HTMLButtonElement>("[data-about]").forEach((b) =>
    b.addEventListener("click", () => {
      closeMenus(root);
      after();
      ctx.about();
    }),
  );
  root.querySelectorAll<HTMLButtonElement>("[data-menu]").forEach((b) =>
    b.addEventListener("click", (e) => {
      e.stopPropagation();
      const m = b.nextElementSibling as HTMLElement;
      const open = m.hidden;
      closeMenus(root);
      m.hidden = !open;
    }),
  );
  document.addEventListener("click", () => closeMenus(root));
}

function closeMenus(root: HTMLElement) {
  root.querySelectorAll<HTMLElement>(".menu").forEach((m) => (m.hidden = true));
}

function markActive(root: HTMLElement, lens: string) {
  root.querySelectorAll<HTMLElement>("[data-lens]").forEach((b) => b.classList.toggle("on", b.dataset.lens === lens));
}
