# One repo, data and site kept apart, static output

`vc-map` is one repo with `data/` (gathering the Dataset) and `site/` (the Visualization). `site/` is fully self-contained (own index.html, relative paths, logos copied in, no backend, no secrets) so it can be copied to `mysite/public/vc-map/`. The only link between the two parts is one generated JSON file inside `site/`. We chose one repo over two because a solo beginner gains nothing from the extra overhead.
