<script lang="ts">
  //@ts-nocheck
	import { fade } from "svelte/transition";
  export let data;
  $: categories = [['All', ''], ...[...new Set(data.all_courses.map(i=>i.category.title + '@' + i.category.slug))].map(i=>[i.split('@')[0], i.split('@')[1]])];
  let batch = '';
</script>

<svelte:head>
  <title>BiologyAdda Cracked</title>
</svelte:head>

<div>
<div class="herosec text-center py-15 flex flex-col items-center justify-center gap-3">
  <h1 class="ht animate__animated animate__pulse animate__infinite">BiologyAdda Cracked</h1>
  <p class="text-lg sm:text-xl md:text-2xl lg:text-3xl">All courses of BiologyAdda are now free in one piece!</p>
  <a class="btn btn-success sm:text-lg md:text-xl lg:text-2xl" href="#crs">View Courses</a>
</div>

<div class="py-10"></div>

<h2 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl text-center py-5" id="crs">Cracked Courses</h2>

<div class="ctabs flex flex-wrap items-center justify-center gap-3 mb-5">
  {#each categories as [t, s]}
    <button class="btn btn-success {batch == s ? '' : 'btn-soft'}" on:click={()=>batch = s}>{t}</button>
  {/each}
</div>

<div class="crs grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
  {#each data.all_courses as c }
    {#if c.category.slug.indexOf(batch) != -1}
    <div class="card bg-base-300 shadow-md" transition:fade>
      <figure class="px-5 pt-5">
        <img
          src="{c.img}"
          alt="{c.title}"
          class="rounded-md" />
      </figure>
      <div class="card-body items-center text-center">
        <h2 class="card-title">{c.title}</h2>
        <div class="card-actions">
          <a class="btn btn-primary btn-soft" href="/crs-{c.slug}">View Course</a>
        </div>
      </div>
    </div>
    {/if}
  {/each}
</div>
</div>

<style lang="postcss">
  @reference 'tailwindcss';
  .ht {@apply text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold bg-gradient-to-r from-emerald-400 to-cyan-600 bg-clip-text text-transparent py-2;}
</style>
