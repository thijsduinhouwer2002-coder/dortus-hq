#!/usr/bin/env python3
"""Leest voor een lichting Shopware-extensies het prijsblok opnieuw (tussen 'Downloads:' en 'Compatible with:').
Gebruik: python3 shopware-prijs-script.py alle.jsonl van(YYYY-MM-DD) tot(YYYY-MM-DD) uit.jsonl"""
import sys, json, re, html, urllib.request, datetime, concurrent.futures as cf, time
UA = "Mozilla/5.0 (compatible; DortusResearch/1.0)"
van, tot = [datetime.date.fromisoformat(x) for x in sys.argv[2:4]]
def dt(s):
    try: return datetime.datetime.strptime(s, '%d %B %Y').date()
    except: return None
D = [json.loads(l) for l in open(sys.argv[1])]
D = [d for d in D if not d.get('fout') and dt(d.get('publicatie') or '') and van <= dt(d['publicatie']) <= tot]
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=40).read().decode('utf-8','replace')
        except Exception: time.sleep(3)
def f(d):
    s = get(d['url']) or ''
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    L = [l.strip() for l in html.unescape(re.sub(r"<[^>]+>", "\n", t)).split("\n") if l.strip()]
    try:
        a = L.index("Downloads:"); b = L.index("Compatible with:", a)
        blok = L[a+2:b]
    except ValueError: blok = []
    blok = [x for x in blok if x not in ("Skip image gallery", "Watch video") and len(x) < 80]
    d['prijsblok'] = blok
    tx = " | ".join(blok)
    if re.search(r"\bFree\b|€0\.00", tx) and "€" not in tx.replace("€0.00", ""): d['model'] = 'gratis'
    elif "/month" in tx or "Monthly" in tx or "/year" in tx: d['model'] = 'huur'
    elif "€" in tx: d['model'] = 'eenmalig'
    else: d['model'] = 'onbekend'
    m = re.findall(r"€([\d,]+\.\d\d)\*?\s*\|\s*/month", tx)
    d['per_maand'] = float(m[-1].replace(',', '')) if m else None
    return d
with cf.ThreadPoolExecutor(8) as ex, open(sys.argv[4], 'w') as out:
    for d in ex.map(f, D): out.write(json.dumps(d, ensure_ascii=False) + "\n")
print(len(D), file=sys.stderr)
