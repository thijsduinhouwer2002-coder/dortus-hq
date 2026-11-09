"""Productkans Steam Desktop Companion (Vera, 9 nov 2026).
Stap 1: alle apps met label Desktop Companion (tag 1320952) via de openbare zoekpagina, met reviews en % positief.
Stap 2: per app de winkelpagina (labels, korte tekst, makers, recente reviews) en het laatste nieuwsbericht (ISteamNews, open).
Gebruik: python3 -I steam-kans-haal-script.py <uitmap>
"""
import json, re, sys, time, html, urllib.request, urllib.parse, os
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0', 'Cookie': 'birthtime=568022401; lastagecheckage=1-0-1988; wants_mature_content=1'}
def get(u, t=60):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read().decode('utf-8', 'replace')
lijst = os.path.join(out, 'lijst.json')
if not os.path.exists(lijst):
    res = []; start = 0
    while True:
        q = urllib.parse.urlencode({'start': start, 'count': 100, 'tags': 1320952, 'sort_by': 'Released_DESC', 'infinite': 1, 'category1': '998', 'cc': 'us', 'l': 'english', 'ndl': 1})
        d = json.loads(get('https://store.steampowered.com/search/results/?' + q))
        blocks = d['results_html'].split('<a href=')[1:]
        if not blocks: break
        for b in blocks:
            a = re.search(r'data-ds-appid="([\d,]+)"', b); t = re.search(r'<span class="title">(.*?)</span>', b, re.S)
            r = re.search(r'search_released[^>]*>\s*(.*?)\s*</div>', b, re.S)
            rv = re.search(r'data-tooltip-html="([^"]*)"', b); n = 0; pc = None
            if rv:
                tt = html.unescape(rv.group(1))
                m = re.search(r'of the ([\d,]+) user reviews', tt); n = int(m.group(1).replace(',', '')) if m else 0
                m = re.search(r'(\d+)% of', tt); pc = int(m.group(1)) if m else None
            p = re.search(r'data-price-final="(\d+)"', b)
            res.append({'appid': int(a.group(1).split(',')[0]), 'title': html.unescape(t.group(1)) if t else '', 'released': r.group(1) if r else '', 'reviews': n, 'pos': pc, 'price': int(p.group(1)) / 100 if p else None})
        start += 100
        if start >= d['total_count']: break
        time.sleep(1.5)
    json.dump(res, open(lijst, 'w')); print('lijst', len(res))
res = json.load(open(lijst))
det = os.path.join(out, 'details.jsonl')
klaar = set()
if os.path.exists(det):
    klaar = {json.loads(l)['appid'] for l in open(det)}
f = open(det, 'a')
for x in res:
    if x['appid'] in klaar: continue
    a = x['appid']; rec = {'appid': a}
    try:
        h = get(f'https://store.steampowered.com/app/{a}/?cc=us&l=english')
        rec['tags'] = [html.unescape(t.strip()) for t in re.findall(r'class="app_tag"[^>]*>\s*([^<]+?)\s*</a>', h)]
        m = re.search(r'game_description_snippet">\s*(.*?)\s*</div>', h, re.S); rec['short'] = html.unescape(m.group(1)) if m else ''
        m = re.search(r'id="developers_list">(.*?)</div>', h, re.S); rec['dev'] = [html.unescape(d) for d in re.findall(r'>([^<]+)</a>', m.group(1))] if m else []
        m = re.search(r'Publisher:</div>\s*<div class="summary column">(.*?)</div>', h, re.S); rec['pub'] = re.findall(r'>([^<]+)</a>', m.group(1)) if m else []
        m = re.search(r'Recent Reviews:.*?data-tooltip-html="([^"]*)"', h, re.S); rec['recent'] = html.unescape(m.group(1)) if m else ''
        rec['early'] = 'Early Access' in h and 'early_access_header' in h
    except Exception as e: rec['err'] = str(e)
    try:
        n = json.loads(get(f'https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={a}&count=5&maxlength=1&feeds=steam_community_announcements', 30))
        rec['news'] = [i['date'] for i in n.get('appnews', {}).get('newsitems', [])]
    except Exception as e: rec['news_err'] = str(e)
    f.write(json.dumps(rec) + '\n'); f.flush()
    time.sleep(1.2)
print('klaar')
