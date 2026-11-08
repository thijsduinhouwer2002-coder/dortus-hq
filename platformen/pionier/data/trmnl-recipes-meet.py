#!/usr/bin/env python3
"""Telt alle TRMNL-recipes via de open API (trmnl.com/recipes.json) en voegt een regel toe aan trmnl-recipes.csv.
Gebruik: python3 trmnl-recipes-meet.py [dumpmap]. Rustig: 1 verzoek per 1,5 seconde (limiet is 60 per minuut)."""
import json, sys, os, time, statistics, urllib.request, collections, datetime
hier = os.path.dirname(os.path.abspath(__file__))
alle = []; page = 1
while True:
    url = f"https://trmnl.com/recipes.json?per_page=100&page={page}&sort-by=install"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "dortus-meting"}), timeout=60))
    items = d.get("data", d if isinstance(d, list) else [])
    if not items: break
    alle += items; page += 1; time.sleep(1.5)
    if page > 60: break
if len(sys.argv) > 1:
    json.dump(alle, open(sys.argv[1], "w"))
inst = [r.get("stats", {}).get("installs", 0) or 0 for r in alle]
conn = [(r.get("stats", {}).get("installs", 0) or 0) + (r.get("stats", {}).get("forks", 0) or 0) for r in alle]
auteurs = {r.get("user_id") for r in alle}
vandaag = datetime.date.today().isoformat()
regel = [vandaag, len(alle), len(auteurs), sum(inst), sum(conn) - sum(inst), sum(c >= 50 for c in conn), sum(i >= 500 for i in inst), statistics.median(inst) if inst else 0]
pad = os.path.join(hier, "trmnl-recipes.csv")
nieuw = not os.path.exists(pad)
with open(pad, "a") as f:
    if nieuw: f.write("datum,recipes,auteurs,installs,forks,boven_50_connections,boven_500_installs,mediaan_installs\n")
    f.write(",".join(map(str, regel)) + "\n")
print(regel)
