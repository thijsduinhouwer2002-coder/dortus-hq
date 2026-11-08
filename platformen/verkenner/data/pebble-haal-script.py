# Haalt alle zichtbare Pebble-apps en wijzerplaten uit de open API van apps.repebble.com
# Gebruik: python3 -I pebble-haal-script.py  (schrijft watchapps-and-companions.json en watchfaces.json)
import json,urllib.request,time
for c in ['watchapps-and-companions','watchfaces']:
    out=[];off=0
    while True:
        u=f"https://appstore-api.repebble.com/api/v1/apps/collection/all/{c}?limit=100&offset={off}"
        d=json.load(urllib.request.urlopen(u,timeout=60))
        for a in d['data']:
            ch=a.get('changelog') or [{}]
            out.append({'id':a['id'],'title':a['title'],'author':a['author'],'hearts':a.get('hearts'),
                        'created_at':a.get('created_at'),'first':ch[-1].get('published_date'),
                        'description':a.get('description')})
        if not d['data'] or not d['links'].get('nextPage'): break
        off+=100; time.sleep(0.3)
    json.dump(out,open(c+'.json','w')); print(c,len(out))
