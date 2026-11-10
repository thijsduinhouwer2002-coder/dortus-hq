# Mila 10 nov run 10: schermafbeeldingen v2 (Daan keuring 6). Echte opnames van de strook op 1920 breed
# (workflow steam-hol-winkel.yml, tak schermen, map steam-hol/winkel-1920/los/). Geen tekst, geen kaders, geen merk.
# Het bureaublad is decor (eigen tekening: avondlucht, een neutraal venster, een kale taakbalk), de strook is de echte
# opname met zijn doorzichtige lucht, zoals hij in het spel boven de taakbalk ligt.
#   python3 maak_schermen2.py bureau <opname.png> <uit.png>            hele scherm, 1:1
#   python3 maak_schermen2.py zoom <opname.png> <x_midden> <k> <uit.png>  stuk van het bureaublad k keer (2 of 3), strook onderaan
import sys
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 1080
BALK_H = 48
STROOK_H = 120

def lucht(w, h, k):
    """Avondlucht in bureaublad-coordinaten maal k. Rustig, zodat de strook en het venster spreken."""
    im = Image.new("RGB", (w, h))
    px = im.load()
    boven, midden, onder = (0x14, 0x0e, 0x24), (0x4a, 0x2c, 0x5a), (0xe0, 0x8a, 0x5c)
    for y in range(h):
        t = y / h
        if t < 0.45:
            u = t / 0.45; a, b = boven, midden
        else:
            u = min(1, (t - 0.45) / 0.27); a, b = midden, onder
        c = tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))
        for x in range(w):
            px[x, y] = c
    d = ImageDraw.Draw(im)
    # sterren (vast patroon), maan
    import random
    r = random.Random(3)
    for _ in range(140):
        x, y = r.random() * W, r.random() * H * 0.55
        s = r.choice([1, 1, 1, 2]) * k
        d.rectangle((x * k, y * k, x * k + s - 1, y * k + s - 1), fill=(0xe8, 0xdc, 0xf0))
    mx, my, mr = 1560 * k, 190 * k, 62 * k
    gloed = Image.new("L", (w, h), 0)
    ImageDraw.Draw(gloed).ellipse((mx - mr * 3, my - mr * 3, mx + mr * 3, my + mr * 3), fill=70)
    gloed = gloed.filter(ImageFilter.GaussianBlur(40 * k))
    im.paste((0xf7, 0xd9, 0xa8), (0, 0), gloed)
    d.ellipse((mx - mr, my - mr, mx + mr, my + mr), fill=(0xfa, 0xe8, 0xc0))
    # verre heuvels, laag en donker, ruim boven de strook zodat ze niet met het gras botsen
    for (hy, kl, amp, f) in ((H - 330, (0x4a, 0x30, 0x58), 40, 0.004), (H - 270, (0x33, 0x22, 0x40), 30, 0.007)):
        pts = [(0, h)]
        import math
        for x in range(0, W + 20, 20):
            pts.append((x * k, (hy - amp * (0.6 * math.sin(x * f + hy) + 0.4 * math.sin(x * f * 2.3))) * k))
        pts.append((w, h))
        d.polygon(pts, fill=kl)
    return im

def venster(d, k):
    """Een neutraal venster als 'je werk': geen merk, geen echte woorden."""
    x0, y0, x1, y1 = 260, 110, 1100, 830
    S = lambda *v: tuple(int(a * k) for a in v)
    d.rounded_rectangle(S(x0 + 10, y0 + 14, x1 + 10, y1 + 14), radius=12 * k, fill=(0x0c, 0x08, 0x12))
    d.rounded_rectangle(S(x0, y0, x1, y1), radius=10 * k, fill=(0x2a, 0x25, 0x31))
    d.rounded_rectangle(S(x0, y0, x1, y0 + 44), radius=10 * k, fill=(0x22, 0x1d, 0x28))
    d.rectangle(S(x0, y0 + 30, x1, y0 + 44), fill=(0x22, 0x1d, 0x28))
    for i, c in enumerate([(0x6a, 0x62, 0x72)] * 3):
        cx = x1 - 30 - i * 34
        d.rectangle(S(cx - 7, y0 + 21, cx + 7, y0 + 23), fill=c)
    grijs = (0x4a, 0x43, 0x54)
    y = y0 + 90
    d.rounded_rectangle(S(x0 + 60, y, x0 + 470, y + 22), radius=4 * k, fill=(0x7a, 0x70, 0x86))
    y += 64
    lengtes = [720, 690, 740, 610, 0, 700, 730, 520, 0, 680, 710, 745, 640, 0, 560]
    for L in lengtes:
        if L:
            d.rounded_rectangle(S(x0 + 60, y, x0 + 60 + L, y + 12), radius=3 * k, fill=grijs)
        y += 36

def taakbalk(d, k):
    y = H - BALK_H
    d.rectangle((0, y * k, W * k, H * k), fill=(0x1b, 0x16, 0x22))
    d.line((0, y * k, W * k, y * k), fill=(0x2c, 0x25, 0x35), width=max(1, k))
    for i in range(5):
        cx = 40 + i * 48
        d.rounded_rectangle(((cx - 14) * k, (y + 10) * k, (cx + 14) * k, (y + 38) * k), radius=6 * k, fill=(0x34, 0x2c, 0x3f))
    d.rounded_rectangle(((W - 120) * k, (y + 18) * k, (W - 30) * k, (y + 30) * k), radius=3 * k, fill=(0x34, 0x2c, 0x3f))

def bureau(k, opname):
    im = lucht(W * k, H * k, k)
    d = ImageDraw.Draw(im)
    venster(d, k)
    taakbalk(d, k)
    s = Image.open(opname).convert("RGBA")
    if s.size != (W, STROOK_H):
        raise SystemExit(f"opname is {s.size}, verwacht {(W, STROOK_H)}")
    s = s.resize((W * k, STROOK_H * k), Image.NEAREST)
    im = im.convert("RGBA")
    im.alpha_composite(s, (0, (H - BALK_H - STROOK_H) * k))
    return im.convert("RGB")

if __name__ == "__main__":
    if sys.argv[1] == "bureau":
        bureau(1, sys.argv[2]).save(sys.argv[3])
    else:
        opname, xm, k, uit = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        groot = bureau(k, opname)
        cw, ch = W, H                      # uitsnede in pixels van het k-keer bureaublad
        x0 = max(0, min(W * k - cw, xm * k - cw // 2))
        x0 -= x0 % (3 * k)                 # op de spelpixelrand
        groot.crop((x0, H * k - ch, x0 + cw, H * k)).save(uit)
