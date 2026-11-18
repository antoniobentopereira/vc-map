# Testing and checks

Python standard library only; tests use `unittest`.

- **Tests:** `python -m unittest discover -s tests`
- **Data check:** `python scripts/check_data.py`
- A pre-commit hook in `.githooks/` runs both. A fresh clone enables it once with `git config core.hooksPath .githooks`.

## Agreed seams

Tests go at these public seams and nowhere else, so `/tdd` need not ask again. To add a seam, confirm it with the owner first.

- **`check_files(data, root)`** in `scripts/check_data.py`: every validation rule, driven through small CSV files in a temp folder.
- **`first_investment`, `last_round`, `follow_on`** in `scripts/derive.py`: the views derived from a company's Rounds.
- **`write_csv`** in `scripts/build_roster.py`: rebuilding the roster keeps the columns later steps filled in.
- **`docs/data-model.md`**: a test checks that every value the check script allows is named in it.
