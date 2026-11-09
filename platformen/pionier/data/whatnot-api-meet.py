"""Herhaalmeting Whatnot Seller API (Noor, 9 nov 2026).

Kijkt of Whatnot de Seller API opent voor apps van derden (partners, OAuth-apps
voor meerdere verkopers, een app-lijst). Draai: python3 -I data/whatnot-api-meet.py
Schrijft niets weg; vergelijk de uitvoer met de stand van 9 nov 2026 in
voorstellen/whatnot-seller-api.md (llms-full.txt ±69.450 tekens, woorden hieronder).
"""
import hashlib
import re
import subprocess

BRONNEN = {
    "docs": "https://developers.whatnot.com/llms-full.txt",
    "blog": "https://blog.teamwhatnot.com/unitedstates/whatnot-seller-api",
}
WOORDEN = [
    "partner", "app directory", "marketplace", "approved your app",
    "third-party", "third party", "vendor", "client secret", "apply",
    "connected app", "installation", "more updates",
]


def lees(url):
    # curl, want Python-urllib krijgt 403 op developers.whatnot.com
    out = subprocess.run(["curl", "-sfL", "--max-time", "60", url],
                         capture_output=True, check=True)
    return out.stdout.decode("utf-8", "replace")


for naam, url in BRONNEN.items():
    try:
        t = lees(url)
    except Exception as e:  # noqa: BLE001
        print(naam, "FOUT", e)
        continue
    tekst = re.sub(r"<[^>]+>", " ", t).lower()
    print(f"{naam}: {len(t)} tekens, sha1 {hashlib.sha1(t.encode()).hexdigest()[:12]}")
    for w in WOORDEN:
        n = tekst.count(w)
        if n:
            print(f"  {w!r}: {n}")
