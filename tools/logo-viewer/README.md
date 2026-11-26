# Logo viewer

A local page for choosing which page background each logo is legible on, so a white logo is not shown on white.

1. `python tools/logo-viewer/serve.py`
2. Open http://localhost:8765

Each logo shows on black (left) and white (right). Pick `dark`, `light` or `both` under it; each click is saved at once to the `logo_background` column of `data/companies.csv`. "Only not reviewed" hides the logos already picked. Stop with Ctrl+C.

Run `python scripts/check_data.py` afterwards. Logos replaced by `scripts/fetch_logos.py` lose their pick and need reviewing again.
