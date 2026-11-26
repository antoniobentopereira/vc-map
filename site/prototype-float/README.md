# PROTOTYPE: Float feel, one Lens switch, shell layouts

**Throwaway.** Lives only on the `prototype/float` branch and is never merged. Main keeps the verdicts (below), not this code.

Questions it answers:
1. How should Float feel (drift, collisions, cursor push, dot size)?
2. How should a Lens switch move (Float → grouped balls → Float)?
3. Which navigation shell wins: A pill bar, B left rail, C minimal top bar?

## Run

```sh
cd site/prototype-float
npm install      # once
npm run data     # once, regenerates src/companies.json from data/companies.csv
npm run dev      # opens http://localhost:5173/?variant=A
```

## Driving it

- `?variant=A|B|C`, or the ← → buttons (or arrow keys) in the black prototype bar.
- **Lens ⇄** or key `L`: Float ⇄ Fund (stand-in). Fund I/II is only a stand-in grouping to judge the
  transition, because `data/sectors.csv` is still empty. It is not a Sector Lens.
- **Tune** or key `T`: live physics sliders, with fps, current Lens, seconds since the switch and
  "spread" (mean px from dots to their Lens targets; near 0 = settled). Values persist across reloads
  (localStorage). **Copy values** copies them as JSON. `H` hides the prototype chrome.
- Click or tap a dot: it pauses (yellow ring) and a placeholder card opens. Esc or Close resumes it.
- Narrow check: devtools at 320px, or open the Network URL Vite prints on a phone.

Physics runs at a fixed 60 Hz step, so tuned values mean the same on any screen refresh rate.
Logos are the raw files from `site/logos/`: squarish marks cover the circle, and wide wordmarks
(aspect ≥ 1.25) are fitted inside it. Real circle assets come from `tools/logo-studio/` (ADR 0015).

## Verdicts (owner, 2026-11-25)

- **Shell layout chosen: A (bottom pill bar).**
- **Bits to steal from the others:** Layout C's top-bar structure, with Receipts and Views both inside the navigation menu, and two adjustments:
  - Make the menu trigger much more prominent, so it reads as primary site navigation and not a secondary settings menu. About stays a separate standalone `?` button, as in A.
  - On mobile, a single fixed viewport for the Sector Lens cramps the dots and nearly merges the Fund I and Fund II clusters. Let the stage grow vertically into a scrollable page on mobile, so the clusters have room and stay clearly separate.
- **Physics values** (desktop, 1502 px wide):

```json
{
 "drift": 0.06,
 "wander": 0.15,
 "damping": 0.255,
 "collidePad": 4,
 "collideStrength": 0.65,
 "cursorForce": 0.65,
 "cursorRadius": 80,
 "size": 23,
 "ring": 0.2,
 "lensPull": 0.04,
 "lensDrift": 0.25,
 "transitionMs": 1000,
 "staggerMs": 800
}
```

- **Dot radius:** 23 px at desktop, 14 px at 320 px.
- **Transition timing and feel:** the values above are the ones that felt best: 1000 ms ramp, 800 ms stagger, pull 0.04, grouped balls keep 25% of the Float drift.
- **Anything that changes an ADR or the v1 definition of done** (Claude's suggestions, not yet reviewed by the owner):
  - Physics must use a fixed 60 Hz step, or the tuned values change with screen refresh rate.
  - Wide wordmark logos are only readable when fitted inside the circle, which raises the importance of the logo-studio circles (ADR 0015).
  - The v1 text says the Float Lens works at 320 px but gives no minimum dot size. 14 px radius is the tested value.
  - "Scrollable stage on mobile" may conflict with the one-fixed-canvas assumption in ADR 0014. The prototype only tested a fixed viewport.
- **Open questions for the spec** (from building the prototype):
  - Does the mobile scrollable stage apply to Float too, or only to grouped Lenses?
  - Do the Lens pills scroll sideways on phones (as in the prototype), or move into a sheet?
  - Should dots stay clear of the top bar and pill bar (as in the prototype), or be allowed behind them?
  - Does the Views menu hold all eight Views, or are some grouped?
