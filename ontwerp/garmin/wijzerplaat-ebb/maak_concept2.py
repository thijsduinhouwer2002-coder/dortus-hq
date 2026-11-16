# Mila, 16 nov 2026, concept 2 "Ebb Porthole" (Daans moets 11:00 UTC: geen "tide", koperen patrijspoortrand met zes boutjes; kan: sterren, golf niet door de cijfers).
# Concept 1: (bericht hoofdchat 09:55 NL, tweede wijzerplaat).
# Haak 1: je stappen zijn het tij. Het water in de patrijspoort stijgt met je stappen; bij je doel is het vloed.
# Haak 2: elk uur zwemt er een ander dier uit Ebb langs (24 van de 25), en alleen bij vloed komt de walvis.
# Dieren uit Ebb (ontwerp/garmin/dieren83/alle25-454.png: rij 1, 3, 5 kleur, rij 2, 4, 6 silhouet), dus dezelfde dieren als de app.
import os, math
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
BLAD = Image.open(os.path.join(HIER, '../dieren83/alle25-454.png')).convert('RGB')
F = os.path.join(HIER, '../bron/fonts/BarlowCondensed-SemiBold.ttf')
NAMEN = ['Fish', 'Shrimp', 'Jellyfish', 'Turtle', 'Crab', 'Seahorse', 'Starfish', 'Clownfish', 'Pufferfish', 'Octopus', 'Eel', 'Ray',
         'Seal', 'Dolphin', 'Swordfish', 'Sea otter', 'Manta', 'Shark', 'Sunfish', 'Orca', 'Narwhal', 'Squid', 'Lobster', 'Whale', 'Sea cucumber']
WALVIS = 23

def dier(nr, silhouet=False):
    """Uitsnede van dier nr (0..24) uit het blad, zwart wordt doorzichtig."""
    rij, kol = divmod(nr, 9)
    cw, ch = BLAD.width / 9, BLAD.height / 6
    y0 = round((rij * 2 + (1 if silhouet else 0)) * ch)
    vak = BLAD.crop((round(kol * cw), y0, round((kol + 1) * cw), round(y0 + ch)))
    al = vak.convert('L').point(lambda v: 255 if v > 18 else 0)
    im = vak.convert('RGBA'); im.putalpha(al)
    return im.crop(im.getbbox())

def tekst(d, xy, s, maat, kleur, anker='mm', rand=0):
    d.text(xy, s, font=ImageFont.truetype(F, maat), fill=kleur, anchor=anker, stroke_width=rand, stroke_fill=(0, 10, 30))

def maak(W, stappen, doel, uur, minuut, datum, hart, accu, aod=False):
    im = Image.new('RGBA', (W, W), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
    frac = min(1.0, stappen / doel)   # nooit droog: ook om 0 stappen zwemt het dier van het uur
    nr = WALVIS if stappen >= doel else [i for i in range(25) if i != WALVIS][uur % 24]
    if not aod:
        # lucht: nachtblauw boven, het water stijgt van onder; drie vaste tinten (MIP-palet 0055AA, 00AAFF, 00FFFF-rand)
        d.ellipse((0, 0, W - 1, W - 1), fill=(0, 0, 40))
        lijn = W * (0.70 - 0.27 * frac)   # bij vloed net onder de tijd: de golf loopt nooit door de cijfers
        # sterren in de lucht, alleen boven het water en niet achter de tekst (vaste plekken, MIP-kleuren)
        for sx, sy, sr in ((0.24, 0.20, 1.0), (0.78, 0.22, 1.0), (0.18, 0.36, 0.7), (0.84, 0.38, 0.8), (0.12, 0.52, 0.6), (0.90, 0.56, 0.7)):
            if W * sy < lijn - W * 0.04:
                r = max(1, round(W * 0.007 * sr)); x, y = W * sx, W * sy
                d.rectangle((x - r * 2, y - r / 2, x + r * 2, y + r / 2), fill=(255, 255, 170)); d.rectangle((x - r / 2, y - r * 2, x + r / 2, y + r * 2), fill=(255, 255, 170))
        # maan: een sikkel rechtsboven, verdwijnt zodra het water hoog staat
        if lijn > W * 0.55:
            mx, my, mr = W * 0.70, W * 0.14, W * 0.035
            d.ellipse((mx - mr, my - mr, mx + mr, my + mr), fill=(255, 255, 170)); d.ellipse((mx - mr * 0.45, my - mr * 1.1, mx + mr * 1.5, my + mr * 0.9), fill=(0, 0, 40))
        for laag, kleur, dy in ((0, (0, 170, 255), 0), (1, (0, 85, 170), W * 0.16), (2, (0, 0, 85), W * 0.34)):
            pts = [(x, lijn + dy + W * 0.018 * math.sin(x / W * 2 * math.pi * 2.5 + laag)) for x in range(0, W + 1, 4)]
            d.polygon(pts + [(W, W), (0, W)], fill=kleur)
        pts = [(x, lijn + W * 0.018 * math.sin(x / W * 2 * math.pi * 2.5)) for x in range(0, W + 1, 4)]
        d.line(pts, fill=(0, 255, 255), width=max(2, W // 110))
        for bx, by, br in ((0.70, 0.08, 0.012), (0.76, 0.16, 0.008), (0.30, 0.22, 0.010)):
            if lijn + W * by < W * 0.95:
                d.ellipse((W * bx - W * br, lijn + W * by - W * br, W * bx + W * br, lijn + W * by + W * br), outline=(170, 255, 255), width=2)
    # het dier van het uur, in het water (bij laag tij net onder de golf, bij vloed midden in beeld)
    a = dier(nr, silhouet=aod)
    s = (0.42 if nr == WALVIS else 0.30) * W / a.width
    a = a.resize((round(a.width * s), round(a.height * s)), Image.NEAREST)
    if aod or nr == WALVIS:
        ay = W * (0.62 if aod else 0.68)
    else:
        ay = min(W * 0.68, max(W * 0.64, lijn + a.height / 2 + W * 0.05))   # altijd onder de stappen en boven de onderregel
    ax = round(W * 0.5 - a.width / 2); im.alpha_composite(a, (ax, round(ay - a.height / 2)))
    if nr == WALVIS and not aod:   # bij vloed blaast de walvis: een fontein van belletjes tot boven de golf
        d = ImageDraw.Draw(im)
        bx = ax + a.width * 0.30; by = ay - a.height / 2
        for i, (dx, dy, r) in enumerate(((0, -0.025, 0.011), (-0.018, -0.05, 0.009), (0.018, -0.05, 0.009), (-0.03, -0.07, 0.007), (0.03, -0.07, 0.007))):
            d.ellipse((bx + W * dx - W * r, by + W * dy - W * r, bx + W * dx + W * r, by + W * dy + W * r), fill=(220, 255, 255))
    # rond masker
    m = Image.new('L', (W, W), 0); ImageDraw.Draw(m).ellipse((0, 0, W - 1, W - 1), fill=255)
    zwart = Image.new('RGBA', (W, W), (0, 0, 0, 255)); im = Image.composite(im, zwart, m); d = ImageDraw.Draw(im)
    # patrijspoort: dunne koperen ring met zes boutjes; twee effen tinten plus een donkere binnenlijn (werkt ook op MIP)
    rb = max(5, round(W * 0.035)); KOPER, LICHT, DONK = (170, 85, 0), (255, 170, 85), (85, 0, 0)
    if aod: KOPER, LICHT, DONK = (60, 30, 0), (110, 55, 0), (0, 0, 0)
    d.ellipse((0, 0, W - 1, W - 1), outline=KOPER, width=rb)
    d.arc((1, 1, W - 2, W - 2), 200, 290, fill=LICHT, width=max(2, rb // 3))   # licht linksboven
    d.ellipse((rb - 1, rb - 1, W - rb, W - rb), outline=DONK, width=max(1, W // 200))
    for k in range(6):
        hoek = math.radians(30 + 60 * k); br = rb * 0.42
        bx, by = W / 2 + (W / 2 - rb / 2) * math.cos(hoek), W / 2 + (W / 2 - rb / 2) * math.sin(hoek)
        d.ellipse((bx - br, by - br, bx + br, by + br), fill=DONK)
        d.ellipse((bx - br * 0.75, by - br * 0.95, bx + br * 0.55, by + br * 0.35), fill=LICHT if not aod else KOPER)
    wit = (255, 255, 255) if not aod else (170, 170, 170)
    tekst(d, (W * 0.5, W * 0.30), '%d:%02d' % (uur, minuut), round(W * 0.26), wit, rand=0 if aod else max(2, W // 120))
    if not aod:
        tekst(d, (W * 0.5, W * 0.12), datum, round(W * 0.075), (255, 85, 85))
        onder = 'FULL SEA  ·  %s' % NAMEN[nr].upper() if stappen >= doel else '%d:00  ·  %s' % (uur, NAMEN[nr].upper())
        tekst(d, (W * 0.5, W * 0.885), onder, round(W * 0.06), (255, 255, 255), rand=2)
        tekst(d, (W * 0.5, W * 0.47), '{:,}'.format(stappen).replace(',', '.') + ' steps', round(W * 0.075), (0, 255, 255), rand=2)
        hx, hy, hr = W * 0.115, W * 0.50, W * 0.018   # hartje getekend (de letter kent geen hart)
        d.ellipse((hx - 2 * hr, hy - hr * 1.3, hx, hy + hr * 0.5), fill=(255, 85, 85)); d.ellipse((hx, hy - hr * 1.3, hx + 2 * hr, hy + hr * 0.5), fill=(255, 85, 85))
        d.polygon([(hx - 2 * hr, hy - hr * 0.2), (hx + 2 * hr, hy - hr * 0.2), (hx, hy + hr * 1.9)], fill=(255, 85, 85))
        tekst(d, (W * 0.15, W * 0.50), '%d' % hart, round(W * 0.055), (255, 85, 85), anker='lm', rand=2)
        tekst(d, (W * 0.83, W * 0.50), '%d%%' % accu, round(W * 0.055), (255, 255, 255), rand=2)
    return im

if __name__ == '__main__':
    W = 454
    standen = [maak(W, 2140, 10000, 8, 12, 'MON 16', 61, 88), maak(W, 6480, 10000, 14, 37, 'MON 16', 74, 61),
               maak(W, 10412, 10000, 19, 5, 'MON 16', 68, 40), maak(W, 10412, 10000, 19, 5, 'MON 16', 68, 40, aod=True)]
    blad = Image.new('RGBA', (W * 4 + 60, W + 40), (40, 40, 46, 255))
    for i, s in enumerate(standen):
        blad.alpha_composite(s, (20 + i * (W + 7), 20))
    blad.save(os.path.join(HIER, 'concept2-454-ochtend-middag-vloed-aod.png'))
    # op ware grootte voor de kijk: Venu 3 is 454 px op ±3 cm; 1x en een kleine 260-versie
    k = [maak(260, 6480, 10000, 14, 37, 'MON 16', 74, 61), maak(260, 10412, 10000, 19, 5, 'MON 16', 68, 40)]
    b2 = Image.new('RGBA', (560, 280), (40, 40, 46, 255))
    for i, s in enumerate(k): b2.alpha_composite(s, (10 + i * 285, 10))
    b2.save(os.path.join(HIER, 'concept2-260-middag-vloed.png'))
    print('klaar')
