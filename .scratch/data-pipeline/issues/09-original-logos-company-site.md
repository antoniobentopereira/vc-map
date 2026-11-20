# 09: Original logos from company sites, with recorded origin

**What to build:** Replace the Norte-recolored logos with Original logos (see GLOSSARY and ADR 0004). `companies.csv` gains `logo_origin` and `logo_source`. The logo script stops using the portfolio page for logos and finds logos only on each company's own homepage. All 130 legacy logos are replaced. Companies with no usable logo end up with an empty `logo` and appear on a manual-follow-up report. This supersedes the "portfolio page first" order in ticket 02.

**Blocked by:** 02 (Logos), 03 (Check script).

**Status:** resolved

**Implemented in commit 684cde2.** Resolved on 2026-11-18 after the owner's visual review.

**Outcome:** the homepage pass found 84 company-site logos. In review, the owner rejected six (Deco, Gabriel, Trybe, Neofin, Osana Salud, Super) as too small or low resolution, and all 52 empty rows were then filled by hand with `logo_origin=manual` and the source URL. All 130 companies now have a logo. Super was renamed Attach Media Partners after a rebrand. Glue keeps its Norte portfolio logo as a documented exception (ADR 0004, `NORTE_LOGO_EXCEPTIONS` in `scripts/check_data.py`).

**Code review of 684cde2 (Standards + Spec):** no documented-standard violations; all five acceptance boxes met in substance. Findings left open, none blocking:
- The "no logo" rule and the column list are duplicated across `check_data.py`, `fetch_logos.py` and `build_roster.py`; origin strings are bare literals. Candidate for a shared constant.
- `fetch_logos.py` retries every empty-logo row on each run (46 today), so a re-run is not literally a no-op while rows are unresolved. Likely intended; the spec does not say whether empty rows count as resolved.
- Only the exact content types `image/svg+xml` and `image/png` are accepted, so sites serving SVG as `text/plain` or `application/octet-stream` are skipped. This may account for some of the 46 missing logos.
- No banner or aspect-ratio filter, though the spec says "never banners". A wide PNG in a header could be accepted.

**Rules**
- Usable logo: SVG, or PNG at least 128 px; clearly the right company, in its own colors.
- Homepage candidates, in order: a header `<img>` whose class, alt or src contains "logo"; an SVG icon link; an `apple-touch-icon`. Never `og:image`, `.ico`, tiny favicons or banners.
- `logo_origin` is `company-site`, `web-search` or `manual`. `logo_source` is the URL the file was downloaded from (for `manual`, the page it was taken from).
- Re-runs keep `manual` and `web-search` rows; they keep `company-site` rows unless the file is missing.
- A logo with no `logo_origin` is legacy (Norte-derived): re-fetch it, and if nothing usable is found delete the old file from `site/logos/` and clear `logo`, `logo_origin` and `logo_source`. All 130 current logos are legacy; none were hand-added.
- The Norte logos stay available in git history (commit 44e3f3b) for ticket 10; no copy stays in the working tree.
- The check script: an empty `logo` is valid and listed for manual follow-up; a set `logo` needs a valid `logo_origin` and a valid-URL `logo_source`; `logo_source` on a `norte.ventures` domain is an error; an empty `logo` with leftover origin or source is an error.
- The report lists, per company, the origin of its logo, and separately every company still without a logo.

- [x] `companies.csv` has `logo_origin` and `logo_source`; `check_data.py` enforces the rules above, each caught by a deliberate-mistake sample
- [x] The script no longer reads logos from the portfolio page
- [x] No legacy Norte logo remains in `site/logos/` or in the CSV
- [x] Every remaining logo has a valid origin and source; the manual-follow-up report lists the rest
- [x] Re-running the script changes nothing when all rows are already resolved
