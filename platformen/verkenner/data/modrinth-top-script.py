# Momentopname van downloads van de top N projecten (alle soorten), om downloads per uur te schatten.
# Gebruik: python3 modrinth-top-script.py <N> <uitvoer.json>
import json, sys, time, urllib.request, urllib.parse
n, uit = int(sys.argv[1]), sys.argv[2]
res = {}
for off in range(0, n, 100):
    q = urllib.parse.urlencode({"index": "downloads", "limit": 100, "offset": off})
    req = urllib.request.Request("https://api.modrinth.com/v2/search?" + q, headers={"User-Agent": "dortus-verkenner"})
    for h in json.load(urllib.request.urlopen(req, timeout=60))["hits"]:
        res[h["project_id"]] = h["downloads"]
    time.sleep(0.2)
json.dump({"tijd": time.time(), "dl": res}, open(uit, "w"))
print(len(res), sum(res.values()))
