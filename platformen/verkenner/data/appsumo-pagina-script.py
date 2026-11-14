# Leest productpagina's van AppSumo en haalt de verkoopteller (current_purchases) en andere velden uit __NEXT_DATA__.
# Gebruik: python3 -I appsumo-pagina-script.py slugs.txt uit.jsonl
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
slugs = [s.strip() for s in open(sys.argv[1]) if s.strip()]
def haal(slug):
    url = f"https://appsumo.com/products/{slug}/"
    for poging in range(3):
        try:
            h = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Dortus verkenner)"}), timeout=60).read().decode("utf-8", "replace")
            m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
            d = json.loads(m.group(1))["props"]["pageProps"]["deal"]
            tax = d.get("taxonomy") or {}
            r = {"slug": slug, "naam": d.get("public_name"), "verkocht": d.get("current_purchases"),
                 "soort": d.get("listing_type"), "marketplace": d.get("is_marketplace"),
                 "start": (d.get("dates") or {}).get("start_date"), "eind": (d.get("dates") or {}).get("end_date"),
                 "prijs": d.get("price"), "status": d.get("deal_status"), "gratis": d.get("is_free"),
                 "reviews": (d.get("deal_review") or {}).get("review_count"), "rating": (d.get("deal_review") or {}).get("average_rating"),
                 "comments": (d.get("deal_comment") or {}).get("comment_count"),
                 "plannen": d.get("plan_stack_count"), "product_url": d.get("product_url"),
                 "categorie": json.dumps(tax)[:300], "founders": json.dumps(d.get("founders"))[:300],
                 "addon": d.get("is_addon"), "labs": d.get("is_labs")}
            time.sleep(0.5)
            return r
        except Exception as e:
            err = str(e); time.sleep(3)
    return {"slug": slug, "fout": err}
with open(sys.argv[2], "w") as uit, ThreadPoolExecutor(3) as ex:
    for i, r in enumerate(ex.map(haal, slugs)):
        uit.write(json.dumps(r) + "\n")
        if i % 50 == 0: print(i, file=sys.stderr, flush=True)
