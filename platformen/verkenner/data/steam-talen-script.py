# Vera 16 nov 2026: reviews per taal voor bureaubladspellen (winkelpagina met ?l=, itemprop reviewCount).
# Alleen openbare winkelpagina's, 1 verzoek per ~1,5 s, stopt bij 429. Gebruik: python3 -I steam-talen-script.py kaart.csv uit.jsonl
import csv, json, re, subprocess, sys, time, os
TALEN = ['english','schinese','tchinese','koreana','japanese','russian','brazilian','german']
kaart, uit = sys.argv[1], sys.argv[2]
r = list(csv.DictReader(open(kaart)))
g = [x for x in r if x['binnenkort']=='False' and x['soort_spel']!='programma of hulpmiddel'
     and x['gratis']=='False' and int(x['reviews_totaal'] or 0) >= 100]
g.sort(key=lambda x: (-int(x['lijkt_op_hats'] or 0), -int(x['reviews_totaal'])))
klaar = set()
if os.path.exists(uit):
    for l in open(uit):
        d = json.loads(l); klaar.add((d['appid'], d['taal']))
for x in g:
    for t in TALEN:
        if (x['appid'], t) in klaar: continue
        res = subprocess.run(['curl','-sS','-m','25','-A','Mozilla/5.0','-b','birthtime=0; wants_mature_content=1',
            '-w','\n%{http_code}', f"https://store.steampowered.com/app/{x['appid']}/?l={t}&cc=us"], capture_output=True, text=True)
        body, _, code = res.stdout.rpartition('\n')
        if code == '429':
            print('429, stop', x['appid'], t, flush=True); sys.exit(2)
        m = re.search(r'itemprop="reviewCount" content="(\d+)"', body)
        v = re.search(r'itemprop="ratingValue" content="(\d+)"', body)
        tips = re.findall(r'data-tooltip-html="([^"]*)"', body)[:3]
        d = {'appid': x['appid'], 'naam': x['naam'], 'taal': t, 'http': code,
             'reviewCount': int(m.group(1)) if m else None, 'ratingValue': int(v.group(1)) if v else None,
             'tooltips': tips, 'reviews_totaal': int(x['reviews_totaal']), 'tijd': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}
        with open(uit, 'a') as f: f.write(json.dumps(d, ensure_ascii=False) + '\n')
        time.sleep(1.5)
print('klaar', flush=True)
