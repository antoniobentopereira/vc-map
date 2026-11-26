import { describe, expect, it } from "vitest";
import { deviceOf, layoutLens, type Viewport } from "./lens";

const insets = { top: 0, right: 0, bottom: 0, left: 0 };
const desktop: Viewport = { width: 1500, height: 900, insets };
const phone: Viewport = { width: 320, height: 568, insets };

describe("Float Lens layout", () => {
  it.each([desktop, phone])("gives every dot no target and a stage as tall as the viewport", (viewport) => {
    const layout = layoutLens("float", 130, viewport);
    expect(layout.targets).toHaveLength(130);
    expect(layout.targets.every((t) => t === null)).toBe(true);
    expect(layout.stageHeight).toBe(viewport.height);
    expect(layout.decorations).toEqual([]);
  });

  it("tells phones from desktops by width", () => {
    expect(deviceOf(desktop)).toBe("desktop");
    expect(deviceOf(phone)).toBe("phone");
  });
});
