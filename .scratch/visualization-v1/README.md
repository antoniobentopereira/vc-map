# Visualization v1: how to check the work yourself

Spec: `spec.md`. Tickets: `issues/`. This page says how to run what exists and what to look at. Right now that is **ticket 01** (site skeleton, floating logos).

## Run it

Node lives in `C:\Program Files\nodejs`. In PowerShell use `npm.cmd`; if `node` is not found, add that folder to PATH.

```powershell
cd site
npm.cmd install        # first time only
npm.cmd run dev        # prints a local URL, usually http://localhost:5173
```

Open the URL. To try it on your phone, use the "Network" URL the dev server prints (same Wi-Fi).

## Run the checks

From the repo root:

| What | Command |
| --- | --- |
| Python tests | `python -m unittest discover -s tests` |
| Data check | `python scripts/check_data.py` |
| Rebuild the site data file | `python scripts/build_site_data.py` (or `npm.cmd run data` in `site/`) |
| Site tests (Vitest) | `cd site; npm.cmd run test` |
| Types | `cd site; npm.cmd run typecheck` |
| Production build | `cd site; npm.cmd run build` (output in `site/dist/`) |
| Preview the build | `cd site; npx.cmd vite preview` |

## Ticket 01: what to look at

Open the site at about **1500px wide** (desktop) and again at **320px** (browser dev tools, device toolbar, or your phone).

- [ ] All 130 dots are visible, each a circle with a logo and a thin brown ring.
- [ ] Dots drift slowly like gas and never stop. Compare the feel to the prototype (see below).
- [ ] Dots bump into each other softly, with no hard jitter or overlapping pile.
- [ ] Moving the cursor pushes nearby dots away (desktop).
- [ ] On touch, tapping empty canvas gives a brief push. Tapping a dot does not push.
- [ ] Hovering a dot grows it slightly. Clicking one stops it with a yellow ring, then it drifts again after 1.5 seconds (placeholder until the Company card).
- [ ] Dots stay inside the window and bunch up at no edge.
- [ ] Resize the window: dots re-fit. Below 640px they get smaller (14px radius instead of 23px).
- [ ] The motion speed is the same on a 120/144 Hz screen as on 60 Hz, if you have one.
- [ ] `npm.cmd run build` works, and `site/dist/index.html` opens from a plain static server with logos showing (relative paths).

Known and expected for now (not feedback-worthy yet):
- Some logos look blank: white-on-white. Fills come with the logo studio (tickets 07 to 09).
- No top bar, bottom bar or card yet (tickets 02 and 05).
- The font loads from Google Fonts; bundling it is a release task.

## Compare with the prototype

The prototype is on branch `prototype/float`, folder `site/prototype-float/`. To run it side by side without leaving `main`:

```powershell
git worktree add ../vc-map-proto prototype/float
cd ../vc-map-proto/site/prototype-float
npm.cmd install
npm.cmd run dev -- --port 5180
```

Remove it afterwards: `git worktree remove ../vc-map-proto` (from the repo).

## Tuning the feel

All physics values are in one object: `site/src/engine/config.ts` (`physics` and `dot`). Edit, save, and the dev server reloads. Note the values you change and why, so they can go back into the spec.

### Temporary tuning panel (remove when you are satisfied)

Press **T** (or click **Tune (T)**, bottom left) on the dev server to get sliders for the physics and dot values. **Reset** goes back to the current defaults. **Make default** writes your current slider values into `site/src/engine/config.ts` (the page then reloads with them as the defaults); review and commit that change like any other. **Copy values** copies your settings to the clipboard.

It appears only under `npm run dev` and is not in the build. To remove it later, delete `site/src/tune.ts`, its last line in `site/src/main.ts` (the `if (import.meta.env.DEV) ... mountTune(engine)` line), and the `tuneDefaults` plugin in `site/vite.config.ts` (the function and its entry in `plugins`). The `.tune-*` and `#tune` rules at the bottom of `site/src/style.css`, and `applyConfig()`/`fps()` in the engine, can go too, but are harmless if left.

## Giving feedback

Write it in the checklist above, or as a new file in `issues/` using the labels in `docs/agents/triage-labels.md`. Useful detail: screen width, browser, what you did, what you expected.
