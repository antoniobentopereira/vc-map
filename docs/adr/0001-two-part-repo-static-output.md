# One repo, data and site kept apart, static output

`vc-map` is one repo with `data/` (gathering the Dataset) and `site/` (the Visualization). We chose one repo over two because a solo beginner gains nothing from the extra overhead.

`site/` is the Visualization's source project (ADR 0014). Building it produces `site/dist/`, which is fully self-contained (own index.html, relative paths, logos included, no backend, no secrets). The only link between the two parts is one generated JSON file inside `site/`, built from `data/`.

`site/dist/` is copied to `mysite/public/vc-map/` by an explicit sync command the owner runs. It is never synced automatically on save or build. The command is `npm run sync` in `site/`.
