#!/usr/bin/env python3
"""Meet elk uur spelers tegelijk in demo's tijdens een fest (Sem, 16 nov 2026).
Draait in GitHub Actions (steam-fest-meting.yml), zodat de meting doorloopt ook als er geen run van Sem valt.
Gebruik: python3 fest-meting.py <meetlijsten.csv> <uitmap>
meetlijsten.csv: naam,cache,start_utc,eind_utc  (cache = csv met appid,naam,demo_appid, uit demo-spelers-lijst.py)
Per actieve lijst komt er per demo een regel bij in <uitmap>/<naam>.csv: tijd_utc,appid,naam,demo_appid,spelers_tegelijk
Alleen de openbare API GetNumberOfCurrentPlayers, zonder sleutel, rustig (±3 verzoeken per seconde)."""
import csv, json, os, sys, time, urllib.request, datetime as dt

def spelers(demo):
    for _ in range(3):
        try:
            with urllib.request.urlopen(f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={demo}", timeout=20) as f:
                return json.load(f)["response"].get("player_count", "")
        except Exception:
            time.sleep(2)
    return ""

nu = dt.datetime.now(dt.timezone.utc)
os.makedirs(sys.argv[2], exist_ok=True)
for l in csv.DictReader(open(sys.argv[1])):
    start = dt.datetime.fromisoformat(l["start_utc"]).replace(tzinfo=dt.timezone.utc)
    eind = dt.datetime.fromisoformat(l["eind_utc"]).replace(tzinfo=dt.timezone.utc)
    if not (start <= nu <= eind):
        print(l["naam"], "niet actief"); continue
    uit = os.path.join(sys.argv[2], l["naam"] + ".csv")
    nieuw = not os.path.exists(uit)
    rijen = [r for r in csv.DictReader(open(l["cache"])) if r.get("demo_appid")]
    with open(uit, "a", newline="") as f:
        w = csv.writer(f)
        if nieuw: w.writerow(["tijd_utc", "appid", "naam", "demo_appid", "spelers_tegelijk"])
        t = nu.strftime("%Y-%m-%dT%H:%MZ")
        for r in rijen:
            w.writerow([t, r["appid"], r["naam"], r["demo_appid"], spelers(r["demo_appid"])])
            time.sleep(0.3)
    print(l["naam"], len(rijen), "demo's gemeten om", t)
