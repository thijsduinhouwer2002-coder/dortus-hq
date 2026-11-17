import json,statistics as st,collections,re,sys
R=[json.loads(l) for l in open('/tmp/b/items.jsonl')]
R=[r for r in R if 'published_at' in r and r.get('published_at')]
print('totaal met data',len(R))
print(collections.Counter(r['cat'] for r in R).most_common(12))
def addon(r):
    n=(r['name'] or '').lower()
    return ('アドオン' in r['name'] or 'addon' in n or 'add-on' in n or 'プラグイン' in r['name'] or 'スクリプト' in r['name']) and r['cat'] not in ('3Dキャラクター','3D衣装','3D装飾品','3Dモーション・アニメーション','3D環境・ワールド','3D小道具')
A=[r for r in R if addon(r)]
print('addons',len(A),collections.Counter(r['cat'] for r in A).most_common(8))
def stats(L,lab):
    paid=[r for r in L if min([p for p in r['prices'] if p is not None] or [0])>0]
    lk=[r['likes'] for r in paid]
    if not lk: print(lab,'geen');return
    pr=[min(r['prices']) for r in paid]
    print(f"{lab}: n={len(L)} betaald={len(paid)} mediaan likes={st.median(lk)} 50+={sum(x>=50 for x in lk)/len(lk):.0%} 100+={sum(x>=100 for x in lk)/len(lk):.0%} 500+={sum(x>=500 for x in lk)/len(lk):.0%} mediaanprijs=¥{st.median(pr)} winkels={len({r['shop'] for r in paid})}")
    return paid
for a,b,lab in [('2025-01','2025-12','2025'),('2026-01','2026-04','jan-apr 2026'),('2026-05','2026-08','mei-aug 2026'),('2026-09','2026-11','sep-nov 2026')]:
    L=[r for r in A if a<=r['published_at'][:7]<=b]
    stats(L,lab)
print('per maand',sorted(collections.Counter(r['published_at'][:7] for r in A).items())[-14:])
W=[r for r in A if '2026-03'<=r['published_at'][:7]<='2026-08' and min(r['prices'] or [0])>0]
W.sort(key=lambda r:-r['likes'])
for r in W[:20]: print(r['likes'],min(r['prices']),r['published_at'][:10],r['shop'],r['name'][:70])
