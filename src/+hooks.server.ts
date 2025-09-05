import { redirect, type Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	let host = event.request.headers.get('Host');
	console.log(host);
	
	if (host == 'bacracked.onrender.com') {
		redirect(301, new URL(event.url.pathname, 'http://bacracked.top'))
	}

	const response = await resolve(event);
	return response;
};
