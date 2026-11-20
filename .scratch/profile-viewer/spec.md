# Spec: Company profile viewer (internal review tool)

**Status:** ready-for-agent

## Problem Statement

I am collecting the Dataset by hand and reviewing the Pilot personally. Checking what we know about one Portfolio company means reading raw rows across `claims.csv`, `rounds.csv`, `companies.csv` and `sectors.csv`, which is slow and hides what is missing. I want one tidy profile page per company so I can review the research, give feedback, and fill gaps by hand.

## Solution

A local, read-only **profile viewer**: a single page where I pick a researched Portfolio company from a searchable list and see its full profile. Every field in `docs/data-model.md` is always shown in a fixed position. A field with no data appears as a clearly marked red placeholder that says why it is empty and what row to add. Each value shows its Basis, Confidence and a small "source" button, and uncertain values look different from reported ones. A completeness indicator summarises how much of the profile is filled.

This is a throwaway internal tool for data collection and checking. It is not the Visualization (stage 4), not a preview of the final site's design, and ships nothing. Whether stage 4 reuses any of it (for example the code that assembles a profile from the CSVs) is decided later.

## User Stories

1. As the owner reviewing the Pilot, I want to pick a company from a searchable dropdown, so that I can open its profile without scrolling a CSV.
2. As the owner, I want the dropdown to list only companies that have at least one row in `claims.csv` or `rounds.csv` (plus any with `researched_on` set), so that I am not wading through 130 empty profiles.
3. As the owner, I want the chosen company kept in the page address, so that a refresh or a bookmark returns me to the same profile.
4. As the owner, I want previous and next buttons that step through the picker's list in roster order, so that I can review company after company.
5. As the owner, I want to see the company's logo and name at the top, so that I know I am looking at the right company.
6. As the owner, I want a placeholder in the logo spot when a company has no logo, so that the layout never shifts.
7. As the owner, I want the Status shown as a tag next to the name, so that I see at a glance whether the company is operating.
8. As the owner, I want the short description in serif italic under the header, so that I get the one-line picture first.
9. As the owner, I want a Facts box in a fixed order (Sub-sector and Sector, Status, business model, year founded, HQ now, HQ at first investment, acquirer, acquisition year), so that general facts come first and a gap is always in the same place.
10. As the owner, I want the long description below the Facts, so that I read detail after the overview.
11. As the owner, I want a History timeline anchored on years that merges Milestones and Rounds chronologically, so that I understand the company's story visually.
12. As the owner, I want Rounds styled differently from Milestones on the timeline, so that funding events stand out.
13. As the owner, I want month- and day-dated Milestones to sort before year-only items within a year, so that the order is predictable.
14. As the owner, I want record details at the bottom (website, Fund, Highlight, Exit, logo, Logo origin and its source, `researched_on`), so that every field in the data model is visible.
15. As the owner, I want Founders, markets and accelerators as stacks of small boxes in the right column, so that list fields are easy to scan.
16. As the owner, I want an Investment Rounds table with type, year, size in USD and whether Norte took part, so that I can read the funding history quickly.
17. As the owner, I want a second line per Round with the reported amount, currency and co-investors, so that I can check the USD conversion and who else invested.
18. As the owner, I want a summary line above the Rounds table showing the first investment, last round and follow-on, so that the derived views are visible, computed by the existing derive logic.
19. As the owner, I want a field that is missing from a researched company to show a red "NOT FOUND" placeholder with the research date, so that I know it was looked for and nothing public turned up.
20. As the owner, I want a field of a company with empty `researched_on` to show a red-outlined "NOT RESEARCHED" placeholder and a banner on the profile, so that I never mistake an unresearched gap for a finding.
21. As the owner, I want the acquirer and acquisition-year placeholders to read "none recorded (not acquired, or not found)", so that a normal absence is not presented as a failure.
22. As the owner, I want estimated or low-confidence values to have a dashed amber border, an "EST" or "LOW" tag and the note visible, so that guesses never pass as reported facts (ADR 0003).
23. As the owner, I want a small confidence dot beside every value with a Confidence (green high, yellow medium, red low), so that I read certainty at a glance.
24. As the owner, I want medium Confidence to count as certain enough (dot only, no uncertain styling), so that the uncertain styling stays meaningful.
25. As the owner, I want every value to show its Basis, and its note when present, so that I can verify the reasoning.
26. As the owner, I want a small "source" button on each value that reveals the link, with Open (new tab) and Copy, so that I can verify a Source without full URLs cluttering the page.
27. As the owner, I want a completeness indicator such as "11 / 13 filled, 2 uncertain, 2 not found", so that I can compare companies.
28. As the owner, I want acquisition fields excluded from the completeness count, so that a company that was never acquired is not penalised.
29. As the owner, I want a flag when no Norte Round is recorded, so that I notice a missing first investment.
30. As the owner, I want a legend in the header explaining the dots and tags, so that I do not have to remember them.
31. As the owner, I want any data errors from the check script for the selected company shown as a banner, so that I see rule violations while reviewing.
32. As the owner, I want each missing field to offer a collapsed "How to add this" with the exact CSV line pre-filled (company name, field name), so that I can add the row myself.
33. As the owner, I want the expected format and allowed values next to that line (City, Country; `b2b`/`b2c`/`b2b2c`; the Sub-sector list from `sectors.csv`; the Status table; Round types; date formats), so that I enter valid data first time.
34. As the owner, I want a copy button on the row template, so that I can paste it straight into the CSV.
35. As the owner, I want missing Rounds to offer a `rounds.csv` template the same way, so that I can fill funding gaps.
36. As the owner, I want the page to be read-only, so that I can never damage the CSVs from it; feedback happens by editing the `note` column or telling the agent.
37. As the owner, I want to regenerate the page's data with one documented command after editing a CSV, so that I never forget how.
38. As the owner, I want to open the page by double-click with no server or build step, so that it stays cheap.

## Implementation Decisions

- **Placement:** a top-level `tools/profile-viewer/` outside `site/`, so it never ships with the Visualization (ADR 0001). It reads logos from `site/logos/` read-only and writes nothing to `site/` or `data/`.
- **Data flow:** a generator script (Python standard library only) reads the CSVs and writes one generated data file that the page loads as a script, because browsers cannot fetch CSVs from a `file://` page. The generated file is gitignored and disposable; it is not a source of truth, so ADR 0002 (CSVs are the single source) stands.
- **Reuse, not duplication:** the generator imports the existing Round derivations (first investment, last round, follow-on) and the data check, so there is one definition of each. The check's findings for the company are attached to its profile.
- **Front end:** HTML, CSS and vanilla JS only. No frameworks, no build tooling.
- **Picker rule:** a company is listed if it has at least one Claim or Round row, or `researched_on` set. Roster order. Selection stored in the URL hash.
- **Field states** (single classification, applied to every field slot):
  - reported: Basis `reported`, Confidence medium or high.
  - uncertain: Basis `estimated` or Confidence `low`.
  - not found: `researched_on` set and no row.
  - not researched: `researched_on` empty and no row (rows that exist are still shown).
  - acquirer and acquisition year use their own "none recorded" wording for the empty case.
- **Visual language:** red-bordered tagged placeholders for missing values; dashed amber for uncertain; confidence dot (green, yellow, red) beside any value with a Confidence. Red for missing and red for low-confidence coexist deliberately (decided with the owner).
- **Completeness:** counts the 8 single-value fields excluding the two acquisition fields, the 4 list fields (filled if at least one row) and Rounds (filled if at least one row), plus a separate uncertain count and a not-found count; a "no Norte round" flag. Acquisition fields are shown but not counted. (Exact denominators to be fixed by the implementer from `data-model.md`; the owner's example is illustrative.)
- **Layout (general first, detail below):**
  - Header strip: logo, name and Status tag, search with previous and next, completeness, legend.
  - Left column: short description, Facts box, long description, History timeline, record details.
  - Right column: Founders, Investment Rounds (summary line, then table), markets, accelerators.
  - The owner's rough PNG mockup is a loose reference for mood and arrangement only (off-white background, thin dark borders, serif italic short description, small uppercase labels). None of its placeholder text is used.
- **History timeline:** chronological, year-anchored; Milestones come from Claims, Rounds from `rounds.csv`; partial dates (`2021`, `2021-03`, `2021-03-19`) sort with dated items before year-only items within a year; Rounds have a year only.
- **Source detail:** under each value, Basis tag, confidence dot, note when present and a small "source" button revealing the link (Open in new tab, Copy). No raw URLs in the page body.
- **Gap filling:** per missing field a collapsed "How to add this" with a pre-filled CSV line, a copy button, the expected format and allowed values taken from `data-model.md` and `sectors.csv`. No in-tool feedback.
- **Docs to write alongside:** ADR 0008 (the viewer is disposable, outside `site/`, its generated file is not a source of truth) and a short README in the viewer folder with the regenerate command and how to open the page. No new Glossary term; the viewer is never called a "dashboard" or "app" and is distinct from the Visualization.
- **ADR check:** no conflict with ADR 0001 (viewer outside `site/`), ADR 0002 (CSVs stay the source; generated file is a derivative), ADR 0003 (Estimated values always visibly different) or ADR 0007 (one value per field; the viewer shows the kept value and its note with discarded values).

## Testing Decisions

- The owner decided: no automated tests and no new seams for this tool. It is a throwaway helper; correctness is checked by running the generator and opening the page against a few real companies (for example Tractian, which is fully researched) and an unresearched or thin one.
- Existing seams are untouched, and `docs/agents/testing.md` is not changed. The existing pre-commit hook (`unittest` plus `check_data.py`) keeps running as before.
- A good manual check covers each state: a reported value, an estimated value, a low-confidence value, a not-found field, a not-researched company, a company with no Norte Round, and a company with no logo.

## Out of Scope

- Stage 4 (Visualization v1), its design, or reuse of the viewer as the site; shipping anything.
- Editing data from the page, saving feedback in the tool, or writing to `data/` or `site/`.
- Automated tests, polish, responsive or mobile design, accessibility audits, filters or sorting beyond the picker.
- Showing companies with no Claim, Round or `researched_on`.
- Assigning Sectors or changing the data model.

## Further Notes

- Rerun command (to go in the README): `python tools/profile-viewer/build_data.py`, then open `tools/profile-viewer/index.html`.
- The Glossary's "Visualization" entry says to avoid "dashboard" and "app"; the viewer deliberately avoids both.
- ADR 0002 still describes "two tables" while the Dataset now has five CSV files (ADR 0005 added Rounds and `data-model.md` lists them). That staleness is not caused by this tool, but is worth tidying separately.
