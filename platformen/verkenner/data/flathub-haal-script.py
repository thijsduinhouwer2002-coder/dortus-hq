# Haalt alle apps van Flathub via de open zoek-API (geen sleutel). Gebruik: python3 -I flathub-haal-script.py uit.jsonl
import json,subprocess,sys
keep=['app_id','name','developer_name','added_at','updated_at','installs_last_month','favorites_count','is_free_license','project_license','main_categories','verification_verified','type']
out=open(sys.argv[1],'w')
for p in range(1,40):
    r=subprocess.run(["curl","-sS","-m","60","-X","POST","-H","Content-Type: application/json","https://flathub.org/api/v2/search","-d",json.dumps({"query":"","hits_per_page":250,"page":p})],capture_output=True,text=True).stdout
    h=json.loads(r).get("hits",[])
    if not h: break
    for a in h: out.write(json.dumps({k:a.get(k) for k in keep})+"\n")
# Daarna: groepeer op maand van added_at, mediaan installs_last_month en aandeel 100+.
# Betalen live? curl https://flathub.org/api/v2/vending/config en per app /api/v2/purchases/storefront-info?app_id=<id> (veld voor prijs?).
