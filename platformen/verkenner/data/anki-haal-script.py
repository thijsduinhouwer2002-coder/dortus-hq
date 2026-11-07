# Vera, 7 nov 2026. Haalt de lijst van alle AnkiWeb-add-ons en per add-on de info (beschrijving, reviews met datum).
# Open endpoints van ankiweb.net (robots.txt verbiedt alleen decks en downloads). Protobuf, zelf uitgepakt.
# Gebruik: python3 anki-haal-script.py <uitmap>
import sys, json, time, urllib.request, os
UA = {"User-Agent": "Mozilla/5.0 (Dortus research, read-only)"}
def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except Exception as e:
            time.sleep(3 * (i + 1)); err = e
    raise err
def varint(b, i):
    s = 0; v = 0
    while True:
        c = b[i]; i += 1; v |= (c & 0x7f) << s; s += 7
        if c < 0x80: return v, i
def parse(b):
    i = 0; out = {}
    while i < len(b):
        k, i = varint(b, i); f, w = k >> 3, k & 7
        if w == 0: v, i = varint(b, i)
        elif w == 2:
            l, i = varint(b, i); v = b[i:i+l]; i += l
        elif w == 1: v = b[i:i+8]; i += 8
        elif w == 5: v = b[i:i+4]; i += 4
        else: raise ValueError(w)
        out.setdefault(f, []).append(v)
    return out
def s(x): return x.decode("utf-8", "replace") if isinstance(x, bytes) else x
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
lst = parse(get("https://ankiweb.net/svc/shared/list-addons?search="))
rows = []
for r in lst.get(1, []):
    p = parse(r)
    mv = p.get(6, [0])[0]
    if mv >= 2**63: mv -= 2**64
    rows.append({"id": p.get(1, [0])[0], "title": s(p.get(2, [b""])[0]), "up": p.get(3, [0])[0],
                 "down": p.get(4, [0])[0], "mtime": p.get(5, [0])[0], "maxver": mv})
json.dump(rows, open(f"{out}/lijst.json", "w"))
print("add-ons in lijst:", len(rows), flush=True)
res = []
for n, r in enumerate(rows):
    try:
        b = get(f"https://ankiweb.net/svc/shared/item-info?sharedId={r['id']}")
        t = parse(b)
        if 1 not in t: res.append({"id": r["id"], "fout": "niet beschikbaar"}); continue
        a = parse(t[1][0])
        revs = []
        for rv in a.get(1, []):
            q = parse(rv)
            revs.append({"t": q.get(1, [0])[0], "up": q.get(2, [0])[0], "body": s(q.get(4, [b""])[0])[:300]})
        res.append({"id": r["id"], "title": s(a.get(5, [b""])[0]), "desc": s(a.get(9, [b""])[0]),
                    "last_updated": a.get(8, [0])[0], "shared_by_user": a.get(13, [0])[0],
                    "up": a.get(18, [0])[0], "down": a.get(19, [0])[0], "too_new": a.get(21, [0])[0],
                    "support": s(a.get(12, [b""])[0]), "reviews": revs})
    except Exception as e:
        res.append({"id": r["id"], "fout": str(e)})
    if n % 200 == 0:
        print(n, flush=True); json.dump(res, open(f"{out}/info.json", "w"))
    time.sleep(0.25)
json.dump(res, open(f"{out}/info.json", "w"))
print("klaar", len(res))
