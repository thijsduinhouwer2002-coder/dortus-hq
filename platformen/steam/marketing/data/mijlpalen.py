#!/usr/bin/env python3
"""Zoekt in de Steam-aankondigingen (nieuws-API, openbaar) van een lijst spellen naar verlanglijst-mijlpalen.
Gebruik: python3 mijlpalen.py demo-spelers-2026-11-16.csv uit.csv
Schrijft per gevonden aankondiging: appid, naam, datum, getal, titel. Rustig: 1 verzoek per 0,7 s."""
import sys, csv, json, re, time, subprocess, datetime
rij = list(csv.DictReader(open(sys.argv[1])))
w = csv.writer(open(sys.argv[2], 'w')); w.writerow(['appid','naam','spelers_demo_16nov','datum','getal','titel'])
pat = re.compile(r'wish ?list', re.I)
def getal(t):
    m = re.search(r'(\d[\d,\.]*)\s*(k|K|000)?\s*(\+)?\s*wish', t) or re.search(r'(\d[\d,\.]*)\s*(k|K)?', t)
    if not m: return ''
    n = m.group(1).replace(',', '')
    try:
        v = float(n)
    except ValueError:
        return ''
    if m.group(2) in ('k', 'K'): v *= 1000
    return int(v)
for r in rij:
    url = f"https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={r['appid']}&count=60&maxlength=1"
    out = subprocess.run(['curl', '-s', '-m', '20', url], capture_output=True, text=True).stdout
    try:
        items = json.loads(out)['appnews']['newsitems']
    except Exception:
        items = []
    for n in items:
        if pat.search(n['title']) and n.get('feedname') == 'steam_community_announcements':
            d = datetime.datetime.fromtimestamp(n['date'], datetime.UTC).date()
            w.writerow([r['appid'], r['naam'], r['spelers_tegelijk'], d, getal(n['title']), n['title']])
    time.sleep(0.7)
