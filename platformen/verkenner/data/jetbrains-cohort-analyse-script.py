# Vera 8 nov 2026 (gebruik: script <cdate.jsonl> <eerste-versie.jsonl>): cohort betaalde/freemium JetBrains-plugins op eerste publicatiedatum.
import json,sys,statistics,datetime as dt,collections
r=[json.loads(l) for l in open(sys.argv[1])]
E={}
for l in open(sys.argv[2]):
    e=json.loads(l)
    if e.get('eerste'): E[e['id']]=e['eerste']
for x in r: x['cdate']=E.get(x['id'])  # leeftijd = oudste versie, niet het veld cdate van de plugin
print('fouten',sum(1 for x in r if x.get('fout')))
r=[x for x in r if not x.get('fout') and x.get('cdate')]
GROOT={'JetBrains s.r.o.','JetBrains'}
nu=dt.datetime(2026,11,8)
def leeftijd(x): return (nu-dt.datetime.utcfromtimestamp(x['cdate']/1000)).days/30.44
per=collections.Counter(dt.datetime.utcfromtimestamp(x['cdate']/1000).year for x in r)
print('per jaar eerste publicatie',sorted(per.items()))
for lo,hi in ((3,6),(3,9),(6,12)):
    c=[x for x in r if lo<=leeftijd(x)<hi and x['maker'] not in GROOT]
    d=sorted(x['downloads'] for x in c)
    if not d: continue
    print(f'\n{lo}-{hi} mnd: n={len(c)} makers={len({x["maker"] for x in c})} paid={sum(x["model"]=="PAID" for x in c)} freemium={sum(x["model"]=="FREEMIUM" for x in c)}')
    print(' mediaan',statistics.median(d),' 100+',round(100*sum(v>=100 for v in d)/len(d)),'% 1000+',round(100*sum(v>=1000 for v in d)/len(d)),'% 5000+',sum(v>=5000 for v in d))
    print(' per maand nieuw', round(len(c)/(hi-lo),1))
    if (lo,hi)==(3,9):
        for x in sorted(c,key=lambda x:-x['downloads'])[:12]: print('  ',x['naam'],x['model'],x['downloads'],x['maker'],x['maker_type'],round(leeftijd(x),1))
