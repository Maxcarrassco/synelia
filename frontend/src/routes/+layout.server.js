import { redirect } from "@sveltejs/kit";

export const load = async ({ url }) => {
	const tab = await url.searchParams.get("tab");
	if (url.pathname === "/" && tab === null) {
	  throw redirect(301, "/?tab=Student");
	}
	return {
		tab,
	}
}
