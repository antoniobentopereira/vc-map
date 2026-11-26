/// <reference types="vitest/config" />
import { defineConfig } from "vite";

// Relative base so the built folder works from any sub-path (ADR 0001).
export default defineConfig({
  base: "./",
  server: { host: true },
  // vmThreads: the default pool fails to find the suite on Node 26 / Windows.
  test: { include: ["src/**/*.test.ts"], pool: "vmThreads" },
});
