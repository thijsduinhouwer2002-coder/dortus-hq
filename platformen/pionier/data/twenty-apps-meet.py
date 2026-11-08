#!/usr/bin/env python3
"""Telt Twenty-apps op npm (keyword twenty-app): aantal, eerste publicatie per maand, makers, downloads.
Gebruik: python3 -I twenty-apps-meet.py [uitvoer.json]   (Noor, 8 nov 2026)"""
import json, sys, time, urllib.request, urllib.parse, collections
def get(u):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent':'dortus-research'}), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2)
    return None
pk={}
for frm in range(0, 2000, 250):
    d=get(f'https://registry.npmjs.org/-/v1/search?text=keywords:twenty-app&size=250&from={frm}')
    if not d or not d.get('objects'): break
    for o in d['objects']:
        p=o['package']; pk[p['name']]=p
    if len(d['objects'])<250: break
rows=[]
for n,p in sorted(pk.items()):
    meta=get('https://registry.npmjs.org/'+urllib.parse.quote(n,safe='@'))
    created=(meta or {}).get('time',{}).get('created','')[:10]
    dl=get('https://api.npmjs.org/downloads/point/last-month/'+urllib.parse.quote(n,safe='@'))
    rows.append({'name':n,'created':created,'publisher':(p.get('publisher') or {}).get('username'),
                 'scope':n.split('/')[0] if n.startswith('@') else '', 'desc':(p.get('description') or '')[:120],
                 'downloads_last_month':(dl or {}).get('downloads'),
                 'repo':(p.get('links') or {}).get('repository')})
    time.sleep(0.15)
out=sys.argv[1] if len(sys.argv)>1 else f'twenty-apps-{time.strftime("%Y-%m-%d")}.json'
json.dump(rows, open(out,'w'), indent=1)
print('pakketten', len(rows))
print('nieuw per maand', sorted(collections.Counter(r['created'][:7] for r in rows).items()))
print('makers', len(set(r['publisher'] for r in rows)))
print('top makers', collections.Counter(r['publisher'] for r in rows).most_common(8))
