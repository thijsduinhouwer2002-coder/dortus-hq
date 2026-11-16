# Gloop: Hat Tower, winkelbeelden concept 1 (Mila, 16 nov 2026).
# 800x800 zoals Ebb. Elk scherm is een echte simulatoropname (tak schermen, run van Gijs op e5dbbf2/0b66a2a),
# 1x geplakt in een getekende horlogekast zonder merk. Achtergrond: de donkere warme grot met schuine bundel
# van het icoon, zodat icoon en beelden een familie zijn. Letters: Lilita One, zelfde als Het Hol.
#   python3 gloop_winkel_v1.py
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(HIER, '..', 'gloop-spel')
BRON = os.path.join(G, 'winkel', 'bron')
UIT = os.path.join(G, 'winkel')
KIT = os.path.join(G, 'kit', '454')
LET = os.path.join(HIER, '..', '..', 'steam', 'capsule-3d', 'LilitaOne-Regular.ttf')
W = 800
GEEL = (255, 214, 64)
MINT = (120, 255, 200)


def f(s): return ImageFont.truetype(LET, s)


def grot():
    im = Image.new('RGB', (W, W), (14, 8, 5))
    gl = Image.new('L', (W, W), 0)
    ImageDraw.Draw(gl).ellipse([-0.2 * W, 0.35 * W, 1.2 * W, 1.5 * W], fill=255)
    gl = gl.filter(ImageFilter.GaussianBlur(W * 0.16))
    im = Image.composite(Image.new('RGB', (W, W), (92, 44, 16)), im, gl)
    lam = Image.new('L', (W, W), 0); d = ImageDraw.Draw(lam)
    d.polygon([(W * 0.05, -10), (W * 0.38, -10), (W * 0.70, W), (W * 0.22, W)], fill=70)
    d.polygon([(W * 0.14, -10), (W * 0.28, -10), (W * 0.56, W), (W * 0.36, W)], fill=110)
    lam = lam.filter(ImageFilter.GaussianBlur(W * 0.03))
    im = Image.composite(Image.new('RGB', (W, W), (255, 200, 140)), im, lam.point(lambda v: int(v * 0.55)))
    d2 = ImageDraw.Draw(im)
    for x, y, r in [(0.16, 0.30, 4), (0.30, 0.52, 3), (0.22, 0.70, 4), (0.44, 0.86, 3), (0.12, 0.48, 2)]:
        d2.ellipse([x * W - r, y * W - r, x * W + r, y * W + r], fill=(255, 220, 160))
    return im


def horloge(doek, scherm, cx, cy, R, band=True):
    """Kast zonder merk: donkere ring, lichte rand, scherm op 1x of geschaald met LANCZOS."""
    d = ImageDraw.Draw(doek)
    sch = Image.new('L', doek.size, 0)
    ImageDraw.Draw(sch).ellipse([cx - R - 30, cy - R - 10, cx + R + 30, cy + R + 50], fill=170)
    doek.paste((0, 0, 0), (0, 0), sch.filter(ImageFilter.GaussianBlur(26)))
    # bandjes
    for y0, y1 in ([(cy + R - 40, cy + R + 400)] if band else []):
        d.rounded_rectangle([cx - R * 0.55, y0, cx + R * 0.55, y1], 30, fill=(24, 22, 22))
    rr = R + 26
    d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(30, 28, 28), outline=(120, 104, 90), width=4)
    d.ellipse([cx - R - 6, cy - R - 6, cx + R + 6, cy + R + 6], fill=(0, 0, 0))
    s = scherm.resize((2 * R, 2 * R), Image.LANCZOS) if scherm.width != 2 * R else scherm
    m = Image.new('L', (8 * R, 8 * R), 0); ImageDraw.Draw(m).ellipse([0, 0, 8 * R - 1, 8 * R - 1], fill=255)
    doek.paste(s, (cx - R, cy - R), m.resize((2 * R, 2 * R), Image.LANCZOS))
    # knop rechts (START)
    d.rounded_rectangle([cx + rr - 4, cy - R * 0.55, cx + rr + 14, cy - R * 0.35], 6, fill=(60, 54, 50))


def kop(doek, regels, y, maat):
    d = ImageDraw.Draw(doek)
    for tekst in regels:
        ft = f(maat)
        while d.textlength(''.join(t for t, _ in tekst), font=ft) > W * 0.92: maat -= 2; ft = f(maat)
        tot = sum(d.textlength(t, font=ft) for t, _ in tekst); x = (W - tot) / 2
        for t, k in tekst:
            d.text((x, y), t, font=ft, fill=k or (255, 246, 230), stroke_width=max(3, maat // 14), stroke_fill=(20, 8, 2))
            x += d.textlength(t, font=ft)
        y += int(maat * 1.08)
    return y


def sub(doek, tekst, y, maat=30):
    d = ImageDraw.Draw(doek); ft = f(maat)
    d.text(((W - d.textlength(tekst, font=ft)) / 2, y), tekst, font=ft, fill=(255, 226, 190), stroke_width=3, stroke_fill=(20, 8, 2))


def beeld(naam, scherm, regels, ondertekst, R=227, cy=None, boven=(), kop_y=26):
    doek = grot()
    y = kop(grot(), regels, 26, 74)   # eerst meten, dan horloge, dan letters erover
    horloge(doek, Image.open(os.path.join(BRON, scherm)).convert('RGB'), W // 2, cy or min(W - R - 34, y + 50 + R), R, band=kop_y < 100)
    if boven:
        # de toren loopt in het spel over de rand van het scherm; hier zie je hoe hij buiten het scherm doorgaat
        # (zelfde hoeden uit de kit, zelfde stap van 0,56 x hoedhoogte)
        cyy = cy or min(W - R - 34, y + 50 + R)
        z = 0.92 * R / 227; yb = cyy - R + int(14 * z); xb = W // 2 + 2
        for n, (fn, hoek, dx) in enumerate(boven):
            h = Image.open(os.path.join(KIT, fn)).convert('RGBA')
            h = h.resize((int(h.width * z), int(h.height * z)), Image.LANCZOS)
            rand = h.getchannel('A').point(lambda v: 255 if v > 60 else 0).filter(ImageFilter.MaxFilter(5))
            hr = Image.new('RGBA', h.size, (20, 8, 2, 0)); hr.putalpha(rand); hr.alpha_composite(h)
            hr = hr.rotate(hoek, expand=True, resample=Image.BICUBIC)
            xb += dx
            doek.paste(hr, (int(xb - hr.width / 2), int(yb - hr.height)), hr)
            yb -= h.height * 0.62
    kop(doek, regels, kop_y, 74)
    if ondertekst: sub(doek, ondertekst, y + 2)
    doek.save(os.path.join(UIT, naam))
    return doek


if __name__ == '__main__':
    beeld('concept-1-feed-him.png', 'venu3-14.png',
          [[('Feed him. ', None), ('Keep the hat.', GEEL)]],
          'One button. 30 seconds. Gloop does the rest.')
    beeld('concept-2-taller.png', 'venu3-21.png',
          [[('A tower of hats', None)], [('taller than your watch.', GEEL)]],
          '', R=176, cy=440, kop_y=640, boven=[('hoed-06-emmer.png', 4, 2), ('hoed-09-veermuts.png', -6, 6), ('hoed-03-pet.png', 3, 8), ('hoed-01-puntmuts.png', 10, 9), ('hoed-08-pan.png', -4, 10), ('hoed-07-hoge_hoed.png', 8, 10), ('hoed-05-koksmuts.png', 16, 13), ('hoed-04-kroon.png', 28, 16)])
    beeld('concept-5-mip.png', 'fr255-14.png',
          [[('Same Gloop. ', None), ('Older watch.', GEEL)]],
          'Forerunner 255 and other MIP screens.', R=227)
    print('klaar')
