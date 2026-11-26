# Logo studio

A throwaway local page that walks through each logo in four steps and saves the choices, so the circles can always be rebuilt (ADR 0015, ADR 0008).

1. `python tools/logo-studio/serve.py`
2. Open http://localhost:8765

For each logo:

1. **Crop**: drag a box over the raw logo to strip padding and borders (double-click resets).
2. **Fill**: pick a preset (white, cream, Norte brown, black) or click the cropped logo to sample a color. The first suggestion comes from the old `logo_background` word: `dark` suggests black, `light` or `both` suggest white.
3. **Preview**: the circle on the cream surface with its ring, large and at the real desktop and phone dot sizes, updating live.
4. **Confirm**: writes `logo_crop` and `logo_background` (`#rrggbb`) to `data/companies.csv` (atomically, no other column) and renders the circle into `site/logos/circles/`. Then it moves to the next logo not yet confirmed.

"Only not confirmed" hides the logos already confirmed. Needs Pillow and PyMuPDF (`pip install pillow pymupdf`). Stop with Ctrl+C, then run `python scripts/check_data.py`.

`python scripts/logo_circle.py` rebuilds every circle from the saved columns. Logos replaced by `scripts/fetch_logos.py` lose their choices and need confirming again.
