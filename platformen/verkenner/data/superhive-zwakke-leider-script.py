# Vera 8 nov 2026: betaalde add-ons uit de top van Superhive (op verkoop) met hun beoordelingen.
# Leest per add-on pagina 1 van /ratings: aantal, verdeling 5 tot 1 ster (gemiddelde op de pagina is afgerond,
# daarom zelf uit de verdeling), verkoopteller, publicatie, Blender-versie, prijs, categorie.
# Let op: de reviewlijst staat op sterren (hoog naar laag), daarna op datum. De lage reviews staan dus op de
# laatste pagina's; die haalt superhive-lage-reviews-script.py.
# Gebruik: python3 -I superhive-zwakke-leider-script.py <paginas> uit.jsonl
import re, sys, json, subprocess, time, html, concurrent.futures as cf
P = int(sys.argv[1]); out = sys.argv[2]
UA = 'Mozilla/5.0 (dortus-verkenner)'
def curl(u):
    return subprocess.run(['curl', '-sL', '--max-time', '30', '-A', UA, u], capture_output=True, text=True).stdout
links = []
for p in range(1, P + 1):
    t = curl(f'https://superhivemarket.com/categories/addons/browse?sort_sales=desc&page={p}')
    for l in re.findall(r'href="/products/([^"?/]+)"', t):
        if l not in links: links.append(l)
    time.sleep(0.5)
def plat(h):
    s = re.sub(r'\s+', ' ', re.sub('<[^>]+>', '|', h)); return re.sub(r'(\| ?)+', '|', s)
def info(slug):
    t = curl(f'https://superhivemarket.com/products/{slug}/ratings'); s = plat(t)
    def na(lbl, n=80):
        i = s.find('|' + lbl + '|')
        return s[i + len(lbl) + 2:i + len(lbl) + 2 + n].split('|')[0].strip() if i >= 0 else None
    m = re.search(r'average rating of \|([\d.]+)\|from \|(\d+)\|', s)
    dist = re.findall(r'progress-bar" style="width: (\d+)%', t)[:5]
    cat = re.search(r'\|in \|([^|]+)\|', s)
    pr = re.search(r'"price":(\d+)', t)
    bv = na('Blender Version') or ''
    vers = [float(v) for v in re.findall(r'\b\d\.\d{1,2}\b', bv)]
    return {'slug': slug, 'sales': na('Sales'), 'published': na('Published'), 'blender': bv, 'max_blender': max(vers) if vers else None,
            'prijs': int(pr.group(1)) / 100 if pr else None, 'categorie': cat.group(1).strip() if cat else None,
            'gem': float(m.group(1)) if m else None, 'aantal': int(m.group(2)) if m else 0,
            'verdeling_5_tot_1': [int(d) for d in dist]}
with cf.ThreadPoolExecutor(3) as ex, open(out, 'w') as f:
    for r in ex.map(info, links): f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(len(links))
