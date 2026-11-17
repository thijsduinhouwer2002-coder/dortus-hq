#!/usr/bin/env python3
"""Lanceercohort: bureaubladspellen die tussen twee datums uitkomen, gemeten vóór en na hun uitgave (Sem, run 21, 17 nov 2026).
Doel: eigen ijking voor het lanceerplan van Hats. Hoeveel volgers had een spel op de dag vóór de uitgave, en hoeveel
reviews (van kopers) en spelers tegelijk had het na 1, 7 en 14 dagen? Dat kan je achteraf niet meer meten, want Steam
bewaart de volgers van vroeger niet. Dus: nu een nulmeting, daarna elke run aanvullen.

Gebruik: python3 lanceer-cohort.py <kaart.csv> <uit.csv> <van JJJJ-MM-DD> <tot JJJJ-MM-DD> [False]
Elke aanroep voegt per spel één regel toe (tijd_utc, ...). Draai hem dus gewoon opnieuw voor een volgend meetpunt.
Bronnen, alle openbaar en zonder sleutel: store appdetails, appreviews (query_summary, valt soms weg) en de winkelpagina (meegetelde reviews), memberslistxml (volgers),
GetNumberOfCurrentPlayers. Rustig: ±1 verzoek per 1,5 s."""
import csv, json, os, re, subprocess, sys, time, datetime as dt

def get(url, keer=3):
    for _ in range(keer):
        x = subprocess.run(["curl", "-s", "--compressed", "--max-time", "25", "-A", "Mozilla/5.0", url], capture_output=True, text=True, errors="replace").stdout
        if x.strip():
            return x
        time.sleep(3)
    return ""

def js(url, keer=3):
    try:
        return json.loads(get(url, keer))
    except Exception:
        return {}

kaart, uit, van, tot = sys.argv[1:5]
soort = sys.argv[5] if len(sys.argv) > 5 else "True"  # "False" = al uitgebrachte spellen (terugblik)
rij = [r for r in csv.DictReader(open(kaart)) if r["binnenkort"] == soort and van <= r["releasedatum"] <= tot
       and r["soort_app"] == "game"]
nieuw = not os.path.exists(uit)
t = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
# Al gemeten vandaag (met volgers)? Dan overslaan, zodat een afgebroken meting gewoon kan worden voortgezet.
klaar = set() if nieuw else {o["appid"] for o in csv.DictReader(open(uit)) if o["tijd_utc"][:10] == t[:10] and o["volgers"]}
rij = [r for r in rij if r["appid"] not in klaar]
f = open(uit, "a", newline="", buffering=1)
w = csv.writer(f)
kop = ["tijd_utc", "appid", "naam", "lijkt_op_hats", "datum_kaart", "datum_winkel", "binnenkort_nu", "prijs_usd",
       "demo_appid", "volgers", "reviews_alle", "reviews_kopers", "pct_positief_kopers", "spelers_tegelijk"]
if nieuw:
    w.writerow(kop)
for r in rij:
    a = r["appid"]
    d = js(f"https://store.steampowered.com/api/appdetails?appids={a}&cc=us&l=english").get(a, {}).get("data", {})
    time.sleep(1.5)
    rd = d.get("release_date", {})
    prijs = d.get("price_overview", {}).get("final", "")
    prijs = f"{prijs/100:.2f}" if prijs != "" else ("0" if d.get("is_free") else "")
    demo = ";".join(str(x.get("appid")) for x in d.get("demos", []) or [])
    volg = ""
    for poging in range(4):  # steamcommunity geeft 429 ("null") bij te veel verzoeken: dan wachten en opnieuw
        x = get(f"https://steamcommunity.com/games/{a}/memberslistxml/?xml=1", 1)
        m = re.search(r"<memberCount>(\d+)</memberCount>", x)
        if m:
            volg = m.group(1); break
        time.sleep(30 * (poging + 1))
    time.sleep(3)
    q1 = js(f"https://store.steampowered.com/appreviews/{a}?json=1&language=all&purchase_type=all&num_per_page=0", 1).get("query_summary", {})
    time.sleep(1)
    # appreviews stuurde op 17 nov vanaf hier door naar de voorpagina (302); daarom de winkelpagina zelf.
    # De tooltip "NN% of the N user reviews for this game are positive." telt alleen reviews die meetellen (kopers, geen sleutels).
    pag = get(f"https://store.steampowered.com/app/{a}/?l=english", 1)
    m2 = re.search(r"(\d+)% of the ([\d,]+) user reviews for this game are positive", pag)
    m3 = re.search(r"not_enough_reviews[^>]*>\s*(\d+) user reviews?", pag)
    if m2: tk, pct = m2.group(2).replace(",", ""), m2.group(1)
    elif m3: tk, pct = m3.group(1), ""
    else: tk, pct = ("0" if pag and "No user reviews" in pag else ""), ""
    time.sleep(1.5)
    cc = js(f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={a}").get("response", {}).get("player_count", "")
    time.sleep(1)
    w.writerow([t, a, r["naam"], r["lijkt_op_hats"], r["releasedatum"], rd.get("date", ""), rd.get("coming_soon", ""), prijs,
                demo, volg, q1.get("total_reviews", ""), tk, pct, cc])
    print(a, r["naam"][:40], rd.get("date", ""), volg, tk, cc, flush=True)
