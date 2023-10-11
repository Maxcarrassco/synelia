<script>
  export let selectedTab;
  console.log("Come", selectedTab);
</script>

<div class="tabs justify-center text-4xl">
  {#if selectedTab === "Class"}	
    <a class="tab tab-bordered tab-active" href="/?tab=Class">Class</a> 
  {:else}
    <a class="tab tab-bordered" href="/?tab=Class">Class</a> 
  {/if}
  {#if selectedTab === "Student"}	
    <a class="tab tab-bordered tab-active" href="/?tab=Student">Student</a> 
  {:else}
    <a class="tab tab-bordered" href="/?tab=Student">Student</a> 
  {/if}
  {#if selectedTab === "Subject"}	
    <a class="tab tab-bordered tab-active" href="/?tab=Subject">Subject</a>
  {:else}
    <a class="tab tab-bordered" href="/?tab=Subject">Subject</a>
  {/if}
</div>
