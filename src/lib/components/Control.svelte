<script>
	import MapboxMap from './custom/MapboxMap.svelte';

	export let copy;
</script>

<div class="charts-container">
	<!-- {console.log("Charts: step => ", step)} -->
	{#each copy.body as item, index}
		<div class="type-{item['type']}">
			{#if item.type === 'text'}
				<p class="text-blocks">{@html item.value}</p>
			{/if}
			{#if item.type === 'mapbox-chart-1'}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<MapboxMap {steps} {index} {title} />
			{/if}
			{#if item.type === 'map-box-chart-2'}
				{@const steps = item.value.steps}
				{@const title = item.title}
				<MapboxMap {steps} {index} {title} />
			{/if}
		</div>
	{/each}
</div>
