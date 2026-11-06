# Analyse Discord-steekproef. Gebruik: python3 -I discord-analyse-script.py dir.json [dbl.json]
import json, sys, datetime, statistics as st
from collections import Counter
def made(i):
    return datetime.datetime.utcfromtimestamp(((int(i) >> 22) + 1420070400000)/1000)
def q(v, p):
    v = sorted(v); return v[min(len(v)-1, int(p*len(v)))] if v else None
d = json.load(open(sys.argv[1]))
print("Directory: unieke apps", len(d))
for a in d: a["m"] = made(a["id"]).strftime("%Y-%m")
print("monetized totaal", sum(1 for a in d if a["is_monetized"]), "met primary_sku", sum(1 for a in d if a["primary_sku"]))
per = Counter(a["m"][:4] for a in d); print("per jaar aangemaakt", sorted(per.items()))
print("maand | n | mediaan servers | p25 | p75 | %>=1000 | %monetized | %sku")
for m in sorted({a["m"] for a in d if a["m"] >= "2025-07"}):
    g = [a for a in d if a["m"] == m]; s = [a["guild_count"] or 0 for a in g]
    print(m, len(g), st.median(s), q(s,.25), q(s,.75), round(100*sum(x>=1000 for x in s)/len(s)),
          round(100*sum(bool(a["is_monetized"]) for a in g)/len(g)), round(100*sum(bool(a["primary_sku"]) for a in g)/len(g)))
w = [a for a in d if "2026-02" <= a["m"] <= "2026-08"]; s=[a["guild_count"] or 0 for a in w]
print("feb-aug 2026: n", len(w), "mediaan", st.median(s), "min", min(s), "%<100", round(100*sum(x<100 for x in s)/len(s)), "%>=1000", round(100*sum(x>=1000 for x in s)/len(s)), "%>=10000", round(100*sum(x>=10000 for x in s)/len(s)))
ms = [a for a in w if a["is_monetized"] or a["primary_sku"]]
print("feb-aug 2026 betaald:", len(ms), "mediaan servers", st.median([a["guild_count"] or 0 for a in ms]) if ms else None)
for a in sorted(ms, key=lambda a: -(a["guild_count"] or 0))[:15]: print("  ", a["m"], a["guild_count"], a["name"], a["categories"])
if len(sys.argv) > 2:
    b = [x for x in json.load(open(sys.argv[2])) if x.get("created_at")]
    ids = {a["id"]: a for a in d}
    print("\nDBL: bots met gegevens", len(b), "fouten", sum(1 for x in json.load(open(sys.argv[2])) if x.get("fout")))
    for x in b: x["l"] = datetime.datetime.utcfromtimestamp(x["created_at"]/1000).strftime("%Y-%m")
    print("per jaar op lijst gezet", sorted(Counter(x["l"][:4] for x in b).items()))
    print("maand | n | %in directory | %met serverstat | mediaan servers (stat) ")
    for m in sorted({x["l"] for x in b if x["l"] >= "2025-07"}):
        g = [x for x in b if x["l"] == m]; s=[x["guilds"] for x in g if x["guilds"]]
        print(m, len(g), round(100*sum(x["id"] in ids for x in g)/len(g)), round(100*len(s)/len(g)), st.median(s) if s else None)
    w = [x for x in b if "2026-02" <= x["l"] <= "2026-08"]
    if w:
        ind = [x for x in w if x["id"] in ids]; s=[x["guilds"] for x in w if x["guilds"]]
        print("feb-aug 2026 op DBL:", len(w), "in directory", len(ind), f"({round(100*len(ind)/len(w))}%)", "met serverstat", len(s), "mediaan", st.median(s) if s else None, "%>=100 van die met stat", round(100*sum(v>=100 for v in s)/len(s)) if s else None)
        print("  directory-servers van die in directory:", sorted(ids[x["id"]]["guild_count"] or 0 for x in ind))
