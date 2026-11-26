"""Tekst op het hoofdbeeld met de robot (Beeldmaker, 25 nov 2026, issue #1).

python3 tekst.py <hoofdbeeld-render.png> <hoofdbeeld.json> <uitmap> <fontmap> <icoon.svg> <naam> [labels]

Maakt <naam>-2400x1200.png (Superhive) en <naam>-1920x1080.png (Gumroad) uit één render van 2400x1350.
Links: icoon, "Click Joints Pro", "Rig in. Joints out." en drie regels wat het doet. Met "labels": bij drie gewrichten
een plaatje met soort en bereik; die getallen komen uit hoofdbeeld.json (wat de add-on meldde), niet verzonnen.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON, NAAM = sys.argv[1:7]
LABELS = len(sys.argv) > 7 and sys.argv[7] == "labels"
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT = (255, 246, 230), (255, 196, 84), (226, 216, 232)

PUNTEN = [
    "One click: ball joints and hinges from your rig",
    "Elbows and knees stop where your rig stops",
    os.environ.get("TK_PUNT3", "Bend range in degrees, before you print"),   # #38: andere derde regel mogelijk
] + ([os.environ["TK_PUNT4"]] if os.environ.get("TK_PUNT4") else [])   # #38 ronde 5: vierde regel (export)


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
        d.text((x, y + blur // 3), t, font=f, fill=(0, 0, 0, 190))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    for (x, y), t, f, k in stukken:
        d.text((x, y), t, font=f, fill=k)


def links_donker(img, breed):
    """Zachte donkere overgang achter de tekst, zodat hij altijd leesbaar is."""
    W, H = img.size
    m = Image.new("L", (W, 1), 0)
    for x in range(W):
        t = x / breed
        m.putpixel((x, 0), int(150 * max(0.0, 1 - t) ** 1.6))
    m = m.resize((W, H))
    zwart = Image.new("RGBA", (W, H), (10, 6, 14, 255))
    img.paste(zwart, (0, 0), m)


def label(img, s, p, tekst, kant, zak=0):
    """Plaatje met tekst, met een lijntje en een stip naar het gewricht op p (pixels)."""
    d = ImageDraw.Draw(img)
    f = font("Inter.ttf", int(30 * s), "SemiBold")
    bb = d.textbbox((0, 0), tekst, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    px, py = p
    dx = int((150 if kant == "r" else -150) * s)
    bx = px + dx if kant == "r" else px + dx - w - int(36 * s)
    by = py - h // 2 - int(14 * s) + int(zak * s)   # zak: plaatje lager (#38, labels niet tegen elkaar)
    bw, bh = w + int(36 * s), h + int(28 * s)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((bx, by + 6, bx + bw, by + bh + 6), radius=bh // 2, fill=(0, 0, 0, 150))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    lx = bx if kant == "r" else bx + bw
    d.line((px, py, lx, by + bh // 2), fill=GOUD + (255,), width=max(2, int(3 * s)))
    r = int(9 * s)
    d.ellipse((px - r, py - r, px + r, py + r), fill=GOUD + (255,), outline=(20, 12, 24, 255), width=max(2, int(3 * s)))
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, fill=(24, 16, 30, 235), outline=GOUD + (255,),
                        width=max(2, int(2 * s)))
    d.text((bx + int(18 * s), by + int(14 * s) - bb[1]), tekst, font=f, fill=CREME)


def maak(basis, W, H, meta, dy, schaal_xy):
    img = basis.copy()
    s = H / 1200.0 if W / H > 1.9 else H / 1080.0 * 0.92
    s *= float(os.environ.get("TK_GROOT", "1"))   # #38: Daan (#17) wil de tekst 10 tot 15% groter
    links_donker(img, int(W * 0.62))
    x0 = int(W * 0.055)
    y = int(H * float(os.environ.get("TK_BOVEN", "0.11")))
    ic = icoon(int(96 * s))
    img.alpha_composite(ic, (x0, y))
    f_klein = font("Inter.ttf", int(36 * s), "Medium")
    schaduw_tekst(img, [((x0 + ic.width + int(26 * s), y + ic.height // 2 - int(24 * s)), "Add-on for Blender",
                         f_klein, ZACHT)], 8)
    y += ic.height + int(34 * s)
    f_titel = font("Bricolage.ttf", int(168 * s), "ExtraBold")
    stukken = []
    for regel in ("Click Joints", "Pro"):
        stukken.append(((x0 - int(6 * s), y), regel, f_titel, CREME))
        y += int(170 * s)
    schaduw_tekst(img, stukken, 14)
    y += int(22 * s)
    f_slag = font("Bricolage.ttf", int(82 * s), "Bold")
    schaduw_tekst(img, [((x0, y), "Rig in. Joints out.", f_slag, GOUD)], 10)
    y += int(128 * s)
    f_punt = font("Inter.ttf", int(38 * s), "Medium")
    d = ImageDraw.Draw(img)
    for t in PUNTEN:
        r = int(9 * s)
        cy = y + int(24 * s)
        d.ellipse((x0 + 2, cy - r, x0 + 2 + 2 * r, cy + r), fill=GOUD + (255,))
        schaduw_tekst(img, [((x0 + int(40 * s), y), t, f_punt, CREME)], 8)
        y += int(62 * s)
    if LABELS:
        lab = meta.get("labels", {})

        def p(naam):
            q = lab[naam]
            return (q["x"] * schaal_xy[0], q["y"] * schaal_xy[1] - dy)

        def graden(naam, soort):
            g = lab[naam].get("graden")
            if soort == "SCHARNIER" and g:
                return f"0–{round(float(g)):d}°"
            regel = next((r for r in meta.get("gewrichten", []) if r.startswith(naam + " ")), "")
            return regel.split(" · ")[2] if regel.count(" · ") >= 2 else ""
        keus = [("Left shoulder", "Ball", "r"), ("Left elbow", "Hinge", "r"), ("Left knee", "Hinge", "r")]
        for naam, woord, kant in keus:
            if naam in lab:
                zak = json.loads(os.environ.get("TK_ZAK", "{}")).get(naam, 0)
                label(img, s, p(naam), f"{woord} {graden(naam, lab[naam]['soort'])}", kant, zak)
    return img.convert("RGB")


def main():
    meta = json.load(open(META, encoding="utf-8"))
    r = Image.open(RENDER).convert("RGBA")
    if r.size != (2400, 1350):
        r = r.resize((2400, 1350), Image.LANCZOS)
    a = r.crop((0, 75, 2400, 1275))
    maak(a, 2400, 1200, meta, 75, (2400, 1350)).save(os.path.join(UIT, f"{NAAM}-2400x1200.png"), optimize=True)
    b = r.resize((1920, 1080), Image.LANCZOS)
    maak(b, 1920, 1080, meta, 0, (1920, 1080)).save(os.path.join(UIT, f"{NAAM}-1920x1080.png"), optimize=True)
    print("klaar", NAAM)


main()
