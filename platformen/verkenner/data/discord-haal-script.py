# Haalt apps uit de officiele Discord App Directory (openbare zoek-API, geen sleutel).
# Gebruik: python3 -I discord-haal-script.py <uitvoer.json>
import json, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
BASE = "https://discord.com/api/v9/application-directory-static/search"
QUERIES = list("aeiounrst") + ["bot","game","music","mod","ai","ticket","economy","roblox"]
CATS = [None, 6, 4, 8, 9, 10]
def get(url):
    for t in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"dortus-verkenner"}), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + 3*t)
    return None
apps = {}
def page(args):
    q, c, p = args
    u = BASE + "?" + urllib.parse.urlencode({k:v for k,v in {"query":q,"category_id":c,"page":p}.items() if v is not None})
    d = get(u); return d
def keep(d):
    for x in (d or {}).get("results", []):
        a = x.get("data", {})
        de = a.get("directory_entry") or {}
        apps[a["id"]] = {"id":a["id"],"name":a.get("name"),"is_monetized":a.get("is_monetized"),
            "storefront":a.get("storefront_available"),"primary_sku":a.get("primary_sku_id"),
            "guild_count":de.get("guild_count"),"categories":[c["name"] for c in a.get("categories",[])],
            "tags":a.get("tags"),"short":de.get("short_description")}
jobs = []
with ThreadPoolExecutor(6) as ex:
    for q in QUERIES:
        for c in CATS:
            first = page((q,c,1)); keep(first)
            n = min((first or {}).get("num_pages",0), 143)
            for d in ex.map(page, [(q,c,p) for p in range(2,n+1)]): keep(d)
            print(q, c, n, len(apps), flush=True)
            json.dump(list(apps.values()), open(sys.argv[1],"w"))
json.dump(list(apps.values()), open(sys.argv[1],"w"))
