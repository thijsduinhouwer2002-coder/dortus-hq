#!/usr/bin/env python3
"""Hoeveel volgers geeft een YouTube-weergave? Per aangekondigd bureaubladspel: alle video's op de eerste zoekpagina van YouTube voor "<naam> trailer" en "<naam> game" samen
waarvan de titel de naam van het spel bevat (van iedereen, ook de maker zelf), opgeteld, naast de volgers op Steam van nu.
Sem, 17 nov 2026, run 15. Gebruik: python3 yt-volgers.py <volgers.csv> <uit.csv> [min_volgers]
Rustig: 3 s per zoekopdracht (YouTube) en 2 s per volgerstelling (Steam memberslistxml)."""
import csv, sys, re, time, subprocess, importlib.util, unicodedata
spec = importlib.util.spec_from_file_location("ytz", __file__.replace("yt-volgers.py", "yt-zoek.py"))
ytz = importlib.util.module_from_spec(spec); spec.loader.exec_module(ytz)

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", s).split()

def kern(naam):
    k = re.split(r"\s[-:|]\s?|:\s|\s-", naam)[0].strip()
    return k if len(norm(k)) else naam

def getal(t):
    t = t.replace(",", "").lower()
    m = re.search(r"([\d.]+)\s*([km]?)", t)
    if not m: return 0
    n = float(m.group(1)); return int(n * {"k": 1e3, "m": 1e6}.get(m.group(2), 1))

def volgers(appid):
    for _ in range(2):
        x = subprocess.run(["curl", "-s", "--max-time", "20", "-A", "Mozilla/5.0", f"https://steamcommunity.com/games/{appid}/memberslistxml/?xml=1"], capture_output=True, text=True, errors="replace").stdout
        m = re.search(r"<memberCount>(\d+)</memberCount>", x)
        if m: return int(m.group(1))
        time.sleep(3)
    return ""

mn = int(sys.argv[3]) if len(sys.argv) > 3 else 0
rij = [r for r in csv.DictReader(open(sys.argv[1])) if r["volgers"] and int(r["volgers"]) >= mn]
import os
klaar = {x["appid"] for x in csv.DictReader(open(sys.argv[2]))} if os.path.exists(sys.argv[2]) else set()
rij = [r for r in rij if r["appid"] not in klaar]
w = csv.writer(open(sys.argv[2], "a", newline="", buffering=1))
if not klaar: w.writerow(["appid", "naam", "zoekterm", "zoekresultaten", "volgers_nu", "videos_met_naam", "weergaven_som", "grootste_video", "grootste_kanaal", "grootste_titel", "grootste_id"])
for r in rij:
    k = kern(r["naam"]); kw = norm(k)
    items, gezien = [], set()
    for q in (f"{k} trailer", f"{k} game"):
        for poging in range(2):
            try: res = ytz.zoek(q, "relevant")
            except Exception: res = []
            if res: break
            time.sleep(5)
        for v in res:
            if v["id"] not in gezien: gezien.add(v["id"]); items.append(v)
        time.sleep(3)
    hit = []
    for v in items:
        tw = " ".join(norm(v["titel"]))
        if " ".join(kw) in tw: hit.append(v)
    som = sum(getal(v["weergaven"]) for v in hit)
    top = max(hit, key=lambda v: getal(v["weergaven"])) if hit else {}
    time.sleep(3)
    vn = volgers(r["appid"]); time.sleep(2)
    w.writerow([r["appid"], r["naam"], k, len(items), vn, len(hit), som, getal(top.get("weergaven", "")), top.get("kanaal", ""), top.get("titel", "")[:80], top.get("id", "")])
    print(r["naam"], vn, len(hit), som, flush=True)
