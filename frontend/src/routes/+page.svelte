<script>
  export let data;
  const url = `/new/?tab=${data.tab}`;
</script>

{#if data.tab === "Student"}
<div class="relative overflow-x-auto px-[5%] mt-[3%] md:px-[25%]">
  <div class="flex justify-between">
    <a href={url}><button class="btn btn-primary mb-[2%]">Add {data.tab}</button></a>
    <a href={url + '&&grade=true'}><button class="btn btn-primary mb-[2%]">Record Grade</button></a>
  </div>
  <table class="table border-collapse">
    <thead>
      <tr>
        <th>Student ID</th>
        <th>Name</th>
        <th>Age</th>
        <th>Gender</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody>
   {#each data.obj as s }
      <tr>
        <td>{s.id}</td>
        <td>{s.name}</td>
        <td>{s.age}</td>
        <td>{s.gender}</td>
        <td>{(s.updated_at) ? s.updated_at : s.created_at}</td>
        <a href={'/grades/?id=' + s.id }><button class="btn btn-secondary mb-[2%]"><td>View Grade</td></button></a>
      </tr>
   {/each}
    </tbody>
  </table>
</div>
{:else if data.tab === "Class" || data.tab === "Subject" }	
<div class="relative overflow-x-auto px-[5%] mt-[3%] md:px-[25%]">
  <a href={url}><button class="btn btn-primary mb-[2%]">Add {data.tab}</button></a>
  <table class="table border-collapse">
    <thead>
      <tr>
        <th>ID</th>
        <th>Label</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody>
   {#each data.obj as s }
      <tr>
        <td>{s.id}</td>
        <td>{s.label}</td>
        <td>{(s.updated_at) ? s.updated_at : s.created_at}</td>
      </tr>
   {/each}
    </tbody>
  </table>
 </div>
{:else if data.tab === "Subject" }	
<div class="relative overflow-x-auto px-[5%] mt-[3%] md:px-[25%]">
  <a href={url}><button class="btn btn-primary mb-[2%]">Add {data.tab}</button></a>
  <table class="table border-collapse">
    <thead>
      <tr>
        <th>ID</th>
        <th>Label</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody>
   {#each data.obj as s }
      <tr>
        <td>{s.id}</td>
        <td>{s.label}</td>
        <td>{(s.updated_at) ? s.updated_at : s.created_at}</td>
      </tr>
   {/each}
    </tbody>
  </table>
 </div>
{/if}
