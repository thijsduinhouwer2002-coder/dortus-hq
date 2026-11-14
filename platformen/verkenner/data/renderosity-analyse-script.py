# Analyse van Renderosity best-selling (jsonl van ren-browse.py). Rang = plek in de lijst "Best Selling" (recent venster).
import sys, json, statistics as st, collections as C
rows = [json.loads(l) for l in open(sys.argv[1])]
seen=set(); r=[]
for x in rows:
    if x['item_id'] in seen: continue
    seen.add(x['item_id']); r.append(x)
print('producten', len(r))
# rang in blokken: mediane id en aandeel nieuw (id >= 171000 ~ mrt 2026)
for a,b in [(1,120),(121,500),(501,1000),(1001,2000),(2001,4000),(4001,8000),(8001,16000),(16001,30000),(30001,50000)]:
    s=[x for x in r if a<=x['rang']<=b]
    if not s: continue
    ids=[x['item_id'] for x in s]
    print(f'rang {a}-{b}: n={len(s)} mediane id {int(st.median(ids))}, id>=171000 {sum(i>=171000 for i in ids)/len(s):.0%}, top-icoon {sum(x["top"] for x in s)/len(s):.0%}')
# eerste product per maker
first=C.defaultdict(lambda:10**9); cnt=C.Counter()
for x in r:
    first[x['item_brand']]=min(first[x['item_brand']],x['item_id']); cnt[x['item_brand']]+=1
print('makers', len(first))
cuts={'2025+ (id>=167000)':167000,'sinds aug 2025 (id>=169000)':169000,'2026 (id>=170500)':170500}
for naam,c in cuts.items():
    nieuw={m for m,f in first.items() if f>=c}
    print(naam,'nieuwe makers',len(nieuw))
    for N in (120,500,1000,2000):
        s=[x for x in r if x['rang']<=N]
        print(f'   top {N}: aandeel producten van nieuwe makers {sum(x["item_brand"] in nieuw for x in s)/len(s):.1%}, unieke nieuwe makers {len({x["item_brand"] for x in s if x["item_brand"] in nieuw})}')
# producten mei t/m aug 2026 (id ~171700-172900): rangverdeling, nieuwe vs gevestigde makers
lich=[x for x in r if 171700<=x['item_id']<=172900]
oud=set(m for m,f in first.items() if f<167000)
for naam,s in [('alle',lich),('makers gestart 2025+',[x for x in lich if first[x['item_brand']]>=167000]),('gevestigd',[x for x in lich if x['item_brand'] in oud])]:
    if not s: continue
    rk=sorted(x['rang'] for x in s)
    print(f'lichting mei-aug 2026 {naam}: n={len(s)} mediane rang {int(st.median(rk))}, in top 1000 {sum(k<=1000 for k in rk)/len(rk):.0%}, in top 2000 {sum(k<=2000 for k in rk)/len(rk):.0%}')
# top makers top 1000
tm=C.Counter(x['item_brand'] for x in r if x['rang']<=1000)
print('top 1000 per maker', tm.most_common(12))
print('prijs mediaan', st.median(x['price'] for x in r))
blend=[x for x in r if 'blend' in x['item_name'].lower()]
print('naam met blender', len(blend), 'beste rang', sorted(x['rang'] for x in blend)[:10])
# makers met het icoon Top-Selling Vendor (staat op elk product van die maker)
topm={x['item_brand'] for x in r if x['top']}
print('makers met Top-Selling-icoon', len(topm), 'van', len(first))
for naam,c in cuts.items():
    nieuw={m for m,f in first.items() if f>=c}
    t=sorted(nieuw&topm)
    print(f'  {naam}: {len(t)} van {len(nieuw)} nieuwe makers hebben het icoon: {t}')
    print('     producten per nieuwe maker mediaan', st.median([cnt[m] for m in nieuw]) if nieuw else None)
