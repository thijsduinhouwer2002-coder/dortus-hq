# Leest alle app-pagina's uit de openbare sitemap van marketplace.autodesk.com (robots.txt staat dit toe)
# en haalt per app: naam, maker, soort, eerste uitgave, prijsplannen, producten. Gebruik: python3 autodesk-haal-script.py <uit.jsonl>
import re, json, sys, urllib.request, concurrent.futures as cf
UA = {"User-Agent": "Mozilla/5.0"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read().decode("utf-8", "replace")
idx = re.findall(r"<loc>([^<]+)</loc>", get("https://marketplace.autodesk.com/sitemap.xml"))
urls = []
for s in idx:
    if "/apps-" in s: urls += re.findall(r"<loc>([^<]+/apps/[^<]+)</loc>", get(s))
urls = sorted(set(urls)); print(len(urls), "apps", file=sys.stderr)
def een(u):
    try:
        s = get(u)
        d = json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', s, re.S).group(1))
        a = d["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]
        naam = re.search(r"<title[^>]*>(.*?)</title>", s, re.S); 
        prod = sorted({p.get("productId") or "" for r in a.get("appReleases", []) for t in r.get("targets", []) for p in (t.get("productInfos") or [])})
        return {"url": u, "naam": naam.group(1).strip() if naam else "", "maker": (a.get("publisherProfile") or {}).get("name"),
                "soort": a.get("appTypeName"), "checkout": a.get("checkoutEnabled"), "eerste": a.get("initialReleaseDate"),
                "laatste": a.get("latestReleaseDate"), "legacy": a.get("legacyAppId"), "producten": prod,
                "prijzen": [{"type": p.get("type"), "bedragen": [(x.get("amount"), x.get("currency")) for x in p.get("prices", [])]} for p in a.get("pricePlans", [])]}
    except Exception as e:
        return {"url": u, "fout": str(e)[:100]}
with open(sys.argv[1], "w") as f, cf.ThreadPoolExecutor(24) as ex:
    for r in ex.map(een, urls): f.write(json.dumps(r) + "\n")
