"""Wie staat in de lijst "meest op verlanglijsten" van een tag, en hoeveel volgers heeft die (Sem, run 16, 17 nov 2026).
Openbaar: Steam-zoeken met filter=popularwishlist (zonder inlog) en de memberslistxml voor volgers.
Rustig: 2 s per volgerstelling. Gebruik: python3 top-verlanglijst.py uitvoer.csv
"""
import csv, json, re, subprocess, sys, time

TAGS = {"Desktop Companion": 1320952, "Idler": 615955, "Cozy": 97376}

def curl(url):
    return subprocess.run(["curl", "-s", "--max-time", "25", "-A", "Mozilla/5.0", url],
                          capture_output=True, text=True, errors="replace").stdout

def lijst(tagid):
    rijen, start = [], 0
    while True:
        d = json.loads(curl(f"https://store.steampowered.com/search/results/?query&start={start}&count=100"
                            f"&tags={tagid}&filter=popularwishlist&infinite=1&cc=us&l=english"))
        h = d["results_html"]
        ids = re.findall(r'data-ds-appid="(\d+)"', h)
        namen = re.findall(r'<span class="title">(.*?)</span>', h)
        datums = re.findall(r'search_released[^>]*>\s*(.*?)\s*</div>', h, re.S)
        for a, n, dt in zip(ids, namen, datums):
            rijen.append((a, n.replace("&amp;", "&"), dt))
        start += 100
        if start >= d.get("total_count", 0) or start >= 200 or not ids:
            return rijen, d.get("total_count")

def volgers(appid):
    x = curl(f"https://steamcommunity.com/games/{appid}/memberslistxml/?xml=1")
    m = re.search(r"<memberCount>(\d+)</memberCount>", x)
    return int(m.group(1)) if m else ""

uit = csv.writer(open(sys.argv[1], "w", newline=""))
uit.writerow(["tag", "plek", "totaal_in_lijst", "appid", "naam", "uitgave", "volgers", "gemeten_utc"])
for tag, tid in TAGS.items():
    rijen, totaal = lijst(tid)
    for i, (a, n, dt) in enumerate(rijen[:40], 1):
        v = volgers(a); time.sleep(2)
        uit.writerow([tag, i, totaal, a, n, dt, v, time.strftime("%Y-%m-%d %H:%M", time.gmtime())])
        print(tag, i, n, dt, v, flush=True)
