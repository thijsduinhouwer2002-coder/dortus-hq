import json,collections,statistics as st,datetime as dt
R=[json.loads(l) for l in open('/tmp/zd/lic_items.jsonl')]
R=[r for r in R if r['up'] and r['dl']]
print('n',len(R), collections.Counter(r['pay'] for r in R))
ym=lambda r: dt.datetime.fromtimestamp(int(r['up'])/1000,dt.UTC).strftime('%Y-%m')
print(sorted(collections.Counter(ym(r)[:4] for r in R).items()))
for lo,hi in [('2024-01','2024-12'),('2025-01','2025-06'),('2025-07','2025-12'),('2026-01','2026-04'),('2026-05','2026-08'),('2026-09','2026-11')]:
  for p in ['VIDEO','ZEDGE_TOKENS']:
    s=[int(r['dl']) for r in R if lo<=ym(r)<=hi and r['pay']==p]
    if s: print(lo,hi,p,len(s),'med',st.median(s),'100+',round(100*sum(x>=100 for x in s)/len(s)),'% 1000+',round(100*sum(x>=1000 for x in s)/len(s)),'% max',max(s))
tok=[r for r in R if r['pay']=='ZEDGE_TOKENS']
print('tokens prijzen',collections.Counter(r['price'] for r in tok).most_common(8))
for r in sorted(tok,key=lambda r:-int(r['dl']))[:8]: print(ym(r),r['dl'],r['price'],r['prof'],r['kw'][-30:])
print('makers',len(set(r['prof'] for r in R)))
s26=[r for r in R if ym(r)>='2026-01' and ym(r)<='2026-08']
print('2026 jan-aug',len(s26),'med',st.median([int(r['dl']) for r in s26]) if s26 else None)
