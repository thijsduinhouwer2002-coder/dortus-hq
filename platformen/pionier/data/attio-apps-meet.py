"""Herhaalmeting Attio App Store (Noor, 9 nov 2026).
Gebruik: python3 -I attio-apps-meet.py attio-apps-<datum>.json [vorige.json]
Haalt https://attio.com/apps op, pakt de app-objecten uit de Next.js-payload
(tellen op app_id, de pagina bevat ook een dubbele zoekindex) en vat samen:
aantal apps, niet-officieel, nieuw per maand (created_at), installs per leeftijd,
en bij een vorig bestand: groei van installs per app."""
import sys, re, json, collections, statistics as st, urllib.request
BIG = 9007199254740991
req = urllib.request.Request("https://attio.com/apps", headers={"User-Agent": "Mozilla/5.0"})
t = urllib.request.urlopen(req, timeout=60).read().decode()
chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', t, re.S)
s = "".join(json.loads('"' + c + '"') for c in chunks)
dec = json.JSONDecoder(); apps = {}
for m in re.finditer(r'\{"app":\{"app_id"', s):
    try:
        o, _ = dec.raw_decode(s, m.start())
    except Exception:
        continue
    a = o["app"]
    if a["app_id"] not in apps or isinstance(a.get("developer_account"), dict):
        apps[a["app_id"]] = a
L = list(apps.values())
json.dump(L, open(sys.argv[1], "w"))
dev = lambda a: a["developer_account"]["title"] if isinstance(a["developer_account"], dict) else "?"
print("apps", len(L), "niet-officieel", sum(not a["is_official"] for a in L))
mon = collections.Counter(a["created_at"][:7] for a in L)
print("nieuw per maand (created_at):", dict(sorted(mon.items())[-8:]))
V = [a for a in L if a["installation_count"] != BIG and not a["is_official"]]
V.sort(key=lambda a: -a["installation_count"])
print("top 15 niet-officieel:")
for a in V[:15]:
    print(" ", a["installation_count"], a["title"], "|", dev(a), "|", a["created_at"][:10])
if len(sys.argv) > 2:
    old = {a["app_id"]: a for a in json.load(open(sys.argv[2]))}
    g = [(a["installation_count"] - old[a["app_id"]]["installation_count"], a["title"]) for a in V if a["app_id"] in old and old[a["app_id"]]["installation_count"] != BIG]
    g.sort(reverse=True)
    print("grootste groei installs sinds vorige meting:", g[:15])
    print("nieuwe apps sinds vorige meting:", [a["title"] for a in L if a["app_id"] not in old])
