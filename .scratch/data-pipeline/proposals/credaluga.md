# Proposal: CredAluga (Fund II)

## Claims

```csv
company,field,value,source_url,basis,confidence,note
CredAluga,description,"Brazilian fintech that sells rental guarantees through real estate agencies, replacing the traditional guarantor (fiador) with a fully digital product.",https://credaluga.com.br,reported,high,
CredAluga,long_description,"CredAluga sells rental guarantees to tenants through partner real estate agencies, with fully digital contracting. Products include CredFiança (a fee-based guarantee with recurring commission for agencies), CredReembolsa (a guarantee with cashback) and Fundo CredAluga, a guarantee funded by the tenant's contribution and invested in low-risk fixed income, plus add-ons for painting and debt arrangements. It claims more than 2,000 partner agencies and over 30,000 guaranteed assets.",https://credaluga.com.br,reported,medium,"Company site, read 2026-11-19; figures are the company's own and undated."
CredAluga,sub_sector,Rental guarantees,https://credaluga.com.br,estimated,high,"Our label; NEW sub-sector, must be added to sectors.csv first."
CredAluga,hq,"Barueri, Brazil",https://www.linkedin.com/company/credaluga,estimated,low,"LinkedIn company search result (via Linked API, 2026-11-19) shows location Alphaville, São Paulo (Alphaville is in Barueri); registry seat is also Barueri (BrasilAPI). The site lists offices in both Belo Horizonte and Barueri without naming a HQ; Dealroom (aggregator) says Belo Horizonte and the privacy policy's legal forum is Belo Horizonte. Discarded Belo Horizonte as unsupported by a company statement."
CredAluga,year_founded,2022,https://www.bloomberglinea.com.br/startups/credaluga-capta-r-25-mi-para-melhorar-analise-de-inquilinos-para-imobiliarias/,reported,medium,"Bloomberg Línea (2024-10-28) says founded in 2022; registered 2022-05-12 (BrasilAPI); operating since Q2 2023 per the same article."
CredAluga,status,active,https://portas.com.br/noticias/olx-encerra-parceria-com-creditas-e-investe-na-credaluga/,estimated,high,"OLX investment news dated 2025-10-29; the live site shows current products and a 2026 Reclame Aqui badge."
CredAluga,business_model,b2b2c,https://startups.com.br/negocios/fintech/credaluga-capta-r-22m-para-ampliar-seus-produtos-financeiros/,reported,high,"Works only through partner real estate agencies; the tenant is the end customer."
CredAluga,market,Brazil,https://credaluga.com.br,reported,high,"Partner agencies across Brazil."
CredAluga,founder,Daniel Santos,https://www.bloomberglinea.com.br/startups/credaluga-capta-r-25-mi-para-melhorar-analise-de-inquilinos-para-imobiliarias/,reported,high,"Co-founder and co-CEO. Administrator of the registered company since its opening on 2022-05-12 (BrasilAPI)."
CredAluga,founder,Guilherme Blumer,https://www.bloomberglinea.com.br/startups/credaluga-capta-r-25-mi-para-melhorar-analise-de-inquilinos-para-imobiliarias/,reported,high,"Co-founder and co-CEO. Appears in the registry as administrator only from 2023-08-27; two press articles call him co-founder."
CredAluga,milestone,"2023: Began operating, working only with real estate agencies",https://www.bloomberglinea.com.br/startups/credaluga-capta-r-25-mi-para-melhorar-analise-de-inquilinos-para-imobiliarias/,reported,medium,"Article says operating since Q2 2023."
CredAluga,milestone,"2024-09: Partnership with consultancy Cupola; its founder Rodrigo Werneck becomes CMO",https://startups.com.br/danca-das-cadeiras/credaluga-e-cupola-se-unem-e-anunciam-novo-cmo/,reported,high,"Article dated 2024-09-03."
CredAluga,milestone,"2024: Launched Fundo CredAluga, a fund-backed rental guarantee",https://portas.com.br/noticias/credaluga-capta-r-60-mi-e-planeja-crescer-10x-ate-2030/,reported,medium,"Article (2025-09-29) says the fund launched at the end of 2024."
```

## Rounds

```csv
company,year,type,reported_amount,reported_currency,size_usd,co_investors,norte_participated,source_url,basis,confidence,note
CredAluga,2024,seed,22000000,BRL,4080119,Caravela Capital (lead); Honey Island by 4UM; Terracota Ventures; FJ Labs,TRUE,https://www.bloomberglinea.com.br/startups/credaluga-capta-r-25-mi-para-melhorar-analise-de-inquilinos-para-imobiliarias/,reported,high,"Announced 2024-10-28 as the first external round; names Norte Ventures. startups.com.br gives the same figures. Bloomberg Línea's URL says R$ 25 mi but its text says R$ 22 mi."
CredAluga,2025,series_a,60000000,BRL,10742100,Provence Partners (lead); Caravela Capital; Honey Island by 4UM,TRUE,https://startups.com.br/negocios/rodada-de-investimento/11-meses-apos-seed-credaluga-levanta-mais-r-60m-em-serie-a/,reported,high,"Announced 2025-09-29; names Norte Ventures among the seed investors who joined. Portas gives the same facts. Latamlist lists US$11M."
CredAluga,2025,unknown,5000000,USD,5000000,OLX,UNKNOWN,https://portas.com.br/noticias/olx-encerra-parceria-com-creditas-e-investe-na-credaluga/,reported,low,"OLX takes a minority stake with US$5M (article 2025-10-29). The article does not say whether this is part of the Series A or a separate round, and does not list investors for it; one search summary mentions Prosus as a bridge, unread. Could be double counting with the Series A."
```

FX: no new rate needed (BRL 2024 and 2025 already in fx.csv; USD needs none).

```csv
currency,year,rate,source_url
```

New sub-sector (not in sectors.csv): `Rental guarantees`.

## Search log

| # | Field aimed at | Query / command | URL | Read | Result |
|---|---|---|---|---|---|
| 1 | all (site) | fetch homepage | https://credaluga.com.br | yes | Products, markets, offices BH and Barueri; footer CNPJ misread by the fetch tool as 46.381.179 |
| 2 | Rounds | "CredAluga rodada investimento startup" | web search | n/a (leads) | Series A, seed, OLX articles |
| 3 | Series A, Norte | startups.com.br article | https://startups.com.br/negocios/rodada-de-investimento/11-meses-apos-seed-credaluga-levanta-mais-r-60m-em-serie-a/ | yes | Norte named; Provence lead |
| 4 | Seed, founders, year | Bloomberg Línea | https://www.bloomberglinea.com.br/startups/credaluga-capta-r-25-mi-para-melhorar-analise-de-inquilinos-para-imobiliarias/ | yes | R$ 22M seed, Norte named, 2022 |
| 5 | Registry | BrasilAPI 46381179000103 | https://brasilapi.com.br/api/cnpj/v1/46381179000103 | yes (400) | Invalid CNPJ (misread) |
| 6 | About | /quem-somos/ | https://credaluga.com.br/quem-somos/ | yes | No founders or year; two offices |
| 7 | OLX round | Portas | https://portas.com.br/noticias/olx-encerra-parceria-com-creditas-e-investe-na-credaluga/ | yes | US$5M OLX, 2025-10-29 |
| 8 | Series A/seed | fusoesaquisicoes | https://fusoesaquisicoes.com/acontece-no-setor/credaluga-atrai-fundos/ | no, 403 | - |
| 9 | HQ, founders | web search founders/HQ | web search | n/a | Leads only (Dealroom, Seedtable) |
| 10 | Seed | startups.com.br seed | https://startups.com.br/negocios/fintech/credaluga-capta-r-22m-para-ampliar-seus-produtos-financeiros/ | yes | Norte named; B2B2C |
| 11 | Milestone | Cupola CMO | https://startups.com.br/danca-das-cadeiras/credaluga-e-cupola-se-unem-e-anunciam-novo-cmo/ | yes | 2024-09-03 |
| 12 | CNPJ | search legal name + CNPJ | web search | n/a | Correct CNPJ 46.361.179/0001-03 |
| 13 | Registry | BrasilAPI 46361179000103 | https://brasilapi.com.br/api/cnpj/v1/46361179000103 | yes | CREDALUGA LTDA, Barueri, opened 2022-05-12, admins incl. Daniel Santos (2022), Blumer (2023-08), holding LLC partner since 2025-01-20 |
| 14 | Legal name, address | privacy policy | https://credaluga.com.br/politica-de-privacidade/ | yes | CNPJ confirmed; forum in Belo Horizonte |
| 15 | Series A, milestones | Portas Series A | https://portas.com.br/noticias/credaluga-capta-r-60-mi-e-planeja-crescer-10x-ate-2030/ | yes | Norte named; Fundo end of 2024 |
| 16 | HQ | web search "sede em" | web search | n/a | No HQ statement found |
| 17 | HQ (step 7) | `linkedin.py search-companies "CredAluga garantia locação"` | - | yes, exit 0, no workflowId shown | Empty result |
| 18 | HQ (step 7) | `linkedin.py search-companies "CredAluga"` | https://www.linkedin.com/company/credaluga | yes, exit 0, workflowId not shown | Location Alphaville, São Paulo |
| 19 | HQ (step 7) | `linkedin.py company https://www.linkedin.com/company/credaluga` | - | no: killed by my 550 s timeout (exit 124), workflowId not captured | Not read; likely queued |

## Open questions

- HQ is Estimated low (Barueri vs Belo Horizonte); the company page workflow (#19) timed out while queued and was not retried. A re-run of `company` could confirm the stated location.
- `hq_at_first_investment`: no dated source found; left missing.
- OLX US$5M (2025): relationship to the Series A is unknown; Norte UNKNOWN. Prosus bridge mention unread.
- Founders' start dates not checked via LinkedIn (not needed: year from press).
- Registry: CNPJ 46.361.179/0001-03 is a Ltda in Barueri with a foreign LLC partner (CREDALUGA HOLDING LLC, 2025-01-20), suggesting a US holding set up around the Series A; not a Round.
- No acquirer or accelerator found.
- Norte: TRUE for seed and Series A (named in the articles).
- Linked API: 3 workflows used; no parked exit-3 workflows.
