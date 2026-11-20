# Batch 2026-11-20: Ume, Nexa, Flash, Syntage, Unxpose

Rows 1 to 5 of the remaining companies in file order (the 11th to 15th researched). All five have `researched_on` 2026-11-20 and `python scripts/check_data.py` passes; unit tests pass (107). Pages were fetched with a small text extractor (stdlib `urllib`), because no WebFetch tool was available; pages that returned 403 (Foley, TechCrunch, LetsMoney) were not cited.

Norte count per company (Rounds): Ume TRUE 1 / UNKNOWN 6; Nexa TRUE 2 / UNKNOWN 1; Flash TRUE 0 / UNKNOWN 5; Syntage TRUE 0 / UNKNOWN 1; Unxpose TRUE 0 / UNKNOWN 1. No FALSE.

## Linked API
| Workflow | Command | Result |
|---|---|---|
| wf-b0382f59-4ed4-43ab-b515-cc178cea646e | `company .../company/ume-fintech` | failed, `unexpectedError` (the slug may be wrong; not retried) |
| wf-2e947809-0028-409b-9969-2f6fdd9b0689 | `search-posts "Flash benefícios" --mentioning "Norte Ventures"` | success, one irrelevant post (a CB Insights roundup); Norte still UNKNOWN |
| wf-908cf622-391d-4fd4-b41e-1cbb5bce812d | `company .../company/syntage --posts 20` | failed, `unexpectedError` (not retried) |
| wf-1074529e-0346-48eb-a05b-83e6461d694a | `search-posts "Unxpose" --mentioning "Norte Ventures"` | success, no posts found (fetched after the Batch with `result`); Norte stays UNKNOWN |

Nexa: no workflow (the press named Norte in the pre-seed and seed). Both `company` workflows (the step 7 command for HQ and founders) failed with the same error, so HQ for Ume and Syntage comes from other pages.

## Ume
Reads: ume.com.br home and /sobre (history, stats), privacy policy (CNPJ 29.311.808/0001-71, Belo Horizonte seat), BrasilAPI registry, Brazil Journal 2022 (seed, origin) and 2024 (Series A), Finsiders 2025 and Bloomberg Línea 2025 (Series B), Bloomberg Línea 2024-11 (CTO and founders), Startups.com.br and Central do Varejo (2026 FIDCs).
Rounds: seed 2022 (Norte TRUE, named by Brazil Journal), debt 2022, Series A 2024, FIDC 2024, Series B 2025, two FIDCs 2026 (BRL 2026 average not in `fx.csv`, so `size_usd` empty).
Gaps: `hq` is the registered seat (Belo Horizonte), `hq_at_first_investment` is a guess (Manaus). Series A and B lists are partial (UNKNOWN). Brazil Journal's 2025 Series A figure (R$81M) came only from a search summary and was ignored. `year_founded` 2017 (site, registry) vs 2019 (press): 2017 kept.

## Nexa
Reads: nexafinance.com.br home (footer address), Brazil Journal and Startups.com.br 2025 (seed), Startups.com.br and Radar 2026 (Genesis), Portal Tela 2025 (token launch; an auto-summarised page, used only for date), BrasilAPI (CNPJ 54.048.859/0001-08, from a search result), bpmoney (adviser counts).
Rounds: pre-seed 2024 (Norte TRUE, only from Startups.com.br's "investor since the pre-seed"; year from aggregators, Confidence low), seed 2025 (TRUE), 2026 round with Valor and Citrino (UNKNOWN).
Gaps: pre-seed amount and investors; Portal Tela's R$20M and R$10M earlier raises (Brainvest, Koli) look like fund or debt money and were not recorded.

## Flash
Reads: flashapp.com.br home and footer (CNPJ 32.223.020/0001-18), BrasilAPI, InfoMoney 2026 (origin), Exame 2020 and 2021 (seed, Series A, traction), Startupi 2021 and Startups.com.br 2022 (Series B, C), Startups.com.br 2022 and 2023 (ExpenseOn, FolhaCerta), Startups.com.br 2024 interview, Bloomberg Línea 2026-05, Startups.com.br 2026-08 (Series D).
Gaps: seed and Series A amounts (about US$9M together in year one, per Exame); Norte not named anywhere (an aggregator lists it in the Series A, which does not make it TRUE). Series D's US$29M figure came from a LinkedIn post summary, so only R$150M is recorded.

## Syntage
Reads: syntage.com home, blog "Hello, we are Syntage" (seed, founders, history), Clara case, QED and Costanoa portfolio pages, Descubre.vc, INEGI census release (PDF read with its text stream).
Gaps: no Mexican registry lookup (not tested before); Costanoa says its first investment was a pre-seed, but no source gives the year, so it is not a Round; Norte appears only in an aggregator. Seed UNKNOWN.

## Unxpose
Reads: unxpose.com home and cases, footer (CNPJ 41.183.306/0001-08), BrasilAPI, Startups.com.br and Canaltech (2021-09-01), Google blog (2025-10-28 cohort), Brasscom via TeleTime.
Gaps: no round size, no further rounds, Norte only in an aggregator (CB Insights, seen only in a search summary); year founded 2021 (registry) vs 2020 (aggregator); the founders Tiago Assumpção and Patrick Costa are named only in a photo caption.

## Cross-company notes
- Brazil Journal and Startups.com.br pages were all readable; Bloomberg Línea pages printed the first part only after the navigation text, so the extractor needs a start marker.
- In all five companies Norte is named in a Round only where one article says so (Ume seed, Nexa pre-seed and seed).
