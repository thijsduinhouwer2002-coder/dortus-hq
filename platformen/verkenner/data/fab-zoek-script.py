# Bladert de open zoek-API van Fab door (nieuwste eerst) voor een listingtype, tot een datum.
# Let op: de zoekresultaten hebben geen firstPublishedAt; die komt uit fab-haal-script.py.
# Gebruik: python3 -I fab-zoek-script.py <type> <tot JJJJ-MM-DD> <uitvoer.json>
import json, sys, time, urllib.request
typ, tot, uit = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://www.fab.com/i/listings/search?listing_types={typ}&sort_by=-createdAt&count=100"
alle = []
while url:
    for k in range(4):
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "dortus-verkenner"}), timeout=40).read()); break
        except Exception as e:
            time.sleep(5 * (k + 1)); d = None
    if not d: print("gestopt door fout"); break
    for r in d["results"]:
        rt = r.get("ratings") or {}
        alle.append({"uid": r.get("uid"), "titel": r.get("title"), "type": r.get("listingType"),
                     "laatst_gepubliceerd": r.get("publishedAt"),
                     "beoordelingen": rt.get("total"), "gemiddeld": rt.get("averageRating"), "gratis": r.get("isFree"),
                     "prijs": (r.get("startingPrice") or {}).get("price"),
                     "maker": (r.get("user") or {}).get("sellerName")})
    # publishedAt is de laatste update; stop als de mediaan van de pagina ouder is dan tot
    pd = sorted((r.get("publishedAt") or "")[:10] for r in d["results"])
    if not d["results"] or pd[len(pd)//2] < tot or len(alle) >= 6000: break
    url = d.get("next"); time.sleep(0.5)
json.dump(alle, open(uit, "w"))
print("klaar", len(alle), "oudste", alle[-1]["laatst_gepubliceerd"] if alle else None)
