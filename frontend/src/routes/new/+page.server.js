import { postData } from "$lib/request_utils.js";
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
  student: async (event) => {
	  const formData = await event.request.formData();
	  const data = Object.fromEntries(await formData);
	  const obj = {
		  name: data.name,
		  age: data.age,
		  gender: data.gender,
	  };
	  try {
	    await postData(obj, "students");
	  } catch (err) {
		  return fail(500, "Oop! An error occurred! We are working on it");
	  }
         throw redirect(301, "/?tab=Student")
  },
  classes: async (event) => {
	  const formData = await event.request.formData();
	  const data = Object.fromEntries(await formData);
	  const obj = {
		  label: data.label,
	  };
	  try {
	    await postData(obj, "classes");
	  } catch (err) {
		  return fail(500, "Oop! An error occurred! We are working on it");
	  }
         throw redirect(301, "/?tab=Class")
  },
  subject: async (event) => {
	  const formData = await event.request.formData();
	  const data = Object.fromEntries(await formData);
	  const obj = {
		  label: data.label,
	  };
	  try {
	    await postData(obj, "subjects");
	  } catch (err) {
		  return fail(500, "Oop! An error occurred! We are working on it");
	  }
         throw redirect(301, "/?tab=Subject")
  }
};
