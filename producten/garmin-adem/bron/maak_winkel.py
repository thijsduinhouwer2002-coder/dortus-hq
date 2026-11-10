# Schermafbeelding uit de simulator naar winkelmaat: menubalk en statusbalk eraf, wit rond het horloge zwart,
# hoogstens 500 px hoog, onder 150 KB. Gebruik: python3 maak_winkel.py <in.png> <uit.png>. Gijs, 10 nov 2026.
import os, sys
from PIL import Image, ImageDraw
w = Image.open(sys.argv[1]).convert("RGB")
w = w.crop((6, 30, w.width - 6, w.height - 30))
for hoek in [(10, 10), (w.width - 10, 10), (10, w.height - 10), (w.width - 10, w.height - 10)]:
    ImageDraw.floodfill(w, hoek, (0, 0, 0), thresh=40)
s = 500 / w.height
w = w.resize((int(w.width * s), 500), Image.LANCZOS).quantize(colors=200, method=Image.Quantize.FASTOCTREE)
w.save(sys.argv[2], optimize=True)
print(sys.argv[2], os.path.getsize(sys.argv[2]))
