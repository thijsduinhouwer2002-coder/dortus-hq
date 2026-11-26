"""Tekst op galerijbeeld Click Cuts "Magnet holes or pins" (Beeldmaker, 26 nov 2026, issue #137; tekst #200).

python3 tekst_magneet.py <render-paard.png> <paard.json> <render-macro.png> <macro.json> <uitmap> <fontmap> <icoon.svg>

Maakt magneet-2400x1200.jpg (Superhive) en magneet-1920x1080.jpg (Gumroad) uit renders van 2400x1350.
Zelfde opzet als "Numbered for assembly" (tekst_nummer_paard.py, GESLAAGD): links merk, titel en één regel; midden
het hele paard, gesneden door Click Cuts met Joint: Magnets (nummer_paard.py, HB_VERBINDER=MAGNET), met een
schijfmagneet in elk gat; rechts een kaart met de naad 5-9 van dichtbij (snijvlak.py): magneet in het gat en het
gegraveerde nummer. Getallen uit de json-bestanden, niets verzonnen.
Omgeving: KT_X, KT_Y, KT_B, KT_H (kaart), MG_CX (midden van de uitsnede, deel van de macro-breedte).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, MACRO, MMETA, UIT, FONTS, ICOON = sys.argv[1:8]
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT, DONKER = (255, 246, 230), (255, 210, 92), (222, 212, 232), (20, 12, 28)
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
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(schaduw)))
    ImageDraw.Draw(img).text(xy, tekst, font=f, fill=kleur, anchor=anchor)


def regels(tekst, f, breed):
    uit, nu = [], ""
    for w in tekst.split(" "):
        t = (nu + " " + w).strip()
        if f.getlength(t) > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = t
    return uit + [nu]


def main():
    m = json.load(open(META))
    mm = json.load(open(MMETA))
    img = Image.open(RENDER).convert("RGBA").resize((W, H), Image.LANCZOS)
    verloop = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(verloop)
    for x in range(1000):
        dv.line([(x, 0), (x, H)], fill=int(175 * (1 - x / 1000) ** 1.5))
    img = Image.composite(Image.new("RGBA", (W, H), (14, 8, 20, 255)), img, verloop)

    # links: merk, titel, één regel
    x = 120
    img.alpha_composite(icoon(84), (x, 150))
    schaduwtekst(img, (x + 104, 192), "Click Cuts", font("Bricolage.ttf", 64, "Bold"), CREME, anchor="lm")
    y = 300
    for regel, kl in (("Magnet holes", CREME), ("or pins.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 112, "ExtraBold"), kl)
        y += 132
    y += 34
    zin = "Pick Magnets instead of pins: each cut gets a hole on both sides where a disc magnet fits, sized with your clearance."
    fz = font("Inter.ttf", 44, "Medium")
    for r in regels(zin, fz, 740):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 62
    y += 40
    schaduwtekst(img, (x, y), f"{m['stukken']} parts, {m['pennen']} magnet holes", font("Inter.ttf", 38, "SemiBold"),
                 GOUD, schaduw=6)
    schaduwtekst(img, (x, y + 58), "5 sizes, 5x2 to 10x3 mm. Magnets not included.", font("Inter.ttf", 32, "Medium"),
                 ZACHT, schaduw=5)

    # rechts: kaart met de naad van dichtbij, uit de macro-render (staande uitsnede rond de magneet en het nummer)
    kx, ky = int(os.environ.get("KT_X", "1680")), int(os.environ.get("KT_Y", "150"))
    kb, kh = int(os.environ.get("KT_B", "600")), int(os.environ.get("KT_H", "1050"))
    onder = 170
    bh = kh - onder
    z = Image.open(MACRO).convert("RGBA")
    zw, zh = z.size
    links = min(mm["pennen_beeld"], key=lambda p: p[0])
    lb = mm["label_beeld"]
    ch = zh
    cw = ch * kb / bh
    cx = float(os.environ["MG_CX"]) * zw if os.environ.get("MG_CX") else (links[0] + lb[0]) / 2 * zw
    lx = min(max(cx - cw / 2, 0), zw - cw)
    box = (int(lx), 0, int(lx + cw), int(ch))
    kaartbeeld = z.crop(box).resize((kb, bh), Image.LANCZOS)
    sc = kb / (box[2] - box[0])
    mag = ((links[0] * zw - box[0]) * sc, links[1] * zh * sc)
    lab = ((lb[0] * zw - box[0]) * sc, lb[1] * zh * sc)

    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((kx + 10, ky + 18, kx + kb + 10, ky + kh + 18), radius=32,
                                           fill=(0, 0, 0, 160))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(18)))
    kaart = Image.new("RGBA", (kb, kh), DONKER + (255,))
    kaart.paste(kaartbeeld, (0, 0))
    masker = Image.new("L", (kb, kh), 0)
    ImageDraw.Draw(masker).rounded_rectangle((0, 0, kb - 1, kh - 1), radius=32, fill=255)

    # gouden lijn van de naad in het paard naar de kaart
    if m.get("naad_beeld"):
        nx, ny = m["naad_beeld"][0] * W, m["naad_beeld"][1] * H
        d = ImageDraw.Draw(img)
        d.line([(nx, ny), (kx + 4, ky + mag[1])], fill=GOUD + (255,), width=4)
        r = 13
        d.ellipse((nx - r, ny - r, nx + r, ny + r), fill=GOUD + (255,), outline=DONKER + (255,), width=3)
    img.paste(kaart, (kx, ky), masker)
    d = ImageDraw.Draw(img)
    d.line([(kx + 30, ky + bh), (kx + kb - 30, ky + bh)], fill=(255, 210, 92, 90), width=2)
    d.rounded_rectangle((kx, ky, kx + kb, ky + kh), radius=32, outline=GOUD + (255,), width=4)

    # pillen in de kaart: bij de magneet en bij het nummer
    fp = font("Inter.ttf", 32, "SemiBold")

    def pil(px, py, tekst, dy):
        pw = fp.getlength(tekst) + 36
        bx = min(max(px - pw / 2, kx + 24), kx + kb - 24 - pw)
        by = py + dy
        d.line([(px, py + (12 if dy > 0 else -12)), (bx + pw / 2, by + (0 if dy > 0 else 50))], fill=GOUD + (255,),
               width=3)
        d.rounded_rectangle((bx, by, bx + pw, by + 50), radius=25, fill=DONKER + (235,), outline=GOUD + (255,),
                            width=3)
        d.text((bx + pw / 2, by + 25), tekst, font=fp, fill=CREME, anchor="mm")

    d_mm = mm["pen_d_mm"]
    t_mm = float(mm["magneet"].split("x")[1])
    pil(kx + mag[0], ky + mag[1], f"{d_mm:g} x {t_mm:g} mm magnet", -float(os.environ.get("KT_PIL_DY", "130")))
    pil(kx + lab[0], ky + lab[1], f"{mm['label']} engraved", 90)
    tx, ty = kx + 40, ky + bh + 38
    schaduwtekst(img, (tx, ty), f"Where part {mm['buur']} sits on part {mm['stuk']}", font("Bricolage.ttf", 44, "Bold"), CREME,
                 schaduw=5)
    schaduwtekst(img, (tx, ty + 60), f"Hole {2 * (d_mm / 2 + mm['speling_mm']):g} mm, magnet {d_mm:g} mm",
                 font("Inter.ttf", 34, "Medium"), GOUD, schaduw=5)

    naam = os.environ.get("MG_NAAM", "magneet")
    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, f"{naam}-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, f"{naam}-1920x1080.jpg"), quality=92)
    print("klaar", naam)


main()
