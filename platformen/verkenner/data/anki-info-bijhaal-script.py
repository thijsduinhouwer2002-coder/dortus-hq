# Vera, 7 nov 2026. Haalt item-info voor add-ons gewijzigd sinds een datum, met 2 draden, en voegt toe aan info.json.
# Gebruik: python3 anki-info-bijhaal-script.py <uitmap> <unix-tijd-vanaf>
import sys, json, time, importlib.util, threading
from concurrent.futures import ThreadPoolExecutor
out, since = sys.argv[1], int(sys.argv[2])
sys.argv = ["x", "/dev/null"]
src = open(__file__.replace("anki-info-bijhaal-script.py", "anki-haal-script.py")).read().split("out = sys.argv[1]")[0]
exec(src)
rows = json.load(open(f"{out}/lijst.json"))
try: have = json.load(open(f"{out}/info.json"))
except: have = []
done = {x["id"] for x in have}
todo = [r for r in rows if r["mtime"] >= since and r["id"] not in done]
print("te doen", len(todo), flush=True)
lock = threading.Lock()
def one(r):
    try:
        t = parse(get(f"https://ankiweb.net/svc/shared/item-info?sharedId={r['id']}"))
        if 1 not in t: x = {"id": r["id"], "fout": "niet beschikbaar"}
        else:
            a = parse(t[1][0]); revs = []
            for rv in a.get(1, []):
                q = parse(rv); revs.append({"t": q.get(1, [0])[0], "up": q.get(2, [0])[0], "body": s(q.get(4, [b""])[0])[:300]})
            x = {"id": r["id"], "title": s(a.get(5, [b""])[0]), "desc": s(a.get(9, [b""])[0]), "last_updated": a.get(8, [0])[0],
                 "shared_by_user": a.get(13, [0])[0], "up": a.get(18, [0])[0], "down": a.get(19, [0])[0],
                 "too_new": a.get(21, [0])[0], "support": s(a.get(12, [b""])[0]), "reviews": revs}
    except Exception as e: x = {"id": r["id"], "fout": str(e)}
    with lock:
        have.append(x)
        if len(have) % 200 == 0:
            json.dump(have, open(f"{out}/info.json", "w")); print(len(have), flush=True)
    time.sleep(0.3)
with ThreadPoolExecutor(2) as ex: list(ex.map(one, todo))
json.dump(have, open(f"{out}/info.json", "w")); print("klaar", len(have))
