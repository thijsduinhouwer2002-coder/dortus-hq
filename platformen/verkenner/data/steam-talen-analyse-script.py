# Vera 16 nov 2026: analyse van steam-talen-2026-11-16.jsonl. Gebruik: python3 -I steam-talen-analyse-script.py talen.jsonl kaart.csv
import json, sys, csv, statistics as st, collections
TERUG = {'english':'for this game','schinese':'此游戏的','tchinese':'給予此遊戲好評','koreana':'이 게임에 대한',
         'japanese':'このゲームのユーザーレビュー','russian':None,'brazilian':'deste jogo','german':'für dieses Spiel'}
kaart = {x['appid']: x for x in csv.DictReader(open(sys.argv[2]))}
per = collections.defaultdict(dict)
for l in open(sys.argv[1]):
    d = json.loads(l)
    if d['reviewCount'] is None: continue
    per[d['appid']][d['taal']] = d
TALEN = ['english','schinese','tchinese','koreana','japanese','russian','brazilian','german']
rows = []
for a, t in per.items():
    if not all(x in t for x in TALEN): continue
    alle = max([int(kaart[a]['reviews_totaal'])] + [v['reviewCount'] for v in t.values()])
    r = {'appid': a, 'naam': kaart[a]['naam'], 'alle': alle, 'lijkt': kaart[a]['lijkt_op_hats'],
         'soort': kaart[a]['soort_spel'], 'talen_spel': kaart[a]['talen']}
    for x in TALEN:
        v = t[x]; c = v['reviewCount']
        tip = next((s for s in v['tooltips'] if f"{c:,}" in s or str(c) in s), '')
        terug = (TERUG[x] and TERUG[x] in tip) or abs(c-alle) <= max(3, alle*0.01)
        r[x] = None if terug else c
        r[x+'_pos'] = None if terug else v['ratingValue']
    rows.append(r)
print('spellen compleet:', len(rows))
for x in TALEN:
    shown = [r for r in rows if r[x] is not None]
    aand = [r[x]/r['alle'] for r in shown]
    print(f"{x:10s} eigen score bij {len(shown):3d}/{len(rows)}; aandeel waar getoond: mediaan {st.median(aand)*100:.0f}% ; min getoond {min((r[x] for r in shown), default=0)}" if shown else x)
# Ondergrens per spel: som van getoonde talen; rest = niet-getoonde talen samen
som = collections.Counter(); tot = 0
for r in rows:
    tot += r['alle']
    for x in TALEN:
        if r[x] is not None: som[x] += r[x]
print('gewogen aandeel (som getoond / som alle reviews, ondergrens):')
for x in TALEN: print(f"  {x:10s} {som[x]/tot*100:5.1f}%")
print(f"  rest (niet getoond of andere taal) {(tot-sum(som.values()))/tot*100:.1f}%")
# Engels-aandeel per spel en Chinees
for r in sorted(rows, key=lambda r: -r['alle']):
    sc = (r['schinese'] or 0) + (r['tchinese'] or 0)
    def p(v): return '-' if v is None else f"{v/r['alle']*100:.0f}%"
    print(f"{r['naam'][:32]:32s} {r['alle']:6d} lijkt{r['lijkt']} en {p(r['english'])} zh {p(r['schinese'])}/{p(r['tchinese'])} ko {p(r['koreana'])} ja {p(r['japanese'])} ru {p(r['russian'])} br {p(r['brazilian'])} de {p(r['german'])} | pos en {r['english_pos']} zh {r['schinese_pos']} | zh-in-spel {'Simplified Chinese' in r['talen_spel']}")
json.dump(rows, open('/dev/stdout' if len(sys.argv)<4 else sys.argv[3],'w'), ensure_ascii=False) if len(sys.argv)>3 else None
