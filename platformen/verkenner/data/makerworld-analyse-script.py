import json,sys,statistics as st,collections as C
rows=[json.loads(l) for l in open(sys.argv[1])]
ok=[r for r in rows if "err" not in r]; pub=[r for r in ok if r.get("uid") and r.get("status")==1]
print("totaal",len(rows),"fout",len(rows)-len(ok),"gepubliceerd met maker",len(pub),"zonder maker/status",len(ok)-len(pub))
def s(L,lab):
    if not L: return
    d=sorted(r["dl"] for r in L); p=sorted(r["pr"] for r in L)
    q=lambda a,f: a[int(f*(len(a)-1))]
    print(f"{lab}: n={len(L)} dl mediaan {st.median(d)} p75 {q(d,.75)} p90 {q(d,.9)} p99 {q(d,.99)} max {d[-1]} | 100+ {100*sum(x>=100 for x in d)/len(d):.1f}% 1000+ {100*sum(x>=1000 for x in d)/len(d):.1f}% 0 {100*sum(x==0 for x in d)/len(d):.1f}% | prints mediaan {st.median(p)} 100+prints {100*sum(x>=100 for x in p)/len(p):.1f}%")
s(pub,"alle")
for m in ["2026-05","2026-06","2026-07","2026-08"]: s([r for r in pub if r["t"].startswith(m)],m)
s([r for r in pub if r["excl"]],"exclusive")
s([r for r in pub if not r["excl"]],"niet-excl")
s([r for r in pub if r["aigc"] or "Generative 3D Model" in r["cats"]],"AI/generatief")
s([r for r in pub if r["makerlab"]],"makerlab")
s([r for r in pub if (r["cust"] or 0)>0],"cust>0")
s([r for r in pub if r["official"]],"officieel")
print("paid",sum(bool(r["paid"]) for r in pub),"crowd",sum(bool(r["crowd"]) for r in pub),"redeem",sum(bool(r["redeem"]) for r in pub),"boost>0",sum((r["boost"] or 0)>0 for r in pub),"staff",sum(bool(r["staff"]) for r in pub))
b=sorted((r["boost"] or 0) for r in pub); print("boost p90",b[int(.9*(len(b)-1))],"max",b[-1])
cat=C.Counter(c for r in pub for c in r["cats"][:1]); print(cat.most_common(15))
mk=C.Counter(r["uid"] for r in pub); print("makers",len(mk),"top maker aandelen",mk.most_common(5))
print("aandeel van downloads top 1%:", sum(sorted((r['dl'] for r in pub),reverse=True)[:max(1,len(pub)//100)])/max(1,sum(r['dl'] for r in pub)))
