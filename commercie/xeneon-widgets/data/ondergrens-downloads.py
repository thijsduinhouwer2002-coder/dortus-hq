#!/usr/bin/env python3
"""Ondergrens van downloads per iCUE-widget uit de openbare volgorde Popular (ordering=-download_count) van mp-gateway.elgato.com.
Gelijke tellingen staan op id oplopend; elke breuk in die oplopende reeks is een lagere telling. Het aantal breuken onder een widget is dus een ondergrens.
Gebruik: python3 -I ondergrens-downloads.py widgets-<datum>.json (gemaakt met platformen/pionier/data/xeneon-widgets-meet.py)
Wisselkoersen in FX zijn ruwe GOK-koersen van nov 2026."""
import json,sys,collections,statistics as st
b=json.load(open(sys.argv[1]))
w={x['id']:x for x in b['widgets']};r=[i for i in b['rang_downloads'] if i in w]
# groups: maximal runs of ascending id; each break = strictly lower download count
groups=[[r[0]]]
for p,q in zip(r,r[1:]):
    (groups[-1].append(q) if q>p else groups.append([q]))
G=len(groups); print('widgets',len(r),'groepen (min. aantal verschillende downloadtellingen)',G)
lb={}
for gi,g in enumerate(groups):
    for i in g: lb[i]=G-1-gi
print('grootte onderste 6 groepen',[len(g) for g in groups[-6:]])
paid=lambda i: not w[i]['variants'][0]['is_free']
P=[i for i in r if paid(i)]
print('betaald: ondergrens downloads, verdeling', collections.Counter(min(lb[i],50)//5*5 for i in P))
print('betaald in onderste groep',sum(lb[i]==0 for i in P),'van',len(P))
print('betaald ondergrens >=10:',sum(lb[i]>=10 for i in P),'>=20:',sum(lb[i]>=20 for i in P),'>=50:',sum(lb[i]>=50 for i in P))
for i in P[:25]:
    x=w[i];print(lb[i],x['name'],'|',x['org_name'],x['variants'][0]['price']['unit_amount']/100,x['created_at'][:10])
F=[i for i in r if not paid(i)]
print('gratis ondergrens top 5',[ (w[i]['name'],lb[i]) for i in F[:5]])
# per maker: min. omzet = sum lb*price*0.7
om=collections.Counter()
for i in P: om[w[i]['org_name']]+=lb[i]*w[i]['variants'][0]['price']['unit_amount']/100*0.7
print('ondergrens netto per maker ($, 70%)',[(k,round(v)) for k,v in om.most_common(12)])
# by month created
for m in ['2026-08','2026-09','2026-10','2026-11']:
    s=[lb[i] for i in P if w[i]['created_at'][:7]==m]; print(m,len(s),'mediaan ondergrens',st.median(s) if s else None,'aandeel >=5',round(sum(v>=5 for v in s)/len(s),2) if s else None)
print('valuta',collections.Counter(w[i]['variants'][0]['price']['currency'] for i in P))
FX={'USD':1,'SAR':1/3.75,'EUR':1.08,'GBP':1.27,'CAD':0.72,'AUD':0.65,'MXN':0.055,'AED':0.272,'ILS':0.27,'JPY':0.66}
om=collections.Counter(); tot=0
for i in P:
    p=w[i]['variants'][0]['price']; v=lb[i]*p['unit_amount']/100*FX.get(p['currency'],float('nan'))*0.7; om[w[i]['org_name']]+=v; tot+=v
print('ondergrens netto per maker in USD',[(k,round(v)) for k,v in om.most_common(10)],'totaal',round(tot))
print('makers met ondergrens >= $100:',sum(v>=100 for v in om.values()),'van',len(om))
usd=[w[i]['variants'][0]['price']['unit_amount']/100*FX.get(w[i]['variants'][0]['price']['currency'],float('nan')) for i in P]
print('prijs mediaan USD',round(st.median(usd),2))
a=[i for i in P if w[i]['name']=='AI Usage Dashboard'];print('AI Usage Dashboard ondergrens',[lb[i] for i in a],[w[i]['variants'][0]['price'] for i in a])
