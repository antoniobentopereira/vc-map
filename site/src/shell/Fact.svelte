<script lang="ts">
  import { fade } from "svelte/transition";
  import { NOT_AVAILABLE, type Field } from "./card-data";

  let { field, number = false, block = false }: { field: Field | undefined; number?: boolean; block?: boolean } = $props();
  let open = $state(false);
</script>

{#if !field}
  <span class="missing">{NOT_AVAILABLE}</span>
{:else}
  <span class="fact" class:block role="presentation" onmouseleave={() => (open = false)}>
    <button
      class="value"
      class:est={field.basis === "estimated"}
      aria-expanded={open}
      onpointerenter={(e) => e.pointerType === "mouse" && (open = true)}
      onfocus={(e) => e.currentTarget.matches(":focus-visible") && (open = true)}
      onclick={() => (open = !open)}
    >{#if field.basis === "estimated" && number}≈ {/if}{field.value}</button>
    {#if open}
      <span class="tip" role="tooltip" transition:fade={{ duration: 120 }}>
        <span><b>Basis</b> {field.basis}</span>
        <span><b>Confidence</b> {field.confidence}</span>
        <a href={field.source} target="_blank" rel="noopener noreferrer"><b>Source</b> open ↗</a>
      </span>
    {/if}
  </span>
{/if}

<style>
  .fact { position: relative; }
  .fact.block { display: block; }
  .value { all: unset; cursor: pointer; }
  .block .value { display: block; white-space: pre-line; }
  .value:focus-visible { outline: 2px solid var(--yellow); outline-offset: 2px; border-radius: 3px; }
  /* The Estimated convention (see the About panel): muted brown, dotted underline, ≈ before numbers. */
  .est { color: var(--soft); text-decoration: underline dotted; text-decoration-color: var(--soft); text-underline-offset: 3px; }
  .missing { color: var(--soft); font-style: italic; }
  .tip {
    position: absolute; z-index: 2; left: 0; top: 100%; display: flex; flex-direction: column; gap: 2px; min-width: 150px;
    padding: 8px 10px; background: var(--brown); color: var(--cream); border-radius: 10px; font-size: 12px;
    line-height: 1.35; font-style: normal; text-decoration: none; white-space: nowrap;
  }
  .tip b { font-weight: 600; margin-right: 4px; opacity: 0.7; }
  .tip a { color: inherit; }
</style>
