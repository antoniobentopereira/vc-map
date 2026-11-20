# 06: Gap-filling templates and record details

**What to build:** Each missing field offers a collapsed "How to add this" with the exact `claims.csv` line pre-filled (company name, field name), a copy button, and the expected format and allowed values (City, Country; `b2b`/`b2c`/`b2b2c`; the Sub-sector list from `sectors.csv`; the Status table; date formats). Missing Rounds offer a `rounds.csv` template, with Round types and the `co_investors` format. A record-details block at the bottom of the left column shows website, Fund, Highlight, Exit, logo and Logo origin with its source, and `researched_on`, so every field in the data model is visible.

**Blocked by:** 03 (Founders, markets, accelerators and Rounds).

**Status:** resolved

- [x] Every missing field has a template with correct format and allowed values
- [x] A copied line pasted into the right CSV passes `python scripts/check_data.py` once the value is filled
- [x] Record details show every company-level column, with placeholders where empty
- [x] Page stays read-only; no in-tool feedback box
