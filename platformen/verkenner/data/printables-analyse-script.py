import json,sys,statistics as st,collections as C
q=lambda a,f: a[int(f*(len(a)-1))] if a else None
def show(L,lab,key):
    v=sorted(r[key] or 0 for r in L)
    if not v: print(lab,"leeg"); return
    print(f"{lab}: n={len(v)} {key} mediaan {st.median(v)} p75 {q(v,.75)} p90 {q(v,.9)} max {v[-1]} | 0: {100*sum(x==0 for x in v)/len(v):.0f}% 1+: {100*sum(x>=1 for x in v)/len(v):.0f}% 5+: {100*sum(x>=5 for x in v)/len(v):.1f}% 10+: {100*sum(x>=10 for x in v)/len(v):.1f}% 100+: {100*sum(x>=100 for x in v)/len(v):.1f}%")
mode=sys.argv[1]
if mode=="vrij":
    R=[json.loads(l) for f in sys.argv[2:] for l in open(f)]
    R=[r for r in R if r.get("t")]
    print("met datum",len(R))
    V=[r for r in R if "2026-05"<=r["t"][:7]<="2026-08" and not r["price"] and not r["premium"]]
    show(V,"gratis mei-aug","dl")
    for m in ["05","06","07","08"]: show([r for r in V if r["t"][5:7]==m],"gratis 2026-"+m,"dl")
    show([r for r in V if r["ai"]],"gratis AI","dl")
    print("betaald in steekproef",sum(bool(r["price"]) for r in R),"club",sum(bool(r["premium"]) for r in R))
else:
    R=[json.loads(l) for l in open(sys.argv[2])]
    print("totaal betaald geoogst",len(R))
    m=C.Counter((r["firstPublish"] or "")[:7] for r in R); print(sorted(m.items())[-10:])
    V=[r for r in R if "2026-05"<=(r["firstPublish"] or "")[:7]<="2026-08"]
    show(V,"betaald mei-aug","ratingCount"); show(V,"betaald mei-aug","makesCount"); show(V,"betaald mei-aug","likesCount")
    for mm in ["05","06","07","08"]: show([r for r in V if r["firstPublish"][5:7]==mm],"betaald 2026-"+mm,"ratingCount")
    mk=C.Counter(r["user"]["id"] for r in V); print("makers",len(mk),"top",[(k,c) for k,c in mk.most_common(5)])
    pr=sorted(float(r["price"]) for r in V if r["price"]); print("prijs mediaan",st.median(pr) if pr else None)
    print("AI",sum(bool(r["aiGenerated"]) for r in V))
    top=sorted(V,key=lambda r:-(r["ratingCount"] or 0))[:8]
    for r in top: print(r["ratingCount"],r["makesCount"],r["likesCount"],r["price"],r["firstPublish"][:10],r["user"]["handle"],r["name"][:50])
