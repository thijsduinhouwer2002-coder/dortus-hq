"""Eerste beeld en slotkaart van de Click Cuts-Short (#135, Regisseur 26 nov 2026). Beide zijn een echt beeld uit de
schermopname (3D-weergave van Blender, 685 punten breed vergroot naar 1080x1920), met grote tekst erop.
Gebruik: python3 beelden.py <heel.png> <uit_elkaar.png> <eerste.jpg> <slot.jpg>"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
DONKER = (18, 20, 24)
GOUD = (255, 201, 74)


def tekst(doek, regels, y, maat, kleuren):
    d = ImageDraw.Draw(doek)
    f = ImageFont.truetype(FONT, maat)
    for regel, kleur in zip(regels, kleuren):
        w = d.textlength(regel, font=f)
        x = (1080 - w) / 2
        schaduw = Image.new("L", doek.size, 0)
        ImageDraw.Draw(schaduw).text((x, y + 8), regel, font=f, fill=220)
        doek.paste((8, 8, 10), mask=schaduw.filter(ImageFilter.GaussianBlur(12)))
        d.text((x, y), regel, font=f, fill=kleur, stroke_width=8, stroke_fill=DONKER)
        y += maat + 24
    return y


def naar_beneden(pad, schuif):
    """Het beeld zakt schuif punten, zodat de tekst boven op lege grijze vloer staat (geen verzonnen pixels)."""
    im = Image.open(pad).convert("RGB").resize((1080, 1920))
    doek = Image.new("RGB", (1080, 1920))
    rij = im.crop((0, 0, 1080, 6)).resize((1, 1), Image.Resampling.BOX).getpixel((0, 0))
    doek.paste(rij, (0, 0, 1080, schuif + 6))   # effen vloerkleur, geen uitgerekte knoppen
    doek.paste(im.crop((0, 0, 1080, 1920 - schuif)), (0, schuif))
    return doek


a = sys.argv[1:]
# eerste beeld: voor en na naast elkaar, allebei echte beelden uit dezelfde opname
voor = Image.open(a[0]).convert("RGB").resize((1080, 1920))
na = Image.open(a[1]).convert("RGB").resize((1080, 1920))
grond = voor.crop((0, 0, 1080, 6)).resize((1, 1), Image.Resampling.BOX).getpixel((0, 0))
e = Image.new("RGB", (1080, 1920), grond)
H = 1180
e.paste(voor.crop((60, 420, 940, 1900)).resize((int(880 * H / 1480 * 0.8), int(H * 0.8))), (0, 620))
e.paste(na.crop((100, 360, 950, 1900)).resize((int(850 * H / 1540 * 0.8), int(H * 0.8))), (520, 620))
tekst(e, ["Too big for", "your printer?"], 130, 118, ["white", GOUD])
d = ImageDraw.Draw(e)
f = ImageFont.truetype(FONT, 58)
for regel, x, kleur in (("520 mm", 270, "white"), ("1 click", 810, GOUD)):
    w = d.textlength(regel, font=f)
    d.text((x - w / 2, 1640), regel, font=f, fill=kleur, stroke_width=6, stroke_fill=DONKER)
e.save(a[2], quality=92)

s = naar_beneden(a[1], 150)
tekst(s, ["Click Cuts", "for Blender", "on Gumroad"], 110, 112, ["white", "white", GOUD])
s.save(a[3], quality=92)
