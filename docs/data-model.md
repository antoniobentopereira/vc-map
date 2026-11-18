# Data model

The Dataset is a set of CSV files in `data/`, edited by hand. `python scripts/check_data.py` enforces everything marked as a rule below. Terms are defined in `GLOSSARY.md`; the reasons are in `docs/adr/`.

| File | One row per | Filled by |
|---|---|---|
| `companies.csv` | Portfolio company | Roster and logo scripts, plus `researched_on` by hand |
| `claims.csv` | Claim (one fact about a company) | Research |
| `rounds.csv` | Round (any funding event, with or without Norte) | Research |
| `fx.csv` | Currency and year (annual average rate) | Research, when a Round needs it |
| `sectors.csv` | Sub-sector, mapped to its Sector | Research adds sub-sectors; Sectors are assigned after the whole portfolio is classified |

## companies.csv

`researched_on` is the date (`2026-11-18`) a company was last fully researched. If it is set, a field with no row means "not publicly available as of that date". If it is empty, the company has not been researched yet.

## claims.csv

Columns: `company, field, value, source_url, basis, confidence, note`.

Rules for every Claim:

- One Source link per Claim, valid http(s).
- `basis` is `reported` (a Source states it) or `estimated` (we deduced it; the reasoning goes in `note`).
- `confidence` is `high`, `medium` or `low`.
- Values stay on one line, and descriptions are written in our own words (short quotes only).
- **One value per field.** A single-value field has at most one row per company. When Sources conflict, weigh them, keep the most likely value (the one we are most confident in), and write the discarded values and the reasoning in its note.
- Missing information gets no row. It is recorded in the research notes, and `researched_on` tells the site it was looked for.

### Single-value fields

| Field | Value |
|---|---|
| `description` | One or two sentences on what the company does. |
| `long_description` | One paragraph on product, customers and business model, from one Source. |
| `sub_sector` | A detailed label, such as `Industrial predictive maintenance`. It must be listed in `sectors.csv` first, so labels are reused rather than reworded. |
| `hq` | Current headquarters, as `City, Country` (country name in English). HQ is where the company says its headquarters is; legal incorporation (such as a US holding company) never counts. |
| `hq_at_first_investment` | HQ when Norte first invested, same format. |
| `year_founded` | A four-digit year. |
| `status` | Operating status (table below). |
| `business_model` | `b2b`, `b2c` or `b2b2c`. |
| `acquirer` | Who acquired the company, if it was acquired. |
| `acquisition_year` | A four-digit year, not before `year_founded`. |

### List fields (one row per value)

| Field | Value |
|---|---|
| `founder` | One Founder's name. |
| `market` | One country where the company operates or sells. |
| `accelerator` | One accelerator programme, such as `Y Combinator` (batch in the note). |
| `milestone` | `date: event`, where the date is `2021`, `2021-03` or `2021-03-19`. Milestones are non-funding events (launches, pivots, offices, HQ moves); Rounds come from `rounds.csv`, and the site puts both on one timeline. |

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
- `norte_participated`: `TRUE` or `FALSE`. If Norte is not named in any Source for a Round, record `FALSE` with a lower Confidence and say so in the note.
- Same Source, Basis, Confidence and one-line rules as Claims.

### Derived views (not stored)

`scripts/derive.py` computes these from a company's Rounds, in Glossary terms:

- **First investment** (the first Norte round): the earliest Round with `norte_participated` TRUE. Its year, type, size and co-investors are the investment year, round type, round size and co-investors.
- **Last round:** the latest Round that is not `debt`, whether or not Norte took part.
- **Follow-on** (`norte_follow_on` on the site): TRUE if Norte took part in more than one Round, FALSE if in one, unknown if in none recorded.

Rounds are ordered by year, then by stage within a year. A Round of `unknown` type has no stage, so within its year it comes before every known stage. The last Round can be the same as the first investment.

## fx.csv

Columns: `currency, year, rate, source_url`. `rate` is the annual average, in units of the currency per US dollar. Use the central bank of the currency: Banco Central do Brasil (PTAX, SGS series 3694) for BRL, Banxico for MXN, and that country's central bank for any other. A year with no published average yet cannot be converted; the Round keeps its reported amount and currency, and `size_usd` is filled once the average is added here.

## sectors.csv

Columns: `sub_sector, sector`. Each sub-sector appears once. `sector` stays empty until the whole portfolio is classified; then sub-sectors are grouped into broader Sectors here, in one place.
