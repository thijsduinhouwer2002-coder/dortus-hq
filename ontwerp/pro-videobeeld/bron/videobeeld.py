"""Videobeeld (YouTube-thumbnail) voor de lange Click Joints Pro-video 4-3l3MZZWPc (Beeldmaker, 26 nov 2026, #94 stap 3).

python3 videobeeld.py <render-klik.png> <klik.json> <uitmap> <fontmap met Bricolage.ttf en Inter.ttf> <icoon.svg> [naam]

Uit één render van 2400x1350 (workflow pro-videobeeld.yml, release pro-videobeeld-1): links het MakeHuman-figuur zoals
je het aanlevert (half doorzichtig, met de botten van de rig), rechts de delen uit de echte knop Figure from rig.
Erop: icoon en naam, de titel in 3 tot 4 woorden groot (leesbaar op een telefoon), één regel wat het doet, en een
gouden pijl met "1 click" tussen de twee figuren. Maakt <naam>-1280x720.jpg (YouTube) en <naam>-1920x1080.jpg.
Het aantal gewrichten komt uit klik.json, dus uit wat de add-on maakte.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RENDER, META, UIT, FONTS, ICOON = sys.argv[1:6]
NAAM = sys.argv[6] if len(sys.argv) > 6 else "videobeeld"
os.makedirs(UIT, exist_ok=True)
CREME, GOUD, ZACHT, DONKER, BLAUW = (255, 246, 230), (255, 196, 84), (226, 216, 232), (24, 16, 30), (79, 179, 255)
TITEL = os.environ.get("VB_TITEL", "Rig in.|Parts out.").split("|")
REGEL = os.environ.get("VB_REGEL", "Rigged figure to printable parts in Blender")
MAAT = int(os.environ.get("VB_MAAT", "176"))


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


def schaduw_tekst(img, stukken, blur, sterk=210):
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for (x, y), t, f, _k in stukken:
        d.text((x, y + blur // 3), t, font=f, fill=(0, 0, 0, sterk))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    for (x, y), t, f, k in stukken:
        d.text((x, y), t, font=f, fill=k)


def donker_links(img, breed, sterk):
    W, H = img.size
    m = Image.new("L", (W, 1), 0)
    for x in range(W):
        m.putpixel((x, 0), int(sterk * max(0.0, 1 - x / breed) ** 1.4))
    img.paste(Image.new("RGBA", (W, H), (10, 6, 14, 255)), (0, 0), m.resize((W, H)))


def pil(img, xy, tekst, maat, rand=GOUD):
    d = ImageDraw.Draw(img)
    f = font("Inter.ttf", maat, "Bold")
    bb = d.textbbox((0, 0), tekst, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    bw, bh = w + int(maat * 1.0), h + int(maat * 0.8)
    bx, by = xy[0] - bw // 2, xy[1] - bh // 2
    laag = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((bx, by + 6, bx + bw, by + bh + 6), radius=bh // 2, fill=(0, 0, 0, 160))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, fill=DONKER + (240,), outline=rand + (255,),
                        width=max(3, maat // 12))
    d.text((bx + (bw - w) // 2, by + (bh - h) // 2 - bb[1]), tekst, font=f, fill=CREME)


def passend(d, tekst, f, breed):
    regels, nu = [], ""
    for w in tekst.split(" "):
        proef = (nu + " " + w).strip()
        if d.textlength(proef, font=f) > breed and nu:
            regels.append(nu)
            nu = w
        else:
            nu = proef
    return regels + [nu]


def maak(basis, meta):
    """Alles op 1920x1080; daarna verkleind naar 1280x720."""
    img = basis.convert("RGBA").resize((1920, 1080), Image.LANCZOS)
    W, H = img.size
    donker_links(img, int(W * float(os.environ.get("VB_DONKER_BREED", "0.62"))), int(os.environ.get("VB_DONKER", "215")))
    x0, y = 84, 70
    ic = icoon(92)
    img.alpha_composite(ic, (x0, y))
    f_naam = font("Inter.ttf", 46, "Bold")
    schaduw_tekst(img, [((x0 + ic.width + 24, y + ic.height // 2 - 28), "Click Joints Pro", f_naam, ZACHT)], 8)
    y += ic.height + 40
    f_t = font("Bricolage.ttf", MAAT, "ExtraBold")
    kleuren = [CREME, GOUD, CREME]
    stukken = []
    for i, t in enumerate(TITEL):
        stukken.append(((x0 - 6, y), t, f_t, kleuren[i % 3]))
        y += int(MAAT * 1.02)
    schaduw_tekst(img, stukken, 18, 235)
    y += 26
    f_r = font("Inter.ttf", 50, "SemiBold")
    d = ImageDraw.Draw(img)
    for t in passend(d, REGEL, f_r, int(W * 0.40)):
        schaduw_tekst(img, [((x0, y), t, f_r, ZACHT)], 8)
        y += 64
    # gouden pijl met "1 click" tussen het figuur met rig en de delen
    kr, kd = meta["kaders"]["rig"], meta["kaders"]["delen"]
    links_x = kr[1][0] * W
    rechts_x = kd[0][0] * W
    py = int(H * float(os.environ.get("VB_PIJL_Y", "0.62")))
    x1, x2 = int(links_x + 10), int(rechts_x - 10)
    if x2 - x1 > 120:
        d = ImageDraw.Draw(img)
        d.line((x1, py, x2 - 40, py), fill=GOUD + (255,), width=12)
        d.polygon([(x2, py), (x2 - 54, py - 32), (x2 - 54, py + 32)], fill=GOUD + (255,))
        pil(img, ((x1 + x2) // 2, py - 74), "1 click", 44)
    n_s = sum(1 for g in meta.get("gewrichten", []) if " Hinge " in g)
    n_k = sum(1 for g in meta.get("gewrichten", []) if " Ball " in g)
    if os.environ.get("VB_TELLER", "1") == "1" and n_s + n_k:
        pil(img, (int((kd[0][0] + kd[1][0]) / 2 * W), int(H * 0.92)), f"{n_s + n_k} joints", 40)
    return img.convert("RGB")


def main():
    meta = json.load(open(META, encoding="utf-8"))
    r = Image.open(RENDER)
    groot = maak(r, meta)
    groot.save(os.path.join(UIT, f"{NAAM}-1920x1080.jpg"), quality=92)
    groot.resize((1280, 720), Image.LANCZOS).save(os.path.join(UIT, f"{NAAM}-1280x720.jpg"), quality=92)
    for f in os.listdir(UIT):
        if f.startswith("_icoon_"):
            os.remove(os.path.join(UIT, f))
    print("klaar", NAAM)


main()
