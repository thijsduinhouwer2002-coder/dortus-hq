# Vera 8 nov 2026: haalt de lage reviews (1 en 2 sterren) van gekozen Superhive-add-ons.
# De reviewlijst op /ratings staat op sterren (hoog naar laag), daarna op datum, 10 per pagina.
# Daarom de laatste pagina's lezen tot er geen 1 of 2 sterren meer bij komen.
# Gebruik: python3 -I superhive-lage-reviews-script.py top600.jsonl uit.jsonl <min_verkoop> <min_aandeel_laag>
import re, sys, json, subprocess, math, html, time
src, out, MINV, MINL = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
UA = 'Mozilla/5.0 (dortus-verkenner)'
def curl(u):
    return subprocess.run(['curl', '-sL', '--max-time', '30', '-A', UA, u], capture_output=True, text=True).stdout
def n(s):
    m = re.match(r'([\d,]+)', s or ''); return int(m.group(1).replace(',', '')) if m else 0
def reviews(t):
    rs = []
    for b in re.split(r'<li class="message-item', t)[1:]:
        sr = re.search(r'star-ratings">(.*?)</div>', b, re.S)
        ag = re.search(r'small">\s*([^<]+?)\s*<', b)
        body = b.split('</div>', 1)[0]
        tekst = re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', b[sr.end():] if sr else b))
        rs.append({'ster': sr.group(1).count('fa fa-star"') if sr else None, 'leeftijd': ag.group(1) if ag else None,
                   'tekst': html.unescape(tekst).strip()[:400]})
    return rs
with open(out, 'w') as f:
    for l in open(src):
        r = json.loads(l); d = r['verdeling_5_tot_1']
        if len(d) < 5 or r['aantal'] < 15 or n(r['sales']) < MINV or d[3] + d[4] < MINL: continue
        pages = math.ceil(r['aantal'] / 10); laag = []
        for p in range(pages, 0, -1):
            rs = reviews(curl(f"https://superhivemarket.com/products/{r['slug']}/ratings?page={p}")); time.sleep(0.4)
            nieuw = [x for x in rs if x['ster'] is not None and x['ster'] <= 2]
            laag += nieuw
            if rs and min(x['ster'] or 5 for x in rs) > 2: break
        f.write(json.dumps({'slug': r['slug'], 'sales': r['sales'], 'aantal': r['aantal'], 'verdeling_5_tot_1': d, 'laag': laag}, ensure_ascii=False) + '\n')
        print(r['slug'], len(laag), flush=True)
