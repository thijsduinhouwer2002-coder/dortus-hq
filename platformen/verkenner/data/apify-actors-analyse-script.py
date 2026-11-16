import json,glob,collections,statistics as st
maker=collections.Counter(l.split('~')[0] for l in open('actors.txt').read().split())
rows=[]
for f in glob.glob('det/*.json'):
    try: d=json.load(open(f)).get('data')
    except: continue
    if not d: continue
    s=d.get('stats',{}); pi=d.get('pricingInfos') or [{}]
    rows.append(dict(u=d['username'],n=d['name'],c=d['createdAt'][:7],tu=s.get('totalUsers',0),u30=s.get('totalUsers30Days',0),
      rev=s.get('actorReviewCount',0),pm=(pi[-1] or {}).get('pricingModel','FREE'),dep=d.get('isDeprecated'),mk=maker[d['username']]))
print('n',len(rows))
by=collections.defaultdict(list)
for r in rows: by[r['c']].append(r)
def med(x): return st.median(x) if x else None
print('maand n medTotaal med30 %tot100+ %30d100+ %30d10+ %30d0 %betaald')
for m in sorted(by):
    if m<'2024-01': continue
    L=by[m]; t=[r['tu'] for r in L]; u=[r['u30'] for r in L]
    print(m,len(L),med(t),med(u),round(100*sum(x>=100 for x in t)/len(L)),round(100*sum(x>=100 for x in u)/len(L),1),round(100*sum(x>=10 for x in u)/len(L)),round(100*sum(x==0 for x in u)/len(L)),round(100*sum(r['pm']!='FREE' for r in L)/len(L)))
co=[r for r in rows if '2026-05'<=r['c']<='2026-08']
print('cohort mei-aug',len(co),'med tot',med([r['tu'] for r in co]),'med30',med([r['u30'] for r in co]),'100+ tot',sum(r['tu']>=100 for r in co),'100+ 30d',sum(r['u30']>=100 for r in co))
small=[r for r in co if r['mk']<=5]; big=[r for r in co if r['mk']>=50]
for nm,L in (('makers<=5 actors',small),('makers 50+',big)):
    print(nm,len(L),'med tot',med([r['tu'] for r in L]),'%100+tot',round(100*sum(r['tu']>=100 for r in L)/max(1,len(L))),'%30d 10+',round(100*sum(r['u30']>=10 for r in L)/max(1,len(L))))
json.dump(rows,open('det_rows.json','w'))
