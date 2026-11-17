import csv,sys,json
from datetime import date
sys.path.insert(0,'..')
from bn_vers import versions
from bn_rate import daily,win
rows=[r for r in csv.DictReader(open('/home/claude/dortus-hq/platformen/succes/data/blender-extensions-nieuw-2026-11-16.csv')) if '2026-09-01'<=r['eerste']<='2026-11-02']
ext={e['id']:e for e in json.load(open('ext.json'))['data']}
res=[]
for r in rows:
    e=ext.get(r['id'])
    if not e: continue
    slug=e['website'].rstrip('/').split('/')[-1] if 'extensions.blender.org' in (e['website'] or '') else r['id'].replace('_','-')
    vs=versions(slug)
    if not vs: continue
    ser=daily(vs); f=min(date.fromisoformat(v[2]) for v in vs)
    a=win(ser,f,0,3); b=win(ser,f,4,10)
    if a[0] and b[1]>=7: res.append((r['naam'],a[0],b[0],b[0]/a[0] if a[0] else 0,len(vs)))
res.sort(key=lambda x:-x[3])
print(len(res))
import statistics
print('mediaan verhouding dag4-10/dag0-3',statistics.median([x[3] for x in res]))
print('aandeel >=3x',sum(1 for x in res if x[3]>=3)/len(res), sum(1 for x in res if x[3]>=3))
for x in res[:15]: print(x)
json.dump(res,open('ctrl.json','w'))
