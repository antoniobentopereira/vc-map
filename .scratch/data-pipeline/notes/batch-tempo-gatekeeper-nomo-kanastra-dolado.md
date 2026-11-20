# Batch: Tempo, Gatekeeper, Nomo, Kanastra, Dolado (2026-11-20)

Five companies chosen in file order from `data/companies.csv` (empty `researched_on`, no claims). Researched one at a time; `python scripts/check_data.py` passed after each; unit tests pass (107). The skill was renamed from `research-batch` to `research-companies` at the start of this run (folder, `name:` in SKILL.md, AGENTS.md, ADRs 0012 and 0013).

Reading was done with a plain HTTP fetch (text-stripped) and web searches; the fetch subagent was used for two homepages only. Search summaries were used as leads, never as Sources.

## Summary

| Company | Rounds | Norte TRUE / FALSE / UNKNOWN | Milestones | Linked API workflows |
|---|---|---|---|---|
| Tempo | 1 (2025 seed, US$4.5M) | 1 / 0 / 0 | 5 | 3 |
| Gatekeeper | 1 (2026 strategic, undisclosed) | 0 / 0 / 1 | 6 | 3 |
| Nomo | 1 (2021, ~R$14M) | 1 / 0 / 0 | 8 | 3 |
| Kanastra | 4 (seed, A, Itau stake, B) | 1 / 0 / 3 | 7 | 1 |
| Dolado | 2 (2020 seed, 2022 A) | 1 / 1 / 0 | 6 | 2 |
| **Total** | 9 | **4 / 1 / 5** | 32 | 12 |

## Tempo

- Reads: Startups.com.br 2025-04-02 (round), Brazil Journal 2025-02-11, Maya Capital post, Norte Manifesto. Not readable: seutempo.com (403 on every path and through the fetch agent). Baguete article about "Tempo" is a different company (insurance assistance).
- Linked API: `search-companies` wf-db5593a3-3a1d-4783-975f-1cec747ec5b2 (empty); `company ... --posts 20` wf-bf51469d-839b-431b-bc41-fa815b1d3149 (page exists, no HQ, no year, no posts); `founders` was rejected by Linked API (`invalidWorkflow`, duplicate `st.openCompanyPage` in `then`), no workflow id.
- Filled: description, long description, thesis, sub-sector, year founded (2024, estimated), status (active, low), business model, founders, market, 5 milestones, 1 Round.
- Gaps: HQ, HQ at first investment, CNPJ and legal name (site unreadable, registry number not found), later news after April 2025. Likely cause: Cloudflare-style 403 on the site; the company is young and thinly covered.
- Open point: Maya's first 2024 investment (amount and type unknown) is described in the Round note but has no row.

## Gatekeeper (GatekeeperX)

- Reads: gatekeeperx.com home, /company, a business case; Enter.co 2026-07-01 interview; Impactotic interview; Latam Fintech Hub 2026-01-15 and 2026-05-08; Colombia Fintech press release 2026-05-07; Ecosistema Startup 2026-10-10 and 2025-12-09. Not readable: Portafolio (connection reset), Startup Researcher (429), colombiaone (certificate).
- Linked API: `search-companies` wf-7142a5f3-9a37-41f3-b067-2a3607b19cdb; `company ... --posts 20` wf-4be08b51-e7c2-4837-9b3b-4aee36d79c14 (28 employees, posts to 2026-11-19, no HQ); `search-posts "GatekeeperX" --mentioning "Norte Ventures"` wf-104222d6-b4c5-47f7-bc75-663164517ed9 (one post, 2026-05-06, says the company "already had" Norte's backing).
- Filled: description, long description, thesis, sub-sector (new: Fraud prevention and AML platform), HQ (Bogota, estimated low, from a press-release dateline), year founded (2025, estimated), status, business model, 4 founders (medium: the company page lists four leaders and two interviews say four ex-Rappi colleagues started it), markets (Colombia, Brazil), 6 milestones, 1 Round.
- Gaps: Norte's own Round (listed as an existing backer in May 2026 but no read page dates or sizes it; an aggregator snippet dating an early-stage deal to May 2025 was not read), HQ at first investment, which five countries it operates in. Norte is UNKNOWN for the 2026 Round.

## Nomo

- Reads: Startupi 2021-11-11 (round, names Norte), Brazil Journal 2021-11-11, Consumidor Moderno 2023-02-13, Brazil Journal and Fusoes & Aquisicoes 2024-01-02 (Bemobi), Mobile Time 2025-04-23, 2025-05-21 and 2025-12-05, Kamelo interview 2022-10-17. nomo.com.br is script-rendered (title only). Not readable: The Latin American Lawyer (403).
- Linked API: `search-companies "Wave Nomo telecom Henrique Garrido"` wf-e2a6105e-9271-485f-a1f6-03221fbe88d8 (empty); `search-companies "Nomo operadora digital"` wf-04cfa90c-1e2c-4099-ad6e-f4ef71a14805; `company https://www.linkedin.com/company/nomotelecom --posts 20` wf-15b98a57-d5ac-442b-ae56-055c3cdf050e (Sao Paulo, 5 employees, posts to 2026-01-01).
- Filled: all single-value fields except CNPJ-based ones; acquirer Bemobi 2024 (51% of Wave Tech, the B2B company; the consumer brand is now controlled by Algar, no Source for that transaction); 4 founders; markets Brazil, Mexico, Colombia, Chile; 8 milestones.
- Gaps: CNPJ and legal name (a search snippet named "200 Tech Servicos do Brasil" and a Wave Tech do Brasil S.A. formed 2022-11-30 in Rio; neither page was read), when Algar took control of the consumer brand, round type for 2021 (`unknown`).

## Kanastra

- Reads: Brazil Journal 2023-06-14 (seed, names Norte Ventures), 2024-06-05 (Series A), 2025-10-01 (Series B); Startups.com.br 2024-06 and 2025-10-01; Baguete 2025-01-31 (Itau). kanastra.com.br is script-rendered.
- Linked API: `company https://www.linkedin.com/company/kanastra --posts 20` wf-f988d5a0-e669-4010-a005-27ff9732bb22 (Uberlandia, 224 employees, posts to 2026-10-20).
- Filled: everything except CNPJ; 4 Rounds; 7 milestones.
- Norte: TRUE for the 2023 seed only. The Series A ("all previous investors"), the Itau stake and the Series B list partial investors without Norte, so UNKNOWN. A later look at a fuller cap-table source (Kaszek's portfolio page, Series B press kit) could settle them.
- Gaps: CNPJ (search found sister entities such as Kanastra Securitizadora S.A. but not the operating company), HQ at first investment (estimated low). One outlet dates the seed 2022 and R$13M; discarded in favour of June 2023 and US$13M.

## Dolado

- Reads: Startupi 2020-12-09 (seed, names "Norte Capital"), NeoFeed 2020-12-09, Startups.com.br 2022-04-06 (Series A), Bloomberg Linea 2022-04-06, NeoFeed 2022-04-06, NeoFeed 2024-12-13 (standfirst only). dolado.com.br renders nothing without JavaScript (fetch agent got 8 characters).
- Linked API: `search-companies` wf-12030aca-ebd2-4213-b2b8-1816fd503bc8 (empty); `company https://www.linkedin.com/company/dolado --posts 20` wf-0fe68dc9-9bcc-4e76-b088-ed49ebdd0081 (Sao Paulo, 68 employees, posts to 2026-10-21; current description is a marketplace-seller accelerator).
- Filled: all single-value fields except CNPJ; 3 founders; 2 Rounds; 6 milestones.
- Norte: seed TRUE (Source writes "Norte Capital"; identity with Norte is our judgement, medium confidence). Series A FALSE: three outlets list the same participants without Norte; the lists may omit small existing investors.
- Gaps: when and why Dolado changed from small-shop restocking to marketplace sellers, current revenue and customers, any round after 2022 (a search summary mentioned "R$70 million from Valor Capital" on the company site; it could not be verified and was not used), CNPJ. My first search used a wrong guess ("tax intelligence"); the search results corrected it.

## Process notes and recipe lessons

- A script slip wrote Dolado's rows once with claims I had decided to cut (a 100,000-merchant goal I had only seen in a search summary). The rows were removed, the script fixed and re-run; the final data contains only claims from read pages. Lesson: run the row-writing script only after confirming the edit step succeeded (do not chain it after an edit with `&&` when the edit can fail silently).
- `python scripts/linkedin.py founders <company-url>` fails with `invalidWorkflow` (duplicate action type in the `then` array); fix the script before relying on it. `search-companies` returned empty results for 4 of 6 queries; passing the likely company URL to `company` worked every time and is cheaper.
- Script-rendered sites (nomo, kanastra, dolado) and 403 sites (seutempo) gave nothing; for four of five companies the Round articles carried most facts. Recipe step 1 should say: when the site has no text, go straight to press and Linked API.
- Press often writes "Norte Capital" for Norte Ventures (Dolado 2020 and 2022); worth stating in the recipe.
- Linked API posts are a good, current source for `status`, milestones in the last year and HQ (`location`); the `headquarters` field returned only "BR".
