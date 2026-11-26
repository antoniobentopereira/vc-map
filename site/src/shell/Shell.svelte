<script lang="ts">
  import { LENSES, VIEWS } from "./shell-data";
  import type { Insets } from "../engine/lens";

  let { activeLens, onLens, onInsets }: {
    activeLens: string;
    onLens: (id: string) => void;
    onInsets: (insets: Insets) => void;
  } = $props();

  let topBar: HTMLElement;
  let bottomBars: HTMLElement;
  let menuWrap: HTMLElement;
  let menuOpen = $state(false);

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
  <h1 class="title">VC Map</h1>
  <div class="menu-wrap" bind:this={menuWrap}>
    <button
      class="menu-trigger"
      aria-haspopup="true"
      aria-expanded={menuOpen}
      aria-controls="views-menu"
      onclick={() => (menuOpen = !menuOpen)}
    >
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" /></svg>
      Views
    </button>
    {#if menuOpen}
      <div class="menu" id="views-menu">
        <ul>
          {#each VIEWS as view (view.id)}
            <li>
              <button class="menu-item" disabled={!view.built}>
                <span>{view.label}</span>
                {#if !view.built}<small>soon</small>{/if}
              </button>
            </li>
          {/each}
        </ul>
        <label class="receipts">
          <input type="checkbox" disabled />
          <span>Receipts</span>
          <small>soon</small>
        </label>
      </div>
    {/if}
  </div>
  <span class="spacer"></span>
  <button class="play" disabled title="Quiz: coming soon">
    <svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 1l9 5-9 5z" fill="currentColor" /></svg>
    Play
  </button>
  <!-- Opens the About panel in ticket 03. -->
  <button class="help" aria-label="About this project" title="About">?</button>
</header>

<div class="bottom" bind:this={bottomBars}>
  <nav class="lenses" aria-label="Lenses">
    <ul>
      {#each LENSES as lens (lens.id)}
        <li>
          <button
            class="pill"
            class:active={lens.built && lens.id === activeLens}
            disabled={!lens.built}
            aria-current={lens.id === activeLens ? "true" : undefined}
            title={lens.built ? undefined : "Coming soon"}
            onclick={() => onLens(lens.id)}
          >
            {lens.label}
            {#if !lens.built}<small>soon</small>{/if}
          </button>
        </li>
      {/each}
    </ul>
  </nav>
  <footer class="footer">
    <span>Unofficial project · not affiliated with Norte Ventures</span>
    <span class="desktop-note">works best on desktop</span>
  </footer>
</div>

<style>
  button {
    font: inherit;
    color: inherit;
    cursor: pointer;
  }
  button:disabled {
    cursor: default;
  }
  small {
    font-size: 0.7em;
    opacity: 0.8;
    letter-spacing: 0.02em;
  }

  .top {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 5;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 14px;
    background: var(--cream);
    border-bottom: 1px solid color-mix(in srgb, var(--brown) 18%, transparent);
  }
  .title {
    margin: 0;
    font-size: 1.15rem;
    font-weight: 700;
    white-space: nowrap;
  }
  .spacer {
    flex: 1;
  }

  .menu-wrap {
    position: relative;
  }
  .menu-trigger {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 14px;
    border: 1.5px solid var(--brown);
    border-radius: 999px;
    background: transparent;
    font-weight: 600;
  }
  .menu-trigger:hover,
  .menu-trigger[aria-expanded="true"] {
    background: var(--yellow);
  }
  .menu {
    position: absolute;
    top: calc(100% + 8px);
    left: 0;
    width: min(280px, calc(100vw - 28px));
    box-sizing: border-box;
    padding: 6px;
    background: var(--cream);
    border: 1.5px solid var(--brown);
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(70, 37, 0, 0.18);
  }
  .menu ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .menu-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 9px 10px;
    border: 0;
    border-radius: 8px;
    background: transparent;
    text-align: left;
  }
  .menu-item:disabled {
    opacity: 0.45;
  }
  .receipts {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 4px;
    padding: 9px 10px;
    border-top: 1px solid color-mix(in srgb, var(--brown) 18%, transparent);
    opacity: 0.45;
  }
  .receipts small {
    margin-left: auto;
  }

  .play {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    border: 1.5px solid var(--yellow);
    border-radius: 999px;
    background: var(--yellow);
    font-weight: 600;
  }
  .play:disabled {
    opacity: 0.4;
  }
  .help {
    width: 34px;
    height: 34px;
    flex: none;
    border: 1.5px solid var(--brown);
    border-radius: 50%;
    background: transparent;
    font-weight: 700;
  }
  .help:hover {
    background: var(--yellow);
  }

  .bottom {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 5;
    background: var(--cream);
    border-top: 1px solid color-mix(in srgb, var(--brown) 18%, transparent);
  }
  .lenses {
    overflow-x: auto;
    scrollbar-width: none;
    padding: 10px 14px 6px;
  }
  .lenses::-webkit-scrollbar {
    display: none;
  }
  .lenses ul {
    display: flex;
    gap: 8px;
    width: max-content;
    margin: 0 auto;
    padding: 0;
    list-style: none;
  }
  .pill {
    display: inline-flex;
    align-items: baseline;
    gap: 6px;
    padding: 7px 14px;
    border: 1.5px solid var(--brown);
    border-radius: 999px;
    background: transparent;
    font-weight: 600;
    white-space: nowrap;
  }
  .pill:not(:disabled):hover {
    background: var(--yellow);
  }
  .pill.active {
    background: var(--brown);
    color: var(--cream);
  }
  .pill:disabled {
    opacity: 0.4;
    border-style: dashed;
  }
  .footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2px 10px;
    padding: 2px 14px 8px;
    font-size: 0.72rem;
    opacity: 0.7;
  }
  .desktop-note::before {
    content: "·";
    margin-right: 10px;
  }

  @media (max-width: 480px) {
    .top {
      padding: 8px 10px;
      gap: 6px;
    }
    .title {
      font-size: 1rem;
    }
    .menu-trigger,
    .play {
      padding: 6px 10px;
    }
    .desktop-note::before {
      content: none;
    }
  }
</style>
