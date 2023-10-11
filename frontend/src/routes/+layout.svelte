<script>
  import "../app.css";
  import Navbar from "$lib/components/Navbar.svelte";
  import Header from "$lib/components/Header.svelte";
  export let data;
</script>

<div class="mb-8">
  <Navbar />
</div>
<Header selectedTab={data.tab} />
<slot />
