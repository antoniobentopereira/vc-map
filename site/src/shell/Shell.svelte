<script lang="ts">
  import { LENSES, VIEWS } from "./shell-data";
  import type { Insets } from "../engine/lens";
  import About from "./About.svelte";
  import { fly } from "svelte/transition";
  import { cubicOut } from "svelte/easing";

  let { activeLens, onLens, onInsets }: {
    activeLens: string;
    onLens: (id: string) => void;
    onInsets: (insets: Insets) => void;
  } = $props();

  let topBar: HTMLElement;
  let bottomBars: HTMLElement;
  let menuWrap: HTMLElement;
  let menuOpen = $state(false);
  let aboutOpen = $state(false);

  // One shared indicator slides under whichever pill is active, matching its size.
  let pillsEl: HTMLElement;
  let pillEls: Record<string, HTMLElement> = {};
  let ind = $state({ x: 0, y: 0, w: 0, h: 0, show: false, anim: false });
  const activeBuilt = $derived(LENSES.some((l) => l.built && l.id === activeLens));
  $effect(() => {
    const id = activeLens;
    const place = () => {
      const el = pillEls[id];
      if (!el || !activeBuilt) return void (ind.show = false);
      ind.x = el.offsetLeft; ind.y = el.offsetTop; ind.w = el.offsetWidth; ind.h = el.offsetHeight; ind.show = true;
    };
    place();
    // Animate only after the first placement, and not while the bar itself is resizing.
    requestAnimationFrame(() => (ind.anim = true));
    const observer = new ResizeObserver(() => {
      ind.anim = false;
      place();
      requestAnimationFrame(() => (ind.anim = true));
    });
    observer.observe(pillsEl);
    for (const el of Object.values(pillEls)) observer.observe(el);
    return () => observer.disconnect();
  });

  // Report the bars' heights to the engine whenever they change (resize, wrapping text, fonts).
  $effect(() => {
    const report = () =>
      onInsets({ top: topBar.offsetHeight, right: 0, bottom: bottomBars.offsetHeight, left: 0 });
    const observer = new ResizeObserver(report);
    observer.observe(topBar);
    observer.observe(bottomBars);
    report();
    return () => observer.disconnect();
  });

  function onWindowPointerDown(e: PointerEvent) {
    if (menuOpen && !menuWrap.contains(e.target as Node)) menuOpen = false;
  }
  function onWindowKey(e: KeyboardEvent) {
    if (e.key === "Escape") menuOpen = false;
  }
</script>

<svelte:window onpointerdown={onWindowPointerDown} onkeydown={onWindowKey} />

<header class="top" bind:this={topBar}>
  <div class="mark">VC Map <span class="sub">Norte portfolio</span></div>
  <div class="actions">
    <div class="menu-wrap" bind:this={menuWrap}>
      <button
        class="btn"
        aria-haspopup="true"
        aria-expanded={menuOpen}
        aria-controls="views-menu"
        onclick={() => (menuOpen = !menuOpen)}
      >Views ▾</button>
      {#if menuOpen}
        <div class="menu" id="views-menu" transition:fly={{ y: -6, duration: 140, easing: cubicOut }}>
          {#each VIEWS as view (view.id)}
            <button class="menu-item" disabled={!view.built} title={view.built ? undefined : "Coming soon"}>
              <span>{view.label}</span>
              {#if !view.built}<span class="soon">soon</span>{/if}
            </button>
          {/each}
          <hr />
          <label class="menu-item toggle" title="Coming soon">
            <span><input type="checkbox" disabled /> Receipts</span>
            <span class="soon">soon</span>
          </label>
        </div>
      {/if}
    </div>
    <button class="btn play" disabled title="Quiz coming soon">▶ Play</button>
    <button class="btn icon" aria-label="About this project" title="About" onclick={() => (aboutOpen = true)}>?</button>
  </div>
</header>

{#if aboutOpen}<About onClose={() => (aboutOpen = false)} />{/if}

<div class="bottom" bind:this={bottomBars}>
  <nav class="pills" aria-label="Lenses" bind:this={pillsEl}>
    <span
      class="indicator"
      class:anim={ind.anim}
      aria-hidden="true"
      style="transform: translate({ind.x}px, {ind.y}px); width: {ind.w}px; height: {ind.h}px; opacity: {ind.show ? 1 : 0};"
    ></span>
    {#each LENSES as lens (lens.id)}
      <button
        class="pill"
        class:on={lens.built && lens.id === activeLens}
        bind:this={pillEls[lens.id]}
        disabled={!lens.built}
        aria-current={lens.id === activeLens ? "true" : undefined}
        title={lens.built ? undefined : "Coming soon"}
        onclick={() => onLens(lens.id)}
      >{lens.label}</button>
    {/each}
  </nav>
  <footer class="foot">
    <span>Unofficial project · not affiliated with Norte Ventures</span>
    <span class="desktop-note">works best on desktop</span>
  </footer>
</div>

<style>
  button { font: inherit; color: inherit; }

  /* No boxed bars: the controls float over the canvas and the dots wander around them (via insets). */
  .top, .bottom { position: fixed; left: 0; right: 0; z-index: 5; pointer-events: none; }
  .top > *, .bottom > * { pointer-events: auto; }
  .top { top: 0; display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 14px 20px; }
  .mark { font-weight: 700; font-size: 20px; letter-spacing: -0.02em; white-space: nowrap; }
  .sub { font-weight: 400; font-size: 14px; color: var(--soft); margin-left: 6px; }
  .actions { display: flex; align-items: center; gap: 10px; }

  .btn {
    background: var(--cream); border: 1px solid var(--line); border-radius: 999px;
    padding: 7px 14px; cursor: pointer; font-size: 14px; white-space: nowrap;
    transition: border-color 0.15s, transform 0.15s, opacity 0.15s;
  }
  .btn:active:not(:disabled) { transform: scale(0.96); }
  .btn:hover:not(:disabled) { border-color: var(--brown); }
  .btn.icon { width: 34px; padding: 7px 0; }
  .btn.play { background: var(--brown); color: var(--cream); border-color: var(--brown); font-weight: 600; }
  .btn:disabled, .pill:disabled, .menu-item:disabled { opacity: 0.38; cursor: not-allowed; }
  .btn.play:disabled { opacity: 0.3; }

  .menu-wrap { position: relative; }
  .menu {
    position: absolute; top: calc(100% + 6px); right: 0; width: min(280px, calc(100vw - 24px)); max-height: 70vh; overflow-x: hidden; overflow-y: auto;
    background: var(--cream); border: 1px solid var(--line); border-radius: 14px; padding: 6px;
    box-shadow: 0 10px 30px rgba(70, 37, 0, 0.12);
  }
  .menu-item {
    display: flex; align-items: center; justify-content: space-between; width: 100%; box-sizing: border-box; text-align: left;
    background: none; border: 0; border-radius: 9px; padding: 8px 10px; cursor: pointer; font-size: 14px; transition: background 0.15s;
  }
  .menu-item:hover:not(:disabled) { background: rgba(70, 37, 0, 0.06); }
  .toggle { opacity: 0.45; cursor: not-allowed; box-sizing: border-box; }
  .menu hr { border: 0; border-top: 1px solid var(--line); margin: 6px 4px; }
  .soon { font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; margin-left: 8px; color: var(--soft); }

  .bottom { bottom: 0; display: flex; flex-direction: column; align-items: center; gap: 8px; padding-bottom: 10px; }
  .pills {
    position: relative; max-width: calc(100vw - 32px); display: flex; gap: 4px; padding: 5px; overflow-x: auto; scrollbar-width: none;
    background: var(--cream); border: 1px solid var(--line); border-radius: 999px; box-shadow: 0 6px 24px rgba(70, 37, 0, 0.08);
  }
  .pills::-webkit-scrollbar { display: none; }
  .pill { border: 0; background: none; position: relative; border-radius: 999px; padding: 8px 14px; cursor: pointer; font-size: 14px; white-space: nowrap; transition: background 0.2s, color 0.25s; }
  .indicator { position: absolute; left: 0; top: 0; border-radius: 999px; background: var(--brown); pointer-events: none; }
  .indicator.anim { transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1), width 0.35s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.2s; }
  .pill:hover:not(:disabled):not(.on) { background: rgba(70, 37, 0, 0.06); }
  .on { color: var(--cream) !important; }

  .foot { font-size: 11px; color: var(--soft); text-align: center; padding: 0 16px; pointer-events: none; }
  .desktop-note::before { content: "·"; margin: 0 6px 0 4px; }

  @media (max-width: 640px) {
    .top { padding: 10px 12px; }
    .sub, .desktop-note::before { display: none; }
    .actions { gap: 6px; }
    .actions .btn { padding: 7px 10px; }
    .actions .btn.icon { padding: 7px 0; }
    .pills { width: calc(100vw - 32px); }
  }
</style>
