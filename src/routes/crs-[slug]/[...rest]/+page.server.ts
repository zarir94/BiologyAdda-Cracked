//@ts-nocheck
import courses from "$lib/courses";
import { error, redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async ({ params, cookies }) => {
    let { slug, rest } = params;
    let [sec_slug, con_slug] = rest.split('/');
    let cur_content;
    try {
        cur_content = courses
        .find((i) => i.slug == slug)
        .sections.find((i) => i.slug == sec_slug)
        ?.contents.find((i) => i.slug == con_slug);
    } catch (err) {
        error(404);
    }
    if (!cur_content) {
        sec_slug = courses.find(i=>i.slug == slug).sections[0].slug;
        con_slug = courses.find(i=>i.slug == slug).sections[0].contents[0].slug;
        redirect(302, `/crs-${slug}/${sec_slug}/${con_slug}`)
    }
    return {
        slug, sec_slug, con_slug, cur_content,
        pin: cookies.get('pin') != 'false',
        info: (()=>{
            let crs = courses.find(i=>i.slug == slug);
            return {
                        title: crs.title,
                        slug: crs.slug,
                        sections: crs.sections.map((i) => ({
                            title: i.title,
                            slug: i.slug,
                            contents: i.contents.map((i) => ({ title: i.title, slug: i.slug }))
                        }))
                    };
            })()
    }
};