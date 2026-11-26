# 10: Sector Lens

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** Choosing Sector in the pill bar animates every Logo dot into one floating ball per Sector, each with an icon and a title above it. Choosing Float returns the dots to where they were and lets them drift again. On phones the balls stack into a vertically scrollable stage. `#/sector` opens straight on this Lens.

**Blocked by:** 02, 03, 04

**Status:** done

- [x] The Sector layout has one ball per Sector, sized by its company count. Balls don't overlap one another or the insets. Each Sector gets an icon and a title, returned by the Lens as decorations and drawn by the engine.
- [x] Dots keep a share of the Float drift while grouped (lensDrift). Switching in either direction uses the prototype's ramped pull and stagger. Returning to Float pulls the dots back to their pre-switch positions, then releases them.
- [x] On a phone the balls stack in one column, and the stage grows taller than the screen and scrolls. On desktop it fits one screen. Float never scrolls.
- [x] The Sector pill is enabled, `#/sector` loads the Lens, and clicking a dot inside a ball opens its Company card just as on Float.
- [x] Vitest at the Lens layout seam checks that:
  - each dot lands in its own Sector's ball;
  - balls don't overlap;
  - there is one title per Sector;
  - the phone stage is taller than the viewport, while the desktop stage fits.
- [x] Checked in the browser at about 1500px and 320px.
