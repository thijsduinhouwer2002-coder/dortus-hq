# Bram 17 nov 2026 (Iris keuring 19 punt 1): zet een aantal hoeden op Gloop in hol.json en de bewaartijd terug,
# zodat de weg-stap ook de nacht van een speler met een volle toren en een berg toetst.
# Gebruik: python save_hoeden.py <pad naar hol.json> <hoeden> <seconden terug>
import json, sys
pad, n, sec = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
with open(pad, encoding="utf-8") as f:
    d = json.load(f)
sl = d.setdefault("slijm", {})
sl["hoeden"] = [(i * 7) % 10 for i in range(n)]
sl["gegeten"] = max(n, int(sl.get("gegeten", 0)))
d["tijd"] = float(d["tijd"]) - sec
with open(pad, "w", encoding="utf-8") as f:
    json.dump(d, f)
print("hoeden=%d tijd=%d" % (n, int(d["tijd"])))
