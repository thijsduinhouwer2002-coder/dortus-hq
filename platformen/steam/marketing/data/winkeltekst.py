#!/usr/bin/env python3
"""Wat staat er in de winkeltekst van bureaubladspellen die het goed doen, tegenover die het niet doen?
Groepen: 13 winnaars en 4 kerkerflops (lijst uit routekaart.py), 11 aangekondigde spellen waarvan de demo
20+ spelers tegelijk had (demo-spelers-2026-11-16.csv) en 20 vaste (eerste in de lijst) die op Hats lijken
en 0 spelers hadden. Per spel via de openbare appdetails: korte beschrijving (woorden, eerste woorden,
noemt taakbalk/bureaublad, noemt idle, noemt 'while you work'), lengte lange beschrijving, aantal
schermafbeeldingen en filmpjes, aantal talen. Rustig: 1,6 s per verzoek; bij 429 stoppen.
Gebruik: python3 winkeltekst.py uit.csv
"""
import csv, json, re, sys, time, subprocess, html

# zelfde lijst als routekaart.py
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

def get(url):
    r = subprocess.run(["curl", "-s", "-w", "\n%{http_code}", "--max-time", "30", url], capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    return code, body

def kaal(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()

lijst = [(soort, appid, naam) for soort, appid, naam in SPELLEN]
rows = list(csv.DictReader(open("demo-spelers-2026-11-16.csv")))
for r in rows:
    if int(r["spelers_tegelijk"] or 0) >= 20:
        lijst.append(("demo_20plus", int(r["appid"]), r["naam"]))
nul = [r for r in rows if r["spelers_tegelijk"] == "0" and r["lijkt_op_hats"] == "1"][:20]
for r in nul:
    lijst.append(("demo_0_lijkt", int(r["appid"]), r["naam"]))

PLEK = re.compile(r"taskbar|task bar|desktop|bottom of (your|the) screen|corner of (your|the) screen|screen", re.I)
IDLE = re.compile(r"\bidle\b|incremental|afk", re.I)
WERK = re.compile(r"while you (work|study|browse|play|game)|in the background|while working|productiv", re.I)

out = csv.writer(open(sys.argv[1], "w", newline=""))
out.writerow(["soort", "appid", "naam", "kort_woorden", "kort_tekens", "eerste_woorden", "noemt_plek", "noemt_idle",
              "noemt_werk", "lang_woorden", "schermafbeeldingen", "filmpjes", "talen", "korte_beschrijving"])
for soort, appid, naam in lijst:
    code, body = get(f"https://store.steampowered.com/api/appdetails?appids={appid}&l=english&cc=us")
    if code == "429":
        print("429, gestopt bij", naam); break
    try:
        d = json.loads(body)[str(appid)]["data"]
    except Exception:
        print("geen data", appid, naam); time.sleep(1.6); continue
    kort = kaal(d.get("short_description"))
    lang = kaal(d.get("about_the_game"))
    talen = len([t for t in re.split(r",", kaal(d.get("supported_languages", ""))) if t.strip()])
    out.writerow([soort, appid, d.get("name", naam), len(kort.split()), len(kort), " ".join(kort.split()[:6]),
                  int(bool(PLEK.search(kort))), int(bool(IDLE.search(kort))), int(bool(WERK.search(kort))),
                  len(lang.split()), len(d.get("screenshots", [])), len(d.get("movies", [])), talen, kort])
    print(soort, naam, len(kort.split()))
    time.sleep(1.6)
