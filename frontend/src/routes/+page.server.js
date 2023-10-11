import { getData } from '$lib/request_utils.js';

export const load = async ({ url }) => {
	const tab = await url.searchParams.get("tab");
	let route = "students";
	if (tab === "Subject") {
		route = "subjects";
	} else if (tab === "Class") {
		route = "classes";
	}
	const data = await getData(route);
	return {
		obj: await data.json(),
	}
}
