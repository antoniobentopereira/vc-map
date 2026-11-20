# Story pass: the 13 already-researched companies (2026-11-20)

Goal: bring every company with `researched_on` through the later changes (ADR 0012 and 0013): rewrite `long_description`, add `investment_thesis`, add the missing milestones. Other rows were kept. One company at a time, no sub-agents; `python scripts/check_data.py` passed after each; unit tests pass (107).

Method per company: 3 to 6 page reads of primary pages (company site, the Round article, interviews) plus 1 to 2 searches aimed at market size. Page text was fetched with a small script and read in full; search summaries were used only to find pages, except where a note says a figure is relayed. `researched_on` unchanged.

New milestones were added only when a dated source stated them. Where the existing and new sources conflicted (Jota's FalaTap: May per Brazil Journal, Q1 per Startups.com.br), the old month-level milestone was replaced by a year-only one and the note says why.

## Per company

| Company | Long description (chars) | Thesis (chars) | Milestones now | Linked API | Main gaps |
|---|---|---|---|---|---|
| NG.CASH | 2121 | 2502 | 9 | none | Trampolin/Stone sale only from a search summary; market is our arithmetic (IBGE 20-24 figure from a snippet, not opened) |
| CredAluga | 2225 | 2670 | 6 | none | R$36bn guarantee market is a company/press estimate; 2025 modular launch dropped (no date) |
| Flieber | 1966 | 2550 | 2 | none | Nothing public since the 2021 round; competitors and market are assumptions |
| Carbonext | 2247 | 2406 | 5 | none | No price/yield source for REDD+; NaturAll stake undated; Norte never named |
| Tractian | 2471 | 2716 | 9 | none | Siemens and Deloitte figures read only as quoted in Tractian's own post |
| Jota | 2444 | 2608 | 6 | none | FalaTap month conflicts between two articles |
| Stay | 2379 | 2731 | 3 | none | Contribution and fee assumptions; Caio Elias founder status unclear |
| tapi | 2517 | 2695 | 5 | none | No independent market size; take rate assumed |
| Norma | 2414 | 2450 | 2 | 1 workflow: `wf-81a578fe-b655-47f5-bb88-ec181f8d3f24` (company page + 20 posts, 2026-11-20, exit 0) | No rounds, no coverage beyond its own site and posts; a namesake legaltech named Norma shows up in startups.com.br and was not used; the posts output was cut at 9,000 characters, so only the newest posts were read |
| idwall | 2243 | 2486 | 6 | none | Sale price (R$400 to 450M) from unnamed sources; 2018 Series A milestone dropped (page did not state the year) |
| Kolors | 2211 | 2423 | 4 | none | No funding or revenue facts after 2022; date of the shift to staff transport not found; the 2022 Series A is UNKNOWN for Norte |
| Legiti | 2125 | 2394 | 5 | none | Competitors not named in sources; market arithmetic overstated on purpose and flagged |
| Palomma | 2183 | 2700 | 3 | none | Pivot date not stated; market figures are the company's, relayed by Forbes Colombia |

Norte counts (Rounds, unchanged by this pass): TRUE 12, FALSE 5, UNKNOWN 18 across the 13 companies.

## What the pass taught

- Thesis confidence ended `low` for 9 of 13 and `medium` for 4 (CredAluga, Jota, Tractian, Palomma): a read, non-company market figure was only available for those. Market size is the usual weak link, as the recipe predicted.
- Several articles that name Norte (Jota's seed, CredAluga's seed and Series A, Stay's Series A, Legiti's 2020 seed, Palomma's returning investors) were already reflected in `rounds.csv`; Palomma's Forbes piece implies an earlier Norte round with no description.
- The Startups.com.br "related news" box can name a different company with the same name (Norma). Check the page before using it.
- Cost: about 5 to 8 page reads per company for the story and thesis, about 1 search for market size.
