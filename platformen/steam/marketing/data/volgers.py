#!/usr/bin/env python3
"""Volgers (leden van de communitygroep) van aangekondigde spellen, via de openbare memberslistxml (zonder inlog). Met curl: Python-urllib kreeg bij ±2 van 3 verzoeken geen getal terug (run 7).
Sem, 16 nov 2026. Gebruik: python3 volgers.py <kaart.csv> <uit.csv> [lijkt_op_hats-waarden, bv. 2,3]
Vult aan: appids die al een getal hebben in <uit.csv> worden overgeslagen. Steam geeft 429 bij meer dan ±1 per seconde; daarom 2 s per verzoek.
Alleen spellen met binnenkort=True. Rustig: ±2 verzoeken per seconde."""
import csv, re, sys, time, subprocess
import os
rij = [r for r in csv.DictReader(open(sys.argv[1])) if r["binnenkort"] == "True"]
if len(sys.argv) > 3: rij = [r for r in rij if r["lijkt_op_hats"] in sys.argv[3].split(",")]
oud = {}
if os.path.exists(sys.argv[2]):
    oud = {r["appid"]: r for r in csv.DictReader(open(sys.argv[2])) if r["volgers"]}
uitf = open(sys.argv[2], "w", newline="", buffering=1)
w = csv.writer(uitf)
w.writerow(["appid", "naam", "releasedatum", "demo", "lijkt_op_hats", "aantal_talen", "volgers"])
for o in oud.values():
    w.writerow([o[k] for k in ["appid", "naam", "releasedatum", "demo", "lijkt_op_hats", "aantal_talen", "volgers"]])
for r in rij:
    if r["appid"] in oud: continue
    n = ""
    for _ in range(2):
        try:
            x = subprocess.run(["curl", "-s", "--max-time", "20", "-A", "Mozilla/5.0", f"https://steamcommunity.com/games/{r['appid']}/memberslistxml/?xml=1"], capture_output=True, text=True).stdout
            m = re.search(r"<memberCount>(\d+)</memberCount>", x)
            n = m.group(1) if m else ""
            if n: break
            time.sleep(3)
        except Exception:
            time.sleep(10)
    w.writerow([r["appid"], r["naam"], r["releasedatum"], r["demo"], r["lijkt_op_hats"], r["aantal_talen"], n])
    time.sleep(2)
