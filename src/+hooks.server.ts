import { redirect, type Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	if (event.request.headers.get('Host') == 'bacracked.onrender.com') {
		redirect(301, new URL(event.url.pathname, 'http://bacracked.top'))
	}

	const response = await resolve(event);
	return response;
};
