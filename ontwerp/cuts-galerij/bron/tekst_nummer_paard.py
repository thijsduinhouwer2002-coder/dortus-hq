"""Tekst op galerijbeeld Click Cuts "Numbered for assembly" met het hele paard (Beeldmaker, 26 nov 2026, issue #105).

python3 tekst_nummer_paard.py <render-paard.png> <nummer-paard.json> <render-naad.png> <nummer-naad.json> <uitmap> <fontmap> <icoon.svg>

Maakt nummer-paard-2400x1200.jpg (Superhive) en nummer-paard-1920x1080.jpg (Gumroad) uit renders van 2400x1350.
Links merk, titel en één regel. Midden het hele paard, gesneden door Click Cuts (nummer_paard.py). Rechts een kaart
met de close-up van één naad (snijvlak.py): het hoofd zakt op de borst, met de pennen en het gegraveerde nummer.
Een gouden lijn loopt van die naad in het paard naar de kaart. Getallen uit de twee json-bestanden, niets verzonnen.
Omgeving: KT_X, KT_Y, KT_B, KT_H (kaart), KT_LIJN_Y (waar de lijn de kaart raakt, deel van de beeldhoogte in de kaart).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, NAAD, NMETA, UIT, FONTS, ICOON = sys.argv[1:8]
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
    for w in tekst.split(" "):
        t = (nu + " " + w).strip()
        if f.getlength(t) > breed and nu:
            uit.append(nu)
            nu = w
        else:
            nu = t
    return uit + [nu]


def uitsnede(z, nm, bw, bh):
    """Snij de close-up bij rond beide stukken, in de verhouding van het beeldvak van de kaart."""
    zw, zh = z.size
    vs, vb = nm["vak_stuk"], nm["vak_buur"]
    x0, x1 = min(vs[0], vb[0]) * zw, max(vs[1], vb[1]) * zw
    y0, y1 = max(0.0, min(vs[2], vb[2])) * zh, min(1.0, max(vs[3], vb[3])) * zh
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    h = min(zh, max(y1 - y0, (x1 - x0) * bh / bw) * float(os.environ.get("KT_RUIMTE", "1.12")))
    w = h * bw / bh
    lx = min(max(cx - w / 2, 0), zw - w)
    ly = min(max(cy - h / 2, 0), zh - h)
    box = (int(lx), int(ly), int(lx + w), int(ly + h))
    lb = nm["label_beeld"]
    lp = ((lb[0] * zw - box[0]) * bw / (box[2] - box[0]), (lb[1] * zh - box[1]) * bh / (box[3] - box[1]))
    return z.crop(box).resize((bw, bh), Image.LANCZOS), lp


def main():
    m = json.load(open(META))
    nm = json.load(open(NMETA))
    img = Image.open(RENDER).convert("RGBA").resize((W, H), Image.LANCZOS)
    verloop = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(verloop)
    for x in range(1000):
        dv.line([(x, 0), (x, H)], fill=int(175 * (1 - x / 1000) ** 1.5))
    img = Image.composite(Image.new("RGBA", (W, H), (14, 8, 20, 255)), img, verloop)

    # links: merk, titel, één regel
    x = 120
    ic = icoon(84)
    img.alpha_composite(ic, (x, 150))
    schaduwtekst(img, (x + 104, 192), "Click Cuts", font("Bricolage.ttf", 64, "Bold"), CREME, anchor="lm")
    y = 300
    for regel, kl in (("Numbered", CREME), ("for assembly.", GOUD)):
        schaduwtekst(img, (x, y), regel, font("Bricolage.ttf", 112, "ExtraBold"), kl)
        y += 132
    y += 34
    a, b = nm["stuk"], nm["buur"]
    zin = (f"Cut faces get pin holes and an engraved part number, like {nm['label']} where part {a} "
           f"meets part {b}.")
    fz = font("Inter.ttf", 44, "Medium")
    for r in regels(zin, fz, 740):
        schaduwtekst(img, (x, y), r, fz, ZACHT, schaduw=6)
        y += 62
    # onder de regel: het hele paard in getallen, uit nummer-paard.json
    y += 40
    fk = font("Inter.ttf", 38, "SemiBold")
    schaduwtekst(img, (x, y), f"{m['stukken']} parts, {m['pennen']} pins, every part numbered", fk, GOUD, schaduw=6)

    # rechts: kaart met de close-up van de naad
    kx, ky = int(os.environ.get("KT_X", "1680")), int(os.environ.get("KT_Y", "150"))
    kb, kh = int(os.environ.get("KT_B", "600")), int(os.environ.get("KT_H", "1050"))
    onder = 170
    bh = kh - onder
    z, lp = uitsnede(Image.open(NAAD).convert("RGBA"), nm, kb, bh)
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((kx + 10, ky + 18, kx + kb + 10, ky + kh + 18), radius=32,
                                           fill=(0, 0, 0, 160))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(18)))
    kaart = Image.new("RGBA", (kb, kh), (20, 12, 28, 255))
    kaart.paste(z, (0, 0))
    masker = Image.new("L", (kb, kh), 0)
    ImageDraw.Draw(masker).rounded_rectangle((0, 0, kb - 1, kh - 1), radius=32, fill=255)

    # gouden lijn van de naad in het paard naar de kaart (onder de kaart getekend)
    if m.get("naad_beeld"):
        nx, ny = m["naad_beeld"][0] * W, m["naad_beeld"][1] * H
        ly = ky + (bh * float(os.environ["KT_LIJN_Y"]) if os.environ.get("KT_LIJN_Y") else lp[1])
        d = ImageDraw.Draw(img)
        d.line([(nx, ny), (kx + 4, ly)], fill=GOUD + (255,), width=4)
        r = 13
        d.ellipse((nx - r, ny - r, nx + r, ny + r), fill=GOUD + (255,), outline=(20, 12, 28, 255), width=3)
    img.paste(kaart, (kx, ky), masker)
    d = ImageDraw.Draw(img)
    d.line([(kx + 30, ky + bh), (kx + kb - 30, ky + bh)], fill=(255, 210, 92, 90), width=2)
    d.rounded_rectangle((kx, ky, kx + kb, ky + kh), radius=32, outline=GOUD + (255,), width=4)
    # pil bij het gegraveerde nummer in de close-up
    px, py = kx + lp[0], ky + lp[1]
    fp = font("Inter.ttf", 32, "SemiBold")
    pt = f"{nm['label']} engraved"
    pw = fp.getlength(pt) + 36
    bx = min(max(px - pw / 2 + float(os.environ.get("KT_PIL_DX", "0")), kx + 24), kx + kb - 24 - pw)
    by = py + float(os.environ.get("KT_PIL_DY", "70"))
    d.line([(px, py + 10), (bx + pw / 2, by)], fill=GOUD + (255,), width=3)
    d.ellipse((px - 7, py - 7, px + 7, py + 7), fill=GOUD + (255,))
    d.rounded_rectangle((bx, by, bx + pw, by + 50), radius=25, fill=(20, 12, 28, 235), outline=GOUD + (255,), width=3)
    d.text((bx + pw / 2, by + 25), pt, font=fp, fill=CREME, anchor="mm")
    tx, ty = kx + 40, ky + bh + 38
    schaduwtekst(img, (tx, ty), f"Part {b} drops onto part {a}", font("Bricolage.ttf", 44, "Bold"), CREME,
                 schaduw=5)
    schaduwtekst(img, (tx, ty + 60), f"{nm['pen_d_mm']:g} mm pins, {nm['speling_mm']:g} mm clearance",
                 font("Inter.ttf", 34, "Medium"), GOUD, schaduw=5)

    naam = os.environ.get("KT_NAAM", "nummer-paard")
    rgb = img.convert("RGB")
    rgb.crop((0, 75, W, 75 + 1200)).save(os.path.join(UIT, f"{naam}-2400x1200.jpg"), quality=92)
    rgb.resize((1920, 1080), Image.LANCZOS).save(os.path.join(UIT, f"{naam}-1920x1080.jpg"), quality=92)
    print("klaar", naam)


main()
