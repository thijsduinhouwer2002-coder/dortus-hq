"""Eerste beeld (thumbnail) van de twee sale-Shorts van issue #75 (Regisseur, 25 nov 2026).
Bron: studio-renders van de eigen robot (release regisseur-14 render-2 = uit elkaar, regisseur-24 render-1 = knie gebogen).
Grote hookvraag bovenaan, klein saleplaatje onderaan. Gebruik: python3 eerste_beeld.py <render> <uit.jpg> <regel1> <regel2>"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"


def maak(bron, uit, r1, r2, schuif="170", sale="25% OFF THIS WEEK"):
    im = Image.open(bron).convert("RGB").resize((1080, 1920))
    # robot iets lager: boven ruimte voor de vraag
    schuif = int(schuif)
    doek = Image.new("RGB", (1080, 1920))
    doek.paste(im.crop((0, 0, 1080, 8)).resize((1080, schuif + 8)), (0, 0))
    doek.paste(im.crop((0, 0, 1080, 1920 - schuif)), (0, schuif))
    d = ImageDraw.Draw(doek)
    f = ImageFont.truetype(FONT, 104)
    y = 120
    for regel in (r1, r2):
        w = d.textlength(regel, font=f)
        x = (1080 - w) / 2
        schaduw = Image.new("L", (1080, 1920), 0)
        ImageDraw.Draw(schaduw).text((x, y + 6), regel, font=f, fill=200)
        schaduw = schaduw.filter(ImageFilter.GaussianBlur(10))
        doek.paste((20, 30, 30), mask=schaduw)
        d.text((x, y), regel, font=f, fill="white", stroke_width=7, stroke_fill=(18, 24, 28))
        y += 128
    fs = ImageFont.truetype(FONT, 58)
    w = d.textlength(sale, font=fs)
    bx, by = (1080 - w) / 2 - 34, 1780
    d.rounded_rectangle([bx, by, bx + w + 68, by + 100], radius=50, fill=(255, 196, 0))
    d.text((bx + 34, by + 16), sale, font=fs, fill=(18, 24, 28))
    doek.save(uit, quality=92)


if __name__ == "__main__":
    maak(*sys.argv[1:6])
