# Pilot notes: Jota, tapi, idwall, Legiti (companies 2 to 5 of 10)

Researched one at a time on 2026-11-18, in the revised data model. `python scripts/check_data.py` passed after each company.

## New things learned

- **Norte is often not named in later Rounds.** tapi has no Source naming Norte in any Round (it is in Fund I per norte.ventures/portfolio), so all three Rounds are FALSE with low Confidence and the first investment cannot be derived. The question of an explicit `unknown` in `norte_participated` (open since Tractian) is now more pressing.
- **Where the first Norte round hides.** idwall: Norte first appears in the 2021 Series C (Finsiders lists earlier investors separately, and Norte is not among them). Jota: the 2025 seed. Legiti: the 2020 seed.
- **Pre-seed and seed rounds with no year or size** (idwall's seed from 500 Startups, Jota's pre-seed, tapi's Tap-wallet round) are mentioned in passing. They get no row (a Round needs a year) and are noted in the nearest Round's note.
- **Sub-sectors** added: Conversational business banking, Payments infrastructure, Identity verification and fraud prevention, Fraud prevention for e-commerce. The last two are close; merge when Sectors are assigned.
- **Acquisition vs team hire**: Legiti's 2023 deal with Signifyd is announced as hiring the team, not buying the company, so no acquirer is recorded and Status is `inactive`. legiti.com now redirects to a domain-for-sale page.
- **Exits that keep operating**: idwall was acquired by Serasa Experian (completed 2026-07-01) and stays `active` with medium Confidence, since no Source says the brand is retired.
- **Currency**: tapi and Jota report in USD, so no new FX needed; BRL rates for 2021 and 2022 already existed. Press conflicts on size are common (R$60M vs US$8.9M for Jota; R$40M vs US$10M for idwall's 2019 round); the original announcement's currency was preferred.

## Sources that worked

- Brazilian press again for BRL rounds (startups.com.br, Brazil Journal, Baguete, Canaltech, Finsiders).
- LatamFintech and Forbes Argentina for tapi (Series A and B, the founder story); Bloomberg Línea for the Series A.
- LAVCA for idwall's 2018 Series A; Crunchbase News for the 2019 Series B (WebFetch worked on it).
- Serasa Experian's press room for the idwall acquisition. Kaszek's company page for Legiti.

## Missing or uncertain

- **Jota**: HQ and HQ at first investment not found (press says only "cearense" and São Paulo from aggregators). Its Series A has Norte FALSE at medium Confidence; an aggregator lists Norte. Tiago Guilhon is on jota.ai's founding team but is not confirmed as a Founder in press, so he is left out.
- **tapi**: no source for Norte's participation anywhere; accelerator none found.
- **idwall**: no recent HQ source (2019 Crunchbase News used, Estimated). Accelerator "500 Startups" recorded as Estimated, low, because the Source may mean an investment only.
- **Legiti**: round type of the 2022 R$42M round not stated anywhere (`unknown`); Norte not named in it. Sources not readable: El Referente (403), Business Wire (403).
- Everything about idwall's and Legiti's customers beyond what is in the Claims was not pursued.

## Effort

Roughly 15 to 20 page reads each. Searching with WebSearch first and then fetching 3 to 5 articles per company was enough; the hard part is Norte's participation, not the facts.
