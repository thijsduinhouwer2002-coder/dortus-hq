"""Aanvulling Steam desktop-kaart (Vera, 16 nov 2026): de eerste ronde las de Engelse score alleen bij
"for this game", niet bij "for this software", en apps onder 10 reviews tonen geen score.
Leest opnieuw de winkelpagina van uitgebrachte games en programma's zonder Engelse telling.
Gebruik: python3 -I steam-desktop-aanvul-script.py <map met details-*.jsonl> [ids.txt]  (schrijft aanvul.jsonl in die map;
met ids.txt alleen die apps, bijvoorbeeld alleen wat in de kaart valt)
"""
import json, sys, glob, re, time, os, urllib.request
UA = {'User-Agent': 'Mozilla/5.0', 'Cookie': 'birthtime=568022401; lastagecheckage=1-0-1988; wants_mature_content=1'}
m_ = sys.argv[1]; uitp = os.path.join(m_, 'aanvul.jsonl')
klaar = {json.loads(l)['appid'] for l in open(uitp)} if os.path.exists(uitp) else set()
f = open(uitp, 'a')
alleen = {int(x) for x in open(sys.argv[2]).read().split()} if len(sys.argv) > 2 else None
for p in sorted(glob.glob(m_ + '/details-*.jsonl')):
    for l in open(p):
        r = json.loads(l)
        if r.get('type') not in ('game', 'application') or r.get('soon') or 'en_rev' in r or r['appid'] in klaar: continue
        if alleen is not None and r['appid'] not in alleen: continue
        rec = {'appid': r['appid']}
        try:
            h = urllib.request.urlopen(urllib.request.Request(f"https://store.steampowered.com/app/{r['appid']}/?cc=us&l=english", headers=UA), timeout=60).read().decode('utf-8', 'replace')
            m = re.search(r'(\d+)% of the ([\d,]+) user reviews for this (game|software|application|product|video)', h)
            if m: rec['en_pct'] = int(m.group(1)); rec['en_rev'] = int(m.group(2).replace(',', ''))
            else:
                m = re.search(r'([\d,]+) user reviews? for this', h) or re.search(r'reviewCount" content="(\d+)"', h)
                if m: rec['en_rev'] = int(m.group(1).replace(',', ''))
                elif 'No user reviews' in h: rec['en_rev'] = 0
                else:
                    m = re.search(r'>\s*(\d) user reviews?\s*<', h)
                    rec['en_rev'] = int(m.group(1)) if m else 0
                    rec['onzeker'] = not m
        except Exception as e: rec['err'] = str(e)
        f.write(json.dumps(rec) + '\n'); f.flush(); time.sleep(1.0)
print('klaar')
