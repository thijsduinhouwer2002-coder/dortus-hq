#!/usr/bin/env python3
"""Lange beschrijving (about_the_game) van dezelfde 47 spellen als winkeltekst.py:
aantal woorden, plaatjes, bewegende plaatjes (gif/webm/mp4 of animated), kopjes, opsommingen.
Leest de appids uit winkeltekst-2026-11-16.csv. Rustig: 1,6 s per verzoek; bij 429 stoppen.
Gebruik: python3 winkeltekst_lang.py winkeltekst-2026-11-16.csv uit.csv
"""
import csv, json, re, sys, time, subprocess, html
rows = list(csv.DictReader(open(sys.argv[1])))
out = csv.writer(open(sys.argv[2], "w", newline=""))
out.writerow(["soort", "appid", "naam", "woorden", "plaatjes", "bewegend", "kopjes", "opsomming_punten", "eerste_kop"])
for r in rows:
    p = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "--max-time", "30",
        f"https://store.steampowered.com/api/appdetails?appids={r['appid']}&l=english&cc=us"], capture_output=True, text=True)
    body, _, code = p.stdout.rpartition("\n")
    if code == "429": print("429, gestopt"); break
    try: a = json.loads(body)[r["appid"]]["data"].get("about_the_game", "")
    except Exception: print("geen data", r["naam"]); time.sleep(1.6); continue
    imgs = re.findall(r"<img[^>]+src=\"([^\"]+)\"", a)
    bew = [i for i in imgs if re.search(r"\.(gif|webm|mp4)|animated", i, re.I)] + re.findall(r"<video", a)
    kop = re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", a, re.S)
    punten = len(re.findall(r"<li", a))
    tekst = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", a))).strip()
    eerste = re.sub(r"<[^>]+>", "", kop[0]).strip() if kop else ""
    out.writerow([r["soort"], r["appid"], r["naam"], len(tekst.split()), len(imgs), len(bew), len(kop), punten, eerste[:60]])
    time.sleep(1.6)
