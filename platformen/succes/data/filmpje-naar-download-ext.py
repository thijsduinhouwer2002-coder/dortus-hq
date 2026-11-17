# Haalt de lijst van extensies van extensions.blender.org naar een json (de API geeft alles op één pagina).
# Gebruik: python3 filmpje-naar-download-ext.py <uit.json>
import json, sys, urllib.request
d = json.load(urllib.request.urlopen("https://extensions.blender.org/api/v1/extensions/", timeout=60))
alle = {x['id']: {k: x.get(k) for k in ('id', 'name', 'tagline', 'type', 'website')} for x in d['data']}
json.dump(list(alle.values()), open(sys.argv[1], 'w'))
print(len(alle))
