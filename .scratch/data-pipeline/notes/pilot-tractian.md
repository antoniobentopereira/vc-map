# Pilot notes: Tractian (company 1 of 10)

Researched with web search plus page fetches. 11 claims in `data/claims.csv`; `python scripts/check_data.py` passes.

## What worked
- The company's own Series D post and About page gave description, sector and location.
- Brazilian startup press (startupi, startups.com.br) gave the Feb 2021 pre-seed: size, investors, founders.

## Gaps and conflicts
- **Year founded**: only one passing mention (2019, a Spanish-language column). No company page states it. Medium confidence.
- **Founders**: sources disagree. Startupi: Marinelli + Lameirinhas. Emprendedor: Vieira + Marinelli. Company pages say "Gabriel Lima". Recorded all three, one row each; owner should confirm.
- **Round size**: pre-seed is R$2M in startupi but US$500k in an aggregator. Used the press figure.
- **Several Investments**: Norte invested in pre-seed 2021, seed 2021, Series B 2023, Series C 2024 and Series D 2026. The claims table has no "which investment" column, so only the first Investment is recorded (investment_year, round_size, co_investors) and the follow-ons are in the note. Decision needed for scale-up (Glossary says a company can have several Investments).
- Multi-value fields (co_investors) are one row with values joined by "; ".
- Missing data has no row (the check script requires value and source), so gaps live in this file only.
- Seedtable and the company's seed blog post were blocked (403/404); aggregators were not used as sources.

## Status
Awaiting owner review (ticket 05, third box).
