# Batch 6 (2026-11-24): Malga, Cayena, Quansa, Sanii, Vendah, Jitter, Caveo, Level AI

Eight companies, in file order, one at a time. Norte's Manifesto re-read 2026-11-24 (unchanged). `python scripts/check_data.py` passes and `python -m unittest discover -s tests` passes (107 tests). Tools: page reads (`curl --compressed` plus a text extractor that drops short navigation lines), web search, minhareceita.org for the registry (BrasilAPI URL cited), Linked API for 9 workflows in total.

## Norte counts (rounds written)

| Company | TRUE | FALSE | UNKNOWN | Rounds |
|---|---|---|---|---|
| Malga | 2 | 0 | 1 | 3 (seed 2021, seed extension 2022, Series A 2025) |
| Cayena | 3 | 0 | 1 | 4 (seed 2020, Series A 2021, Series A 2022, Series B 2024) |
| Quansa | 1 | 0 | 0 | 1 |
| Sanii | 1 | 0 | 1 | 2 |
| Vendah | 1 | 0 | 1 | 2 |
| Jitter | 0 | 0 | 0 | 0 (Norte appears only in aggregators; no round row) |
| Caveo | 1 | 0 | 1 | 2 (Series A written as one Round of two tranches) |
| Level AI | 2 | 0 | 1 | 3 |

Total: 11 TRUE, 0 FALSE, 5 UNKNOWN. Main gaps: Jitter has no readable Round; Level AI's 2022 round has no amount; Malga's 2022 extension has no amount; Quansa has no round after 2021; no company has an exact month for every milestone.

## Linked API workflows

`search-companies` by name alone, run in one background script (the first attempt was killed when its shell call ended; wf-5725af93-951a-429c-8c7c-a11cc0697432 started and was not read). Results used for HQ only:

- Malga wf-64c07f81-2585-4afa-979c-1aad601de6a2: page `gomalga`, location "Remoto, Brasil" (so HQ São Paulo is Estimated, from the footer and registry).
- Cayena wf-63a87cea-dbed-4853-87b3-4cff28358068: `oicayena`, São Paulo, SP.
- Quansa wf-159d0b26-7bdc-4e22-83e5-6adb44e83679: São Paulo.
- Sanii wf-407cd2e0-71de-4c60-83b6-f0e4c0a6fde5: `sanii`, São Paulo, SP (a second "Sanii" in Buenos Aires is a namesake).
- Vendah wf-ce32e30b-ed88-4609-a2ca-e70205717094: "Vendah (YC W23)", São Paulo, SP.
- Jitter wf-25a34f2f-fddc-48a2-8672-46bc5ee8404a: `jittervideo`, Paris.
- Caveo wf-3a655ea9-96a5-45b6-a510-ba93d136b945: `caveotecnologia`, São Paulo, SP.
- Level AI wf-cb3053d9-ec3b-44c2-aa09-4a1a0910b99e: namesakes only (Mountain View, Kathmandu and others); no page for the Brazilian company. HQ comes from the company site.
- Jitter `search-posts "Jitter motion design" --mentioning "Norte Ventures"` wf-a292e7d5-5f81-4636-964b-65d6d400f33b: `[]`.

## Malga

- **Reads:** malga.io home; Brazil Journal (Series A, 2025-02-25); Startups.com.br (rebrand 2023-02-07, volume 2025-11-28); Bloomberg Línea (Drip 2024-12-16; Plug seed 2021-11-17; weekly rounds); LatamFintech (Brazil Journal copy); Finsiders (Abecs 2025 card volume); minhareceita (Malga Consultoria e Serviços Ltda, opened 2020-05-13, São Paulo; partners Alex Vilhena, Thiago Garuti, a US LLC).
- **Rounds:** 2021 seed US$2.7M (Norte TRUE, Startups.com.br 2023), 2022 extension (amount unknown, UNKNOWN), 2025 Series A R$32M (Norte TRUE).
- **Conflicts:** Startups.com.br later gives a US$6.5M total seed (summary, unread); LatamFintech says US$5M and CB Insights US$5.55M for the Series A (not used); Brazil Journal says R$4B volume for 2024, Bloomberg Línea R$5B annualised.
- **Gaps:** Y Combinator batch name (not in the pages read); pricing; Plug's move from Rio de Janeiro (2021) to São Paulo; Marcel Nicolay is not in the registry's partner list.

## Cayena

- **Reads:** cayena.com (a JavaScript page, nothing readable); Norte's own case post "Cayena: The Streamliners" (market, founders' story); Startups.com.br (Series B 2024-09-18); Bloomberg Línea (2021 Series A); Exame via `curl --compressed` (2020 seed and 2021 Series A, with Norte); Brazil Journal and Startupi (2022 round); LatamList (Series B).
- **Rounds:** 2020 seed R$2.5M (Norte TRUE, Exame), 2021 Series A R$20M (TRUE), 2022 R$100M (UNKNOWN: Startupi's list ends "entre outras"), 2024 Series B R$300M (TRUE).
- **Conflicts:** Startups.com.br (2024) calls the 2021 US$3.5M round a "seed"; Bloomberg Línea and Exame call it a Series A and agree on size (R$20M is US$3.7M). LatamList says founded 2020; Bloomberg Línea says the MVP launched September 2019 (kept).
- **Gaps:** CNPJ (none on the page); breakeven (InvestNews, search summary only); news after the Series B.

## Quansa

- **Reads:** quansa.com.br home and /sobre (CNPJ 41.090.066/0001-05, founders, customers); quansa.io (Chile site, Spanish); NeoFeed and Startups.com.br (seed, July 2021); RAIS 2024 release (Agência Gov). The Valor Capital blog returned a Mod_Security error; Finsiders returned page-builder code.
- **Rounds:** 2021 seed US$3.6M (Norte TRUE).
- **Gaps:** any round after 2021; HQ city in 2021 (Santiago is our assumption); when the product moved from financial health to frontline retention.

## Sanii

- **Reads:** sanii.com.br and /sobre-nos; Startups.com.br (pre-seed 2023-10-25; Campinas 2026-07-06); Startupi (pre-seed); InfoMoney (R$5M follow-on 2025-12-16). Publication dates read from the `published_time` meta.
- **Rounds:** 2023 pre-seed R$8M (Norte TRUE), 2025 follow-on R$5M (UNKNOWN).
- **Conflicts:** founded 2022 (InfoMoney) vs. early 2023 (Startups.com.br): 2023 kept. Its site's "14 years" is Senior Services, a company the founders bought and merged (date not found; the milestone was dropped).
- **Gaps:** CNPJ (not on the pages read); date of the Senior Services purchase and of the change from prevention visits to caregiver placement.

## Vendah

- **Reads:** vendah.com.br (CNPJ 41.798.727/0001-43); Y Combinator profile (W23, pivot, traction); Startups.com.br, Startupi, bpmoney and LatamList (2023 seed, 2021 pre-seed); minhareceita (Vendah Atividades de Internet Ltda, opened 2021-05-03; administrators Luis Felipe Franco and Marcelo Canovas).
- **Rounds:** 2021 pre-seed R$8.5M (Norte TRUE, named in the 2023 articles), 2023 seed R$12M (UNKNOWN; CB Insights lists Norte, an aggregator).
- **Leads to verify:** Pedro Pedruzzi (CTO) and Ilana Nasser (co-founder) from directory sites only; Marcelo Canovas is a founder only from the registry (Estimated).
- **Gaps:** date of the move from home goods to beauty plus credit; any round after 2023.

## Jitter

- **Reads:** jitter.video home, pricing, changelog, Figma plugin page, blog "Welcome to motion design"; Y Combinator profile (Winter 2020, Paris, two founders); diginomica (Figma revenue 2025). Seedtable, Village.ai, CB Insights and Crunchbase pages returned nothing readable.
- **Rounds:** none written. Aggregators (seen in search summaries) list Norte Ventures and a US$150K seed with Y Combinator; no readable page, so no row.
- **Gaps:** the round and Norte's participation; plan prices; the alternativeto article on Figma's motion tool (June 2026) was not read, so the thesis cites only Jitter's blog for it.

## Caveo

- **Reads:** caveo.com.br (CNPJ 41.042.624/0001-59); Brazil Journal (Feb 2025 and Dec 2025); Startups.com.br, Baguete (Series A, 2025-12-10); NeoFeed (Afya round, 2024-06-13); Portal Tela; minhareceita (Caveo Tecnologia Ltda, opened 2021-03-01).
- **Rounds:** 2024 seed ~US$1M (UNKNOWN: "investors such as"), 2025 Series A R$54M in two tranches (Norte TRUE in both).
- **Conflicts:** founded 2021 (registry, Baguete) vs. 2022 (Brazil Journal, NeoFeed): 2022 kept. The February R$20M is called pre-Series A by Brazil Journal and part of the Series A by Startups.com.br: one Round.
- **Gaps:** the R$6.5M earlier "pool of doctors" round (no date); whether Norte was in the 2024 round; Lorenço Boettcher is a founder only from Brazil Journal.

## Level AI (formerly NeuralMed)

- **Reads:** levelai.com.br home and /sobre; NeoFeed (Spanish edition, 2026-04-03, rename and reset); Baguete (2021-03-24 and 2021-08-17); MedicinaSA (GNDI stake); Startups.com.br (2022-11-16); O Liberal (ANS beneficiaries); Folha de Pernambuco (operators' profit).
- **Rounds:** 2021 pre-seed R$3.2M (TRUE), 2021 R$10M (TRUE), 2022 undisclosed, GK lead (UNKNOWN, type `unknown`).
- **Gaps:** CNPJ; HQ at first investment; Kortex Ventures' round and the IDB's separate investment (dates); Linked API found no page. The domain-to-NeuralMed link rests on the word NeuralMed in the site's code and on NeoFeed.

## Lessons for the recipe

See `docs/research-recipe.md`, "Lessons from Batch 6".
