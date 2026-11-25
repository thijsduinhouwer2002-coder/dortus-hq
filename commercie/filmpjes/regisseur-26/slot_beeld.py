"""Slotkaart van de sale-Shorts (#75): robot (release regisseur-14 render-1) met de slotzin groot, zoals Max hem zegt.
Gebruik: python3 slot_beeld.py <render> <uit.jpg>"""
import sys
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
im = Image.open(sys.argv[1]).convert("RGB").resize((1080, 1920))
schuif = 260
doek = Image.new("RGB", (1080, 1920))
doek.paste(im.crop((0, 0, 1080, 8)).resize((1080, schuif + 8)), (0, 0))
doek.paste(im.crop((0, 0, 1080, 1920 - schuif)), (0, schuif))
d = ImageDraw.Draw(doek)
f = ImageFont.truetype(FONT, 112)
for i, r in enumerate(("Click Joints Pro", "on Gumroad")):
    y = 110 + i * 140
    x = (1080 - d.textlength(r, font=f)) / 2
    d.text((x, y), r, font=f, fill="white", stroke_width=8, stroke_fill=(18, 24, 28))
fs = ImageFont.truetype(FONT, 76)
t = "25% OFF THIS WEEK"
w = d.textlength(t, font=fs)
bx, by = (1080 - w) / 2 - 40, 1700
d.rounded_rectangle([bx, by, bx + w + 80, by + 124], radius=62, fill=(255, 196, 0))
d.text((bx + 40, by + 20), t, font=fs, fill=(18, 24, 28))
doek.save(sys.argv[2], quality=92)
