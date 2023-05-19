<script>
	let prompt = '';
	let message = '';
	let isLoading = false;

	const sendPrompt = async () => {
		isLoading = true;
		try {
			const response = await fetch('http://127.0.0.1:5000?prompt=' + prompt);
			const data = await response.json();

			message = data.message;
		} catch (error) {
			console.log(error.message);
		} finally {
			isLoading = false;
		}
	};
</script>

<input type="text" bind:value={prompt} />
<button on:click={sendPrompt}>Ask gpt</button>
<h1>Este es el mensaje</h1>
{#if isLoading}
	<p>Cargando...</p>
{:else}
	<p>
		{message}
	</p>
{/if}
