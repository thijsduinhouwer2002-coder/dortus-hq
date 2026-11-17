# Zoekmeting Chrome Web Store (Chris, 17 nov 2026).
# Gebruik: python3 -I zoek-winkel.py "zoekwoord 1" "zoekwoord 2" ...
# Per zoekwoord: de eerste 10 resultaten met gebruikers, sterren, aantal beoordelingen
# en of de winkel "in-app purchases" toont. Rustig: 1 verzoek per seconde.
import re, subprocess, sys, time, urllib.parse

def haal(url):
    r = subprocess.run(['curl', '-sS', '-L', '-m', '30', '-A', 'Mozilla/5.0', url],
                       capture_output=True, text=True)
    return r.stdout

def getal(t):
    return int(t.replace(',', '')) if t else 0

def detail(pad):
    h = haal('https://chromewebstore.google.com/' + pad + '?hl=en')
    naam = re.search(r'<title>([^<]*?) - Chrome Web Store', h)
    users = re.search(r'>([\d,]+) users?<', h)
    ster = re.search(r'([\d.]+) out of 5', h)
    aantal = re.search(r'>?([\d,.K]+) ratings?<', h)
    return {
        'naam': (naam.group(1) if naam else pad).replace('&amp;', '&').replace('\u2013', ':').replace('\u2014', ':').replace('|', '/')[:60],
        'users': getal(users.group(1)) if users else 0,
        'ster': ster.group(1) if ster else '-',
        'beoord': aantal.group(1) if aantal else '0',
        'iap': 'ja' if 'in-app purchases' in h else 'nee',
    }

for zoek in sys.argv[1:]:
    h = haal('https://chromewebstore.google.com/search/' + urllib.parse.quote(zoek) + '?hl=en')
    paden = []
    for p in re.findall(r'detail/[a-z0-9-]*/[a-p]{32}', h):
        if p not in paden:
            paden.append(p)
    rijen = []
    for p in paden[:10]:
        time.sleep(1)
        rijen.append(detail(p))
    print(f'\n### "{zoek}"\n')
    print('| # | Extensie | Gebruikers | Sterren | Beoordelingen | In-app |')
    print('|---|---|---|---|---|---|')
    for i, r in enumerate(rijen, 1):
        print(f"| {i} | {r['naam']} | {r['users']:,} | {r['ster']} | {r['beoord']} | {r['iap']} |".replace(',', '.'))
    top = max([r['users'] for r in rijen] or [0])
    print(f"\nGrootste in top 10: {top:,} gebruikers. Met in-app: {sum(r['iap']=='ja' for r in rijen)} van {len(rijen)}.".replace(',', '.'))
