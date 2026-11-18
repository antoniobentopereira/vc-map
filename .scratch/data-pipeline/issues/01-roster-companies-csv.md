# 01: Roster: all Portfolio companies in a companies CSV

**What to build:** One Python script (standard library only) reads the official Norte Ventures portfolio page and writes every unique Portfolio company to the companies CSV in `data/`, with name, website, Fund (I or II), `is_highlight` and `is_exit`. It prints a report with the total count and and, if any company has both Funds or no Fund, lists it in an error and stops without writing a file, so the owner decides (never resolved automatically). First step: inspect the real page to learn how Highlights and Exits are marked. The owner opens the file in VS Code and sees about 130 rows.

**Blocked by:** None (can start immediately).

**Status:** resolved

- [x] Every unique company on the page appears exactly once, with name, website and Fund
- [x] `is_highlight` and `is_exit` are TRUE/FALSE and match what the page shows
- [x] Companies appearing in both Funds (or with no Fund) are reported with a clear error and stop the script, never silently merged or assigned
- [x] The report states the total count so the owner can compare it with the page
- [x] The owner has looked through the file

## Comments

Implemented in `scripts/build_roster.py` (tests in `tests/test_build_roster.py`). Real page: 130 companies (Fund I: 79, Fund II: 51), 27 Highlights, 8 Exits, matching the page sections.

Decision (owner): a company tagged with both Funds, listed separately in both Funds, or tagged with no Fund is never resolved automatically. The script lists every such company in an error, writes no file and exits non-zero, so the owner decides how the dataset represents it. None occur on the current page.

Owner reviewed `data/companies.csv` and approved. Final code review of the both-Fund/no-Fund fix (commit a71f5ae) found no blocking issues. Non-blocking follow-ups: no test of `main()` (exit code, no file on error); name matching does not strip whitespace; `parse_portfolio` could be split into smaller helpers. The logo column is ticket 02.
