#!/usr/bin/env python3
"""Leest alle Shopware Store-pagina's (Engels) uit de sitemap en haalt per extensie:
naam, maker, downloads, rating, reviews, publicatiedatum, laatste update, compatibiliteit, prijs.
Gebruik: python3 shopware-haal-script.py uit.jsonl   (robots.txt staat alles toe)"""
import sys, re, html, json, gzip, urllib.request, concurrent.futures as cf, time
UA = "Mozilla/5.0 (compatible; DortusResearch/1.0)"
def get(u, tries=3):
    for i in range(tries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=40)
            b = r.read()
            return gzip.decompress(b) if u.endswith('.gz') else b
        except Exception as e:
            time.sleep(2 + i * 3)
    return None
idx = get("https://store.shopware.com/en/sitemap.xml").decode()
urls = []
for sm in re.findall(r"<loc>([^<]+\.xml\.gz)</loc>", idx):
    urls += re.findall(r"<loc>([^<]+)</loc>", get(sm).decode())
seen, todo = set(), []
for u in urls:
    m = re.search(r"/en/([a-z]+[0-9]+)(m12|m|f)/", u)
    if not m: continue
    key = m.group(1) + ('f' if m.group(2) == 'f' else 'm')
    if key in seen: continue
    seen.add(key); todo.append(u)
print(len(urls), "urls,", len(todo), "uniek", file=sys.stderr)
def after(L, k):
    return L[L.index(k) + 1] if k in L and L.index(k) + 1 < len(L) else None
def parse(u):
    b = get(u)
    if not b: return {"url": u, "fout": True}
    s = b.decode("utf-8", "replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    L = [l.strip() for l in html.unescape(re.sub(r"<[^>]+>", "\n", t)).split("\n") if l.strip()]
    d = {"url": u}
    try:
        i = L.index("by"); d["naam"] = L[i - 1]; d["maker"] = L[i + 1]
    except ValueError: pass
    d["downloads"] = after(L, "Downloads:")
    d["rating"] = after(L, "Rating:")
    m = re.search(r"Reviews\s*\((\d+)\)", "\n".join(L).replace("Reviews\n(", "Reviews ("))
    d["reviews"] = int(m.group(1)) if m else None
    d["publicatie"] = after(L, "Publication date:")
    d["update"] = after(L, "Latest update:")
    d["compat"] = after(L, "Compatible with:")
    d["categorie"] = after(L, "Category:")
    d["premium"] = "Premium Extension" in L
    d["partnerstatus"] = after(L, "Partner Status") and L[L.index("Partner Status") + 2] if "Partner Status" in L else None
    d["partner_sinds"] = after(L, "Partner since:")
    d["partner_ext"] = after(L, "Extensions:")
    pr = [l for l in L[:L.index("Description")] if l.startswith("€")] if "Description" in L else []
    d["prijzen"] = pr[:6]
    d["maand"] = "Monthly" in L or "/month" in L
    d["gratis"] = "Free" in L[:L.index("Description")] if "Description" in L else None
    return d
out = open(sys.argv[1], "w")
with cf.ThreadPoolExecutor(10) as ex:
    for n, d in enumerate(ex.map(parse, todo)):
        out.write(json.dumps(d, ensure_ascii=False) + "\n")
        if n % 500 == 0: print(n, file=sys.stderr, flush=True)
