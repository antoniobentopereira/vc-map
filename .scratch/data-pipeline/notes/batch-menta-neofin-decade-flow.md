# Batch 10 (2026-11-24): Menta, Neofin, Decade, Flow

Rows written to `data/` for all four, `researched_on` set, `python scripts/check_data.py` and `python -m unittest discover -s tests` pass. Norte count over the 5 Rounds: TRUE 3 (Neofin seed 2025, Decade seed 2025, Flow pre-seed 2025), FALSE 0, UNKNOWN 2 (Menta pre-seed 2021 and seed 2022). New sub-sectors: White-label payment acceptance for B2B networks; Accounts receivable and collections automation; AI wealth management advisory; Home equity credit marketplace. No new FX rate (BRL 2025 and USD were already usable).

Linked API (all through `scripts/linkedin.py`, name-only `search-companies` run as one script under `run_in_background`):

| Company | Workflow | Result |
|---|---|---|
| Menta | wf-39c0d9ac-8418-4ecd-b9ae-af0840fdb9fa | five namesakes; `menta-payments` (CABA, BS AS) is the right one |
| Menta `company .../menta-payments` | wf-d9d9a12d-593c-4b3a-80ef-f180b1ab7150 | website menta.global, 54 employees, HQ AR, location CABA, yearFounded 2021 (not used alone) |
| Menta `search-posts "Menta" --mentioning "Norte Ventures"` | wf-1997a56e-2ef8-4737-a234-d92a48930788 | `[]` |
| Neofin | wf-daec09d8-c889-47dc-aa5b-48f0bfa3423a | `neofintecnologia`, São Paulo (plus four namesakes) |
| Decade | wf-a1aeb895-1afc-4f00-a30d-9fb0559b6c58 | `decade-wealth`, São Paulo (plus namesakes) |
| Flow | wf-a10f8a98-b1d4-4168-b70e-194f8f30ad13 | namesakes only (Rabat, Santiago, Caribbean...); FlowCredi not returned, so HQ came from the registry |

## Menta (Argentine paytech, not the Argentine healthtech Menta)

- **Reads:** menta.global (Next.js; only meta description readable, "Infraestructura de cobro marca blanca"); Forbes Argentina 2022 (seed) and 2024 (US$23M billing, ~40 staff); El Cronista 2022 (founders, pre-seed Pear, US$33M valuation); Contxto, LatamList, Bloomberg Línea (2022), Portafolio (Colombia), Fintech Nexus, Latamfintech, Impacto TIC (CEO profile). Discarded: Ecosistema Startup 2026-08-28, which is another Menta (healthtech for clinics, Lucas Tortonese).
- **Fields filled:** description, long description, thesis, sub-sector, HQ (Linked API page), HQ at first investment (low), year (2021), status, model, 3 founders, 3 markets, accelerator (Pear W22 cohort, from founders' LinkedIn per Contxto), 6 milestones. Rounds: pre-seed 2021 US$1.7M (Pear lead), seed 2022 US$6M (Base10 lead).
- **Norte UNKNOWN twice:** the 2022 articles list "some funds such as" Pear, Matterscale, Gilgamesh and an extra note for more investors; CB Insights lists Norte and Fin Capital without a round (page not readable). Linked API post search found nothing.
- **Gaps:** no 2025 or 2026 news on rounds, customers or new markets (status rests on the live site and the LinkedIn page); no registry (Argentina not tried; CUIT not on the site); Norte's actual round; the pre-seed month (September vs November 2021); Quirno's current title is from Forbes 2024 only.
- **Leads to verify:** Fin Capital as an investor (CB Insights only); Menta in the WEF directory (search result, not read); a 2026 LinkedIn post by a product manager (search summary, not read).

## Neofin

- **Reads:** neofin.com.br (home, /sobre, /termos, /privacidade, /integracoes-e-parceiros, BHub case, /blog); Finsiders and Startupi (2025-02-05), LatamList, Latamfintech (two Spanish translations of the GlobeNewswire and Exame pieces, undated), Bloomberg Línea Brasil (2025-02-10), Portal ERP (Nomus, date from page source 2024-07-02), G1 sponsored special (2026-04-13), Contábeis (2026-05-21); minhareceita for CNPJ 48.864.960/0001-26 (Neofin Tecnologia Ltda, active since 2022-12-12, administrators Laura Camargo and Arthur Cunha, foreign partner Neofin Holding LLC).
- **Fields filled:** description, long description, thesis, sub-sector, HQ, HQ at first investment, year (2023; registry 2022-12-12 in the note), status, model, 3 founders, market, 6 milestones. Round: seed 2025 R$35M (Quona and Upload co-leads), Norte TRUE (Finsiders, Startupi, LatamList, Latamfintech).
- **Conflicts:** US$5M, US$6M, US$7M in the English and Spanish pieces versus R$35M in Brazil: BRL kept (R$35M is US$6.3M at the 2025 average). Founders' prior employers differ slightly across pieces (Laura: Pátria and General Atlantic vs Gympass and Inventa).
- **Gaps:** an earlier angel round (Cesar Carvalho, Patrick Sigrist) with no date, size or article; CB Insights shows a 2023 entry (page not readable) so no row; Leandro Sarmento's role is only press (not in the registry); the Web Summit Rio piece and Band article returned no text; no competitor research beyond ERPs.
- **Leads to verify:** Series A or later news (none found for 2026); the date of the Serasa partnership.

## Decade

- **Reads:** decade.com (home, FAQ, newsroom release, blog), NeoFeed, Brazil Journal, Bloomberg Línea Brasil, Forbes Brasil, Startups.com.br, The Next Web (all 2026-08-04 to 08); Business Wire and Fintech Futures did not open; Anbima 2026-02-24 release and InfoMoney (UBS Global Wealth Report 2026) for the market; minhareceita for Decade Wealth Management (CNPJ 64.755.417/0001-47, started 2026-01-23) and Decade Asset Management (62.051.122/0001-64, started 2025-08-04), administrators Vitor Olivier, Gustavo Ferreira de Matos, Jasper Bal.
- **Fields filled:** all single-value fields, 2 founders, market, 6 milestones. Round: seed 2025 US$85M, Norte TRUE (NeoFeed, Brazil Journal, Forbes Brasil, Startups.com.br; Bloomberg Línea and TNW omit it); no lead marked because no article names one.
- **Conflicts:** year 2025 (money entered at the end of 2025, company founded September 2025) versus announcement in 2026; Olivier left Nubank in August (Brazil Journal) or September 2025 (NeoFeed); The Next Web says no product, the others say it launched with a waitlist.
- **Gaps:** the lead investor; any customer or AUM number beyond "a few billion reais"; whether the other officers on the site (Carolina Maciel, Juliana Renault, Gustavo Matos, Jasper Bal, João Paulo Parizotto) are cofounders (site shows two founders only).
- **Leads to verify:** none outstanding.

## Flow (FlowCredi)

- **Reads:** flowcredi.com.br (home, /quemsomos; CNPJ in footer); Startupi and Startups.com.br (2025-12-10), LatamList (2025-12-12), Finsiders (2025-12-11, 2026-04-23), Capital Aberto (2026-09), Startups.com.br MVP podcast (2026-11-18); minhareceita for CNPJ 31.520.218/0001-09 (Flowcredi Promotora de Serviços Ltda, started 2018-09-17, partners Bruno Gama, Caio Alfano, Deivid Bastos, Luciana de Sena, Luis Felipe Fleury, Mayle Vaz, Rodrigo Gordinho). Let's Money returned nothing.
- **Fields filled:** all single-value fields, 2 founders, market, 6 milestones. Round: pre-seed 2025 R$3.5M, Verve and Norte co-leads, Norte TRUE.
- **Conflicts:** founders: Startupi lists Bastos, Gordinho, Vaz and Alfano; Startups.com.br and LatamList list Alfano and Bastos (kept); Bruno Gama is a Credihome cofounder who became CEO in late 2025. R$3.5M vs US$650K (consistent). R$500M approved credit in 2025 vs R$100M operations in 2026 are different measures. 20 institutions (site) vs 14 (CEO, 2026-11).
- **Gaps:** HQ is Estimated from the registry (no page states a city); no independent market-size source (the R$10-11 billion and R$500 billion figures are company or sector projections); Linked API did not return the company page (namesakes), so no headcount or location check.
- **Leads to verify:** whether Rodrigo Gordinho and Mayle Vaz count as founders (registry partners since 2025-07-29).
