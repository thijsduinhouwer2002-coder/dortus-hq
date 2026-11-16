# Sem, 16 nov 2026: som, mediaan en top per meetmoment uit een fest-meting. Gebruik: python3 fest-stat.py (vanuit deze map, leest autobattler-fest-2026-11.csv)
import csv, statistics as st, collections
d=collections.defaultdict(dict)
for r in csv.DictReader(open('autobattler-fest-2026-11.csv')):
    if r['spelers_tegelijk']!='': d[r['tijd_utc']][r['appid']]=(int(r['spelers_tegelijk']),r['naam'])
for t in sorted(d):
    v=[x[0] for x in d[t].values()]
    top=max(d[t].values())
    print(t,len(v),'som',sum(v),'med',st.median(v),'0:',sum(1 for x in v if x==0),'>=20:',sum(1 for x in v if x>=20),'>=100:',sum(1 for x in v if x>=100),'top',top)
