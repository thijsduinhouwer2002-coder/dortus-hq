# Poster (eerste winkelplaatje) voor Ebb: kop, het horloge groot, water onderin. Stijl Mila: vlakke MIP-kleuren.
# Gebruik: python3 maak_poster.py <horloge-scene.png> <uit.png>   (scène uit de plaatjesbouw, tak schermen)
# Gijs, 10 nov 2026.
import math, os, sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1000, 1000
bron, uit = sys.argv[1], sys.argv[2]
hier = os.path.dirname(os.path.abspath(__file__))
letter = os.path.join(hier, "barlow-condensed-latin-500-normal.woff")
img = Image.new("RGB", (W, H), (0, 0, 0))
d = ImageDraw.Draw(img)
# water onderin met een schuimrand
lijn = [(x, 760 + 18 * math.sin(2 * math.pi * 1.5 * x / W + 0.8)) for x in range(0, W + 1, 5)]
d.polygon(lijn + [(W, H), (0, H)], fill=(0x00, 0x55, 0xAA))
d.line(lijn, fill=(0x55, 0xFF, 0xFF), width=6)
for bx, by, br in [(120, 880, 14), (150, 940, 8), (860, 850, 11), (900, 920, 6)]:
    d.ellipse([bx - br, by - br, bx + br, by + br], outline=(0x55, 0xAA, 0xFF), width=3)
kop = ImageFont.truetype(letter, 110)
sub = ImageFont.truetype(letter, 44)
d.text((W / 2, 70), "Breathe like the tide", font=kop, fill=(255, 255, 255), anchor="mt")
d.text((W / 2, 200), "Breath-hold rounds  ·  calm patterns  ·  your sea log", font=sub, fill=(0x55, 0xAA, 0xAA), anchor="mt")
# horloge zonder simulatorbalken: bovenste menubalk en onderste statusbalk eraf
w = Image.open(bron).convert("RGB")
w = w.crop((6, 30, w.width - 6, w.height - 30))
# alleen de witte achtergrond rond het horloge doorzichtig maken (vullen vanaf de randen, de witte cijfers blijven)
w = w.convert("RGBA")
for hoek in [(10, 10), (w.width - 10, 10), (10, w.height - 10), (w.width - 10, w.height - 10)]:
    ImageDraw.floodfill(w, hoek, (0, 0, 0, 0), thresh=40)
schaal = 640 / w.height
w = w.resize((int(w.width * schaal), 640), Image.LANCZOS)
img.paste(w, ((W - w.width) // 2, 290), w)
img = img.resize((640, 640), Image.LANCZOS).quantize(colors=200, method=Image.Quantize.FASTOCTREE)  # onder 150 KB (winkel)
img.save(uit, optimize=True)
print(uit, os.path.getsize(uit))
