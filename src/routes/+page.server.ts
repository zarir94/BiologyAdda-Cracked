//@ts-nocheck
import courses from '$lib/courses';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
    let all_courses = courses.map(i=>{
        i = structuredClone(i);
        delete i.sections;
        return i;
    });
    
    return { all_courses }    
};
