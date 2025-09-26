from requests import get
from bs4 import BeautifulSoup
import json, time


def modGet(*a, **kw):
    try:
        r = get(*a, **kw)
        if r.status_code == 500:
            time.sleep(5)
            return modGet(*a, **kw)
        return r
    except Exception as e:
        print('modGet:', e)
        return modGet(*a, **kw)


def getURLfromHTML(html: str, removeArgs: bool = False):
    doc = BeautifulSoup(html or '', 'html.parser')
    if e := doc.select_one('[href],[src]'):
        u = e.get('href', e.get('src', None))
        if u and removeArgs: u = u.split('?')[0]
        return u


def get_single_course_data(slug: str):
    data = modGet('https://api.biologyadda.com/api/courses/' + slug).json()
    course = dict(title=data['title'], slug=data['slug'], img=data['image']['link'], sections=[])

    for s in data['sections']:
        asec = dict(title=s['title'], slug=s['slug'], contents=[])
        for c in s['contents']:
            acon = dict(title=c['title'], slug=c['slug'], type=c['type'])
            rd = modGet('https://api.biologyadda.com/api/content/' + c["slug"]).json()['data'][c['type']]
            if c['type'] == 'video':
                lk = None
                if rd['source'] == 'embedded':
                    lk = getURLfromHTML(rd.get('embedded'), True)
                acon = acon | dict(source=rd['source'], link=lk or rd.get('link'))
            elif c['type'] == 'link' or c['type'] == 'pdf':
                acon['link'] = rd['link']
            elif c['type'] == 'note':
                acon['html'] = rd['body']
            elif c['type'] == 'exam':
                pass
            else:
                raise Exception('Unsupported content type %s. Data: %s' % (c['type'], str(rd)))
            asec['contents'].append(acon)
        course['sections'].append(asec)

    return course


def get_all_course_data():
    all_courses = []
    done_slugs = []
    rd = modGet('https://api.biologyadda.com/api/course-category').json()['data']
    for s, t in {l['slug']: l['title'] for l in rd}.items():
        rd = modGet('https://api.biologyadda.com/api/courses?category_slug=' + s).json()['data']
        for c in rd:
            if c['slug'] in done_slugs: continue
            all_courses.append(get_single_course_data(c['slug']) | dict(category=dict(title=t, slug=s)))
            done_slugs.append(c['slug'])
    return all_courses



if __name__ == '__main__':
    cd = get_all_course_data()
    # print(cd)
    json.dump(cd, open('data.json', 'w'), indent=4)
