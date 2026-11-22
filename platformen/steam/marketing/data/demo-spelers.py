# Meet spelers tegelijk in de demo's van aangekondigde bureaubladspellen (Sem).
# Bron: Vera's kaart (binnenkort + demo), appdetails voor het demo-appid,
# ISteamUserStats/GetNumberOfCurrentPlayers (openbaar, zonder sleutel).
import csv, json, sys, time, urllib.request, datetime
KAART = 'onderzoek/verkenner/data/steam-desktop-kaart-2026-11-16.csv'
UIT = sys.argv[1]
def get(url):
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as f:
                return json.load(f)
        except Exception:
            time.sleep(3)
    return None
rij = [x for x in csv.DictReader(open(KAART)) if x['binnenkort'] == 'True' and x['demo'] == 'True']
uit = []
for x in rij:
    d = get(f"https://store.steampowered.com/api/appdetails?appids={x['appid']}&filters=demos")
    demo = None
    try:
        demo = d[x['appid']]['data']['demos'][0]['appid']
    except Exception:
        pass
    n = ''
    if demo:
        p = get(f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={demo}")
        try: n = p['response']['player_count']
        except Exception: n = ''
    uit.append([x['appid'], x['naam'], demo or '', n, x['lijkt_op_hats'], x['soort_spel']])
    time.sleep(1.2)
w = csv.writer(open(UIT, 'w', newline=''))
w.writerow(['appid', 'naam', 'demo_appid', 'spelers_tegelijk', 'lijkt_op_hats', 'soort_spel'])
w.writerows(uit)
print(datetime.datetime.utcnow().isoformat(), len(uit))
