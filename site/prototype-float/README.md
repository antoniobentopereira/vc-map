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

## Verdicts (fill in after looking)

- Shell layout chosen:
- Bits to steal from the others:
- Physics values (paste **Copy values** output, note the screen width):
- Dot radius at desktop / at 320px:
- Transition timing and feel notes:
- Anything that changes an ADR or the v1 definition of done:
- Open questions for the spec:
