# The Visualization uses a build step and libraries, unlike the rest of antoniobento.me

`mysite`'s rules ask for plain HTML/CSS/JS, no build step, and libraries saved as single local files. VC Map deliberately breaks those rules. Its planned Lenses and Views (gas-like floating logos, animated Lens switches, a zooming clustered map, money piles, stick-figure games, a quiz) need state management, a WebGL renderer and two kinds of physics, and hand-writing that in plain DOM code would become the hardest part of the project to maintain.

The stack:
- **Vite + TypeScript** to build. The output is still a static, self-contained folder with relative paths (ADR 0001).
- **Svelte** for the controls and pages around the canvas (navigation shell, Company card and profile, Quiz).
- **PixiJS** (WebGL 2D) for the stage the Logo dots, map and games are drawn on.
- **d3-force** for layout physics: every Lens sets target positions and the simulation moves the dots there.
- **Matter.js** for gravity physics (piles, falling objects), loaded only by the game-style Views.
- **GSAP** for choreographed sequences (camera zooms, pops, drops).
- **d3-geo + TopoJSON** for the map.

The engine (PixiJS + d3-force: Logo dots, Lenses, physics) is plain TypeScript behind a small interface (set the Lens, be told when a dot is clicked, pause or resume a dot) and never depends on Svelte. Svelte owns the stateful DOM around it: the navigation shell, the Company card, the Company profile and the About panel. Matter.js and GSAP are added only when a View first needs them; the Float prototype (branch `prototype/float`) needed neither. That prototype also showed the physics must run at a fixed 60 Hz step, not once per frame, or the feel changes with the screen's refresh rate.

Considered: DOM `<img>` dots with d3-force only. It is enough for 130 logos, but not for hundreds of animated sprites or rigid-body piles. Canvas without WebGL was also considered; Pixi gives the same and more with crisp scaling. What is still shared with `mysite`: the static output, no backend, no secrets, and the Bricolage Grotesque font.
