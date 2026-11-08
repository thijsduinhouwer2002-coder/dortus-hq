#!/usr/bin/env python3
"""Meet de Command Palette Extension Gallery (PowerToys).
Haalt extensions.json uit microsoft/CmdPal-Extensions en per Store-extensie
prijs, beoordelingen en releasedatum uit de openbare Store-API.
Gebruik: python3 cmdpal-meet.py [uitvoer.json]"""
import json, sys, urllib.request, time, collections
G = "https://raw.githubusercontent.com/microsoft/CmdPal-Extensions/main/extensions.json"
S = "https://storeedgefd.dsx.mp.microsoft.com/v9.0/products/{}?market=US&locale=en-us&deviceFamily=Windows.Desktop"
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "dortus-meet"}), timeout=30) as r:
        return json.load(r)
g = get(G); rows = []
for x in g["extensions"]:
    r = {"id": x["id"], "titel": x["title"], "toegevoegd": x["addedAt"], "cat": x["categories"],
         "bronnen": [s["type"] for s in x["installSources"]]}
    st = [s["id"] for s in x["installSources"] if s["type"] == "msstore"]
    if st:
        try:
            p = get(S.format(st[0]))["Payload"]
            pr = p.get("ProductRatings") or [{}]
            r.update(prijs=p.get("Price"), toon=p.get("DisplayPrice"),
                     sterren=p.get("AverageRating"), beoordelingen=p.get("RatingCount"),
                     release=(p.get("ReleaseDateUtc") or "")[:10],
                     iap=any("InAppOffer" in json.dumps(s) or s.get("SkuType") not in ("full", None) for s in p.get("Skus", [])))
        except Exception as e:
            r["fout"] = str(e)[:80]
        time.sleep(0.5)
    rows.append(r)
uit = sys.argv[1] if len(sys.argv) > 1 else "cmdpal-%s.json" % time.strftime("%Y-%m-%d")
json.dump({"gemeten": time.strftime("%Y-%m-%d"), "generatedAt": g["generatedAt"], "rijen": rows}, open(uit, "w"), indent=1)
print("extensies", len(rows), "per maand", sorted(collections.Counter(r["toegevoegd"][:7] for r in rows).items()))
betaald = [r for r in rows if (r.get("prijs") or 0) > 0]
print("betaald", len(betaald), [(r["titel"], r["toon"]) for r in betaald])
top = sorted([r for r in rows if r.get("beoordelingen")], key=lambda r: -r["beoordelingen"])
for r in top[:15]: print(r["beoordelingen"], r["sterren"], r["titel"], r.get("release"))
print("som beoordelingen", sum(r.get("beoordelingen") or 0 for r in rows))
