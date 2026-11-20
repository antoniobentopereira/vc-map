# Research runs one company at a time, in Batches the owner sizes

Ticket 11 ran three companies in parallel, one sub-agent each. The reads and rows were in line with the Pilot, but Linked API runs one workflow at a time on the owner's account, so the agents' LinkedIn steps queued behind each other. Waiting agents gave up on their own timeouts, and four workflows were cut off or their output lost. The step that most needs care was the one parallelism broke.

So the owner decided (2026-11-20) to drop sub-agents. Research runs in the main session, one company at a time, from the site through Linked API, and each company's rows go straight into `data/` and pass the check script before the next company starts. The owner names how many companies each Batch holds. Proposals, the intermediate files that let several agents avoid editing `data/` at once, are no longer needed.

We accept that a Batch takes longer end to end, in exchange for no queue between companies, one place that edits `data/`, and each company fully checked before the next.
