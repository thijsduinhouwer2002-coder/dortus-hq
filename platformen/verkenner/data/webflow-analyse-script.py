# Vera, 7 nov 2026. Telt de kaartjes uit webflow-haal-script.py per goedkeuringsmaand.
# Gebruik: python3 -I webflow-analyse-script.py wf.jsonl
import sys, json, statistics
from datetime import datetime
from collections import defaultdict

t = {}
for l in open(sys.argv[1]):
    for k in json.loads(l)["kaarten"]:
        slug = (k.get("templateLink") or {}).get("href", "")
        if slug:
            t[slug] = k
print("unieke templates gezien:", len(t))

def maand(k):
    try:
        return datetime.strptime(k["approvalDate"], "%B %d, %Y").strftime("%Y-%m")
    except Exception:
        return "?"

groep = defaultdict(list)
for k in t.values():
    groep[maand(k)].append(k)

def num(x):
    try:
        return int(str(x).replace(",", ""))
    except Exception:
        return None

print("maand | aantal | betaald | met aankoopcijfer | mediaan aankopen | % 10+ | % 50+ | max | mediaan prijs")
for m in sorted(groep):
    ks = groep[m]
    bet = [k for k in ks if not k.get("isFree") and num(k.get("priceNumeric"))]
    p = [num(k["cumulativePurchases"]) for k in bet if num(k.get("cumulativePurchases")) is not None]
    pr = [num(k["priceNumeric"]) for k in bet]
    if not p:
        print(m, len(ks), len(bet), 0)
        continue
    print(m, len(ks), len(bet), len(p), statistics.median(p),
          round(100 * sum(x >= 10 for x in p) / len(p)), round(100 * sum(x >= 50 for x in p) / len(p)),
          max(p), statistics.median(pr) if pr else "-")
