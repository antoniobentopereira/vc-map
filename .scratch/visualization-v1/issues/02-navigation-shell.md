# 02: Navigation shell

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** The floating dots are framed by the full navigation shell, so a visitor sees every Lens and View the project plans, with the unbuilt ones greyed out. The layout follows the prototype verdict (layout A, borrowing C's menu):
- a bottom pill bar of Lenses;
- a top bar with a prominent navigation menu, a disabled Play button and a `?` button;
- a footer notice.

Dots never pass behind the bars.

**Blocked by:** 01

**Status:** done

- [x] Svelte owns the shell. It talks to the engine only through the engine's interface.
- [x] The bottom pill bar lists every Lens (Float, Sector, Status, Country, Founding year, Money raised, Employee count, Business model). Float is enabled; the rest are greyed with a "coming soon" hint. On phones the bar scrolls sideways.
- [x] The top bar has the project title, a prominent navigation menu trigger, a disabled Play button and a standalone `?` button. The `?` button opens nothing until ticket 03.
- [x] The menu holds a flat list of every View, all greyed: Norte Timeline, Investors (one entry), Theme Explorer, How early does Norte get in?, Exit Wall, Founder graph. It also holds a disabled Receipts toggle.
- [x] The footer reads "Unofficial project · not affiliated with Norte Ventures", with a small "works best on desktop" note beside it.
- [x] The shell reports its bar heights to the engine as insets, and dots stay clear of the bars, including after a window resize.
- [x] Works by tap at 320px. Checked in the browser at about 1500px and 320px.
