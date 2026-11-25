"""Vierkante Gumroad-thumbnail met de robot (Beeldmaker, 25 nov 2026, issue #94).

python3 vierkant.py <render-1200x1200.png> <uitmap> <fontmap> <icoon.svg> [sale]

Maakt robot-vierkant-1200x1200.png en robot-vierkant-600x600.png (met "sale": robot-vierkant-sale-*),
uit één render van hoofdbeeld.py met HB_W=1200 HB_H=1200 (robot rechts). Links: icoon, "Click Joints Pro" groot,
"Rig in. Joints out." in goud en één regel wat het doet. Groot genoeg om op 100 px nog te lezen.
Sale: dezelfde gouden sticker als sale.py rechtsboven naast het hoofd (alleen Gumroad, 27 nov t/m 1 dec 2026).
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, UIT, FONTS, ICOON = sys.argv[1:5]
SALE = len(sys.argv) > 5 and sys.argv[5] == "sale"
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT, PRUIM = (255, 246, 230), (255, 196, 84), (226, 216, 232), (46, 31, 58)


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:  # noqa: BLE001
        pass
    return f


def icoon(maat):
    p = os.path.join(UIT, f"_icoon_{maat}.png")
    if not os.path.exists(p):
        os.system(f"rsvg-convert -w {maat} '{ICOON}' -o '{p}'")
    return Image.open(p).convert("RGBA")


def schaduw_tekst(img, stukken, blur):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for (x, y), t, f, _k in stukken:
        d.text((x, y + blur // 3), t, font=f, fill=(0, 0, 0, 200))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    for (x, y), t, f, k in stukken:
        d.text((x, y), t, font=f, fill=k)


def links_donker(img, breed):
    W, H = img.size
    m = Image.new("L", (W, 1), 0)
    for x in range(W):
        m.putpixel((x, 0), int(165 * max(0.0, 1 - x / breed) ** 1.5))
    img.paste(Image.new("RGBA", (W, H), (10, 6, 14, 255)), (0, 0), m.resize((W, H)))


def sticker(img, cx, cy, d):
    S = 3 * d
    st = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    g = ImageDraw.Draw(st)
    g.ellipse([0, 0, S - 1, S - 1], fill=GOUD + (255,))
    r = int(S * 0.045)
    g.ellipse([r, r, S - 1 - r, S - 1 - r], outline=PRUIM + (255,), width=max(3, int(S * 0.012)))
    for s_, f, y in (("-25%", font("Bricolage.ttf", int(S * 0.27), "ExtraBold"), 0.45),
                     ("CYBER25", font("Inter.ttf", int(S * 0.095), "Bold"), 0.68),
                     ("until Dec 1", font("Inter.ttf", int(S * 0.08), "SemiBold"), 0.81)):
        bx = g.textbbox((0, 0), s_, font=f)
        g.text(((S - (bx[2] - bx[0])) / 2 - bx[0], S * y - (bx[3] - bx[1]) / 2 - bx[1]), s_, font=f,
               fill=PRUIM + (255,))
    st = st.rotate(9, resample=Image.BICUBIC).resize((d, d), Image.LANCZOS)
    sch = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse([cx - d // 2 + 5, cy - d // 2 + 12, cx + d // 2 + 5, cy + d // 2 + 12],
                                fill=(0, 0, 0, 130))
    img.alpha_composite(sch.filter(ImageFilter.GaussianBlur(d // 14)))
    img.alpha_composite(st, (cx - d // 2, cy - d // 2))


def main():
    img = Image.open(RENDER).convert("RGBA")
    if img.size != (1200, 1200):
        img = img.resize((1200, 1200), Image.LANCZOS)
    links_donker(img, 760)
    x0, y = 64, 70
    ic = icoon(78)
    img.alpha_composite(ic, (x0, y))
    schaduw_tekst(img, [((x0 + ic.width + 20, y + ic.height // 2 - 20), "Add-on for Blender",
                         font("Inter.ttf", 32, "SemiBold"), ZACHT)], 6)
    y += ic.height + 26
    f_titel = font("Bricolage.ttf", 168, "ExtraBold")
    stukken = []
    for regel in ("Click", "Joints", "Pro"):
        stukken.append(((x0 - 8, y), regel, f_titel, GOUD if regel == "Pro" else CREME))
        y += 166
    schaduw_tekst(img, stukken, 14)
    y += 48
    f_slag = font("Bricolage.ttf", 78, "Bold")
    schaduw_tekst(img, [((x0, y), "Rig in.", f_slag, CREME), ((x0, y + 88), "Joints out.", f_slag, GOUD)], 10)
    y += 88 + 128
    f_punt = font("Inter.ttf", 34, "Medium")
    for t in ("Ball joints and hinges", "with bend limits, ready", "to 3D print"):
        schaduw_tekst(img, [((x0, y), t, f_punt, ZACHT)], 6)
        y += 46
    if SALE:
        sticker(img, 1050, 160, 250)
    naam = "robot-vierkant-sale" if SALE else "robot-vierkant"
    rgb = img.convert("RGB")
    rgb.save(os.path.join(UIT, f"{naam}-1200x1200.jpg"), quality=93, subsampling=0)
    rgb.resize((600, 600), Image.LANCZOS).save(os.path.join(UIT, f"{naam}-600x600.jpg"), quality=93, subsampling=0)
    rgb.resize((100, 100), Image.LANCZOS).save(os.path.join(UIT, f"_{naam}-100.png"))
    print("klaar", naam)


main()
