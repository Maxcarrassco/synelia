<script>
  export let data;
  const url = `/?tab=${data.tab}`;
</script>


{#if data.tab === "Student"}
<form class="flex justify-center flex-col items-center my-[10%] p-8 border-4 mx-[15%] rounded-md" method="POST" action="?/student">
  <div class="w-2/5">
    <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
    <input id="name" name="name" type="text" placeholder="Type the student name here" required class="block w-full p-8 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
  </div>
  <div class="w-2/5 mt-4">
    <label for="age" class="block text-sm font-medium leading-6 text-gray-900">Age</label>
    <input id="age" name="age" type="number" placeholder="Type the student age here" required class="block w-full p-8 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
  </div>
  <div class="form-control">
    <label class="label cursor-pointer">
      <span class="label-text">Male</span> 
      <input type="radio" name="gender" value="male" class="radio checked:bg-red-500" />
    </label>
  </div>
  <div class="form-control">
    <label class="label cursor-pointer">
      <span class="label-text">Female</span> 
      <input type="radio" name="gender" value="female" class="radio checked:bg-blue-500" />
    </label>
  </div>
  <div class="md:flex md:w-1/5 md:p-4 md:justify-between">
   <a class="btn btn-secondary" href={url}>Cancel</a>
   <button class="btn btn-primary">Save</button>
  </div>
</form>

{:else if data.tab === "Class"}
<form class="flex justify-center flex-col items-center my-[10%] p-8 border-4 mx-[15%] rounded-md" method="POST" action="?/classes">
  <div class="w-2/5">
    <label for="label" class="block text-sm font-medium leading-6 text-gray-900">Label</label>
    <input id="label" name="label" type="text" placeholder="Type the class name here" required class="block w-full p-8 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
  </div>
  <div class="md:flex md:w-1/5 md:p-4 md:justify-between">
   <a class="btn btn-secondary" href={url}>Cancel</a>
   <button class="btn btn-primary">Save</button>
  </div>
</form>
{:else if data.tab === "Subject"}	
<form class="flex justify-center flex-col items-center my-[10%] p-8 border-4 mx-[15%] rounded-md" method="POST" action="?/subject">
  <div class="w-2/5">
    <label for="label" class="block text-sm font-medium leading-6 text-gray-900">Label</label>
    <input id="label" name="label" type="text" placeholder="Type the class name here" required class="block w-full p-8 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
  </div>
  <div class="md:flex md:w-1/5 md:p-4 md:justify-between">
   <a class="btn btn-secondary" href={url}>Cancel</a>
   <button class="btn btn-primary">Save</button>
  </div>
</form>	
{/if}
