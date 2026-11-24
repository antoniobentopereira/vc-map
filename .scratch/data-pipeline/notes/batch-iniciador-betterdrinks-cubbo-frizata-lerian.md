# Batch: Iniciador, Better Drinks, Cubbo, Frizata, Lerian

Researched 2026-11-20 (written up 2026-11-24). Sequential, no sub-agents. Manifesto re-read (unchanged from the recipe's summary).

| Company | Rounds | Norte TRUE / FALSE / UNKNOWN | Linked API |
|---|---|---|---|
| Iniciador | 2 (pre-seed 2021, R$32M 2025) | 1 / 0 / 1 | none needed |
| Better Drinks | 2 (R$25M 2022, R$65M debt 2023) | 1 / 1 / 0 | none needed |
| Cubbo | 2 (US$4M seed 2021, undisclosed pre-A 2022) | 0 / 0 / 2 | 2 workflows |
| Frizata | 1 (R$25M Series A 2021) | 1 / 0 / 0 | none needed |
| Lerian | 2 (R$18M 2024, R$30M 2026) | 2 / 0 / 0 | none needed |

## Per company

**Iniciador.** Reads: site (home, About), Brazil Journal, Finsiders, Startupi, LatamList, LatamFintech, launch post of 2026-05-19, Finsiders Pix-initiation volume article, BrasilAPI (CNPJ 44.471.172/0001-19, opened 2021-12-03). Norte named in the 2025 round by four outlets. Gaps: year and investors of the R$1.2M first round (year 2021 is our estimate, type our label); no competitor named in any source; Guilherme Decampo (Finsiders) vs registry's Guilherme Campos Gomes da Silva could not be reconciled; Let's Money returned 403.

**Better Drinks.** Reads: site, Brazil Journal (2023 debt), Bloomberg Línea, Forbes Brasil, NeoFeed 2022 and 2026, SuperVarejo, Startups.com.br (Mamba), Exame (Heineken 2024), BrasilAPI (CNPJ 38449212000123 is an S/A seat in Serra, ES, opened 2020: not used for HQ or year). Norte named only in SuperVarejo's list of angels in the R$25M launch round. Heineken's 2026 purchase of control is pending Cade approval, so no `acquirer` or `acquisition_year` row yet: add them when it closes. Gaps: Norte's stake and amount; HQ dated only by today's footer.

**Cubbo.** Reads: site, Bloomberg Línea (Spanish and English), El Referente, Forbes Colombia (DedaLog, pre-A), Mexico Business News, Mexico Industry, Xataka, Startups.com.br (2026-10-20), AMVO study via Informa BTL, ABIACOM via Mercado&Consumo, Descubre.vc. TechCrunch returned a Cloudflare block. Linked API: `search-posts "Cubbo" --mentioning "Norte Ventures"` (wf-da74cbb3-6f27-47c1-9918-9e580b1061fa) completed with one BluStone post about its portfolio, no Cubbo round post; `company https://www.linkedin.com/company/cubbo-mexico` (wf-6f7e8e76-eb0c-4839-a3ba-9c4f2ea280cc) ended in `unexpectedError` (a first fetch also hit a network timeout), not retried. Gaps: Norte's round (Norte is on the Portfolio page but no source names it in a Cubbo Round); HQ (Mexico City vs Colombia, no page states it); the US$4M between the seed and the US$8M total; any Series A.

**Frizata.** Reads: site (Argentine shop, no About page), Brazil Journal, Forbes Brasil, Forbes Argentina, LatamList, AgFeed 2023, Cronista, Descubre.vc (June 2026, second-hand from puntobiz.com.ar), IMARC. Norte named by Brazil Journal and LatamList in the 2021 Series A. Gaps: whether Brazil is still served in 2026; revenue after 2023; no Argentine market-size figure; 2018 vs 2019 start.

**Lerian.** Reads: site (home, Sobre, privacy policy with CNPJ 57.616.968/0001-64), Brazil Journal, Startups.com.br (two articles), Baguete (two), Finsiders 2026, Fintech Global, Jornal do Brás, Visa's Pismo release, Market Research Future. BrasilAPI: opened 2024-10-09, one administrator, a foreign LLC partner (a US holding, a lead only). Norte named in both rounds. Gaps: 2026 `size_usd` (no 2026 BRL average in `fx.csv`); the founder list (Zapata in 2024, Maísa Amaral in 2026); Midaz licence terms not read (the README fetch returned nothing); Let's Money returned 403.

## For the recipe

- Brazilian sites that render empty without JavaScript (Iniciador PT) work in English (`/en`).
- Cloudflare blocks TechCrunch; Bloomberg Línea carries the same stories.
- A Linked API client run can die on a network timeout while polling: fetch the workflow later with `result <id>`.
- Market-research summaries (IMARC, Market Research Future) change between editions; cite the page read and call it a rough order of magnitude.
