# Leest productdata van Fab via de open JSON https://www.fab.com/i/listings/<uid> (geen sleutel).
# Gebruik: python3 -I fab-haal-script.py <urls.txt> <uitvoer.json>
import json, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
def lees(u):
    uid = u.rstrip("/").rsplit("/", 1)[1]
    err = ""
    for k in range(3):
        try:
            req = urllib.request.Request("https://www.fab.com/i/listings/" + uid, headers={"User-Agent": "dortus-verkenner"})
            d = json.loads(urllib.request.urlopen(req, timeout=40).read())
            r = d.get("ratings") or {}
            sp = d.get("startingPrice") or {}
            us = d.get("user") or {}
            return {"uid": uid, "titel": d.get("title"), "type": d.get("listingType"),
                    "eerst": d.get("firstPublishedAt"), "beoordelingen": sum(r.get(f"rating{i}", 0) or 0 for i in range(1, 6)),
                    "reviews": d.get("reviewCount"), "gemiddeld": d.get("averageRating"),
                    "prijs": sp.get("price"), "formaten": [a["assetFormatType"]["code"] for a in d.get("assetFormats") or []],
                    "maker": us.get("sellerName") or us.get("profileUrl") or us.get("uid"), "categorie": (d.get("category") or {}).get("path")}
        except Exception as e:
            err = str(e); time.sleep(3)
    return {"uid": uid, "fout": err}
with ThreadPoolExecutor(8) as ex:
    out = list(ex.map(lees, urls))
json.dump(out, open(sys.argv[2], "w"))
print("klaar", len(out), "fouten", sum(1 for o in out if o.get("fout")))
