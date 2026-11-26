import "./style.css";
import { Engine } from "./engine/engine";
import data from "./data/companies.json";
import { mount } from "svelte";
import Shell from "./shell/Shell.svelte";
import type { Insets, LensId } from "./engine/lens";
import { hashOf, parseHash, type Route } from "./routes";
import { LENSES, VIEWS } from "./shell/shell-data";
import { nav } from "./shell/nav.svelte";

// Logo files live in site/logos/; Vite hashes and copies them into the build with relative URLs.
const logoUrls = import.meta.glob<string>("../logos/*", { eager: true, query: "?url", import: "default" });
const logoUrl = (path: string) => logoUrls[`../${path}`] ?? "";

const host = document.getElementById("stage")!;
const engine = new Engine();

// The shell reports its bar heights; the engine keeps dots clear of them, also after a resize.
let insets: Insets = { top: 0, right: 0, bottom: 0, left: 0 };
let ready = false;
const fit = () => ready && engine.setViewport(host.clientWidth, host.clientHeight, insets);

// The address is the source of truth for Lens, View and Company; the browser history follows it.
const known = {
  lenses: LENSES.filter((l) => l.built).map((l) => l.id),
  views: VIEWS.filter((v) => v.built).map((v) => v.id),
  companies: data.companies.map((c) => c.slug),
};
const apply = (route: Route) => {
  // Views and Company profiles arrive with their own tickets; until then the dots keep floating.
  if (route.kind === "lens") {
    nav.lens = route.id;
    if (ready) engine.setLens(route.id as LensId);
  }
};
const go = (route: Route) => {
  const hash = hashOf(route);
  if (location.hash !== hash && !(hash === "#/" && (location.hash === "" || location.hash === "#"))) location.hash = hash;
};
addEventListener("hashchange", () => {
  const route = parseHash(location.hash, known);
  apply(route);
  // Rewrite a broken address to the one it resolved to.
  if (hashOf(route) !== location.hash && location.hash !== "") history.replaceState(null, "", hashOf(route));
});

mount(Shell, {
  target: document.getElementById("shell")!,
  props: {
    get activeLens() {
      return nav.lens;
    },
    onLens: (id: string) => go({ kind: "lens", id }),
    onInsets: (next: Insets) => {
      insets = next;
      fit();
    },
  },
});

new ResizeObserver(fit).observe(host);

await document.fonts.load('600 15px "Bricolage Grotesque"').catch(() => {});
await engine.init(host);
await engine.load(data.companies.map((c) => ({ slug: c.slug, name: c.name, logoUrl: logoUrl(c.logo), fund: c.fund })));
ready = true;
fit();
{
  const route = parseHash(location.hash, known);
  if (location.hash !== "" && hashOf(route) !== location.hash) history.replaceState(null, "", hashOf(route));
  apply(route);
}

// Placeholder until the Company card exists: a clicked dot stays paused for a moment.
engine.onDotClick = () => setTimeout(() => engine.resume(), 1500);

// TEMPORARY: physics sliders, dev server only. Delete src/tune.ts and this line when tuning is done.
if (import.meta.env.DEV) (await import("./tune")).mountTune(engine);
