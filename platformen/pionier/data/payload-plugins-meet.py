#!/usr/bin/env python3
"""Meet het Payload-plugin-ecosysteem op npm (Noor, pionier).
Haalt alle pakketten met keyword payload-plugin plus naam payload-plugin-*,
per pakket eerste publicatiedatum, laatste versie, peer-versie van payload,
en downloads van de afgelopen maand. Schrijft data/payload-plugins-<datum>.json.
Gebruik: python3 data/payload-plugins-meet.py"""
import json, urllib.request, urllib.parse, datetime, concurrent.futures, os, time
def get(u):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent':'dortus-meting'}), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2*(i+1)); err=e
    return {'_fout': str(err)}
namen=set()
for q in ['keywords:payload-plugin','keywords:payloadcms-plugin','payload-plugin','keywords:payload keywords:plugin','@payloadcms/plugin']:
    for start in range(0,1000,250):
        d=get('https://registry.npmjs.org/-/v1/search?'+urllib.parse.urlencode({'text':q,'size':250,'from':start}))
        objs=d.get('objects',[])
        for o in objs: namen.add(o['package']['name'])
        if len(objs)<250: break
def info(n):
    e=urllib.parse.quote(n,safe='@')
    m=get('https://registry.npmjs.org/'+e.replace('/','%2F'))
    if '_fout' in m: return None
    t=m.get('time',{}); lat=m.get('dist-tags',{}).get('latest')
    v=m.get('versions',{}).get(lat,{}) if lat else {}
    peer=(v.get('peerDependencies') or {}).get('payload') or (v.get('dependencies') or {}).get('payload')
    kw=v.get('keywords') or []
    dl=get('https://api.npmjs.org/downloads/point/last-month/'+e).get('downloads',0)
    return {'naam':n,'eerste':t.get('created','')[:10],'laatst':t.get('modified','')[:10],'versie':lat,
            'payload':peer,'licentie':v.get('license') if isinstance(v.get('license'),str) else str(v.get('license')),
            'keywords':kw[:12],'downloads_maand':dl,'omschrijving':(v.get('description') or '')[:160]}
with concurrent.futures.ThreadPoolExecutor(6) as ex:
    rij=[r for r in ex.map(info, sorted(namen)) if r]
# alleen echte payload-pakketten: payload als peer/afhankelijkheid
rij=[r for r in rij if r['payload']]
out=os.path.join(os.path.dirname(__file__),'payload-plugins-%s.json'%datetime.date.today())
json.dump(rij,open(out,'w'),indent=1)
print(len(namen),'gevonden,',len(rij),'met payload als afhankelijkheid ->',out)
