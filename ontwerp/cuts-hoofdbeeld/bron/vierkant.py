"""Vierkante Gumroad-thumbnail van Click Cuts uit de render van het GESLAAGDE paard-hoofdbeeld (Beeldmaker, issue #147).

python3 vierkant.py <paard-render.jpg 2400x1350> <paard.json> <uitmap> <fontmap met Bricolage.ttf en Inter.ttf> <icoon.svg>

Geen nieuwe render: een vierkante uitsnede (x 1025 tot 2375) van dezelfde Blender-render als het hoofdbeeld
(beelden/paard-render.jpg). Boven de render is 220 px lucht bijgemaakt door de bovenste rij te herhalen en te
vervagen, zodat de titel ruimte heeft. Bovenaan icoon en "Click Cuts" groot, eronder de haak, in de scène
"1 click" met pijl en twee korte labels. Maakt paard-vierkant-1200x1200.jpg en paard-vierkant-600x600.jpg.
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON = sys.argv[1:6]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT = (255, 246, 230), (255, 196, 84), (226, 216, 232)
X0, X1, BOVEN, ONDER = 1025, 2375, 220, 1130   # uitsnede in render-pixels (1350 x 1350)
S = 1200
F = S / (X1 - X0)


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
    ImageDraw.Draw(laag).text(xy, tekst, font=f, fill=(0, 0, 0, 190), anchor=anchor)
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(schaduw)))
    ImageDraw.Draw(img).text(xy, tekst, font=f, fill=kleur, anchor=anchor)


def pijl(img, x0, y0, x1, y1, kleur, dik=8):
    d = ImageDraw.Draw(img)
    pts = []
    mx, my = (x0 + x1) / 2, min(y0, y1) - 60
    for i in range(41):
        t = i / 40
        pts.append(((1 - t) ** 2 * x0 + 2 * (1 - t) * t * mx + t ** 2 * x1,
                    (1 - t) ** 2 * y0 + 2 * (1 - t) * t * my + t ** 2 * y1))
    d.line(pts[:-3], fill=kleur, width=dik, joint="curve")
    (ax, ay), (bx, by) = pts[-6], pts[-1]
    h = math.atan2(by - ay, bx - ax)
    L = 26
    d.polygon([(bx, by), (bx - L * math.cos(h - 0.45), by - L * math.sin(h - 0.45)),
               (bx - L * math.cos(h + 0.45), by - L * math.sin(h + 0.45))], fill=kleur)


def naar(x, y):
    """render-pixel naar vierkant-pixel"""
    return (x - X0) * F, (y + BOVEN) * F


def main():
    meta = json.load(open(META))
    r = Image.open(RENDER).convert("RGB").resize((2400, 1350), Image.LANCZOS)
    stuk = r.crop((X0, 0, X1, ONDER))
    W = X1 - X0
    doek = Image.new("RGB", (W, BOVEN + ONDER))
    lucht = stuk.crop((0, 0, W, 4)).resize((W, BOVEN + 40)).filter(ImageFilter.GaussianBlur(30))
    doek.paste(lucht, (0, 0))
    doek.paste(stuk, (0, BOVEN))
    # naad zacht maken
    naad = doek.crop((0, BOVEN - 20, W, BOVEN + 40)).filter(ImageFilter.GaussianBlur(12))
    doek.paste(naad, (0, BOVEN - 20))
    img = doek.resize((S, S), Image.LANCZOS).convert("RGBA")
    # bovenste strook iets donkerder voor de titel
    m = Image.new("L", (1, S), 0)
    for y in range(S):
        m.putpixel((0, y), int(120 * max(0.0, 1 - y / 360) ** 1.4))
    img.paste(Image.new("RGBA", (S, S), (12, 7, 18, 255)), (0, 0), m.resize((S, S)))

    x = 56
    ic = icoon(124)
    img.alpha_composite(ic, (x, 44))
    schaduwtekst(img, (x + 148, 44 + 62), "Click Cuts", font("Bricolage.ttf", 168, "ExtraBold"), CREME,
                 schaduw=14, anchor="lm")
    fs = font("Bricolage.ttf", 64, "Bold")
    y = 200
    d = ImageDraw.Draw(img)
    t1 = "Too big to print? "
    w1 = d.textlength(t1, font=fs)
    schaduwtekst(img, (x, y), t1, fs, CREME)
    schaduwtekst(img, (x + w1, y), "One click.", fs, GOUD)
    # ronde 2: ChatGPT vroeg twee keer om "Blender add-on" in beeld
    fpil = font("Inter.ttf", 28, "Bold")
    tp = "Blender add-on"
    px0 = x + w1 + d.textlength("One click.", font=fs) + 24
    bb = d.textbbox((0, 0), tp, font=fpil)
    d.rounded_rectangle((px0, y + 8, px0 + bb[2] + 32, y + 66), radius=29, fill=(24, 16, 30, 235),
                        outline=GOUD + (255,), width=3)
    d.text((px0 + 16, y + 37 - (bb[3] + bb[1]) / 2), tp, font=fpil, fill=CREME)

    v, n, b = meta["vak_voor"], meta["vak_na"], meta["vak_bed"]
    vx0, vy0 = naar(v[0] * 2400, v[2] * 1350)
    vx1, vy1 = naar(v[1] * 2400, v[3] * 1350)
    nx0, ny0 = naar(n[0] * 2400, n[2] * 1350)
    nx1, ny1 = naar(n[1] * 2400, n[3] * 1350)
    _, by0 = naar(0, b[2] * 1350)
    _, by1 = naar(0, b[3] * 1350)
    bx_mid, _ = naar((b[0] + b[1]) / 2 * 2400, 0)
    # pijl tussen voor en na
    py = by0 + 0.15 * (by1 - by0)
    pijl(img, vx1 + 10, py, nx0 - 4, py, GOUD)
    schaduwtekst(img, ((vx1 + nx0) / 2, py - 112), "1 click", font("Bricolage.ttf", 50, "Bold"), GOUD, anchor="ma")
    # labels
    onder = min(max(vy1, ny1) + 10, S - 116)  # ronde 2: labels groter (Gemini)
    fl = font("Inter.ttf", 42, "Bold")
    fk = font("Inter.ttf", 38, "SemiBold")
    schaduwtekst(img, (bx_mid, onder), f"{meta['hoogte_mm']:.0f} mm tall", fl, CREME, schaduw=6, anchor="ma")
    schaduwtekst(img, (bx_mid, onder + 50), f"gold box: {meta['bed_mm']:.0f} mm bed", fk, GOUD, schaduw=6, anchor="ma")
    nm = (nx0 + nx1) / 2
    schaduwtekst(img, (nm, onder), f"{meta['stukken']} parts, {meta['pennen']} pins", fl, CREME, schaduw=6, anchor="ma")
    schaduwtekst(img, (nm, onder + 50), "every part fits", fk, GOUD, schaduw=6, anchor="ma")

    rgb = img.convert("RGB")
    rgb.save(os.path.join(UIT, "paard-vierkant-1200x1200.jpg"), quality=93, subsampling=0)
    rgb.resize((600, 600), Image.LANCZOS).save(os.path.join(UIT, "paard-vierkant-600x600.jpg"), quality=93,
                                              subsampling=0)
    rgb.resize((200, 200), Image.LANCZOS).save(os.path.join(UIT, "_paard-vierkant-200.png"))
    print("klaar")


main()
