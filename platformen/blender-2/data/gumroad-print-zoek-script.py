# Ronde 3 (Olaf, 8 nov 2026): Blender print-add-ons op Gumroad (nieuwe bron naast Superhive).
# Leest de openbare zoek-API van Gumroad rustig uit en schrijft een jsonl.
import json, sys, time, urllib.parse, urllib.request
VRAGEN = ["blender 3d print", "blender addon 3d printing", "blender split print", "blender print ready",
 "blender miniature addon", "blender stl addon", "blender hollow", "blender wall thickness", "blender overhang",
 "blender connectors print", "blender dowel", "blender keys print", "blender articulated", "blender print in place",
 "blender cosplay print", "blender bambu", "blender 3mf", "blender lithophane", "blender base miniature",
 "blender supports", "blender mesh repair", "blender figure print", "blender tolerance", "blender print joints",
 "blender relief", "blender print tools", "blender cad addon", "blender multicolor print", "blender print bed"]
uit = {}
for v in VRAGEN:
    for start in (0, 9, 18, 27, 36):
        url = "https://gumroad.com/products/search?" + urllib.parse.urlencode({"query": v, "from": start})
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (dortus-onderzoek)"})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=30))
        except Exception as e:
            print("fout", v, start, e, file=sys.stderr); break
        ps = d.get("products", [])
        for p in ps:
            k = p["id"]
            if k not in uit:
                uit[k] = {"naam": p["name"], "maker": p["seller"]["name"], "url": p["url"].split("?")[0],
                          "prijs_usd": p["price_cents"] / 100, "pwyw": p.get("is_pay_what_you_want"),
                          "reviews": p["ratings"]["count"], "gem": p["ratings"]["average"], "vragen": []}
            uit[k]["vragen"].append(v)
        time.sleep(0.7)
        if len(ps) < 9: break
with open(sys.argv[1], "w") as f:
    for r in sorted(uit.values(), key=lambda r: -r["reviews"]):
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(uit), "producten")
