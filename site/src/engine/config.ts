/** Physics values the owner chose in the Float prototype (branch prototype/float, ~1500px wide). */
export const physics = {
  drift: 0.06, // velocity added per tick by the random walk
  wander: 0.15, // how fast each dot's heading turns
  damping: 0.255, // d3 velocityDecay: share of velocity lost per tick
  collidePad: 4, // px of empty space kept between dots
  collideStrength: 0.45, // 0..1, how hard overlaps are resolved
  cursorForce: 0.6, // push strength at the cursor
  cursorRadius: 175, // px reach of the push
  lensPull: 0.04, // pull toward a Lens target once fully ramped
  lensDrift: 0.25, // share of Float drift kept while grouped
  transitionMs: 1000, // pull ramp duration
  staggerMs: 800, // max random start delay per dot
  stepMs: 1000 / 60, // fixed physics step
};

export const dot = { radiusDesktop: 24, radiusPhone: 14, ringOpacity: 0.3 };

/** Design tokens (also in style.css). */
/** Untouched copies, so the tuning panel can reset. */
export const physicsDefaults = { ...physics };
export const dotDefaults = { ...dot };

export const tokens = { cream: 0xfaf6e4, brown: 0x462500, yellow: 0xfbcf00 };

/** Below this viewport width the phone layout and dot size apply. */
export const PHONE_BREAKPOINT = 640;
