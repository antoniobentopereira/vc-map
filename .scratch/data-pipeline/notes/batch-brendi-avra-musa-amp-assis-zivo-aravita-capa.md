# Batch 8 (2026-11-24): Brendi, Avra, Musa, Attach Media Partners, Assis, Zivo, Aravita, Capa

Rows written to `data/` for all eight, `researched_on` set, `python scripts/check_data.py` and `python -m unittest discover -s tests` (107 tests) pass. Norte count over the 8 Rounds: TRUE 5 (Brendi 2026, Avra 2024, Assis 2023, Zivo 2023, Aravita 2023), FALSE 1 (Zivo Series A 2026), UNKNOWN 2 (Brendi 2021 Locaweb round, Capa 2025 pre-seed). Musa and Attach Media Partners have no Round row.

Linked API (all through `scripts/linkedin.py`, the owner's account): one script of eight `search-companies` runs by name alone, then extra workflows for Attach Media Partners.

| Company | Workflow | Result |
|---|---|---|
| Brendi | wf-55a5770b-b0b3-414a-938b-de6d41bed645 | page `brenditech`, São José dos Campos, SP (matches the terms of use) |
| Avra | none printed | only namesakes (pharma India, NGO, Crete travel) |
| Musa | none printed | only namesakes (Milan agency, Lima edtech) |
| Attach Media Partners | wf-ec06d7db-6a0b-41b1-a75e-91c216b16837 | page `attachmediapartners`, location null |
| Assis | none printed | `assis-app`, "Tecnologia, Informação e Internet", São Paulo (among law-firm and hospital namesakes) |
| Zivo | none printed | only namesakes |
| Aravita | wf-f52a1161-8865-4db6-8bad-2f6d65a2bc4c | page `aravita`, São Paulo, SP (plus Florida namesakes) |
| Capa | none printed | only namesakes |
| AMP `company <url>` | wf-a1ee59e3-456a-472e-bca7-8b30da6151c7 | worked: description "formerly Super Company, 2021 to 2026", 30+ titles, 100M downloads, 45 employees, no location |
| AMP `founders <url>` | wf-7e6e2364-2e09-43d3-91d5-9a030e5b8ee3 | Douglas Souza (Co-Founder at Super Company), "Bruno O." (Co-Founder at AMP), a VP of CorpDev in São Paulo, two unrelated people |
| AMP `person brunoonto --experience` | wf-613b5907-9bc4-4c8e-8e20-e7e9f85472db | "Bruno O.", CEO and co-founder at AMP since 2022-06; earlier iFood, MovilePay, Zoop |

(A second `founders` run for AMP was started after the first tail was cut; its workflow id was not printed, so the table lists only the ids that were.)

## Brendi

- **Reads:** brendi.com.br (home, /sobre-nos, /planos, /termos-de-uso); Startup Researcher and Techloy (2026 seed, Techloy dated 2026-07-17); SJC city-hall article (2022-02-08); Baguete and Startups.com.br (2026-11, key accounts); Monitor Mercantil and Gironews (Abrasel figures).
- **Rounds:** 2026 seed US$6.6M (TRUE, Norte named by both articles); 2021 "R$650 thousand with Locaweb" (type unknown, UNKNOWN; the year is our estimate from "nos últimos meses" before February 2022).
- **Conflicts:** CB Insights dates the seed September 2025, Caplight US$7M on 2026-07-01, Seedtable 2026-07-15; Startup Researcher's text mentions 2024 ARR targets, which look copied from an older piece.
- **Gaps:** the other two ITA co-founders; CNPJ (not on the pages read); pre-seed details (Bouncewatch US$420 thousand did not open).
- **Leads:** two unnamed co-founders (SJC article); CB Insights "pre-seed" and Locaweb as investor.

## Avra

- **Reads:** avra.ai (home, /about, /careers, /blog, /research, /terms, /solutions/cases/credit, two blog posts whose bodies did not render); Startupi (2024-07-11); LatamList (2024-07-16); registry via minhareceita (BLOOM TECNOLOGIA LTDA, opened 2024-02-06, administrators Viviane Meister Vignoli and Bruno Alano Medina, partner Bloom Technology LLC from 2024-05-15); Agência Sebrae.
- **Rounds:** 2024 US$2M led by MAYA (TRUE, Norte named by Startupi and LatamList). "Seed" type comes from Dealroom's label, so Confidence is medium.
- **Gaps:** later rounds (CB Insights lists an AWS accelerator entry, aggregator only); dates for the product pivot from SMEs to relational foundation models; the HQ move from Curitiba (terms) to São Paulo (registry, careers).
- **Not used:** Fundamental's US$255M (search results only).

## Musa

- **Reads:** musa.co (home, /tecnologia, /politica-de-privacidade for the CNPJ); InfoMoney (2022-12-12); Mercado&Consumo (Alelo, 2022-05-17); Boring Business Nerd (June 2023 profile); Lower Carbon Capital; Kaszek page; ImpactAlpha (about another company, read for waste statistics); registry (MUSA TECNOLOGIA LTDA, opened 2020-11-13, administrators Martin Junck and since 2024-09-12 Anderson Taniguchi, partner Musa Technology LLC).
- **Rounds:** none written. VC Backed lists a US$15M Series A in October 2021 with Norte, Kaszek, GFC, Endurance28 and Silence, but the page did not open (aggregator). InfoMoney names JFC and Kaszek as investors without year or amount.
- **Gaps:** Round dates and amounts, Norte participation, current traction, Fabrício Guimarães's role today (not in the registry).
- **Leads to verify:** the October 2021 Series A (VC Backed, search summary); PitchBook's US$280K debt deal.

## Attach Media Partners (formerly Super Company, Supercompany)

- **Reads:** attachmp.com home; supercompany.io (old site, partner criteria); Grand Screen catalog page (Supercharge Mobile titles, not used for claims); LinkedIn company page and two profiles through Linked API only.
- **Rounds:** none. CB Insights and PitchBook (search summaries) list a Norte seed dated 2022-02-22; neither opened.
- **Gaps:** HQ (the LinkedIn page has no location, the CEO's profile says United States, the VP is in São Paulo); registry (no CNPJ on either site); the other co-founder's full name ("Bruno O."); any press coverage, acquisitions, revenue, rebrand month; market data.
- **Leads:** "Super Company is São Paulo-based, founded 2022" (aggregator summaries); a March 2025 Saga Origins partnership (search summary); an old LinkedIn page `super-company-io` (not fetched: LinkedIn is read only through Linked API).
- Founded: 2021 from the LinkedIn text "Super Company 2021 to 2026", Confidence low, against 2022-06 on the CEO's profile.

## Assis

- **Reads:** assis.co home; Startups.com.br (2023-04-04); Baguete (2023-04-12); registry (NBT TECNOLOGIA LTDA, trade name ASSIS, opened 2022-06-20, administrators Machioni and Bergamo, partner NBT Intermediate Holdings LLC); bpmoney (Ancord, 2026-05-17). Bloomberg Línea's page returned a different article; Finextra returned nothing.
- **Rounds:** 2023 R$27.5M (TRUE). Type "seed" comes from Finsmes/Finextra headlines; Finsmes' "led by Costanoa" is not in the Portuguese articles, so no lead is marked.
- **Gaps:** when and why the product moved from self-employed workers to investment advisors; any later round; traction.

## Zivo (formerly Comp)

- **Reads:** zivo.ai home; Startup Researcher (rebrand 2026-11-17); Startups.com.br (2023-03-28); Baguete and Brazil Journal (2026-02-23); LatamList (2026-02-24). `zivo.ai/about` and `/privacy` rendered nothing.
- **Rounds:** 2023 R$14M (TRUE; Baguete calls it pre-seed US$2.7M, kept as seed); 2026 Series A R$100M (FALSE: three outlets list the investors without Norte; `size_usd` empty until the 2026 BRL average is in `fx.csv`).
- **Gaps:** CNPJ and registry (none read); date of the move from compensation data to full HR services.

## Aravita

- **Reads:** aravita.com home; Baguete (2023-03-31, 2023-07-28); NeoFeed (2023-03-30); Central do Varejo (2023-08-28); AgFeed (2026-07-22); Abras via Folha PE.
- **Rounds:** 2023 seed R$12M (TRUE, the press writes "Norte Capital"; HiPartners' July 2023 addition is part of the same row).
- **Conflicts:** founded 2022 (Baguete, NeoFeed) vs "early 2023" (AgFeed).
- **Leads:** St. Marche results (20% less waste, 30% fewer stock-outs) appeared only in search summaries and were left out.
- **Gaps:** CNPJ and registry; the 2025 Abras total (R$1.14 trillion) was only a search summary.

## Capa

- **Reads:** capa.fi (home, /blogs and the pre-seed post); Emprefinanzas (2025-02-01); PR Newswire (Borderless.xyz, 2025-04-10); DFNS (2026-06-30); Solana Compass; UnoTV (Banxico remittances). `capa.fi/about`, `/team`, `/terms` and `/privacy` rendered nothing; Benzinga was blocked.
- **Rounds:** 2025 pre-seed US$2.5M including a US$1M extension (Norte UNKNOWN: two partial investor lists, neither names Norte; aggregators list it).
- **Gaps:** HQ (not stated: VC Backed says Santo Domingo, CB Insights San Francisco, legal entity Mexican); founders (the press names a CEO, CTO, CFO and CMO, but not as founders); year founded rests on the RFC digits (2022-04-05).
- **Leads:** Juan Diego Oliva (CEO), Juan David Torres (CTO), Levit Salcedo (CFO), Daniel Forero (CMO), from Emprefinanzas; check each profile in step 7 next time.

## Recipe changes

See "Lessons from Batch 8" in `docs/research-recipe.md`.
