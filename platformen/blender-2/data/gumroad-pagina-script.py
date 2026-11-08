# Ronde 3: leest per Gumroad-productpagina de teller sales_count (alleen als de maker die toont) en de beschrijving-samenvatting.
import json, re, sys, time, html, urllib.request
def haal(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (dortus-onderzoek)"})
    t = html.unescape(urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace"))
    m = re.search(r'"sales_count":(\d+|null)', t); f = re.search(r'"free_sales":(true|false)', t)
    return {"sales_count": m.group(1) if m else None, "free_sales": f.group(1) if f else None}
for url in sys.argv[1:]:
    try: print(json.dumps({"url": url, **haal(url)}))
    except Exception as e: print(json.dumps({"url": url, "fout": str(e)}))
    time.sleep(0.8)
