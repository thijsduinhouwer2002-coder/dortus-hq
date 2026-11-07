# Analyse van polymart-haal-script uitvoer. Gebruik: python3 polymart-analyse-script.py recent.jsonl
import sys, json, statistics as st, datetime as dt, collections
rijen = [json.loads(l) for l in open(sys.argv[1])]
ok = [r for r in rijen if "fout" not in r]
print("totaal", len(rijen), "leesbaar", len(ok), "fouten", collections.Counter(r["fout"][:40] for r in rijen if "fout" in r).most_common(4))
def maand(r): return dt.datetime.utcfromtimestamp(r["gemaakt"]).strftime("%Y-%m")
per = collections.Counter(maand(r) for r in ok)
print("nieuw per maand (alle):", sorted(per.items()))
print("betaald per maand:", sorted(collections.Counter(maand(r) for r in ok if r["prijs"] > 0).items()))
def toon(naam, groep):
    if not groep: print(naam, "leeg"); return
    d = sorted(r["downloads"] or 0 for r in groep)
    n = len(d)
    omzet = sorted((r["downloads"] or 0) * r["prijs"] for r in groep)
    print(f"{naam}: n={n} mediaan {st.median(d)} | 1+ {sum(x>=1 for x in d)/n:.0%} | 10+ {sum(x>=10 for x in d)/n:.0%} | 50+ {sum(x>=50 for x in d)/n:.0%} | 100+ {sum(x>=100 for x in d)/n:.0%} | mediaanprijs {st.median(r['prijs'] for r in groep):.2f} | omzet bruto mediaan ${st.median(omzet):.0f}, p90 ${omzet[int(n*0.9)]:.0f}, max ${omzet[-1]:.0f}, som ${sum(omzet):.0f}")
mei_aug = [r for r in ok if "2026-05" <= maand(r) <= "2026-08"]
toon("betaald mei-aug 2026", [r for r in mei_aug if r["prijs"] > 0])
toon("gratis mei-aug 2026", [r for r in mei_aug if r["prijs"] == 0])
nov_apr = [r for r in ok if "2025-11" <= maand(r) <= "2026-04"]
toon("betaald nov 2025-apr 2026", [r for r in nov_apr if r["prijs"] > 0])
toon("gratis nov 2025-apr 2026", [r for r in nov_apr if r["prijs"] == 0])
print("top 12 betaald op bruto omzet (nov 2025 tot aug 2026):")
for r in sorted([r for r in ok if r["prijs"] > 0 and "2025-11" <= maand(r) <= "2026-08"], key=lambda r: -(r["downloads"] or 0) * r["prijs"])[:12]:
    print(" ", r["id"], maand(r), r["titel"][:40], r["prijs"], r["munt"], r["downloads"], "eigenaar", r["owner_id"], "reviews", r["reviews"])
