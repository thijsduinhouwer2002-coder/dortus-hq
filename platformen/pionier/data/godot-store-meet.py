#!/usr/bin/env python3
"""Herhaalmeting Godot Asset Store (Noor). Haalt alle items via de open API
(store.godotengine.org/api/v1/assets/?page=N, 24 per pagina) en telt totaal, betaald,
items met 5+ en 10+ stemmen. Telt ook nieuwe items per maand via de scroll-sleutel van
de zoekpagina (sort=created_desc, die bevat de aanmaaktijd per blok van 24).
Voegt een regel toe aan godot-store.csv. Gebruik: python3 -I godot-store-meet.py"""
import base64, collections, csv, datetime, html, json, os, re, time, urllib.request

UA = {"User-Agent": "Dortus-onderzoek"}

def get(url, extra=None):
    h = dict(UA, **(extra or {}))
    return urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60).read().decode()

items, p = [], 1
while p < 300:
    try:
        d = json.loads(get(f"https://store.godotengine.org/api/v1/assets/?page={p}"))
    except Exception:
        break
    if not d:
        break
    items += d; p += 1; time.sleep(0.4)

base = "https://store.godotengine.org/search/?sort=created_desc"
url, n, prev, mnd = base, 0, 0, collections.Counter()
for _ in range(300):
    t = get(url, {"HX-Request": "true"})
    n += len(set(re.findall(r'href="/asset/(?!new/)([^"]+)"', t)))
    m = re.findall(r"scroll=([A-Za-z0-9_=-]+)", html.unescape(t))
    if not m:
        break
    tok = m[-1]
    ts = json.loads(base64.urlsafe_b64decode(tok + "=" * (-len(tok) % 4)))["order_by"][0]["value"]
    mnd[datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%Y-%m")] += n - prev
    prev = n; url = base + "&scroll=" + tok; time.sleep(0.4)

rij = {
    "datum": datetime.date.today().isoformat(),
    "totaal": len(items),
    "betaald": sum(1 for x in items if x.get("price_cent", 0) > 0),
    "stemmen_5plus": sum(1 for x in items if x["reviews_score"] >= 5),
    "stemmen_10plus": sum(1 for x in items if x["reviews_score"] >= 10),
    "per_maand": json.dumps(dict(sorted(mnd.items()))),
}
pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "godot-store.csv")
nieuw = not os.path.exists(pad)
with open(pad, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rij))
    if nieuw:
        w.writeheader()
    w.writerow(rij)
print(rij)
