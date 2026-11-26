import { dot, PHONE_BREAKPOINT, physics } from "./config";

export type LensId = "float" | "fund";
export type Point = { x: number; y: number };
export type Insets = { top: number; right: number; bottom: number; left: number };
export type Viewport = { width: number; height: number; insets: Insets };
export type Device = "desktop" | "phone";
/** A title drawn above a ball of dots. */
export type Decoration = { text: string; x: number; y: number };
/** What a Lens needs to know about a company. */
export type LensCompany = { fund: string };

export type LensLayout = {
  /** One target per Logo dot, in company order; null means the dot is left to drift (Float). */
  targets: (Point | null)[];
  /** Height of the stage in px. Float never scrolls, so it equals the viewport. */
  stageHeight: number;
  decorations: Decoration[];
};

export const deviceOf = (viewport: Viewport): Device => (viewport.width < PHONE_BREAKPOINT ? "phone" : "desktop");

/** A Lens is a pure layout: companies, Lens and viewport in; one target per dot and a stage height out. */
export function layoutLens(lens: LensId, companies: LensCompany[], viewport: Viewport): LensLayout {
  switch (lens) {
    case "float":
      return { targets: Array<null>(companies.length).fill(null), stageHeight: viewport.height, decorations: [] };
    case "fund":
      return layoutBalls(companies.map((c) => c.fund), (key) => `Fund ${key}`, viewport);
  }
}

/** One ball per group, side by side on a wide viewport and stacked on a tall one; dots on a sunflower spiral. */
function layoutBalls(keys: string[], title: (key: string) => string, viewport: Viewport): LensLayout {
  const { width, height, insets } = viewport;
  const W = width - insets.left - insets.right;
  const H = height - insets.top - insets.bottom;
  const horizontal = W >= H;
  const cell = (deviceOf(viewport) === "phone" ? dot.radiusPhone : dot.radiusDesktop) + physics.collidePad;
  const groups = [...new Set(keys)].sort();
  const members = new Map(groups.map((g) => [g, keys.flatMap((k, i) => (k === g ? [i] : []))]));
  const targets: (Point | null)[] = Array(keys.length).fill(null);
  const decorations: Decoration[] = [];
  groups.forEach((g, gi) => {
    const frac = (gi + 0.5) / groups.length;
    const cx = insets.left + (horizontal ? W * frac : W / 2);
    const cy = insets.top + (horizontal ? H / 2 : H * frac) + 14;
    const ids = members.get(g)!;
    ids.forEach((id, k) => {
      const angle = k * 2.39996; // golden angle
      const r = cell * 1.05 * Math.sqrt(k + 0.5);
      targets[id] = { x: cx + Math.cos(angle) * r, y: cy + Math.sin(angle) * r };
    });
    const ballRadius = cell * Math.sqrt(ids.length) * 1.05;
    decorations.push({ text: `${title(g)} · ${ids.length}`, x: cx, y: cy - ballRadius - 10 });
  });
  return { targets, stageHeight: height, decorations };
}
