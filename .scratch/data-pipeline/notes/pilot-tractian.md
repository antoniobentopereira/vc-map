# Pilot notes: Tractian (company 1 of 10)

Researched 2026-11-18, then redone in the revised data model (`docs/data-model.md`) after the owner's first review. 21 Claims and 7 Rounds; `python scripts/check_data.py` passes.

## Sources that worked

- **Company pages**: About page (description, sub-sector) and the Series C and Series D announcements (HQ, investors).
- **Y Combinator profile**: founding year, batch, current HQ. A good primary source for any YC company.
- **Brazilian press** (startupi, startups.com.br, InfoMoney, IT Forum, Brazil Journal): one article per Round, with size, lead and investors. Usually the only place a BRL figure appears.
- **Norte's case post** (norte.ventures/content/tractian-brio): good for the early story (pivot to hardware, how the founders met, Norte's first check during YC), but undated and promotional. Used only for the pivot milestone (Estimated, since the year is deduced) and as background.
- **BCB SGS series 3694** (annual average PTAX) for BRL rates, from a direct JSON link.

## Missing or uncertain

- **HQ at first investment**: no 2021 source names a city. Recorded as São Paulo, Estimated, low Confidence (founders from the University of São Paulo, no US office until 2022).
- **Norte in the Series A (2022) and Series C (2024)**: not named in the announcements, so recorded as FALSE. For the Series C an aggregator lists Norte, so that row has low Confidence. A yes/no column cannot say "unknown"; see the open question below.
- **BNDES debt (2026, R$120.1M)**: the 2026 annual BRL average is not published yet, so the reported amount is kept and `size_usd` is empty until it is.
- **Investor names**: the Series D post writes "N47" and "Catalyst"; normalised to Next47 and M&G Catalyst so the same investor matches across Rounds.
- **Founders**: 2021 articles name two; Brazil Journal (2026) and the Norte post name three. Recorded all three.
- **Year founded**: settled at 2019 (YC profile, Brazil Journal, InfoMoney).
- Seedtable returned 403 and one Tractian blog post returned 404; aggregators were not used as Sources.

## Open questions for the owner

- `norte_participated` is TRUE or FALSE. "Norte not named anywhere" is recorded as FALSE with a lower Confidence. Should there be an explicit `unknown`?
- Milestones exclude funding events, which come from the Rounds instead. Confirm this split for the timeline.

## Effort

Roughly 20 page reads for one well-documented company, most of them for the Rounds. Expect fewer for thin companies, but more searching per fact.
