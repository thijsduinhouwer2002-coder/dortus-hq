# Haalt nieuwe Modrinth-projecten (mods) op, nieuwste eerst, tot een einddatum.
# Gebruik: python3 modrinth-haal-script.py <type> <vanaf-datum> <uitvoer.json>
import json, sys, time, urllib.request, urllib.parse
typ, vanaf, uit = sys.argv[1], sys.argv[2], sys.argv[3]
res, off = [], 0
while True:
    q = urllib.parse.urlencode({"index": "newest", "limit": 100, "offset": off,
        "facets": json.dumps([[f"project_type:{typ}"]])})
    req = urllib.request.Request("https://api.modrinth.com/v2/search?" + q, headers={"User-Agent": "dortus-verkenner"})
    hits = json.load(urllib.request.urlopen(req, timeout=60))["hits"]
    if not hits: break
    for h in hits:
        res.append({k: h.get(k) for k in ["project_id","slug","title","author","downloads","follows","date_created","categories","client_side","server_side"]})
    off += 100
    if hits[-1]["date_created"][:10] < vanaf: break
    time.sleep(0.25)
json.dump(res, open(uit, "w"))
print(len(res), res[-1]["date_created"])
