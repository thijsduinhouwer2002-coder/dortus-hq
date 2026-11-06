# Analyse Unity-steekproef (tools). Gebruik: python3 -I unity-analyse-script.py tools.json
import json, sys, statistics as st
from collections import Counter
d = [o for o in json.load(open(sys.argv[1])) if not o.get("fout") and o.get("eerst")]
print("gelezen", len(d))
for o in d: o["m"]=o["eerst"][:7]; o["r"]=int(o["reviews"] or 0); o["p"]=float(o["prijs"] or 0)
print("per maand eerste publicatie (2025-2026):", sorted((k,v) for k,v in Counter(o["m"] for o in d).items() if k>="2025-01"))
def blok(g, lab):
    if not g: return
    r=[o["r"] for o in g]
    print(f"{lab}: n {len(g)}, mediaan reviews {st.median(r)}, % met 1+ {round(100*sum(x>=1 for x in r)/len(r))}, % 5+ {round(100*sum(x>=5 for x in r)/len(r))}, % 10+ {round(100*sum(x>=10 for x in r)/len(r))}, max {max(r)}")
for lo,hi,lab in [("2026-05","2026-08","mei-aug 2026"),("2026-02","2026-04","feb-apr 2026"),("2025-01","2025-06","jan-jun 2025")]:
    g=[o for o in d if lo<=o["m"]<=hi]; blok(g, lab+" alles"); blok([o for o in g if o["p"]>0], lab+" betaald")
b=[o for o in d if "2026-05"<=o["m"]<="2026-08" and o["p"]>0]
if b: print("prijsmediaan betaald mei-aug 2026", st.median(o["p"] for o in b))
print("top nieuwe betaalde (feb-aug 2026):")
for o in sorted([o for o in d if "2026-02"<=o["m"]<="2026-08" and o["p"]>0], key=lambda o:-o["r"])[:10]: print("  ", o["m"], o["r"], o["p"], o["uitgevernaam"], o["url"].rsplit("/",1)[1])
