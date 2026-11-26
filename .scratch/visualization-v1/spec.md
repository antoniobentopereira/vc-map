# Spec: Visualization v1 (Float home, Sector Lens, navigation shell, Company card and profile)

**Status:** ready-for-agent

## Problem Statement

The Dataset is finished: all 130 Portfolio companies have been researched, with Claims, Rounds and Original logos in `data/`. But it can only be read as CSV rows or in the internal profile viewer. Nobody outside the project can see it, and none of the ideas in `IDEAS.md` (Lenses, Views, the Quiz) exist yet.

Three things stand in the way of a first public release. Logos come in uneven shapes and formats, so they can't be shown as uniform Logo dots. No Sub-sector has a Sector yet. And there is no site: no engine, no shell, no way to open a company.

## Solution

A first public release of the Visualization, served as a static folder under antoniobento.me:

- **Home is the Float Lens.** All 130 Logo dots drift around the screen like gas atoms, bump into each other softly and move away from the cursor. Each dot is a uniform circle showing the company's Original logo on a chosen fill color.
- **The Sector Lens is the first grouped Lens.** Choosing it animates every Logo dot into one floating ball per Sector, each with an icon and a title. Choosing Float releases them back to drifting. On phones, the balls stack into a vertically scrollable stage.
- **The full navigation shell is in place from day one.** It has a bottom pill bar of every Lens, a top bar with a navigation menu of every View plus the Receipts toggle, a Play button and a `?` About button. Everything not built yet is visible but greyed out, so visitors see where the project is heading.
- **Clicking a Logo dot** stops it and opens a small, centered **Company card**. From the card, "Open full card" leads to a first-version **Company profile** with everything the Dataset knows about that company.
- **Estimated values always look different** from Reported ones, by one consistent convention that the About panel explains.
- **Every Lens, View and Company profile has its own shareable address.**
- **The site is desktop-first.** Float, the shell, the card and the profile still work on a 320px phone by tap. A footer line says the project is unofficial and works best on desktop.

Supporting work that comes with it:
- the Sub-sector to Sector mapping;
- a local **logo studio** where the owner crops each logo and picks its circle fill;
- a script that rebuilds every logo circle from those saved choices;
- a script that builds the site's single data file from the CSVs;
- an explicit command that copies the built site into the personal site's folder.

## User Stories

### Visitor: home and Float
1. As a visitor, I want the home page to open straight onto all 130 Logo dots floating, so that I immediately see the size and variety of the portfolio.
2. As a visitor, I want the dots to drift slowly and bump into each other softly, so that the page feels alive without being distracting.
3. As a visitor, I want the dots to move gently out of my cursor's way, so that the page reacts to me.
4. As a visitor on a phone, I want a tap on empty canvas to give the dots a brief push, so that touch has a reaction too.
5. As a visitor, I want every dot to be the same-size circle with the logo neatly fitted, so that the page looks intentional rather than a pile of mismatched images.
6. As a visitor, I want a thin ring around every dot, so that light-colored circles stay visible on the cream background.
7. As a visitor, I want the dots never to hide behind the top bar or the pill bar, so that every dot stays visible and tappable.
8. As a visitor, I want the motion to feel the same on any screen, so that a 120 Hz monitor doesn't make the gas move twice as fast.
9. As a visitor on a phone, I want to see all 130 companies at a size I can still tap, so that the phone shows the same portfolio as the desktop.
10. As a visitor on a phone, I want Float to fill one screen without scrolling, so that the floating effect stays whole.

### Visitor: Sector Lens
11. As a visitor, I want to pick the Sector Lens and watch every dot fly into one ball per Sector, so that I see how the portfolio splits across markets.
12. As a visitor, I want each Sector ball to have an icon and a title above it, so that I know which Sector it is without clicking.
13. As a visitor, I want the dots inside a ball to keep drifting gently, so that grouped dots still feel alive.
14. As a visitor, I want the balls never to overlap one another or the bars, so that every Sector reads as its own group.
15. As a visitor, I want to go back to Float and see the dots return to where they were and drift off again, so that switching feels reversible.
16. As a visitor on a phone, I want the Sector balls stacked in a page I can scroll vertically, so that the groups aren't cramped into one screen.
17. As a visitor, I want clicking a dot inside a Sector ball to open its Company card just as on Float, so that every Lens behaves the same.
18. As a visitor, I want a `#/sector` link to open directly on the Sector Lens, so that I can share it.

### Visitor: navigation shell
19. As a visitor, I want a bottom bar listing every Lens (Float, Sector, Status, Country, Founding year, Money raised, Employee count, Business model), so that I see all the ways the portfolio will be arranged.
20. As a visitor, I want Lenses that aren't built yet to be greyed out and marked as coming soon, so that I know the project is ongoing and nothing seems broken.
21. As a visitor on a phone, I want the Lens bar to scroll sideways, so that every Lens fits without an extra menu.
22. As a visitor, I want a clearly visible navigation menu in the top bar, so that I find the Views without hunting.
23. As a visitor, I want that menu to list every View in one flat list (Norte Timeline, Investors, Theme Explorer, How early does Norte get in?, Exit Wall, Founder graph), with the unbuilt ones greyed out, so that the menu is easy to scan.
24. As a visitor, I want Investors to be a single entry in the menu, so that the menu stays short and its three parts (Orbit, Leaders and followers, Top pairings) live inside that View.
25. As a visitor, I want to see a Receipts mode toggle in the menu, disabled for now, so that I know the research is sourced and a sourced mode is coming.
26. As a visitor, I want a Play button for the Quiz, disabled for now, so that I know a game is coming.
27. As a visitor, I want a `?` button that opens an About panel, so that I can learn what this project is.
28. As a visitor, I want the About panel to say that the project is unofficial and not affiliated with Norte Ventures, why it was built, and that it was built with AI, so that I understand its context.
29. As a visitor, I want the About panel to explain how Estimated values look and what Basis and Confidence mean, so that I can read the uncertainty markers everywhere else.
30. As a visitor, I want a small permanent footer line ("Unofficial project · not affiliated with Norte Ventures"), so that the notice is always visible without being loud.
31. As a visitor on a phone, I want a small note beside that footer line saying the site works best on desktop, so that I know a richer version exists.

### Visitor: Company card
32. As a visitor, I want to click or tap a Logo dot to open its Company card, so that I can find out what the company is.
33. As a visitor, I want the clicked dot to stop moving while its card is open, so that the dot and the card clearly belong together.
34. As a visitor, I want the card centered and minimal, showing name, logo, Sector, short description, year founded and Fund, so that I get the essentials at a glance.
35. As a visitor, I want Estimated values on the card styled differently from Reported ones, so that I'm never misled about how sure a fact is.
36. As a visitor, I want to close the card by clicking outside it, with a close button or with Escape, so that I can return to the floating dots easily.
37. As a visitor, I want the dot to start drifting again when I close the card, so that the page goes back to normal.
38. As a visitor, I want an "Open full card" button on the card, so that I can see everything known about the company.

### Visitor: Company profile
39. As a visitor, I want the Company profile to show the company's logo, name, Status and short description at the top, so that I know where I am.
40. As a visitor, I want a facts section (Sector and Sub-sector, Status, business model, year founded, HQ now and at the first investment, Fund, acquirer and acquisition year when acquired), so that the general facts come first.
41. As a visitor, I want to read the long description, so that I understand the company's story.
42. As a visitor, I want to read the Investment thesis, clearly labelled as our own estimated reasoning, so that I don't take it for Norte's own words.
43. As a visitor, I want the Founders, markets and accelerators listed, so that I see who started it and where it operates.
44. As a visitor, I want one timeline merging Milestones and Rounds in date order, with Rounds styled differently, so that I see the company's history in one place.
45. As a visitor, I want Rounds to show their type, year, size in USD and whether Norte took part (yes, no or unknown), so that I can follow the funding.
46. As a visitor, I want every value on the profile to give me a way to its Source, so that I can check it myself.
47. As a visitor, I want Estimated values on the profile styled with the same convention as everywhere else, so that uncertainty reads the same across the site.
48. As a visitor, I want fields that research found nothing for to say "not publicly available", so that a gap reads as "looked for, not found" rather than as an error.
49. As a visitor, I want a way back from the profile to the floating dots, so that I can keep exploring.
50. As a visitor on a phone, I want the profile to read well at 320px, so that a shared link works anywhere.

### Visitor: addresses
51. As a visitor, I want the address to change as I switch Lens or open a profile, so that I can share exactly what I'm looking at.
52. As a visitor, I want a shared profile link to open straight on that company's profile, so that sharing a company works.
53. As a visitor, I want an unknown or not-yet-built address to land me on Float, so that a broken link never shows a blank page.
54. As a visitor, I want the browser's back button to undo my last navigation, so that the site behaves like a normal website.
55. As a visitor using a keyboard or screen reader, I want a way to reach every company by name, so that the canvas doesn't lock me out.

### Owner: data and logos
56. As the owner, I want Claude to propose a short list of Sectors (about 8 to 12), each with an icon, and map all 122 Sub-sectors to them for my review, so that the card and the Sector Lens have a Sector to show.
57. As the owner, I want the check script to fail while any Sub-sector has no Sector, so that an unmapped company can never ship.
58. As the owner, I want a local logo studio that walks me through each logo in four steps (crop, pick fill, preview, confirm), so that every circle looks intentional.
59. As the owner, I want to crop away padding and borders by dragging a box, so that only the logo mark stays.
60. As the owner, I want to pick the circle's fill with an eyedropper or from presets (white, cream, Norte brown, black), so that the fill matches the logo.
61. As the owner, I want the studio to suggest a first fill from the old legibility value (dark, light or both), so that I start from a sensible guess.
62. As the owner, I want the preview to show the circle at its real sizes on the cream surface with its ring, so that I judge it as visitors will see it.
63. As the owner, I want wide wordmark logos fitted inside the circle and squarish marks filling it, so that neither is badly clipped.
64. As the owner, I want confirming to save my crop and fill to `companies.csv` and produce the circle at once, so that my choice is saved immediately and safe to rerun.
65. As the owner, I want a filter for logos I haven't confirmed yet, so that I can work through all 130 across several sittings.
66. As the owner, I want one command that rebuilds every circle from the saved choices, so that changing the size or format never means re-cropping by hand.
67. As the owner, I want replacing a logo file to clear its saved crop and fill, so that a stale crop is never applied to a new image.
68. As the owner, I want the check script to accept hex fills and the old words while I work through the logos, so that nothing breaks partway through.
69. As the owner, I want `docs/data-model.md` to describe the new and changed columns, so that the data model stays the one reference.

### Owner: build and publish
70. As the owner, I want one command that builds the site's single data file from the CSVs, so that the site always shows the current Dataset.
71. As the owner, I want that data file to carry each value's Basis, Confidence and Source, so that Receipts mode can be added later without a rewrite.
72. As the owner, I want the data build to refuse to run when the check script fails, so that invalid data never reaches the site.
73. As the owner, I want a local dev server with live reload, so that I can see changes while building.
74. As the owner, I want a build that produces a self-contained static folder with relative paths only, so that it works wherever it is copied.
75. As the owner, I want an explicit sync command that copies the built folder into the personal site's `public/vc-map/`, so that publishing is one deliberate step and never happens on save.
76. As the owner, I want `STATUS.md` updated as v1 progresses, so that a new session knows where things stand.

## Implementation Decisions

### Architecture (ADR 0001, ADR 0014)
- `site/` becomes a Vite + TypeScript project. Its build output is a self-contained static folder with relative paths only. No backend, no secrets.
- There are two layers with one interface between them:
  - **The engine** is plain TypeScript using PixiJS for drawing and d3-force for physics. It owns the stage, the Logo dots, the Lenses and the physics. Its interface is small: load the companies, set the Lens, set the viewport size and insets, be told when a dot is clicked, pause or resume a dot, and report the stage height. The engine never imports Svelte.
  - **Svelte** owns the DOM around the stage: the navigation shell, Company card, Company profile, About panel and footer. It talks to the engine only through that interface.
- Matter.js and GSAP are not used in v1. They are added only when a View first needs them.
- A **route** module maps hash addresses to app state and back. Addresses are `#/` (Float), `#/<lens>`, `#/<view>` and `#/company/<slug>`. Unknown or unbuilt addresses resolve to Float. The browser history follows navigation.
- A **Lens** is a pure layout function. It takes the companies, the viewport and the device class, and returns one target per Logo dot plus a stage height. Float returns no targets and keeps the stage height equal to the viewport. Grouped Lenses may return a stage taller than the viewport on phones, which becomes a vertically scrollable stage. Float never scrolls. A Lens also returns its decorations (for Sector: each ball's icon and title and where they sit), which the engine draws.
- **The Sector Lens** is the one grouped Lens in v1:
  - one ball per Sector, sized to the number of companies it holds;
  - balls packed so they don't overlap one another or the bars;
  - an icon and title above each ball;
  - on phones, balls stacked in one column inside the scrollable stage.
  - Sector icons are a small set of inline line icons in the ink color, one per Sector, chosen during the mapping review.
  - Splitting a Sector ball into Sub-sector balls is out of scope.
- For accessibility, there is a visually hidden, keyboard-reachable list of every company (name linking to its Company profile) alongside the canvas.

### Engine behaviour (from the Float prototype, branch `prototype/float`)
- The d3-force simulation never cools down. Custom forces provide random-walk drift, a push away from the cursor, and soft walls inset from the shell's bars.
- Physics advances in a **fixed 60 Hz step** driven by an accumulator, never once per frame.
- A Lens sets per-dot targets with a pull that ramps up over the transition. Each dot keeps a share of the Float drift while grouped. Returning to Float pulls dots back to their positions before the switch, then releases them.
- On touch, a tap on empty canvas applies a brief push at that point instead of a cursor.
- Clicking a dot pauses only that dot, which stays where it is. Closing the card resumes it.
- The values the owner chose live in one config object, `site/src/engine/config.ts` (`physics` and `dot`). **That file is the source of truth; the block below is only the starting point** (the prototype verdicts). The owner has since retuned some values in the dev tuning panel (collideStrength 0.45, cursorForce 0.6, cursorRadius 175 at the time of ticket 01), so read the file for current numbers:

  ```ts
  // STARTING VALUES from the Float prototype verdicts (desktop, ~1500 px wide); current ones: config.ts
  const physics = {
    drift: 0.06, wander: 0.15, damping: 0.255,
    collidePad: 4, collideStrength: 0.65,
    cursorForce: 0.65, cursorRadius: 80,
    lensPull: 0.04, lensDrift: 0.25,       // share of Float drift kept while grouped
    transitionMs: 1000, staggerMs: 800,
  };
  const dot = { radiusDesktop: 23, radiusPhone: 14, ringOpacity: 0.2 };
  ```

### Shell layout (prototype verdict: layout A, borrowing C's menu)
- The **bottom pill bar** lists every Lens. Float and Sector are enabled; the rest are greyed with a "coming soon" hint. On phones it scrolls sideways.
- The **top bar** holds the project title, a prominent navigation menu trigger, the Play button (disabled) and a standalone `?` About button. The menu holds a flat list of every View (Investors is one entry), with all unbuilt ones greyed, and the Receipts toggle (disabled).
- The **footer** has one small line: "Unofficial project · not affiliated with Norte Ventures", plus a short "works best on desktop" note.
- The shell reports its bar heights to the engine as insets, so dots stay clear of the bars.

### Design tokens
- Surface: cream `#FAF6E4`. Ink and hairlines: brown `#462500`. The single rare accent is yellow `#FBCF00` (hover, selection, Play). Font: Bricolage Grotesque, system-ui as fallback.
- The Logo dot ring is drawn by the renderer, never baked into images: about 1px of brown at the ring-opacity token.
- **The Estimated convention:**
  - text in muted brown with a dotted underline;
  - numbers prefixed with "≈";
  - shapes with dashed outlines;
  - hover or tap shows the Basis, Confidence and Source.
  - Reported values are plain.
  - The About panel explains this.
- Phone layouts apply below a breakpoint chosen so 320px works. Desktop is the reference design.

### Company card and Company profile
- **The card shows:** name, logo, Sector, short description, year founded and Fund.
  - Estimated values use the convention.
  - The card can be closed by clicking outside it, with the close button or with Escape.
  - "Open full card" goes to `#/company/<slug>`.
- **The profile is a first version in the spirit of the internal profile viewer**, to be deepened after v1. In order, it shows:
  - header: logo, name, Status, description;
  - facts;
  - long description;
  - Investment thesis, labelled as our estimated reasoning;
  - Founders, markets and accelerators;
  - one timeline of Milestones and Rounds, with Rounds styled differently;
  - record details: website and Fund.
- Every value links to its Source. A field with no data reads "not publicly available", because every company has `researched_on` set.

### Site data file (the contract between `data/` and `site/`)
- A Python builder reads the CSVs and writes one JSON file inside the site. It runs the check first and refuses to write if the check fails.
- There is one entry per Portfolio company, keyed by a stable slug (also used in addresses). It carries:
  - from `companies.csv`: name, website, Fund, Highlight, Exit and the logo circle's path;
  - per single-value field, `{value, basis, confidence, source}`;
  - per list field, a list of those;
  - its Sector, taken from the mapping, never stored per company;
  - its Rounds, each with its own `{basis, confidence, source}`, the USD size, and Norte's participation as true, false or unknown;
  - first investment and follow-on, taken from the existing derived views.
- A field with no Claim is absent, never guessed. The site treats absent as "not publicly available".
- The file holds only what the site shows. Notes are not shipped.

### Sector mapping (ADR 0006)
- Claude proposes about 8 to 12 Sectors, each with an icon idea, and maps all 122 Sub-sectors. The owner reviews before it is final.
- The check script now requires every Sub-sector to have a Sector.

### Logo circles (ADR 0015)
- New columns or meanings in `companies.csv`:
  - `logo_crop` holds the crop box as four fractions of the source image (`x,y,w,h`, each from 0 to 1). It is set only together with a logo.
  - `logo_background` becomes the circle fill as `#rrggbb`. The old `dark` / `light` / `both` values stay valid until every logo is confirmed, then the check drops them.
- **The logo circle renderer** is one Python function. Given a source image, a crop and a fill, it produces a 512px WebP circle with transparent corners. Wide wordmarks (aspect ratio of 1.25 or more) are fitted inside a safe inner circle; squarish marks cover it. A rebuild command regenerates every circle from the CSV.
- **The logo studio** is a local server tool that replaces the logo viewer. It is disposable, lives outside `site/` and writes only its own columns (as in ADR 0008).
  - Its four steps are: crop, pick fill (eyedropper or presets), preview on the cream surface with the ring at real dot sizes, and confirm.
  - Confirming writes `logo_crop` and `logo_background` and renders the circle through the renderer.
  - The studio suggests the first fill from the old legibility value.
  - It can filter to logos not yet confirmed.
- Replacing a logo file (the logo fetch script) clears `logo_crop` and `logo_background`.
- Raw Original logos remain the inputs. Circles are outputs that can always be rebuilt, and those outputs ship with the site.

### Publishing
- An explicit sync command copies the built folder into `mysite/public/vc-map/`. It never runs on save or on build.

### Docs
- `docs/data-model.md` describes `logo_crop`, the new meaning of `logo_background`, and the required Sector.
- `docs/agents/testing.md` lists the new seams.
- `STATUS.md` is updated as tickets land.

## Testing Decisions

- **What makes a good test here:** it drives a public seam with small, made-up inputs and checks behaviour a user or the owner would notice, not internal structure. The physics feel, the Pixi rendering and the Svelte views are checked visually instead. That means running the site with the `run` skill and taking screenshots at about 1500px and 320px, compared against the prototype's verdicts.
- **Python seams** use standard-library `unittest`, with small CSVs and images in a temp folder, the same style as the existing `check_files` tests:
  1. **`check_files`** (existing): the new Sector, `logo_crop` and `logo_background` rules, including the transition period that accepts both formats. The existing logo fetch tests are extended so that replacing a logo clears both columns. The test that checks every allowed value appears in `docs/data-model.md` covers the new values.
  2. **The site data builder** (new): it writes one entry per company; it includes `{value, basis, confidence, source}` per field; Sectors come from the mapping; missing fields are absent; Rounds include Norte's participation; first investment and follow-on match the existing derived views; notes are not shipped; it refuses to run when the check fails.
  3. **The logo circle renderer** (new), tested on tiny generated images: the corners are transparent; the fill sits behind the mark; a wide mark is fitted inside the circle and a square mark covers it; the same inputs always give the same output. The studio's save path is tested like the logo viewer's CSV write: only the owned columns change, and the write is atomic.
- **TypeScript seams** use Vitest, a new dev dependency:
  4. **Lens layout**: every Logo dot gets exactly one target; Float keeps the stage height equal to the viewport. For Sector, tests check that:
     - each dot lands in its own Sector's ball;
     - balls don't overlap one another or the insets;
     - every Sector gets exactly one title;
     - on a phone viewport the stage grows taller than the screen, while on desktop it fits.
  5. **Routes**: addresses round-trip to state and back for Lenses, Views and `#/company/<slug>`; unknown and unbuilt addresses resolve to Float.
- **Prior art:** `tests/test_check_data.py` (temp-folder CSVs), `tests/test_derive.py` (pure functions over Round rows), and `tests/test_fetch_logos.py` (logo file side effects).
- The pre-commit hook keeps running the Python tests and the data check. Vitest runs from the site's own package scripts.

## Out of Scope

- Every Lens other than Float and Sector, and the Sector Lens's second level (Sub-sector balls). Status, Country, Founding year, Money raised, Employee count and Business model appear in the shell, greyed out.
- Every View: Norte Timeline, Investors, Theme Explorer, How early does Norte get in?, Exit Wall, Founder graph. They appear in the menu, greyed out.
- The Quiz. Play is shown, disabled.
- Receipts mode. The toggle is shown, disabled, but the data file already carries what it needs.
- A deeper Company profile design (beyond the first version), and Founder profiles.
- Normalizing investor names, map data, founding month, world events, employee counts and theme tags: these are data needs of later Lenses and Views.
- Automating the sync on build or deploy, and any change to the personal site's homepage.
- Matter.js, GSAP and the map stack (d3-geo, TopoJSON).

## Further Notes

- Order of work (`docs/stages.md` §4): the Sector mapping and the logo studio can go in parallel with the site skeleton. The site's Float needs logo circles to look finished, but can start on raw logos clipped to circles, as the prototype did.
- The prototype is kept on branch `prototype/float` (never merged) as a primary source. Its README's "Verdicts" section is the reference for shell layout, physics values and dot sizes.
- Node runs on this machine from `C:\Program Files\nodejs`. Older terminals may need it added to PATH; PowerShell needs `npm.cmd`.
- The owner pulled the Sector Lens into v1 (2026-11-25) because it is the cheapest Lens once the mapping exists, and the first real test of grouped layouts and the scrollable phone stage, which the prototype only imagined. The Sector Lens depends on the Sector mapping being reviewed.
