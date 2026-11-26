<script lang="ts">
  import type { Field } from "./card-data";
  import Fact from "./Fact.svelte";

  type CardCompany = { slug: string; name: string; website: string; logo: string; fund: string; fields: Record<string, Field | undefined> };
  let { company, logoUrl, onClose, onOpen }: {
    company: CardCompany | undefined;
    logoUrl: (path: string) => string;
    onClose: () => void;
    onOpen: (slug: string) => void;
  } = $props();

  let closeBtn = $state<HTMLButtonElement>();
  $effect(() => closeBtn?.focus());
</script>

<svelte:window onkeydown={(e) => e.key === "Escape" && company && onClose()} />

{#if company}

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_static_element_interactions -->
<div class="backdrop" onclick={(e) => e.target === e.currentTarget && onClose()}>
  <div class="card" role="dialog" aria-modal="true" aria-labelledby="card-title">
    <button class="close" bind:this={closeBtn} aria-label="Close" onclick={onClose}>×</button>
    <header>
      <img src={logoUrl(company.logo)} alt="" />
      <div>
        <h2 id="card-title">{company.name}</h2>
        <div class="sector"><Fact field={company.fields.sector} /></div>
      </div>
    </header>
    <p class="desc"><Fact field={company.fields.description} /></p>
    <dl>
      <div><dt>Founded</dt><dd><Fact field={company.fields.year_founded} number /></dd></div>
      <div><dt>Fund</dt><dd>Fund {company.fund}</dd></div>
      {#if company.website}
        <div><dt>Site</dt><dd><a href={company.website} target="_blank" rel="noopener noreferrer">Website ↗</a></dd></div>
      {/if}
    </dl>
    <button class="open" onclick={() => onOpen(company.slug)}>Open full card</button>
  </div>
</div>
{/if}

<style>
  .backdrop {
    position: fixed; inset: 0; z-index: 20; display: flex; align-items: center; justify-content: center;
    padding: 16px; background: rgba(70, 37, 0, 0.18);
  }
  .card {
    position: relative; box-sizing: border-box; width: min(380px, 100%); max-height: calc(100vh - 32px); overflow-y: auto;
    background: var(--cream); border: 1px solid var(--line); border-radius: 18px; padding: 20px;
    box-shadow: 0 16px 48px rgba(70, 37, 0, 0.2); font-size: 15px; line-height: 1.45;
  }
  header { display: flex; align-items: center; gap: 12px; margin-right: 28px; }
  img { width: 56px; height: 56px; border-radius: 50%; border: 1px solid var(--line); object-fit: contain; background: #fff; flex: none; }
  h2 { margin: 0; font-size: 21px; letter-spacing: -0.02em; line-height: 1.15; }
  .sector { font-size: 13px; color: var(--soft); margin-top: 2px; }
  .desc { margin: 14px 0; }
  dl { display: flex; gap: 24px; margin: 0 0 16px; }
  dl div { display: flex; flex-direction: column; gap: 2px; }
  dt { font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--soft); }
  dd { margin: 0; }
  dd a { color: inherit; text-underline-offset: 3px; }
  .close {
    position: absolute; top: 12px; right: 12px; width: 32px; height: 32px; border-radius: 999px; cursor: pointer;
    background: none; border: 1px solid var(--line); color: inherit; font: inherit; font-size: 20px; line-height: 1;
  }
  .close:hover { border-color: var(--brown); }
  .open {
    width: 100%; background: var(--brown); color: var(--cream); border: 0; border-radius: 999px; padding: 9px 14px;
    font: inherit; font-weight: 600; font-size: 14px; cursor: pointer;
  }
</style>
