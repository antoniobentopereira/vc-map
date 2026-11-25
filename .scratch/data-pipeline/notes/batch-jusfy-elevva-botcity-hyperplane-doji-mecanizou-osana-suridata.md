# Batch 7 (2026-11-24): Jusfy, Elevva, BotCity, Hyperplane, Doji, Mecanizou, Osana Salud, Suridata

Rows written to `data/` for all eight, `researched_on` set, `python scripts/check_data.py` and `python -m unittest discover -s tests` pass. Norte count over the 15 Rounds: TRUE 7 (Jusfy 2, Elevva, BotCity, Hyperplane, Doji 2), FALSE 2 (Mecanizou Series A, Osana Series A), UNKNOWN 6 (Jusfy 2026, BotCity 2025, Doji 2021 pre-seed and 2023, Mecanizou seed, Osana seed). Suridata has no Round.

Linked API (all through `scripts/linkedin.py`, the account's own LinkedIn): one script, eight `search-companies` runs by name alone, then extra workflows for Mecanizou and Suridata.

| Company | Workflow | Result |
|---|---|---|
| Jusfy | wf-5d4b04ed-73fc-4cc3-91f5-74fead30eb1e | page `jusfy`, location "Brasil" only (not used for HQ) |
| Elevva | wf-19792fd4-2c1b-40aa-ae41-9836a7f79d4b | five namesakes; `elevvalatam` (linked from elevva.co) is Capital Federal, so Buenos Aires |
| BotCity | wf-f0354490-fef6-45f2-b410-c37550d44a34 | page `botcity`, San Francisco (a US presence; HQ is Campinas) |
| Hyperplane | wf-b80cdf89-5d08-45c6-8fd9-0cd569b15576 | "Hyperplane (acquired by nubank)", Palo Alto |
| Doji | wf-42d8d9d2-399c-4312-95a2-98dde0e5b999 | page `doji`, São Paulo, SP |
| Mecanizou | wf-b8a98c69-01fb-4121-b978-8a80b1580c93 | page `mecanizou`, São Paulo |
| Osana Salud | wf-b3dd4e55-cc7d-4006-8820-846f5874dfb8 | `[]` |
| Suridata | wf-2e8e6782-bde9-4df7-a63d-44ea93bd8790 | page `suridata`, São Paulo (plus a Tel Aviv namesake) |
| Mecanizou `search-posts ... --mentioning "Norte Ventures"` | wf-a6e1e43c-274e-4d4f-bce9-d17a4ba1b0a0 | `[]` |
| Suridata `founders` and `search-posts` (script `li3.sh`) | not printed yet when this note was written | see "Leads" under Suridata |

## Jusfy

- **Reads:** jusfy.com.br home; Brazil Journal (2025-03-05); Startups.com.br (seed 2022-12-20, CPTO 2025-03-21, fintech 2025-08-08, JusGPT 2026-03-06, Series A 2026-07-22); Baguete (2022-12-20, 2026-07-22); Startupi (2025-03-07); Advbox (OAB register); minhareceita (Jusfy Serviços de Internet Ltda, opened 2021-01-26, Santa Maria RS; partner Jusfy LLC from 2023-01-11, administrator Rafael Saccol Bagolin). CNPJ came from a web search summary and was checked in the registry, since the site carries none.
- **Rounds:** 2022 seed R$7M (TRUE), 2025 pre-Series A (size undisclosed, valuation about US$30M, TRUE), 2026 Series A US$15M (UNKNOWN: "fundos como").
- **Conflicts:** founded 2020 (Baguete) vs 2021 (registry, Brazil Journal, Startups.com.br): 2021. HQ São Paulo (press) vs Santa Maria (registry): São Paulo. 2025 lead: SaaSholic and MAYA co-lead (Brazil Journal), MAYA (Startupi). R$7M vs US$1.3M for the seed: BRL kept.
- **Gaps:** Cristian Bastianello is a founder from one article only; current prices of the three plans; Jusfy Pay launch month.
- **Not used:** Clio valuation (BetaKit, AOL and Bloomberg unreadable); OAB-RJ resolution (headline only); Dealroom, CB Insights, Seedtable, LatamList.

## Elevva

- **Reads:** elevva.co (home, /quienes-somos, /que-hacemos); Forbes Argentina, El Referente and Startups.com.br (seed, May 2022); La República (Colombia launch, 2021-12-15); La Nación (2026-01-07) and CNN Chile (2025-11-24) on BodyTrainer; Revista Mercado (CACE 2025); CNBC (Thrasio).
- **Rounds:** 2022 seed US$30M (TRUE, Norte named by Forbes Argentina, El Referente and Startups.com.br, which headlines "Norte").
- **Conflicts:** CB Insights US$34M total vs US$30M (aggregator, not used).
- **Gaps:** revenue, brands acquired, current headcount, any later round, CNPJ or Argentine registry (not tried); city of HQ rests on LinkedIn page location. Mexico and "about 10 brands, 80 to 100 staff" appeared only in a search summary (leads).
- **Note for readers:** the BodyTrainer dispute is in the long description and one milestone, told from the parties' accounts as the press reports them (Elevva denies fraud, has appealed the arbitral award).

## BotCity

- **Reads:** botcity.dev home and privacy policy; Startups.com.br (seed 2021-12-16, Series A 2025-09-25); Bloomberg Línea and Forbes Brasil (2021-12-17); IT Forum interview; Y Combinator profile (Winter 2022, Campinas, founded 2020); StartupHub; diginomica (UiPath ARR); minhareceita (BotCity Desenvolvimento de Sistemas Ltda, opened 2018-05-25, administrators Caproni and Archanjo since 2020-06-16, partner BotCity LLC from 2021-11-18).
- **Rounds:** 2021 seed R$15M (TRUE), 2025 Series A R$65M (UNKNOWN: "investidores como").
- **Conflicts:** founded 2018 (registry, Preqin) vs 2020 (Forbes, YC, IT Forum): 2020. StartupHub says the seed was extended by US$500K from YC (US$3M total) in September 2025, the same day as the Series A, so it was not written as a Round.
- **Gaps:** revenue and customer count; whether Sentinel (2025 press) and Sprav (site) are the same product (assumed).
- **Not used:** UiPath's own results pages (StockTitan, Business Wire unreadable; diginomica used); Preqin, CB Insights.

## Hyperplane

- **Reads:** Nubank press release (2024-06-26, also served at hyperplane.ai); Maginative (2023-12-13); Startups.com.br (2023-12-14, 2024-06-26); Brazil Journal (2024-06-26); Yahoo copy of TechCrunch; Nubank engineering blog (2025-06-11). TechCrunch itself was blocked by Cloudflare.
- **Rounds:** 2023 seed US$6M (TRUE: Maginative and Startups.com.br list Norte; Brazil Journal and the Yahoo copy of TechCrunch's acquisition piece list the same investors without it).
- **Conflicts:** founded 2022 (Nubank, TechCrunch, Brazil Journal) vs 2021 (Startups.com.br): 2022. HQ San Francisco (TechCrunch, Maginative) vs Palo Alto (LinkedIn): San Francisco. Acquisition announced 2024-06-26, "July 2024" in Nubank's blog: 2024.
- **Status:** `closed` is our inference (brand discontinued: hyperplane.ai serves Nubank's release, LinkedIn page renamed "acquired by nubank"). The owner may prefer `active` under the rule for acquired companies that keep operating; the sources read say the team works inside Nubank.
- **Gaps:** price (undisclosed; Startups.com.br's sources say share swap); Norte's return.

## Doji

- **Reads:** doji.com.br (doji.co returned nothing); Bloomberg Línea and Startupi (2021-11-08); Startups Magazine (2022-01-25); Baguete (2023-08-11, 2023-10-26, 2025-11-18); Brazil Journal (2025-11-17); PEGN copy at Fusões & Aquisições (2025-06-25); Startupi (2025-11-27); Tecnoblog (Abinee/IDC figures). No registry (Doji Brasil Ltda CNPJ not found).
- **Rounds:** 2021 pre-seed US$800K (UNKNOWN, year is the article's), 2021 seed US$3M (TRUE), 2023 RBS Ventures undisclosed (UNKNOWN, type `unknown`), 2025 R$13M in two tranches (TRUE, from PEGN).
- **Conflicts:** founded January 2020 (Startups Magazine) vs 2021 (Startupi, Baguete, Brazil Journal): 2021. The June 2025 tranche's investors: Brazil Journal and Baguete omit Norte and Raio Capital, PEGN includes them; TRUE kept because a Source names Norte. The first tranche is R$10M (Baguete, Brazil Journal) or US$2M / R$11M (PEGN).
- **Gaps:** CNPJ and registry; the date of the US$800K pre-seed; Norte's role in the 2023 and November 2025 rounds.

## Mecanizou

- **Reads:** mecanizou.com home; Startups.com.br (Series A 2023-03-22, CTO 2024-06-27); Startupi (2023-03-21); Bloomberg Línea (2023-03-24); LAVCA (2023-03-21); Convergência Digital (2024-02-20); Startups.com.br tag page. TechCrunch blocked.
- **Rounds:** 2022 seed US$4M (UNKNOWN: no page lists the whole group), 2023 Series A US$14.5M (FALSE: four articles list Monashees, Alexia, FJ Labs and Dalus without Norte).
- **Conflicts:** seed in January (press) vs February 2022 (LAVCA); seed lead Alexia (LAVCA) vs Monashees, Alexia and H2O Capital (Convergência Digital). `search-posts ... --mentioning "Norte Ventures"` found nothing. VC Backed lists Norte (aggregator, not read).
- **Gaps:** CNPJ and registry (not on the site, search found only namesakes); anything after June 2024; Norte's participation at all; founding year is our estimate (2021).

## Osana Salud

- **Reads:** LAVCA (copy of TechCrunch), El Referente, DPL News (2021); Forbes Argentina, iProfesional (2022); Infomercado (2022-09-15); Mercado (Sadosky, 2022-12-01); osanasalud.com (Framer page published 2026-02-20; text not extractable, meta description only). WEF, yespress and Dealroom pages unreadable.
- **Rounds:** 2021 seed (no amount: about US$6.5M by subtraction, UNKNOWN; Dealroom lists Norte), 2021 Series A US$20M (FALSE: LAVCA/TechCrunch list General Catalyst, Quiet, Preface, FJ Labs, AforeVC, K50 and Addition).
- **Gaps:** HQ city (Buenos Aires assumed); anything after 2022 (WEF Technology Pioneer 2023, Edison Alliance and HEAL appeared only in search summaries: leads); revenue; Linked API found no page (`[]`). The iProfesional page shows a "24/7/2026" header but its text and `published_time` are 2022.

## Suridata

- **Reads:** suridata.com.br home, /sobre, /solucoes, /cases, /blog, /ferramentas/suri-gestao, /politica-de-privacidade (CNPJ 31.937.540/0001-20); minhareceita (Suridata Tecnologia Ltda, opened 2018-11-05, São Paulo; administrators Vagner Pinheiro de Assis since opening and Daniel Sobral Barra since 2021-06-02); Jornal de Brasília and Monitor Mercantil (ANS collective-plan adjustments).
- **Rounds:** none written. CB Insights (search summary) lists Norte Ventures and AlperTech in an "incubator/accelerator" round on 2023-08-28; no readable page.
- **Leads to verify:** Vagner Pinheiro de Assis as founder (registry only, so `founder` Estimated with Confidence low); Linked API `founders` for the company page and `search-posts "Suridata" --mentioning "Norte Ventures"` were started in the background (script `li3.sh`) and had not returned when this note was written; if they return, fetch with `result <workflow-id>` and add what they show.
- **Gaps:** founders' names and roles from any press; any round; customers count; `hq_at_first_investment` left out (Norte's first investment unconfirmed); market size.

## Lessons for the recipe

See `docs/research-recipe.md`, "Lessons from Batch 7".
