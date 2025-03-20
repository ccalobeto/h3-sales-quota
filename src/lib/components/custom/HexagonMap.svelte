<script>
	import { Map, MapSource, MapLayer } from '@onsvisual/svelte-maps';

	import { mapStyle } from '$lib/config.js';

	export let data;
	export let bounds;

	let hovered;
	let map = null;
</script>

{#if data}
	<div class="map-container">
		<Map bind:map style={mapStyle} controls location={{ bounds }}>
			<MapSource id="geo" type="geojson" {data} promoteId="areacd">
				<MapLayer
					id="geo-fill"
					type="fill"
					paint={{
						'fill-color': 'gray',
						'fill-opacity': ['case', ['==', ['feature-state', 'hovered'], true], 0.3, 0]
					}}
					hover
					bind:hovered
				></MapLayer>
				<MapLayer
					id="geo-line"
					type="line"
					paint={{
						'line-color': 'gray',
						'line-width': ['case', ['==', ['feature-state', 'hovered'], true], 2.5, 0.7]
					}}
				/>
			</MapSource>
		</Map>
	</div>
{/if}

<style>
	.map-container {
		height: 500px;
	}
</style>
