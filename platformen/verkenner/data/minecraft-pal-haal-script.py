# Haalt itempagina's van MinecraftPal (robots.txt staat /marketplace/item toe) en leest de openbare velden.
import sys, re, json, time, random, html, urllib.request
from concurrent.futures import ThreadPoolExecutor
A = "Mozilla/5.0 (compatible; ClaudeBot/1.0)"
def haal(u):
    for p in range(2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": A}), timeout=40)
            t = r.read().decode("utf-8", "replace"); break
        except Exception as e:
            t = None; time.sleep(3)
    time.sleep(0.4)
    if not t: return {"url": u, "fout": 1}
    d = {"url": u, "maker": u.split("/")[-1]}
    m = re.search(r'"aggregateRating":\{"@type":"AggregateRating","ratingValue":([\d.]+),"ratingCount":(\d+)\}', t)
    d["rating"], d["n"] = (float(m.group(1)), int(m.group(2))) if m else (None, 0)
    m = re.search(r'"brand":\{"@type":"Organization","name":"([^"]*)"', t); d["maker"] = html.unescape(m.group(1)) if m else None
    m = re.search(r'"@type":"Product","name":"((?:[^"\\]|\\.)*)"', t); d["naam"] = m.group(1) if m else None
    tx = re.sub(r"<[^>]+>", " ", t); tx = re.sub(r"\s+", " ", tx)
    for k, pat in [("type", r"Pack Type (.+?) Created"), ("created", r"Created ([A-Z][a-z]+ \d{1,2}, \d{4})"), ("updated", r"Updated ([A-Z][a-z]+ \d{1,2}, \d{4})"), ("prijs", r"available for (\d+) Minecoins"), ("ctype", r"Content Type (\S+)")]:
        m = re.search(pat, tx); d[k] = m.group(1) if m else None
    if d["prijs"] is None and re.search(r"is free to download", tx): d["prijs"] = "0"
    return d
urls = [l.strip() for l in open(sys.argv[1]) if l.strip()]
with ThreadPoolExecutor(3) as ex, open(sys.argv[2], "a") as out:
    for d in ex.map(haal, urls):
        out.write(json.dumps(d, ensure_ascii=False) + "\n"); out.flush()
