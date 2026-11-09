"""Analyse productkans Steam Desktop Companion (Vera, 9 nov 2026).
Deelt elke app in soorten in (op labels plus woorden in titel en korte tekst; een app kan in meer soorten vallen)
en geeft per soort: aantal, betaald, reviews, de top 3 met % positief en laatste nieuwsbericht.
Gebruik: python3 -I steam-kans-analyse-script.py <uitmap>
"""
import json, sys, statistics as st, datetime as dt, re
out = sys.argv[1]
L = {x['appid']: x for x in json.load(open(out + '/lijst.json'))}
D = {}
for l in open(out + '/details.jsonl'):
    r = json.loads(l); D[r['appid']] = r
NU = dt.date(2026, 11, 9)
def pd(s):
    for f in ('%b %d, %Y', '%d %b, %Y'):
        try: return dt.datetime.strptime(s, f).date()
        except: pass
    return None
SOORT = {
    'focus/productiviteit': (['Time Management', 'Productivity', 'Utilities'], r'focus|pomodoro|productiv|study|to-?do|task|timer|work session|habit'),
    'huisdier/dier': (['Cats', 'Dog', 'Pets', 'Animals', 'Birds'], r'\bpets?\b|\bcats?\b|kitten|\bdogs?\b|puppy|hamster|bird|animal|creature|critter|axolotl|frog|duck'),
    'boerderij/tuin/planten': (['Farming', 'Farming Sim', 'Gardening'], r'farm|garden|plant|crop|grow|flower|greenhouse|bonsai'),
    'vissen/aquarium': (['Fishing'], r'fish|aquarium|\bpond\b|ocean|sea\b'),
    'idle-rpg/gevecht': (['Auto Battler', 'RPG', 'Dungeon Crawler', 'Action RPG', 'Party-Based RPG', 'Roguelike', 'Tower Defense'], r'dungeon|battle|hero|monster|rpg|slay|loot|tower defen'),
    'fabriek/mijnbouw/bouwen': (['Automation', 'City Builder', 'Base Building', 'Mining', 'Colony Sim'], r'factory|mine|mining|automat|build (a|your)|city|colony|village|town'),
    'kamer/inrichten': (['Decorating', 'Interior Decoration', 'Design & Illustration'], r'decorat|room|cozy space|furnish|diorama'),
    'muziek/lofi/sfeer': (['Music', 'Ambient', 'Soundtrack'], r'lofi|lo-fi|music|ambient|ambience|rain sounds|playlist|radio'),
    'anime/ai-chat/vtuber': (['Anime', 'Dating Sim', 'Visual Novel', 'Sexual Content', 'Nudity', 'Mature'], r'\bai\b|chat|waifu|girlfriend|anime|vtuber|live2d|assistant'),
    'toetsen/klikken/muis': ([], r'keyboard|typing|click|mouse|keystroke|bongo|cursor|taskbar'),
}
def soorten(a):
    x = L[a]; d = D.get(a, {}); tags = set(d.get('tags', [])); txt = (x['title'] + ' ' + d.get('short', '')).lower()
    s = [k for k, (tg, rx) in SOORT.items() if tags & set(tg) or re.search(rx, txt)]
    return s or ['overig']
def laatste(a):
    n = D.get(a, {}).get('news') or []
    return dt.date.fromtimestamp(max(n)) if n else None
rij = []
for a, x in L.items():
    r = pd(x['released'])
    if not r or r > NU: continue
    rij.append(dict(appid=a, title=x['title'], rel=r, rev=x['reviews'], pos=x['pos'], price=x['price'] or 0, s=soorten(a), last=laatste(a),
                    dev=D.get(a, {}).get('dev', []), pub=D.get(a, {}).get('pub', []), recent=D.get(a, {}).get('recent', ''), early=D.get(a, {}).get('early')))
print('uitgekomen apps', len(rij), 'met details', sum(1 for x in rij if x['appid'] in D))
def q(v, p):
    v = sorted(v); return v[int(p * (len(v) - 1))] if v else 0
print('\nsoort | apps | betaald | betaald 2026 | betaald 2026 mediaan rev | 10+ | 100+ | som reviews betaald | top 3 betaald (reviews, %pos, uit, laatste nieuws, maker)')
for k in list(SOORT) + ['overig']:
    g = [x for x in rij if k in x['s']]; b = [x for x in g if x['price'] > 0]
    b26 = [x for x in b if x['rel'] >= dt.date(2026, 1, 1) and x['rel'] <= dt.date(2026, 9, 30)]
    v = [x['rev'] for x in b26]
    top = sorted(b, key=lambda x: -x['rev'])[:3]
    ts = '; '.join(f"{x['title'][:28]} ({x['rev']}, {x['pos']}%, {x['rel']:%b %y}, nieuws {x['last'] or '-'}, ${x['price']}, {'/'.join(x['dev'])[:20]})" for x in top)
    print(f"{k} | {len(g)} | {len(b)} | {len(b26)} | {q(v,.5)} | {sum(1 for i in v if i>=10)} | {sum(1 for i in v if i>=100)} | {sum(x['rev'] for x in b)} | {ts}")
json.dump([dict(x, rel=str(x['rel']), last=str(x['last'])) for x in rij], open(out + '/analyse.json', 'w'))
