# Winkelproducten (SKU's met prijs) van Activities met betaalvlag of winkel, aangemaakt vanaf een maand.
# Gebruik: python3 -I discord-activities-sku-script.py dir.json 2025-09 <uitvoer.json>
import json, sys, datetime, urllib.request, time
from concurrent.futures import ThreadPoolExecutor
d = json.load(open(sys.argv[1]))
def m(i): return datetime.datetime.fromtimestamp(((int(i)>>22)+1420070400000)/1000, datetime.UTC).strftime("%Y-%m")
w = [a for a in d if a["embedded"] and m(a["id"]) >= sys.argv[2] and (a["is_monetized"] or a["storefront"] or a["primary_sku"])]
def get(a):
    for t in range(3):
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request("https://discord.com/api/v9/store/published-listings/skus?application_id="+a["id"], headers={"User-Agent":"dortus-verkenner"}), timeout=30))
            return {"id":a["id"],"name":a["name"],"maand":m(a["id"]),"servers":a["guild_count"],
                    "skus":[{"naam":l["sku"]["name"],"type":l["sku"]["type"],"prijs":(l["sku"].get("price") or {}).get("amount")} for l in r]}
        except Exception: time.sleep(3)
    return {"id":a["id"],"name":a["name"],"fout":True}
with ThreadPoolExecutor(4) as ex: out = list(ex.map(get, w))
json.dump(out, open(sys.argv[3],"w"), indent=0)
ok=[o for o in out if not o.get("fout")]; met=[o for o in ok if o["skus"]]
print("Activities met betaalvlag/winkel vanaf", sys.argv[2], ":", len(w), "gelezen", len(ok), "met producten", len(met))
pr=sorted(s["prijs"] for o in met for s in o["skus"] if s["prijs"]); print("prijzen (cent):", len(pr), "mediaan", pr[len(pr)//2] if pr else None)
for o in sorted(met, key=lambda o:-(o["servers"] or 0))[:25]:
    print(f"  {o['servers']:>7} {o['maand']} {o['name'][:30]} | " + "; ".join(f"{s['naam'][:25]} {s['prijs']}" for s in o["skus"][:4]))
