import json,sys,statistics as st,collections as C
r=[json.loads(l) for l in open(sys.argv[1])]
r=[x for x in r if x.get('productType')]  # lege foutpagina's eruit
print('pagina ok',len(r))
d=[x for x in r if x.get('releaseDateUtc')]
print('met datum',len(d),'zonder (XP e.d.)',len(r)-len(d))
apps=[x for x in d if str(x.get('mediaType','')).lower()=='apps']  # zonder games
print('apps met datum',len(apps))
byy=C.Counter(x['releaseDateUtc'][:4] for x in apps); print('apps per jaar',sorted(byy.items()))
bym=C.Counter(x['releaseDateUtc'][:7] for x in apps if x['releaseDateUtc']>='2025-07'); print('apps per maand',sorted(bym.items()))
def rep(name,g):
    if not g: print(name,0);return
    rc=sorted(x.get('ratingCount',0) or 0 for x in g)
    print(f"{name}: n={len(g)} mediaan={st.median(rc)} onder5(toont0)={sum(v==0 for v in rc)/len(g):.0%} 5+={sum(v>=5 for v in rc)/len(g):.0%} 20+={sum(v>=20 for v in rc)/len(g):.0%} 100+={sum(v>=100 for v in rc)/len(g):.0%} max={rc[-1]}")
coh=[x for x in apps if '2026-05'<=x['releaseDateUtc'][:7]<='2026-08']
old=[x for x in apps if '2025-09'<=x['releaseDateUtc'][:7]<='2026-02']
for nm,c in [('lichting mei-aug 2026',coh),('lichting sep 2025-feb 2026',old)]:
    rep(nm+' alle apps',c)
    rep(nm+' betaald',[x for x in c if (x.get('price') or 0)>0])
    rep(nm+' gratis met add-ons',[x for x in c if not (x.get('price') or 0)>0 and x.get('hasAddOns')])
    rep(nm+' gratis zonder add-ons',[x for x in c if not (x.get('price') or 0)>0 and not x.get('hasAddOns')])
    rep(nm+' Utilities',[x for x in c if x.get('categoryId')=='Utilities & tools'])
    print(' categorieen',C.Counter(x.get('categoryId') for x in c).most_common(8))
    pub=C.Counter(x.get('publisherId') for x in c); print(' makers',len(pub),'grootste',pub.most_common(3))
