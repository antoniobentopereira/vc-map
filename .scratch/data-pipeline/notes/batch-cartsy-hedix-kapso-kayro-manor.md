# Batch 12 (2026-11-24): Cartsy, Hedix, Kapso, Kayro, Manor

Rows written to `data/` for all five, `researched_on` set, `python scripts/check_data.py` and `python -m unittest discover -s tests` (107 tests) pass. The five are the first Fund II companies without `researched_on`, in file order. One Round found (Kapso seed 2026). Norte count over 1 Round: TRUE 1, FALSE 0, UNKNOWN 0. Four sub-sectors added to `sectors.csv`; no new FX rate (the only Round is in USD).

These are the youngest companies yet (registries opened between September and October 2025): four have no press at all, so most profiles rest on the company's own site and the registry, and are short.

## Linked API (all through `scripts/linkedin.py`)

One script (`search-companies` by name alone for Cartsy, Hedix, Kapso, Kayro, Manor, in that order) under `run_in_background`. The first workflow, **Cartsy, `wf-aa9c70bf-bfe1-4731-89ef-73b92fb952b3`**, had not returned after more than 30 minutes when this note was written, and the account runs one workflow at a time, so the other four were not started. Fetch with `python scripts/linkedin.py result wf-aa9c70bf-bfe1-4731-89ef-73b92fb952b3`. `check` succeeded. No `search-posts` was run: Norte's only Round here came from press. Nothing in `data/` depends on Linked API.

## Cartsy

- **Reads:** cartsy.com (the page returned only after a `curl` with a browser agent; the visible text is in the HTML, not in an extractor's output), its privacy policy (names CR AI Labs, Inc.). Web searches returned only namesakes (cartsyai.com, a design kit) and no press.
- **Fields filled:** description, long description, thesis, sub-sector, status, business model, accelerator (a16z speedrun, estimated, low: the page shows 'Backed by' and a Speedrun logo).
- **Gaps:** founders, HQ, year, markets, any Round (speedrun usually invests, which would be a Round, but no page says so), user numbers, launch date, whether Norte's participation can be dated.
- **Leads to verify:** that the Speedrun logo is a16z speedrun and which cohort; founders and Instagram handle activity.

## Hedix

- **Reads:** hedix.com.br (a one-page waitlist and legal notice; /sobre and /carreiras 404); minhareceita.org for CNPJ 63.022.244/0001-95 (HEDIX Tecnologia e Marketing Ltda., opened 2025-10-03, São Paulo; administrators João Marcelo da Cunha Pinheiro Naves Gomes and Matheus Brandão Salomão since opening; partner HEDIX LLC, a foreign entity, from 2025-12-29); Finsiders Brasil 2026-03-09 and Startups.com.br 2026-02-12 (Prévias) for the prediction-market context. Three searches found nothing on Hedix.
- **Fields filled:** description, long description, thesis, sub-sector (estimated, low), HQ (Estimated), year (Estimated), status `stealth`, model, 2 founders (registry, Low), market. No milestones (registry events are housekeeping). No Round.
- **Gaps:** what the contracts actually are (the site never says prediction market), launch date, funding, whether Norte invested, who the founders are beyond the registry.
- **Leads to verify:** the HEDIX LLC partner (US holding, often a round marker); the claim that Brazilian platforms were in regulatory limbo since April 2026 (search summary only).

## Kapso

- **Reads:** kapso.ai (home, /about, /blog), five Kapso blog posts (seed round 2026-08-23, 10k developers 2026-03-26, 5000 developers 2026-01-14, managed billing 2026-07-23, product updates 2026-02-12), Dealroom News 2026-08-24, SignalBase 2026-08-28. Startup Researcher returned 429 twice and was not used.
- **Fields filled:** description, long description, thesis, sub-sector, status, model, founder (Andrés Matte), 4 milestones. Round: seed 2026, US$1.4M, Norte `TRUE` (Dealroom News and SignalBase list Norte Ventures; no lead named).
- **Gaps:** HQ (Dealroom says Chilean startup, no page states an HQ), year founded (an aggregator says 2024, not used), markets, lead investor, revenue, Norte's stake in earlier rounds (none known), whether this is Norte's first investment (assumed, one Round only).
- **Leads to verify:** the 2024 founding year (startup-seeker, unread); HQ.

## Kayro

- **Reads:** usekayro.ai (home, /copiloto-de-vendas; /sobre 404); Mercado & Consumo 2026-05-12 (ABAD/NielsenIQ ranking: R$616.6 billion, 768 respondents, 1.18 million points of sale); Startups.com.br 2026-08-28 (Sharpi, a comparable). Four searches found no page about Kayro.
- **Fields filled:** description, long description, thesis, sub-sector, HQ (site footer address in Jardim Europa, São Paulo), status, model, market. No founders, year, milestones or Rounds.
- **Gaps:** founders, CNPJ (not on the pages read, so no registry check), year founded, customers, funding, whether Norte took part in a Round.
- **Leads to verify:** the company says the largest manufacturers, distributors and wholesalers already operate with Kayro (not named); Canals (US$35M) and Anchr as competitors (search summary only).

## Manor

- **Reads:** manor.com.br (home; /sobre and /quem-somos 404); minhareceita.org for CNPJ 62.490.945/0001-96 in the footer (Manor Desenvolvimento de Software Ltda., opened 2025-09-01, Campinas; sole administrator Rodrigo Augusto Gomes Salvador; partner Manor Tax LLC, a foreign entity); Sitecontabil (101,880 accounting organisations). Three searches found no press on Manor.
- **Fields filled:** description, long description, thesis, sub-sector (`Tax intelligence`, existing), HQ (registered seat, Estimated, Low), year (Estimated, Low), status, model, founder (registry, Low), market. No milestones, no Round.
- **Gaps:** founders beyond the registry, the real HQ, customers, funding and the OAB/SC partnership's date, Norte's participation.
- **Leads to verify:** that the site offers an ERP integration, MCP and AI agents (a search summary said so; the pages read did not); Manor Tax LLC as a US holding.

## Recipe changes

Added "Lessons from Batch 12" to `docs/research-recipe.md`.
