"""Kaart van de Steam-markt voor Hats of the Fallen (Vera, 16 nov 2026, opdracht hoofdchat 16 nov 04:00).
Stap 1: kandidaten. (a) alles met label Desktop Companion (tag 1320952), alle soorten, ook binnenkort;
        (b) zoektermen op de openbare zoekpagina (taskbar, desktop pet, ...), daarna alleen houden wat in de
        winkeltekst echt over taakbalk, onderkant scherm of bureaublad gaat.
Stap 2: per app appdetails (maker, prijs, datum, talen, demo, tekst), winkelpagina (labels) en
        appreviews (totaal en positief, alle talen, alle kopers).
Gebruik: python3 -I steam-desktop-haal-script.py <uitmap> [kandidaten.json] [deel] [aantal delen]
Met een kandidatenbestand slaat hij stap 1 over; met deel/aantal doet hij elke n-de app (voor GitHub Actions).
Rustig: ongeveer 1 verzoek per seconde, alleen openbare pagina's.
"""
import json, re, sys, time, html, urllib.request, urllib.parse, os
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0', 'Cookie': 'birthtime=568022401; lastagecheckage=1-0-1988; wants_mature_content=1'}
def get(u, t=60):
    for poging in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read().decode('utf-8', 'replace')
        except Exception as e:
            if poging == 3: raise
            time.sleep(10 * (poging + 1))

def zoek(params):
    ids = []; start = 0
    while True:
        p = dict(params); p.update({'start': start, 'count': 100, 'infinite': 1, 'cc': 'us', 'l': 'english', 'ndl': 1})
        d = json.loads(get('https://store.steampowered.com/search/results/?' + urllib.parse.urlencode(p)))
        found = re.findall(r'data-ds-appid="(\d+)', d['results_html'])
        if not found: break
        ids += [int(x) for x in found]
        start += 100
        if start >= d['total_count'] or start >= 1500: break
        time.sleep(1.2)
    return ids

kfile = sys.argv[2] if len(sys.argv) > 2 else os.path.join(out, 'kandidaten.json')
deel, delen = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, 1)
if not os.path.exists(kfile):
    bron = {}
    for a in zoek({'tags': 1320952}): bron.setdefault(a, set()).add('label')
    for a in zoek({'tags': 1320952, 'filter': 'comingsoon'}): bron.setdefault(a, set()).add('label')
    for term in ['taskbar', 'desktop pet', 'desktop companion', 'desktop idle', 'idle desktop', 'bottom of your screen',
                 'while you work', 'desktop game', 'desktop buddy', 'screen companion', 'desktop farm', 'desktop dungeon']:
        for a in zoek({'term': term}): bron.setdefault(a, set()).add('zoek:' + term)
        time.sleep(1.2)
    json.dump({str(k): sorted(v) for k, v in bron.items()}, open(kfile, 'w')); print('kandidaten', len(bron), flush=True)
bron = json.load(open(kfile))
det = os.path.join(out, f'details-{deel}.jsonl')
klaar = set()
if os.path.exists(det):
    klaar = {json.loads(l)['appid'] for l in open(det)}
f = open(det, 'a')
for i, (a, b) in enumerate(bron.items()):
    a = int(a)
    if i % delen != deel or a in klaar: continue
    rec = {'appid': a, 'bron': b}
    try:
        d = json.loads(get(f'https://store.steampowered.com/api/appdetails?appids={a}&cc=us&l=english'))[str(a)]
        if d.get('success'):
            d = d['data']
            rec.update({'name': d.get('name'), 'type': d.get('type'), 'dev': d.get('developers', []), 'pub': d.get('publishers', []),
                        'free': d.get('is_free'), 'price': (d.get('price_overview') or {}).get('initial'),
                        'date': (d.get('release_date') or {}).get('date'), 'soon': (d.get('release_date') or {}).get('coming_soon'),
                        'lang': re.sub(r'<[^>]+>', '', d.get('supported_languages') or '').replace('languages with full audio support', '').strip(),
                        'demo': bool(d.get('demos')), 'short': d.get('short_description', ''),
                        'about': re.sub(r'<[^>]+>', ' ', d.get('about_the_game') or '')[:4000],
                        'genres': [g['description'] for g in d.get('genres', [])], 'dlc': len(d.get('dlc', []))})
    except Exception as e: rec['err'] = str(e)
    time.sleep(1.0)
    if rec.get('type') in ('game', 'application', 'demo', None):
        try:
            h = get(f'https://store.steampowered.com/app/{a}/?cc=us&l=english')
            rec['tags'] = [html.unescape(t.strip()) for t in re.findall(r'class="app_tag"[^>]*>\s*([^<]+?)\s*</a>', h)]
        except Exception as e: rec['tag_err'] = str(e)
        time.sleep(1.0)
        if not rec.get('soon'):
            try:
                r = json.loads(get(f'https://store.steampowered.com/appreviews/{a}?json=1&language=all&purchase_type=all&num_per_page=0&filter=all'))
                q = r.get('query_summary', {}); rec['rev'] = q.get('total_reviews'); rec['revpos'] = q.get('total_positive')
            except Exception as e: rec['rev_err'] = str(e)
            time.sleep(1.0)
    f.write(json.dumps(rec) + '\n'); f.flush()
    if i % 50 == 0: print(i, flush=True)
print('klaar', flush=True)
