# 01: Site skeleton: 130 raw logos floating

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** Opening the site shows all 130 Logo dots floating on the cream surface with the Float Lens's gas-like drift, soft collisions and cursor push, using the physics values the owner chose in the Float prototype. For now, the logos are the raw Original logos clipped to circles. The site runs on a dev server and builds into a self-contained static folder. A first version of the site data builder produces the data file the site reads.

**Blocked by:** None (can start immediately)

**Status:** done

- [ ] `site/` is a Vite + TypeScript project (ADR 0014). The dev server starts with one command, and the build produces a static folder with relative paths only (ADR 0001).
- [ ] Vitest is set up and runs from the site's package scripts.
- [ ] First version of the Python site data builder: one entry per Portfolio company, with a stable slug, name, Fund and logo path. Tested at its seam with small CSVs in a temp folder.
- [ ] The engine (plain TypeScript, PixiJS + d3-force, no Svelte) draws one Logo dot per company: the raw logo clipped to a circle, with a ring drawn by the renderer at the ring-opacity token.
- [ ] Float behaviour:
  - the simulation never cools down;
  - random-walk drift, cursor push and soft walls;
  - on touch, a tap on empty canvas gives a brief push.
- [ ] Physics advances at a fixed 60 Hz step (accumulator), never once per frame.
- [ ] The prototype's values are the defaults, in one config object (from the prototype verdicts): drift 0.06, wander 0.15, damping 0.255, collidePad 4, collideStrength 0.65, cursorForce 0.65, cursorRadius 80, lensPull 0.04, lensDrift 0.25, transitionMs 1000, staggerMs 800; dot radius 23px on desktop, 14px on phones; ring opacity 0.2.
- [ ] The engine exposes its small interface: load the companies, set the Lens, set the viewport and insets, a callback when a dot is clicked, pause or resume a dot, and report the stage height.
- [ ] The Lens layout seam exists, with the Float Lens. Vitest checks that every dot gets exactly one target (or none, for Float) and that the stage height equals the viewport.
- [ ] Design tokens defined: cream `#FAF6E4`, brown `#462500`, yellow `#FBCF00`, and Bricolage Grotesque with system-ui as fallback.
- [ ] Checked in the browser at about 1500px and 320px: all 130 dots are visible and the motion matches the prototype's feel.
- [ ] The test commands in `docs/agents/testing.md` include the site's Vitest command.
