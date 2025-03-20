<script>
	import { onMount } from 'svelte';
	import { bbox } from 'topojson-client';
	import { geoTypes } from '$lib/config';

	import HexagonMap from './custom/HexagonMap.svelte';

	import topo from '$lib/data/peru-100k.json';
	import { hexagons, geoData } from '$lib/data/cookedData';

	export let copy;

	let bounds;
	const geoPoints = geoData();
	const h3Hexagons = hexagons();

	// console.log('Control: hexagons => ', h3Hexagons);

	async function init() {
		bounds = bbox(topo);
	}

	onMount(init);
	$: console.log('Control: bounds => ', bounds);
</script>

<div class="charts-container">
	<!-- {console.log("Charts: step => ", step)} -->
	{#each copy.body as item, index}
		<div class="type-{item['type']}">
			{#if item.type === 'text'}
				<p class="text-blocks">{@html item.value}</p>
			{/if}
			<!-- {#if item.type === 'mapbox-chart-1'}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<MapboxMap {steps} {index} {title} />
			{/if} -->
			{#if item.type === 'map-box-chart-2'}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<HexagonMap data={h3Hexagons} {bounds} />
			{/if}
		</div>
	{/each}
</div>
