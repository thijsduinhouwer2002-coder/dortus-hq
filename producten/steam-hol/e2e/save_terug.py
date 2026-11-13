# Olaf 13 nov 2026, demolijst punt 4: zet de bewaartijd in hol.json een aantal seconden terug (of vooruit bij een negatief getal; 0 = alleen lezen),
# zodat de volgende start doet alsof je zo lang weg was. Gebruik: python save_terug.py <pad naar hol.json> <seconden>
# Schrijft daarna regel "tijd=<unix> goud=<n> gangen=<n> vallen=<json> boven=<json> upgrades=<json>" zodat de stap kan vergelijken.
import json, sys
pad, sec = sys.argv[1], int(sys.argv[2])
with open(pad, encoding="utf-8") as f:
    d = json.load(f)
d["tijd"] = float(d["tijd"]) - sec
with open(pad, "w", encoding="utf-8") as f:
    json.dump(d, f)
print("tijd=%d goud=%d gangen=%d vallen=%s boven=%s upgrades=%s" % (int(d["tijd"]), int(d.get("goud", 0)), sum(1 for g in d.get("gang", []) if g),
      json.dumps(d.get("vallen", []), separators=(",", ":")), json.dumps(d.get("boven", []), separators=(",", ":")),
      json.dumps(d.get("upgrades", {}), sort_keys=True)))
