#!/usr/bin/env python3
"""Tags (door spelers gestemd, volgorde van Steam) van de 43 spellen uit winkeltekst-2026-11-16.csv
zonder de kerkerflops, plus de tags van ons voorstel. Leest de winkelpagina met curl (InitAppTagModal).
Rustig: 2 s per pagina; bij 429 stoppen. Gebruik: python3 tags.py winkeltekst-2026-11-16.csv uit.csv
"""
import csv, json, re, sys, time, subprocess
rows = [r for r in csv.DictReader(open(sys.argv[1]))]
out = csv.writer(open(sys.argv[2], "w", newline=""))
out.writerow(["soort", "appid", "naam", "tags_op_volgorde"])
for r in rows:
    p = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "--max-time", "30", "-b", "birthtime=0; lastagecheckage=1-0-1990; Steam_Language=english",
        f"https://store.steampowered.com/app/{r['appid']}/?l=english"], capture_output=True, text=True)
    body, _, code = p.stdout.rpartition("\n")
    if code == "429": print("429, gestopt"); break
    m = re.search(r"InitAppTagModal\(\s*\d+,\s*(\[.*?\])\s*,", body, re.S)
    tags = [t["name"] for t in json.loads(m.group(1))] if m else []
    out.writerow([r["soort"], r["appid"], r["naam"], "|".join(tags)])
    print(r["soort"], r["naam"][:25], len(tags))
    time.sleep(2)
