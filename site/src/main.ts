import "./style.css";
import { Engine } from "./engine/engine";
import data from "./data/companies.json";

// Logo files live in site/logos/; Vite hashes and copies them into the build with relative URLs.
const logoUrls = import.meta.glob<string>("../logos/*", { eager: true, query: "?url", import: "default" });
const logoUrl = (path: string) => logoUrls[`../${path}`] ?? "";

const host = document.getElementById("stage")!;
const engine = new Engine();

await document.fonts.load('600 15px "Bricolage Grotesque"').catch(() => {});
await engine.init(host);
await engine.load(data.companies.map((c) => ({ slug: c.slug, name: c.name, logoUrl: logoUrl(c.logo) })));

const noInsets = { top: 0, right: 0, bottom: 0, left: 0 };
new ResizeObserver(() => engine.setViewport(host.clientWidth, host.clientHeight, noInsets)).observe(host);

// Placeholder until the Company card exists: a clicked dot stays paused for a moment.
engine.onDotClick = () => setTimeout(() => engine.resume(), 1500);
