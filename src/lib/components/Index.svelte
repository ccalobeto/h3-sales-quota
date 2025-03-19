<script>
	import { getContext } from 'svelte';
	import Control from './Control.svelte';

	const copy = getContext('copy');
</script>

<main>
	<section>
		<h1>{copy.title}</h1>
		<p>{@html copy.description}</p>
		<img src="missing-child.jpg" alt="" />
		<p class="byline">{@html copy.byline}</p>
	</section>

	<article>
		<Control {copy} />
	</article>

	<div class="footer">
		<p class="made-with">{@html copy.footer}</p>
	</div>
</main>
