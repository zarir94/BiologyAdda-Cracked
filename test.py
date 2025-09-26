import json

data = json.load(open('data.json'))

typesAndSources = list(set([(ct.get('type'), ct.get('source')) for c in data for s in c.get('sections') for ct in s.get('contents')]))
# types = list(set([ct.get('type') for c in data for s in c.get('sections') for ct in s.get('contents')]))
# sources = list(set([ct.get('source') for c in data for s in c.get('sections') for ct in s.get('contents')]))

print(typesAndSources)
# print(types)
# print(sources)

