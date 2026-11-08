# Haalt per itch.io-pagina het aantal beoordelingen, AI-melding en makerprofiel op.
# Gebruik: python3 itch-pagina-script.py <lijst.json> <van JJJJ-MM-DD> <tot JJJJ-MM-DD> <uit.json>
import sys, json, time, re, urllib.request
from concurrent.futures import ThreadPoolExecutor
lijst, van, tot, uit = sys.argv[1:5]
items = [i for i in json.load(open(lijst)) if van <= i["pub"][:10] < tot]
seen=set(); items=[i for i in items if not (i["url"] in seen or seen.add(i["url"]))]
def haal(i):
    for p in range(3):
        try:
            h = urllib.request.urlopen(urllib.request.Request(i["url"], headers={"User-Agent": "Mozilla/5.0 (onderzoek)"}), timeout=30).read().decode("utf8", "replace")
            break
        except Exception as e:
            if "404" in str(e): i["weg"] = True; return i
            time.sleep(3)
    else:
        i["fout"] = True; return i
    m = re.search(r'"ratingCount":(\d+)', h)
    i["ratings"] = int(m.group(1)) if m else 0
    m = re.search(r'"ratingValue":"([\d.]+)"', h); i["score"] = float(m.group(1)) if m else None
    m = re.search(r'<td>AI Disclosure</td><td>(.*?)</td>', h, re.S)
    i["ai"] = re.sub(r"<[^>]+>", " ", m.group(1)).strip() if m else ""
    m = re.search(r'Comments?</h2>|class="community_post', h); i["reacties"] = len(re.findall(r'class="community_post ', h))
    time.sleep(0.3)
    return i
with ThreadPoolExecutor(3) as ex:
    res = list(ex.map(haal, items))
json.dump(res, open(uit, "w"), indent=0)
print("klaar", len(res))
