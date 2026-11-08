#!/usr/bin/env python3
"""Haalt alle apps uit de TikTok Shop App Store (openbare portal-API, geen login).
Gebruik: python3 -I data/tiktokshop-apps-meet.py [REGIO=US] [uitvoer.json]
Regio's: US (seller-us.tiktok.com), GB (seller-uk.tiktok.com), JP, BR, MX (seller-jp/br/mx.tiktok.com, sinds 8 nov 20:55), andere via seller-<x>.tiktok.com als ze bestaan.
"""
import json, sys, time, urllib.request, datetime
reg = sys.argv[1] if len(sys.argv) > 1 else "US"
host = {"US": "seller-us.tiktok.com", "GB": "seller-uk.tiktok.com", "JP": "seller-jp.tiktok.com", "BR": "seller-br.tiktok.com", "MX": "seller-mx.tiktok.com"}.get(reg, "seller-eu.tiktok.com")  # EU-markten (DE, FR, IT, ES, IE, NL, BE, AT, PL) via seller-eu
uit = sys.argv[2] if len(sys.argv) > 2 else f"data/tiktokshop-apps-{reg}-{datetime.date.today()}.json"
url = f"https://{host}/api/v2/open/bso/portal/service/search?locale=en&language=en&shop_region={reg}&seller_type=2"
def haal(veld):
    rijen, pagina, tot = [], 1, None
    while True:
        body = {"condition": {"search_text": ""}, "pagination": {"page": pagina, "size": 50}, "sort_option": {"field": veld}, "service_business_type": 2}
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"})
        r = json.load(urllib.request.urlopen(req, timeout=60)); d = r.get("data")
        if d is None:
            print("fout op pagina", pagina, r.get("code"), r.get("message")); break
        tot = d.get("total"); rij = d.get("view_list") or []
        rijen += rij
        if not rij or len(rijen) >= (tot or 0):
            break
        pagina += 1; time.sleep(1)
    return rijen, tot
# Sortering 3 is de standaardvolgorde van de winkel, maar verschuift tijdens het bladeren (dubbele en gemiste apps).
# Sortering 1 is stabiel. Daarom: volgorde van 3 bewaren, dubbele weg, gemiste aanvullen uit 1 (8 nov 21:00).
alles, totaal = haal(3)
gezien = {}
for a in alles: gezien.setdefault(a["service_id"], a)
if len(gezien) < (totaal or 0):
    for a in haal(1)[0]: gezien.setdefault(a["service_id"], a)
alles = list(gezien.values())
json.dump({"gemeten": datetime.datetime.now(datetime.timezone.utc).isoformat(), "regio": reg, "totaal": totaal, "apps": alles}, open(uit, "w"))
print(reg, len(alles), "uniek, API zegt", totaal, "naar", uit)
