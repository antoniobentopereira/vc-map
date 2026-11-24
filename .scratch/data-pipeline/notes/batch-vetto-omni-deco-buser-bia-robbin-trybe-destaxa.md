# Batch 4 (2026-11-24): Vetto, Omni Saúde, deco, Buser, Bia, Robbin, Trybe, Destaxa

Eight companies, in file order, one at a time. Norte's Manifesto re-read 2026-11-24 (unchanged in substance). `python scripts/check_data.py` passes and `python -m unittest discover -s tests` passes (107 tests). Tools: plain page reads (`curl --compressed` and a text extractor), web search, minhareceita.org for the registry (BrasilAPI URL cited), Linked API for 8 workflows in total.

## Norte counts (rounds written)

| Company | TRUE | FALSE | UNKNOWN | Rounds |
|---|---|---|---|---|
| Vetto | 1 | 0 | 1 | 2 |
| Omni Saúde | 1 | 1 | 3 | 5 |
| deco | 0 | 1 | 1 | 2 |
| Buser | 0 | 4 | 1 | 5 |
| Bia | 0 | 1 | 3 | 4 |
| Robbin | 1 | 0 | 0 | 1 |
| Trybe | 1 | 2 | 2 | 5 (one is debt) |
| Destaxa | 1 | 1 | 0 | 2 |

Three companies (deco, Buser, Bia) have no Round with Norte `TRUE`: aggregators list Norte as an investor, but no article names it in any Round. This is the main gap of the Batch.

## Vetto (formerly Start Carreiras)

- **Reads:** vetto.ai home, /talent, careers, research pages; Baguete (seed R$13M, 2025-04-14); Bloomberg Linea (two pieces, 2025-04); Startups.com.br (2024-08 repositioning; 2026-01-29 CTO hire; tag page for Lucas Smaira); Sacra Scale AI page (market comparable).
- **Linked API:** `search-companies "Vetto"` wf-62f0ac61-2549-4df4-b9c1-befc79d3beca (found "Vetto AI", San Francisco; used for HQ, medium).
- **Fields filled:** description, long description, thesis, sub-sector (new: AI training data and model evaluation), HQ, HQ at first investment, year, status, model, 3 founders, market, 6 milestones.
- **Rounds:** 2023 pre-seed R$7M (Maya lead; Reach, Graphene; Norte UNKNOWN: Bloomberg says Norte was in the cap table before 2025), 2025 seed R$13M (Norte TRUE, Baguete and Bloomberg).
- **Gaps:** date of the rename Start Carreiras to Vetto; CNPJ; Series A/other rounds after the pivot; customers and revenue after the pivot; month of Lucas Smaira's hire. Rodrigo Schmidt is not a Founder (joined January 2026, called co-founder by the press: the data-model rule makes him a leadership hire, so left as a Milestone).
- **Leads not used:** PitchBook and Dealroom entries (US$2.25M seed, São Paulo HQ, São José dos Campos HQ), an aggregator's December 2023 date for the R$7M round, and a LinkedIn-derived "Start Carreiras role until January 2026" date for the rename.

## Omni Saúde

- **Reads:** omnisaude.app home and privacy policy (legal name, CNPJ 48.979.674/0001-06); minhareceita (opened 2022-12-26; Fernando Domingues 2022-12-26, Leopoldo Veras 2023-05-12); Startups.com.br (seed 2023-06-29, third round 2024-08-08, Wayra 2025-05-29); Saúde Business; Brazil Journal (2026-11-03, ACNext round); Portal Tela (2026-05); Central do Varejo (IQVIA market).
- **Linked API:** `search-companies "Omni Saúde"` wf-6ac6b60a-2c5b-4463-beec-d570006d5ba5 (São Paulo; HQ already known from the site).
- **Rounds:** seed 2023 R$5M (VEC lead); 2024 Greenrock R$10M; Aug 2024 Norte round (TRUE; amount undisclosed, about R$1M by our arithmetic); 2025 Enseada + Wayra (US$1M); 2026 ACNext (Norte not listed, FALSE medium).
- **Gaps:** round types (only the seed is typed); the amounts of the Norte, Enseada and ACNext cheques; the number of rounds (Portal Tela says five and R$25M, Brazil Journal three and R$30M, our list has five).

## deco (deco.cx, decocms.com)

- **Reads:** decocms.com home and VTEX Day 2026 post; Baguete, Bloomberg Linea and Brazil Journal (2024-01); Baguete SuperFrete (2026-05-13); ABComm via Mercado&Consumo.
- **Unreadable:** Exame (Web Summit Rio 2024 winner) returned compressed bytes with my plain fetch; with `curl --compressed` it works for other Exame pages but this article was not retried, so the award is not recorded.
- **Linked API:** `search-companies "deco cx"` wf-df75e3ee-371a-4751-8724-605ecfe0687f returned `[]`; `search-posts "deco" --mentioning "Norte Ventures"` wf-3c80101c-4f44-4871-bdb4-2a1c1cdde45c returned `[]`.
- **Rounds:** 2022 angel US$600k (only individuals per Bloomberg: Norte FALSE), 2024 seed US$2.2M (Maya lead; FJ Labs, Lanx, Crivo; Norte UNKNOWN because a search summary says CB Insights lists Norte).
- **Gaps:** where and when Norte invested; CNPJ and registered seat (not on the site); HQ is only "carioca" in 2024 press; current revenue; date of the pivot to operating stores for results; any round after 2024.

## Buser

- **Reads:** buser.com.br/sobre (story, CNPJ 29.365.880/0001-81); Exame (2019-10-07 Series B, 2022-04-26) and Startupi (2021-06 Series C), both read only with `curl --compressed`; Startups.com.br (2025 4Equity); NeoFeed (2026-11-03); Valor Capital's post; Moon BH (2026-10-18); minhareceita (seat São Paulo, opened 2018-01-05, Buser LLC partner).
- **Linked API:** `search-posts "Buser" --mentioning "Norte Ventures"` wf-c36a4f4c-53cc-4221-80e8-5d209ad5a193 returned `[]`.
- **Rounds:** seed 2018 and Series A 2018 and Series B 2019 (amounts undisclosed; FALSE), Series C 2021 R$700M (investor list partly from search summaries, FALSE medium), 2025 media-for-equity R$30M (UNKNOWN).
- **Gaps:** where Norte invested (Fund I); a possible 2020 extension; round amounts for A and B; exact date of Series A and B (aggregators say 2019 and 2020); Series C participants beyond the lead (Forbes and LAVCA pages not read). Layoff and airline-ticket headlines seen only in search results (not used).

## Bia (Colombia)

- **Reads:** bia.app (Spanish home); LatamList 2022-07-27 (pre-seed); Ecosistema Startup 2023-10-12 (Series A) and 2026-08-25 (US$18.5M); Forbes Colombia 2024-11-26 and Portafolio 2024-12 (bridge); Kaszek page.
- **Linked API:** `search-posts "Bia Energy" --mentioning "Norte Ventures"` wf-44f8388c-8bf5-4cb2-89cc-d28dd43011ac returned one Palomma event post that tags both Bia and Norte (not a round post); `search-companies "Bia Energy"` wf-1b3404cf-20a5-41dd-8c57-d2efe1ee411a (Bogotá D.C.).
- **Rounds:** 2022 pre-seed US$6M (FALSE: full list with angels), Series A 2023 US$16.5M, 2024 bridge US$8.5M (typed series_a), 2026 US$18.5M (type unknown). Norte UNKNOWN in the last three.
- **Gaps:** Norte's round (aggregators and an event post link it to Bia); the type of the 2026 round (Series B not stated); legal name and registry (Colombian registry untried); Guillermo Plaza's role in 2026 (only two founders named).

## Robbin

- **Reads:** robbin.com.br; Startups.com.br, Brazil Journal, Finsiders and Startupi on the 2026-05 seed. Let's Money returned 403.
- **Linked API:** `search-companies "Robbin"` wf-8dcf7360-c7ba-4b57-89f3-7787f999996f (São Paulo; name and sector match only).
- **Rounds:** seed 2026 US$8M (Norte TRUE in 4 outlets). The FIDC of US$100M has no row (a credit fund, not Robbin's own round).
- **Gaps:** CNPJ and registry (not on the pages read), founding month, any milestone before 2026 (only "founded in 2023" and "R$200M of credit since inception" are given), market size (no published figure for B2B trade credit in Brazil).

## Trybe

- **Reads:** betrybe.com home, terms of use and privacy policy (CNPJ 34.389.271/0001-00 and Trybe SCD); Contxto (Series A, 2020-02-29); NeoFeed (2021-06-15: seed US$3.7M, Series A extension US$6M, Jungle Devs); Baguete and Forbes (Series B 2021-10-06); Startups.com.br (layoffs 2022 and 2023, 2023-05-31 profile); Convergência Digital (Brasscom); minhareceita (seat Belo Horizonte; opened 2019-08-01; partner Trybe Holding LLC).
- **Linked API:** none used (founders, HQ and Norte were found without it).
- **Rounds:** seed 2019 (FALSE, low), Series A 2020 R$42M (Norte TRUE, Contxto and Baguete), Series A extension 2021 (UNKNOWN), Series B 2021 R$145M (FALSE), FIDC 2021 R$50M (debt, UNKNOWN).
- **Gaps:** date of the seed (before February 2020); when and why the school moved to AI training; current revenue; any round after 2021 (a CB Insights snippet lists a US$30M "Series A" dated 2026-01-12: lead, not used); HQ (registry only: low).

## Destaxa

- **Reads:** destaxa.com.br home and /sobre; Startups.com.br (2023-11-24 round, 2024-06-25 interview); Finsiders (2024-06-24); Finsiders (Abecs 2025 volume). Fintech Futures, IBS Intelligence and Financial IT pages returned unreadable or empty text (seed size US$3.1M stays a lead).
- **Linked API:** `search-companies "Destaxa"` wf-2c042c07-2b71-45ae-aa75-d3da5b5cd334 (São Paulo, SP).
- **Rounds:** 2022 seed R$15M (Norte TRUE in Startups.com.br; the press also writes "Norte Capital"), 2023 R$30M (FALSE medium).
- **Gaps:** CNPJ; seed size (R$15M vs US$5M vs US$3.1M); any news after June 2024 (status `active` is low confidence); the planned Series A; revenue.

## Recipe changes

Added to `docs/research-recipe.md` under "Lessons from Batch 4".
