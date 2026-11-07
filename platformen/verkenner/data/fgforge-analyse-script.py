# Gebruik: python3 fgforge-analyse-script.py fgforge-items-<datum>.json
import json, sys, statistics as st, collections, datetime as dt
d = json.load(open(sys.argv[1]))["data"]
EXT = "16"  # product_type_id van Extension
for p in d: p["sub"] = int(p["subcount"] or 0); p["pr"] = float(p["price"] or 0) / 100; p["m"] = p["created_at"][:7]
def rapport(s, label):
    v = sorted(p["sub"] for p in s); n = len(v)
    if not n: return
    print(f"{label}: n={n} mediaan={st.median(v)} p75={v[int(n*.75)]} p90={v[int(n*.9)]} 10+={sum(i>=10 for i in v)/n:.0%} 100+={sum(i>=100 for i in v)/n:.0%}")
w = [p for p in d if "2026-05" <= p["m"] <= "2026-08" and p["product_type_id"] == EXT]
rapport([p for p in w if p["pr"] == 0], "extensies gratis mei-aug 2026")
rapport([p for p in w if p["pr"] > 0], "extensies betaald mei-aug 2026")
print("mediaanprijs betaald", st.median([p["pr"] for p in w if p["pr"] > 0]))
by = collections.defaultdict(list)
for p in d: by[p["crafter"]].append(p)
rows = []
for c, ps in by.items():
    eerste = min(p["created_at"] for p in ps)[:10]
    betaald = [p for p in ps if p["pr"] > 0 and p["product_type_id"] == EXT]
    if betaald: rows.append((sum(p["sub"] * p["pr"] for p in betaald), c, eerste, len(betaald)))
rows.sort(reverse=True)
print("makers met betaalde extensies:", len(rows), "waarvan eerste item sinds 2025:", sum(r[2] >= "2025-01-01" for r in rows))
for r in [r for r in rows if r[2] >= "2025-01-01"][:10]:
    mnd = (dt.date(2026, 11, 7) - dt.date.fromisoformat(r[2])).days / 30.4
    print(f"  {r[1]}: bruto ${r[0]:.0f}, ±${r[0]/mnd:.0f} per maand, sinds {r[2]}, {r[3]} betaalde extensies")
