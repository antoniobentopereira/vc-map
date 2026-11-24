# Batch 5 (2026-11-24): Patagon AI, Backchannel, Igual, 180° Insurance, Henry, Salu, Vaas, Refer

Eight companies, in file order, one at a time. Norte's Manifesto re-read 2026-11-24 (unchanged). `python scripts/check_data.py` passes and `python -m unittest discover -s tests` passes (107 tests). Tools: plain page reads (`curl --compressed` plus a text extractor), web search, minhareceita.org for the registry (BrasilAPI URL cited), Linked API for 8 workflows in total (Igual used 2).

## Norte counts (rounds written)

| Company | TRUE | FALSE | UNKNOWN | Rounds |
|---|---|---|---|---|
| Patagon AI | 1 | 0 | 1 | 2 |
| Backchannel | 2 | 0 | 0 | 2 |
| Igual | 0 | 0 | 0 | 0 |
| 180° Insurance | 2 | 1 | 2 | 5 (one is debt) |
| Henry | 0 | 1 | 2 | 3 |
| Salu | 1 | 0 | 0 | 1 |
| Vaas | 0 | 1 | 0 | 1 |
| Refer | 1 | 0 | 0 | 1 (single-source TRUE, Confidence low) |

Main gaps: Igual has no readable round or founder; Henry and Vaas have no round with Norte `TRUE` (the company's own investor lists leave Norte out of Vaas's seed, and Forbes Argentina's full list leaves it out of Henry's Series A); Refer's Norte comes from one Spanish blog.

## Patagon AI

- **Reads:** patagon.ai home; Brazil Journal (2025-11-04); Baguete (2025-11-05); iProUP; Contxto (2024-11-27); La Nota Económica; Forbes Argentina; Kfund post; LatamList.
- **Linked API:** `search-companies "Patagon AI"` wf-c6f3c7b1-119b-45e8-b7ac-fa4196f25ee1 (Buenos Aires, confirms HQ).
- **Rounds:** 2024 pre-seed US$1.1M (OneVC, 17Sigma; Norte UNKNOWN: Brazil Journal says Norte was already in the cap table before the seed), 2025 seed R$15M (Kfund lead; Norte TRUE, Brazil Journal names it).
- **Gaps:** month of founding; country list; revenue after October 2025; date of the Attribution product. Market size not found (bottom-up in the thesis). Primicias.ec and the Forbes Argentina 2.75M page did not render usable text.

## Backchannel

- **Reads:** startups.com.br (2026-03-23); Bloomberg Línea; Accion release (2026-03-23); LatamList; Brazil Journal (2025-06-26); startups.com.br column on overstock; iProUP (rejected: describes a factoring platform, nothing like the other sources).
- **Linked API:** `search-companies "Backchannel"` wf-27d9db4a-d79d-498f-8f25-fefe5aadbc04 (São Paulo; two namesakes returned).
- **Rounds:** 2024 pre-seed R$17M (Cathay Latam lead; Norte TRUE, Brazil Journal), 2026 seed R$25M (Sunna lead; Norte TRUE). Seed `size_usd` empty: the 2026 BRL average is not in `fx.csv`.
- **Conflicts:** Bloomberg Línea dates the pre-seed October 2025, three sources say October 2024 (kept). Accion lists "SC Latam Innovation Fund" where others list Cathay Latam.
- **Gaps:** CNPJ (a Nuvemshop listing names BACKCHANNEL SOLUCOES DE INVENTARIO LTDA only); exact founding month; current GMV beyond company goals.

## Igual

- **Reads:** igual.com (a single page for every path: products, job posts, no About or founders); Stanford CodeX TechIndex (founded 2024, Curitiba, law firms, subscription); StartupsBR. A first web search assumed an "equal pay" product and returned noise: the recipe's "read the company's site before searching by sector" applies.
- **Linked API:** `search-companies "Igual"` wf-8cc447ac-92af-470e-ab08-f50b787f7c6f (found "igual", Curitiba, `igualparatodos`); `founders https://www.linkedin.com/company/igualparatodos` wf-c2bef45a-4001-4e2d-a21c-36c1a7d9fe0b failed with `unexpectedError` (`st.openCompanyPage`) after more than 30 minutes.
- **Fields filled:** description, long description (short), thesis (low), sub-sector, HQ, year, status, model, market, one milestone. No founders, no rounds.
- **Leads to verify:** CB Insights lists a seed of about US$2M with Norte, BFF Ventures, Honey Island Capital, 1616 Ventures and 4UM Investments; another directory lists a 2024 pre-seed with Norte (aggregators, unreadable, no year for the seed). The 2022 Startupi article on Zeno (Curitiba) is a different company.

## 180° Insurance

- **Reads:** 180s.com.br (footer: CNPJ 39.999.619/0001-97, Pinheiros); NeoFeed (seed 2021-05-05, Series A 2022-02-02); Startups.com.br (seed; pre-Series B 2025-09-04; Vivo Ventures 2025-10-23); Bloomberg Línea (2022-02-02); Brazil Journal (valuation R$1.35B); Forbes Collab (sponsored; used only for the founding month); minhareceita (180 SEGUROS S.A., active since 2020-12-03).
- **Linked API:** none (not needed).
- **Rounds:** 2021 seed R$44M (Norte TRUE, NeoFeed); 2022 Series A US$31.4M (Norte TRUE); 2025 pre-Series B R$35M equity, recorded as `series_a` because the sources call it pre-Series B (Norte UNKNOWN: only the leaders and FJ Labs named); R$15M subordinated debt; Vivo Ventures US$2.5M extension (type `unknown`, Norte FALSE: Vivo alone).
- **Conflicts:** Forbes Collab dates the seed October 2020 (discarded). The Series A is kept in USD because R$177M converted at the 2022 average would give US$34M, not the announced 31.4M.
- **Gaps:** the 2026 Series B (planned for H1 2026; none found); date of the Susep insurer licence; Alex Körner's departure date (only a headline about Dobbra.ai).

## Henry

- **Reads:** soyhenry.com and /nosotros; Y Combinator profile (Summer 2020, Buenos Aires, 100 people, founded 2019); Accion seed release; Yahoo copy of TechCrunch (seed; TechCrunch itself returned a Cloudflare block); Forbes Argentina and Bloomberg Línea (Series A); Diario Financiero; Forbes Colombia; Mercado.com.ar. El Cronista (pre-seed) returned only a paywall.
- **Linked API:** `search-companies "soyHenry"` wf-c75866d4-3825-45ba-a59a-b0b523c0ab7c returned the page `school/henryok` (Buenos Aires, CABA), which agrees with the Y Combinator HQ; not added as a second Source.
- **Rounds:** 2020 pre-seed US$300K (our arithmetic: Forbes Colombia says US$1.8M in two rounds; Norte UNKNOWN), 2020 seed US$1.5M (Norte UNKNOWN: unnamed angels), 2022 Series A US$10M (Norte FALSE: Forbes Argentina lists every investor). CB Insights lists Norte in the Series A: an aggregator, not used.
- **Gaps:** where and when Norte invested (nothing readable); revenue after 2022 (a search summary of Forbes Argentina gave US$3.3M for 2022, page unread); the founding group differs between sources (Federico Hernández in Diario Financiero, Antonio Tralice in TechCrunch). Tralice stays a lead.

## Salu

- **Reads:** salu.com.vc (CNPJ in the footer); Brazil Journal (seed 2022-03-29; acquisition 2026-06); Startups.com.br (2022-03-29, 2022-09-15, 2026-06-10); Senior's notice via Finance News; minhareceita (SAUDE DIGITAL, TECNOLOGIA E CONSULTORIA S.A., active since 2020-02-28, Senior executives as administrators since 2026-09-04).
- **Linked API:** `search-companies "Salú"` wf-a564ddc3-903b-4caa-bd05-2a9074b68b33 (São Paulo).
- **Rounds:** 2022 seed R$12M (SoftBank lead; Norte TRUE: Brazil Journal writes "Norte Ventures", Startups.com.br "Norte Capital").
- **Acquisition:** Senior Sistemas, R$318.7M, announced 2026-06-10, subject to Cade; the registry change of 2026-09-04 suggests it closed (our reading).
- **Gaps:** the closing date; Irineu Massaia as a fourth founder (Startups.com.br wording is ambiguous, so he is a lead); Norte's stake and return.

## Vaas

- **Reads:** getvaas.com home (empty without JavaScript) and /en/about-us; the company's seed blog post (full investor list); Forbes Colombia; LatamList; Gunderson Dettmer; Valora Analitik; 30N Ventures post; The Bogota Post; La Frontera podcast page.
- **Linked API:** `search-companies "Vaas"` wf-a4a7d9f5-33fc-4551-9bcf-8d9974967239 (the Vaas page `get-vaas` returned no location; the other results were namesakes), so HQ stays missing.
- **Rounds:** 2023 seed US$5M (a16z lead; Norte FALSE: the company's own post lists every investor).
- **Gaps:** HQ (the founder is from Cali; no source states the company's base); a 30N Ventures investment of unknown size and date; any later round, where Norte might sit; undated timeline items on the company page.

## Refer (Cardinal Refer)

- **Reads:** cardinalrefer.com home and /about; Ecosistema Startup (2026-07-30); Staffing Industry Analysts; Runtime Wire (Business Insider summary); KMPH; Startup Researcher. dnyuz.com returned unrelated content.
- **Linked API:** `search-companies "Refer Lia AI career agent"` wf-50881706-545f-434b-ac66-ae51854ccdfa returned `[]`.
- **Rounds:** 2026 seed US$7.5M (Canary lead). Norte `TRUE` only from the Ecosistema Startup blog (Confidence low); the earlier US$2.5M round has no date or readable investor list and is not recorded.
- **Gaps:** co-founders (none named); date and investors of the first round; HQ (Palo Alto on the company's pages, San Francisco in the press).

## Leads still unverified

Igual founders and its rounds (CB Insights, directories); Henry's Norte role; Refer's earlier US$2.5M round; Vaas's later rounds and HQ; Salu's Irineu Massaia; Henry's Antonio Tralice.
