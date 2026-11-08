# Analyse van de Premiere-lijst uit Adobe Exchange. Gebruik: python3 premiere-uxp-analyse.py premiere-uxp-<datum>.json
# Meten: node premiere-uxp-meet.js premiere-uxp-<datum>.json (bladert met Playwright door alle pagina s, ±6 minuten)
import json,statistics as st,collections as C,sys
L=json.load(open(sys.argv[1]))
print('totaal',len(L))
t=C.Counter(x.get('type') for x in L);print('soort',t)
def dl(x):return x.get('uniqueDownloadsCount') or 0
def price(x):return (x.get('pricingInfo') or {}).get('price') or 0
for typ in ['UXP','ZXP']:
  S=[x for x in L if x.get('type')==typ]
  m=C.Counter(x['firstPublishedAt'][:7] for x in S if x.get('firstPublishedAt'))
  print(typ,'per maand (2025-07..):',{k:v for k,v in sorted(m.items()) if k>='2025-07'})
  paid=[x for x in S if price(x)>0];print(typ,'betaald',len(paid),'van',len(S))
  subs=[x for x in S if (x.get('pricingInfo') or {}).get('subscription')];print(typ,'abonnement',len(subs))
  ds=[dl(x) for x in S];print(typ,'downloads mediaan',st.median(ds) if ds else 0,'100+',sum(d>=100 for d in ds),'1000+',sum(d>=1000 for d in ds))
U=[x for x in L if x.get('type')=='UXP']
# leeftijd 2-6 maanden (mei-sep 2026)
g=[x for x in U if '2026-05'<=x['firstPublishedAt'][:7]<='2026-09']
ds=sorted(dl(x) for x in g);print('UXP gepubliceerd mei-sep 2026:',len(g),'mediaan dl',st.median(ds) if ds else '-', 'kwartielen',ds[len(ds)//4] if ds else '',ds[3*len(ds)//4] if ds else '')
print('\nTop 25 UXP op downloads:')
for x in sorted(U,key=dl,reverse=True)[:25]:
  print(dl(x),x['firstPublishedAt'][:10],price(x),'|',x.get('naam') or x['localizedMetadata']['name'],'|',x.get('maker'),'|',x.get('summary'))
print('\nBetaalde UXP:')
for x in sorted(U,key=dl,reverse=True):
  if price(x)>0: print(dl(x),x['firstPublishedAt'][:10],price(x),(x.get('pricingInfo') or {}).get('subscription'),'|',x.get('naam') or x['localizedMetadata']['name'],'|',x.get('summary'))
print('\nTop 30 CEP op downloads:')
C2=[x for x in L if x.get('type')=='ZXP']
for x in sorted(C2,key=dl,reverse=True)[:30]:
  print(dl(x),x['firstPublishedAt'][:10],price(x),'|',x.get('naam') or x['localizedMetadata']['name'],'|',x.get('summary'))
