# Vera, 7 nov 2026. Leest openbare templatepagina's van templates.webflow.com (staan in de sitemap,
# robots.txt van templates.webflow.com verbiedt niets) en haalt de templatekaartjes eruit.
# Elk kaartje toont van een (andere) template: goedkeuringsdatum, prijs, maker en soms
# cumulativePurchases en uniqueViewers. We gebruiken NIET de /api/ (robots.txt van webflow.com verbiedt /api/).
# Gebruik: python3 -I webflow-haal-script.py urls.txt uit.jsonl [max]
import sys, re, json, html, subprocess, concurrent.futures as cf

urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
uit = sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else len(urls)
urls = urls[:mx]
rx = re.compile(r'data-props="(\{[^"]*?&quot;templateName&quot;[^"]*\})"')

def haal(u):
    try:
        r = subprocess.run(["curl", "-s", "--compressed", "-m", "40", "-A", "Mozilla/5.0", u],
                           capture_output=True, timeout=60)
        t = r.stdout.decode("utf-8", "replace")
    except Exception:
        return u, []
    kaarten = []
    for m in rx.finditer(t):
        try:
            d = json.loads(html.unescape(m.group(1)))
        except Exception:
            continue
        if "approvalDate" not in d:
            continue
        kaarten.append({k: d.get(k) for k in ("templateName", "templateLink", "priceNumeric", "creatorName",
                        "approvalDate", "popularityScore", "cumulativePurchases", "uniqueViewers", "isFree")})
    return u, kaarten

with open(uit, "a") as f, cf.ThreadPoolExecutor(8) as ex:
    for i, (u, k) in enumerate(ex.map(haal, urls)):
        f.write(json.dumps({"bron": u, "kaarten": k}) + "\n")
        if i % 200 == 0:
            print(i, len(k), flush=True)
