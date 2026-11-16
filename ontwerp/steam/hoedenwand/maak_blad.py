# Mila, 16 nov 2026: de 10 hoedenwand-renders als één blad op spelmaat, in de vorm van sprites.json ("soort": "stukken", px 4),
# zodat Bram/Olaf het naast deco.png kunnen zetten. Breedte per stuk 13 spelpixels (52 px), anker "midden" = midden van de holte.
import os, json
from PIL import Image
HIER = os.path.dirname(os.path.abspath(__file__))
PX, BREED_SP = 4, 13
stukken, ims, x = {}, [], 4
for nr in range(10):
    im = Image.open(os.path.join(HIER, 'renders', f'wand-{nr}.png')).convert('RGBA'); im = im.crop(im.getbbox())
    w = BREED_SP * PX; h = round(im.height * w / im.width); h += (-h) % PX
    im = im.resize((w, h), Image.LANCZOS); ims.append((im, x))
    stukken[f'wand-{nr}'] = {"maat": [BREED_SP, h // PX], "vak_px": [x, 4, w, h], "midden": [BREED_SP / 2, round(h * 0.45 / PX, 1)]}
    x += w + 8
H = max(i.height for i, _ in ims) + 8
blad = Image.new('RGBA', (x, H), (0, 0, 0, 0))
for im, xx in ims: blad.alpha_composite(im, (xx, 4))
blad.save(os.path.join(HIER, 'blad', 'hoedenwand.png'), optimize=True)
json.dump({"hoedenwand": {"blad": "res://kunst/3d/hoedenwand.png", "model": "ontwerp/steam/hoedenwand/hoedenwand.py", "px": PX,
           "samples": 32, "soort": "stukken", "stukken": stukken}}, open(os.path.join(HIER, 'blad', 'hoedenwand.json'), 'w'), indent=1)
print(blad.size, os.path.getsize(os.path.join(HIER, 'blad', 'hoedenwand.png')))
