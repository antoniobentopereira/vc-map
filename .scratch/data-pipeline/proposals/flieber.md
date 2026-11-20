# Flieber proposal

Fund I. Website https://flieber.com. A New York company (founder Brazilian by background, not confirmed by a read page). No CNPJ: the registry step does not apply.

New sub-sector needed in `data/sectors.csv` first: `Inventory planning software`. New FX rate: none (all Rounds in USD).

## Claims

```csv
company,field,value,source_url,basis,confidence,note
Flieber,description,"Software for multichannel commerce brands that connects sales channels, forecasts demand and recommends inventory replenishment, usable in its app, Slack, Google Sheets or through AI tools.",https://flieber.com,reported,high,Homepage (2026).
Flieber,long_description,"Flieber sells inventory planning software to commerce brands and to agencies or aggregators that sell across Amazon, Shopify, Walmart, TikTok Shop, eBay, Etsy and BigCommerce. A data layer pulls live sales and stock data from those channels, a planning engine produces demand and inventory forecasts and replenishment plans, and workflows carry out approved decisions. It is offered as self-serve software or with managed services, and is reachable from the app, Slack, Google Sheets, an API, a CLI and an MCP server for AI assistants. The company says it has served more than 1,000 brands since 2019.",https://flieber.com,reported,high,Homepage (2026); revenue model is inferred from the Self-Serve and Managed Services offers.
Flieber,sub_sector,Inventory planning software,https://flieber.com,estimated,high,Our label (new sub-sector; to be added to sectors.csv first).
Flieber,hq,"New York, United States",https://flieber.com,reported,high,"Footer address: 169 Madison Avenue, New York. TechCrunch (2021) also says New York. One aggregator (Tracxn, not read) lists San Jose; discarded."
Flieber,hq_at_first_investment,"New York, United States",https://techcrunch.com/2021/09/22/inventory-optimization-startup-flieber-bags-12m-aims-to-help-retailers-avoid-out-of-stock-overstock-moments/,estimated,low,"Norte's first investment year is unknown. TechCrunch (2021-09-22) gives New York as the base at the Series A, the closest dated source; no earlier source found."
Flieber,year_founded,2019,https://techcrunch.com/2021/09/22/inventory-optimization-startup-flieber-bags-12m-aims-to-help-retailers-avoid-out-of-stock-overstock-moments/,reported,medium,"TechCrunch says the CEO co-founded Flieber in 2019; the company site also says it has served brands since 2019. No month found, and no registration date."
Flieber,status,active,https://flieber.com,estimated,high,"Live site with a 2026 copyright, current AI-agent products (MCP, CLI) and named customers."
Flieber,business_model,b2b,https://flieber.com,reported,high,Sold to commerce brands and to agencies and aggregators.
Flieber,founder,Fabricio Miranda,https://techcrunch.com/2021/09/22/inventory-optimization-startup-flieber-bags-12m-aims-to-help-retailers-avoid-out-of-stock-overstock-moments/,reported,high,"Co-founder and CEO; the company site also names him Founder and CEO. TechCrunch: earlier founded and sold a water-treatment company in Brazil, worked at a hedge fund, then sold on Amazon."
Flieber,founder,Jair Vercosa,https://techcrunch.com/2021/09/22/inventory-optimization-startup-flieber-bags-12m-aims-to-help-retailers-avoid-out-of-stock-overstock-moments/,reported,high,Co-founder and CTO per TechCrunch (2021).
Flieber,founder,Joao Pedro Sant Anna,https://www.alleywatch.com/2021/09/the-alleywatch-startup-daily-funding-report-9-13-2021/,reported,low,"Only AlleyWatch's 2021 funding report lists him among the founders; TechCrunch names just two. Spelling as in AlleyWatch, no accent. A search snippet also named a co-founder Rituparna Agrawal, not read, so not recorded."
Flieber,market,United States,https://flieber.com,estimated,medium,"New York company whose integrations are US marketplaces (Amazon, Walmart, Shopify) and whose data is hosted in the US. TechCrunch (2021) says clients sell in 15 countries, not named."
```

## Rounds

```csv
company,year,type,reported_amount,reported_currency,size_usd,co_investors,norte_participated,source_url,basis,confidence,note
Flieber,2021,series_a,12000000,USD,12000000,GGV Capital (co-lead); Monashees (co-lead),UNKNOWN,https://techcrunch.com/2021/09/22/inventory-optimization-startup-flieber-bags-12m-aims-to-help-retailers-avoid-out-of-stock-overstock-moments/,reported,medium,"Announced 2021-09-22; TechCrunch names only the two co-leads and says total funding reached US$20M. Norte is not named, but the investor list is partial; an aggregator (VC Backed) lists Norte Ventures, Cherubic Ventures, Notable Capital (GGV's later name) and the two leads for this Round, so Norte may have taken part. AlleyWatch (2021-09-13, from an SEC filing) says ten investors took part, unnamed. Discarded: other aggregators give totals of US$15M to US$19.4M."
```

FX rows needed: none.

```csv
currency,year,rate,source_url
```

## Search log

Reads counted: 8 pages read (flieber.com, thesaasnews, TechCrunch, retailtechinnovationhub, VC Backed, AlleyWatch, startupintros (empty error page), plus the 404s listed as not read). Linked API: 4 workflows launched, 3 finished or lost, 1 unresolved (see Open questions).

| Field aimed at | Query | URL or command | Read | Result |
|---|---|---|---|---|
| description, HQ, founders, markets, product | homepage | https://flieber.com | yes | Product, customers, New York footer address, Fabricio Miranda as Founder and CEO; no CNPJ or legal name |
| founders, history | About page | https://www.flieber.com/about | no (404) | Nothing |
| HQ, work model | Careers page | https://www.flieber.com/careers | no (404) | Nothing |
| Rounds, Norte | Flieber rodada de investimento inventory planning startup | web search | snippets only | Leads: Series A Sept 2021, GGV and Monashees, aggregators list Norte |
| Round | thesaasnews article | https://www.thesaasnews.com/news/inventory-optimization-startup-flieber-raises-12-million-in-series-a/ | yes | Rewrite of TechCrunch; US$12M, co-leads GGV and Monashees, founders Miranda and Vercosa |
| Founders, Round, year | Flieber Fabricio Miranda founder ... Norte Ventures | web search | snippets only | Founders, aggregator Norte mentions, no seed round found |
| Round, year, founders | TechCrunch original | https://techcrunch.com/2021/09/22/inventory-optimization-startup-flieber-bags-12m-aims-to-help-retailers-avoid-out-of-stock-overstock-moments/ | yes | Series A US$12M, co-leads, total US$20M, founded 2019, New York, founders backgrounds |
| Founders | careers/about alternative | search: "Flieber" Techstars/YC/accelerator | snippets only | No accelerator found |
| Rounds | search: Flieber seed round 2020 | web search | snippets only | No seed announcement; CB Insights lists undated seed rounds |
| Rounds | search in Portuguese, Monashees GGV | web search | snippets only | No Brazilian press coverage found |
| Round, founders | Retail Tech Innovation Hub | https://retailtechinnovationhub.com/home/2021/9/23/supply-chain-technology-startup-flieber-nabs-series-a-funding | yes | US$12M Series A, total US$20M since 2019, no other investors |
| Norte, Round | VC Backed company page | https://www.vcbacked.co/company/flieber | yes | Aggregator: Series A Sept 2021, lists Norte Ventures, Notable Capital, Cherubic, GGV, Monashees (lead only, not a Source for TRUE) |
| Seed rounds, Norte | search: seed/pre-seed, Cherubic, Endeavor | web search | snippets only | PitchBook seeds (2019-03 US$450K, 2019-10 US$3.5M, 2020-11) seen only in a snippet, not read |
| Founders, Round | AlleyWatch funding report 2021-09-13 | https://www.alleywatch.com/2021/09/the-alleywatch-startup-daily-funding-report-9-13-2021/ | yes | US$12M, ten investors unnamed, third founder Joao Pedro Sant Anna, total US$19.4M |
| Founding story | Category Visionaries podcast | podbean URL | no (redirect to login) | Nothing |
| Rounds | CB Insights | https://www.cbinsights.com/company/flieber | no (403) | Nothing |
| Rounds, history | Crunchbase | https://www.crunchbase.com/organization/flieber | no (403) | Nothing |
| History | cavac.at draft article; yespress.io; Wikipedia draft | various | no (host not found / 403 / 404) | Nothing |
| Founders, accelerator | search in Portuguese for interviews | web search | snippets only | Nothing relevant |
| Round, Norte | search: Series A press release Norte, Cherubic, AME Cloud | web search | snippets only | No original release naming investors |
| Round | startupintros | https://startupintros.com/news/flieber-series-a-2021-09 | yes (error page) | "News Not Found", nothing |
| Norte in Round | Linked API workflow 1: `python scripts/linkedin.py search-posts "Flieber" --mentioning "Norte Ventures"` | command | yes | exit 0, workflowStatus completed, data empty; workflowId not printed by the client |
| Company page | Linked API workflow 2: `python scripts/linkedin.py search-companies "Flieber inventory planning"` | command | yes | exit 0, completed, data empty; workflowId not printed |
| Company posts, round announcement | Linked API workflow 3: `python scripts/linkedin.py company https://www.linkedin.com/company/flieber --posts 20` | command | no | My own 290s `timeout` wrapper killed it (exit 124) while queued behind other agents' workflows; no result, workflowId not captured |
| Company posts, round announcement | Linked API workflow 4: same command re-run with no wrapper | command | no | Finished with exit 3: workflowStatus running, "usually takes about 6-8 minutes"; parked. The client output printed no workflowId. Budget of 4 is used |

## Open questions

- **Norte in the Series A:** UNKNOWN. Only aggregators (VC Backed, CB Insights "Norte Capital", PitchBook snippet) list Norte; no read Source names it. Linked API: the Norte mentions search returned nothing, and the company page and posts query did not return a result in this run (workflow 3 was cut by my wrapper; workflow 4 ended with exit 3, parked). Whoever consolidates should check the output file of workflow 4 (`C:\Users\anton\AppData\Local\Temp\claude\30bdf4e0f1a2f732\df2d7d90-3af1-4ae7-b7d3-1797a3b71a3a\tasks\breonz3n5.output`, if the harness still holds it) for a company post naming Norte, and fetch it with `python scripts/linkedin.py result <workflow-id>` if the id is visible. Workflow 4 returned exit code 3 (parked) but printed no workflowId, so it cannot be fetched with `result`; re-run `company https://www.linkedin.com/company/flieber --posts 20` later if wanted. Workflow 3 was cut by my own wrapper.
- **Earlier rounds (seed):** TechCrunch implies about US$8M raised before the Series A (US$20M total minus US$12M), and aggregators list seed rounds (PitchBook snippet: 2019-03 US$450K, 2019-10 US$3.5M; CB Insights: 2020-11). None was read on a readable page, so no rows. Norte's first investment is probably one of those, so Norte's first investment year and the first-investment fields stay unknown.
- **Co-investors beyond the leads:** Cherubic, AME Cloud, Endeavor Scale-Up Brazil, Propel, Spectra appear in aggregators or in AlleyWatch as earlier investors; none is tied to a Round by a read Source.
- **Founders:** the third founder (Joao Pedro Sant Anna) rests on one source; Rituparna Agrawal appeared only in a snippet.
- **Legal registration date, HQ before 2021, accelerators:** nothing found. About and Careers pages return 404; no registry applies (US company).
- **Brazil connection:** founders' Brazilian background was not confirmed by a read page beyond TechCrunch's mention of a Brazilian water-treatment company; no Brazilian press coverage found.
