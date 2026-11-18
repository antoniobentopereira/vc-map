# CSV files in data/ are the single source of truth; two tables, one row per Claim

The Dataset lives in plain CSV files in `data/`, committed to git, which also gives history. The owner edits them by hand in VS Code, using a CSV/table-view extension for a spreadsheet-style view. We use no Google Sheets, connectors, syncing or import/export steps. Google Sheets was considered first and dropped: automatic syncing was the riskiest, most complex part of the plan, for a project meant to stay simple.

There are two tables: `companies` (one row per Portfolio company) and `claims` (one row per fact: company, field, value, source_url, basis, confidence, note). There is deliberately no separate sources table: a Source is just a link on the Claim row, and several Sources for one fact are several rows. A check script validates the files before any site JSON is generated.
