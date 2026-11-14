# Analyse van de productpagina's: verkopen per soort (select of labs/marketplace) en per startmaand.
# Gebruik: python3 -I appsumo-analyse-script.py pagina.jsonl
import json, sys, statistics as st, collections
rows = [json.loads(l) for l in open(sys.argv[1])]
rows = [r for r in rows if "fout" not in r and not r.get("gratis") and not r.get("addon")]
print("pagina's", len(rows), "fouten", sum(1 for l in open(sys.argv[1]) if '"fout"' in l))
def blok(naam, rr):
    if not rr: return
    v = sorted((r["verkocht"] or 0) for r in rr)
    omzet = sorted((r["verkocht"] or 0) * (r["prijs"] or 0) for r in rr)
    n = len(v)
    pct = lambda f: round(100 * sum(1 for x in v if f(x)) / n)
    print(f"{naam}: n={n} mediaan verkocht {st.median(v)}, gem {round(sum(v)/n)}, 0 verkocht {pct(lambda x:x==0)}%, 10+ {pct(lambda x:x>=10)}%, 100+ {pct(lambda x:x>=100)}%, 1000+ {pct(lambda x:x>=1000)}%, max {v[-1]}")
    print(f"   bruto (verkocht x laagste prijs): mediaan ${st.median(omzet):,.0f}, {round(100*sum(1 for x in omzet if x>=1800)/n)}% boven $1.800 (= ±$300/mnd over een half jaar), {round(100*sum(1 for x in omzet if x>=10000)/n)}% boven $10.000; reviews mediaan {st.median([r['reviews'] or 0 for r in rr])}")
soort = collections.defaultdict(list)
for r in rows: soort[r["soort"]].append(r)
for s, rr in soort.items(): blok(f"soort {s}", rr)
maand = collections.defaultdict(list)
for r in rows: maand[(r["start"] or "")[:7], r["soort"]].append(r)
for k in sorted(maand): blok(f"{k[0]} {k[1]}", maand[k])
top = sorted(rows, key=lambda r: -(r["verkocht"] or 0))[:12]
for r in top: print("  top:", r["naam"], r["soort"], r["verkocht"], "x $", r["prijs"], r["start"][:10], "reviews", r["reviews"])
