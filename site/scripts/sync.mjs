// Deliberate release step (ADR 0001): copies the built site/dist/ into mysite/public/vc-map/.
// Run by hand with `npm run sync`; never wired to save or build.
import { cpSync, existsSync, rmSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";

const dist = fileURLToPath(new URL("../dist/", import.meta.url));
const target = fileURLToPath(new URL("../../../mysite/public/vc-map/", import.meta.url));

if (!existsSync(dist + "index.html")) {
  console.error("site/dist/ is missing or empty. Run `npm run build` first.");
  process.exit(1);
}
if (!existsSync(fileURLToPath(new URL("../../../mysite/public/", import.meta.url)))) {
  console.error("mysite/public/ not found next to vc-map/. Nothing copied.");
  process.exit(1);
}
rmSync(target, { recursive: true, force: true });
mkdirSync(target, { recursive: true });
cpSync(dist, target, { recursive: true });
console.log(`Synced ${dist} -> ${target}`);
