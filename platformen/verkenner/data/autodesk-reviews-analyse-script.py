# Gebruik: python3 -I autodesk-reviews-analyse-script.py (in deze map; reviews per app, ontdubbeld, per leeftijd en makergrootte)
import json,statistics as st,collections as C
R=json.load(open('autodesk-ratings-2026-11-09.json'))
A=[json.loads(l) for l in open('autodesk-apps-2026-11-07.jsonl')]
def betaald(a):
    return any(p['type'] in('ONE_TIME','SUBSCRIPTION_MONTHLY','SUBSCRIPTION_ANNUAL') or any(float(b[0] or 0)>0 for b in p['bedragen']) for p in a.get('prijzen',[]))
def prijs(a):
    o=[]
    for p in a.get('prijzen',[]):
        for b in p['bedragen']:
            if b[1]=='USD' and float(b[0] or 0)>0: o.append((p['type'],float(b[0])))
    return o
for a in A:
    a['id']=a['url'].split('/')[-1]; r=R[a['id']]; a['n']=r['totalRatings']; a['avg']=r['averageRating']; a['b']=betaald(a); a['e']=(a.get('eerste') or '')
# ontdubbelen: zelfde maker + zelfde n + avg (n>0) of zelfde legacy
seen=set(); D=[]
for a in sorted(A,key=lambda a:a['e']):
    k=(a.get('maker'),a['n'],a['avg']) if a['n']>=3 else ('L',a.get('legacy'),a['id'])
    if k in seen: continue
    seen.add(k); D.append(a)
print('na ontdubbelen',len(D),'reviews',sum(a['n'] for a in D))
mk=C.Counter(a.get('maker') for a in D)
klein=lambda a: mk[a.get('maker')]<=3
print('makers',len(mk),'kleine makers (<=3 apps)',sum(1 for m,v in mk.items() if v<=3))
P=[a for a in D if a['b']]
print('betaald',len(P),'reviews op betaalde',sum(a['n'] for a in P))
print('\nTop 30 betaalde apps op reviews:')
for a in sorted(P,key=lambda a:-a['n'])[:30]: print(a['n'],a['avg'],a.get('maker'),'apps:',mk[a.get('maker')],a['e'][:10],a.get('producten',[])[:2],prijs(a)[:2])
def rij(naam,S):
    n=[a['n'] for a in S]
    if not S: print(naam,0);return
    print(f"{naam}: n={len(S)} mediaan={st.median(n)} 1+={sum(x>=1 for x in n)/len(S):.0%} 5+={sum(x>=5 for x in n)/len(S):.0%} 10+={sum(x>=10 for x in n)/len(S):.0%} 20+={sum(x>=20 for x in n)/len(S)}")
for lo,hi,nm in [('2025-05-09','2025-11-09','12-18m'),('2025-11-09','2026-05-09','6-12m'),('2026-05-09','2026-08-09','3-6m')]:
    S=[a for a in D if lo<=a['e']<hi]
    rij(nm+' betaald klein',[a for a in S if a['b'] and klein(a)]); rij(nm+' betaald groot',[a for a in S if a['b'] and not klein(a)]); rij(nm+' gratis/proef',[a for a in S if not a['b']])
print('\nbetaalde apps van kleine makers sinds 2024 met 5+ reviews:')
for a in sorted([a for a in P if klein(a) and a['e']>='2024' and a['n']>=5],key=lambda a:-a['n']): print(a['n'],a['avg'],a.get('maker'),a['e'][:10],a.get('producten',[])[:2],prijs(a)[:2],a['url'])
