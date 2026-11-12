# Ebb werelden v4, familie "licht" (run 50, 12 nov): kwal, zeepaardje, maanvis en haai in de opzet van krab, schildpad en clownvis.
# Leunt op werelden_v32 (bundel, kap, nachtkleuren), werelden_v3 (lucht, zee, tekst, kantelen) en werelden_v21 (Doek, water).
# Per dier een eigen plek onder water en een eigen grap als los voorwerp (het dier zelf verandert niet):
#  - kwal: open blauw met lichtbolletjes / hij is een parapluutje: regenwolkje boven hem, handvat onder zijn hoed
#  - zeepaardje: paal in het zand met zeegrasplukjes / draaimolenpaardje: rood-witte paal met gouden knop
#  - maanvis: licht zand vlak onder het oppervlak / hij zonnebaadt met een zonnebril (bij nacht omhoog), onder water aan een koordje
#  - haai: poetsstation tussen twee rotsen / boven water een grote tandenborstel met schuim, onder water twee poetsvisjes
# Coordinaten in 1/260 D.   python3 werelden_v4_licht.py <uitmap> [jelly seahorse sunfish shark]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v32 as v
import werelden_v21 as w
import werelden_v3 as v3
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ROZE, ZAND, ZAND_DONKER, ROTS, ROTS_R, D, fonkel, stofjes, kring, bellen
from blad_v9 import stippen
from PIL import Image

KWAL, PAARD, MAAN, HAAI = D[2], D[5], D[18], D[17]
DONKER = (0, 0, 85)
ROOD = (255, 0, 0)
GOUD, GOUD_L = (255, 170, 0), (255, 255, 85)


def rot(cx, cy, m, hoek):
    """Punt t.o.v. het midden van het dier (in maat m), draait mee zoals v3.dier_kantel (+ = neus omhoog)."""
    a = math.radians(hoek)
    def r(dx, dy):
        x, y = dx * m, dy * m
        return (cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a))
    return r


def lijn(d, pts, c, dikte):
    d.dr.line([d.P(*p) for p in pts], fill=c, width=max(1, round(dikte * d.s)), joint='curve')
    for p in (pts[0], pts[-1]): d.rondje(p[0], p[1], dikte / 2, dikte / 2, c)


def golfje(d, hx, y0, breed, nacht):
    """Golfje voor het lijf: het dier drijft IN het water (zoals bij de schildpad)."""
    zk = ((0, 85, 175) if not nacht else (0, 75, 150)) if d.am else ((0, 85, 170) if not nacht else (0, 0, 170))
    pts = [(x, y0 + 1.8 * math.sin((x - hx) / 7)) for x in range(int(hx - breed), int(hx + breed) + 1, 2)]
    d.blob(pts + [(hx + breed * .9, y0 + 8), (hx - breed * .9, y0 + 8)], zk)
    d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.6 * d.s)))


# ---------------- grapvoorwerpen ----------------
def regenwolk(d, x, y, nacht, druppels=True):
    """Klein regenwolkje met druppels die op de hoed vallen: de kwal is een parapluutje."""
    wk = (170, 170, 170) if not nacht else (85, 85, 170)
    for cx, cy, rx, ry in [(x - 12, y + 2, 10, 7), (x, y - 3, 12, 10), (x + 12, y + 2, 9, 7)]: d.rondje(cx, cy, rx, ry, WIT)
    for cx, cy, rx, ry in [(x - 12, y + 2, 8.4, 5.4), (x, y - 3, 10.4, 8.4), (x + 12, y + 2, 7.4, 5.4)]: d.rondje(cx, cy, rx, ry, wk)
    d.rondje(x, y + 6, 20, 3.6, wk)
    if druppels:
        for dx, dy in [(-14, 14), (-4, 20), (6, 13), (15, 19), (-10, 26), (10, 27)]:
            px, py = x + dx, y + dy
            d.blob([(px, py - 3.6), (px + 2.1, py + .6), (px, py + 2.4), (px - 2.1, py + .6)], (85, 255, 255), WIT, .8)


def handvat(d, r, nacht):
    """Paraplu-handvat onder de hoed: rechte steel en een krul (J), geel met donkere rand."""
    steel = [r(0, -.1), r(0, 1.12)]
    krul = [r(.24 * math.cos(t) + .24, 1.12 + .24 * math.sin(t)) for t in [math.pi * i / 12 for i in range(0, 13)]]
    pts = steel + krul
    lijn(d, pts, DONKER, 8.4)
    lijn(d, pts, GOUD_L if not nacht else (255, 255, 170), 5.2)


def paal(d, x, y0, y1, knop=True):
    """Rood-witte draaimolenpaal van y0 (boven) tot y1, met een gouden knop bovenop."""
    br = 3.4
    d.dr.rectangle([(x - br - 1.2) * d.s, y0 * d.s, (x + br + 1.2) * d.s, y1 * d.s], fill=DONKER)
    y = y0; i = 0
    while y < y1:
        y2 = min(y1, y + 7)
        d.dr.polygon([d.P(x - br, y), d.P(x + br, y - 3), d.P(x + br, y2 - 3), d.P(x - br, y2)], fill=ROOD if i % 2 == 0 else WIT)
        y = y2; i += 1
    d.dr.rectangle([(x - br - 1.2) * d.s, (y0 - 4) * d.s, (x + br + 1.2) * d.s, y0 * d.s], fill=DONKER)
    if knop:
        d.rondje(x, y0 - 6, 6, 6, GOUD, DONKER, glans=GOUD_L, dikte=1.4)
        d.rondje(x, y0 - 13.5, 2, 2, GOUD, DONKER, dikte=1.0)


def zonnebril(d, r, omhoog=False):
    """Zonnebril op de maanvis: glas over zijn oog, het tweede glas steekt voor zijn neus uit, pootje naar achter.
    omhoog = bij nacht op zijn voorhoofd."""
    dy = -.36 if omhoog else 0
    g1, g2 = r(-.32, -.15 + dy), r(-.72, -.13 + dy)
    lijn(d, [r(-.32, -.15 + dy), r(.10, -.24 + dy)], DONKER, 2.4)        # pootje
    lijn(d, [g2, g1], DONKER, 2.6)                                        # brug
    for g, rr in ((g1, .17), (g2, .13)):
        dm = rr * (d.D and 1)
    m = math.hypot(r(1, 0)[0] - r(0, 0)[0], r(1, 0)[1] - r(0, 0)[1])
    for g, rr in ((g1, .17), (g2, .135)):
        d.rondje(g[0], g[1], rr * m, rr * m * .82, (0, 0, 0), WIT, dikte=1.3)
        d.rondje(g[0] - rr * m * .35, g[1] - rr * m * .3, rr * m * .28, rr * m * .2, (85, 85, 170))


def bril_aan_koord(d, r):
    """Onder water: de zonnebril hangt aan een koordje om zijn nek."""
    m = math.hypot(r(1, 0)[0] - r(0, 0)[0], r(1, 0)[1] - r(0, 0)[1])
    a, b = r(-.42, .40), r(-.12, .44)
    lijn(d, [r(-.1, -.3), r(-.22, .1), a], WIT, 1.2)
    lijn(d, [r(.12, -.3), r(.06, .1), b], WIT, 1.2)
    lijn(d, [a, b], DONKER, 2.4)
    for g, rr in ((a, .14), (b, .14)):
        d.rondje(g[0], g[1], rr * m, rr * m * .82, (0, 0, 0), WIT, dikte=1.3)
        d.rondje(g[0] - rr * m * .35, g[1] - rr * m * .3, rr * m * .28, rr * m * .2, (85, 85, 170))


def tandenborstel(d, r):
    """Grote tandenborstel in de bek van de haai, met schuimbelletjes: hij poetst zijn tanden."""
    steel = [r(-1.0, .26), r(-1.75, .02)]
    lijn(d, steel, WIT, 8.6); lijn(d, steel, ROZE, 5.8)
    kop = [r(-.66, .18), r(-1.04, .18), r(-1.04, .34), r(-.66, .34)]
    d.blob(kop, ROZE, WIT, 1.4)
    for i in range(5):      # witte haren bovenop de kop, tegen zijn tanden
        t = i / 4; p = r(-1.0 + .32 * t, .12)
        d.rondje(p[0], p[1], 1.9, 3.0, WIT)
    for dx, dy, k in [(-.58, .0, 3.4), (-.52, .36, 2.8), (-1.12, .04, 2.6), (-1.14, .40, 3.0), (-.80, .46, 2.4), (-.44, .18, 2.2), (-.86, -.06, 2.0)]:
        p = r(dx, dy); d.rondje(p[0], p[1], k, k, WIT, (85, 170, 255), dikte=.8)


def poetsvisje(d, x, y, k=1.0, borstel=False, kijk=-1):
    """Poetsvisje (blauw met zwarte streep), kijkt naar de haai; borstel = piepklein borsteltje voor zijn bek."""
    d.blob([(x - 9 * k * kijk, y), (x - 3 * k * kijk, y - 4 * k), (x + 6 * k * kijk, y - 3 * k), (x + 11 * k * kijk, y - 4.5 * k),
            (x + 10 * k * kijk, y), (x + 11 * k * kijk, y + 4.5 * k), (x + 6 * k * kijk, y + 3 * k), (x - 3 * k * kijk, y + 4 * k)], (85, 170, 255), WIT, 1.2)
    d.dr.line([d.P(x - 8 * k * kijk, y), d.P(x + 8 * k * kijk, y)], fill=(0, 0, 0), width=max(1, round(1.6 * k * d.s)))
    d.rondje(x - 5 * k * kijk, y - 1.6 * k, 1.2 * k, 1.2 * k, (0, 0, 0))
    if borstel:
        bx = x - 10 * k * kijk
        lijn(d, [(bx, y + 1), (bx - 7 * k * kijk, y + 1)], (255, 255, 0), 1.6 * k)
        xa, xb = sorted([bx - 9.5 * k * kijk, bx - 6 * k * kijk])
        d.dr.rectangle([xa * d.s, (y - 2 * k) * d.s, xb * d.s, (y + 1 * k) * d.s], fill=WIT)


# ---------------- held met grap (een groep: dier en voorwerp) ----------------
def held_jelly(d, hx, hy, m, hoek, nacht, boven=False):
    r = rot(hx, hy, m, hoek)
    handvat(d, r, nacht)
    v3.dier_kantel(d, hx, hy, m, KWAL, hoek)
    if boven: regenwolk(d, hx + 2, hy - .88 * m - 30, nacht)


def held_seahorse(d, hx, hy, m, hoek, nacht, boven=False, paal_top=None):
    px = hx + .30 * m
    if not boven:
        paal(d, px, paal_top if paal_top is not None else hy - 1.0 * m, hy + 1.0 * m + 20)
    v3.dier_kantel(d, hx, hy, m, PAARD, hoek)
    if not boven:     # de paal loopt voor zijn staartkrul langs: zijn staart zit eromheen
        d.dr.rectangle([(px - 4.6) * d.s, (hy + .62 * m) * d.s, (px + 4.6) * d.s, (hy + .70 * m) * d.s], fill=DONKER)
        d.dr.rectangle([(px - 3.4) * d.s, (hy + .63 * m) * d.s, (px + 3.4) * d.s, (hy + .69 * m) * d.s], fill=ROOD)


def held_sunfish(d, hx, hy, m, hoek, nacht, boven=False):
    r = rot(hx, hy, m, hoek)
    v3.dier_kantel(d, hx, hy, m, MAAN, hoek)
    if boven: zonnebril(d, r, omhoog=nacht)
    else: bril_aan_koord(d, r)


def held_shark(d, hx, hy, m, hoek, nacht, boven=False):
    r = rot(hx, hy, m, hoek)
    v3.dier_kantel(d, hx, hy, m, HAAI, hoek)
    if boven: tandenborstel(d, r)
    else:
        poetsvisje(d, *r(-.66, .66), k=1.35 * m / 36, borstel=True, kijk=1)
        poetsvisje(d, *r(-1.05, -.36), k=1.25 * m / 36, borstel=True, kijk=1)
        for dx, dy, k in [(-1.2, .14, 2.0), (-1.34, .0, 1.5)]:
            p = r(dx, dy); d.rondje(p[0], p[1], k, k, WIT, (85, 170, 255), dikte=.7)


# ---------------- plekken onder water ----------------
def bodem(d, dd, zak, heuvel=226, ruggen=((30, 190, 56, 26), (140, 200, 70, 16), (236, 184, 50, 32)), zand=None, gloed_x=130):
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in ruggen: d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-40 * s, (heuvel + zak) * s, 300 * s, 340 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-30 * s, (heuvel + 4 + zak) * s, 290 * s, 340 * s], fill=zand or (ZAND if not d.am else (235, 225, 150)))
    if d.am: d.gloed_ellips(gloed_x, heuvel + 10 + zak, 46, 9, WIT, .4)


def plek_jelly(d, dd, zak=0, nacht=False):
    """Open blauw met lichtbolletjes: alleen een lage zandbank, drie zwevende lichtbolletjes, twee steentjes."""
    bodem(d, dd, zak, heuvel=234, ruggen=((40, 200, 60, 18), (220, 196, 60, 22)))
    licht = (170, 255, 255) if not nacht else (85, 255, 170)
    for x, y, r_ in [(36, 176, 5), (52, 196, 3.6), (222, 170, 4.4), (236, 190, 3)]:
        d.rondje(x, y + zak, r_, r_, licht, WIT, dikte=1.2); d.rondje(x - r_ * .3, y + zak - r_ * .3, r_ * .35, r_ * .35, WIT)
    d.rondje(78, 244 + zak, 7, 4.5, (170, 170, 255), WIT, dikte=1.2)
    d.rondje(190, 246 + zak, 6, 4, (255, 170, 170), WIT, dikte=1.2)


def plek_seahorse(d, dd, zak=0, nacht=False):
    """Zandheuvel met twee plukjes zeegras in geelgroen, een gouden ring in het zand en twee steentjes."""
    bodem(d, dd, zak)
    for x, n, hgt in [(42, 4, 34), (222, 5, 40)]:
        v3.pluk(d, x, 236 + zak, n, hgt, (85, 170, 0), (170, 255, 85))
    d.rondje(84, 244 + zak, 8, 4.4, GOUD, DONKER, dikte=1.2); d.rondje(84, 244 + zak, 4.6, 2.0, ZAND if not d.am else (235, 225, 150))
    d.rondje(184, 246 + zak, 6, 4, (170, 170, 255), WIT, dikte=1.2)


def plek_sunfish(d, dd, zak=0, nacht=False):
    """Licht zand vlak onder het oppervlak: lichtringen van de zon op het zand, een schelp en een strandbal."""
    bodem(d, dd, zak, heuvel=222, ruggen=((40, 196, 60, 20), (230, 192, 56, 24)))
    ring = (255, 255, 255) if not nacht else (170, 170, 255)
    for cx, cy, rx, ry in [(70, 240, 14, 4), (196, 238, 16, 4.6), (130, 250, 12, 3.4)]:
        d.dr.ellipse([(cx - rx) * d.s, (cy - ry + zak) * d.s, (cx + rx) * d.s, (cy + ry + zak) * d.s], outline=ring, width=max(1, round(1.4 * d.s)))
    d.rondje(46, 230 + zak, 7, 5, (255, 170, 170), WIT, dikte=1.2)
    bx, by = 220, 222 + zak
    d.rondje(bx, by, 8, 8, WIT, DONKER, dikte=1.2)
    d.dr.pieslice([(bx - 8) * d.s, (by - 8) * d.s, (bx + 8) * d.s, (by + 8) * d.s], 200, 260, fill=ROOD)
    d.dr.pieslice([(bx - 8) * d.s, (by - 8) * d.s, (bx + 8) * d.s, (by + 8) * d.s], 320, 20, fill=(0, 85, 255))
    d.dr.pieslice([(bx - 8) * d.s, (by - 8) * d.s, (bx + 8) * d.s, (by + 8) * d.s], 80, 140, fill=(255, 255, 0))


def plek_shark(d, dd, zak=0, nacht=False):
    """Poetsstation: twee ronde rotsen links en rechts met sponsbolletjes, zand ertussen."""
    bodem(d, dd, zak)
    for x, y, rx, ry in [(30, 214, 34, 26), (232, 212, 34, 28)]:
        d.rondje(x, y + zak, rx, ry, ROTS, ROTS_R, glans=ROTS_R)
    for x, y, r_, c in [(22, 190, 5, (255, 170, 0)), (38, 194, 3.6, (255, 85, 170)), (238, 186, 5, (255, 85, 170)), (224, 192, 3.6, (255, 255, 85))]:
        d.rondje(x, y + zak, r_, r_, c, WIT, dikte=1.1)


PLEK = dict(jelly=plek_jelly, seahorse=plek_seahorse, sunfish=plek_sunfish, shark=plek_shark)
HELD = dict(jelly=held_jelly, seahorse=held_seahorse, sunfish=held_sunfish, shark=held_shark)
VRIEND = dict(jelly=(D[5], 'Seahorse'), seahorse=(D[6], 'Starfish'), sunfish=(D[19], 'Orca'), shark=(D[18], 'Sunfish'))
# positie (hx, hy, maat) bij hold, menu en eind
POS = dict(
    jelly=dict(hold=(130, 189, 44), menu=(130, 188, 42), eind=(70, 106, 30)),
    seahorse=dict(hold=(124, 198, 42), menu=(124, 200, 40), eind=(68, 119, 30)),
    sunfish=dict(hold=(128, 192, 48), menu=(128, 194, 46), eind=(70, 108, 32)),
    shark=dict(hold=(136, 182, 36), menu=(136, 184, 34), eind=(74, 104, 28)),
)


# ---------------- boven water ----------------
def adem(D_, am, dd, nacht, dier, fase):
    top, woord, getal, onder = {'in': (134, 'breathe in', '12', 'round 2 · 18 left'), 'uit': (170, 'breathe out', '9', 'round 2 · 18 left'),
                                'calm': (146, 'breathe out', '5', '4-7-8 · 2 of 4')}[fase]
    v._KAP['y'] = 140
    d = Doek(D_, am)
    v3.lucht(d, dd, nacht, top)
    if dier == 'shark':
        wk = WIT if not nacht else (85, 85, 170); wr = (170, 255, 255) if not nacht else (0, 0, 170)
        for cx, cy, rx, ry in [(214, 70, 14, 8), (226, 64, 12, 10), (236, 72, 11, 7)]: d.rondje(cx, cy, rx, ry, wr)
        for cx, cy, rx, ry in [(214, 69, 12, 6.5), (226, 63, 10, 8.5), (236, 71, 9, 5.5)]: d.rondje(cx, cy, rx, ry, wk)
    v3.zee(d, nacht, top)
    if dier != 'seahorse': v3.volgende_vriend(d, nacht, top, x=200 if dier != 'shark' else 214)
    hoek = {'in': 8, 'calm': 3, 'uit': 0}[fase]
    if dier == 'jelly':
        hx = 198; hy = top - 2
        held_jelly(d, hx, hy, 34, hoek, nacht, boven=True)
    elif dier == 'seahorse':
        hx = 194; m = 36
        paal(d, hx + .30 * m, 60, 262)                       # de paal staat vast, het paardje gaat op en neer met de zee
        held_seahorse(d, hx, top - 6, m, hoek, nacht, boven=True)
        p = hx + .30 * m      # paal voor de staartkrul langs
        d.dr.rectangle([(p - 4.6) * d.s, (top - 6 + .62 * m) * d.s, (p + 4.6) * d.s, (top - 6 + .70 * m) * d.s], fill=DONKER)
        d.dr.rectangle([(p - 3.4) * d.s, (top - 6 + .63 * m) * d.s, (p + 3.4) * d.s, (top - 6 + .69 * m) * d.s], fill=ROOD)
    elif dier == 'sunfish':
        hx = 196; m = 40; hy = top + 2
        v3.dier_kantel(d, hx, hy, m, MAAN, hoek)
        golfje(d, hx + 4, top + 12, m * .78, nacht)
        zonnebril(d, rot(hx, hy, m, hoek), omhoog=nacht)
    else:
        hx = 178 if fase == 'in' else (170 if fase == 'calm' else 150); m = 38; hy = top - 2
        v3.dier_kantel(d, hx, hy, m, HAAI, hoek)
        golfje(d, hx + 10, top + 14, m * .95, nacht)
        tandenborstel(d, rot(hx, hy, m, hoek))
    v3.tekst_adem(d, top, woord, getal, onder)
    return d.klaar()


# ---------------- onder water ----------------
def hold(D_, am, dd, nacht, dier):
    v._KAP['y'] = 117 + 22
    hx, hy, m = POS[dier]['hold']
    d = Doek(D_, am); v3.onder(d, dd, nacht, xo=hx - 4, xh=hx)
    PLEK[dier](d, dd, 0, nacht)
    if dier == 'seahorse': HELD[dier](d, hx, hy, m, 0, nacht, paal_top=hy - .80 * m)
    else: HELD[dier](d, hx, hy, m, 0, nacht)
    stofjes(d, dd)
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 117, '61 bpm · round 2', 18, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht, dier):
    v._KAP['y'] = 140
    hx, hy, m = POS[dier]['menu']
    d = Doek(D_, am); v3.onder(d, dd, nacht, xo=hx - 6, xh=hx)
    PLEK[dier](d, dd, 4, nacht)
    if dier == 'seahorse': HELD[dier](d, hx, hy, m, 0, nacht, paal_top=hy - .80 * m)
    else: HELD[dier](d, hx, hy, m, 0, nacht)
    stofjes(d, dd); s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t in [(52, 'Rounds'), (86, 'Calm 4-7-8')]:
        fill = ((0, 30, 60) if dd is DAG else (0, 0, 50)) if am else (0, 0, 85)
        d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                               outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


def eind(D_, am, dd, nacht, dier):
    """Indeling van v3.2 (d): kop en tijden tot y 70, held links, vriend in het belletje, naam van y 150 tot 196."""
    v._KAP['y'] = 72
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    v.bundel(d, dd, nacht, xo=184, xh=184, yh=136)
    PLEK[dier](d, dd, 16, nacht)
    stofjes(d, dd)
    vriend, naam = VRIEND[dier]
    for x, y, k in [(228, 76, 7), (236, 140, 5)]: fonkel(d, x, y, k)
    bx, by, brx, bry = 186, 108, 36, 32
    kring(d, dd, bx, by, 40)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 3.6, 3.6, WIT)
    d.dier(bx, by + 1, 26 if vriend is D[5] else (24 if vriend is D[19] else 28), vriend)
    hart = [(132 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 94 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 18, '3 rounds done', 27, GEEL)
    d.tekst(130, 46, '1:20   1:45   1:58', 22, WIT)
    hx, hy, m = POS[dier]['eind']
    if dier == 'seahorse': HELD[dier](d, hx, hy, m, 0, nacht, paal_top=hy - .80 * m)
    else: HELD[dier](d, hx, hy, m, 0, nacht)
    d.tekst(130, 150, 'new friend', 18, WIT, False)
    d.tekst(130, 166, naam, 32 if len(naam) < 9 else 29, GEEL)
    stippen(d.dr, 130 * d.s, 212 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def scherm(naam, dier):
    if naam in ('in', 'uit', 'calm'): return lambda D_, am, dd, n: adem(D_, am, dd, n, dier, naam)
    return lambda D_, am, dd, n: {'hold': hold, 'menu': menu, 'eind': eind}[naam](D_, am, dd, n, dier)


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']
DIEREN = ['jelly', 'seahorse', 'sunfish', 'shark']

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for dier in sys.argv[2:] or DIEREN:
        rij = {}
        for nacht in (False, True):
            dd = NACHT if nacht else DAG
            for D_, am in ((454, True), (260, False)):
                for naam in NAMEN:
                    im = scherm(naam, dier)(D_, am, dd, nacht)
                    im.save(os.path.join(uit, f'{dier}-{naam}-{"nacht" if nacht else "dag"}-{D_}.png')); rij[(naam, nacht, D_)] = im
        for D_, k in ((454, 1), (260, 2)):
            g = 12 * k; W = D_ * k; n = len(NAMEN)
            ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
            for j, nacht in enumerate((False, True)):
                for i, naam in enumerate(NAMEN):
                    ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
            ov.save(os.path.join(uit, f'overzicht-{dier}-{D_}-{k}x.png'))
