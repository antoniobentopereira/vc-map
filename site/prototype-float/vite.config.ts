import { defineConfig } from "vite";

// PROTOTYPE. Raw logos are served straight from site/logos/ as the public dir.
export default defineConfig({
  base: "./",
  publicDir: "../logos",
  server: { host: true },
});
