#!/usr/bin/env python3
"""Meet de Microsoft 365-apps en Copilot-agents in Microsoft Marketplace (Noor, 9 nov 2026).
Stap 1: sitemap_en-us_1..5.xml van marketplace.microsoft.com geeft alle WA-id's (Office/Teams/Copilot).
Stap 2: openbare catalogus-API (api-version 2018-08-01-beta, zonder sleutel) per 30 id's.
Gebruik: python3 -I m365-agents-meet.py <uitvoer.jsonl>   (rustig: 1 verzoek per seconde)"""
import sys, re, json, time, urllib.request, urllib.parse
out = sys.argv[1]
ids = set()
for i in range(1, 6):
    x = urllib.request.urlopen(f"https://marketplace.microsoft.com/sitemap_en-us_{i}.xml", timeout=90).read().decode()
    ids |= {m.upper() for m in re.findall(r'/product/(wa\d+)', x, re.I)}
    time.sleep(2)
ids = sorted(ids)
print(len(ids), "WA-id's", file=sys.stderr)
keep = ['bigId','displayName','publisherDisplayName','publisherId','releaseDate','badges','applicableProducts',
        'appFreeType','hasPrices','pricingTypes','isThirdParty','popularity','categoryIds','longSummary','bigCatLastModifiedDate']
with open(out, 'w') as f:
    for k in range(0, len(ids), 30):
        part = ids[k:k+30]
        flt = "bigId in (" + ",".join(f"'{i}'" for i in part) + ")"
        url = "https://catalogapi.azure.com/products?" + urllib.parse.urlencode({'market':'US','api-version':'2018-08-01-beta','storefront':'any','$filter':flt})
        for poging in range(3):
            try:
                d = json.load(urllib.request.urlopen(url, timeout=60)); break
            except Exception as e:
                print('fout', k, e, file=sys.stderr); time.sleep(5); d = {'items': []}
        for it in d.get('items', []):
            r = {x: it.get(x) for x in keep}
            ed = it.get('enrichedData') or {}
            r['rating'] = ed.get('rating')
            f.write(json.dumps(r) + "\n")
        time.sleep(1)
