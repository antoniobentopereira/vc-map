# Sub-agent run: NG.CASH, CredAluga, Flieber (ticket 11), 2026-11-19

The owner delegated the choice ("choose any 3 with no rows in claims.csv"); no control company was used, so there is no field-by-field comparison. Three sub-agents ran in parallel; none edited `data/` (checked by diff before consolidating).

| | NG.CASH | CredAluga | Flieber |
|---|---|---|---|
| Page reads (Pilot: 8 to 20) | 14 (+1 404) | about 12 (+1 403) | 7 (+8 failed) |
| Linked API workflows (max 4) | 3 | 3 | 4 (1 unresolved) |
| Claim rows | 19 | 13 | 12 |
| Rounds | 5 | 3 | 1 |
| Norte TRUE / FALSE / UNKNOWN | 1 / 0 / 4 | 2 / 0 / 1 | 0 / 0 / 1 |

## What each source added
- **Registry:** NG.CASH (opening date 2021-02-04, seat) and CredAluga (opening date, administrators, foreign LLC partner since 2025-01, a lead only). Not applicable to Flieber (US company).
- **Linked API:** only one useful result. CredAluga's company search gave Alphaville (Barueri) as HQ, used as the low-confidence HQ claim. NG.CASH's founder-post query returned only 2026 posts, no round announcements, and one search-posts hit (Mario Sá, 2025-11-19) suggesting Norte was in the 2021 pre-seed, not usable as a Source. Flieber's four workflows gave nothing. So Linked API added no Norte `TRUE`; the TRUE rows came from press.

## Consolidation
- Added sub-sectors: Youth digital banking, Rental guarantees, Inventory planning software (sector column left empty, as for the existing rows).
- Fixed: NG.CASH Series A `size_usd` 12054897 to 12054896 (check script rounding).
- Verified myself: Norte named in the CredAluga seed and Series A articles (startups.com.br, Portas) and the NG.CASH seed article.
- Not changed, but weak: CredAluga HQ (Barueri vs Belo Horizonte, low); Flieber third founder (one source, low) and its Round, where Norte appears only on aggregators (so UNKNOWN); CredAluga OLX US$5M may double count the Series A.
- `researched_on` set to 2026-11-19 for all three. `check_data.py` passes; 104 unit tests pass.

## Problems in the run
- The agents wrapped Linked API calls in their own timeouts. Workflows queue behind each other (one at a time on the account), so three calls were killed (CredAluga 1, Flieber 1) or their output lost (NG.CASH 1); none printed a workflowId, so none could be fetched later. Flieber's last workflow ended parked (exit 3, "usually takes about 6-8 minutes") with no workflowId printed, so it cannot be fetched with `result`; the client should print the workflowId before waiting. A re-run (budget already used) could settle Norte in Flieber's Series A.
- Flieber is the thin one: About and Careers 404, aggregator-only earlier rounds, no Brazilian coverage. About 8 of its fetches failed.

## Retries (2026-11-20, run sequentially from the main session)
- CredAluga `company .../credaluga` (`wf-8e1bbb05-b906-4247-873a-56608833346c`, exit 0): location "Alphaville, São Paulo", offices in São Paulo and Minas Gerais. HQ claim upgraded to Reported, medium.
- Flieber `company .../flieber --posts 20` (`wf-e9502f4b-2981-455b-8b00-4597bb5fcf33`, exit 0; 5th workflow, over the budget at the owner's request): New York and 2019 confirmed (already in data); posts reach back only to 2026-05, none on rounds or Norte. No change; Norte stays UNKNOWN.
- NG.CASH: nothing to retry; its lost workflow 2 had already been re-run as workflow 3.

## Decision (2026-11-20)
The owner chose to stay sequential: one company at a time, in Batches the owner sizes (ADR 0011). The client now prints the `workflowId` as soon as a workflow starts and returns it when parked, so a cut-off workflow can always be fetched with `result`.

## Recommendation (superseded by the decision above)
Use sub-agents for Scale-up, after changing the recipe: (1) tell agents never to wrap `linkedin.py` in a timeout and to record the workflowId (have the client print it first, or run the Linked API step in the consolidating session, serially); (2) keep the 4-workflow budget but count queued time as expected. Reads were within the Pilot range and rows passed the check with one rounding fix. Linked API paid off once in three companies, so keep it last-resort. Owner review of the three companies is still pending.
