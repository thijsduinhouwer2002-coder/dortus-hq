# Vera 15 nov 2026: alle add-ons van Superhive van de laatste 6 maanden (opdracht hoofdchat 15 nov 20:20).
# Leest de lijst op datum (nieuwste eerst) en daarna elke productpagina. Rustig: 1 pagina per 2 seconden,
# alleen openbare pagina's, niet inloggen. Bewaart alleen productgegevens (geen mailadressen).
# Gebruik: python3 -I superhive-6mnd-script.py uit.csv [max_lijstpaginas]
import re, sys, csv, time, html, subprocess, datetime

OUT = sys.argv[1]
MAXP = int(sys.argv[2]) if len(sys.argv) > 2 else 200
UA = 'Mozilla/5.0 (dortus-verkenner; alleen lezen)'
WACHT = 2.0
laatst = [0.0]

def curl(u):
    for poging in range(5):
        tijd = time.time() - laatst[0]
        if tijd < WACHT: time.sleep(WACHT - tijd)
        laatst[0] = time.time()
        r = subprocess.run(['curl', '-sL', '--max-time', '30', '-A', UA, '-w', '\n%{http_code}', u],
                           capture_output=True, text=True)
        s, code = r.stdout.rsplit('\n', 1) if '\n' in r.stdout else ('', r.stdout)
        if code not in ('429', '500', '502', '503', '000'): return s, code
        time.sleep(10 * (poging + 1))
    return s, code

def leeftijd(pub):
    """'3 months ago' -> maanden (benadering, Rails time_ago_in_words)."""
    if not pub: return None
    p = pub.lower()
    if any(w in p for w in ('second', 'minute', 'hour')): return 0.0
    m = re.search(r'(\d+)\s+day', p)
    if m: return int(m.group(1)) / 30.4
    if 'about 1 month' in p or p.startswith('1 month'): return 1.0
    m = re.search(r'(\d+)\s+month', p)
    if m: return float(m.group(1))
    if 'year' in p:
        m = re.search(r'(\d+)\s+year', p); j = int(m.group(1)) if m else 1
        return 12.0 * j + (3 if 'over' in p else 0) + (9 if 'almost' in p else 0) - (12 if 'almost' in p else 0)
    return None

def txt(h): return re.sub(r'\s+', ' ', re.sub('<[^>]+>', '|', h))

def info(slug, pos):
    t, code = curl('https://superhivemarket.com/products/' + slug)
    d = {'positie': pos, 'slug': slug, 'code': code}
    if code != '200': return d
    s = txt(t)
    def na(lbl, n=160):
        i = s.find('|' + lbl + '|')
        if i < 0: return ''
        return re.sub(r'\|+', '|', s[i + len(lbl) + 2:i + len(lbl) + 2 + n]).strip('| ').split('|')[0].strip()
    d['sales'] = na('Sales', 20)
    d['published'] = na('Published', 40)
    d['leeftijd_mnd'] = leeftijd(d['published'])
    d['blender'] = na('Blender Version', 80)
    d['type'] = na('Extension Type', 40)
    m = re.search(r'"price"\s*:\s*"([\d.]+)"', t)
    if m: d['prijs'] = float(m.group(1))
    else:
        m = re.search(r'"price"\s*:\s*(\d+)', t); d['prijs'] = int(m.group(1)) / 100 if m else ''
    m = re.search(r'"offers".{0,400}?"lowPrice"\s*:\s*"?([\d.]+)', t, re.S)
    d['prijs_laag'] = m.group(1) if m else ''
    m = re.search(r'<title>(.*?)</title>', t, re.S)
    d['titel'] = html.unescape(m.group(1)).replace(' - Superhive (formerly Blender Market)', '').strip() if m else ''
    m = re.search(r'<meta name="description" content="([^"]*)"', t)
    d['beschrijving'] = html.unescape(m.group(1))[:250].replace('\n', ' ') if m else ''
    m = re.search(r'"seller":\{"@type":"[A-Za-z]+","name":"([^"]*)"', t)
    d['maker'] = html.unescape(m.group(1)) if m else ''
    c = re.findall(r'href="/categories/([^"?]*)"', t)
    d['cat'] = ';'.join(sorted(x for x in set(c) if c.count(x) == 1 and x not in ('addons',)))
    m = re.search(r'"reviewCount"\s*:\s*"?(\d+)', t); d['ratings'] = int(m.group(1)) if m else 0
    m = re.search(r'"ratingValue"\s*:\s*"?([\d.]+)', t); d['rating'] = m.group(1) if m else ''
    m = re.search(r'(\d+)\s+Items', s); d['items_maker'] = m.group(1) if m else ''
    return d

VELDEN = ['positie', 'slug', 'code', 'titel', 'maker', 'items_maker', 'prijs', 'prijs_laag', 'sales', 'ratings',
          'rating', 'published', 'leeftijd_mnd', 'cat', 'type', 'blender', 'beschrijving', 'gemeten']
links = []
for p in range(1, MAXP + 1):
    t, code = curl(f'https://superhivemarket.com/categories/addons/browse?sort_date=desc&page={p}')
    nieuw = [l for l in dict.fromkeys(re.findall(r'href="/products/([^"?/#]+)"', t)) if l not in links]
    links += nieuw
    print('lijst', p, code, len(links), flush=True)
    if not nieuw: break
    # stop met de lijst zodra we ruim voorbij 6 maanden zijn: controleer de laatste van deze pagina
    if p % 10 == 0:
        d = info(links[-1], len(links))
        print('  peil', p, d.get('published'), flush=True)
        if (d.get('leeftijd_mnd') or 0) >= 8: break

nu = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')
oud = 0
with open(OUT, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=VELDEN); w.writeheader()
    for i, slug in enumerate(links):
        d = info(slug, i + 1); d['gemeten'] = nu
        w.writerow({k: d.get(k, '') for k in VELDEN}); f.flush()
        if i % 100 == 0: print('product', i, d.get('published'), d.get('sales'), flush=True)
        oud = oud + 1 if (d.get('leeftijd_mnd') or 0) >= 7 else 0
        if oud >= 40: print('40 op rij 7+ maanden oud: klaar', flush=True); break
print('klaar', nu, flush=True)
