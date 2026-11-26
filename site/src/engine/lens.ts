import { PHONE_BREAKPOINT } from "./config";

export type LensId = "float";
export type Point = { x: number; y: number };
export type Insets = { top: number; right: number; bottom: number; left: number };
export type Viewport = { width: number; height: number; insets: Insets };
export type Device = "desktop" | "phone";
export type Decoration = never; // Grouped Lenses will add ball icons and titles.

export type LensLayout = {
  /** One target per Logo dot, in company order; null means the dot is left to drift (Float). */
  targets: (Point | null)[];
  /** Height of the stage in px. Float never scrolls, so it equals the viewport. */
  stageHeight: number;
  decorations: Decoration[];
};

export const deviceOf = (viewport: Viewport): Device => (viewport.width < PHONE_BREAKPOINT ? "phone" : "desktop");

/** A Lens is a pure layout: companies, Lens and viewport in; one target per dot and a stage height out. */
export function layoutLens(lens: LensId, count: number, viewport: Viewport): LensLayout {
  switch (lens) {
    case "float":
      return { targets: Array<null>(count).fill(null), stageHeight: viewport.height, decorations: [] };
  }
}
