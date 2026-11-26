# Data model

The Dataset is a set of CSV files in `data/`, edited by hand. `python scripts/check_data.py` enforces everything marked as a rule below. Terms are defined in `GLOSSARY.md`; the reasons are in `docs/adr/`.

| File | One row per | Filled by |
|---|---|---|
| `companies.csv` | Portfolio company | Roster and logo scripts, plus `researched_on` by hand |
| `claims.csv` | Claim (one fact about a company) | Research |
| `rounds.csv` | Round (any funding event, with or without Norte) | Research |
| `fx.csv` | Currency and year (annual average rate) | Research, when a Round needs it |
| `sectors.csv` | Sub-sector, mapped to its Sector | Research adds sub-sectors; every one must have a Sector |

## companies.csv

`logo_crop` and `logo_background` are the two choices the logo studio saves for each logo (ADR 0015); never set them by hand or in research. Both are cleared whenever the logo file is replaced, and a company with no logo cannot have either.

- `logo_crop` is the crop box on the raw logo as four fractions of the image, `x,y,w,h` (left, top, width, height), for example `0.1,0.2,0.5,0.5`. The box may extend past the image's edges (for example `-0.25,-0.25,1.5,1.5`), which adds transparent padding around an oversized logo; it must overlap the image and be at most 3 times its size. Empty means the whole image.
- `logo_background` is the fill behind the mark in the logo circle, as `#rrggbb`. Older rows still use the previous meaning, which page background the logo is legible on: `dark`, `light` or `both`; those stay valid until every logo is confirmed. Empty means not reviewed yet.

`python scripts/logo_circle.py` rebuilds every circle (512px WebP in `site/logos/circles/`) from the raw logo and these two columns; SVG logos need PyMuPDF (`pip install pymupdf`); rows without a `#rrggbb` fill get none, and the site falls back to the raw logo clipped to a circle.

`researched_on` is the date (`2026-11-18`) a company was last fully researched. If it is set, a field with no row means "not publicly available as of that date". If it is empty, the company has not been researched yet.

Renamed companies: Norte's portfolio page may still link an old domain. Zivo was Comp (`trycomp.io`) and Attach Media Partners was Supercompany (`supercompany.io`); each is one company, listed once under its current name.

## claims.csv

Columns: `company, field, value, source_url, basis, confidence, note`.

Rules for every Claim:

- One Source link per Claim, valid http(s). For company registry facts (Brazil's CNPJ data: opening date, registered address, administrators), the lookup URL `https://brasilapi.com.br/api/cnpj/v1/<cnpj>` is an accepted Source; it need not be an exact page about the fact. The registered seat is not the HQ unless the company also says so, so use it as Estimated. A LinkedIn company page, profile or post is also accepted when its content was actually read, by the owner or through Linked API (ADR 0010; the note says "via Linked API" and the date). A company page's "Founded" year is set by the page admin and is often the page's creation year, so it never sets `year_founded` on its own; a founder's start date in that company, from their profile, can (Estimated).
- `basis` is `reported` (a Source states it) or `estimated` (we deduced it; the reasoning goes in `note`).
- `confidence` is `high`, `medium` or `low`.
- Values stay on one line, and descriptions are written in our own words (short quotes only).
- **One value per field.** A single-value field has at most one row per company. When Sources conflict, weigh them, keep the most likely value (the one we are most confident in), and write the discarded values and the reasoning in its note.
- Missing information gets no row. It is recorded in the research notes, and `researched_on` tells the site it was looked for.

### Single-value fields

| Field | Value |
|---|---|
| `description` | One or two sentences on what the company does. |
| `long_description` | The company's profile in our own words, as long as the sources support: what it does and for whom, each product, how it makes money, where it came from (the founders' story, the problem they started with), traction with dates and numbers, and where it is heading. Aim for roughly 1,500 to 4,500 characters (about 10 times the `description`) when there is that much to say; a company with little public coverage gets a shorter text, never padding or guesses. One line. `source_url` is the main page it draws on; every other page used goes in the `note`, and every page named must have been read. |
| `investment_thesis` | Why this company is worth backing, in our own words and on one line, as long as the evidence supports (aim for roughly 1,500 to 4,000 characters). Cover, in this order when possible: the problem and who has it; the logic of the business (why this solution works, why now); the size of the market and the share the company can realistically reach; what it does differently and why it is special; why it fits Norte (how its founders, stage and needs match what Norte says it looks for); and the main risks. Mostly deduced, so Basis is `estimated`, Confidence is the weakest link, and the `note` shows the reasoning: each market-size figure with its source (or the arithmetic behind our own estimate), and the pages used. Own research from sources not about the company (industry reports, central-bank or statistics data, comparable companies) is allowed, if the page was read. Never state Norte's own reasoning as fact unless a Source (a Norte page, a partner's quote) says it. |
| `sub_sector` | A detailed label, such as `Industrial predictive maintenance`. It must be listed in `sectors.csv` first, so labels are reused rather than reworded. |
| `hq` | Current headquarters, as `City, Country` (country name in English). HQ is where the company says its headquarters is; legal incorporation (such as a US holding company) never counts. |
| `hq_at_first_investment` | HQ when Norte first invested, same format. |
| `year_founded` | A four-digit year: the start of work, the earliest year the company itself counts as a working company. It can precede legal registration; give the registration date in the note when it differs. |
| `status` | Operating status (table below). |
| `business_model` | `b2b`, `b2c` or `b2b2c`. |
| `acquirer` | Who acquired the company, if it was acquired. |
| `acquisition_year` | A four-digit year, not before `year_founded`. |

### List fields (one row per value)

| Field | Value |
|---|---|
| `founder` | One Founder's name: a person who started the company. Someone who joined later, or who co-founded only a later holding company or restructuring, is not a Founder (a leadership change can be a Milestone). |
| `market` | One country where the company operates or sells. |
| `accelerator` | One accelerator programme, such as `Y Combinator` (batch in the note). |
| `milestone` | `date: event`, where the date is `2021`, `2021-03` or `2021-03-19`. Milestones are the non-funding events that tell the company's story (launches, pivots, offices, HQ moves, accelerators, acquisitions it makes, key hires, big customers, product lines, user or revenue marks, awards, licences). Write each as one or two sentences that say what happened and why it mattered, not a bare label, and cover the whole history from the first product to the latest news. Aim for 8 to 15 per company when the sources support it; fewer when they do not. Rounds come from `rounds.csv`, and the site puts both on one timeline. Corporate housekeeping (legal registration, holding companies, restructurings) is not a Milestone. |

### Status

| Value | Meaning | Usual Basis |
|---|---|---|
| `stealth` | Operating but not publicly launched | reported or estimated |
| `active` | Evidence of activity in the last ~18 months | estimated, with the latest evidence as the Source |
| `inactive` | No recent activity found, but no confirmed shutdown | estimated, low or medium Confidence |
| `closed` | A Source confirms it shut down, or its brand was discontinued | reported |

Acquisition is recorded separately (`acquirer`, `acquisition_year`). An acquired company that keeps operating stays `active`. An Exit (`is_exit` in `companies.csv`) is what the Firm lists; it need not be an acquisition, since Norte may have sold its stake to someone else.

## rounds.csv

Columns: `company, year, type, reported_amount, reported_currency, size_usd, co_investors, norte_participated, source_url, basis, confidence, note`.

- Record every Round found, whether or not Norte took part. If no evidence of a Round exists, there is no row.
- `type` is one of `angel`, `pre_seed`, `seed`, `series_a`, `series_b`, `series_c`, `series_d`, `series_e`, `series_f_plus`, `unknown`, `debt`.
  - Extensions and bridges take their base type (a seed extension is `seed`), and the note says so.
  - Debt and credit facilities are `debt`. They are recorded, but never count as the last Round.
  - `unknown` only when the Round exists but no Source states its type.
- Size: `reported_amount` and `reported_currency` are the total Round size as the chosen Source reports it (a whole number and a code such as `BRL` or `USD`). `size_usd` is that amount in whole US dollars, divided by the `fx.csv` rate for that currency and year and rounded; the check script recomputes it. If the size is not disclosed, all three stay empty. If the year's annual average is not published yet, `size_usd` alone stays empty until it is.
- **One row per Round.** A second row with the same company, year and type is rejected; weigh conflicting figures and put the discarded ones in the note. Debt and `unknown` Rounds are told apart by amount, since a company can take several in one year.
- `co_investors`: everyone else in the Round except Norte, separated by `; `, with `(lead)` or `(co-lead)` after the name. Use one name per investor across all Rounds (`Next47`, even where a Source writes `N47`) and note the Source's spelling.
- `norte_participated`: `TRUE`, `FALSE` or `UNKNOWN`. `TRUE` when a Source names Norte in the Round. `FALSE` only when a Source lists the Round's investors (or says who took part) and Norte is not among them, and no other Source places Norte there. `UNKNOWN` when the Sources do not settle it (Norte not named in a partial list, or an aggregator lists Norte without a Round); the note says what was found. Never use `FALSE` for "not named".
- Same Source, Basis, Confidence and one-line rules as Claims.

### Derived views (not stored)

`scripts/derive.py` computes these from a company's Rounds, in Glossary terms:

- **First investment** (the first Norte round): the earliest Round with `norte_participated` TRUE. Its year, type, size and co-investors are the investment year, round type, round size and co-investors.
- **Last round:** the latest Round that is not `debt`, whether or not Norte took part.
- **Follow-on** (`norte_follow_on` on the site): TRUE if Norte took part in more than one Round, FALSE if in one and no other Round is `UNKNOWN`, unknown if in none recorded or if an `UNKNOWN` Round could still change the answer.

An `UNKNOWN` Round is never counted as an Investment. If one comes before the first investment, the real first investment may be earlier than the derived one.

Rounds are ordered by year, then by stage within a year. A Round of `unknown` type has no stage, so within its year it comes before every known stage. The last Round can be the same as the first investment.

## fx.csv

Columns: `currency, year, rate, source_url`. `rate` is the annual average, in units of the currency per US dollar. Use the central bank of the currency: Banco Central do Brasil (PTAX, SGS series 3694) for BRL, Banxico for MXN, and that country's central bank for any other. A year with no published average yet cannot be converted; the Round keeps its reported amount and currency, and `size_usd` is filled once the average is added here.

## sectors.csv

Columns: `sub_sector, sector`. Each sub-sector appears once. `sector` is required: every sub-sector belongs to one of the broader Sectors, grouped here in one place. A new sub-sector needs a Sector when it is added (reuse an existing one where it fits). The Sector list and icons for the Sector Lens are in `site/src/sectors.ts`.
