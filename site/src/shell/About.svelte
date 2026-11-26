<script lang="ts">
  let { onClose }: { onClose: () => void } = $props();
  let closeBtn: HTMLButtonElement;
  $effect(() => closeBtn.focus());
</script>

<svelte:window onkeydown={(e) => e.key === "Escape" && onClose()} />

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_static_element_interactions -->
<div class="backdrop" onclick={(e) => e.target === e.currentTarget && onClose()}>
  <div class="panel" role="dialog" aria-modal="true" aria-labelledby="about-title">
    <button class="close" bind:this={closeBtn} aria-label="Close" onclick={onClose}>×</button>
    <h2 id="about-title">About VC Map</h2>

    <p>
      VC Map is an <strong>unofficial</strong> project. It is not affiliated with, endorsed by or
      made by Norte Ventures.
    </p>
    <p>
      It was built to make Norte's portfolio easy to explore: every company as a floating dot you can
      group, open and compare, instead of rows in a spreadsheet. It was built with AI, which gathered
      the data from public sources and helped write the site.
    </p>

    <h3>The Estimated convention</h3>
    <p>
      Some values could not be confirmed from a source and are estimated. They always look the same:
    </p>
    <ul>
      <li>Text: a muted <span class="est-text">dotted underline</span>.</li>
      <li>Numbers: a <span class="est-text">≈</span> before the number, like ≈ 40 employees.</li>
      <li>Shapes: a <span class="est-shape">dashed outline</span>.</li>
    </ul>
    <p>
      Each estimate has a <strong>Basis</strong> (how it was worked out, such as a rounding of a
      reported range or an inference from a related fact) and a <strong>Confidence</strong> (how far
      to trust it: high, medium or low). Both show next to the value, with a link to the Source.
    </p>
  </div>
</div>

<style>
  .backdrop {
    position: fixed; inset: 0; z-index: 20; display: flex; align-items: center; justify-content: center;
    padding: 16px; background: rgba(70, 37, 0, 0.28);
  }
  .panel {
    position: relative; box-sizing: border-box; width: min(520px, 100%); max-height: calc(100vh - 32px); overflow: auto;
    background: var(--cream); border: 1px solid var(--line); border-radius: 18px; padding: 24px 24px 20px;
    box-shadow: 0 16px 48px rgba(70, 37, 0, 0.2); font-size: 15px; line-height: 1.5;
  }
  h2 { margin: 0 32px 12px 0; font-size: 22px; letter-spacing: -0.02em; }
  h3 { margin: 18px 0 6px; font-size: 16px; }
  p { margin: 0 0 10px; }
  ul { margin: 0 0 10px; padding-left: 20px; }
  li { margin-bottom: 4px; }
  .close {
    position: absolute; top: 12px; right: 12px; width: 32px; height: 32px; border-radius: 999px; cursor: pointer;
    background: none; border: 1px solid var(--line); color: inherit; font: inherit; font-size: 20px; line-height: 1;
  }
  .close:hover { border-color: var(--brown); }
  .est-text { text-decoration: underline dotted; text-decoration-color: var(--soft); text-underline-offset: 3px; }
  .est-shape { display: inline-block; border: 1.5px dashed var(--soft); border-radius: 999px; padding: 0 8px; }
  @media (max-width: 640px) { .panel { padding: 20px 16px 16px; font-size: 14px; } }
</style>
