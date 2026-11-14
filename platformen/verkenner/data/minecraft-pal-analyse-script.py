import json, sys, statistics as st
from datetime import datetime
from collections import defaultdict
rows=[json.loads(l) for l in open(sys.argv[1]) if '"fout"' not in l]
for r in rows:
    r["d"]=datetime.strptime(r["created"],"%B %d, %Y") if r.get("created") else None
rows=[r for r in rows if r["d"]]
print("totaal",len(rows))
# eerste item per maker in de steekproef is geen goede maat; per jaar
def q(xs,p): xs=sorted(xs); return xs[int(p*(len(xs)-1))] if xs else None
def blok(naam, rs):
    ns=[r["n"] for r in rs]
    if not ns: print(naam,0); return
    print(f"{naam}: n={len(rs)} mediaan={st.median(ns)} p75={q(ns,.75)} p90={q(ns,.9)} max={max(ns)} 0={sum(x==0 for x in ns)} 10+={sum(x>=10 for x in ns)/len(ns):.0%} 50+={sum(x>=50 for x in ns)/len(ns):.0%} 100+={sum(x>=100 for x in ns)/len(ns):.0%} 500+={sum(x>=500 for x in ns)/len(ns):.0%}")
for j in range(2017,2027): blok(str(j),[r for r in rows if r["d"].year==j])
coh=[r for r in rows if datetime(2026,2,1)<=r["d"]<datetime(2026,8,1)]
blok("cohort feb-jul 2026",coh)
blok("cohort 2025",[r for r in rows if r["d"].year==2025])
tp=defaultdict(list)
for r in [r for r in rows if r["d"]>=datetime(2025,1,1) and r["d"]<datetime(2026,8,1)]: tp[r["type"]].append(r)
for k,v in sorted(tp.items(),key=lambda x:-len(x[1])): blok("  type "+str(k),v)
pr=[int(r["prijs"]) for r in rows if r.get("prijs")]
print("prijs mediaan",st.median(pr), "gratis",sum(p==0 for p in pr))
