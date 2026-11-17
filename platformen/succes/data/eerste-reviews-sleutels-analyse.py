import csv,json,os,sys,datetime as dt,statistics as st,collections
sys.path.insert(0,'.')
from parse import parse
r={x['appid']:x for x in csv.DictReader(open('/home/claude/dortus-hq/platformen/succes/data/nextfest-tussenpoos-bureaublad-2026-11-17.csv'))}
out=[]
for f in os.listdir('k'):
    if not f.endswith('.html') or f=='k.html': continue
    a=f[:-5]; x=r.get(a)
    if not x: continue
    revs=parse(open('k/'+f).read())
    revs=[v for v in revs if isinstance(v['datum'],str) and v['datum'][:2]=='20']
    if not revs: continue
    revs.sort(key=lambda v:v['datum'])
    rel=dt.date.fromisoformat(x['releasedatum'])
    store=int(x['reviews_totaal'])
    hp='h/'+a+'.json'
    if os.path.exists(hp):
        try:
            d=json.load(open(hp))['results']; store=sum(w['recommendations_up']+w['recommendations_down'] for w in d['rollups'])
        except Exception: pass
    pre=[v for v in revs if dt.date.fromisoformat(v['datum'])<rel]
    eerste10=revs[:10]
    gratis=sum(v['gratis'] for v in revs)
    g10=sum(v['gratis'] for v in eerste10)
    d10=(dt.date.fromisoformat(revs[9]['datum'])-rel).days if len(revs)>=10 else None
    up_g=[v['up'] for v in revs if v['gratis']]; up_b=[v['up'] for v in revs if not v['gratis']]
    out.append(dict(appid=a,naam=x['naam'],releasedatum=x['releasedatum'],prijs_usd=x['prijs_usd'],nextfest=int(x['nextfest_editie']!=''),
      reviews_winkel_tellen=store,reviews_community=len(revs),niet_meegeteld=max(0,len(revs)-store),gratis_gemarkeerd=gratis,
      gratis_in_eerste10=g10,voor_uitgave=len(pre),dagen_tot_10e_review_community=d10,
      pct_pos_gratis=round(100*sum(up_g)/len(up_g)) if up_g else '',pct_pos_betaald=round(100*sum(up_b)/len(up_b)) if up_b else '',
      reviews_eerste_28d=x['reviews_eerste_28d']))
json.dump(out,open('anaB.json','w'))
print(len(out))
