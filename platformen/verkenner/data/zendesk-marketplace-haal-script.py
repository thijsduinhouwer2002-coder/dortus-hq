# Vera 16 nov 2026: haalt alle apps uit de open API van de Zendesk Marketplace en schrijft een smalle jsonl.
# Gebruik: python3 -I zendesk-marketplace-haal-script.py uit.jsonl
import json,sys,urllib.request
u="https://marketplace.zendesk.com/api/v2/apps.json"
d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"dortus-verkenner"}),timeout=120))
with open(sys.argv[1],"w") as f:
    for x in d["apps"]:
        f.write(json.dumps({k:x.get(k) for k in ["id","name","author_name","created_at","date_published","installation_count","paid","marketing_only","products","categories"]}|{"rating_n":x["rating"]["total_count"],"rating_avg":x["rating"]["average"],"plans":[(p["amount"],p["plan_type"],p["cost_type"]) for p in x["plans"]],"third_party_pricing":(x.get("third_party_pricing") or {}).get("has_third_party_pricing")},ensure_ascii=False)+"\n")
print(len(d["apps"]),"apps")
