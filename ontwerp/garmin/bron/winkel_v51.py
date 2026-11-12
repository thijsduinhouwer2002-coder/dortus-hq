# Winkelbeelden Ebb v5.1 (Mila, run 55, 12 nov): hoofdchat 07:25: posterkop 'Breathe. Make sea friends.' (harde eis),
# kaart 2 zonder halve cijfers in de uitsneden, nachthorloge met lichte rand. Basis: v5 (Mila, run 54, 12 nov): opdracht hoofdchat 06:00 "winkelbeelden met de werelden erin".
# Poster (1000) en vijf kaarten (800) in de stijl van v4 (nachtblauw, zee met schuimlijn, kop wit met één woord geel),
# maar nu met de werelden: krab met zwemband voorop, één kaart met vijf werelden, één met dag en nacht.
# ONTWERP: de schermen zijn de bladbeelden (454) van Mila. Gijs vervangt ze door echte simulatorschermen
# (zelfde scène, zelfde plek); de kast is hier een neutrale ring, in de echte versie de opname van de fenix 8.
#   python3 winkel_v5.py <uitmap>
import sys, os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
FX = os.path.join(B, 'fonts', 'BarlowCondensed-ExtraBold.woff')
FM = os.path.join(B, 'fonts', 'BarlowCondensed-Medium.ttf')
FS = os.path.join(B, 'fonts', 'BarlowCondensed-SemiBold.ttf')
def f(p, s): return ImageFont.truetype(p, s)
NACHT, DIEP, MIDDEN, SCHUIM, LICHT = (0, 0, 85), (0, 0, 170), (0, 85, 170), (0, 255, 255), (0, 170, 255)
WIT, GEEL = (255, 255, 255), (255, 255, 85)

SCHERM = {   # bladbeeld -> wordt in de echte versie de simulatorscène met dezelfde inhoud
    'krab-in': 'keuring2/krab-in-dag-454-wit.png',
    'krab-in-nacht': 'keuring2/krab-in-nacht-454-wit.png',
    'krab-hold': 'keuring2/krab-hold-dag-454-wit.png',
    'octopus': 'werelden5/octopus-in-dag-454.png',
    'whale': 'werelden5/whale-in-dag-454.png',
    'lobster': 'werelden5/lobster-in-dag-454.png',
    'shark': 'werelden5/shark-in-dag-454.png',
    'today': 'strand2/today-3-454.png',
    'sealog': 'onderwater1/sealog-dag-454.png',
}


def laad(naam):
    return Image.open(os.path.join(G, SCHERM[naam])).convert('RGB')


def rond(im, d):
    im = im.resize((d, d), Image.LANCZOS)
    m = Image.new('L', (d * 4, d * 4), 0); ImageDraw.Draw(m).ellipse([0, 0, d * 4 - 1, d * 4 - 1], fill=255)
    im.putalpha(m.resize((d, d), Image.LANCZOS))
    return im


def kast(doek, cx, cy, r, im, ring=.13, schaduw=True, gloed=None):
    """Patrijspoort: neutrale donkere kastring met 60 streepjes, glimrand, daarin het scherm."""
    R = int(r * (1 + ring))
    if schaduw:
        s = Image.new('L', doek.size, 0); ImageDraw.Draw(s).ellipse([cx - R, cy - R + 10, cx + R, cy + R + 14], fill=150)
        doek.paste((0, 0, 30), (0, 0), s.filter(ImageFilter.GaussianBlur(14)))
    if gloed:   # hoofdchat 07:25 punt 3: lichte gloed en rand, zodat een donker scherm niet wegvalt tegen de kaart
        g = Image.new('L', doek.size, 0); ImageDraw.Draw(g).ellipse([cx - R - 18, cy - R - 18, cx + R + 18, cy + R + 18], fill=120)
        doek.paste(gloed, (0, 0), g.filter(ImageFilter.GaussianBlur(16)))
    dr = ImageDraw.Draw(doek)
    dr.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(28, 30, 38))
    dr.ellipse([cx - R, cy - R, cx + R, cy + R], outline=(200, 200, 255) if gloed else (90, 96, 110), width=max(2, R // 70) + (2 if gloed else 0))
    for i in range(60):
        a = math.radians(i * 6); l = .55 if i % 5 == 0 else .3
        r1 = R - (R - r) * .2; r2 = R - (R - r) * (.2 + l)
        dr.line([(cx + r1 * math.sin(a), cy - r1 * math.cos(a)), (cx + r2 * math.sin(a), cy - r2 * math.cos(a))],
                fill=(120, 126, 140) if i % 5 == 0 else (70, 74, 86), width=max(1, R // (90 if i % 5 == 0 else 160)))
    dr.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], fill=(8, 8, 12))
    sc = rond(im, 2 * r)
    doek.paste(sc, (cx - r, cy - r), sc)


def zee(doek, W, H, y0=.60):
    dr = ImageDraw.Draw(doek)
    def golf(y, a, kl, fase, lijn=None, n=2.0):
        pts = [(x, y + a * math.sin(x / W * 2 * math.pi * n + fase)) for x in range(0, W + 1, 4)]
        dr.polygon(pts + [(W, H), (0, H)], fill=kl)
        if lijn: dr.line(pts, fill=lijn, width=4)
    golf(H * y0, 10, MIDDEN, .6, SCHUIM)
    golf(H * (y0 + .14), 8, DIEP, 2.1)
    golf(H * (y0 + .28), 6, (0, 0, 120), 4.0)
    for bx, by, br in [(0.06, y0 + .1, 10), (0.1, y0 + .18, 6), (0.93, y0 + .07, 9), (0.9, y0 + .16, 5), (0.95, y0 + .26, 7)]:
        dr.ellipse([W * bx - br, H * by - br, W * bx + br, H * by + br], outline=LICHT, width=3)


def kop(dr, W, y, tekst, geel, maat, breed=.93):
    while dr.textlength(tekst, font=f(FX, maat)) > W * breed: maat -= 2
    font = f(FX, maat)
    x = (W - dr.textlength(tekst, font=font)) / 2
    i = tekst.index(geel) if geel in tekst else len(tekst)
    for deel, kl in [(tekst[:i], WIT), (tekst[i:i + len(geel)], GEEL), (tekst[i + len(geel):], WIT)]:
        if deel: dr.text((x, y), deel, font=font, fill=kl); x += dr.textlength(deel, font=font)
    return maat


def onder(dr, W, y, tekst, maat):
    while dr.textlength(tekst, font=f(FM, maat)) > W * .94: maat -= 2
    dr.text((W / 2, y), tekst, font=f(FM, maat), fill=WIT, anchor='mt')


def briefje(doek, x, y, tekst, maat, hoek=-6, pijl=None):
    """Geel briefje met donkere letters, schuin, met een pijltje naar wat het aanwijst: de grap in één blik."""
    font = f(FX, maat)
    tmp = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    tw = int(tmp.textlength(tekst, font=font)); th = int(maat * 1.25)
    b = Image.new('RGBA', (tw + 36, th + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    d.rounded_rectangle([0, 0, b.width - 1, b.height - 1], radius=12, fill=GEEL + (255,))
    d.text((18, 6), tekst, font=font, fill=NACHT)
    b = b.rotate(hoek, expand=True, resample=Image.BICUBIC)
    doek.paste(b, (int(x - b.width / 2), int(y - b.height / 2)), b)
    if pijl:
        dr = ImageDraw.Draw(doek)
        (x1, y1), (x2, y2) = pijl
        mx, my = (x1 + x2) / 2 + 30, (y1 + y2) / 2 - 10
        pts = [((1 - t) ** 2 * x1 + 2 * (1 - t) * t * mx + t * t * x2, (1 - t) ** 2 * y1 + 2 * (1 - t) * t * my + t * t * y2) for t in [i / 20 for i in range(21)]]
        dr.line(pts, fill=GEEL, width=6, joint='curve')
        a = math.atan2(y2 - pts[-3][1], x2 - pts[-3][0])
        for da in (2.6, -2.6):
            dr.line([(x2, y2), (x2 + 22 * math.cos(a + da), y2 + 22 * math.sin(a + da))], fill=GEEL, width=6)


# ---------------- de beelden ----------------
PIJL_POSTER = (468, 668)


def poster(uit):
    W = 1000; im = Image.new('RGB', (W, W), NACHT); zee(im, W, W, .50); dr = ImageDraw.Draw(im)
    # HARDE EIS hoofdchat 07:25 en besluit 11 nov 23:25: nooit inhouden als doel; kop 'Breathe. Make sea friends.'
    kop(dr, W, 16, 'Breathe.', '', 108)
    kop(dr, W, 124, 'Make sea friends.', 'sea friends', 108)
    onder(dr, W, 244, 'Each one in their own little world.', 50)
    # ademscherm in plaats van het inhoudscherm: geen timer van het inhouden op de poster (harde eis 07:25)
    kast(im, 500, 630, 265, laad('krab-in'), ring=.10)
    # de grap: de krab kan niet zwemmen. Briefje links, pijl naar de linkerkant van de zwemband
    briefje(im, 128, 548, "can't swim yet", 46, hoek=8, pijl=((150, 592), PIJL_POSTER))
    dr = ImageDraw.Draw(im)
    # frisse keuring v5 punt 3: de koopreden als badge, groot genoeg voor 220 px
    t = 'One payment · no subscription'; ft = f(FX, 50); tw = dr.textlength(t, font=ft)
    dr.rounded_rectangle([W / 2 - tw / 2 - 28, 924, W / 2 + tw / 2 + 28, 994], radius=35, fill=GEEL)
    dr.text((W / 2, 959), t, font=ft, fill=NACHT, anchor='mm')
    im.save(os.path.join(uit, '0-poster.png'))
    return im


def kaart_een(naam, tekst, geel, sub, uit, nr):
    W = 800; im = Image.new('RGB', (W, W), NACHT); zee(im, W, W); dr = ImageDraw.Draw(im)
    kop(dr, W, 20, tekst, geel, 84); onder(dr, W, 130, sub, 56)
    kast(im, 400, 492, 250, laad(naam))
    im.save(os.path.join(uit, f'{nr}.png')); return im


def inzoom(im, x, y, z=.38):
    """Vergroot stuk van het echte scherm rond de held (zoals de loep van v2): niets bijgetekend."""
    n = im.width; h = z * n / 2
    return im.crop((int(x * n - h), int(y * n - h), int(x * n + h), int(y * n + h)))


PLEK_WERELDEN = [(138, 'krab-in', .50, .515, 'in a float'), (400, 'octopus', .60, .515, 'in a bath'), (662, 'shark', .64, .515, 'brushing')]


def kaart_werelden(uit):
    """Frisse keuring v5 punt 1: niet vijf hele schermen maar drie helden groot, elk met zijn grap als onderschrift."""
    W = 800; im = Image.new('RGB', (W, W), NACHT); zee(im, W, W, .66); dr = ImageDraw.Draw(im)
    kop(dr, W, 20, 'Every friend, their own world.', 'own world', 84); onder(dr, W, 130, 'And their own silly thing.', 56)
    # hoofdchat 07:25 punt 2: geen half cijfer bovenin de rondjes; venster y 159 tot 309 van 454: onder het cijfer (eind y 153) en boven 'round 2' (begin y 316), gemeten op de witte pixels
    for x, n, hx, hy, t in PLEK_WERELDEN:
        kast(im, x, 455, 120, inzoom(laad(n), hx, hy, .33), ring=.06)
        ImageDraw.Draw(im).text((x, 620), t, font=f(FX, 54), fill=GEEL, anchor='mt')
    im.save(os.path.join(uit, '2-worlds.png')); return im


def kaart_dagnacht(uit):
    W = 800; im = Image.new('RGB', (W, W), NACHT); zee(im, W, W); dr = ImageDraw.Draw(im)
    kop(dr, W, 20, 'The sea keeps your time.', 'your time', 84); onder(dr, W, 130, 'Sun by day. Moon by night.', 56)
    # frisse keuring v5b punt 1: geen scheidslijn door cijfer en krab, maar twee schermen naast elkaar (nacht achter, dag voor)
    kast(im, 560, 520, 185, laad('krab-in-nacht'), gloed=(70, 70, 200))
    kast(im, 240, 470, 185, laad('krab-in'))
    dr = ImageDraw.Draw(im)
    dr.text((200, 700), 'day', font=f(FX, 56), fill=SCHUIM, anchor='mm')
    dr.text((640, 752), 'night', font=f(FX, 56), fill=(170, 170, 255), anchor='mm')
    im.save(os.path.join(uit, '3-day-night.png')); return im


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    p = poster(uit)
    k = [kaart_een('krab-in', 'Breathe in. The sea rises.', 'rises', 'Breathe out, it sinks.', uit, '1-breathe'),
         kaart_werelden(uit), kaart_dagnacht(uit),
         kaart_een('today', 'Your day is a beach walk.', 'beach walk', 'Every session leaves a shell.', uit, '4-beach'),
         kaart_een('sealog', 'Fill your sea log.', 'sea log', 'Every friend you meet, saved.', uit, '5-sea-log')]
    # rij op winkelformaat (220) en groot overzicht
    rij = Image.new('RGB', (6 * 228 + 8, 236), (30, 30, 30))
    for i, b in enumerate([p] + k): rij.paste(b.resize((220, 220), Image.LANCZOS), (8 + i * 228, 8))
    rij.save(os.path.join(uit, 'rij-220.png'))
    groot = Image.new('RGB', (3 * 500 + 40, 2 * 500 + 30), (30, 30, 30))
    for i, b in enumerate([p] + k): groot.paste(b.resize((500, 500), Image.LANCZOS), (10 + (i % 3) * 510, 10 + (i // 3) * 510))
    groot.save(os.path.join(uit, 'overzicht-500.png'))
