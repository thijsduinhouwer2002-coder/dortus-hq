#!/usr/bin/env python3
"""Herhaalmeting World App mini apps (Noor). Leest alleen openbare bronnen.
Gebruik: python3 data/worldapp-meet.py  -> schrijft data/worldapp-<datum>.json en drukt een samenvatting af."""
import json, re, statistics, urllib.request, datetime, os
UA = {"User-Agent": "dortus-meting"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode()
m = json.loads(get("https://metrics.worldcoin.org"))
t = get("https://www.miniapps.world/")
u7 = sorted(map(int, re.findall(r'\\?"unique_users_7d\\?":\s*(\d+)', t)), reverse=True)
uit = {
    "datum": datetime.date.today().isoformat(),
    "snapshot": m.get("snapshot_timestamp"),
    "orb_geverifieerd": m.get("n_verifications"),
    "actief_30d": m.get("last_30_days_active_users"),
    "actief_7d": m.get("last_7_days_active_users"),
    "actief_dag": m.get("last_day_active_users"),
    "nieuwe_accounts_7d": m.get("last_7_days_accounts"),
    "mini_apps_goedgekeurd": m.get("total_mini_apps_approved"),
    "mini_apps_in_lijst": len(u7),
    "unieke_gebruikers_7d_som": sum(u7),
    "mediaan_7d": statistics.median(u7) if u7 else None,
    "apps_1000_plus_7d": sum(x >= 1000 for x in u7),
    "top10_7d": u7[:10],
}
p = os.path.join(os.path.dirname(__file__), f"worldapp-{uit['datum']}.json")
json.dump(uit, open(p, "w"), indent=1)
print(json.dumps(uit, indent=1))
print("Teken van herstel: actief_30d twee metingen op rij hoger en orb_geverifieerd weer +100.000 per maand.")
