# Batch 9 (2026-11-24): Arcca Franquias, Hashdex, Isa Health, Lexter, Winnin, Alude, Cannect, Gabriel

Rows written to `data/` for all eight, `researched_on` set, `python scripts/check_data.py` and `python -m unittest discover -s tests` pass (107 tests). Norte over the 16 Rounds: TRUE 3 (Hashdex Series A 2021, Isa Health 2021, Gabriel Series A 2021), FALSE 4 (Lexter 2024, Cannect 2024 media-for-equity, Gabriel's two debt rows), UNKNOWN 9. Arcca and Winnin-before-2024 have no readable Round with Norte.

Norte's Manifesto (read once through the web-fetch agent, 2026-11-24) is unchanged from the 2026-11-20 reading: obsessed founders, no operational role, a network ("Norte Mafia", 400+), top funds and angels onto cap tables, size of the pie.

Linked API (all through `scripts/linkedin.py`, one script file for eight `search-companies` runs by name alone, plus one `search-posts`):

| Company | Workflow | Result |
|---|---|---|
| Arcca | wf-fa958b83-a03d-4992-8314-48336db0df1d | "Grupo Arcca", Rio de Janeiro, RJ (used for HQ) |
| Hashdex | wf-1600ecd7-123b-4bcb-a172-3eca4bd93271 | page `hashdex`, New York |
| Isa Health | wf-7ee6df47-f27e-4ede-a6c3-ad54187c2199 | namesakes only (Isa Saúde not returned) |
| Lexter | wf-8867766f-3588-4b07-960e-dfd7bf98d1b8 | `lexter-ai`, São Paulo |
| Lexter (`search-posts "Lexter" --mentioning "Norte Ventures"`) | wf-a49ddf4e-e94b-4169-8729-5b95d74c9372 | `[]` |
| Winnin | wf-575e2689-e5c8-4ce2-9356-d143e7fb4c22 | page `winnin`, New York (registry says Rio) |
| Alude | wf-25cb362b-8e78-4f55-8134-74d5ed166744 | `aludealugueldescomplicado`, São Paulo |
| Cannect | wf-6f6f6203-19e0-4022-a894-0cbc2f9d2e3d | `cannect-saude`, São Paulo |
| Gabriel | wf-3c95190b-1920-4a67-af80-07145778dfc3 | `eusouagabriel`, São Paulo |

No workflow used more than 2 per company. Registry (minhareceita.org, cited as the BrasilAPI URL): Arcca (45.998.376/0001-75), Winnin (21.464.289/0001-70), Alude (32.098.856/0001-38). Hashdex, Isa Health, Lexter, Cannect and Gabriel: no CNPJ found on the pages read, so no registry.

## Arcca Franquias
Reads: arcca.io (home, sobre-nos), Giro News (Tapí kiosk, 2026-03-20), Portal do Franchising (Amélie), Giro News (ABF 2025 figures), registry. Fields filled: description, long description, sub-sector, HQ, year, status, business model, founder (registry only, low), market, 6 milestones, thesis. **No Round**: three web searches found nothing about a round, investors or founders; Norte appears in the owner's portfolio only. Gaps: founders (only a registry administrator since 2022-04-12, Renata Pessoa Silva), investor, round, revenue. Likely cause: a holding with press coverage only of its brands. Leads: none.

## Hashdex
Reads: hashdex.com, Brazil Journal (Series A), Startups.com.br, Finsiders, Forbes Brasil, InfoMoney (history), Wedbush copy of the 2026-03-05 release, Decrypt (2023), InvesTalk (Receita crypto volume). Round: Series A 2021, R$135M (Forbes, Finsiders) = US$26M (Brazil Journal); **Norte `TRUE`** from Brazil Journal and InfoMoney, while Forbes, Finsiders and Startups.com.br omit Norte and write "Endeavor Catalyst". Gaps: the 2018 seed (Dealroom and CB Insights, unreadable), HQ (LinkedIn New York, press dateline "New York / Rio / London"). Third founder Thiago Costa from InfoMoney only (low). Leads: Aug 2026 closing of two European ETPs and ~US$1B AUM (cryptojobslist summary), the 2025 US launch of NCIQ (summary only).

## Isa Health
Reads: isasaude.com (no text without JavaScript), Bloomberg Línea, Brazil Journal (2021), Startups.com.br (2022), NeoFeed (2022), Saúde Business, IFC interview, ANS panel via Istoé Dinheiro. Rounds: 2021 R$13M (typed `seed`; Brazil Journal calls it Series A), **Norte `TRUE`**; 2022 R$60M + R$30M = R$90M Series A, UNKNOWN; 2025 R$160M Series B, UNKNOWN (existing investors unnamed). Founding year conflicts (2017, 2018, 2019, 2020): 2017 kept. Gaps: CNPJ, registry, exact HQ.

## Lexter
Reads: lexter.ai, Startups.com.br and Startupi (2024), Mobile Time (2023), YC profile, Stanford TechIndex, Advbox, OAB-SP. Rounds: 2022 pre-seed (US$500K per Startups.com.br; Caplight says US$1.5M; the same article also says a US$1M YC pre-seed), UNKNOWN; 2024 R$16M, **`FALSE`** (two articles list the same four investors; Parsers and VC Backed list Norte, unreadable). Linked API `search-posts` with Norte: `[]`. Leads: the five other partners in the 2024 photo caption (Guilherme Delai, Pedro Calderón, Lucas Kawazoi, Daniela Labella, Jean Peguim) are "sócios", not confirmed founders; a later Exame piece (~200 customers, revenue x3 in 2023) came only through a search summary.

## Winnin
Reads: winnin.com, NeoFeed (2020 and 2024), Startups.com.br (2024 and 2026), Startupi, Jornal do Comércio, InfoMoney (2024), TheSaaSNews, company blog, dentsu (ad spend), registry. Round: 2024 Series A (amount undisclosed), UNKNOWN. **Earlier rounds are undated** (Coca-Cola seed; ZX Ventures and Dynamo founders as individuals in a later round, US$8M total by 2020): no row, since a Round needs a year. Norte appears only in a CB Insights summary. HQ: registry Rio de Janeiro (Estimated) vs LinkedIn New York.

## Alude
Reads: alude.com.br, Startupi, Distrito, Contxto, Cofeci/DataZAP survey via Paraíba Business, registry. Round: 2020 seed US$3.3M, UNKNOWN (partial list). No later round found in four searches; CB Insights calls the 2020 round Series A (not opened). Note: results for "Alude" mix with CredAluga (a different company, researched in an earlier Batch).

## Cannect
Reads: cannect.com.br, NeoFeed (2021, 2023), Startups.com.br (2024), Exame (2026-08-03). Rounds: 2021 angel (R$1.5M+, our dating), 2022 seed (R$10M+), 2023 institutional (undisclosed, `unknown`), 2024 R$5M media-for-equity; Norte `UNKNOWN` ×3, `FALSE` ×1. VC Backed lists Norte for a July 2023 seed (aggregator, unreadable): lead only.

## Gabriel
Reads: gabriel.com.br, Startupi and Brazil Journal (2021), Startups.com.br (2021, 2026), Brazil Journal (2024, 2026), Baguete (2026), InvestNews and Monitor Mercantil (Abese). Rounds: 2021 R$66M Series A (**Norte `TRUE`**, two readable articles), 2024 R$35M extension (UNKNOWN: list names only the leads and Globo), debt R$25M Itaú (2025) and R$20M Desenvolve SP (2026, `size_usd` empty until the 2026 BRL average exists). The company says it raised R$150M in equity since 2021, which leaves about R$49M unaccounted for beyond the two known equity rounds: possibly an undisclosed round; no row.

## Open questions
- Winnin's early rounds and Norte's role; Arcca's investor; Alude's later history.
- Hashdex HQ and the 2018 seed; Isa Health's registry.
- The 2026 BRL average (Gabriel debt).
