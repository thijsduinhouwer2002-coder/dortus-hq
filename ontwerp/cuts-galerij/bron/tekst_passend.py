"""Tekst op galerijbeeld Click Cuts "Pins that fit your printer" (Beeldmaker, 25 nov 2026, issue #39).

python3 tekst_passend.py <render-passend.png> <passend.json> <render-zak.png> <uitmap> <fontmap> <icoon.svg>

Maakt passend-2400x1200.jpg (Superhive) en passend-1920x1080.jpg (Gumroad) uit een render van 2400x1350.
Links: merk, titel en de regel uit onderschrift 6 van `producten/blender-splitser/galerij.md`, ingekort. Rechts het
proefblokje uit Make fit test; bij het blok een label met de spelingen en de pen uit passend.json (niet verzonnen).
Linksonder een kaartje: stuk 11 van het paard zweeft boven stuk 7 met de pennen (render-zak, uit snijvlak.py).
Omgeving: ZK_KADER (x0,y0,x1,y1 als deel van render-zak), LB_DX, LB_DY (plek van het label).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, ZAK, UIT, FONTS, ICOON = sys.argv[1:7]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT = (255, 246, 230), (255, 210, 92), (222, 212, 232)
W, H = 2400, 1350


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def icoon(maat):
    p = os.path.join(UIT, f"_icoon_{maat}.png")
    os.system(f"rsvg-convert -w {maat} '{ICOON}' -o '{p}'")
    im = Image.open(p).convert("RGBA")
    os.remove(p)
    return im


def schaduwtekst(img, xy, tekst, f, kleur, schaduw=10, anchor="la"):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).text(xy, tekst, font=f, fill=(0, 0, 0, 170), anchor=anchor)
    laag = laag.filter(ImageFilter.GaussianBlur(schaduw))
    img.alpha_composite(laag)
    ImageDraw.Draw(img).text(xy, tekst, font=f, fill=kleur, anchor=anchor)


def regels(tekst, f, breed):
    uit, nu = [], ""
    for w in tekst.split(" "):  # alleen gewone spaties, zodat "5 mm" bij elkaar blijft
        t = (nu + " " + w).strip()
        if f.getlength(t) > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = t
    return uit + [nu]


def kaart(img, x0, y0, bw, bh, m):
    """Kaartje linksonder: het paard op de pennen, met één regel."""
    z = Image.open(ZAK).convert("RGBA")
    k = [float(v) for v in os.environ.get("ZK_KADER", "0.55,0.0,0.86,1.0").split(",")]
    zw, zh = z.size
    z = z.crop((int(k[0] * zw), int(k[1] * zh), int(k[2] * zw), int(k[3] * zh)))
    iw = int(bh * z.size[0] / z.size[1])
    z = z.resize((iw, bh), Image.LANCZOS)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((x0 + 8, y0 + 14, x0 + bw + 8, y0 + bh + 14), radius=28,
                                           fill=(0, 0, 0, 150))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(14)))
    kaartbeeld = Image.new("RGBA", (bw, bh), (20, 12, 28, 255))
    kaartbeeld.paste(z, (0, 0))
    masker = Image.new("L", (bw, bh), 0)
    ImageDraw.Draw(masker).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=28, fill=255)
    img.paste(kaartbeeld, (x0, y0), masker)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radius=28, outline=GOUD + (255,), width=3)
    tx = x0 + iw + 36
    ty = y0 + 60
    f1 = font("Bricolage.ttf", 46, "Bold")
    for t in ("Then every cut", "gets that clearance"):
        schaduwtekst(img, (tx, ty), t, f1, CREME, schaduw=6)
        ty += 58
    ty += 18
    f2 = font("Inter.ttf", 32, "Medium")
    zin = (f"Part 11 lowers onto part 7: the pins and holes Click Cuts added, {m['pen_d_mm']:g} mm pins.")
    for t in regels(zin, f2, bw - iw - 70):
        schaduwtekst(img, (tx, ty), t, f2, ZACHT, schaduw=6)
        ty += 44


def main():
    m = json.load(open(META))
    img = Image.open(RENDER).convert("RGBA").resize((W, H), Image.LANCZOS)
    verloop = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(verloop)
    for x in range(1250):
        dv.line([(x, 0), (x, H)], fill=int(175 * (1 - x / 1250) ** 1.5))
    img = Image.composite(Image.new("RGBA", (W, H), (14, 8, 20, 255)), img, verloop)

    x = 120
    ic = icoon(84)
    img.alpha_composite(ic, (x, 150))
    schaduwtekst(img, (x + 104, 192), "Click Cuts", font("Bricolage.ttf", 64, "Bold"), CREME, anchor="lm")
    y = 290
    for regel, kl in (("Pins that fit", CREME), ("your printer.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 132, "ExtraBold"), kl)
        y += 150
    y += 30
    zin = ("Print the small fit test block first: your own pin at four clearances. "
           "Pick the one that fits, and Click Cuts remembers it.")
    fz = font("Inter.ttf", 46, "Medium")
    for r in regels(zin, fz, 940):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 64

    # label boven het blok: de vier spelingen en de pen, uit passend.json
    sp = m["spelingen_mm"]
    nr = m["nummers"]
    ax = (nr[0]["gat"][0] + nr[1]["gat"][0]) / 2 * W
    ay = min(n["gat"][1] for n in nr) * H
    lx = ax + float(os.environ.get("LB_DX", "-120"))
    ly = ay + float(os.environ.get("LB_DY", "-250"))
    fl = font("Inter.ttf", 40, "SemiBold")
    fk = font("Inter.ttf", 34, "Medium")
    schaduwtekst(img, (lx, ly), f"{sp[0]:.2f} to {sp[-1]:.2f} mm, engraved", fl, CREME, schaduw=6, anchor="ma")
    schaduwtekst(img, (lx, ly + 48), f"your {m['pen_d_mm']:g} mm pin, four clearances", fk, GOUD, schaduw=6,
                 anchor="ma")

    kaart(img, x, int(os.environ.get("ZK_Y", "880")), int(os.environ.get("ZK_B", "960")),
          int(os.environ.get("ZK_H", "330")), m)

    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, "passend-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, "passend-1920x1080.jpg"), quality=92)
    print("klaar passend")


main()
