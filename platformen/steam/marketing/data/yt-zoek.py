#!/usr/bin/env python3
"""Leest de YouTube-zoekpagina (openbaar, met curl) en geeft per video: kanaal, kanaal-id, titel, weergaven, leeftijd.
Gebruik: python3 yt-zoek.py "zoekterm" [sorteer: relevant|views] > uit.json
"""
import sys, json, re, subprocess, urllib.parse

def zoek(q, sort="views"):
    sp = "&sp=CAM%253D" if sort == "views" else ""
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q) + sp + "&hl=en&gl=US"
    html = subprocess.run(["curl", "-sL", "--max-time", "30", "-H", "Accept-Language: en-US,en;q=0.9",
                           "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36", url],
                          capture_output=True, text=True).stdout
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m:
        return []
    data = json.loads(m.group(1))
    uit = []
    def loop(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                v = o["videoRenderer"]
                own = v.get("ownerText", {}).get("runs", [{}])[0]
                uit.append({
                    "id": v.get("videoId"),
                    "titel": "".join(r.get("text", "") for r in v.get("title", {}).get("runs", [])),
                    "kanaal": own.get("text"),
                    "kanaal_url": own.get("navigationEndpoint", {}).get("commandMetadata", {}).get("webCommandMetadata", {}).get("url"),
                    "kanaal_id": own.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId"),
                    "weergaven": v.get("viewCountText", {}).get("simpleText", ""),
                    "leeftijd": v.get("publishedTimeText", {}).get("simpleText", ""),
                    "duur": v.get("lengthText", {}).get("simpleText", ""),
                })
                return
            for x in o.values(): loop(x)
        elif isinstance(o, list):
            for x in o: loop(x)
    loop(data)
    return uit

if __name__ == "__main__":
    q = sys.argv[1]; s = sys.argv[2] if len(sys.argv) > 2 else "views"
    print(json.dumps({"q": q, "sort": s, "items": zoek(q, s)}, ensure_ascii=False))
