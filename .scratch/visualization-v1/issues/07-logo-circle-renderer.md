# 07: Logo circle renderer

Spec: `.scratch/visualization-v1/spec.md`

**What to build:** Logo circles can be built from a raw Original logo plus two choices saved in `companies.csv`, the crop and the fill (ADR 0015), and one command rebuilds them all. The site shows a company's circle when one exists and otherwise falls back to the raw logo clipped to a circle.

**Blocked by:** 01

**Status:** done

- [x] One Python renderer takes a source image, `logo_crop` (`x,y,w,h` as fractions from 0 to 1) and `logo_background` (`#rrggbb`), and produces a 512px WebP circle with transparent corners. Wide marks (aspect ratio of 1.25 or more) are fitted inside a safe inner circle; squarish marks cover it.
- [x] Renderer tests on tiny generated images check that:
  - the corners are transparent;
  - the fill sits behind the mark;
  - a wordmark is fitted and a square mark covers the circle;
  - the same inputs give the same output.
- [x] A rebuild command regenerates every circle from the CSV.
- [x] `check_files` accepts `logo_crop` only together with a logo and only as four fractions. It accepts `logo_background` as `#rrggbb` or the old `dark` / `light` / `both`. Tested.
- [x] When the logo fetch script replaces a logo file, it clears `logo_crop` and `logo_background`. The existing fetch tests are extended to cover this.
- [x] `docs/data-model.md` describes `logo_crop` and the new meaning of `logo_background`, and the allowed-values doc test passes.
- [x] The site data builder points to the circle when it exists and to the raw logo otherwise, and the site shows it.
