# 10: Original logos: search-assisted pass for the leftovers

**What to build:** For every company still without a logo after ticket 09, an agent looks for a credible Original logo using web search as a discovery step only (see ADR 0004). Each kept logo is downloaded into `site/logos/` and recorded in `companies.csv` with `logo_origin=web-search` and `logo_source` set to the URL it was downloaded from. Companies with no credible logo stay empty and on the manual-follow-up report.

**Blocked by:** 09 (Original logos from company sites).

**Status:** wontfix (obsolete)

**Why obsolete (2026-11-18):** this ticket covered only companies still without a logo after ticket 09. The owner found logos for all 52 by hand, recorded as `logo_origin=manual`, so no company is left without a logo and no search-assisted pass is needed. The `web-search` origin stays valid in `check_data.py` in case it is wanted later.

**Rules**
- No search API, no scraping of image-search results, nothing scripted. Search only finds a page; the agent fetches the image from that page.
- The agent opens each candidate image and confirms: right company, original colors, not a banner, not watermarked, SVG or PNG at least 128 px.
- Source preference: the company's own other pages (press kit, blog, app listing), then public brand repositories, then other sources.
- A cheap sub-agent compares each candidate with the old Norte logo as a sanity check (same company?). The Norte logos are extracted from git history (commit 44e3f3b) into the scratchpad folder, outside `site/` and uncommitted, and discarded afterwards. A Norte logo is never kept or used as a fallback.
- Re-runs of the logo script keep these `web-search` rows.

- [x] Every company that had no logo after ticket 09 is either resolved with a `web-search` logo or listed for manual follow-up
- [x] Every new logo has `logo_origin=web-search` and a `logo_source` URL; `check_data.py` passes
- [x] No Norte logo is in `site/logos/` or the CSV
- [x] The final manual-follow-up list is handed to the owner
