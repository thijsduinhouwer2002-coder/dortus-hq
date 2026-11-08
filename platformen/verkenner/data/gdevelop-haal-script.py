# Haalt de openbare winkellijsten van GDevelop op (asset-packs, game-sjablonen, bundels)
# en telt per jaar/maand en per maker. Gebruik: python3 gdevelop-haal-script.py <uitmap>
import json, sys, os, urllib.request, collections
uit = sys.argv[1] if len(sys.argv) > 1 else "."
os.makedirs(uit, exist_ok=True)
for p in ["asset-pack", "game-template", "bundle"]:
    with urllib.request.urlopen("https://api.gdevelop.io/shop/" + p) as r:
        d = json.load(r)
    json.dump(d, open(os.path.join(uit, "gdevelop-" + p + ".json"), "w"))
    derden = [x for x in d if not x.get("isSellerGDevelop")]
    print(p, "totaal", len(d), "derden", len(derden),
          "makers", len(set(x["sellerId"] for x in derden)))
    print("  derden per jaar", sorted(collections.Counter(x["createdAt"][:4] for x in derden).items()))
