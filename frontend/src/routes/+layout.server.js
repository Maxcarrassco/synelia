export const load = async ({ url }) => {
	const tab = await url.searchParams.get("tab");
	return {
		tab,
	}
}
