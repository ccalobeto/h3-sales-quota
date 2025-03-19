<script>
	export let steps;
	export let index;
	export let title;
</script>

<h1>This is mapbox map!!</h1>
<h2>{title}</h2>

{#each steps as step}
	<p>{step}: {index}</p>
{/each}
