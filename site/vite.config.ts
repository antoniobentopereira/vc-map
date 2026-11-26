/// <reference types="vitest/config" />
import { readFileSync, writeFileSync } from "node:fs";
import { defineConfig, type Plugin } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// TEMPORARY, dev server only: the tuning panel's "Make default" posts its values here and they are
// written into the `physics` and `dot` objects of src/engine/config.ts. Remove with src/tune.ts.
function tuneDefaults(): Plugin {
  return {
    name: "tune-defaults",
    apply: "serve",
    configureServer(server) {
      server.middlewares.use("/__tune/defaults", (req, res) => {
        if (req.method !== "POST") return void res.writeHead(405).end();
        let body = "";
        req.on("data", (chunk) => (body += chunk));
        req.on("end", () => {
          try {
            const file = new URL("./src/engine/config.ts", import.meta.url);
            let text = readFileSync(file, "utf8");
            const values = JSON.parse(body) as Record<string, Record<string, number>>;
            for (const [group, keys] of Object.entries(values)) {
              const start = text.indexOf(`export const ${group} = {`);
              const end = text.indexOf("};", start) + 2;
              if (start < 0 || end < start) throw new Error(`no ${group} object in config.ts`);
              let block = text.slice(start, end);
              for (const [key, value] of Object.entries(keys)) {
                if (!/^\w+$/.test(key) || !Number.isFinite(value)) throw new Error(`bad value for ${key}`);
                block = block.replace(new RegExp(`(\\b${key}:\\s*)-?[\\d.]+`), `$1${value}`);
              }
              text = text.slice(0, start) + block + text.slice(end);
            }
            writeFileSync(file, text);
            res.writeHead(200).end("ok");
          } catch (e) {
            res.writeHead(400).end(String(e));
          }
        });
      });
    },
  };
}

// Relative base so the built folder works from any sub-path (ADR 0001).
export default defineConfig({
  base: "./",
  plugins: [svelte(), tuneDefaults()],
  server: { host: true },
  // vmThreads: the default pool fails to find the suite on Node 26 / Windows.
  test: { include: ["src/**/*.test.ts"], pool: "vmThreads" },
});
