import { postData } from "$lib/request_utils.js";
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
  default: async (event) => {
	  const formData = await event.request.formData();
	  const data = Object.fromEntries(await formData);
	  const obj = {
		  name: data.name,
		  gender: data.gender,
	  };
	  try {
	    await postData(obj, "students");
	  } catch (err) {
		  return fail(500, "Oop! An error occurred! We are working on it");
	  }
         throw redirect(301, "/")
  }
};
