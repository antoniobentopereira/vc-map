## Agent skills

### Issue tracker

Issues and specs are local markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-label vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.

### Testing and checks

Test and data-check commands, and the agreed test seams: `docs/agents/testing.md`.

### Researching a company

Read `docs/data-model.md` (every field and rule) before writing any row to `data/`, and `docs/research-recipe.md` (where to look, in what order, and when to stop) before researching. LinkedIn is read only through `python scripts/linkedin.py` (Linked API, read-only, last resort; ADR 0010), never directly.
