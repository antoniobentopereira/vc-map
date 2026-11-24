# Batch 2026-11-24 (second): Kovi, Nekt, Liti, Alchemy, Null Platform, ComunicaIn, Kamino, Ximple

Researched in file order of `data/companies.csv` (the first 8 without `researched_on`). Each company has description, long description, investment thesis, sub-sector, status, business model, founders (where readable), markets, milestones and Rounds. `check_data.py` and the unit tests (107) pass.

## Summary

| Company | Rounds | Norte TRUE / FALSE / UNKNOWN | Linked API workflows |
|---|---|---|---|
| Kovi | 3 (seed 2019, US$30M 2019, Series B 2021) | 1 / 0 / 2 | 1 (search-posts, empty) |
| Nekt | 2 (R$5M 2025, Norte R$1.3M 2025) | 1 / 1 / 0 | 0 |
| Liti | 1 (R$21M seed 2022) | 1 / 0 / 0 | 2 (search-companies empty; company failed) |
| Alchemy | 0 | none | 4 (search-companies and person worked; company and founders failed) |
| Null Platform | 0 | none | 2 (search-posts empty; search-companies found the page, location ".") |
| ComunicaIn | 1 (R$10M seed 2021) | 1 / 0 / 0 | 0 |
| Kamino | 2 (US$6.1M pre-seed 2022, R$54M 2025) | 1 / 0 / 1 | 0 |
| Ximple | 1 (US$2.7M pre-seed 2024) | 0 / 0 / 1 | 0 |

## Per company

**Kovi.** Reads: kovi.com.br (home, /sobre-nos), privacy PDF (CNPJ 30.980.329/0001-27; BrasilAPI: opened 2018-07-20, active), Startups.com.br (Series B 2021; Moove deal 2025), Brazil Journal (seed 2019), Contxto (seed), Suno (US$30M round), YC profile, NeoFeed (2022 recalibration); Forbes and Istoé Dinheiro read only as leads. Linked API: `search-posts "Kovi aluguel de carros" --mentioning "Norte Ventures"` wf-1b855452-9042-4d39-bd1a-3c6dbfa39125, completed, no posts. Norte TRUE in the 2021 Series B (Startups.com.br lists "Norte"); the 2019 rounds' investor lists omit Norte but may be partial. Acquired by Moove in 2025 (share deal, undisclosed). Gaps: price of the Moove deal; whether Norte took part in 2019; date of the Zanzar investment; Mexico launch date (planned for end of 2019 per Suno, "eight months" in 2021 per Startups.com.br).

**Nekt.** Reads: nekt.ai, Startups.com.br (R$5M, R$1.3M, Mountain View move), Startupi (R$1.3M), Baguete (R$5M), Jornal do Brás (founder story), LatamList (blank page). The site gives no CNPJ; the search for it returned namesakes. Norte TRUE only for the R$1.3M (Oct 2025); FALSE for the R$5M (Startups.com.br lists the investors without Norte and says Norte joined three months later). Gaps: HQ never stated (Florianópolis inferred, low); the stage of the rounds (pre_seed is our reading from the CEO talking of a coming Seed round). The two 2025 rounds could not both be `pre_seed` (one row per company, year and type), so the Norte round is `unknown`.

**Liti.** Reads: liti.com.br (the home renders only a title; its script `assets/index-*.js` holds the page text and was read), Startups.com.br, InfoMoney, Forbes (2022, front matter only), Bloomberg Línea (2023), LatamList, GPCA, Vitat (2023), Forbes (GLP-1 market, 2026), L.E.K. (market). Exame returned compressed data we could not decode. Linked API: `search-companies "Liti Saúde emagrecimento"` wf-7ae79d8d-3ce4-4b58-acc9-1a55be0d3ddc (empty); `company https://www.linkedin.com/company/litisaude` wf-fa9df6c8-28b5-41e2-b14e-054695f36598 (unexpectedError after about 20 minutes; the slug was a guess). Norte TRUE in the 2022 seed (four outlets). Gaps: HQ and CNPJ not found; no news after 2023, so status active rests on the live site; the earlier Monashees-led round has no amount or date.

**Alchemy.** Reads: usealchemy.io (PT and EN; the site is a single page), its careers site, and the Brazil Journal Brands launch article (sponsored, "2 months ago"), read from a PDF the owner supplied after the first pass, because the page returns only navigation. The PDF gave founders (Fernando Ribeiro CEO, ex-CFO of Pitzi and ex-Bridgewater; Willian Menegali CTO), customers with operations in Brazil, Mexico and the United States, 130 institutions, and the Rillet comparable; the data were rewritten from it (first pass had no founders or markets beyond the site). Linked API: `search-companies "Alchemy ERP AI-native"` wf-e4b3e91f-9351-4a1d-b8fc-7e1e5f90cf68 (found https://www.linkedin.com/company/alchemy-erp, São Paulo); `company` wf-6b1f0868-aec0-4483-add1-9e500668988a and `founders` wf-6250a51f-4d61-4154-b0c2-76bf310db819, both unexpectedError; `person https://www.linkedin.com/in/willianmenegali --experience` wf-b512b075-a89f-40e7-a593-7bf0ea04dd4e (worked: CTO and co-founder at Alchemy ERP from 2026-01, before that co-founder of Alinea Health 2021-08 to 2025-12, Curitiba). That is 4 of 4 workflows. `year_founded` 2026 is Estimated, low, from Menegali's start date. Leads to verify: Ribeiro's LinkedIn profile and start date (a web search did not find its URL; Linked API has no people search); an earlier founding date. Gaps: funding and Norte participation, CNPJ.

**Null Platform.** Reads: nullplatform.io (home, /about-us, /contact-us), iProfesional (2024 interview), Innovación Digital 360 (2024). Round data exist only on aggregators (VCBacked, Crunchbase, Teaser Club, Bouncewatch: pre-seed June 2023, Carao Ventures, 17Sigma, Norte Ventures, about US$1.5M) and all returned 403 or 429, so no Round row. Linked API: `search-posts "nullplatform" --mentioning "Norte Ventures"` wf-76289771-a854-4179-b72c-bc52ac4055e6 (empty, took about 10 minutes); `search-companies "nullplatform"` wf-04b5b357-6a8d-4a99-afa9-72038fb07115 (page found, location "."). Gaps: HQ, the pre-seed Round, CNPJ.

**ComunicaIn.** Reads: comunica.in, its privacy policy (CNPJ 27.119.789/0001-50, Curitiba), BrasilAPI (opened 2017-02-06; administrator Felipe Hotz since 2018-07-10; a foreign LLC partner since 2022-02-16), Startups.com.br, Bloomberg Línea (PT), Startupi (2023). Norte TRUE in the 2021 seed ("Norte Capital" in two outlets, "Norte Ventures" in Startupi). Gaps: co-founders (only Hotz is named); CB Insights lists a Seed II of September 2022 with Norte but could not be read; Bloomberg Línea's English headline says US$2M against R$10M in Portuguese.

**Kamino.** Reads: kamino.com.br (home, /quem-somos/), Startups.com.br (R$54M, 2023 shift to SMEs, 2026 AI), Bloomberg Línea (2022 pre-seed; 2025 round), LatamFintech (2025), Finsiders (2022, front matter only), Flourish job board. No CNPJ found. Norte TRUE in the 2022 pre-seed (Bloomberg Línea). Gaps: about R$22M missing between the stated R$108M total and the two Rounds read; the site calls Juliana Strohl a fifth founder while Bloomberg Línea says she joined later (kept out of `founder`); HQ (São Paulo) only from a job board.

**Ximple.** Reads: ximple.co (home, privacy notice), Contxto, LatamFintech (round and card), LatamList, fintech.global, Venture Capital Mx, Rest of World and Milenio (market). Norte is named nowhere, only on Norte's portfolio page; the 2024 round's investor list is partial, so UNKNOWN. Gaps: VCBacked's December 2025 seed (unreadable); the founders' backgrounds.

## Open questions

- Alchemy and Null Platform have no Rounds and no Norte participation recorded; a readable route to LinkedIn would be needed (`company` and `founders` workflows failed 3 of 3 this Batch).
- Nekt's two 2025 rounds share a year and type; the schema allows one row each, so one carries type `unknown`.

## Leads to verify (kept, not in `data/`)

- Alchemy: Fernando Ribeiro's LinkedIn profile and start date; whether the company existed before 2026.
- Null Platform: pre-seed of June 2023 (about US$1.5M; Carao Ventures, 17Sigma, Norte Ventures) from VCBacked, Crunchbase and Teaser Club snippets; no readable page.
- ComunicaIn: Seed II of September 2022 with Norte (CB Insights snippet).
- Ximple: seed of December 2025 (VCBacked snippet).
- Kamino: the missing about R$22M of the R$108M total.
