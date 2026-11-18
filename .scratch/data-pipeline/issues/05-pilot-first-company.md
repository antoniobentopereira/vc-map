# 05: Pilot: research the first company end to end

**What to build:** One Batch 1 company (Tractian) researched across every field in `docs/data-model.md` (the Claims plus every Round found) using only public sources. Every Claim and Round has a source link, a Basis and a Confidence. Missing information is recorded as missing; deduced facts are Estimated with their reasoning in the note. The check script passes and the owner reviews this one company. Findings (what worked, what was unavailable) go into a short notes file.

**Blocked by:** 03 (Check script), 04 (Choose the Pilot's 10 companies).

**Status:** resolved

The owner's first review (2026-11-18) led to a revised data model (ADRs 0005 to 0007, `docs/data-model.md`); Tractian was redone in it and the owner approved the result.

- [x] All fields are either filled with a sourced Claim or Round, or recorded as missing
- [x] The check script passes
- [x] The owner has reviewed the company and given feedback (two reviews; the second approved the revised data)
- [x] Notes on the process and source availability are written down
