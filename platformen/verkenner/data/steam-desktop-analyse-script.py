"""Analyse Steam desktop-kaart (Vera, 16 nov 2026).
Gebruik: python3 -I steam-desktop-analyse-script.py <map met details-*.jsonl> <uit.csv> <uit-analyse.json>
Houdt alleen games en programma's die op het bureaublad draaien: label Desktop Companion, of een winkeltekst
over taakbalk, onderkant of rand van het scherm, bureaublad-huisdier, enz.
"""
import json, sys, glob, re, csv, statistics, datetime, collections
recs = {}
for p in glob.glob(sys.argv[1] + '/details-*.jsonl'):
    for l in open(p):
        r = json.loads(l); recs[r['appid']] = r
import os
if os.path.exists(sys.argv[1] + '/aanvul.jsonl'):
    for l in open(sys.argv[1] + '/aanvul.jsonl'):
        x = json.loads(l)
        if x['appid'] in recs: recs[x['appid']].update({k: v for k, v in x.items() if k != 'err'})
KW = re.compile(r'taskbar|task bar|bottom of (your|the) (screen|desktop|monitor)|desktop (pet|companion|buddy|mate|idle|widget)|'
                r'(on|across|of) your desktop|edge of your screen|corner of your screen|always[- ]on[- ]top|transparent (window|overlay|background)|'
                r'while you (work|study|browse|code)|in the background while', re.I)
def datum(s):
    for f in ('%b %d, %Y', '%d %b, %Y', '%B %d, %Y', '%b %Y', '%B %Y'):  # los jaartal blijft tekst
        try: return datetime.datetime.strptime((s or '').strip(), f).date()
        except Exception: pass
    return None
NU = datetime.date(2026, 11, 16)
def soort(r):
    t = set(r.get('tags', [])); tx = (r.get('name', '') + ' ' + r.get('short', '')).lower()
    if r.get('type') == 'application' or t & {'Utilities', 'Software', 'Productivity', 'Design & Illustration', 'Audio Production', 'Animation & Modeling'} and not t & {'RPG', 'Idler', 'Farming Sim'}:
        return 'programma of hulpmiddel'
    if re.search(r'dungeon|hero|monster|raid|battle|loot', tx) or t & {'Dungeon Crawler', 'Auto Battler', 'Party-Based RPG', 'Action RPG', 'Roguelite', 'RPG', 'Tower Defense'}:
        return 'gevecht, kerker of RPG'
    if re.search(r'farm|garden|plant|crop|harvest', tx) or t & {'Farming Sim', 'Farming', 'Agriculture'}:
        return 'boerderij of tuin'
    if re.search(r'fish', tx) or 'Fishing' in t: return 'vissen'
    if re.search(r'\bpet\b|cat\b|cats\b|dog\b|kitten|tamagotchi|creature|companion', tx) or t & {'Cats', 'Dogs', 'Virtual Pet', 'Cute'}:
        return 'huisdier of maatje'
    if re.search(r'focus|pomodoro|timer|productiv|study|habit|to-do|todo', tx): return 'focus en productiviteit'
    if t & {'Clicker', 'Incremental'} or 'idle' in tx: return 'idle of clicker (overig)'
    return 'overig'
rows = []
for a, r in recs.items():
    if r.get('type') not in ('game', 'application'): continue
    tags = r.get('tags', [])
    label = 'label' in r.get('bron', []) or 'Desktop Companion' in tags
    tekst = bool(KW.search((r.get('short', '') or '') + ' ' + (r.get('about', '') or '')))
    if not (label or tekst): continue
    d = datum(r.get('date'))
    rev = max(r.get('rev') or 0, r.get('en_rev') or 0); en = r.get('en_rev') or 0; pct = r.get('en_pct')
    prijs = (r['price'] / 100) if r.get('price') else (0.0 if r.get('free') else None)
    talen = [x.strip().rstrip('*') for x in (r.get('lang') or '').split(',') if x.strip()]
    tx = (r.get('name', '') + ' ' + r.get('short', '') + ' ' + ' '.join(tags)).lower()
    hats = sum([bool(re.search(r'dungeon|lair|hero|heroes|monster|slime|villain|evil', tx)),
                bool(re.search(r'collect|hat\b|hats|cosmetic|outfit', tx)),
                bool(re.search(r'funny|comedy|humou?r|silly|goofy', tx))])
    rows.append({'appid': a, 'naam': r.get('name'), 'maker': '; '.join(r.get('dev', [])), 'uitgever': '; '.join(r.get('pub', [])),
                 'soort_app': r.get('type'), 'prijs_usd': prijs, 'gratis': bool(r.get('free')), 'releasedatum': d.isoformat() if d else (r.get('date') or ''),
                 'binnenkort': bool(r.get('soon')), 'reviews_totaal': rev if not r.get('soon') else '', 'reviews_engels': en if not r.get('soon') else '',
                 'reviews_engels_positief': round(en * pct / 100) if (en and pct is not None) else '', 'pct_positief': pct if pct is not None else '', 'labels': '; '.join(tags[:12]), 'aantal_talen': len(talen),
                 'talen': '; '.join(talen), 'demo': bool(r.get('demo')), 'dlc_aantal': r.get('dlc', 0),
                 'gevonden_via': 'label Desktop Companion' if label else 'winkeltekst', 'soort_spel': soort(r), 'lijkt_op_hats': hats,
                 'op_desktop_companion_fest': 'nog niet (eerste fest 14 tot 18 jan 2027)', '_d': d})
rows.sort(key=lambda x: -(x['reviews_totaal'] or 0))
with open(sys.argv[2], 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=[k for k in rows[0] if not k.startswith('_')]); w.writeheader()
    for x in rows: w.writerow({k: v for k, v in x.items() if not k.startswith('_')})
uit = rows_rel = [x for x in rows if not x['binnenkort'] and x['_d'] and x['_d'] <= NU]
def emmers(xs):
    n = len(xs) or 1; rv = [x['reviews_totaal'] or 0 for x in xs]
    return {'n': len(xs), '0-9': round(100 * sum(v < 10 for v in rv) / n, 1), '10-99': round(100 * sum(10 <= v < 100 for v in rv) / n, 1),
            '100+': round(100 * sum(v >= 100 for v in rv) / n, 1), '1000+': round(100 * sum(v >= 1000 for v in rv) / n, 1),
            '10000+': round(100 * sum(v >= 10000 for v in rv) / n, 1), 'aantal_100+': sum(v >= 100 for v in rv),
            'aantal_1000+': sum(v >= 1000 for v in rv), 'aantal_10000+': sum(v >= 10000 for v in rv),
            'mediaan_reviews': statistics.median(rv) if rv else None, 'som_reviews': sum(rv)}
A = {'totaal_in_kaart': len(rows), 'uit': len(uit), 'binnenkort': sum(x['binnenkort'] for x in rows),
     'via_label': sum(x['gevonden_via'].startswith('label') for x in rows)}
betaald = [x for x in uit if x['prijs_usd'] and x['prijs_usd'] > 0]; gratis = [x for x in uit if x['prijs_usd'] == 0]
A['alle_uit'] = emmers(uit); A['betaald'] = emmers(betaald); A['gratis'] = emmers(gratis)
A['mediaan_prijs_betaald'] = statistics.median([x['prijs_usd'] for x in betaald])
A['top10_aandeel_reviews'] = round(100 * sum(x['reviews_totaal'] for x in uit[:10]) / max(1, sum(x['reviews_totaal'] or 0 for x in uit)), 1)
A['per_jaar'] = {}
for j in range(2019, 2027):
    xs = [x for x in uit if x['_d'].year == j]
    if xs: A['per_jaar'][j] = emmers(xs)
A['per_maand_2025_2026'] = {}
for x in uit:
    if x['_d'].year >= 2025: A['per_maand_2025_2026'].setdefault(x['_d'].strftime('%Y-%m'), []).append(x)
A['per_maand_2025_2026'] = {m: emmers(v) | {'betaald': sum(1 for y in v if y['prijs_usd']), 'mediaan_betaald': statistics.median([y['reviews_totaal'] for y in v if y['prijs_usd']] or [0])}
                            for m, v in sorted(A['per_maand_2025_2026'].items())}
# kalendermaand van uitbrengen (alle jaren t/m sep 2026, betaald)
km = collections.defaultdict(list)
for x in betaald:
    if x['_d'] <= datetime.date(2026, 9, 30): km[x['_d'].month].append(x)
A['kalendermaand_betaald_tm_sep2026'] = {m: emmers(v) for m, v in sorted(km.items())}
# per soort, betaald en minstens 2 maanden uit (eerlijker)
oud = [x for x in betaald if (NU - x['_d']).days >= 60]
ps = collections.defaultdict(list)
for x in oud: ps[x['soort_spel']].append(x)
A['soort_betaald_2mnd_oud'] = {k: emmers(v) for k, v in sorted(ps.items(), key=lambda kv: -len(kv[1]))}
pb = collections.defaultdict(list)
for x in oud:
    p = x['prijs_usd']; b = '<2' if p < 2 else '2-3,99' if p < 4 else '4-5,99' if p < 6 else '6-7,99' if p < 8 else '8-9,99' if p < 10 else '10+'
    pb[b].append(x)
A['prijs_betaald_2mnd_oud'] = {k: emmers(v) for k, v in pb.items()}
A['demo_betaald_2mnd_oud'] = {'demo': emmers([x for x in oud if x['demo']]), 'geen demo': emmers([x for x in oud if not x['demo']])}
tb = collections.defaultdict(list)
for x in oud: tb['1' if x['aantal_talen'] <= 1 else '2-5' if x['aantal_talen'] <= 5 else '6-10' if x['aantal_talen'] <= 10 else '11+'].append(x)
A['talen_betaald_2mnd_oud'] = {k: emmers(v) for k, v in tb.items()}
A['lijkt_op_hats'] = {str(k): emmers([x for x in uit if x['lijkt_op_hats'] == k]) for k in range(4)}
A['top25'] = [{k: x[k] for k in ('appid', 'naam', 'maker', 'prijs_usd', 'releasedatum', 'reviews_totaal', 'pct_positief', 'soort_spel', 'demo', 'aantal_talen')} for x in uit[:25]]
A['hats_achtig'] = [{k: x[k] for k in ('appid', 'naam', 'maker', 'prijs_usd', 'releasedatum', 'reviews_totaal', 'pct_positief', 'soort_spel', 'lijkt_op_hats', 'labels')}
                    for x in uit if x['lijkt_op_hats'] >= 2][:30]
A['beste_2026_betaald'] = [{k: x[k] for k in ('appid', 'naam', 'maker', 'prijs_usd', 'releasedatum', 'reviews_totaal', 'pct_positief', 'soort_spel', 'demo')}
                           for x in betaald if x['_d'].year == 2026][:25]
json.dump(A, open(sys.argv[3], 'w'), indent=1, default=str, ensure_ascii=False)
print(json.dumps({k: A[k] for k in ('totaal_in_kaart', 'uit', 'binnenkort', 'alle_uit', 'betaald', 'gratis', 'mediaan_prijs_betaald', 'top10_aandeel_reviews')}, indent=1, default=str))
