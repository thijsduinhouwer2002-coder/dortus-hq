#!/usr/bin/env python3
"""Telt alle apps en watchfaces in de Pebble-appstore van Core (open API, geen login) en voegt een regel toe aan pebble-appstore.csv.
Gebruik: python3 pebble-appstore-meet.py [dumpmap]. Rustig: 1 verzoek per seconde."""
import json, sys, os, time, statistics, urllib.request, datetime
hier = os.path.dirname(os.path.abspath(__file__))
API = "https://appstore-api.repebble.com/api/v1/apps/collection/all/{}?limit=100&offset={}"
def haal(soort):
    alle, off = [], 0
    while True:
        d = json.load(urllib.request.urlopen(urllib.request.Request(API.format(soort, off), headers={"User-Agent": "dortus-meting"}), timeout=60))
        items = d.get("data", [])
        if not items: break
        alle += items; off += 100; time.sleep(1)
        if off > 20000: break
    return alle
apps, faces = haal("watchapps-and-companions"), haal("watchfaces")
if len(sys.argv) > 1:
    json.dump({"apps": apps, "faces": faces}, open(sys.argv[1], "w"))
jaar = str(datetime.date.today().year)
def datum(x): return x.get("created_at") or x.get("published_date") or ""  # created_at = eerste upload; published_date is vaak leeg en latest_release is de laatste update
def nieuw(xs): return [x for x in xs if datum(x)[:4] == jaar]
hn = [x.get("hearts", 0) or 0 for x in nieuw(apps)]
regel = [datetime.date.today().isoformat(), len(apps), len(faces), len(nieuw(apps)), len(nieuw(faces)),
         statistics.median(hn) if hn else 0, sum(h >= 100 for h in hn)]
pad = os.path.join(hier, "pebble-appstore.csv")
nieuwbestand = not os.path.exists(pad)
with open(pad, "a") as f:
    if nieuwbestand: f.write("datum,apps,watchfaces,apps_dit_jaar,watchfaces_dit_jaar,mediaan_hearts_nieuwe_apps,nieuwe_apps_100plus_hearts\n")
    f.write(",".join(map(str, regel)) + "\n")
print(regel)
