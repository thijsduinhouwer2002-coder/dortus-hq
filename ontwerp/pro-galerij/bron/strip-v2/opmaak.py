"""Opmaak nieuw strip-beeld: doorsnede groot, uitvergroting van het spleetje, rij nummers. Stijl van ontwerp/pro-galerij."""
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

R = '/home/claude/render/'
FONTS = '/tmp/f'
ICOON = '/tmp/hc/ontwerp/click-joints/bron/icoon.svg'
CREME, GOUD, ZACHT, DONKER = (255, 246, 230), (255, 196, 84), (226, 216, 232), (24, 16, 30)
PRO = '--zonder-pro' not in sys.argv


def font(naam, maat, gewicht):
    f = ImageFont.truetype(os.path.join(FONTS, naam), maat)
    try:
        f.set_variation_by_name(gewicht)
    except Exception:
        pass
    return f


def schaduw(img, stukken, blur):
    laag = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for (x, y), t, f, _ in stukken:
        d.text((x, y + blur // 3), t, font=f, fill=(0, 0, 0, 200))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    for (x, y), t, f, k in stukken:
        d.text((x, y), t, font=f, fill=k)


def pil(img, xy, tekst, maat=30, rand=GOUD):
    d = ImageDraw.Draw(img)
    f = font('Inter.ttf', maat, 'SemiBold')
    bb = d.textbbox((0, 0), tekst, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    bw, bh = w + 36, h + 28
    x, y = xy
    bx, by = x - bw // 2, y - bh // 2
    laag = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(laag).rounded_rectangle((bx, by + 6, bx + bw, by + bh + 6), radius=bh // 2, fill=(0, 0, 0, 150))
    img.alpha_composite(laag.filter(ImageFilter.GaussianBlur(10)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=bh // 2, fill=DONKER + (235,), outline=rand + (255,), width=3)
    d.text((bx + 18, by + 14 - bb[1]), tekst, font=f, fill=CREME)


def achtergrond(W, H):
    img = Image.new('RGBA', (W, H), (10, 6, 14, 255))
    gloed = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(gloed)
    d.ellipse((int(W * 0.48), int(H * 0.05), int(W * 1.05), int(H * 1.0)), fill=(70, 40, 110, 120))
    d.ellipse((-int(W * 0.2), int(H * 0.55), int(W * 0.5), int(H * 1.3)), fill=(120, 60, 40, 60))
    img.alpha_composite(gloed.filter(ImageFilter.GaussianBlur(220)))
    # vloer met perspectiefraster
    raster = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(raster)
    hor = int(H * 0.62); vx = W * 0.7
    for i in range(-30, 31):
        d.line((vx + i * 40, hor, vx + i * 260, H + 200), fill=(120, 100, 200, 40), width=2)
    y, stap = hor + 8, 10
    while y < H:
        d.line((0, y, W, y), fill=(120, 100, 200, 40), width=2)
        stap *= 1.28; y += stap
    m = Image.new('L', (1, H), 0)
    for yy in range(H):
        m.putpixel((0, yy), int(255 * max(0, min(1, (yy - hor) / (H - hor) * 1.6))))
    raster.putalpha(Image.composite(raster.split()[3], Image.new('L', (W, H), 0), m.resize((W, H))))
    img.alpha_composite(raster)
    return img


def maak(W, H, uit):
    img = achtergrond(W, H)
    s = H / 1200
    d = ImageDraw.Draw(img)

    # doorsnede: bovenste deel, groter, onderkant vervaagd
    ds = Image.open(R + 'f-doorsnede.png').convert('RGBA').crop((480, 190, 940, 1000))
    k = 0.98 * s
    ds = ds.resize((int(ds.width * k), int(ds.height * k)), Image.LANCZOS)
    a = ds.split()[3]
    m = Image.new('L', (1, ds.height), 255)
    for y in range(ds.height):
        m.putpixel((0, y), int(255 * max(0, min(1, (ds.height - y) / (ds.height * 0.22)))))
    ds.putalpha(Image.composite(a, Image.new('L', ds.size, 0), m.resize(ds.size)))
    dx, dy = int(W * 0.47), int(H * 0.5 - ds.height * 0.5)
    img.alpha_composite(ds, (dx, dy))
    # bovenkant spleet in de doorsnede (gemeten: goud x 597-804, y 532-754 in de render)
    gx = dx + int((700 - 480) * k); gy = dy + int((532 - 190) * k)

    pil(img, (dx + ds.width // 2, dy - int(30 * s)), 'cut open to show the inside', int(26 * s), rand=(150, 130, 170))
    # uitvergroting, rond
    D = int(470 * s)
    zm = Image.open(R + 'f-zoom.png').convert('RGBA').crop((150, 88, 750, 688)).resize((D, D), Image.LANCZOS)
    mask = Image.new('L', (D, D), 0); ImageDraw.Draw(mask).ellipse((0, 0, D - 1, D - 1), fill=255)
    zx, zy = int(W - D - 90 * s), int(90 * s)
    # lijnen van spleet naar cirkel
    d.line((gx, gy, zx + D * 0.15, zy + D * 0.85), fill=GOUD + (200,), width=max(2, int(3 * s)))
    d.ellipse((gx - 12 * s, gy - 12 * s, gx + 12 * s, gy + 12 * s), outline=GOUD, width=max(2, int(4 * s)))
    sch = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse((zx, zy + 14, zx + D, zy + D + 14), fill=(0, 0, 0, 170))
    img.alpha_composite(sch.filter(ImageFilter.GaussianBlur(18)))
    img.paste(zm, (zx, zy), mask)
    d = ImageDraw.Draw(img)
    d.ellipse((zx, zy, zx + D, zy + D), outline=GOUD, width=max(3, int(5 * s)))
    # pijltje naar de spleet in de cirkel (spleet op y 328-348 van 900 -> na crop en schaal)
    sy = zy + int((338 - 88) / 600 * D)
    pil(img, (zx + D // 2, sy - int(80 * s)), 'this gap: 0.20 mm', int(32 * s))
    d.line((zx + D // 2, sy - int(52 * s), zx + D // 2, sy - int(6 * s)), fill=GOUD, width=max(3, int(4 * s)))
    d.polygon([(zx + D // 2 - 10 * s, sy - 20 * s), (zx + D // 2 + 10 * s, sy - 20 * s), (zx + D // 2, sy - 4 * s)], fill=GOUD)
    f = font('Inter.ttf', int(28 * s), 'Medium')
    for i, t in enumerate(['Same 12 mm ball in all five.', 'Only this gap changes.']):
        schaduw(img, [((zx + D // 2 - d.textlength(t, font=f) / 2, zy + D + int((24 + i * 40) * s)), t, f, ZACHT)], 6)

    # kop links
    x0, y = int(110 * s), int(80 * s)
    if PRO:
        p = R + f'_icoon_{int(72 * s)}.png'
        os.system(f"rsvg-convert -w {int(72 * s)} '{ICOON}' -o '{p}'")
        ic = Image.open(p).convert('RGBA'); img.alpha_composite(ic, (x0, y))
        schaduw(img, [((x0 + ic.width + int(22 * s), y + ic.height // 2 - int(20 * s)), 'Click Joints Pro',
                       font('Inter.ttf', int(32 * s), 'SemiBold'), ZACHT)], 8)
        y += ic.height + int(30 * s)
    ft = font('Bricolage.ttf', int(104 * s), 'ExtraBold')
    st = []
    for t in ['Find the fit', 'for your printer']:
        st.append(((x0 - int(4 * s), y), t, ft, CREME)); y += int(112 * s)
    schaduw(img, st, 14)
    y += int(18 * s)
    fr = font('Inter.ttf', int(40 * s), 'Medium')
    for t in ['Five gaps, 0.10 to 0.30 mm. Keep the', 'one that turns without wobble.']:
        schaduw(img, [((x0, y), t, fr, GOUD)], 8); y += int(56 * s)

    # rij nummers met labels
    y += int(40 * s)
    nr = Image.open(R + 'f-nummers.png').convert('RGBA').crop((150, 80, 1450, 450))
    k2 = (int(W * 0.42) - x0) / nr.width
    nr = nr.resize((int(nr.width * k2), int(nr.height * k2)), Image.LANCZOS)
    img.alpha_composite(nr, (x0, y))
    stap = nr.width / 5
    for i, g in enumerate(['0.10', '0.15', '0.20', '0.25', '0.30']):
        pil(img, (int(x0 + stap * (i + 0.5)), y + nr.height + int(36 * s)), f'{g} mm', int(26 * s),
            rand=GOUD if g == '0.20' else (150, 130, 170))
    y += nr.height + int(36 * s)

    # kaartje van de robot (uit het geslaagde strip-beeld)
    if PRO:
        kaart = Image.open('/tmp/hc/ontwerp/pro-galerij/beelden/strip-1920x1080.jpg').convert('RGBA').crop((96, 668, 684, 1002))
        kk = 0.70 * s * 1.25
        kaart = kaart.resize((int(kaart.width * kk), int(kaart.height * kk)), Image.LANCZOS)
        km = Image.new('L', kaart.size, 0); ImageDraw.Draw(km).rounded_rectangle((2, 2, kaart.width - 3, kaart.height - 3), radius=int(24 * kk), fill=255)
        kx, ky = int(W - kaart.width - 90 * s), int(H - kaart.height - 70 * s)
        img.paste(kaart, (kx, ky), km)
    img.convert('RGB').save(uit, quality=92)


maak(2400, 1200, R + 'strip-v2-2400x1200.jpg')
big = R + '_strip_2400x1350.jpg'
maak(2400, 1350, big)
Image.open(big).resize((1920, 1080), Image.LANCZOS).save(R + 'strip-v2-1920x1080.jpg', quality=92)
print('ok')
