# Telt: hele steekproef (subs.json) en apps met 1 tot 5 reviews naar maand van eerste review (rev15.jsonl).
import json,sys,statistics as st
from collections import Counter
subs=json.load(open(sys.argv[1])); apps={}
for k,v in subs.items():
    if k.startswith('featured-apps/'): continue
    for a in v['apps']: apps[a['slug']]=a
r=[a['reviews']['totalCount'] for a in apps.values()]
print('apps uniek',len(apps),'mediaan reviews',st.median(r),'0 reviews',sum(x==0 for x in r),'10+',sum(x>=10 for x in r),'100+',sum(x>=100 for x in r))
print('prijsvormen',Counter(a['pricing'] if isinstance(a['pricing'],str) else a['pricing']['label']['type'] for a in apps.values()))
rows=[json.loads(l) for l in open(sys.argv[2])]
rows=[x for x in rows if not x.get('fout') and x['dates']]
fm=Counter(min(x['dates'])[:7] for x in rows)
print('eerste review per maand (apps met 1-5 reviews):',sorted(fm.items())[-14:])
g=[x for x in rows if '2026-05'<=min(x['dates'])[:7]<='2026-08']
print('eerste review mei-aug 2026: n',len(g),'reviews',Counter(x['reviews']['totalCount'] for x in g))
print('bedrijven',Counter(x['company'] for x in g).most_common(8))
