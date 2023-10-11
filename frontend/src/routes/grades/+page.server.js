import { getData } from '$lib/request_utils.js';

export const load = async ({ url }) => {
	const students_id = await url.searchParams.get("id");
	const route =  `students/${students_id}/grades`;
	const data = await getData(route);
	const avg = await getData(route+"/avg");
	return {
		obj: await data.json(),
		avg: await avg.json(),
	}
}
