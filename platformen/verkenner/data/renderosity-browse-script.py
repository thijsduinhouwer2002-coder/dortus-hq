# Haal Renderosity browse-pagina's op (sorteervolgorde sb), schrijf jsonl met rang, id, maker, prijs, categorie, topverkoper-icoon.
import sys, re, json, time, html, urllib.request
sb, start, end, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
UA = {'User-Agent': 'Mozilla/5.0 (Dortus-verkenner; leest rustig)'}
f = open(out, 'a')
for p in range(start, end + 1):
    url = f'https://www.renderosity.com/marketplace/browse?sb={sb}&results_per_page=120&page={p}&_empty=1'
    for t in range(3):
        try:
            h = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode('utf8', 'ignore'); break
        except Exception as e:
            time.sleep(5); h = ''
    tiles = h.split('rr-mktproduct-tile rr-mktproduct-tile-complete')[1:]
    if not tiles: print('leeg', p); break
    for i, t in enumerate(tiles):
        m = re.search(r'data-gtm_model="([^"]*)"', t)
        if not m: continue
        d = json.loads(html.unescape(m.group(1)))
        d['rang'] = (p - 1) * 120 + i + 1
        d['top'] = 'icon-topseller' in t
        d['elite'] = 'elite-showcase' in t[:300]
        f.write(json.dumps(d) + '\n')
    f.flush(); time.sleep(1)
print('klaar', sb, start, end)
