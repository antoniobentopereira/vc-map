import { dot, PHONE_BREAKPOINT, physics } from "./config";
import { SECTORS } from "../sectors";

export type LensId = "float" | "fund" | "sector";
export type Point = { x: number; y: number };
export type Insets = { top: number; right: number; bottom: number; left: number };
export type Viewport = { width: number; height: number; insets: Insets };
export type Device = "desktop" | "phone";
/** A title drawn above a ball of dots. */
export type Decoration = { text: string; x: number; y: number; /** Name of a line icon drawn above the title. */ icon?: string };
/** A ball of dots: its center and radius, for the engine's benefit and for tests. */
export type Ball = { key: string; x: number; y: number; radius: number };
/** What a Lens needs to know about a company. */
export type LensCompany = { fund: string; sector: string };

export type LensLayout = {
  /** One target per Logo dot, in company order; null means the dot is left to drift (Float). */
  targets: (Point | null)[];
  /** Height of the stage in px. Float never scrolls, so it equals the viewport. */
  stageHeight: number;
  /** Width of the stage in px: the viewport, except a wide Lens may extend past the right edge (the view then pans). */
  stageWidth: number;
  decorations: Decoration[];
  balls: Ball[];
};

export const deviceOf = (viewport: Viewport): Device => (viewport.width < PHONE_BREAKPOINT ? "phone" : "desktop");

/** A Lens is a pure layout: companies, Lens and viewport in; one target per dot and a stage height out. */
export function layoutLens(lens: LensId, companies: LensCompany[], viewport: Viewport): LensLayout {
  switch (lens) {
    case "float":
      return { targets: Array<null>(companies.length).fill(null), stageHeight: viewport.height, stageWidth: viewport.width, decorations: [], balls: [] };
    case "fund":
      return layoutBalls(companies.map((c) => c.fund), (key) => `Fund ${key}`, viewport);
    case "sector":
      return layoutSector(companies.map((c) => c.sector), viewport);
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
  const balls: Ball[] = [];
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
    balls.push({ key: g, x: cx, y: cy, radius: ballRadius });
  });
  return { targets, stageHeight: height, stageWidth: width, decorations, balls };
}

/** Space a ball's icon and title take above it. */
const TITLE_BLOCK = 54;
/** Empty space kept at each side of a packed stage. */
const SIDE_MARGIN = 24;
const GOLDEN_ANGLE = 2.39996;

/**
 * One ball per Sector, sized by its company count. A wide viewport lines the balls up in one row (the stage
 * extends right and pans when the row is wider than the screen); a phone stacks them in one column on a taller stage.
 */
function layoutSector(keys: string[], viewport: Viewport): LensLayout {
  const { width, height, insets } = viewport;
  const W = width - insets.left - insets.right;
  const H = height - insets.top - insets.bottom;
  const phone = deviceOf(viewport) === "phone";
  const radius = phone ? dot.radiusPhone : dot.radiusDesktop;
  const cell = radius + physics.collidePad;
  const gap = phone ? cell : cell * 1.4;
  const known: readonly string[] = SECTORS.map((s) => s.name);
  const groups = [...known.filter((k) => keys.includes(k)), ...new Set(keys.filter((k) => !known.includes(k)))];
  const members = new Map(groups.map((g) => [g, keys.flatMap((k, i) => (k === g ? [i] : []))]));
  groups.sort((a, b) => members.get(b)!.length - members.get(a)!.length); // biggest first (stable, so ties keep Sector order)
  /** Width a ball and its title need side by side (the 15px semibold title is often wider than the ball). */
  const blockWidth = (g: string, scale: number) =>
    Math.max(2 * ballRadius(members.get(g)!.length, scale), `${g} · ${members.get(g)!.length}`.length * 7.8 + 6);
  const ballRadius = (n: number, scale: number) => (cell * 1.05 * Math.sqrt(n - 0.5) + radius) * scale;

  // Ball centers per group, as offsets from the stage's top-left corner (inside the insets).
  let centers = new Map<string, Point>();
  const scale = 1;
  let contentHeight: number;
  let stageW = W;
  if (phone) {
    let y = 0;
    for (const g of groups) {
      const r = ballRadius(members.get(g)!.length, 1);
      centers.set(g, { x: W / 2, y: y + TITLE_BLOCK + r });
      y += TITLE_BLOCK + 2 * r + gap;
    }
    contentHeight = y - gap;
  } else {
    // One row, biggest Sector on the left. If that is wider than the screen the stage extends to
    // the right and the view pans. The balls share one center line, the tallest one with its title centered vertically.
    const row = groups;
    const widths = row.map((g) => blockWidth(g, 1));
    const rowWidth = widths.reduce((sum, w) => sum + w, 0) + gap * (groups.length - 1) + SIDE_MARGIN * 2;
    stageW = Math.max(W, rowWidth);
    const tallest = Math.max(...groups.map((g) => ballRadius(members.get(g)!.length, 1)));
    const axis = H / 2 + TITLE_BLOCK / 2;
    let x = (stageW - (rowWidth - SIDE_MARGIN * 2)) / 2;
    row.forEach((g, i) => {
      centers.set(g, { x: x + widths[i] / 2, y: axis });
      x += widths[i] + gap;
    });
    contentHeight = 2 * tallest + TITLE_BLOCK;
  }

  const targets: (Point | null)[] = Array(keys.length).fill(null);
  const decorations: Decoration[] = [];
  const balls: Ball[] = [];
  for (const g of groups) {
    const ids = members.get(g)!;
    const c = centers.get(g)!;
    const cx = insets.left + c.x;
    const cy = insets.top + c.y;
    ids.forEach((id, k) => {
      const r = cell * 1.05 * Math.sqrt(k + 0.5) * scale;
      targets[id] = { x: cx + Math.cos(k * GOLDEN_ANGLE) * r, y: cy + Math.sin(k * GOLDEN_ANGLE) * r };
    });
    const r = ballRadius(ids.length, scale);
    balls.push({ key: g, x: cx, y: cy, radius: r });
    decorations.push({ text: `${g} · ${ids.length}`, x: cx, y: cy - r - 8, icon: SECTORS.find((s) => s.name === g)?.icon });
  }
  const stageHeight = phone ? Math.max(height, insets.top + contentHeight + insets.bottom + gap) : Math.max(height, insets.top + contentHeight + insets.bottom);
  return { targets, stageHeight, stageWidth: stageW + insets.left + insets.right, decorations, balls };
}
