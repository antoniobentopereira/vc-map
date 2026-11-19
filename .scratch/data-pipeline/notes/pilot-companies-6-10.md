# Pilot notes: Carbonext, Kolors, Norma, Stay, Palomma (companies 6 to 10 of 10)

Researched one at a time on 2026-11-19. `python scripts/check_data.py` passed after each company.

## New things learned

- **Batch proposals were guesses from names.** Stay is a corporate-pensions fintech, not hospitality; Norma is tax intelligence, not general compliance; Palomma is Colombian (Medellín), not Mexican; Kolors has moved from intercity buses to employee transport. Sub-sectors were set from sources.
- **Norte is named in later Rounds only.** Stay (2026 Series A) and Palomma (2026 Series A, as a "returning investor") name Norte; every earlier Round names no one for Norte, so they are FALSE at low or medium Confidence. Carbonext and Kolors have no press naming Norte anywhere; only aggregators (VC Backed, CB Insights) list it, so all their Rounds are FALSE/low and no first investment can be derived. The open `unknown` question for `norte_participated` now affects 4 of 10 companies.
- **"Total funding" headlines vs the Round.** Kolors (US$26M total, US$20M Series A) and Palomma (US$14M total including US$4M undisclosed, US$10M Series A) headline totals. The Round row uses the Round figure; the rest goes in the note.
- **Aggregators disagree on type and currency.** Carbonext's 2022 Round is R$200M (press) or US$40M (Reuters); type `series_b` comes only from VC Backed. Stay's 2026 USD figures disagree inside one Dealroom article, so BRL was kept.
- **2026 BRL average not published**, so Stay's 2026 Round has `size_usd` empty (as with Tractian's BNDES debt).
- **Seed Rounds with a year but no amount** (Carbonext 2021 angels, Kolors 2020) get a row with empty size fields; the lead is often unnamed.
- Sub-sectors added: Forest carbon credit development, Bus and employee transport platform, Tax intelligence, Corporate pensions and employee benefits, Real estate rent payments and AI.

## Sources that worked

- Company sites (About pages, product pages) for description, HQ and founders: Carbonext, Stay, Norma, Palomma.
- Brazilian press (Brazil Journal, startups.com.br, Times Brasil), Reuters via Notícias Agrícolas; TechCrunch, PR Newswire and Alumni Ventures' blog for Kolors; Forbes Colombia and Ecosistema Startup for Palomma; Y Combinator profile for Palomma's batch and founding year.
- Dealroom news for Stay's round type. Fund pages (norte.ventures/portfolio) only list the company and fund, nothing more.

## Missing or uncertain

- **Norma**: almost no public coverage. No founders ("founded by engineers and tax specialists"), no founding year, no Rounds, no accelerator; HQ is only the footer's registered address (estimated, low). Norte's participation is unknown; no Rounds found.
- **Carbonext**: no source names Norte; Series A and seed investors only partly named. HQ at first investment assumed. Status relies on a Carbon Pulse piece that could not be read (403); its 2025 date is inferred.
- **Kolors**: year founded (2020) is the company's own; date of the shift to employee transport not found; no accelerator found; Norte not named anywhere in press.
- **Stay**: Caio Elias is a founder in 2024 coverage but only CTO in 2026; kept at medium Confidence. Accelerator none found.
- **Palomma**: the US$4M pre-Series A has no year or investors; Norte's first (earlier) investment is not described anywhere.
- Unreadable: CB Insights and Carbon Pulse (403), fusoesaquisicoes (403).

## Effort

About 8 to 12 page reads per company; Norma needed 5 searches and still yielded only its own site. A thin company costs about as much as a documented one, because the empty searches are the cost.
