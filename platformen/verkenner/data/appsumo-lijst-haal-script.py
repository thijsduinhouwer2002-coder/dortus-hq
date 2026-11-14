# Haalt alle deals van AppSumo via de open lijst-API (dezelfde die de site gebruikt).
# Gebruik: python3 -I appsumo-lijst-haal-script.py uit.jsonl [startpagina]
# Let op: elke pagina van 100 duurt ±12 seconden, alles ±10 minuten.
import json, sys, time, urllib.request
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
uit = open(sys.argv[1], "a" if start > 1 else "w")
page, tot = start, None
while True:
    url = f"https://appsumo.com/api/v2/deals/?per_page=100&page={page}"
    for poging in range(3):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Dortus verkenner)"}), timeout=60))
            break
        except Exception as e:
            time.sleep(5)
    tot = d["meta"]["total_pages"]
    for x in d["deals"]:
        r = {k: x.get(k) for k in ["id","slug","public_name","is_marketplace","price","default_price","original_price","is_free","is_addon","is_labs","browse_deal_status","has_ended","product_url","dates","deal_review","unique_plan_types","partner_user_ids"]}
        r["taxonomy"] = x.get("taxonomy")
        uit.write(json.dumps(r) + "\n")
    print(page, tot, file=sys.stderr)
    if page >= tot: break
    page += 1
    time.sleep(1)
