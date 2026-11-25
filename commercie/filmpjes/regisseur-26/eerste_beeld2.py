"""Eerste beeld sale-eindstop, tweede poging (issue #75, Regisseur 25 nov 2026, na NIET GESLAAGD in de blinde test
pro-sale-shorts-2026-11-25-1912: rechters wilden de Blender-interface zien en het mechaniek van de knie, en dat het
over printbare gewrichten gaat).
Bronnen: studio-render robot met gebogen knie (release regisseur-24 render-3) en een echt beeld uit de schermopname
van release regisseur-26 (scherm.mkv op 195,3 s: Bend 119,9, groene boog "Left knee 0-120°").
Gebruik: python3 eerste_beeld2.py <render.png> <scherm.png> <uit-inzet.jpg> <uit-scherm.jpg>"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
DONKER = (18, 24, 28)


def kop(doek, regels, y=110, maat=112):
    d = ImageDraw.Draw(doek)
    f = ImageFont.truetype(FONT, maat)
    for regel in regels:
        w = d.textlength(regel, font=f)
        x = (1080 - w) / 2
        schaduw = Image.new("L", doek.size, 0)
        ImageDraw.Draw(schaduw).text((x, y + 6), regel, font=f, fill=200)
        doek.paste((20, 30, 30), mask=schaduw.filter(ImageFilter.GaussianBlur(10)))
        d.text((x, y), regel, font=f, fill="white", stroke_width=7, stroke_fill=DONKER)
        y += maat + 26
    return y


def regel_klein(doek, tekst, y, maat=50):
    d = ImageDraw.Draw(doek)
    f = ImageFont.truetype(FONT, maat)
    w = d.textlength(tekst, font=f)
    d.text(((1080 - w) / 2, y), tekst, font=f, fill="white", stroke_width=5, stroke_fill=DONKER)


def sale(doek, tekst="25% OFF THIS WEEK"):
    d = ImageDraw.Draw(doek)
    fs = ImageFont.truetype(FONT, 58)
    w = d.textlength(tekst, font=fs)
    bx, by = (1080 - w) / 2 - 34, 1780
    d.rounded_rectangle([bx, by, bx + w + 68, by + 100], radius=50, fill=(255, 196, 0))
    d.text((bx + 34, by + 16), tekst, font=fs, fill=DONKER)


def knie_uit_scherm(scherm):
    # alleen de 3D-weergave (het paneel begint rond x=1090), rond de knie met de groene boog
    return Image.open(scherm).convert("RGB").crop((140, 190, 1040, 1010))


def met_inzet(render, scherm, uit):
    doek = Image.open(render).convert("RGB").resize((1080, 1920))
    # robot lager zodat de kop erboven past (render met rechte benen, de inzet toont de knie)
    basis = Image.new("RGB", (1080, 1920))
    basis.paste(doek.crop((0, 0, 1080, 8)).resize((1080, 180)), (0, 0))
    basis.paste(doek.crop((0, 0, 1080, 1740)), (0, 180))
    doek = basis
    kop(doek, ["Knee bends", "too far?"])
    inzet = knie_uit_scherm(scherm).resize((560, 510))
    rand = Image.new("RGB", (inzet.width + 16, inzet.height + 16), "white")
    masker = Image.new("L", rand.size, 0)
    ImageDraw.Draw(masker).rounded_rectangle([0, 0, rand.width - 1, rand.height - 1], radius=34, fill=255)
    rand.paste(inzet, (8, 8))
    schaduw = Image.new("L", doek.size, 0)
    px, py = 1080 - rand.width - 30, 1030
    ImageDraw.Draw(schaduw).rounded_rectangle([px + 8, py + 16, px + rand.width + 8, py + rand.height + 16],
                                              radius=34, fill=150)
    doek.paste((10, 15, 15), mask=schaduw.filter(ImageFilter.GaussianBlur(18)))
    doek.paste(rand, (px, py), masker)
    d = ImageDraw.Draw(doek)
    f = ImageFont.truetype(FONT, 40)
    t = "End stop in Blender"
    w = d.textlength(t, font=f)
    cx = px + rand.width / 2
    d.rounded_rectangle([cx - w / 2 - 24, py - 70, cx + w / 2 + 24, py - 8], radius=30, fill=DONKER)
    d.text((cx - w / 2, py - 64), t, font=f, fill="white")
    sale(doek)
    doek.save(uit, quality=92)


def scherm_groot(render, scherm, uit):
    doek = Image.new("RGB", (1080, 1920), (40, 42, 46))
    knie = knie_uit_scherm(scherm)
    k = knie.resize((1080, int(knie.height * 1080 / knie.width)))
    doek.paste(k, (0, 520))
    # zachte overgang boven en onder het schermbeeld
    for y0, richting in ((520, 1), (520 + k.height, -1)):
        for i in range(60):
            a = int(255 * (1 - i / 60))
            band = Image.new("RGB", (1080, 1), (40, 42, 46))
            doek.paste(band, (0, y0 + richting * i - (1 if richting < 0 else 0)),
                       Image.new("L", (1080, 1), a))
    y = kop(doek, ["Does your knee", "bend too far?"], y=150, maat=104)
    regel_klein(doek, "Printable joints with an end stop", y + 10)
    sale(doek)
    doek.save(uit, quality=92)


if __name__ == "__main__":
    render, scherm, uit1, uit2 = sys.argv[1:5]
    met_inzet(render, scherm, uit1)
    scherm_groot(render, scherm, uit2)
