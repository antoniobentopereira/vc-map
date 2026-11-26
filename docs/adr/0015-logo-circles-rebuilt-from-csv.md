# Logo circles are chosen by hand and rebuilt from CSV columns

Every Logo dot is a uniform circle: the Original logo's mark, cropped and fitted on a fill color. Raw logos vary too much (padding, borders, white or dark marks, wide wordmarks) for a blind script to get this right, so the owner sets each one in a local tool, `tools/logo-studio/`, in four steps: crop, pick the fill (eyedropper or presets), preview the circle on the site surface with its ring, confirm.

The tool saves the decisions, not just an image: `logo_crop` (the crop box as fractions of the source image) and `logo_background` (the fill as `#rrggbb`) in `data/companies.csv`. A script rebuilds every circle (512px WebP, transparent corners) from the raw logo and those two columns, so the circles are output that can always be rebuilt (ADR 0002) and a change of size or format never means re-cropping by hand. Replacing a logo file clears both columns.

The thin ring around each circle is drawn by the site, not baked in, so it stays one design token. `logo_background` previously meant which page background a logo is legible on (`dark`, `light`, `both`); the old words stay valid until all logos are confirmed, and the tool uses them as its first suggestion.
