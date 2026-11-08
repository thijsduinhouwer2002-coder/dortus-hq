#!/usr/bin/env python3
"""Meting Cfx Marketplace (marketplace.cfx.re). Alleen lezen, max ~1.5 verzoek/s.
Gebruik: python3 -I data/cfx-marketplace-meet.py  -> schrijft data/cfx-marketplace-<datum>/*.json (±4 minuten)
"""
import json, re, time, os, sys, urllib.request, datetime, collections

BASE = 'https://marketplace.cfx.re'
UA = 'Mozilla/5.0 (X11; Linux x86_64) Chrome/130 Safari/537.36'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cfx-marketplace-' + datetime.date.today().isoformat())
os.makedirs(OUT, exist_ok=True)
PLATFORMS = ['fivem', 'redm', 'rdr2-sp', 'gta5-sp']
CATS = ['maps', 'scripts', 'character', 'clothing', 'vehicles', 'misc', 'animations', 'weapons']

def get(url, data=None, headers=None):
    time.sleep(0.7)
    h = {'User-Agent': UA}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf-8', 'replace')

def rsc(html):
    parts = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', html, re.S)
    return ''.join(json.loads('"' + p + '"') for p in parts)

def meta_total(path):
    s = rsc(get(BASE + path))
    m = re.search(r'"meta":(\{[^}]*\})', s)
    return json.loads(m.group(1))['total'] if m else None

def save(name, obj):
    with open(os.path.join(OUT, name), 'w') as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)

# 1. sitemap
sm = get(BASE + '/sitemap.xml')
entries = re.findall(r'<loc>([^<]*)</loc>\s*<lastmod>([^<]*)</lastmod>', sm)
pk_lastmod = {re.search(r'/packages/(\d+)', u).group(1): lm for u, lm in entries if '/packages/' in u}
sm_creators = [u.split('/creators/')[1] for u in re.findall(r'<loc>([^<]*)</loc>', sm) if '/creators/' in u]
discover_paths = sorted({u.replace(BASE, '') for u, _ in entries if '/discover' in u})
save('sitemap.json', {'packages_lastmod': pk_lastmod, 'creators': sm_creators, 'discover': discover_paths})

# 2. makers
s = rsc(get(BASE + '/creators'))
creators = [dict(zip(['tebexProjectId', 'name', 'downloadCount', 'slug', 'cfxUserId', 'approvedPackageCount'], (int(a), b, int(c), d, int(e), int(f))))
            for a, b, c, d, e, f in re.findall(r'\{"tebexProjectId":(\d+),"avatarUrl":"[^"]*","name":"([^"]*)","downloadCount":(\d+),"slug":"([^"]*)","cfxUserId":(\d+),"approvedPackageCount":(\d+)\}', s)]
save('creators.json', creators)

# 3. tellingen per categorie/subcategorie/platform
totals = {}
for p in ['/discover'] + discover_paths:
    if p in totals: continue
    totals[p] = meta_total(p)
for c in [''] + ['/' + c for c in CATS]:
    for pf in PLATFORMS:
        totals[f'/discover{c}?tag__{pf}__platform=true'] = meta_total(f'/discover{c}?tag__{pf}__platform=true')
for extra in ['price__free=true', 'type__subscription=true', 'bundle__bundle=true',
              'tag__qbcore__framework=true', 'tag__esx__framework=true', 'tag__qbox__framework=true',
              'tag__standalone__framework=true', 'tag__vorp-core__framework=true', 'tag__rsg-core__framework=true']:
    totals['/discover?' + extra] = meta_total('/discover?' + extra)
save('totals.json', totals)

# 4. alle items via server-action loadProductsPage (volgorde 'newest' = recent toegevoegd)
html = get(BASE + '/discover')
s = rsc(html)
i = s.find('"filterItems":')
filters = json.JSONDecoder().raw_decode(s[i + len('"filterItems":'):])[0]
action = None
for c in sorted(set(re.findall(r'/_next/static/chunks/[A-Za-z0-9_.-]+\.js', html))):
    m = re.search(r'createServerReference\)\("([0-9a-f]+)"[^)]*"loadProductsPage"', get(BASE + c))
    if m: action = m.group(1); break
print('action', action, file=sys.stderr)

def load_page(page, flt):
    body = json.dumps(['newest', page, flt]).encode()
    t = get(BASE + '/discover', data=body, headers={'next-action': action, 'accept': 'text/x-component',
                                                     'content-type': 'text/plain;charset=UTF-8'})
    line = [l for l in t.split('\n') if l.startswith('1:')][0][2:]
    return json.loads(line)

def all_items(flt):
    out, page, last = [], 1, 1
    while page <= last:
        d = load_page(page, flt)
        last = d['meta']['last_page']
        out += d['data']
        page += 1
    return out

items = all_items(filters)
for rank, it in enumerate(items):
    it['rank_newest'] = rank
    for k in ('image', 'images', 'bundleImages', 'blurDataURL'): it.pop(k, None)
    it['sitemap_lastmod'] = pk_lastmod.get(str(it['id']))
plat_ids = {}
for pf in ['fivem', 'redm']:
    f2 = json.loads(json.dumps(filters))
    for o in f2[0]['options']:
        if o['id'] == f'tag__{pf}__platform': o['value'] = True
    plat_ids[pf] = [x['id'] for x in all_items(f2)]
for it in items:
    it['platforms'] = [pf for pf in plat_ids if it['id'] in set(plat_ids[pf])]
save('items.json', items)

# samenvatting
cnt = collections.Counter(c for it in items for c in it['categoryLabels'])
summary = {'measured_at': datetime.datetime.utcnow().isoformat() + 'Z', 'items': len(items),
           'creators_with_items': len(creators), 'creators_in_sitemap': len(sm_creators),
           'per_category_from_items': cnt, 'platform_counts': {k: len(v) for k, v in plat_ids.items()},
           'sum_downloads': sum(c['downloadCount'] for c in creators)}
save('summary.json', summary)
print(json.dumps(summary, indent=1))
