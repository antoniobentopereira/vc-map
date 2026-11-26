<script lang="ts">
  // Thin translucent chevrons at the stage's side edges: they appear only when the stage extends past that edge.
  let { host }: { host: HTMLElement } = $props();

  let canLeft = $state(false);
  let canRight = $state(false);

  $effect(() => {
    const update = () => {
      canLeft = host.scrollLeft > 2;
      canRight = host.scrollLeft + host.clientWidth < host.scrollWidth - 2;
    };
    const observer = new ResizeObserver(update);
    observer.observe(host);
    host.addEventListener("scroll", update, { passive: true });
    host.addEventListener("stagesize", update);
    update();
    return () => {
      observer.disconnect();
      host.removeEventListener("scroll", update);
      host.removeEventListener("stagesize", update);
    };
  });

  const pan = (dir: 1 | -1) => host.scrollBy({ left: dir * host.clientWidth * 0.7, behavior: "smooth" });
</script>

{#if canLeft}
  <button class="chev left" aria-label="Pan left" onclick={() => pan(-1)}>
    <svg viewBox="0 0 24 48" aria-hidden="true"><path d="M18 6 6 24l12 18" /></svg>
  </button>
{/if}
{#if canRight}
  <button class="chev right" aria-label="Pan right" onclick={() => pan(1)}>
    <svg viewBox="0 0 24 48" aria-hidden="true"><path d="M6 6l12 18L6 42" /></svg>
  </button>
{/if}

<style>
  .chev {
    position: fixed; top: 50%; transform: translateY(-50%); z-index: 4;
    width: 44px; height: 88px; padding: 0; border: 0; background: none; cursor: pointer;
    color: var(--brown); opacity: 0.35; transition: opacity 0.15s;
  }
  .chev:hover, .chev:focus-visible { opacity: 0.8; }
  .left { left: 4px; }
  .right { right: 4px; }
  svg { width: 100%; height: 100%; fill: none; stroke: currentColor; stroke-width: 1.2; stroke-linecap: round; stroke-linejoin: round; }
</style>
