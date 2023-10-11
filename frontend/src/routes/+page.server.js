import { getData } from '$lib/request_utils.js';

export const load = async ({ url }) => {
	const tab = await url.searchParams.get("tab");
	const data = await getData("students");
	return {
		student: await data.json(),
		tab,
	}
}
