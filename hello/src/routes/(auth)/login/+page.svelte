<script>
	let username = '';
	let password = '';

	function submit() {
		console.log(username, password);
	}
</script>

<input class="border border-gray-800" type="text" bind:value={username} />
<input class="border border-gray-800" type="password" bind:value={password} />

<a href="/" class="my-button"> click me! </a>

<style lang="postcss">
	.my-button {
		@apply bg-blue-500 text-white font-bold py-2 px-4 rounded;
	}
</style>
