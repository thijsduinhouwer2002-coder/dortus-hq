#!/usr/bin/env python3
"""Leest de winkelbeschrijving van Steam-spellen (openbare appdetails-API, rustig) en zoekt naar
een koppeling met Twitch of chat (woorden: twitch, streamer, chat command). Telt ook reviews
(het getal 'recommendations'). Gebruik: python3 twitch-koppeling.py apps.txt uit.csv
apps.txt: per regel een appid (rest van de regel mag een naam zijn).
Sem, 16 nov 2026. De lijst apps kwam uit de Steam-zoekpagina (search/results, sort_by=Reviews_DESC)
op: desktop idle, taskbar, desktop companion, bottom of your screen, idle desktop pet."""
import json, sys, re, subprocess, time, csv
EXTRA = "4623570 3772810 3678970 3339780 4547080 3659410 3122460 3733510 3959890 5368130".split()
def get(u):
    r = subprocess.run(["curl", "-s", "--max-time", "30", u], capture_output=True, text=True).stdout
    try: return json.loads(r)
    except Exception: return None
ids = list(dict.fromkeys(EXTRA + [l.split()[0] for l in open(sys.argv[1]) if l.strip()]))
w = csv.writer(open(sys.argv[2], "w", newline=""))
w.writerow(["appid", "naam", "reviews", "uitgekomen", "koppeling_chat", "zin"])
for a in ids:
    d = get(f"https://store.steampowered.com/api/appdetails?appids={a}&l=english&cc=us"); time.sleep(0.6)
    if not d or not d.get(a, {}).get("success") or d[a]["data"].get("type") != "game": continue
    x = d[a]["data"]
    t = re.sub(r"<[^>]+>", " ", x.get("detailed_description", ""))
    m = re.search(r"(?i)[^.]{0,160}(twitch|streamer|chat command)[^.]{0,160}", t)
    w.writerow([a, x["name"], x.get("recommendations", {}).get("total", 0), x.get("release_date", {}).get("date", ""),
                "ja" if m else "nee", re.sub(r"\s+", " ", m.group(0)).strip()[:200] if m else ""])
