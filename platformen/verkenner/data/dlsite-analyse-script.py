# Analyse DLsite (alle leeftijden): verkopen (dl_count) van nieuwe betaalde werken per soort. Gebruik: python3 dlsite-analyse-script.py dlsite-mrt-aug.jsonl
import json,sys,collections,statistics as st
rs={}
for l in open(sys.argv[1]):
    r=json.loads(l); rs[r['id']]=r
rs=list(rs.values())
def s(g,label):
    pc=[r['dl_count'] or 0 for r in g]
    if not pc: return
    p=lambda k:round(100*sum(x>=k for x in pc)/len(pc),1)
    print(f"{label}: n={len(pc)} mediaan={st.median(pc)} 0={100-p(1)}% 10+={p(10)}% 100+={p(100)}% 1000+={p(1000)}% makers={len({r['maker_id'] for r in g})} mediaanprijs={st.median([r['price'] for r in g])}")
paid=[r for r in rs if not r['is_free'] and (r['price'] or 0)>0]
print("totaal",len(rs),"betaald",len(paid))
for m in ['2026-03','2026-04','2026-05','2026-06','2026-07','2026-08']:
    s([r for r in paid if r['regist_date'].startswith(m)],m)
coh=[r for r in paid if r['regist_date'][:7] in ('2026-05','2026-06','2026-07','2026-08')]
s(coh,"cohort mei-aug betaald")
for t,_ in collections.Counter(r['work_type'] for r in coh).most_common(14):
    s([r for r in coh if r['work_type']==t],"  soort "+t)
mk=collections.Counter(r['maker_id'] for r in rs)
s([r for r in coh if mk[r['maker_id']]==1],"cohort, maker met maar 1 werk in mrt-aug")
# netto schatting: verkopen x prijs x ~0,6
om=collections.defaultdict(int)
for r in coh: om[r['maker_id']]+=(r['dl_count'] or 0)*r['price']
v=sorted(om.values(),reverse=True)
print("bruto yen per maker (cohort):","mediaan",st.median(v),"p75",v[len(v)//4],"top5",v[:5],"makers",len(v),">=50.000 yen:",sum(x>=50000 for x in v))
