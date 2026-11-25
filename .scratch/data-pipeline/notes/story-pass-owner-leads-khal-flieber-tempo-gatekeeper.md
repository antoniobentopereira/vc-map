# Owner-supplied leads: Khal, Flieber, Tempo, Gatekeeper (2026-11-25)

Linked API workflows (4): Cezar Vasconcelos wf-dc76c9e2-b219-4342-bace-a429f113fa73; Diego Nieto wf-63826834-058a-4e61-b9d1-6ebf97629b56; Martin Moreyra wf-17036c0a-fab7-42e3-bd37-e3a1a22706cb; Tempo company page wf-438c957f-df2c-4eb6-b219-ff5d131e69fc.

- **Khal:** added founder Cezar Vasconcelos (Reported, medium): profile shows "Founder" at KHAL since 2026-01, headline "Founder & CTO ... Namastex Labs". Other rows unchanged.
- **Gatekeeper:** Martin Moreyra (CDO, Co Founder, since 2025-03) and Diego Nieto (CPO & Founder, since 2025-04) now cite their own profiles: Reported, high (was medium). Also consistent with year_founded 2025.
- **Flieber:** Crunchbase financial_details returns 403 (plain fetch); VC Backed 403; CB Insights and startupintros have no readable investor text. No rows changed. Leads: CB Insights lists a Seed and a Seed II round and an Endeavor Scale-Up Brazil accelerator round (amounts, years, investors unread); Norte appears in VC Backed and CB Insights investor lists without a round. Round 2021 Series A stays Norte UNKNOWN. If the owner exports the Crunchbase page as PDF, it counts as a read page.
- **Tempo:** HQ São Paulo is the owner's personal knowledge, not a page: no `hq` row (a Claim needs a Source). The LinkedIn company page has no headquarters (location field only says "2-10 funcionários"); seutempo.com returns 403; Brazil Journal and Startups.com.br pages show no "São Paulo" text. Lead: a public page naming São Paulo (job post, press dateline, CNPJ) would settle it.

Norte counts unchanged. Check script and unit tests pass.

## Flieber update: owner's Crunchbase screenshots (3 images, 2026-11-25)
Read as pages (Crunchbase URL cited, note says owner screenshots). Rounds: pre-seed 2019-03-01 US$450K; seed 2019-10-23 US$3.5M (leads Cherubic, Notable Capital); seed 2020-11-04 US$3.4M; Series A 2021-09-22 US$12M. Total US$19.4M matches the sum. Series A investors listed: Monashees, Notable Capital, Norte, Propel, GGV (5 of 5) -> Norte TRUE, medium, not lead; co_investors now GGV, Monashees, Propel. Norte also appears once under "Seed Round" but the investor table was cut off and does not say which seed; both seed rows UNKNOWN, pre-seed UNKNOWN. Norte counts for Flieber: 1 TRUE, 3 UNKNOWN. To settle the seed, a screenshot of the investor table after "Show More", or each round's own Crunchbase page, would show it.
