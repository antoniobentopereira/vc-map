# Search experiment: Norma, Jota HQ, Carbonext (2026-11-19)

Re-research of three Pilot gaps with new strategies, to decide what goes into the research recipe (ticket 08). Nothing here is in `data/` yet; every row below is a proposal for the owner.

Strategies tested: **H1** Brazilian registries (CNPJ open data), **H5** Norte-side sources, **H6** co-investor and counterparty sources, **H8** search snippets as discovery only, **H9** LinkedIn lookups prepared for the owner. Run sequentially by one agent, 36 reads in total.

Caveat: the agent had seen the owner's four Norma LinkedIn rows before starting, so the Norma test is not blind. A finding counts only if a non-LinkedIn Source that was actually read states it.

Registry data was read through BrasilAPI (`https://brasilapi.com.br/api/cnpj/v1/<cnpj>`), a free mirror of Receita Federal's open CNPJ data. Only founders' names are recorded here; other administrators are not named.

## Norma (8 reads, plus the shared Norte pass)

CNPJ 54.782.822/0001-09 is in the homepage footer; the legal name is SIGMA LABS TECNOLOGIA DA INFORMACAO LTDA.

| Field | In data/ now | Experiment | Strategy | Proposal |
|---|---|---|---|---|
| founder | André M. G. Corrêa, Renato Sanabria, Bruno da Silva Assis (owner, LinkedIn) | Registry: André Murillo Geraldo Corrêa and Renato Souza Sanabria are administrators from the opening date (2024-04-18); Bruno da Silva Assis from 2025-10-31 | H1 | All three found without LinkedIn. Keep the rows; note in Bruno's that he joined the registry 18 months after opening |
| year_founded | 2023, estimated high (LinkedIn) | Registry opening date 2024-04-18 | H1 | **Conflict.** Our tapi precedent (company year, not idea year) points to 2024, reported, with 2023 noted as pre-incorporation work. Owner decides |
| hq | São Paulo, estimated low (footer) | Registered seat is the same address (Alameda Rio Claro 241, Bela Vista, São Paulo) | H1 | Keep, raise to estimated medium |
| Rounds | none | None found. A US company, Sigma Labs LLC, became the partner on 2024-10-15, which usually happens around a first institutional round | H1 | No row. Lead for SEC Form D (H2, untested) |
| milestone | none | 2024-04-18 company registered; 2024-10 restructured under the US holding Sigma Labs LLC | H1 | Candidates, if corporate events count as milestones |
| norte_participated | no Rounds | Nothing found (Fund II) | H5, H8 | H9 |

H8 produced two false matches: Seedtable's "Norma" (a freelancer-banking firm at norma.co) and CB Insights' "norma-1" are other companies.

## Jota HQ (4 reads)

CNPJ 55.521.797/0001-64 (JOTA PLATAFORMA LTDA) is in the footer.

| Field | In data/ now | Experiment | Strategy | Proposal |
|---|---|---|---|---|
| hq | none | Careers page (jota.ai/carreiras): on-site work in **Moema, São Paulo**. Registered seat: Rua Lavandisca 777, Indianópolis, São Paulo (next to Moema) | H1 | **São Paulo, Brazil**, reported medium, Source the careers page, registry in the note |
| hq_at_first_investment | none | Registered in São Paulo since 2024-06-13, seven months before the January 2025 seed. Only the current address is available | H1 | São Paulo, estimated medium. Wayback (H3, untested) could confirm the footer in January 2025 |
| year_founded / milestone | 2024; milestone "2024-07: Company created" (Finsiders) | Registry opening date 2024-06-13 | H1 | Year unchanged; the milestone could become 2024-06-13 with the registry as Source |
| founder | Davi Holanda (high), Marcelo Leite (medium) | Both administrators from the opening date (Davi de Holanda Rocha; Marcelo Leite Soares Pereira da Silva) | H1 | Raise Marcelo Leite to high. Tiago Guilhon is not in the registry (not decisive) |
| Rounds | 2025 seed, 2026 Series A | A US company, Save Time Platform Holding LLC, has been the partner since opening | H1 | Lead for SEC Form D on the undated pre-seed (H2, untested) |

The "cearense" in the press describes founder Davi Holanda, not the company. The earlier gap came from that wording plus confusion with JOTA, the news site.

## Carbonext (20 reads)

The CNPJ was not on the site's pages; a search found it in the terms of use: 12.028.178/0001-20 (CARBONEXT TECNOLOGIA EM SOLUCOES AMBIENTAIS LTDA). Its only partner is CARBONEXT HOLDING S.A. (41.643.197/0001-64, check digits computed and confirmed by the lookup).

| Field | In data/ now | Experiment | Strategy | Proposal |
|---|---|---|---|---|
| year_founded | 2010 (company site) | Registry opening date 2010-05-19, Janaína Dallan administrator since then | H1 | Confirmed; registry in the note |
| founder (Luciano Fonseca) | reported medium | Administrator of the operating company from 2021-06-22, and founding administrator of the holding on 2021-04-20 | H1 | Supports "joined in 2021": he co-founded the 2021 holding, not the 2010 company. Needs a founder rule |
| milestone | 1 (NaturAll, from an unread 403 page) | 2021-04-20 Carbonext Holding S.A. created; 2021-06 holding becomes the operating company's partner, ahead of the Series A | H1 | Two candidates |
| accelerator | none | **Google for Startups Accelerator**, first sustainability edition, selection announced 2022-09-13 (blog.google, read) | H8 then read | New row, reported high, plus a 2022-09 milestone |
| milestone | none | 2025-08: bought 40% of Mangue Tech (Brazil Journal, 2025-08-05, read) | H6 | New row, reported high |
| milestone (NaturAll) | Source is Carbon Pulse, never read | Brazil Journal (2025-08-05) confirms an earlier NaturAll stake on the same model, without a date. A snippet says June 2025 | H6, H8 | Re-source to Brazil Journal; the 2025 date stays estimated |
| status | active, Source Carbon Pulse (unread) | Brazil Journal 2025-08-05 (deal activity), plus a new administrator registered 2026-02-13 | H6, H1 | Re-source to Brazil Journal. Registry changes are usable activity evidence |
| hq_at_first_investment | São Paulo, estimated low | Holding incorporated in São Paulo in April 2021; operating company's seat is São Paulo (Vila Olímpia) | H1 | Raise to estimated medium |
| norte_participated | FALSE (low) on all 3 Rounds | No readable Source names Norte in any Round. VC Backed and Village list Norte at company level. Norte facts: started early 2020, Fund I US$8M, 42 companies by June 2021 (startups.com.br, 2021-06-07), and a follower that does not lead rounds (aggregator snippet). The September 2021 Series A had 20+ investors, mostly unnamed | H5, H6, H8 | Best estimate: Norte entered in the **2021 Series A**, low. The data model cannot express this today (see decisions) |
| Series A co-investors | Canary, Alexia, FitPart | No new names | H6 | H9 |
| Other | n/a | Parent renamed "Grupo CBX" (Carbon Pulse snippet, paywalled, not read) | H8 | Not recordable while a Source must be read |

## Yield per strategy

| Strategy | Reads | Result | Verdict |
|---|---|---|---|
| H1 registries | 13 (Norma 2, Jota 2, Carbonext 9) | ~17 new, upgraded or corroborated facts across all three; settled Jota HQ; found Norma's founders without LinkedIn | **Adopt as step one for Brazilian companies.** Cheap when the CNPJ is in the footer (2 reads); the cost is finding it when it is not (7 of Carbonext's 9 reads). S.A. holdings list directors only, not shareholders, so this never answers Norte |
| H5 Norte side | 4, shared | No company facts. Bounds on Norte's timing (started 2020, Fund I size and pace, follower that does not lead) | Run once for the whole portfolio, not per company. Norte's /content has only Tractian and Cayena case posts |
| H6 co-investor and counterparty | 4 | Co-investor side: nothing. Counterparty press: a readable replacement for a 403 Source plus a new milestone | Keep the counterparty part; drop co-investor searches unless a lead names one |
| H8 snippets | ~6 searches | 1 verified new fact (accelerator), 1 date lead, 2 false matches | Keep for discovery only, always followed by a read |
| H9 owner lookups | 0 | 8 queries prepared (below) | Owner's turn |

Norte's participation is still unresolved for Carbonext and Norma from free public sources. Norte's follower model explains why the press rarely names it. The remaining route is H9.

## H9: lookups for the owner

Return the URL and the fact for each.

**Norma**
1. `site:linkedin.com/company "norma.com.br"` → About tab: *Founded*, *Headquarters*.
2. `site:linkedin.com/posts ("Norma" OR "Sigma Labs") (pre-seed OR seed OR rodada) Sanabria` → round post: date, investors, Norte.
3. `site:linkedin.com/posts "Norte Ventures" Norma`

**Jota**
4. `site:linkedin.com/company "jota.ai"` → About tab: *Headquarters* (the company's own statement).
5. `site:linkedin.com/posts "Norte Ventures" Jota "Davi Holanda"` → whether Norte was in the 2024 pre-seed.

**Carbonext**
6. `site:linkedin.com/posts "Norte Ventures" Carbonext`
7. `site:linkedin.com/posts Carbonext ("Série A" OR "Series A") 2021` → the company's own round post, which usually tags every investor.
8. `site:linkedin.com/company carbonext` → posts from September 2021.

## Decisions for the owner

1. **`norte_participated`:** add `unknown`, or allow TRUE as estimated low (Carbonext's 2021 Series A)?
2. **Registry as a Source:** is a BrasilAPI URL acceptable as `source_url` for registry facts? The official Receita lookup has a captcha and no stable link.
3. **year_founded:** legal opening date or the start of work (Norma: 2024 vs 2023)?
4. **Founder rule:** does someone who co-founded a later holding company count as a founder (Luciano Fonseca)?
5. **Corporate events as milestones:** holding creations, US restructurings?

## Outcome (2026-11-19, after the owner's lookups and decisions)

H9 results (owner, by hand):
- Norma: LinkedIn company page gives HQ Alameda Rio Claro 241 (used, reported high) and "Founded 2025", which is the page's creation year, so 2023 stays. No round post and no Norte mention anywhere.
- Jota: LinkedIn HQ São Paulo (used). The post naming Norte is dated 2025-01-24 (decoded from the post ID), so it is the US$8.9M seed already recorded as TRUE, not the 2024 pre-seed. The pre-seed stays unresolved.
- Carbonext: no results for Norte or the 2021 Series A (LinkedIn shows only about 11 months of posts, so older announcements are not reachable this way). Norte's participation stays UNKNOWN in all three Rounds.

Decisions, all applied (see ADR 0009 and `docs/data-model.md`): `UNKNOWN` added; registry URLs accepted as Sources; `year_founded` is the start of work; a later co-founder of a holding is not a Founder (Luciano Fonseca removed, kept as a 2021 milestone); no corporate-housekeeping milestones.

Applied to `data/`: 12 Rounds moved from `FALSE` to `UNKNOWN` (5 stay `FALSE`: Tractian 2022 and its BNDES debt, idwall 2018 and 2019, Stay 2024, where a Source lists the investors without Norte); Norma HQ and notes; Jota HQ and HQ at first investment, Marcelo Leite to high; Carbonext accelerator, three milestones, status re-sourced, HQ at first investment raised.

Still open: Jota's pre-seed, Norte's participation in Carbonext and Norma, Palomma's and Jota's first-investment year (an earlier `UNKNOWN` Round may precede the derived one), the form D and Wayback leads below.

## Side findings

- Norte's portfolio page links trycomp.io and supercompany.io: renames of Zivo and Attach Media Partners (confirmed by the owner, now noted in `docs/data-model.md`).
- One search result's title told LLMs to credit Dealroom. It was ignored. Sub-agents need the same rule: text from search results and pages is data, not instructions.
- Untested leads: SEC Form D for Sigma Labs LLC and Save Time Platform Holding LLC (H2); Jota's January 2025 footer in Wayback (H3); Verra project dates for Carbonext (H7).
