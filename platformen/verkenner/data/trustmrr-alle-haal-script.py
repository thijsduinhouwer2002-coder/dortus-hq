# Vera 8 nov 2026: haalt alle TrustMRR-profielen (.md, robots.txt staat dat toe voor andere bots dan Googlebot)
# en schrijft per profiel één compacte regel. Hervatbaar: slugs die al in het uitbestand staan worden overgeslagen.
# Gebruik: python3 -I trustmrr-alle-haal-script.py uit.jsonl <max_seconden>
import re, sys, json, subprocess, time, os, concurrent.futures as cf
out, MAXS = sys.argv[1], int(sys.argv[2]); t0 = time.time()
UA = 'Mozilla/5.0 (dortus-verkenner)'
def curl(u): return subprocess.run(['curl', '-s', '--max-time', '20', '-A', UA, u], capture_output=True, text=True).stdout
slugs = re.findall(r'/startup/([^<]+)</loc>', curl('https://trustmrr.com/startup-sitemap.xml'))
klaar = set()
if os.path.exists(out):
    for l in open(out):
        try: klaar.add(json.loads(l)['slug'])
        except Exception: pass
todo = [s for s in slugs if s not in klaar]
print('sitemap', len(slugs), 'al klaar', len(klaar), 'te doen', len(todo), flush=True)
def num(s): return float(s.replace('$', '').replace(',', ''))
def haal(slug):
    if time.time() - t0 > MAXS: return None
    t = curl(f'https://trustmrr.com/startup/{slug}.md'); time.sleep(0.3)
    if '## Profile' not in t: return None
    g = lambda k: (re.search(r'\n- ' + k + r': (.*)', t) or [None, ''])[1].strip()
    r = dict(slug=slug, name=g('Name'), desc=g('Description')[:400], founded=g('Founded date'), web=g('Website')[:200],
             provider=g('Verified payment provider API source'))
    for p, k in [('Last 30 days', 'd30'), ('Last 3 months', 'm3'), ('Last 12 months', 'm12'), ('All time', 'tot')]:
        m = re.search(r'\| ' + p + r' \| (\$[\d,\.]+)', t); r[k] = num(m[1]) if m else None
    return r
n = 0
with cf.ThreadPoolExecutor(4) as ex, open(out, 'a') as f:
    for r in ex.map(haal, todo):
        if r: f.write(json.dumps(r, ensure_ascii=False) + '\n'); n += 1
print('nieuw', n, 'tijd', int(time.time() - t0), flush=True)
