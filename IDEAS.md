# VC Map: Ideas

An unofficial, static, interactive visual exploration of Norte Ventures and the companies it has invested in. Not affiliated with Norte.

This file holds concepts and future possibilities only. It is the parent roadmap for planning sessions.
- Current project state is not tracked here; see `STATUS.md`.
- What exists in the data is visible in the repo itself, so it is not repeated here.
- Anything written here about build order, data tasks or open questions is a starting opinion to be challenged during planning, not a decision.

---

## 1. Core concept: floating logo dots + lenses

The whole project is one canvas holding one dot per portfolio company. Each "lens" is a layout. Switching lens animates every dot from where it is to its new place. The dot engine is built once and every view reuses it.

### Home page
- The logos float around the full screen like gas atoms: slow random drift, soft collisions, gentle reaction to the cursor.
- A lens selector somewhere on screen (placement to be decided).
- A "Play" button for the quiz.
- Very minimal design.

### Technical direction (to be challenged)
- One shared dot engine: positions, a physics simulation, animated transitions between layouts.
- A lens is a function that receives the companies and returns target positions, plus labels, clusters and decorations. New lenses should be addable without touching the engine.
- The number of logos is small, so SVG or DOM elements may be enough; canvas only if performance requires it.
- The site stays static (no backend), in line with antoniobento.me. Data is prepared at build time from the CSVs.

---

## 2. Lenses (views)

### 2.1 Country view (map)
- The page becomes a minimalist world map: thin border lines and key country names only.
- It opens with a slow zoom-in onto the regions where Norte has companies, so regions without companies (Asia, Africa, most of Europe) do not take up screen space.
- The floating logos fly to their place on the map during the zoom.
- **Dynamic clustering** (reference: the QuintoAndar Rio de Janeiro map):
  - Locations are grouped into numbered circles sized by how many companies they hold.
  - Progressive zoom: clicking a cluster zooms in and splits it. Example: click a large number over Brazil, the map becomes Brazil with thin state borders and main state and city names, showing state-level clusters. Click a state cluster to see individual companies.
  - Single-company rule: a cluster of 1 shows the company logo instead of a number.
- Possible approach: hierarchical clusters (country, then state, then city) instead of distance-based clustering, since it matches the drill-down.
- Companies with unknown HQ need a holding area.
- Later extras: arcs for HQ moves (HQ at first investment to HQ now); a layer for the markets each company operates in.

**Data needs:** coordinates for HQ locations; boundary data for the world and for Brazilian states.

### 2.2 Sector view
- The floating logos group into floating balls of logos, one ball per sector.
- Above each ball, an icon and a title (e.g. hospital symbol + "Health").
- Possible second level: click a sector ball to split it into sub-sector balls.

**Data needs:** the mapping from sub-sectors to broader sectors; one icon per sector.

### 2.3 Founding Year view
- The page becomes a vertical scroll with one band per year, youngest on top, oldest at the bottom.
- Each band holds the logos of companies founded that year.
- Each band also shows a few world and tech events of that year, very minimal (e.g. 2022: tank icon + Russia and Ukraine flags + "Russia invades Ukraine").
- Inside a year, logos and events are ordered by month: earlier in the year lower, later in the year higher.

**Data needs:** founding month per company (new research, flagged as estimated when unknown); a curated list of world and tech events with dates and sources.

### 2.4 Investment (money raised) view
Split screen:
- **Right side, funding mechanism:** an interactive drop zone (drag money sacks into a box, or a coin-pusher slot) with a live money counter underneath, plus a way to take money out.
- **Left side, portfolio reveal:** starts empty. As the counter rises past a company's total raised, its logo drops from the sky onto a pile. Removing money makes logos vanish with a small bubble-pop. Companies that raised the most land on top because they unlock last.

**Open points:** linear or log scale on the counter; where companies with no known amount go.
**Data needs:** total raised per company, derived from the rounds data.

### 2.5 Status view
Simple layout with groups such as Stealth, Active (independent), Active (acquired), Inactive, Closed.

**Data needs:** a clear rule combining status, acquirer and the exit flag, so each company lands in exactly one group (Hyperplane is a case to look at: closed and acquired).

### 2.6 Employee Count view (future)
Same split screen as the Investment view, playful version:
- **Right side, stick-figure sandbox:** a tiny town. Buttons `+1`, `+10`, `+100` drop that many stick figures from the sky. Remove them with playful weapons: bombs, swords, anvils.
- **Left side, portfolio reveal:** logos appear once the headcount reaches each company's employee count, and disappear when it drops below.

**Data needs:** employee counts (not collected yet).

---

## 3. Norte Timeline view

A horizontal timeline of Norte's history from its start to today.
- **Scroll to move:** scrolling down moves the page horizontally from left (beginning) to right (today).
- **Investment track (bottom):** company bubbles placed on the exact or estimated date of each Norte investment, with a small tag above (Seed, Series A...). Only rounds Norte took part in; other investors' rounds are not shown. Checkpoints on the track mark key moments, such as Fund II starting (2022) and Fund III (2026).
- **Fund bubbles (top):** large bubbles that inflate as you scroll past investments.
  - Fund I: starts tiny, grows with each company, shows a running total of estimated capital deployed (based on public interview figures of roughly US$50k to 100k per startup; the exact figure is to be set in the data later).
  - Fund II: appears at the 2022 checkpoint and grows with its investments.
  - Fund III: appears at the 2026 checkpoint as a "Coming soon" placeholder.
- Estimated entries are drawn differently from confirmed ones (e.g. dashed bubble), so uncertainty is visible.

**Data needs:** Norte's entry round and date per company, with basis and confidence, including an estimation rule where Norte's participation is not confirmed; fund start dates and the average check estimate.

---

## 4. Quiz game (Kahoot-style)

Questions are generated automatically from the data. Start with all facts, then add a setting "only high-confidence facts".

Modes:
- **Guess the logo.** Easy: multiple choice. Hard: type the name.
- **Higher or lower.** "Did Kanastra raise more than Cayena?" "Which was founded first?"
- **Who led the round?** Pick from four VCs.
- **Read the thesis, name the company.** Thesis shown with the company name blanked out.
- **Pin the HQ.** Drop a pin on a map.
- **Match founders to companies.**

Mechanics: timer, streaks, daily challenge, flashcard mode for review.

**Data needs:** mostly present. "Who led" needs normalized investor names; "Pin the HQ" needs coordinates; thesis mode needs name blanking.

---

## 5. Investors views

- **Orbit view.** Norte at the centre; other VCs orbit it, closer when they share more companies. Click a VC to light up the shared companies.
- **Leaders and followers.** Scatter of companies shared (x) against rounds led (y). Leaders such as Monashees and Kaszek sit in the "leaders" corner; Latitud and FJ Labs in "always there, never leading". Show the important names individually and cluster the rest into numbered clusters.
- **Top pairings.** A simple top-50 list of VC pairs that most often appear in the same rounds.

**Data needs:** a table of investor name variants (e.g. MAYA Capital / Maya Capital, ONEVC / OneVC, GGV Capital / Notable Capital) so counts do not split; a decision on how to treat angels and "founders of X" entries.

---

## 6. Other views

### 6.1 Theme Explorer
Cross-sector discovery by searching descriptions and theses. Recurring themes (WhatsApp, Pix, AI agents, FIDC/credit, stablecoins) become clickable tags.
- Search bar plus theme tags.
- Results ranked in three tiers, with sector boundaries kept visible:
  - **High:** the theme is the core product (e.g. a WhatsApp-native platform).
  - **Medium:** the theme powers a major secondary feature (e.g. Decade's WhatsApp bot).
  - **Low:** the theme is only touched lightly.

**Data needs:** theme tags with a relevance tier and a reason per company; free-text search can run over the existing descriptions.

### 6.2 "How early does Norte get in?"
Scatter of founding year against the year of Norte's first check, showing how many years after founding Norte usually enters.
**Data needs:** same Norte entry data as the Timeline.

### 6.3 Exit Wall
A small hall of fame for exits: logo, acquirer, year.
**Data needs:** consistent exit and acquirer data (see Status view).

---

## 7. Parked (write down, build later)

### 7.1 Receipts mode
A global toggle that fades every estimated or low-confidence fact. Clicking any number opens its source. Shows how rigorous the research is.
Design implication to keep in mind early: every number on screen should keep a path back to its source row in the data, so this mode can be added without a rewrite.

### 7.2 Founder graph
A graph of founders linked by shared experience: prior VC experience, prior startup, ex-Nubank, ex-Stone, US or Brazil education, Harvard alumni, etc. Tags act like stars and founders cluster around them. This can be a separate section or even a separate project.
- Can start with data that already exists: founders who also appear as angels in other portfolio companies.
- Needs new research: structured tags per founder, each with a source, basis and confidence.

### 7.3 Business model view
Idea was unclear and is parked. Simplest version: B2B / B2C / B2B2C as one more grouping lens.

---

## 8. UI and design quality direction

Goal: consistent, polished, minimal visuals across all lenses, without every view looking like a different project.

- Bring UI-focused Claude Code skills into the workflow (ones used by strong frontend and UI developers) to improve output quality and consistency. Which ones to adopt is to be decided during planning.
- Candidates already visible in this Claude setup: a frontend design skill (distinctive, non-templated UI) and a data visualization skill (chart and color consistency). Others to be researched.
- Define a small design system early (colors, type, spacing, motion rules, how dots, labels and clusters look) so every lens reuses it.
- Use a visual review loop while building: build, look at it in the browser, compare against the intended look, iterate.
- Use throwaway prototypes for feel-based questions (floating physics, money pile, map zoom) before committing to a design.
- Minimal design is a requirement of the concept, so restraint is part of quality here.

---

## 9. Initial opinion on order of work (to be heavily challenged)

This is a first guess only. The final order should come out of the planning session, after this has been questioned.

Reasoning behind the guess:
- Prove the dot engine early, using views whose data is easiest.
- Ship something visible fast, then build the harder, data-heavy views.
- Do data work alongside building, driven by what each view needs.

Rough sequence:
1. Foundation: data preparation, home page with floating logos, the dot engine, the simplest lenses (Status, Sector).
2. Quiz v1: Guess the logo and Higher or lower (independent of the dot engine).
3. Money and time: Investment view, Norte Timeline, "How early does Norte get in?", Exit Wall.
4. Map: Country view with clustering, Pin the HQ quiz mode.
5. Network and themes: Investors views, Theme Explorer.
6. Data-heavy extras: Founding Year view, Receipts mode, Employee view, Founder graph.

Things planning should question: whether the quiz should come earlier or later, whether the map is harder than it looks, whether the Timeline should wait for better data, and what the smallest impressive first release is.

---

## 10. Proposed starting questions for planning (not prerequisites)

These are suggested openers. Better questions should replace or add to them as planning goes.

1. Framework: plain HTML/JS with D3, or a framework? What does the rest of antoniobento.me use, and does VC Map live in the same repo or on its own?
2. Rendering: SVG/DOM logos or canvas?
3. Animation: d3 only, or add an animation library for the drops, pops and zooms?
4. How is data shipped to the site: prepared into one file at build time, or read directly?
5. Mobile: do all views need to work on a phone, or is it desktop-first with a simpler fallback?
6. Lens selector: where it sits and how people discover it.
7. Investment view: counter scale, and where companies with no known amount go.
8. Timeline: how to estimate Norte's entry date when it is not confirmed, what counts as Norte's start, and sources for fund dates.
9. Status: the final list of groups and the rule for each company.
10. Quiz: any score history (local only) and a shareable result?
11. Source traceability: what identifier links a dot or number back to its data row (needed for Receipts mode)?
12. Disclaimer: on every view or only the home page?

---

## Proposed: STATUS.md

Suggestion for the planning session: create a short `STATUS.md` in the project root to track the current state of the project and recent changes, so new sessions do not have to re-scan everything from scratch. The planning session should decide whether to do this, and what it contains.

Ideas for what it could hold:
- Current phase and what is in progress.
- What is done, and what is known to be missing.
- Decisions made (one line each, pointing to the ADR when one exists).
- A short log of recent changes, newest first, with dates.
- Data caveats worth remembering.

Ideas for how it should behave:
- Stay short and current. It records state, not concepts: concepts stay in `IDEAS.md`.
- Updated at the end of each working session.
- When it disagrees with the repo, the repo wins and the file gets fixed.
- Avoid static counts that go stale; point to where the live numbers can be found.