<script lang="ts">
  import Fact from "./Fact.svelte";
  import { NOT_AVAILABLE } from "./card-data";
  import { timeline, type ProfileCompany } from "./profile-data";

  let { company, logoUrl, onBack }: {
    company: ProfileCompany | undefined;
    logoUrl: (path: string) => string;
    onBack: () => void;
  } = $props();

  let back = $state<HTMLButtonElement>();
  $effect(() => {
    if (company) back?.focus();
  });
  const f = (name: string) => company?.fields[name];
  const items = $derived(company ? timeline(company) : []);
  const acquired = $derived(!!(f("acquirer") || f("acquisition_year")));
  const people = $derived(
    company
      ? [
          { label: "Founders", list: company.lists.founders },
          { label: "Markets", list: company.lists.markets },
          { label: "Accelerators", list: company.lists.accelerators },
        ]
      : [],
  );
</script>

{#if company}
<div class="page" role="region" aria-label="{company.name} profile">
  <article>
    <button class="back" bind:this={back} onclick={onBack}>← Back to the dots</button>

    <header>
      <img src={logoUrl(company.logo)} alt="" />
      <div>
        <h1>{company.name}</h1>
        <div class="status"><Fact field={f("status")} /></div>
      </div>
    </header>
    <p class="lead"><Fact field={f("description")} block /></p>

    <section aria-labelledby="h-facts">
      <h2 id="h-facts">Facts</h2>
      <dl>
        <div><dt>Sector</dt><dd><Fact field={f("sector")} /></dd></div>
        <div><dt>Sub-sector</dt><dd><Fact field={f("sub_sector")} /></dd></div>
        <div><dt>Status</dt><dd><Fact field={f("status")} /></dd></div>
        <div><dt>Business model</dt><dd><Fact field={f("business_model")} /></dd></div>
        <div><dt>Founded</dt><dd><Fact field={f("year_founded")} number /></dd></div>
        <div><dt>HQ now</dt><dd><Fact field={f("hq")} /></dd></div>
        <div><dt>HQ at first investment</dt><dd><Fact field={f("hq_at_first_investment")} /></dd></div>
        <div><dt>Fund</dt><dd>Fund {company.fund}</dd></div>
        {#if acquired}
          <div><dt>Acquired by</dt><dd><Fact field={f("acquirer")} /></dd></div>
          <div><dt>Acquired in</dt><dd><Fact field={f("acquisition_year")} number /></dd></div>
        {/if}
      </dl>
    </section>

    <section aria-labelledby="h-story">
      <h2 id="h-story">The story</h2>
      <p class="long"><Fact field={f("long_description")} block /></p>
    </section>

    <section aria-labelledby="h-thesis">
      <h2 id="h-thesis">Investment thesis</h2>
      <p class="label">Our estimated reasoning, not Norte's own words.</p>
      <p class="long"><Fact field={f("investment_thesis")} block /></p>
    </section>

    <section aria-labelledby="h-people">
      <h2 id="h-people">Founders, markets and accelerators</h2>
      <dl>
        {#each people as { label, list } (label)}
          <div>
            <dt>{label}</dt>
            <dd>
              {#if list.length === 0}<span class="missing">{NOT_AVAILABLE}</span>{/if}
              <ul class="chips">{#each list as item (item.value)}<li><Fact field={item} /></li>{/each}</ul>
            </dd>
          </div>
        {/each}
      </dl>
    </section>

    <section aria-labelledby="h-time">
      <h2 id="h-time">Timeline</h2>
      {#if items.length === 0}
        <p class="missing">{NOT_AVAILABLE}</p>
      {:else}
        <ol class="timeline">
          {#each items as item, i (i)}
            <li class:round={item.kind === "round"}>
              <span class="date">{item.date}</span>
              <span class="body">
                {#if item.kind === "round"}<span class="tag">Round</span>{/if}
                <Fact field={item.field} block />
                {#if item.kind === "round" && item.round.co_investors.length}
                  <span class="co">With {item.round.co_investors.join(", ")}</span>
                {/if}
              </span>
            </li>
          {/each}
        </ol>
      {/if}
    </section>

    <section aria-labelledby="h-record">
      <h2 id="h-record">Record details</h2>
      <dl>
        <div>
          <dt>Website</dt>
          <dd>
            {#if company.website}
              <a href={company.website} target="_blank" rel="noopener noreferrer">{company.website.replace(/^https?:\/\//, "")} ↗</a>
            {:else}
              <span class="missing">{NOT_AVAILABLE}</span>
            {/if}
          </dd>
        </div>
        <div><dt>Fund</dt><dd>Fund {company.fund}</dd></div>
      </dl>
    </section>
  </article>
</div>
{/if}

<style>
  .page { position: fixed; inset: 0; z-index: 15; overflow-y: auto; background: var(--cream); }
  article { box-sizing: border-box; max-width: 720px; margin: 0 auto; padding: 18px 20px 64px; font-size: 16px; line-height: 1.55; }
  .back {
    background: none; border: 1px solid var(--line); border-radius: 999px; padding: 7px 14px; cursor: pointer;
    font: inherit; font-size: 14px; color: inherit;
  }
  .back:hover { border-color: var(--brown); }
  header { display: flex; align-items: center; gap: 16px; margin: 22px 0 10px; }
  img { width: 72px; height: 72px; border-radius: 50%; border: 1px solid var(--line); object-fit: contain; background: #fff; flex: none; }
  h1 { margin: 0; font-size: 34px; line-height: 1.1; letter-spacing: -0.03em; overflow-wrap: anywhere; }
  .status { color: var(--soft); font-size: 14px; text-transform: capitalize; }
  .lead { font-size: 18px; margin: 8px 0 0; }
  section { margin-top: 32px; }
  h2 { font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--soft); margin: 0 0 10px; border-bottom: 1px solid var(--line); padding-bottom: 6px; }
  dl { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 14px 20px; margin: 0; }
  dt { font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--soft); }
  dd { margin: 2px 0 0; overflow-wrap: anywhere; }
  dd a { color: inherit; text-underline-offset: 3px; }
  .long { margin: 0; }
  .label { margin: 0 0 8px; font-size: 13px; font-style: italic; color: var(--soft); }
  .missing { color: var(--soft); font-style: italic; }
  .chips { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 2px; }
  .timeline { list-style: none; margin: 0; padding: 0 0 0 12px; border-left: 2px solid var(--line); }
  .timeline li { display: grid; grid-template-columns: 74px 1fr; gap: 10px; padding: 0 0 16px 12px; position: relative; }
  .timeline li::before {
    content: ""; position: absolute; left: -19px; top: 7px; width: 8px; height: 8px; border-radius: 50%;
    background: var(--cream); border: 2px solid var(--brown);
  }
  .timeline li.round::before { background: var(--yellow); border-radius: 2px; }
  .timeline li.round .body { background: rgba(251, 207, 0, 0.16); border: 1px solid var(--yellow); border-radius: 10px; padding: 6px 10px; }
  .date { font-size: 13px; color: var(--soft); padding-top: 2px; font-variant-numeric: tabular-nums; }
  .body { min-width: 0; overflow-wrap: anywhere; }
  .tag { display: inline-block; font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-bottom: 2px; }
  .co { display: block; font-size: 13px; color: var(--soft); margin-top: 2px; }
  @media (max-width: 640px) {
    article { padding: 14px 16px 56px; }
    h1 { font-size: 27px; }
    img { width: 56px; height: 56px; }
    .lead { font-size: 16px; }
    dl { grid-template-columns: 1fr 1fr; }
    .timeline li { grid-template-columns: 1fr; gap: 0; }
  }
</style>
