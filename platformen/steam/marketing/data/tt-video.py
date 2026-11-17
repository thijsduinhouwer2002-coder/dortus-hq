#!/usr/bin/env python3
"""Leest openbare TikTok-videopagina's en -profielen (curl, rustig) en schrijft per video:
account, volgers, video's, datum, weergaven, likes, weergaven per volger, contact in bio (alleen het soort).
Gebruik: python3 tt-video.py urls.txt uit.csv   (urls.txt: een video-URL per regel, '# naam' mag erachter)"""
import sys, re, json, time, subprocess, csv, datetime
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
def get(url):
    return subprocess.run(["curl", "-sL", "-A", UA, "--max-time", "25", url], capture_output=True, text=True).stdout
def data(html):
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1))["__DEFAULT_SCOPE__"] if m else {}
def soort(bio):
    b = bio.lower()
    if "@" not in b and "mail" not in b: return "geen"
    if re.search(r"@(gmail|hotmail|outlook|yahoo|icloud)\.", b): return "gratis adres"
    if re.search(r"(manag|agency|talent|mgmt)", b): return "bureau-adres"
    if "@" in b: return "eigen domein of bureau"
    return "noemt mail, geen adres"
rows, gezien = [], {}
for line in open(sys.argv[1]):
    url = line.split("#")[0].strip()
    if not url: continue
    d = data(get(url)); time.sleep(2)
    it = d.get("webapp.video-detail", {}).get("itemInfo", {}).get("itemStruct", {})
    if not it: print("geen data", url); continue
    a, st = it["author"], it.get("stats", {})
    u = a["uniqueId"]
    if u not in gezien:
        p = data(get("https://www.tiktok.com/@" + u)); time.sleep(2)
        ui = p.get("webapp.user-detail", {}).get("userInfo", {})
        gezien[u] = (ui.get("stats", {}), ui.get("user", {}).get("signature", a.get("signature", "")))
    ps, bio = gezien[u]
    vol = ps.get("followerCount") or it.get("authorStats", {}).get("followerCount", 0)
    pc = int(st.get("playCount", 0))
    rows.append(dict(account="@" + u, volgers=vol, videos=ps.get("videoCount", ""),
        datum=datetime.datetime.utcfromtimestamp(int(it["createTime"])).date().isoformat(),
        weergaven=pc, likes=st.get("diggCount", ""), per_volger=round(pc / vol, 2) if vol else "",
        contact=soort(bio), tekst=it.get("desc", "")[:90].replace("\n", " "), url=url))
    print(rows[-1]["account"], vol, rows[-1]["datum"], pc)
with open(sys.argv[2], "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
