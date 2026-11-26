<script lang="ts">
  let { companies }: { companies: { slug: string; name: string }[] } = $props();
</script>

<!-- Every company by name, for keyboard and screen-reader users: hidden until a link has focus. -->
<nav class="roster" aria-label="All companies">
  <ul>
    {#each companies as c (c.slug)}<li><a href="#/company/{encodeURIComponent(c.slug)}">{c.name}</a></li>{/each}
  </ul>
</nav>

<style>
  .roster:not(:focus-within) { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
  .roster:focus-within {
    position: fixed; z-index: 30; left: 8px; top: 8px; max-height: calc(100vh - 16px); overflow-y: auto; width: min(260px, calc(100vw - 16px));
    background: var(--cream); border: 1px solid var(--brown); border-radius: 12px; padding: 8px 12px; box-sizing: border-box;
  }
  ul { list-style: none; margin: 0; padding: 0; }
  a { color: inherit; display: block; padding: 3px 0; }
</style>
