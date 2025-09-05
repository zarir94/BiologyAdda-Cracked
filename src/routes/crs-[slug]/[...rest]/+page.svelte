<script lang="ts">
  //@ts-nocheck
	import { goto } from '$app/navigation';
	import { ChevronDown, PinIcon, PinOffIcon } from 'lucide-svelte';
	import { onMount } from 'svelte';
	import { slide } from 'svelte/transition';

  export let data;
  let locals = {
    expandSec: data.sec_slug, selectedCon: data.con_slug,
    ytIDRegex: x=>(x.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?(?:.*&)?v=|embed\/|v\/))([a-zA-Z0-9_-]{11})/)||[])[1],
    gdIDRegex: x=>(x.match(/(?:https?:\/\/)?(?:drive|docs)\.google(?:usercontent)?\.com\/.*?(?:\/d\/|[?&]id=)([a-zA-Z0-9_-]{10,})/i)||[])[1],
  };
  function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  onMount(()=>{
    window.data = data;
  })
</script>

<svelte:head>
  <title>{data.info.title} - BA Cracked</title>
</svelte:head>

<div class="flex items-center mb-5 gap-3 md:gap-5">
  <h2 class="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-semibold">{data.info.title}</h2>
  <button class="btn btn-sm {data.pin ? 'btn-info' : 'btn-ghost'} btn-soft h-auto p-2" on:click={()=>{setCookie('pin', String(!data.pin), 30);data.pin = !data.pin}}>
    <PinIcon size="20"/>
  </button>
</div>

<div class="flex flex-col lg:flex-row gap-5">
  <div class="w-full {data.pin ? 'sticky top-20 z-30' : 'relative'}">
    <div class="{data.pin ? 'sticky top-20 z-30' : 'relative'} w-full h-0 pb-[56.25%] rounded-lg overflow-hidden flex-1">
      <div class="absolute w-full h-full inset-0 keepspin">
        {#if data.cur_content.type == 'exam'}
          <div class="w-full h-full bg-[#162034] p-5 md:p-10 font-bold flex items-center justify-center">
            <div role="alert" class="alert alert-soft alert-error animate__animated animate__headShake animate__infinite">
              <svg xmlns="http://www.w3.org/2000/svg" class="size-6 md:size-10 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span class="md:text-xl">দুঃখিত, এটি একটি পরীক্ষার কনটেন্ট। পরীক্ষা শুধুমাত্র মূল সাইটে দেওয়া যাবে, তাই এখানে আলাদা পরীক্ষার UI যোগ করা সম্ভব নয়।</span>
            </div>
          </div>
        {:else if data.cur_content.type == 'video' && data.cur_content.source == 'youtube' && locals.ytIDRegex(data.cur_content.link || '')}
          <iframe class="w-full h-full" src="https://www.youtube.com/embed/{locals.ytIDRegex(data.cur_content.link || '')}" frameborder="0" title="{data.cur_content.title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        {:else if data.cur_content.type == 'link' && locals.gdIDRegex(data.cur_content.link)}
          <iframe class="w-full h-full" src="https://drive.google.com/file/d/{locals.gdIDRegex(data.cur_content.link)}/preview" frameborder="0" title="{data.cur_content.title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        {:else if data.cur_content.type == 'pdf' && data.cur_content.link?.endsWith('.pdf')}
          <iframe class="w-full h-full" src="https://docs.google.com/gview?url={data.cur_content.link}&embedded=true" frameborder="0" title="{data.cur_content.title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        {:else if data.cur_content.type == 'note'}
          <div class="w-full h-full bg-[#162034] p-5 md:p-10 overflow-auto">
            <div class="prose-sm md:prose">
              {@html data.cur_content.html?.replace(/<(h[1-6])>\s*(<br\s*\/?\s*>|&nbsp;)*\s*<\/\1>/gi, '')}
            </div>
          </div>
        {:else}
          <div class="w-full h-full bg-[#162034] p-5 md:p-10 overflow-auto">
            <h3 class="text-xl md:text-2xl lg:text-3xl font-bold text-red-500 mb-3 md:mb-5">Unsupported content data</h3>
            <pre><code>{JSON.stringify(data.cur_content, null, 4)}</code></pre>
          </div>
        {/if}
      </div>
    </div>
  </div>
  <div class="slist lg:min-w-96 flex-[0] flex flex-col gap-3">
    {#each data.info.sections as s}
    <!-- svelte-ignore a11y_click_events_have_key_events -->
      <div class="bg-base-300 shadow rounded-lg px-5 py-3 border border-slate-800 {locals.expandSec == s.slug ? 'bg-slate-800/40 !border-emerald-800' : 'hover:bg-slate-900 cursor-pointer'} transition duration-300 ease-out" on:click={()=>{locals.expandSec = s.slug }} role="button" tabindex="-1">
        <div class="flex items-center justify-between gap-3">
          <span>{s.title}</span>
          <ChevronDown class="size-4 shrink-0 transition duration-300 ease-out {locals.expandSec == s.slug ? 'rotate-180' : ''}"/>
        </div>
        {#if locals.expandSec == s.slug}
          <div class="clist flex flex-col gap-3 border-t border-slate-600 pt-3 mt-3" transition:slide={{duration: 300}}>
            {#each s.contents as c}
              <a on:click|preventDefault={function () {goto(this.href, {replaceState: true, noScroll: true, keepFocus: true})}} class="btn {locals.selectedCon == c.slug ? 'btn-success' : 'btn-soft'} h-auto py-2" href="/crs-{data.slug}/{s.slug}/{c.slug}">{c.title}</a>
            {/each}
            {#if !s.contents?.length}
              <div role="alert" class="alert alert-warning alert-soft">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
                <span>এই অংশের বিষয়বস্তু এখনো প্রকাশিত হয়নি। যদি ইতিমধ্যে প্রকাশিত হয়ে থাকে, তবে সর্বোচ্চ ৩ ঘণ্টার মধ্যে তা এখানে প্রদর্শিত হবে।</span>
              </div>
            {/if}
          </div>
        {/if}
      </div>
    {/each}
  </div>
</div>


<style lang="postcss">
  @reference 'tailwindcss';
  .keepspin::before {
    @apply size-10 animate-spin;
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    translate: -50% -50%;
    z-index: -1;
    background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiAjMzRkMzk5ICIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWxvYWRlci1pY29uIGx1Y2lkZS1sb2FkZXIiPjxwYXRoIGQ9Ik0xMiAydjQiLz48cGF0aCBkPSJtMTYuMiA3LjggMi45LTIuOSIvPjxwYXRoIGQ9Ik0xOCAxMmg0Ii8+PHBhdGggZD0ibTE2LjIgMTYuMiAyLjkgMi45Ii8+PHBhdGggZD0iTTEyIDE4djQiLz48cGF0aCBkPSJtNC45IDE5LjEgMi45LTIuOSIvPjxwYXRoIGQ9Ik0yIDEyaDQiLz48cGF0aCBkPSJtNC45IDQuOSAyLjkgMi45Ii8+PC9zdmc+);
    background-repeat: no-repeat;
    background-size: contain;
  }
  .keepspin::after {
    content: "";
    top: 0px;
    left: 0px;
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -2;
    background-color: #162034;
  }
</style>