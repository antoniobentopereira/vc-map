# Testing and checks

Python standard library only; tests use `unittest`.

- **Tests:** `python -m unittest discover -s tests`
- **Data check:** `python scripts/check_data.py`
- **Site tests (Vitest):** `cd site && npm run test` (types: `npm run typecheck`; build: `npm run build`; data file: `npm run data`). Node lives in `C:\Program Files
odejs`; PowerShell needs `npm.cmd`.
- A pre-commit hook in `.githooks/` runs both. A fresh clone enables it once with `git config core.hooksPath .githooks`.

## Agreed seams

Tests go at these public seams and nowhere else, so `/tdd` need not ask again. To add a seam, confirm it with the owner first.

- **`check_files(data, root)`** in `scripts/check_data.py`: every validation rule, driven through small CSV files in a temp folder.
- **`first_investment`, `last_round`, `follow_on`** in `scripts/derive.py`: the views derived from a company's Rounds.
- **`write_csv`** in `scripts/build_roster.py`: rebuilding the roster keeps the columns later steps filled in.
- **`docs/data-model.md`**: a test checks that every value the check script allows is named in it.
- **The site data builder** (Python): `data/` in, the site's one JSON file out. Tests check the contract with small CSVs in a temp folder: `{value, basis, confidence, source}` per field, Sector from the mapping, missing fields absent, Rounds with Norte's participation, refusal when the check fails.
- **The logo circle renderer** (Python): source image + `logo_crop` + `logo_background` in, a 512px circle out. Tested on tiny generated images (transparent corners, fill behind the mark, wordmarks fitted, same inputs give the same output). The logo studio's save goes through it.
- **`save_choice`** in `tools/logo-studio/serve.py`: only `logo_crop` and `logo_background` change, the write is atomic, bad input or an unrenderable logo leaves the CSV untouched, and the circle is rendered.
- **Lens layout** (TypeScript, Vitest): a pure function from companies, Lens and viewport to one target per Logo dot, the stage height and the ball titles and balls (Float, Fund and Sector so far).
- **Routes** (TypeScript, Vitest): hash address to app state and back; unknown or unbuilt addresses resolve to Float.
- Physics feel, Pixi rendering and Svelte views are not unit-tested; they are checked in the browser at about 1500px and 320px with the `run` skill.
- `npm run typecheck` does not check `.svelte` files (svelte-check does not yet support TypeScript 7), so keep Svelte components thin.
- **`check_workflow`, `build_workflow`** in `scripts/linkedin.py`: the Linked API client refuses any workflow with an action that is not a read, and every command builds an allowed workflow. `run` hands back the `workflowId` of a parked workflow and prints it on stderr as soon as it starts (tested with `_request` replaced by a fake). No test calls the real API.
