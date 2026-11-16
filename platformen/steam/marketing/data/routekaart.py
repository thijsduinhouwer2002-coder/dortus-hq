#!/usr/bin/env python3
"""Toets voorstel Fenna (routekaart met vinkjes): wanneer posten winnaars en flops een routekaart?
Leest per spel de uitgavedatum (appdetails) en alle eigen aankondigingen (ISteamNews).
Telt aankondigingen voor en na de uitgave, en welke het woord roadmap / upcoming / coming soon to bevatten.
Gebruik: python3 routekaart.py uit.csv
"""
import csv, json, re, sys, time, subprocess, datetime as dt

SPELLEN = [
 ("winnaar", 2666510, "Rusty's Retirement"), ("winnaar", 3678970, "TBH: Task Bar Hero"),
 ("winnaar", 3167550, "Tiny Pasture"), ("winnaar", 3416070, "Ropuka's Idle Island"),
 ("winnaar", 3511030, "Mini Cozy Room"), ("winnaar", 4623570, "Deskrawl"),
 ("winnaar", 3772810, "Desktop Defender"), ("winnaar", 4283650, "Cozy Mining"),
 ("winnaar", 3972410, "Black Cat Book Club"), ("winnaar", 3454590, "Cornerpond"),
 ("winnaar", 2113850, "Spirit City"), ("winnaar", 3399960, "Fish to Dish"),
 ("winnaar", 4111370, "Birdwatching Notebook"),
 ("flop", 4547080, "Minimon"), ("flop", 3982800, "Idle Squire"),
 ("flop", 3897350, "Idlewood Outpost"), ("flop", 5135740, "Dungeoneers Idle"),
]
WOORD = re.compile(r"road ?map|upcoming (update|feature|content)|what'?s (coming|next)|coming soon to|update plan|planned (feature|update)", re.I)

def get(url):
    for _ in range(3):
        r = subprocess.run(["curl", "-s", "--max-time", "30", url], capture_output=True, text=True)
        if r.stdout.strip():
            return r.stdout
        time.sleep(2)
    return ""

def uitdatum(appid):
    d = json.loads(get(f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=us&l=en") or "{}")
    x = d.get(str(appid), {}).get("data", {})
    s = x.get("release_date", {}).get("date", "")
    for f in ("%d %b, %Y", "%b %d, %Y", "%d %B, %Y", "%B %d, %Y"):
        try: return dt.datetime.strptime(s, f).date(), s, x.get("release_date", {}).get("coming_soon")
        except ValueError: pass
    return None, s, x.get("release_date", {}).get("coming_soon")

rijen = []
for soort, appid, naam in SPELLEN:
    uit, ruw, binnenkort = uitdatum(appid)
    n = json.loads(get(f"https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={appid}&count=500&maxlength=0&feeds=steam_community_announcements") or "{}")
    items = n.get("appnews", {}).get("newsitems", [])
    voor = na = rk_voor = rk_na = 0
    eerste_rk_na = None; titels = []
    for it in items:
        d = dt.datetime.fromtimestamp(it["date"], dt.timezone.utc).date()
        hit = bool(WOORD.search(it.get("title", "") + " " + it.get("contents", "")[:4000]))
        if uit and d < uit:
            voor += 1; rk_voor += hit
            if hit: titels.append(f"VOOR {d} {it['title'][:60]}")
        else:
            na += 1; rk_na += hit
            if hit and uit:
                dagen = (d - uit).days
                if eerste_rk_na is None or dagen < eerste_rk_na: eerste_rk_na = dagen
                titels.append(f"NA+{dagen} {it['title'][:60]}")
    rijen.append(dict(soort=soort, appid=appid, naam=naam, uit=ruw, aankondigingen_voor=voor,
        met_routekaart_voor=rk_voor, aankondigingen_na=na, met_routekaart_na=rk_na,
        eerste_routekaart_dagen_na_uitgave=eerste_rk_na, titels=" | ".join(sorted(titels)[:8])))
    print(naam, ruw, voor, rk_voor, na, rk_na, eerste_rk_na, file=sys.stderr)
    time.sleep(1.5)

with open(sys.argv[1], "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rijen[0])); w.writeheader(); w.writerows(rijen)
