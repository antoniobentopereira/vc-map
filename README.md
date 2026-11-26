# VC Map

An unofficial, static visual exploration of Norte Ventures and its portfolio.

Status: data gathering. The roster of about 130 portfolio companies and their logos are done, the Pilot (10 companies) plus three more are researched in `data/`, and the rest are researched one company at a time (see `docs/stages.md`). The visualization comes after a couple of batches.

## Logo studio

Local tool to crop each logo, pick its circle fill and confirm (details in `tools/logo-studio/README.md`).

1. From the repo root: `python tools/logo-studio/serve.py` (needs `pip install pillow pymupdf`).
2. Open http://localhost:8765 in a browser.
3. Stop with Ctrl+C, then run `python scripts/check_data.py`.

Confirmed choices are saved to `data/companies.csv` and the circles to `site/logos/circles/`. `python scripts/logo_circle.py` rebuilds every circle from the saved choices.
