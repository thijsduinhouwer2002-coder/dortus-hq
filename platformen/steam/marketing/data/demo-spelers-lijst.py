# Spelers tegelijk in demo's voor een lijst appids (Sem). Gebruik:
#   python3 demo-spelers-lijst.py <appids.txt> <uit.csv> [demo-appids-cache.csv]
# Met een cache (uitvoer van een eerdere run) slaat hij appdetails over en meet alleen opnieuw.
import csv, json, sys, time, urllib.request, datetime
def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as f:
                return json.load(f)
        except Exception:
            time.sleep(3)
    return None
ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
cache = {}
if len(sys.argv) > 3:
    for x in csv.DictReader(open(sys.argv[3])):
        cache[x['appid']] = (x['naam'], x['demo_appid'])
uit = []
for a in ids:
    if a in cache:
        naam, demo = cache[a]
    else:
        d = get(f"https://store.steampowered.com/api/appdetails?appids={a}&filters=basic,demos")
        naam, demo = '', ''
        try:
            naam = d[a]['data']['name']
            demo = str(d[a]['data'].get('demos', [{}])[0].get('appid', ''))
        except Exception:
            pass
        time.sleep(1.2)
    n = ''
    if demo:
        p = get(f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={demo}")
        try: n = p['response']['player_count']
        except Exception: n = ''
    uit.append([a, naam, demo, n])
w = csv.writer(open(sys.argv[2], 'w', newline=''))
w.writerow(['appid', 'naam', 'demo_appid', 'spelers_tegelijk'])
w.writerows(uit)
print(datetime.datetime.now(datetime.timezone.utc).isoformat(), len(uit))
