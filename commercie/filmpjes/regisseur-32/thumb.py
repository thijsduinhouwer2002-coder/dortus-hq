"""Thumbnail zoekvideo Click Cuts (#332): een echt beeld uit de opname (Blender 5.3, paard in delen, paneel zichtbaar)
met een grote kop. Geen AI-beeld, geen nagebouwde interface.
    python3 thumb.py <beeld.jpg> <uit.jpg> <x0> <y0> <x1> <y1> "<kop regel 1>" "<kop regel 2>"
Het vak x0,y0,x1,y1 (pixels van het 1920x1080-scherm) wordt geschaald tot 1280x720; de kop staat links op een donkere
band, Poppins ExtraBold (OFL 1.1, regisseur-31/fonts)."""
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = __file__.rsplit("/", 2)[0] + "/regisseur-31/fonts/Poppins-ExtraBold.ttf"
bron, uit = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
regels = sys.argv[7:]
im = Image.open(bron).convert("RGB").crop((x0, y0, x1, y1)).resize((1280, 720), Image.LANCZOS)
im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
d = ImageDraw.Draw(im, "RGBA")
# band links, zacht aflopend, zodat de kop leesbaar is boven het grijze raster
for x in range(0, 640):
    a = int(215 * max(0.0, min(1.0, (640 - x) / 260.0)))
    d.line([(x, 0), (x, 720)], fill=(14, 16, 20, a))
maten = [104, 104, 58]
y = 150
for i, tekst in enumerate(regels):
    f = ImageFont.truetype(FONT, maten[min(i, 2)])
    kleur = (255, 201, 74) if i == 1 else (255, 255, 255)
    d.text((48, y), tekst, font=f, fill=kleur, stroke_width=4 if i < 2 else 2, stroke_fill=(10, 10, 12))
    y += int(maten[min(i, 2)] * 1.12)
im.save(uit, quality=92)
print(uit, im.size)
