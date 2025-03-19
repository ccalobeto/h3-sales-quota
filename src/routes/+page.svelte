<script>
	import { setContext } from 'svelte';
	import Meta from '$lib/components/Meta.svelte';
	import Index from '$lib/components/Index.svelte';
	import copy from '$lib/data/copy.json';

	export let data;

	const preloadFont = [
		'https://pudding.cool/assets/fonts/tiempos/TiemposTextWeb-Regular.woff2',
		'https://pudding.cool/assets/fonts/tiempos/TiemposTextWeb-Bold.woff2',
		'https://pudding.cool/assets/fonts/atlas/AtlasGrotesk-Regular-Web.woff2',
		'https://pudding.cool/assets/fonts/atlas/AtlasGrotesk-Bold-Web.woff2'
	];

	const { title, description, url, keywords } = copy;
	setContext('copy', copy);
	setContext('data', data);
</script>

<Meta {title} {description} {url} {preloadFont} {keywords} />
<Index />
