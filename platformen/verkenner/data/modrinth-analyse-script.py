import json, sys, statistics as st, collections
d = json.load(open(sys.argv[1]))
pm = collections.Counter(x["date_created"][:7] for x in d)
print("per maand:", sorted(pm.items()))
def rapport(sel, naam):
    dl = sorted(x["downloads"] for x in sel)
    n = len(dl)
    if not n: return
    pct = lambda g: round(100*sum(v>=g for v in dl)/n,1)
    print(f"{naam}: n={n} mediaan={st.median(dl)} p25={dl[n//4]} p75={dl[3*n//4]} p90={dl[9*n//10]} 100+={pct(100)}% 1000+={pct(1000)}% 10000+={pct(10000)}%")
sel = [x for x in d if "2026-05-01" <= x["date_created"][:10] < "2026-09-01"]
rapport(sel, "mei-aug 2026 (3-6 mnd oud)")
for m in ["2026-05","2026-06","2026-07","2026-08","2026-09","2026-10"]:
    rapport([x for x in d if x["date_created"][:7]==m], m)
# top per maker met 1 project? auteurs met maar 1 project in de set
ac = collections.Counter(x["author"] for x in d)
rapport([x for x in sel if ac[x["author"]]==1], "mei-aug, makers met 1 project in set")
for x in sorted(sel, key=lambda x:-x["downloads"])[:10]: print(x["downloads"], x["title"], x["author"], x["date_created"][:10])
