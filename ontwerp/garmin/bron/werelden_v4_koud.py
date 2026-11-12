# Werelden v4, familie koud (run 50, 12 nov): walvis, orka, narwal en reuzeninktvis in de opzet van werelden_v32.
# Lijst versie 2 (ebb-werelden-v3.md):
#  - Whale: open diep blauw / fontein met regenboog (nacht: witte maanboog); onder water een boog van gekleurde steentjes in het zand.
#  - Orca: open water / rood strikje en muzieknootjes die met de adem stijgen en zakken; onder water een rijtje visjes met nootjes.
#  - Narwhal: onder het ijs met een wak / sjaaltje en want hangen aan zijn tand te drogen; onder water hangt het sjaaltje nog.
#  - Giant squid: schemerig water met lichtpuntjes / slecht verstoppen: achter een piepkleine boei, onder water achter een plantje.
# Hergebruikt lucht, zee, water, bundel en tekstopzet uit werelden_v3 en werelden_v32. Coordinaten in 1/260 D.
#   python3 werelden_v4_koud.py <uitmap> [whale orca narwhal squid]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
import werelden_v3 as v3
import werelden_v32 as v32          # zet de v3.2-bundel en de nachtkleuren
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ROZE, ZAND, ZAND_DONKER, D, bellen, fonkel, stofjes, kring
from blad_v9 import stippen
from PIL import Image

WALVIS, ORKA, NARWAL, INKT = D[23], D[19], D[20], D[21]
VRIEND = {'whale': (D[24], 'Sea cucumber'), 'orca': (NARWAL, 'Narwhal'), 'narwhal': (INKT, 'Giant squid'), 'squid': (D[22], 'Lobster')}
ROOD, ORANJE, GEEL_V, GROEN, BLAUW, PAARS = (255, 0, 0), (255, 170, 0), (255, 255, 85), (85, 255, 85), (85, 170, 255), (170, 85, 255)
NAVY = (0, 0, 85)
IJS, IJS_R = (170, 255, 255), WIT
STEEN, STEEN_R = (85, 85, 170), (170, 170, 255)
HELD_AAN = [True]       # de meetscripts zetten dit uit om de held-groep (dier, grap, vriend) te vinden


def R(hx, hy, m, hoek, dx, dy):
    """Punt t.o.v. het midden van de sticker (in maat m), kantelt mee zoals dier_kantel (+ = neus omhoog)."""
    a = math.radians(hoek); x, y = dx * m, dy * m
    return (hx + x * math.cos(a) - y * math.sin(a), hy + x * math.sin(a) + y * math.cos(a))


def dier(d, hx, hy, m, wie, hoek=0):
    if HELD_AAN[0]: v3.dier_kantel(d, hx, hy, m, wie, hoek)


def boog(d, cx, cy, rx, ry, banden, dikte):
    """Regenboog: banden van buiten naar binnen, bovenste helft van een ellips."""
    for i, c in enumerate(banden):
        r1, r2 = rx - i * dikte, ry - i * dikte
        d.dr.arc([(cx - r1) * d.s, (cy - r2) * d.s, (cx + r1) * d.s, (cy + r2) * d.s], 180, 360, fill=c, width=max(2, round(dikte * d.s + .5)))


def noot(d, x, y, k=1.0, c=GEEL_V, dubbel=False):
    """Muzieknootje: rond kopje, steeltje, vlaggetje; donkere rand zodat hij op lucht en water leest."""
    sw = max(2, round(1.6 * k * d.s))
    def teken(c_, extra):
        e = extra
        d.dr.line([d.P(x + 3.4 * k, y), d.P(x + 3.4 * k, y - 13 * k)], fill=c_, width=sw + round(2 * e * d.s))
        if dubbel:
            d.dr.line([d.P(x + 3.4 * k, y - 13 * k), d.P(x + 13.4 * k, y - 15 * k)], fill=c_, width=round((2.8 * k + 2 * e) * d.s))
            d.dr.line([d.P(x + 13.4 * k, y - 15 * k), d.P(x + 13.4 * k, y - 2 * k)], fill=c_, width=sw + round(2 * e * d.s))
            d.rondje(x + 10 * k, y - 1 * k, 3.6 * k + e, 2.8 * k + e, c_)
        else:
            d.dr.line([d.P(x + 3.4 * k, y - 13 * k), d.P(x + 8.4 * k, y - 8 * k)], fill=c_, width=sw + round(2 * e * d.s))
        d.rondje(x, y + 1 * k, 3.6 * k + e, 2.8 * k + e, c_)
    teken(NAVY, 1.1); teken(c, 0)


def strik(d, x, y, k=1.0, hoek=0):
    """Rood strikje (vlinderdas): twee driehoekjes en een knoopje, witte rand."""
    a = math.radians(hoek)
    def r(dx, dy): return (x + (dx * math.cos(a) - dy * math.sin(a)) * k, y + (dx * math.sin(a) + dy * math.cos(a)) * k)
    for s in (-1, 1):
        d.blob([r(0, 0), r(7 * s, -5), r(8.4 * s, 0), r(7 * s, 5)], ROOD, WIT, 1.3)
    d.rondje(*r(0, 0), 2.2 * k, 2.2 * k, (170, 0, 0), WIT, dikte=.9)


def visje(d, x, y, k, c=ORANJE):
    d.blob([(x + 6 * k, y), (x + 11 * k, y - 4.5 * k), (x + 11 * k, y + 4.5 * k)], c, WIT, 1.1)
    d.rondje(x, y, 7 * k, 4.6 * k, c, WIT, dikte=1.1)
    d.rondje(x - 3.4 * k, y - 1 * k, 1.1 * k, 1.1 * k, (0, 0, 0))


def sjaal(d, x0, y0, x1, y1, k=1.0):
    """Gestreept sjaaltje over de tand gehangen: twee slippen die naar beneden hangen, witte strepen, franjes."""
    mx = (x0 + x1) / 2
    for dx, L in ((-3.4, 16), (3.0, 12)):
        x = mx + dx * k; yt = (y0 + y1) / 2
        d.blob([(x - 3 * k, yt - 1 * k), (x + 3 * k, yt - 1 * k), (x + 3.6 * k, yt + L * k), (x - 2.4 * k, yt + L * k)], ROOD, WIT, 1.2)
        for t in (.35, .7):
            yy = yt + L * t * k
            d.dr.line([d.P(x - 2.8 * k, yy), d.P(x + 3.2 * k, yy)], fill=WIT, width=max(1, round(1.6 * k * d.s)))
        for fx in (-1.6, .6, 2.6):
            d.dr.line([d.P(x + fx * k, yt + L * k), d.P(x + fx * k, yt + (L + 3) * k)], fill=WIT, width=max(1, round(1.1 * d.s)))
    d.rondje(mx, (y0 + y1) / 2, 6 * k, 2.6 * k, ROOD, WIT, dikte=1.1)      # waar hij over de tand ligt


def want(d, x, y, k=1.0):
    """Wollen want aan een knijpertje: hand met duim, witte boord."""
    d.rondje(x, y + 8 * k, 4.6 * k, 6 * k, GROEN, WIT, dikte=1.2)
    d.rondje(x - 4.6 * k, y + 6 * k, 2 * k, 3.2 * k, GROEN, WIT, dikte=1.0)
    d.rondje(x - 4.6 * k, y + 6 * k, 2 * k, 3.2 * k, GROEN)
    d.rondje(x, y + 8 * k, 4.6 * k, 6 * k, GROEN)
    d.dr.rectangle([(x - 4.4 * k) * d.s, (y + 1 * k) * d.s, (x + 4.4 * k) * d.s, (y + 3.4 * k) * d.s], fill=WIT)
    d.dr.line([d.P(x, y - 1.5 * k), d.P(x, y + 1.5 * k)], fill=GEEL_V, width=max(1, round(1.6 * d.s)))


def tand(d, hx, hy, m, hoek):
    """Narwal ronde 2: een eigen lange witte tand met donkere rand, steekt ver buiten de sticker uit."""
    a, b = R(hx, hy, m, hoek, -.6, -.19), R(hx, hy, m, hoek, -1.6, -.24)
    d.dr.line([d.P(*a), d.P(*b)], fill=NAVY, width=round(4.6 * d.s)); d.rondje(*b, 2.3, 2.3, NAVY)
    d.dr.line([d.P(*a), d.P(*b)], fill=WIT, width=max(2, round(2.4 * d.s)))
    for t in (.3, .5, .7, .88):      # draaiing van de tand
        x, y = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        d.dr.line([d.P(x - 1, y - 1.4), d.P(x + 1, y + 1.4)], fill=(170, 170, 255), width=max(1, round(.9 * d.s)))


def schelp(d, x, y, k=1.0):
    """Schelp als podiumpje: waaiervorm met witte rand en ribbels."""
    pts = [(x + 8 * k * math.cos(math.pi + math.pi * i / 10), y + 6 * k * math.sin(math.pi + math.pi * i / 10)) for i in range(11)] + [(x + 2 * k, y + 3 * k), (x - 2 * k, y + 3 * k)]
    d.blob(pts, (255, 170, 170), WIT, 1.2)
    for i in (3, 5, 7):
        a = math.pi + math.pi * i / 10
        d.dr.line([d.P(x, y + 2 * k), d.P(x + 6.5 * k * math.cos(a), y + 5 * k * math.sin(a))], fill=WIT, width=max(1, round(.9 * d.s)))


def ijsje(d, x, y, k=1.0):
    """Ijshoorntje op de punt van de tand: bruin hoorntje (punt op de tand) met een roze bol en een witte rand."""
    d.blob([(x, y + 1 * k), (x - 5 * k, y - 11 * k), (x + 5 * k, y - 11 * k)], (170, 85, 0), WIT, 1.3)
    for t in (.35, .7):
        d.dr.line([d.P(x - 5 * k * t, y - 11 * k * t), d.P(x + 5 * k * t, y - 11 * k * t)], fill=(85, 0, 0), width=max(1, round(.9 * d.s)))
    d.rondje(x, y - 15 * k, 6.4 * k, 5.6 * k, (255, 170, 255), WIT, dikte=1.4)
    d.rondje(x - 2.2 * k, y - 17 * k, 1.6 * k, 1.3 * k, WIT)


def bootje(d, x, y, k=1.0):
    """Papieren bootje van 13 px: wit, dunne donkere rand, romp met een punt in het midden."""
    pts = [(x - 6.5 * k, y - 2 * k), (x - 2.4 * k, y - 2 * k), (x, y - 8 * k), (x + 2.4 * k, y - 2 * k), (x + 6.5 * k, y - 2 * k), (x + 4 * k, y + 2.5 * k), (x - 4 * k, y + 2.5 * k)]
    d.blob(pts, WIT, NAVY, 1.1)
    d.dr.line([d.P(x - 4.6 * k, y - .4 * k), d.P(x + 4.6 * k, y - .4 * k)], fill=(170, 170, 255), width=max(1, round(.8 * d.s)))


def boei(d, x, y, k=1.0):
    """Piepkleine boei: rood-wit, een stokje met een lampje."""
    d.dr.line([d.P(x, y - 4 * k), d.P(x, y - 11 * k)], fill=WIT, width=max(1, round(1.4 * k * d.s)))
    d.rondje(x, y - 11.5 * k, 1.6 * k, 1.6 * k, GEEL_V)
    d.rondje(x, y, 5 * k, 4.6 * k, ROOD, WIT, dikte=1.2)
    d.dr.rectangle([(x - 5 * k) * d.s, (y - 1 * k) * d.s, (x + 5 * k) * d.s, (y + 1.2 * k) * d.s], fill=WIT)


def plantje(d, x, y, k=1.0):
    """Een klein plantje: steeltje met vier ronde blaadjes."""
    d.dr.line([d.P(x, y), d.P(x, y - 20 * k)], fill=WIT, width=round(3.6 * k * d.s))
    d.dr.line([d.P(x, y), d.P(x, y - 20 * k)], fill=(0, 255, 0), width=max(1, round(1.8 * k * d.s)))
    for dx, dy, s in ((-5, -8, 1), (5, -12, 1), (-4, -17, .9), (3, -21, .8)):
        d.rondje(x + dx * k, y + dy * k, 4.4 * k * s, 2.8 * k * s, (85, 255, 0), WIT, dikte=1.0)


# ---------------- boven water ----------------
def golfje(d, hx, m, y0, nacht):
    zk = ((0, 85, 175) if not nacht else (0, 75, 150)) if d.am else ((0, 85, 170) if not nacht else (0, 0, 170))
    pts = [(x, y0 + 1.8 * math.sin((x - hx) / 7)) for x in range(int(hx - m * 1.15), int(hx + m * 1.15) + 1, 2)]
    d.blob(pts + [(hx + m * 1.05, y0 + 7), (hx - m * 1.05, y0 + 7)], zk)
    d.dr.line([d.P(*q) for q in pts], fill=WIT, width=max(1, round(1.6 * d.s)))


def ijsschots(d, x, y, rx, ry):
    d.rondje(x, y + 2, rx, ry, (85, 170, 255))                       # zijkant onder water
    d.rondje(x, y, rx, ry, IJS, IJS_R, dikte=1.6)
    d.rondje(x - rx * .35, y - ry * .3, rx * .3, ry * .3, WIT)


def adem(D_, am, dd, nacht, dier_naam, top=134, woord='breathe in', getal='12', onder='round 2 · 18 left', fase='in'):
    d = Doek(D_, am)
    v3.lucht(d, dd, nacht, top)
    hoek = {'in': 8, 'calm': 3, 'uit': 0}[fase]
    if dier_naam in ('narwhal', 'squid'):          # wolkje rechts (walvis en orka hebben daar hun boog en nootjes)
        wx = 222; wk = WIT if not nacht else (85, 85, 170); wr = (170, 255, 255) if not nacht else (0, 0, 170)
        for cx, cy, rx, ry in [(wx - 8, 70, 14, 8), (wx + 4, 64, 12, 10), (wx + 14, 72, 11, 7)]: d.rondje(cx, cy, rx, ry, wr)
        for cx, cy, rx, ry in [(wx - 8, 69, 12, 6.5), (wx + 4, 63, 10, 8.5), (wx + 14, 71, 9, 5.5)]: d.rondje(cx, cy, rx, ry, wk)
    hx = 128 if top > 160 else (176 if dier_naam == 'whale' else (184 if dier_naam == 'narwhal' and top < 140 else 170)); dy = 0 if top < 140 else -4
    if dier_naam == 'squid':
        # hij steekt achter de zee omhoog: eerst de inktvis, dan de zee eroverheen (de onderkant verdwijnt)
        m = 40; hy = top + dy - 4
        dier(d, hx, hy, m, INKT, hoek * .5)
        v3.zee(d, nacht, top)
        v3.volgende_vriend(d, nacht, top)
        if HELD_AAN[0]:
            bootje(d, hx - 2, top - 1, 1.0)    # ronde 3: piepklein papieren bootje (13 px) vlak voor hem: hij verstopt zich erachter
    else:
        v3.zee(d, nacht, top)
        if dier_naam == 'narwhal':
            ijsschots(d, 40, top + 4, 26, 6); ijsschots(d, 236, top + 10, 22, 5)
        v3.volgende_vriend(d, nacht, top, x=196 if dier_naam != 'whale' else 70)
        if dier_naam == 'whale':
            m = 40; hy = top + dy - 4
            dier(d, hx, hy, m, WALVIS, hoek)
            golfje(d, hx, m, top + dy + 14, nacht)
            if HELD_AAN[0]:
                sx, sy = R(hx, hy, m, hoek, -.6, -.66)        # top van zijn fontein
                rx, ry = 40, 34
                banden = [ROOD, ORANJE, GEEL_V, GROEN, BLAUW, PAARS] if not nacht else [WIT, (170, 170, 255), WIT]
                boog(d, sx + rx - 3, sy + 8, rx, ry, banden, 2.6 if not nacht else 2.2)
                for dx_, dy_, r_ in ((-4, 2, 2.2), (3, -1, 1.8), (-1, -4, 1.6)):
                    d.rondje(sx + dx_, sy + dy_, r_, r_, WIT, (85, 170, 255), dikte=.8)
        elif dier_naam == 'orca':
            m = 38; hy = top + dy - 2
            dier(d, hx, hy, m, ORKA, hoek)
            golfje(d, hx, m, top + dy + 16, nacht)
            if HELD_AAN[0]:
                strik(d, *R(hx, hy, m, hoek, -.42, .42), 1.15, hoek)
                hoog = {'in': 30, 'calm': 18, 'uit': 6}[fase]   # nootjes stijgen bij inademen, zakken bij uitademen
                for nx, ny, k, dub in ((hx + 34, top - 16, 1.05, False), (hx + 50, top - 34, 1.1, True), (hx + 64, top - 18, .95, False)):
                    noot(d, nx, ny - hoog, k, GEEL_V, dub)
        elif dier_naam == 'narwhal':
            m = 38; hy = top + dy - 2 + (3 if top < 140 else 0)      # bij inademen iets lager: het ijsje blijft vrij van het cijfer
            dier(d, hx, hy, m, NARWAL, hoek)
            golfje(d, hx, m, top + dy + 13, nacht)
            if HELD_AAN[0]:
                tand(d, hx, hy, m, hoek)
                ijsje(d, *R(hx, hy, m, hoek, -1.6, -.24), 1.0)
    v3.tekst_adem(d, top, woord, getal, onder)
    return d.klaar()


# ---------------- plekken onder water ----------------
def verre_ruggen(d, dd, lijst, zak):
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in lijst: d.rondje(cx, cy + zak, rx, ry, verder)


def zandbult(d, y, zak, licht=None):
    s = d.s
    d.dr.ellipse([-50 * s, (y + zak) * s, 310 * s, 360 * s], fill=ZAND_DONKER if licht is None else licht[0])
    d.dr.ellipse([-40 * s, (y + 4 + zak) * s, 300 * s, 360 * s], fill=(ZAND if not d.am else (235, 225, 150)) if licht is None else licht[1])


def steentjesboog(d, cx, cy, rx, ry):
    """Walvis onder water: een boog van gekleurde steentjes in het zand (zijn regenboog, nu van steen)."""
    kl = [ROOD, ORANJE, GEEL_V, GROEN, BLAUW, PAARS]
    for rij, (fx, kleur_rij) in enumerate(((1.0, kl), (.78, kl))):
        n = 11 if rij == 0 else 9
        for i in range(n):
            a = math.pi + math.pi * i / (n - 1)
            c = kleur_rij[min(5, int(i / n * 6))] if rij == 0 else kleur_rij[min(5, int(i / n * 6))]
            r_ = 3.6 if rij == 0 else 3.0
            d.rondje(cx + rx * fx * math.cos(a), cy + ry * fx * math.sin(a), r_, r_ * .8, c, WIT, dikte=1.0)


def plek_whale(d, dd, nacht, zak=0):
    """Open diep blauw: verre ruggen, lage zandbult, een grote ronde steen links, een schelp rechts."""
    if d.am: d.tint(lambda ld: ld.rectangle([0, 150 * d.s, d.N, d.N], fill=255), (0, 0, 40), .35)
    verre_ruggen(d, dd, [(40, 206, 70, 16), (226, 202, 60, 18)], zak)
    zandbult(d, 222, zak)
    d.rondje(30, 226 + zak, 16, 11, STEEN, STEEN_R, glans=STEEN_R)
    d.rondje(226, 236 + zak, 6, 4, (255, 170, 170), WIT, dikte=1.2)


def plek_orca(d, dd, nacht, zak=0):
    """Open water: verre ruggen, zandbank, twee ronde stenen rechts, een schelpje."""
    verre_ruggen(d, dd, [(60, 200, 80, 18), (212, 196, 70, 20)], zak)
    zandbult(d, 226, zak)
    d.rondje(218, 230 + zak, 14, 9, STEEN, STEEN_R, glans=STEEN_R)
    d.rondje(238, 222 + zak, 8, 6, STEEN, STEEN_R)
    d.rondje(44, 238 + zak, 5, 3.4, (255, 170, 170), WIT, dikte=1.2)


def plek_narwhal(d, dd, nacht, zak=0, ijs=True):
    """Onder het ijs met een wak: ijs als plafond bovenin met een gat in het midden, bodem van grijs grind, twee ijsbrokjes."""
    if ijs:
        # ijs hangt links en rechts aan het oppervlak, in het midden het wak waar het licht door valt
        for cx, cy, rx, ry in [(26, 26, 40, 16), (234, 26, 40, 16), (60, 14, 22, 9), (200, 14, 22, 9)]:
            d.rondje(cx, cy, rx, ry, IJS, WIT, dikte=1.6)
        for x, y in ((28, 42), (46, 38), (214, 38), (232, 42)):      # ijspegeltjes onder het ijs
            d.blob([(x - 3.4, y - 1), (x + 3.4, y - 1), (x, y + 7)], IJS, WIT, 1.0)
    verre_ruggen(d, dd, [(36, 204, 60, 18), (230, 200, 54, 20)], zak)
    zandbult(d, 226, zak, ((85, 85, 170), (0, 0, 85)))
    for x, y, rx, ry in ((40, 232, 9, 6), (220, 236, 11, 6)):
        d.rondje(x, y + zak, rx, ry, IJS, WIT, dikte=1.4)
        d.rondje(x - rx * .35, y + zak - ry * .35, rx * .25, ry * .25, WIT)


def plek_squid(d, dd, nacht, zak=0):
    """Schemerig water met lichtpuntjes (niet zwart): donkere ronde rotsen met lichte rand, gloeipuntjes bij de bodem."""
    if d.am: d.tint(lambda ld: ld.rectangle([0, 146 * d.s, d.N, d.N], fill=255), (20, 0, 60), .2)
    verre_ruggen(d, dd, [(30, 200, 60, 26), (232, 196, 56, 30)], zak)
    d.rondje(130, 258 + zak, 70, 18, (85, 0, 170), PAARS)
    d.rondje(36, 228 + zak, 20, 12, (85, 0, 170), PAARS, glans=PAARS)
    d.rondje(222, 228 + zak, 22, 13, (85, 0, 170), PAARS, glans=PAARS)
    for x, y, r_ in ((18, 182, 1.4), (30, 172, 1.0), (52, 196, 1.2), (236, 176, 1.4), (246, 194, 1.0), (206, 190, 1.2), (70, 214, 1.0), (190, 212, 1.0)):
        if d.am: d.gloed_ellips(x, y + zak, r_ * 2.6, r_ * 2.6, (170, 255, 255), .45, stappen=2, groei=.5)
        d.rondje(x, y + zak, r_, r_, (170, 255, 255))


PLEK = {'whale': plek_whale, 'orca': plek_orca, 'narwhal': plek_narwhal, 'squid': plek_squid}


def held_onder(d, nacht, dn, hx, hy, m, scherm):
    """Held vooraan met zijn grap onder water."""
    if not HELD_AAN[0]: return
    if dn == 'whale':
        steentjesboog(d, hx, hy + m * .9 + 15, m * 1.02, m * .42)
        v3.dier_kantel(d, hx, hy, m, WALVIS, 0)
    elif dn == 'orca':
        v3.dier_kantel(d, hx, hy, m, ORKA, 0)
        strik(d, *R(hx, hy, m, 0, -.42, .42), m / 34, 0)
        if scherm != 'eind':        # rijtje visjes met nootjes boven hun kop: zijn koortje
            for i, (fx, fy) in enumerate(((hx + m * 1.45, hy + m * .5), (hx + m * 1.95, hy + m * .3), (hx + m * 2.45, hy + m * .1))):
                schelp(d, fx + 2, fy + 11, 1.0)
                visje(d, fx, fy, .95, (ORANJE, GEEL_V, ROZE)[i])
                noot(d, fx - 2, fy - 10, .8, GEEL_V if i != 1 else WIT, i == 1)
    elif dn == 'narwhal':
        v3.dier_kantel(d, hx, hy, m, NARWAL, 0)
        tand(d, hx, hy, m, 0)
        ijsje(d, *R(hx, hy, m, 0, -1.6, -.24), (1.3 if scherm != 'eind' else .85))
    elif dn == 'squid':
        if d.am: d.gloed_ellips(hx, hy + m * .15, m * .85, m * .9, (170, 120, 255), .35, groei=.2)   # licht achter hem: hij komt los van het schemerwater
        v3.dier_kantel(d, hx, hy, m, INKT, 0)
        plantje(d, hx - 2, hy + m * 1.12, 1.3 if scherm != 'eind' else .9)   # een klein plantje voor zijn grote lijf


def hold(D_, am, dd, nacht, dn):
    v32._KAP['y'] = 117 + 22
    d = Doek(D_, am)
    pos = {'whale': (130, 180, 44), 'orca': (98, 186, 40), 'narwhal': (150, 186, 42), 'squid': (130, 198, 48)}[dn]
    v3.onder(d, dd, nacht, xo=pos[0], xh=pos[0])
    PLEK[dn](d, dd, nacht)
    if dn != 'squid': stofjes(d, dd)
    held_onder(d, nacht, dn, *pos, 'hold')
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 117, '61 bpm · round 2', 18, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht, dn):
    v32._KAP['y'] = 140
    d = Doek(D_, am)
    pos = {'whale': (130, 186, 42), 'orca': (98, 190, 38), 'narwhal': (150, 192, 42), 'squid': (130, 198, 48)}[dn]
    v3.onder(d, dd, nacht, xo=pos[0], xh=pos[0])
    PLEK[dn](d, dd, nacht, zak=4)
    if dn != 'squid': stofjes(d, dd)
    held_onder(d, nacht, dn, *pos, 'menu')
    s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t in [(52, 'Rounds'), (86, 'Calm 4-7-8')]:
        fill = ((0, 30, 60) if dd is DAG else (0, 0, 50)) if am else (0, 0, 85)
        d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                               outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


def eind(D_, am, dd, nacht, dn):
    """Zelfde indeling als v32.eind: kop en tijden tot y 70, held links en vriend in een belletje rechts, naam van 150 tot 196."""
    v32._KAP['y'] = 72
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    v32.bundel(d, dd, nacht, xo=184, xh=184, yh=136)
    PLEK[dn](d, dd, nacht, zak=14) if dn != 'narwhal' else plek_narwhal(d, dd, nacht, zak=14, ijs=False)
    if dn != 'squid': stofjes(d, dd)
    for x, y, k in [(228, 76, 7), (236, 140, 5)]: fonkel(d, x, y, k)
    vriend, naam = VRIEND[dn]
    bx, by, brx, bry = 186, 108, 36, 32
    kring(d, dd, bx, by, 40)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 3.6, 3.6, WIT)
    if HELD_AAN[0]: d.dier(bx, by + 1, 22 if vriend in (INKT, D[22]) else 26, vriend)
    hart = [(132 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 94 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 18, '3 rounds done', 27, GEEL)
    d.tekst(130, 46, '1:20   1:45   1:58', 22, WIT)
    pos = {'whale': (74, 112, 30), 'orca': (74, 114, 28), 'narwhal': (80, 116, 26), 'squid': (70, 112, 26)}[dn]
    if dn == 'whale' and HELD_AAN[0]:
        hx, hy, m = pos
        sx, sy = R(hx, hy, m, 0, -.6, -.66)
        boog(d, sx + 24, sy + 6, 26, 22, [ROOD, ORANJE, GEEL_V, GROEN, BLAUW, PAARS] if not nacht else [WIT, (170, 170, 255), WIT], 2.0)
        v3.dier_kantel(d, hx, hy, m, WALVIS, 0)
    else:
        held_onder(d, nacht, dn, *pos, 'eind')
    d.tekst(130, 150, 'new friend', 18, WIT, False)
    d.tekst(130, 166, naam, 32 if len(naam) < 9 else (29 if len(naam) < 11 else 26), GEEL)
    stippen(d.dr, 130 * d.s, 212 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def scherm(naam, dn):
    if naam == 'in': return lambda D_, am, dd, n: adem(D_, am, dd, n, dn)
    if naam == 'uit': return lambda D_, am, dd, n: adem(D_, am, dd, n, dn, top=170, woord='breathe out', getal='9', fase='uit')
    if naam == 'calm': return lambda D_, am, dd, n: adem(D_, am, dd, n, dn, top=146, woord='breathe out', getal='5', onder='4-7-8 · 2 of 4', fase='calm')
    return lambda D_, am, dd, n: {'hold': hold, 'menu': menu, 'eind': eind}[naam](D_, am, dd, n, dn)


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']
DIEREN = ['whale', 'orca', 'narwhal', 'squid']

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for dn in sys.argv[2:] or DIEREN:
        rij = {}
        for nacht in (False, True):
            dd = NACHT if nacht else DAG
            for D_, am in ((454, True), (260, False)):
                for naam in NAMEN:
                    im = scherm(naam, dn)(D_, am, dd, nacht)
                    im.save(os.path.join(uit, f'{dn}-{naam}-{"nacht" if nacht else "dag"}-{D_}.png')); rij[(naam, nacht, D_)] = im
        for D_, k in ((454, 1), (260, 2)):
            g = 12 * k; W = D_ * k; n = len(NAMEN)
            ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
            for j, nacht in enumerate((False, True)):
                for i, naam in enumerate(NAMEN):
                    ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
            ov.save(os.path.join(uit, f'overzicht-{dn}-{D_}-{k}x.png'))
