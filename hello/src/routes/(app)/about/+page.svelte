<h1>about</h1>

<script>
	import { onMount } from 'svelte';
    
    let message = ''

    onMount(async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/about')
            const data = await response.json()

            message = data.message
        } catch (error) {
            console.log(error.message)
        }
    })
</script>


<p>
    {message}
</p>
