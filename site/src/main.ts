import "./style.css";
import { Engine } from "./engine/engine";
import data from "./data/companies.json";
import { mount } from "svelte";
import Shell from "./shell/Shell.svelte";
import type { Insets } from "./engine/lens";

// Logo files live in site/logos/; Vite hashes and copies them into the build with relative URLs.
const logoUrls = import.meta.glob<string>("../logos/*", { eager: true, query: "?url", import: "default" });
const logoUrl = (path: string) => logoUrls[`../${path}`] ?? "";

const host = document.getElementById("stage")!;
const engine = new Engine();

// The shell reports its bar heights; the engine keeps dots clear of them, also after a resize.
let insets: Insets = { top: 0, right: 0, bottom: 0, left: 0 };
let ready = false;
const fit = () => ready && engine.setViewport(host.clientWidth, host.clientHeight, insets);

mount(Shell, {
  target: document.getElementById("shell")!,
  props: {
    activeLens: "float",
    onLens: () => {}, // Float is the only built Lens; Sector arrives with its own ticket.
    onInsets: (next: Insets) => {
      insets = next;
      fit();
    },
  },
});

new ResizeObserver(fit).observe(host);

await document.fonts.load('600 15px "Bricolage Grotesque"').catch(() => {});
await engine.init(host);
await engine.load(data.companies.map((c) => ({ slug: c.slug, name: c.name, logoUrl: logoUrl(c.logo) })));
ready = true;
fit();

// Placeholder until the Company card exists: a clicked dot stays paused for a moment.
engine.onDotClick = () => setTimeout(() => engine.resume(), 1500);

// TEMPORARY: physics sliders, dev server only. Delete src/tune.ts and this line when tuning is done.
if (import.meta.env.DEV) (await import("./tune")).mountTune(engine);
