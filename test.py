import json

data = json.load(open('data.json'))

types = list(set([ct.get('type') for c in data for s in c.get('sections') for ct in s.get('contents')]))
sources = list(set([ct.get('source') for c in data for s in c.get('sections') for ct in s.get('contents')]))

print(types)
print(sources)


