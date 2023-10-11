<script>
  export let data;
  const url = "/?tab=Student";
  console.log(data.avg)
</script>

<div class="relative overflow-x-auto px-[5%] mt-[3%] md:px-[25%]">
  <div class="flex justify-between">
    <a href={url}><button class="btn btn-primary mb-[2%]">Back</button></a>
  </div>
  <table class="table border-collapse">
    <thead>
      <tr>
        <th>Score</th>
        <th>Student ID</th>
        <th>Subject ID</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody>
   {#each data.obj as s }
      <tr>
        <td>{s.grade}</td>
        <td>{s.student_id}</td>
        <td>{s.subject_id}</td>
        <td>{(s.updated_at) ? s.updated_at : s.created_at}</td>
      </tr>
   {/each}
    </tbody>
  </table>
</div>

<div class="relative overflow-x-auto px-[5%] mt-[3%] md:px-[25%]">
  <table class="table border-collapse">
    <thead>
      <tr>
        <th>Subject ID</th>
        <th>Subject</th>
        <th>Average</th>
      </tr>
    </thead>
    <tbody>
   {#each Object.entries(data.avg) as [_, s] }
      <tr>
        <td>{s.subject_id}</td>
        <td>{s.subject}</td>
        <td>{s.avg}</td>
      </tr>
   {/each}
    </tbody>
  </table>
</div>
