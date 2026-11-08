#!/usr/bin/env python3
"""Herhaalmeting Android XR (Noor): installs van XR-apps op Google Play als maat voor het aantal headsets.
Gebruik: python3 androidxr-meet.py  -> voegt regels toe aan androidxr.csv"""
import re, urllib.request, datetime, csv, os
APPS = {
 "com.google.android.apps.immersiveviewxr": "Immersive View (Google, maat voor headsets)",
}
def installs(pkg):
    req = urllib.request.Request(f"https://play.google.com/store/apps/details?id={pkg}&hl=en_US&gl=US", headers={"User-Agent": "Mozilla/5.0"})
    h = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    m = re.search(r'\[\[\["([\d,]+\+?)"\],(\d+),(\d+),"', h) or re.search(r'"(\d[\d,]*\+?)",(\d{3,}),(\d{3,})', h)
    return m.groups() if m else ("?", "?", "?")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "androidxr.csv")
new = not os.path.exists(out)
with open(out, "a", newline="") as f:
    w = csv.writer(f)
    if new: w.writerow(["datum", "pakket", "naam", "label", "installs_afgerond", "installs_exact"])
    for p, n in APPS.items():
        lab, a, b = installs(p)
        w.writerow([datetime.date.today().isoformat(), p, n, lab, a, b]); print(p, lab, a, b)
