# Batch 11 (2026-11-24): Aro, Fly Media, Inner AI, Bond, Maggu, Core AI, Datamint, Oasis, Akash, Asteras

Rows written to `data/` for all ten, `researched_on` set, `python scripts/check_data.py` and `python -m unittest discover -s tests` (107 tests) pass. The ten are the first ten Fund II companies without `researched_on`, in file order. Norte count over the 10 Rounds: TRUE 6 (Aro pre-seed 2026, Fly Media seed 2025, Inner AI seed 2026, Bond pre-seed 2026, Maggu seed 2026, Core AI seed 2026), FALSE 0, UNKNOWN 4 (Inner AI pre-seed 2024, Maggu pre-seed 2024, Core AI pre-seed 2025, Datamint seed 2026). No Round found for Oasis, Akash or Asteras. New sub-sectors (10): AI credit assistant and lender distribution; AI-native media and synthetic influencers; AI productivity platform and agents for SMEs; AI-run accounting operations for firms and SMEs; AI copilot for pharmacy counter staff; AI credit decisioning layer for embedded lending; Industrial asset management AI platform; Workspace for human and AI agent teams; AI intelligence platform for security and defense; Custom AI model training for company agents. No new FX rate: Fly Media (BRL 2025) and Inner AI (BRL 2024) converted; the 2026 BRL average is still missing, so Inner AI seed, Bond and Maggu seed have no `size_usd`.

## Linked API (all through `scripts/linkedin.py`)

Name-only `search-companies`, one script under `run_in_background` (the first attempt, started with `&` inside the call, died after one workflow, so Aro was searched twice).

| Company | Workflow | Result |
|---|---|---|
| Aro | wf-5c369d2d-3a62-455d-9eae-0af105d97242 (and wf-ccd18009-48fd-400a-8fae-8d9720597c4e, the repeat) | `aro-platform`, financial services, São Paulo SP (right page; four namesakes) |
| Fly Media | wf-9e7d108f-0de7-4784-8f3e-7eb9f69ace68 (repeat wf-c3d86ed7-b6ef-4a41-8f1c-5f742229f4b7) | five namesakes (Dubai, Gurgaon, Kansas City, Atlanta); `flymedia-inc` has no location, not confirmed |
| Inner AI | wf-2d2d581a-a20c-4395-b37c-6df845c8ab29 | `innerai` page, no location (several namesakes) |
| Bond | wf-d71cf49d-e9b7-44ab-af64-f7a3b7a3c362 | namesakes only (London, Helsinki, New York, Los Angeles, Toronto); HQ came from the site footer and the registry |
| Maggu | wf-3ab1fc73-ade5-441d-b735-5ac035c6bade | `maggu` page, no location (and an Indian namesake) |
| Core AI | wf-35c49399-8cec-4137-a176-79b0db18246d | `core-ai-tech`, São Paulo (used for HQ, Medium) |
| Datamint | wf-6d5af3cb-666d-4626-b7f0-24f95ac210e2 | `datamint`, Rio de Janeiro RJ (used for HQ, Medium) |
| Oasis | wf-505030e5-36c7-4872-acf2-36148a0f7ba0 | namesakes only; HQ came from the careers page |
| Akash | wf-16aa5be9-deeb-4a3a-9ef5-382dbfa8737f | namesakes only |
| Asteras | wf-9f55dc98-86c0-4a1d-91fb-43905d97a815 | `asteraslab`, AI, no location |
| Second script (li2) | Asteras `company` wf-1cdbc009-240b-499a-8c4e-0c694df83ccb, then Asteras `founders`, Maggu `company`, Fly Media `company flymedia-inc`, Akash `search-companies "Akash SERAPH superinteligencia"` | **Not finished when this note was written** (the first workflow had been running more than 30 minutes). Fetch with `python scripts/linkedin.py result <workflow-id>`; whatever returns can fill HQ for Asteras, Maggu and Fly Media, and founders for Asteras. The output file is the scratchpad `li2.out` of this session; the other workflow ids print on stderr when each starts. |

No `search-posts ... --mentioning "Norte Ventures"` was run: every Norte answer came from press.

## Aro

- **Reads:** aro.ia.br (home, legal footer, CNPJ), NeoFeed 2026-04-13, Let's Money 2026-04-14, LatamList 2026-04-21, Startups.com.br 2026-08-25 (full interview, carve-out, lenders, plans), Serasa press release (84.2M overdue adults, R$597.4B); minhareceita for CNPJ 59.743.959/0001-60 (Aro Plataforma Ltda, opened 2025-03-05, São Paulo; administrators Pedro Milanez since opening and Yuri Mannes only from 2026-09-09; foreign partner StarW LLC).
- **Fields filled:** all single-value fields, 2 founders, market, 5 milestones. Round: pre-seed 2026 US$2.5M (ONEVC and 17Sigma lead), Norte TRUE in all four articles.
- **Gaps:** HQ at first investment (same city, Medium); whether Fund II invested again; who the three embedded-finance clients are; details of the Celcoin licence arrangement and of the carve-out; the exact MVP month (November vs December 2025).
- **Leads to verify:** StarW LLC as a US holding (registry only).

## Fly Media

- **Reads:** flymedia.ai (home only, a Framer-like page with marquee text), Forbes Brasil 2025-12-11 and 2026-04-20, Startups.com.br 2025-12-11, Let's Money 2025-12-11, LatamList 2025-12-12.
- **Fields filled:** description, long description, thesis, sub-sector, year, status, model, 2 founders, market, 2 milestones. Round: seed 2025 R$20M (about US$3.58M at the 2025 average; LatamList says US$3.7M), ONEVC lead, Norte TRUE (Forbes, Startups.com.br, Let's Money).
- **Conflicts:** founding year (company launched December 2025, but the CEO says it was an influencer agency for about ten years): 2025, Low. Investor lists differ (Forbes omits Big Bets).
- **Gaps:** HQ (an aggregator says New York; Brazilian outlets call it Brazilian; no registry or page states it), CNPJ, the site's own claim of over one billion views (company figure shown on the page, not cited), dated events for Foka (launch "a week after Big Brother Brasil 26 began" was left undated) and Fly Studio, customers.
- **Leads to verify:** "1.2 billion views in nine months" (Clickpetróleo summary of Exame, not read); an Exame article quoted second-hand; Caplight's New York location.

## Inner AI

- **Reads:** innerai.com (Black Friday home), Startups.com.br 2024-04-02 and 2026-10-19, Baguete 2026-04-08, Bloomberg Línea Brasil 2026-04-11; Agência Sebrae (small-business openings 2026).
- **Fields filled:** all single-value fields except `hq_at_first_investment` Low, 2 founders, market, 5 milestones. Rounds: pre-seed 2024 R$12M (Canary lead; partial list, Norte UNKNOWN) and seed 2026 R$30M (Canary and ONEVC co-lead, Norte TRUE; Vivo Ventures extension counted in the same Round).
- **Conflicts:** Startups.com.br 2026-10 credits Pedro Salles alone as founder, Baguete and the 2024 pieces credit Salles and Eduardo Mitelman (kept both, Mitelman Medium).
- **Gaps:** paying users and revenue; HQ not on the LinkedIn search result; Exame's 2024 article was not opened.
- **Leads to verify:** Meio & Mensagem piece on a new version with Tadeu Schmidt (title only).

## Bond

- **Reads:** bond.com.br (home and FAQ), Brazil Journal 2026-04-15, LatamList 2026-04-17, LatamFintech 2026-05-08, Portal Tela and Acionista (copies of Brazil Journal); minhareceita for the two CNPJs in the footer: 65.322.071/0001-56 (Arca Holdings Tecnologia Ltda, opened 2026-02-20, São Paulo, administrators Gabriel Proença Jordão and Matheus Agostini Oliveira, foreign partner Arca Tech Holdings LLC) and 64.457.691/0001-30 (the LLC, opened 2026-01-13, suspended); Sitecontabil (101,880 accounting organisations).
- **Fields filled:** all single-value fields, 2 founders, market, 2 milestones. Round: pre-seed 2026 R$10M (Propel lead), Norte TRUE in four articles.
- **Conflicts:** the amount is R$10M (Brazil Journal) or US$2M (LatamList); aggregators call it seed or Series A (not used); the product changed from a full-service accounting firm (April 2026) to an operation partner for accounting offices (current site), with no date for the change.
- **Gaps:** date of the model change; clients and revenue; Propel's full name (Propel Venture Partners in LatamList).

## Maggu

- **Reads:** maggu.ai (almost no text), Startups.com.br 2026-03-09, Baguete 2026-03-09, Funds Society 2026-03-10, LatamList 2026-04-09; Medicina S/A (93 thousand pharmacies) and Mercado & Consumo (Abrafarma ranking).
- **Fields filled:** description, long description, thesis, sub-sector, year, status, model, 5 founders, market, 4 milestones. Rounds: pre-seed 2024 (undisclosed, Latitud and Airborne; Norte UNKNOWN) and seed 2026 R$22M (DGF lead, Norte TRUE in four pieces).
- **Gaps:** HQ (no page states it; LinkedIn search result had no location), CNPJ and registry (not found by search), the pre-seed amount, which cofounder is which role.
- **Leads to verify:** Reslley Gabriel as chief data and AI officer and Pedro Magela as COO (aggregator summaries); SnackIn's sale to Shopper.

## Core AI

- **Reads:** coreai.com.br, NeoFeed 2025-07-02, Brazil Journal 2026-03-19, Let's Money 2026-03-20; Isto É Dinheiro (Banco Central credit stock, R$7.444T in September 2026).
- **Fields filled:** all single-value fields, 3 founders, market, 3 milestones. Rounds: pre-seed 2025 US$1M (Big Bets lead; partial list, Norte UNKNOWN) and seed 2026 US$4.1M (14B lead, Norte TRUE in Brazil Journal only).
- **Conflicts:** pre-seed US$1M (NeoFeed) vs US$400k (Brazil Journal); seed US$4.1M (Brazil Journal, Let's Money) vs US$4.5M (Bloomberg Línea summary, not read); Carolina da Costa Carvalho is a founder in NeoFeed only.
- **Gaps:** CNPJ (a web search returned namesakes), HQ at first investment, the company's own account of its funding, Alude as the only named client.
- **Leads to verify:** VC Backed's list of seed investors (Norte, Big Bets, 14B, GP Investments), page not read.

## Datamint

- **Reads:** datamint.com.br (English), Brazil Journal 2026-06-12, Startups.com.br 2026-06-15, InfoMoney 2026-06-16, Baguete 2026-06-17, Dealroom 2026-06-15, Startup Researcher.
- **Fields filled:** all single-value fields, 1 founder, market, 3 milestones. Round: seed 2026 US$5M (Headline lead); Norte UNKNOWN.
- **Norte:** no readable page names Norte. A FundUp profile (Cloudflare, not readable) lists Norte as a lead investor and a search summary listed Crivo, Verve, Nameless, Vereda and Heyho; both are leads. Startup Researcher says "and others", so the investor list is partial.
- **Conflicts:** Túlio Ribeiro is called a co-founder by Dealroom but joined in April 2026 (Brazil Journal, Baguete), so not a founder; PUC-Rio career length (34 vs 40 years).
- **Gaps:** founders other than Hélio Lopes (students not named), CNPJ, customers, revenue.

## Oasis

- **Reads:** joinoasis.com (home, About, Careers, Blog), a16z speedrun pages (company, Naveen Sharma, Stefano Delmanto), Peerlist. Product Hunt and Digg returned nothing.
- **Fields filled:** description, long description, thesis, sub-sector, HQ (careers page), year (Low, from the first dated blog post), status, model, 2 founders (Medium; one speedrun profile has text about another project), accelerator (a16z speedrun, Medium), 1 milestone. No Round.
- **Gaps:** funding and Norte's participation, customers, the other blog author (Jayson), the speedrun cohort (006 in a search summary only), the Product Hunt launch (August 2026, search summary only).
- **Leads to verify:** a Product Hunt launch in August 2026; speedrun cohort 006 and five employees.

## Akash

- **Reads:** akash.earth (Spanish) and akash.si/en (English) only, two sections with no names. Web searches by name, product (SERAPH) and Norte returned namesakes (Akash Systems, Akashalabdhi).
- **Fields filled:** description, long description, thesis, sub-sector, status (Low), model (Low). No HQ, founders, year, markets or Round: the site gives none and no other page exists.
- **Gaps:** everything about the team, location, customers and funding. Likely cause: stealth-like company with only a landing page.

## Asteras

- **Reads:** asteraslab.com (home, privacy, ethics returned a 404 page), GitHub organisation (no public repositories). Web searches returned namesakes (Astera Institute, Aster).
- **Fields filled:** description, long description, thesis, sub-sector, status (Low), model. No HQ, founders, year, markets or Round.
- **Gaps:** team, location and funding. The Linked API `company` and `founders` workflows were still running at the end of the session (see the table).

## Recipe changes

Added to `docs/research-recipe.md` under "Lessons from Batch 11".
