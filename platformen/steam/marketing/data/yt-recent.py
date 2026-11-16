#!/usr/bin/env python3
"""Laatste video's van een openbaar YouTube-kanaal (met curl), om te zien of een maker nog actief is
en of hij kleine spellen, demo's of fest-overzichten maakt. Gebruik:
  python3 yt-recent.py <uit.csv> /@handle /@handle ...
Per kanaal de eerste ±30 video's op /videos: titel, weergaven, hoe lang geleden.
Daarna per kanaal: aantal in de laatste 30 dagen, mediaan weergaven, en hoeveel titels over
idle, desktop, cozy, demo of fest gaan."""
import sys, re, json, subprocess, csv, statistics, time
WOORDEN = re.compile(r"idle|desktop|taskbar|task bar|cozy|cosy|demo|next fest|fest\b|incremental|while you work|afk", re.I)
def lees(h):
    url = "https://www.youtube.com" + h + "/videos?hl=en&gl=US"
    html = subprocess.run(["curl", "-sL", "--max-time", "30", "-H", "Accept-Language: en-US,en;q=0.9",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36", url],
        capture_output=True, text=True).stdout
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        return []
    data = json.loads(m.group(1))
    uit = []
    def loop(o):
        if isinstance(o, dict):
            if "lockupViewModel" in o or "videoRenderer" in o:
                s = json.dumps(o)
                t = re.search(r'"title": \{"content": "((?:[^"\\]|\\.)*)"', s) or re.search(r'"title": \{"runs": \[\{"text": "((?:[^"\\]|\\.)*)"', s)
                v = re.search(r'"accessibilityLabel": "([\d.,]+(?: thousand| million)?) views?"', s) or re.search(r'"(?:simpleText|text)": "([\d.,]+[KM]?) views"', s)
                d = re.search(r'"accessibilityLabel": "(\d+ (?:second|minute|hour|day|week|month|year)s? ago)"', s) or re.search(r'"(?:simpleText|text)": "(\d+ (?:second|minute|hour|day|week|month|year)s? ago)"', s)
                if t:
                    uit.append([json.loads('"' + t.group(1) + '"'), v.group(1) if v else "", d.group(1) if d else ""])
                return
            for x in o.values(): loop(x)
        elif isinstance(o, list):
            for x in o: loop(x)
    loop(data)
    return uit
def getal(s):
    if not s: return None
    s = s.replace(",", "").replace(" thousand", "K").replace(" million", "M")
    f = 1000 if s.endswith("K") else 1000000 if s.endswith("M") else 1
    return float(s.rstrip("KM")) * f
def dagen(s):
    m = re.match(r"(\d+) (\w+?)s? ago", s or "")
    if not m: return None
    n, e = int(m.group(1)), m.group(2)
    return n * {"second": 0, "minute": 0, "hour": 0, "day": 1, "week": 7, "month": 30, "year": 365}[e]
if __name__ == "__main__":
    w = csv.writer(open(sys.argv[1], "w", newline=""))
    w.writerow(["handle", "videos_gelezen", "laatste_video_dagen", "videos_laatste_30_dagen", "mediaan_weergaven",
                "titels_idle_desktop_cozy_demo_fest", "voorbeelden"])
    for h in sys.argv[2:]:
        v = lees(h)
        d = [dagen(x[2]) for x in v if dagen(x[2]) is not None]
        g = [getal(x[1]) for x in v if getal(x[1]) is not None]
        hit = [x[0] for x in v if WOORDEN.search(x[0])]
        w.writerow([h, len(v), min(d) if d else "", sum(1 for x in d if x <= 30),
                    int(statistics.median(g)) if g else "", len(hit), " | ".join(hit[:3])[:300]])
        print(h, len(v), file=sys.stderr)
        time.sleep(1.5)
