# Batch: Crown, Newtail, Pier, IORQ, The Coffee, BHub, Stark Bank, Nomad

Researched 2026-11-24, sequentially, no sub-agents. Manifesto re-read (unchanged: obsessed founders, network over geniuses, follower and connector role, no operational involvement). Pages were read with `curl` plus a text stripper and web search; TechCrunch, The Block, Blockworks, VC Backed and Dealroom (app) returned Cloudflare blocks. Unit tests: 107 pass. `check_data.py` passes.

| Company | Rounds | Norte TRUE / FALSE / UNKNOWN | Linked API |
|---|---|---|---|
| Crown | 2 (seed US$8.1M, Series A US$13.5M) | 1 / 0 / 1 | 1 workflow |
| Newtail | 3 (pre-seed 2021, pre-seed 2022, seed 2023; amounts hidden) | 0 / 0 / 3 | 1 workflow |
| Pier | 4 (Series A, Series B, IFC debt, doubtful 2023 Series C) | 0 / 2 / 2 | 1 workflow |
| IORQ | 1 (R$35M Series A) | 1 / 0 / 0 | none needed |
| The Coffee | 3 (seed 2019, Series A 2020, Series B 2022) | 1 / 0 / 2 | none |
| BHub | 5 (pre-seed, Series A, extension, IFC 2024, US$10M 2025) | 1 / 2 / 2 | none |
| Stark Bank | 3 (2020 round, Series A, Series B) | 1 / 0 / 2 | none |
| Nomad | 4 (Series A, May 2022, Series B, Series C) | 0 / 0 / 4 | 1 workflow (see below) |

## Per company

**Crown.** Reads: site (home, A Crown, English), Startups.com.br (seed, Series A), Brazil Journal, Cointelegraph, Money Times, Funds Society (FX desk), Valor (Nexa), Livecoins via CoinStats, Central Bank monetary statistics PDF (June 2026), BrasilAPI (CNPJ 59.386.340/0001-45, opened 2025-02-10). Linked API: `search-posts "Crown BRLV" --mentioning "Norte Ventures"` wf-2ffb291b-d881-4597-b628-b982ff403623, completed, found a post that repeats the Series A and names Norte only in the seed. Norte TRUE in the seed (Startups.com.br, Brazil Journal, Money Times). Gaps: who joined the Series A besides Paradigm (The Block unreadable; Brazil Journal lists the pool across both rounds); founding year (2024 per Brazil Journal, registry 2025); Exame story not found. Observation: Crown's "8% of the monetary base = R$1 trillion" matches M3, not the restricted base (R$427.8bn).

**Newtail.** Reads: newtail.com.br (now VTEX Ads), Brazil Journal, Startupi (twice), Baguete, Meio&Mensagem, Mercado&Consumo, Mobile Time, E-Commerce Brasil (founder bio), Startupi on Latitud, CB Insights financials. Linked API: `search-posts "Newtail" --mentioning "Norte Ventures"` wf-127e9180-5959-4e4c-99b7-3fa5ab2448d7, completed with no posts. Gaps: round amounts, investors and which round Norte joined (VC Backed lists Norte for a Jan 2023 seed, page unreadable); CNPJ not found; HQ city only from aggregators; 2020 vs 2021 founding year; Latitud podcast page 404.

**Pier.** Reads: site, Startups.com.br (Series B, new CEO), Brazil Journal, Finsiders, Startupi (Series A), LatamList, Let's Money, CQCS (Series C plan), IFC project page, CB Insights financials, Dealroom, Susep news, BrasilAPI (CNPJ 39.380.513/0001-00, opened 2020-10-09). Linked API: `search-posts "Pier seguro" --mentioning "Norte Ventures"` wf-2d772d29-de03-448c-b24a-a7029739f276, completed with no posts. Gaps: Norte appears only in Dealroom's "other known investors"; the seed and the two pre-Series A rounds Forbes mentions are undescribed; the CB Insights Series C of US$18.51M (2023-02-16) is unconfirmed and clashes with the 2026 plan for a "Series C"; a Susep ruling of June 2026 on minimum capital turned up in a search summary and was not read.

**IORQ.** Reads: site, Startups.com.br, Bloomberg Línea, Startupi, LexLegal, Foley (page read only as a menu), Trademap (CVM data for the Quatá manager), Intellinews (search summary). Norte named by four outlets. Gaps: the IORQ holding's CNPJ (the one found, 09.456.933/0001-62, is the Quatá manager, opened 2008); HQ address from the manager; no 2026 news beyond the site's own figures; Mais Retorno pages 404.

**The Coffee.** Reads: site, NeoFeed, Startupi, Bloomberg Línea (PT and EN), Brazil Journal, Forbes Brasil (2026), Mercado&Consumo, BrasilAPI (Café Fratelli Franqueadora, opened 2018-09-17). Norte TRUE in the 2020 Series A (NeoFeed, Startupi). Gaps: which round Norte first joined (Brazil Journal: US$5.5M in two rounds with Monashees, Shift, Norte, AirAngels); seed amount conflicts (US$500k Bloomberg vs R$500k NeoFeed); the DF Chile article returned only a menu; Japan and Exame 2026 stories not read.

**BHub.** Reads: site (CNPJ 42.330.545/0001-06), Baguete, Startups.com.br (extension, IFC, US$10M), Brazil Journal, BrasilAPI (opened 2021-06-15). Norte TRUE in the September 2022 extension. Gaps: the R$23M pre-seed's investors; the Series A amount (R$115M, R$116M, R$140M across sources); acquisition count (10 vs 20); no independent market-size figure (the gov.br Mapa de Empresas file returned HTML).

**Stark Bank.** Reads: site, Startups.com.br (Series A, credit), Finsiders, NeoFeed, Startupi (2020), Let's Money (2026), Times Brasil (2026), BrasilAPI (CNPJ 20.018.183/0001-80, opened 2014-04-03, not used for the year). The roster name had a trailing space, now removed. Press writes "Norte Capital" (Series A); we treated it as Norte Ventures and said so in the note. Gaps: the 2020 round's amount and type; other two of the "five rounds" (US$61.1M) Let's Money mentions; Times Brasil's allegations (CPIs, Pequi Bank) are from a single outlet and unverified.

**Nomad.** Reads: site, Startups.com.br (Series B, Series C, startups service), Startupi, Bloomberg Línea, Finsiders, Forbes, BrasilAPI (CNPJ 34.662.852/0001-66, opened 2019-08-26). Linked API: `search-posts "Nomad conta global" --mentioning "Norte Ventures"` wf-60159b00-e9e1-4ce6-93c8-0c349cae05cd completed with one unrelated post (a student's Insper Ventures thesis on Nomad), no round post. Gaps: Norte not named in any round; two earlier rounds (about US$7.5M) undescribed; Riotimes and Brazil Journal pages returned navigation only; 2026 BRL average rate not in fx.csv so the Series C `size_usd` is empty.

## For the recipe

- Run the Linked API `search-posts` in the background and carry on: three of the four runs finished long after the first reads were done.
- Several sites served navigation only to the stripper (Forbes, Brazil Journal "?p=" URLs, Rio Times); search for the article's own URL instead.
- Press names the fund "Norte Capital" (Stark Bank, Dolado before); decide the rounds' `TRUE` on the note's stated assumption.
- When a figure in a founder's goal sounds odd (Crown's R$1 trillion), check the denominator against the Central Bank's statistics; here it was M3, not the monetary base.
