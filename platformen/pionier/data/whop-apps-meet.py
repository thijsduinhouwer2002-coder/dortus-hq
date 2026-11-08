#!/usr/bin/env python3
"""Herhaalmeting Whop App Store (Noor, 8 nov 2026).
Telt alle openbare apps via https://api.whop.com/api/v1/apps (geen sleutel nodig)
en haalt per app totalInstalls en totalInstallsLast7Days uit de openbare apppagina.
Schrijft whop-apps-<datum>.json naast dit script en drukt een samenvatting af.
Rustig: 1 verzoek per halve seconde."""
import json, re, subprocess, time, datetime, os, statistics

def get(url):
    return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", "Mozilla/5.0", url],
                          capture_output=True).stdout.decode('utf-8','replace')

apps, cursor = [], None
while True:
    url = "https://api.whop.com/api/v1/apps?first=100" + (f"&after={cursor}" if cursor else "")
    d = json.loads(get(url))
    apps += d["data"]
    if not d["page_info"]["has_next_page"]:
        break
    cursor = d["page_info"]["end_cursor"]
    time.sleep(0.5)

rows = []
for a in apps:
    html = get(f"https://whop.com/apps/{a['id']}/")
    t = re.search(r'totalInstalls\\?"?:(\d+)', html)
    w = re.search(r'totalInstallsLast7Days\\?"?:(\d+)', html)
    rows.append({"id": a["id"], "naam": a["name"], "type": a.get("app_type"),
                 "bedrijf": (a.get("company") or {}).get("title"),
                 "installs": int(t.group(1)) if t else None,
                 "installs_7d": int(w.group(1)) if w else None})
    time.sleep(0.5)

dag = datetime.date.today().isoformat()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"whop-apps-{dag}.json")
json.dump(rows, open(out, "w"), indent=1, ensure_ascii=False)
gemeten = [r for r in rows if r["installs"] is not None]
print(f"{dag}: {len(rows)} apps, {len(gemeten)} met installs gemeten")
if gemeten:
    print("mediaan installs:", statistics.median(r["installs"] for r in gemeten))
    print("apps >100 installs:", sum(r["installs"] > 100 for r in gemeten))
    for r in sorted(gemeten, key=lambda r: -r["installs"])[:15]:
        print(f'  {r["installs"]:>8} ({r["installs_7d"]} in 7d)  {r["naam"]}  [{r["bedrijf"]}]')
