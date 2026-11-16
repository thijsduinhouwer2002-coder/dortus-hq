#!/usr/bin/env python3
"""Zoekt nieuwe YouTube-kanalen die lijsten maken van komende idle-, cozy- en bureaubladspellen (Sem, run 13).
Leest de openbare zoekpagina (yt-zoek.py) voor een vaste set zoektermen, houdt video's van hooguit 12 maanden,
en schrijft per kanaal dat nog niet in makers.md staat: aantal treffers, beste titel en weergaven.
Gebruik: python3 yt-lijstmakers.py ../makers.md <uit.csv>"""
import sys, re, csv, time, importlib.util, os
hier = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("yt_zoek", os.path.join(hier, "yt-zoek.py"))
z = importlib.util.module_from_spec(spec); spec.loader.exec_module(z)
TERMEN = ["upcoming idle games", "upcoming idle games 2027", "upcoming cozy games wishlist", "upcoming cozy games 2027",
          "desktop companion games", "taskbar games steam", "games that sit on your desktop", "idle games to play while working",
          "best new idle games steam", "upcoming incremental games", "steam games coming january 2027", "cozy games coming 2027 pc",
          "new desktop idle games", "hidden gem idle games steam"]
bekend = set(h.lower() for h in re.findall(r"\(@([A-Za-z0-9._-]+)\)", open(sys.argv[1]).read()))
def maanden(s):
    m = re.match(r"(?:Streamed )?(\d+)\s*(second|minute|hour|day|week|month|year|mo|w|d|y|h|min|s)s? ago", s or "")
    if not m: return 99
    n, e = int(m.group(1)), m.group(2)
    f = {"second": 0, "s": 0, "minute": 0, "min": 0, "hour": 0, "h": 0, "day": 1/30, "d": 1/30, "week": 0.25, "w": 0.25,
         "month": 1, "mo": 1, "year": 12, "y": 12}[e]
    return n * f
def getal(s):
    m = re.match(r"([\d,]+) views", s or ""); return int(m.group(1).replace(",", "")) if m else 0
k = {}
for t in TERMEN:
    for sort in ("relevant", "views"):
        for v in z.zoek(t, sort):
            u = v.get("kanaal_url") or ""
            if not u.startswith("/@") or u[2:].lower() in bekend or maanden(v["leeftijd"]) > 12: continue
            d = k.setdefault(u, {"kanaal": v["kanaal"], "treffers": set(), "beste": ("", 0)})
            d["treffers"].add(v["id"])
            if getal(v["weergaven"]) > d["beste"][1]: d["beste"] = (v["titel"], getal(v["weergaven"]))
        time.sleep(2)
w = csv.writer(open(sys.argv[2], "w", newline=""))
w.writerow(["handle", "kanaal", "treffers", "beste_titel", "beste_weergaven"])
for u, d in sorted(k.items(), key=lambda x: -x[1]["beste"][1]):
    w.writerow([u, d["kanaal"], len(d["treffers"]), d["beste"][0][:100], d["beste"][1]])
print(len(k), "nieuwe kanalen", file=sys.stderr)
