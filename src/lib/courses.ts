import fs from 'fs';

let courses : Array<Object> = JSON.parse(fs.readFileSync('./data.json', 'utf-8'));

export default courses;