# Story pass (2026-11-25): Manor, Sempre+, Taicor

All three already had `researched_on` (2026-11-24), so this was a story pass on the owner's leads: long description, investment thesis, founders, milestones rewritten or added; other rows kept. `researched_on` set to 2026-11-25. Norte Manifesto re-read for the thesis (unchanged in substance). Linked API: 2 workflows per company (6 of 12 allowed).

## Manor
- **Owner lead:** founder Rodrigo Salvador, profile https://www.linkedin.com/in/salvadorrodrigo, "many Norte connections in the bio", photo suggests two other people.
- **Reads:** manor.com.br (home, footer), minhareceita.org/62490945000196 (opened 2025-09-01, Rodrigo Augusto Gomes Salvador administrator since opening, Manor Tax LLC partner since opening, capital R$1,539,850), Brazil Journal 2021-03-19 (UOL Edtech buys Passei Direto; founders Rodrigo Salvador and André Simões stay as executives), MIT Innovators Under 35 page (2022 winner). Four web searches (company + founder, Norte): no article on Manor.
- **Linked API:** `person salvadorrodrigo --experience` wf-2239afc6-959d-49dc-95ef-06c4356b6cea: Co-Founder, "Stealth Startup", 2025-10 to now; headline "Helping to build the future of tax"; Passei Direto CEO & co-founder 2012-05 to 2022-01; UOL CEO Passei Direto 2021-03 to 2022-01, VP Strategy, M&A and B2B. `company` for the stealth page wf-0c8b46e7-39a1-46bb-bab8-151ff46a4686: a generic "Stealth Startup" community page (Harmonic, San Francisco, 38,875 employees), no help.
- **Fields changed:** founder (name from the profile, Estimated, medium: the profile never names Manor; the link is the headline, the date and the registry); long description (adds the founder's story and removes an ERP/MCP sentence that only a search summary had given); investment thesis; one milestone (2025-10).
- **Gaps:** other co-founders (the owner sees two more faces; no page names them); customers, revenue, funding; HQ (registry seat Campinas only; the profile says "Brasil"). Norte: no Round, no row; the "Norte connections" are the owner's observation, kept as a lead.
- **Leads to verify:** the two other co-founders; whether Norte or Valutia-type funds backed the US entity (Manor Tax LLC); André Simões (Passei Direto co-founder) as a Manor partner (no evidence).

## Sempre+
- **Owner lead:** https://valutia.com/portfolio/sempre-mais; Valutia is an investor; founded 2026; no investment information.
- **Reads:** valutia.com/portfolio/sempre-mais is a JavaScript app that serves one shell page for every URL; its text is in `/assets/index-37c-MATX.js` (portfolio array: Sempre+ "Bringing primary healthcare to millions of Brazilians through WhatsApp", Founded "—", São Paulo, Early-Stage, founders Bruna Keiserman and Gabriela Migliorini with LinkedIn URLs, metric "150M+ Brazilians without health insurance"). The same list holds Caveo, Nomo, Datamint and Refer, which are also in Norte's portfolio. sempre-mais.com home, /sobre, /medicos re-read. Two web searches: no press.
- **Linked API:** `person bruna-keiserman --experience` wf-175f009d-ff5f-493f-82e1-2ed53c6b6a83 (Founder & CEO from 2025-10; Trybe COO 2022-01 to 2024-03; Atlântico EIR 2024; BrandLovrs COO 2024-11 to 2025-02; Mimic founder 2019). `person gabriela-migliorini --experience` wf-83199f3f-0599-4eb1-bc8d-9874a8cf9823 (Co-Founder & CPTO from 2026-01; Jusbrasil Head of Product Jus IA 2025; Trybe 2019-).
- **Fields changed:** both founders now Reported, high (profile + Valutia + registry); `year_founded` 2026 to 2025 (Bruna's role start 2025-10; registry 2026-03-12 in the note); long description, thesis, two milestones.
- **Round:** none written. Valutia's page gives no year, amount or type, so there is no Round row (undated rounds are not Rounds). Norte `UNKNOWN`. Lead: dPed Holding LLC (registry, 2026-06-12) as the date of a first round.
- **Gaps:** Valutia's amount, date and co-investors; launch date; the 9,000-consultation figure's date.
- **Leads to verify:** Valutia press release or a LinkedIn post for the round; Trybe overlap of the founders (both worked there; the profiles do not show them working together).

## Taicor
- **Owner lead:** co-founder João Henrique Lisboa (https://www.linkedin.com/in/joaolisboa); "try to figure out some clients and understand a case".
- **Reads:** taicor.ai home and /en; Luma event page luma.com/4o81zsdl; Eventos de Marketing page for the Claude Meetup Rio; Mapa IA Brasil (JSON-LD list and HTML list, Taicor with founders João Henrique Lisboa and Luiz Guilherme Gama); minhareceita.org/60804586000179. Searches (5, standard and extended; founders' names; "cliente caso"): **no customer, case study or press article**. A Finsiders article on a Rio AI-agent platform was Tess AI, a different company (not used).
- **Linked API:** `person joaolisboa --experience` wf-7ec090db-6485-4884-99f3-8d873096d11b (Co-Founder Taicor from 2026-01; IP Capital Partners partner, co-PM 2014 to 2025). `person luiz-guilherme-gama --experience` wf-86c87ea4-a806-4a05-873b-0cd37b74bd28 (URL from a web search limited to linkedin.com; Co-Founder from 2026-04; Vista Capital founding partner & CEO 2015 to 2024; Vinci Partners analyst 2012 to 2015).
- **Fields changed:** João added as `founder` (Reported, high; the earlier row had left him out as a late joiner); Luiz Reported, high; `year_founded` 2025 to 2026 (founders' role starts; registry 2025-05-13 in the note, Low); long description, thesis, five milestones (2026-01, 2026-03-23, 2026-04, 2026-06-30, 2026-10).
- **Gaps:** customers and any case (the question the owner asked): not public in anything we could read; funding (Taicor LLC joined the registry 2026-10-08, a lead for a first round); pricing; team size.
- **Leads to verify:** Claude Impact Lab hackathon in Rio (2026-05-24) sponsored by Taicor (a LinkedIn snippet only); employees seen in search results (João Pedro Goes, Felipe Carvalho, both "Taicor" on LinkedIn); a post by Taicor on LinkedIn naming a client (company page not read; `company <url> --posts` failed repeatedly in earlier Batches).

## Counts
Rounds written: 0 for all three; Norte `TRUE` 0, `FALSE` 0, `UNKNOWN` 0 (no Round rows).

## Recipe changes
Added to `docs/research-recipe.md` under "Lessons from the Manor, Sempre+ and Taicor story pass".
