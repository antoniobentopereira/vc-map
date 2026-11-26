# Status

Where the project stands. Short and current: update at the end of each working session. If this disagrees with the repo, the repo wins and this file gets fixed. Concepts live in `IDEAS.md`, terms in `GLOSSARY.md`, decisions in `docs/adr/`, stages in `docs/stages.md`.

## Phase
Stage 4, Visualization v1 (definition of done in `docs/stages.md`). v1 is built and synced into `mysite/public/vc-map/` (2026-11-26); waiting on the owner's visual sign-off at ~1500px and 320px, then commit and deploy mysite. Stages 1 to 3 (Roster, Pilot, Scale-up) are done: every Roster company has been researched (see `researched_on` in `data/companies.csv`).

## Next
1. Done: Float prototype on branch `prototype/float` (never merged); verdicts in its `site/prototype-float/README.md`. Spec written: `.scratch/visualization-v1/spec.md` (v1 = Float + Sector Lens + shell + Company card and profile). Next: `/to-tickets`.
2. Sub-sector to Sector mapping in `data/sectors.csv`: Claude proposes, owner reviews.
3. `tools/logo-studio/` is built (replaced `tools/logo-viewer/`); next, the owner confirms every logo in it (ADR 0015).
4. Real `site/`: done so far: Vite project, first data-to-JSON script, engine and Float on raw logos (ticket 01). Still to do: shell, Company card and profile, sync command.

5. Revisit the design of the Company profile page (`site/src/shell/Profile.svelte`): v1 is functional, not designed. Owner wants to rework it.

## Decisions (one line each)
- Stack: Vite + TypeScript, Svelte, PixiJS, d3-force, Matter.js (games only), GSAP, d3-geo. Breaks mysite's rules on purpose (ADR 0014).
- `site/` is source, `site/dist/` is output, copied to mysite by an explicit sync command (ADR 0001).
- Logo circles: chosen by hand, rebuilt from `logo_crop` and `logo_background` (hex) (ADR 0015).
- Desktop-first; Float, Company card, shell and simple Lenses work at 320px by tap.
- Palette: cream #FAF6E4 surface, brown #462500 ink and hairlines, yellow #FBCF00 as the rare accent. Font: Bricolage Grotesque.
- Estimated: muted brown + dotted underline, "≈" before numbers, dashed outlines on shapes; explained in the About panel.
- Site JSON carries value, Basis, Confidence and Source for every field (for Receipts mode later).
- Hash URLs for every Lens, View and Company profile.
- Float is the default Lens. The shell shows every idea, unbuilt ones greyed out.
- Lenses built: Float, Fund (two balls, Fund I and Fund II). Sector is next, after its mapping.
- Shell: bottom pill bar for Lenses (scrolls sideways on phones); top-bar menu holding a flat list of Views (Investors is one entry) and the Receipts toggle; standalone `?` for About. Dots stay clear of the bars.
- Engine is plain TypeScript behind a small interface; Svelte owns shell, card, profile, About (ADR 0014).
- Footer: unofficial notice plus a small "works best on desktop" note.

## Data caveats
- `data/sectors.csv`: no Sector assigned yet.
- `logo_background` is moving from `dark`/`light`/`both` to hex; both accepted until all logos are confirmed.

## Log (newest first)
- 2026-11-26: v1 release: `npm run sync` (in `site/`) copies `site/dist/` to `mysite/public/vc-map/`; tests, data check and build pass; subpath serving checked. Next phase: rework the Company profile design, then Receipts mode and further Lenses.
- 2026-11-25: Float prototype judged (shell A with C's menu, physics values, 23/14px dots); ADR 0014 and stage 4 updated with its lessons.
- 2026-11-25: Visualization planning session. ADRs 0014 and 0015, ADR 0001 updated, glossary gained Logo dot, Lens, View, Company card, Company profile; stage 4 definition of done set.
