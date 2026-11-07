# Haalt per product de open info op van Polymart (nu voxel.shop) via api.polymart.org.
# Gebruik: python3 polymart-haal-script.py ids.txt uit.jsonl
# ids.txt: een id per regel (uit de sitemap https://polymart.org/sitemap.xml, met -L volgen).
# De API geeft 429 bij te snel vragen: daarom een voor een, rustig, en hervatbaar (slaat ids over die al in uit.jsonl staan).
import sys, json, urllib.request, urllib.error, time, os
ids = [int(l) for l in open(sys.argv[1]) if l.strip()]
klaar = set()
if os.path.exists(sys.argv[2]):
    klaar = {json.loads(l)["id"] for l in open(sys.argv[2])}
f = open(sys.argv[2], "a")
for i in ids:
    if i in klaar: continue
    wacht = 15
    while True:
        try:
            with urllib.request.urlopen(f"https://api.polymart.org/v1/getResourceInfo?resource_id={i}", timeout=15) as r:
                d = json.load(r)["response"]
            break
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(wacht); wacht = min(wacht * 2, 120); continue
            d = {"error": f"http {e.code}"}; break
        except Exception as e:
            time.sleep(5); continue
    x = d.get("resource")
    if not x: rij = {"id": i, "fout": d.get("error")}
    else:
        rij = {"id": i, "titel": x.get("title"), "prijs": float(x.get("price") or 0), "munt": x.get("currency"),
               "gemaakt": x.get("creationTime"), "downloads": x.get("downloads"), "owner_id": x.get("owner_id"),
               "reviews": (x.get("reviews") or {}).get("count"), "sterren": (x.get("reviews") or {}).get("stars"),
               "laatste_update": ((x.get("updates") or {}).get("latest") or {}).get("time")}
    f.write(json.dumps(rij) + "\n"); f.flush()
    time.sleep(0.4)
