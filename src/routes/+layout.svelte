<script>
	import '$lib/styles/app.css';
	// import Header from '$lib/components/Header.svelte';

	export let children;
</script>

<!-- <Header /> -->
<main id="content">
	{@render children?.()}
</main>
