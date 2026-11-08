# Haalt alle gepubliceerde TRMNL-recipes via de open Recipes API (/recipes.json), rustig (1 per 2 s)
import json, time, sys, urllib.request
A={'User-Agent':'Mozilla/5.0 DortusVerkenner'}
out=[]; p=1
while True:
    u=f'https://trmnl.com/recipes.json?sort-by=newest&per_page=100&page={p}'
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=A),timeout=60))
    for r in d['data']:
        r.pop('custom_fields',None); out.append(r)
    if not d.get('next_page_url'): break
    p+=1; time.sleep(2)
json.dump(out,open(sys.argv[1],'w'))
print(len(out))
