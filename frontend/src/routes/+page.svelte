<script>
  export let data;
  const url = `/new/?tab=${data.tab}`;
</script>


<div class="relative overflow-x-auto px-[5%] mt-[3%] md:px-[25%]">
  <a href={url}><button class="btn btn-primary mb-[2%]">Add {data.tab}</button></a>
  <table class="table border-collapse">
    <thead>
      <tr>
        <th>Name</th>
        <th>Gender</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody>
   {#each data.student as s }
      <tr>
        <td>{s.name}</td>
        <td>{s.gender}</td>
        <td>{(s.updated_at) ? s.updated_at : s.created_at}</td>
      </tr>
   {/each}
    </tbody>
  </table>
</div>
