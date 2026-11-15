# Vera 15 nov 2026: analyse van uit.jsonl van nuvemshop-haal-script.py. Gebruik: python3 -I script.py uit.jsonl
import json,sys,statistics as st,collections as C
rs=[json.loads(l) for l in open(sys.argv[1])]
ok=[r for r in rs if r.get('createdAt')]
print('pagina',len(rs),'met app',len(ok))
def m(r): return r['createdAt'][:7]
per=C.Counter(m(r) for r in ok)
print('nieuw per halfjaar:',sorted(C.Counter(m(r)[:4]+('a' if int(m(r)[5:])<=6 else 'b') for r in ok).items()))
print('per maand 2025-2026:',[(k,per[k]) for k in sorted(per) if k>='2025-01'])
dev=C.Counter(r['developer']['name'] for r in ok)
devfirst={}
for r in ok:
    d=r['developer']['name']; devfirst[d]=min(devfirst.get(d,'9'),r['createdAt'])
def stats(lst,naam):
    if not lst: print(naam,'0');return
    v=[r['rating']['count'] for r in lst]
    print(f"{naam}: n={len(v)} mediaan={st.median(v)} 0={sum(x==0 for x in v)} 10+={sum(x>=10 for x in v)} ({100*sum(x>=10 for x in v)/len(v):.0f}%) 30+={sum(x>=30 for x in v)} 100+={sum(x>=100 for x in v)} betaald_extern={sum(1 for r in lst if r['pricing'].get('hasExternalPurchases'))} betaald_nuvem={sum(1 for r in lst if r['pricing'].get('type') not in ('free',None))}")
for a,b,n in [('2024-01','2024-07','lichting 2024 H1'),('2024-07','2025-01','lichting 2024 H2'),('2025-01','2025-07','lichting 2025 H1'),('2025-07','2026-01','lichting 2025 H2'),('2026-01','2026-05','jan-apr 2026'),('2026-05','2026-09','mei-aug 2026'),('2026-09','2027','sep-nov 2026')]:
    lst=[r for r in ok if a<=r['createdAt']<b]
    stats(lst,n)
    nieuwm=[r for r in lst if devfirst[r['developer']['name']]>=a]
    stats(nieuwm,'   waarvan nieuwe makers')
print('top 10 nieuwe (mei 2025 t/m aug 2026) naar reviews:')
for r in sorted([r for r in ok if '2025-05'<=r['createdAt']<'2026-09'],key=lambda r:-r['rating']['count'])[:15]:
    print(' ',r['rating']['count'],r['createdAt'][:10],r['slug'],'|',r['developer']['name'],'| apps maker',dev[r['developer']['name']],'| maker sinds',devfirst[r['developer']['name']][:7],r['pricing'].get('type'),r['pricing'].get('price'),r['pricing'].get('currency'))
# reviews per maand in de hele winkel (alleen getoonde reviews, max per pagina)
rv=C.Counter()
for r in ok:
    for d,_,_ in r.get('revs') or []: rv[d[:7]]+=1
print('getoonde reviews per maand:',[(k,rv[k]) for k in sorted(rv) if k>='2026-01'])
print('getoond per app max',max(len(r.get('revs') or []) for r in ok))
print('valuta',C.Counter(r['pricing'].get('currency') for r in ok))
print('prijs-type',C.Counter(r['pricing'].get('type') for r in ok))
