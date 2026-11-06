# Haalt de winkelproducten (SKU's met prijs) uit Discords eigen winkel voor apps met betaalvlag, aangemaakt feb-aug 2026.
# Gebruik: python3 -I discord-sku-script.py dir.json <uitvoer.json>
import json, sys, datetime, urllib.request, time
from concurrent.futures import ThreadPoolExecutor
d = json.load(open(sys.argv[1]))
def m(i): return datetime.datetime.utcfromtimestamp(((int(i)>>22)+1420070400000)/1000).strftime("%Y-%m")
w = [a for a in d if "2026-02" <= m(a["id"]) <= "2026-08" and (a["is_monetized"] or a["primary_sku"])]
def get(a):
    for t in range(3):
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request("https://discord.com/api/v9/store/published-listings/skus?application_id="+a["id"], headers={"User-Agent":"dortus-verkenner"}), timeout=30))
            return {"id":a["id"],"name":a["name"],"maand":m(a["id"]),"servers":a["guild_count"],
                    "skus":[{"naam":l["sku"]["name"],"type":l["sku"]["type"],"prijs":(l["sku"].get("price") or {}).get("amount")} for l in r]}
        except Exception: time.sleep(3)
    return {"id":a["id"],"name":a["name"],"fout":True}
with ThreadPoolExecutor(5) as ex: out = list(ex.map(get, w))
json.dump(out, open(sys.argv[2],"w"), indent=0)
ok=[o for o in out if not o.get("fout")]; met=[o for o in ok if o["skus"]]
print("apps met betaalvlag feb-aug 2026:", len(w), "gelezen", len(ok), "met producten in Discord-winkel", len(met))
pr=sorted(s["prijs"] for o in met for s in o["skus"] if s["prijs"]); print("prijzen (cent) met bekende prijs:", len(pr), "mediaan", pr[len(pr)//2] if pr else None)
