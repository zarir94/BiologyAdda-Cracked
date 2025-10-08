<script lang="ts">
	import '../app.css';
	import logo from "$lib/assets/logo.png";
	import preview from "$lib/assets/preview.png";
	import { page } from '$app/state';
	import "animate.css";
	import { ProgressBar } from "@prgm/sveltekit-progress-bar";
	import { fade } from 'svelte/transition';
	export let children;
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
	<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;600;700;800&display=swap" rel="stylesheet">
	<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
	<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
	<link rel="manifest" href="/site.webmanifest">
  <meta property="og:title" content="BA Cracked" />
  <meta property="og:description" content="Biology Adda Cracked & Courses are made free for everyone!" />
  <meta property="og:url" content="{page.url.toString()}" />
  <meta property="og:image" content="{preview}" />
</svelte:head>
<ProgressBar class="text-emerald-600" zIndex={50} maximum={0.955}/>

<div class="navbar py-1 backdrop-blur-md bg-slate-950/10 shadow-sm sticky top-0 left-0 z-40">
	<div class="container mx-auto flex items-center">
		<div class="flex-1">
			<a class="btn btn-ghost" href="/">
				<img class="h-full scale-125" src="{logo}" alt="Site-Logo">
			</a>
		</div>
		<div class="flex-none">
			<ul class="menu menu-horizontal px-1 text-lg">
				<li><a href="https://form.jotform.com/252451193893463" target="_blank">Contact</a></li>
			</ul>
		</div>
	</div>
</div>

{#key page.url.pathname}
<div class="container mx-auto my-10 px-5" in:fade={{duration: 250, delay: 250}} out:fade={{duration: 250}}>
	{@render children?.()}
</div>
{/key}

<div class="container mx-auto my-10 px-5">
	<h2 class="text-center font-bold text-xl sm:text-2xl md:text-3xl lg:text-4xl mb-5">What is the purpose?</h2>
	<div class="prose md:prose-lg lg:prose-xl max-w-full">
		<p>এই ওয়েবসাইটটি তৈরি করা হয়েছে একটি উদ্দেশ্য নিয়ে—জ্ঞানকে মুক্ত করার জন্য। আমরা প্রায়শই মনে করি, জ্ঞান আমাদের নিজের একান্ত সম্পদ, যা আমরা শুধুমাত্র নিজের জন্য রাখি। কিন্তু সত্যিই জ্ঞান তার পূর্ণ ক্ষমতা প্রয়োগ করতে পারে <strong>শুধুমাত্র তখনই যখন তা ভাগ করা হয়</strong>। যদি আমরা জ্ঞানকে নিজের মধ্যে আটকে রাখি, তাহলে তা সৃষ্টিশীলতার জন্ম দিতে পারে না; নতুন ধারণা ও উদ্ভাবনের পথ খুলে দিতে পারে না।</p>

		<p>জ্ঞান একটি জীবন্ত প্রক্রিয়া। এটি কেবল শেখা বা মনে রাখার বিষয় নয়, বরং এটি ব্যবহার, আলোচনা ও বিতরণের মধ্য দিয়ে বিকশিত হয়। যখন আমরা অন্যের সঙ্গে আমাদের জ্ঞান ভাগ করি, তখন তা নতুনভাবে প্রসারিত হয়। একাধিক মানুষের দৃষ্টিভঙ্গি, অভিজ্ঞতা ও বিশ্লেষণ একত্রিত হলে জ্ঞান আরও গভীর ও ব্যাপক হয়ে ওঠে। সুতরাং, জ্ঞানকে নিজের মধ্যে সীমাবদ্ধ রাখলে তা একধরনের নিঃশক্ত হয়ে পড়ে, যা কোনো সৃজনশীল কাজ বা উদ্ভাবনকে প্রেরণা দিতে পারে না।</p>

		<p>শিক্ষা ও জ্ঞান কখনোই কোনো ব্যক্তির একক সম্পদ হওয়া উচিত নয়। জ্ঞান ভাগাভাগি করার মধ্য দিয়ে সমাজে সচেতনতা, শিক্ষাগত সমতা এবং সৃজনশীলতার বৃদ্ধি ঘটে। তাই আমি বিশ্বাস করি, <strong>প্রত্যেকের জন্য জ্ঞান উন্মুক্ত থাকা উচিত</strong>, যাতে যে কেউ, যে কোনও সময়, যে কোনো অবস্থান থেকে শিক্ষালাভ করতে পারে।</p>

		<p>এই দৃষ্টিভঙ্গি থেকেই, আমি এই ওয়েবসাইটটি তৈরি করেছি। এখানে আমি সমস্ত পেইড বায়োলজি কোর্স, যা মূলত BiologyAdda-তে পাওয়া যায়, সকলের জন্য <strong>নিঃশুল্ক উপলব্ধ করেছি</strong>। শিক্ষার্থীরা, শিক্ষকেরা বা সাধারণ জ্ঞানচর্চার আগ্রহী যে কেউ, এই কনটেন্টের মাধ্যমে সহজেই তাদের শিক্ষা ও দক্ষতা বাড়াতে পারবে।</p>

		<p>শিক্ষার মূল লক্ষ্য কেবল জ্ঞান অর্জন নয়, বরং তা ব্যবহার করে সৃজনশীল এবং সমৃদ্ধ জীবন গড়া। এই ওয়েবসাইট সেই লক্ষ্যকে সামনে রেখে তৈরি করা হয়েছে—সবাই যাতে সমানভাবে শিক্ষার সুবিধা পায় এবং নিজের সৃজনশীলতার সর্বোচ্চ সম্ভাবনা কাজে লাগাতে পারে।</p>

		<p>সারসংক্ষেপে বলতে গেলে, <strong>এই ওয়েবসাইটটি আমি তৈরি করেছি সকল পেইড BiologyAdda বায়োলজি কোর্সকে ফ্রিতে উপলব্ধ করার জন্য</strong>, যাতে যে কেউ বিনা বাধায় শিক্ষালাভ করতে পারে এবং জ্ঞানকে সত্যিকার অর্থে মুক্তভাবে ব্যবহার করতে পারে।</p>
	</div>
</div>

<div class="my-10 flex items-center justify-center">
	 {@html `
<script src="https://counterapi.com/c.js?ns=bacracked.top" async ></script>
<div class="counterapi" startNumber="2873" key="whole-site" style="min-height:44px" ></div>
`}
</div>

<footer class="footer sm:footer-horizontal footer-center bg-base-200 text-base-content p-4">
  <aside>
    <p>&copy; Copyright {new Date().getFullYear()} - Made with love for all fellow learners!</p>
  </aside>
</footer>


<style lang="postcss">
	@reference 'tailwindcss';
	:global(html::after) {
		content: "";
		position: fixed;
		width: 100vw;
		height: 100vh;
		top: 0px;
		left: 0px;
		z-index: -999;
		background-image: radial-gradient(circle at top right,  #14532d80 1%, transparent 25%), radial-gradient(circle at bottom left,  #155e7580 1%, transparent 25%);
	}
</style>