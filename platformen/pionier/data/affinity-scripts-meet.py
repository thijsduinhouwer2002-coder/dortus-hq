"""Herhaalmeting Affinity-scripts (Noor). Draai: python3 data/affinity-scripts-meet.py
Telt de community-registry van JiriKrblich (scripts, makers, categorieen) en de sterren
en downloads van de Script Manager via shields.io. Schrijft data/affinity-scripts-<datum>.json.
Vergelijk met affinity-scripts-2026-11-08.json."""
import json, collections, urllib.request, datetime, os

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "dortus-meting"})
    return json.load(urllib.request.urlopen(req, timeout=30))

reg = get("https://raw.githubusercontent.com/JiriKrblich/Affinity-Community-Scripts/main/registry.json")
s = reg["scripts"]
uit = {
    "datum": datetime.date.today().isoformat(),
    "registry_last_updated": reg.get("last_updated"),
    "scripts": len(s),
    "makers": len({x.get("author") for x in s}),
    "categorieen": collections.Counter(x.get("category") for x in s).most_common(),
    "top_makers": collections.Counter(x.get("author") for x in s).most_common(10),
}
for naam, url in [
    ("manager_sterren", "https://img.shields.io/github/stars/JiriKrblich/Affinity-script-manager.json"),
    ("manager_downloads", "https://img.shields.io/github/downloads/JiriKrblich/Affinity-script-manager/total.json"),
    ("registry_sterren", "https://img.shields.io/github/stars/JiriKrblich/Affinity-Community-Scripts.json"),
]:
    try:
        uit[naam] = get(url)["value"]
    except Exception as e:
        uit[naam] = f"fout: {e}"
pad = os.path.join(os.path.dirname(__file__), f"affinity-scripts-{uit['datum']}.json")
json.dump(uit, open(pad, "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: uit[k] for k in ("scripts", "makers", "manager_sterren", "manager_downloads")}))
