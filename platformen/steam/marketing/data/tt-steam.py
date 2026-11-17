#!/usr/bin/env python3
"""Koppelt TikTok-video's (uit tt-video.py) aan het spel op Steam: appid (winkelzoeker), volgers (memberslistxml), uitgebracht ja/nee.
Sem, 17 nov 2026. Gebruik: python3 tt-steam.py urls.txt video.csv uit.csv  (urls.txt: 'url # spelnaam')"""
import sys, csv, json, re, time, subprocess, urllib.parse
def curl(u): return subprocess.run(["curl","-s","--max-time","20","-A","Mozilla/5.0",u],capture_output=True,text=True).stdout
naam = {l.split("#")[0].strip(): l.split("#",1)[1].strip() for l in open(sys.argv[1]) if "#" in l}
vid = {r["url"]: r for r in csv.DictReader(open(sys.argv[2]))}
out = []
for url, spel in naam.items():
    r = vid.get(url, {})
    z = json.loads(curl("https://store.steampowered.com/api/storesearch/?cc=us&l=en&term=" + urllib.parse.quote(spel)) or "{}")
    hit = next((i for i in z.get("items", []) if re.sub(r"\W","",i["name"].lower()) == re.sub(r"\W","",spel.lower())), None)
    time.sleep(1.5)
    if not hit: out.append(dict(spel=spel, appid="", volgers="", uit="", video_datum=r.get("datum",""), weergaven=r.get("weergaven",""), volgers_per_1000="")); continue
    a = hit["id"]
    m = re.search(r"<memberCount>(\d+)</memberCount>", curl(f"https://steamcommunity.com/games/{a}/memberslistxml/?xml=1")); time.sleep(2)
    d = json.loads(curl(f"https://store.steampowered.com/api/appdetails?appids={a}&filters=release_date") or "{}").get(str(a), {}).get("data", {}); time.sleep(1.5)
    v = int(m.group(1)) if m else ""
    w = int(r.get("weergaven") or 0)
    out.append(dict(spel=spel, appid=a, volgers=v, uit=d.get("release_date",{}).get("date","") if not d.get("release_date",{}).get("coming_soon") else "binnenkort",
        video_datum=r.get("datum",""), weergaven=w, volgers_per_1000=round(v/w*1000,1) if v and w else ""))
    print(out[-1])
with open(sys.argv[3],"w",newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(out[0].keys())); wr.writeheader(); wr.writerows(out)
