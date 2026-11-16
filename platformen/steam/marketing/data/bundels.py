#!/usr/bin/env python3
"""Bundels op Steam van bureaubladspellen: welke spellen zitten in een bundel, sinds wanneer uit, hoeveel reviews (Sem, 16 nov 2026, run 8).
Gebruik: python3 bundels.py <uit.csv> <bundelid> [<bundelid> ...]
Leest de openbare bundelpagina en appdetails (aanbevelingen = positieve reviews volgens appdetails; appreviews stuurde ons op 16 nov door naar de voorpagina) (zonder inlog), rustig: 2 s per verzoek, opnieuw bij een fout."""
import csv, html, json, re, subprocess, sys, time

def haal(url):
    for poging in range(4):
        x = subprocess.run(["curl", "-s", "-m", "25", "-A", "Mozilla/5.0", url], capture_output=True, text=True).stdout
        time.sleep(2)
        if x.strip():
            return x
        time.sleep(10 * (poging + 1))
    return ""

w = csv.writer(open(sys.argv[1], "w", newline=""))
w.writerow(["bundelid", "bundelnaam", "appid", "naam", "releasedatum", "makers", "uitgevers", "aanbevelingen"])
for b in sys.argv[2:]:
    s = haal(f"https://store.steampowered.com/bundle/{b}/?l=english&cc=us")
    t = re.search(r'<h2 class="pageheader">(.*?)</h2>', s, re.S)
    bnaam = html.unescape(t.group(1).strip()) if t else ""
    ids = list(dict.fromkeys(re.findall(r'data-ds-appid="(\d+)"', s)))
    for a in ids:
        naam = datum = makers = uitg = ""; n = ""
        try:
            d = json.loads(haal(f"https://store.steampowered.com/api/appdetails?appids={a}"))[a].get("data", {})
            naam, datum, makers = d.get("name", ""), d.get("release_date", {}).get("date", ""), "; ".join(d.get("developers", []))
            uitg = "; ".join(x.strip() for x in d.get("publishers", []))
            n = d.get("recommendations", {}).get("total", "")  # leeg = appdetails geeft geen getal
        except Exception:
            pass
        w.writerow([b, bnaam, a, naam, datum, makers, uitg, n])
        print(b, a, naam, datum, n, flush=True)
