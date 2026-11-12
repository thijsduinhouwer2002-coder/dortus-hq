# Werelden v4, familie strand (run 50, 12 nov): garnaal, zeester, kreeft, zeehond en zeeotter
# in de opzet van krab, schildpad en clownvis (werelden_v32). Lucht, zee, water, bundel, tekst en eindscherm-opbouw
# komen uit v21/v3/v32; hier alleen per dier een eigen plek onder water en een eigen los grapvoorwerp.
#  - shrimp:   surfplankje op jouw golf / kiezelstrandje onder een steiger, plankje rechtop in het zand
#  - starfish: telescoopje naar zon (donker glaasje) of maan / getijdenpoel met mosselbank, telescoop ligt in de poel
#  - lobster:  strohoedje, gietertje en bloempotje drijven op de golf / zeegrastuin met een struikje als hartje
#  - seal:     ijsschots met hengel, rode dobber op jouw golf / ijsklonten op de bodem, visje bij de dobber
#  - otter:    schelp en steentje op zijn buik / kelpwoud, hij heeft zich met een kelplint vastgeknoopt
# Coordinaten in 1/260 D.   python3 werelden_v4_strand.py <uitmap> [dier ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
import werelden_v3 as v3
import werelden_v32 as v
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ZON, ROZE, ZAND, ZAND_DONKER, D, bellen, fonkel, stofjes, kring
from blad_v9 import stippen
from PIL import Image

SHRIMP, STAR, SEAL, OTTER, LOBSTER = D[1], D[6], D[12], D[15], D[22]
HELD = {'shrimp': SHRIMP, 'starfish': STAR, 'lobster': LOBSTER, 'seal': SEAL, 'otter': OTTER}
VRIEND = {'shrimp': (D[5], 'Seahorse'), 'starfish': (D[8], 'Pufferfish'), 'lobster': (D[23], 'Whale'),
          'seal': (D[13], 'Dolphin'), 'otter': (D[18], 'Sunfish')}
DONKER = (0, 0, 85)
HOUT, HOUT_L = (170, 85, 0), (255, 170, 85)
GROEN, GROEN_L, GROEN_D = (0, 170, 85), (85, 255, 85), (0, 85, 0)
ROOD = (255, 0, 0)
IJS, IJS_L = (170, 255, 255), WIT
KELP, KELP_L = (85, 170, 0), (170, 255, 85)


def lijn(d, pts, c, b):
    d.dr.line([d.P(*p) for p in pts], fill=c, width=max(1, round(b * d.s)), joint='curve')
    for p in (pts[0], pts[-1]): d.rondje(p[0], p[1], b / 2, b / 2, c)


def rot(cx, cy, a_graden):
    a = math.radians(a_graden)
    return lambda x, y: (cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a))


def staaf(d, p0, p1, b, c, rand=WIT, rb=1.6):
    """Dikke ronde staaf met lichte rand (handvat, steigerpaal, telescoop)."""
    if rand: lijn(d, [p0, p1], rand, b + 2 * rb)
    lijn(d, [p0, p1], c, b)


# ---------------- grapvoorwerpen ----------------
def surfplank(d, cx, cy, L=34, hoek=0, staand=False):
    """Geel surfplankje met rode middenstreep en witte rand; staand = rechtop (onder water in het zand)."""
    a = hoek + (-90 if staand else 0); r = rot(cx, cy, a)
    pts = [r(L * math.cos(t), L * .26 * math.sin(t) * (1 if math.cos(t) < 0 else 1 - .25 * math.cos(t))) for t in [i / 24 * 2 * math.pi for i in range(24)]]
    pts = [r(L * math.cos(t) * (1 if math.cos(t) < 0 else 1.0), (L * .25) * math.sin(t) * (.95 if math.cos(t) < 0 else (1 - .5 * math.cos(t) ** 2))) for t in [i / 24 * 2 * math.pi for i in range(24)]]
    d.blob(pts, (255, 255, 0), WIT, 1.8)
    lijn(d, [r(-L * .82, 0), r(L * .82, 0)], ROOD, 2.6)
    if staand: d.rondje(*r(-L * .55, 0), 2.2, 2.2, ROOD)
    else:   # vinnetje onder de staart
        d.blob([r(-L * .78, L * .2), r(-L * .62, L * .2), r(-L * .74, L * .46)], ROOD)


def telescoop(d, x, y, hoek=-35, k=1.0, nacht=False, poten=True):
    """Telescoopje op drie pootjes. Bij dag een donker glaasje voor de zon (hij kijkt naar de zon), bij nacht een geel glaasje."""
    r = rot(x, y, hoek)
    if poten:
        for dx in (-9, 0, 9): staaf(d, (x, y), (x + dx * k, y + 18 * k), 2.4 * k, HOUT, None)
    staaf(d, r(-14 * k, 0), r(10 * k, 0), 8 * k, (255, 85, 0), WIT)       # dikke buis
    staaf(d, r(10 * k, 0), r(22 * k, 0), 11 * k, (170, 0, 85), WIT)      # wijde kop
    staaf(d, r(-24 * k, 0), r(-14 * k, 0), 5 * k, (255, 170, 0), WIT, 1.2)  # oogstuk
    lx, ly = r(22.5 * k, 0)
    d.rondje(lx, ly, 2.6 * k, 5 * k, (0, 0, 0) if not nacht else (255, 255, 170))
    d.rondje(x, y, 2.4 * k, 2.4 * k, (255, 255, 0))


def strohoed(d, x, y, k=1.0):
    """Strohoedje met rood bandje (tuinman)."""
    d.rondje(x, y, 19 * k, 4.6 * k, (255, 255, 85), (170, 85, 0), dikte=1.4)
    d.blob([(x - 10 * k, y), (x - 9 * k, y - 10 * k), (x - 4 * k, y - 13 * k), (x + 4 * k, y - 13 * k), (x + 9 * k, y - 10 * k), (x + 10 * k, y)], (255, 255, 85), (170, 85, 0), 1.4)
    d.dr.rectangle([d.P(x - 9.6 * k, y - 4.6 * k), d.P(x + 9.6 * k, y - 1.4 * k)], fill=ROOD)


def gieter(d, x, y, k=1.0):
    """Groen gietertje met tuit en handvat, broesje met stipjes."""
    staaf(d, (x + 6 * k, y - 2 * k), (x + 21 * k, y - 15 * k), 3.4 * k, GROEN, WIT, 1.3)   # tuit
    d.rondje(x + 22 * k, y - 16 * k, 4.2 * k, 4.2 * k, GROEN_L, WIT, dikte=1.3)
    d.dr.arc([d.P(x - 16 * k, y - 18 * k), d.P(x + 2 * k, y - 2 * k)], 180, 360, fill=WIT, width=max(2, round(5.4 * k * d.s)))
    d.dr.arc([d.P(x - 16 * k, y - 18 * k), d.P(x + 2 * k, y - 2 * k)], 180, 360, fill=GROEN_D, width=max(1, round(2.8 * k * d.s)))
    d.blob([(x - 12 * k, y - 10 * k), (x + 8 * k, y - 10 * k), (x + 7 * k, y + 6 * k), (x - 11 * k, y + 6 * k)], GROEN, WIT, 1.6)
    d.dr.rectangle([d.P(x - 11.6 * k, y - 4 * k), d.P(x + 7.6 * k, y - 2 * k)], fill=GROEN_L)


def bloempot(d, x, y, k=1.0, bloem=True):
    if bloem:
        staaf(d, (x, y - 6 * k), (x, y - 18 * k), 2 * k, GROEN, None)
        for a in range(5):
            t = a / 5 * 2 * math.pi; d.rondje(x + 4.4 * k * math.cos(t), y - 21 * k + 4.4 * k * math.sin(t), 3 * k, 3 * k, (255, 85, 170), WIT, dikte=.9)
        d.rondje(x, y - 21 * k, 2.6 * k, 2.6 * k, (255, 255, 0))
    d.blob([(x - 9 * k, y - 6 * k), (x + 9 * k, y - 6 * k), (x + 6.5 * k, y + 7 * k), (x - 6.5 * k, y + 7 * k)], (255, 85, 0), WIT, 1.5)
    d.dr.rectangle([d.P(x - 10.5 * k, y - 8.5 * k), d.P(x + 10.5 * k, y - 4 * k)], fill=(170, 85, 0))


def hart_pts(x, y, s):
    return [(x + s * 16 * math.sin(t) ** 3 / 16, y - s * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) / 16)
            for t in [i / 40 * 2 * math.pi for i in range(40)]]


def zeegras_hart(d, x, y, s=26):
    """Een pluk zeegras die als hartje geknipt is, op een stammetje."""
    staaf(d, (x, y + s * .8), (x, y + s * 1.5), 4, GROEN_D, WIT, 1.2)
    d.blob(hart_pts(x, y, s), GROEN, WIT, 2.2)
    d.blob(hart_pts(x - s * .08, y - s * .1, s * .62), GROEN_L)
    for dx, dy in ((-.5, -.3), (.42, -.4), (.05, .25), (-.2, -.05), (.3, .05)):
        d.rondje(x + dx * s, y + dy * s, 1.6, 1.6, GROEN_D)


def ijsschots(d, x, y, b=50, h=9):
    d.blob([(x - b, y), (x - b * .8, y - h), (x + b * .7, y - h * 1.1), (x + b, y - h * .2), (x + b * .85, y + h * .5), (x - b * .85, y + h * .5)], IJS, WIT, 1.8)
    d.blob([(x - b * .7, y - h * .7), (x + b * .55, y - h * .85), (x + b * .5, y - h * .45), (x - b * .65, y - h * .3)], WIT)


def dobber(d, x, y, k=1.0):
    d.rondje(x, y, 5.6 * k, 5.6 * k, ROOD, WIT, dikte=1.4)
    d.dr.pieslice([d.P(x - 5.6 * k, y - 5.6 * k), d.P(x + 5.6 * k, y + 5.6 * k)], 0, 180, fill=WIT)
    staaf(d, (x, y - 5 * k), (x, y - 10 * k), 2 * k, ROOD, None)


def hengel(d, hand, tip, dob):
    staaf(d, hand, tip, 3.2, HOUT, WIT, 1.2)
    d.rondje(hand[0], hand[1], 3.2, 3.2, (85, 85, 85), WIT, dikte=1)
    d.dr.line([d.P(*tip), d.P((tip[0] + dob[0]) / 2, (tip[1] + dob[1]) / 2 + 8), d.P(dob[0], dob[1] - 10)], fill=WIT, width=max(1, round(1.2 * d.s)), joint='curve')


def schelp(d, x, y, k=1.0, c=(255, 170, 170)):
    d.blob([(x + 9 * k * math.cos(t), y - 8 * k * math.sin(t)) for t in [math.pi * i / 10 for i in range(11)]] + [(x + 2 * k, y + 4 * k), (x - 2 * k, y + 4 * k)], c, WIT, 1.4)
    for a in (-60, -25, 25, 60):
        t = math.radians(90 + a); lijn(d, [(x, y + 2 * k), (x + 7 * k * math.cos(t), y - 6.5 * k * math.sin(t))], (255, 85, 85), 1.1 * k)


def steentje(d, x, y, k=1.0):
    d.rondje(x, y, 5.5 * k, 4.4 * k, (170, 170, 170), WIT, glans=WIT, dikte=1.3)


def visje(d, x, y, k=1.0, c=(255, 170, 0), links=True):
    sg = -1 if links else 1
    d.blob([(x - sg * 6 * k, y), (x - sg * 12 * k, y - 5 * k), (x - sg * 12 * k, y + 5 * k)], c, WIT, 1.1)
    d.rondje(x, y, 8 * k, 5 * k, c, WIT, dikte=1.2)
    d.rondje(x + sg * 4 * k, y - 1 * k, 1.3 * k, 1.3 * k, (0, 0, 0))


def kelplint(d, x0, y0, x1, y1, buig=10, b=6):
    pts = []
    for i in range(13):
        t = i / 12; pts.append((x0 + (x1 - x0) * t + buig * math.sin(t * math.pi * 2), y0 + (y1 - y0) * t))
    lijn(d, pts, KELP_L, b + 2.4); lijn(d, pts, KELP, b)


def lint_vast(d, *a, **k):
    """Het kelplint van de otter (grapvoorwerp, los van het kelpwoud)."""
    kelplint(d, *a, **k)


# ---------------- boven water ----------------
def adem(D_, am, dd, nacht, dier, top=134, woord='breathe in', getal='12', onder='round 2 · 18 left', fase='in'):
    d = Doek(D_, am)
    v3.lucht(d, dd, nacht, top)
    wx = 222
    wk = (255, 255, 255) if not nacht else (85, 85, 170); wr = (170, 255, 255) if not nacht else (0, 0, 170)
    if dier not in ('starfish',):
        for cx, cy, rx, ry in [(wx - 8, 70, 14, 8), (wx + 4, 64, 12, 10), (wx + 14, 72, 11, 7)]: d.rondje(cx, cy, rx, ry, wr)
        for cx, cy, rx, ry in [(wx - 8, 69, 12, 6.5), (wx + 4, 63, 10, 8.5), (wx + 14, 71, 9, 5.5)]: d.rondje(cx, cy, rx, ry, wk)
    v3.zee(d, nacht, top)
    v3.volgende_vriend(d, nacht, top, x=196)
    hoek = {'in': 8, 'calm': 3, 'uit': 0}[fase]
    hoog = top > 140            # zee hoog: held naar het midden onder het cijfer
    if dier == 'shrimp':
        hx = 132 if hoog else 156; dy = -2 if hoog else 0
        surfplank(d, hx + 2, top + 2 + dy, 40, hoek=-hoek * .6)
        v3.dier_kantel(d, hx - 2, top - 14 + dy, 34, SHRIMP, hoek)
    elif dier == 'starfish':
        hx = 138 if hoog else 160; hy = top - 2
        v3.dier_kantel(d, hx, hy, 34, STAR, hoek * .5)
        # telescoop naast hem, gericht op zon of maan (links boven); hij kijkt erdoor
        telescoop(d, hx - 40, hy - 6, hoek=-152 - hoek, k=1.15, nacht=nacht)
        # zwemband van het water voor zijn onderkant: hij staat in de golf
    elif dier == 'lobster':
        hx = {134: 166, 146: 180, 170: 140}[top]; hy = top - 4
        gieter(d, hx - 70 if not hoog else hx + 62, top + 4, 1.05)
        bloempot(d, 60 if not hoog else 212, top + 2, 1.05) if not hoog else bloempot(d, hx - 64, top + 2, 1.0)
        v3.dier_kantel(d, hx, hy, 38, LOBSTER, hoek)
        strohoed(d, hx + 2, hy - 25, 1.15)
    elif dier == 'seal':
        hx = 140 if hoog else 176; hy = top - (16 if hoog else 11)
        ijsschots(d, hx + 6, top + 2, 52, 9)
        v3.dier_kantel(d, hx, hy, 32, SEAL, hoek * .6)
        dob = (hx - 76 if not hoog else hx - 80, top + 8)
        hengel(d, (hx - 26, hy + 8), (hx - 60, hy - 18), dob)
        dobber(d, *dob, 1.2)
    elif dier == 'otter':
        hx = 136 if hoog else 158; hy = top - 6
        # ronde 2: 70 tot 90 graden gedraaid geprobeerd (-80, 100, 180): dan staat hij rechtop of op zijn kop.
        # De sticker ligt zelf al op zijn rug met iets op zijn buik; plat laten en de schelp op die buik leggen.
        v3.dier_kantel(d, hx, hy, 36, OTTER, hoek * .6)
        # ronde 3: een grote schelp op zijn buik en een steen erboven (twee vormen, samen ongeveer de helft van zijn breedte)
        schelp(d, hx + 6, hy - 4, 2.0)
        steentje(d, hx + 6, hy - 26, 1.6)
    v3.tekst_adem(d, top, woord, getal, onder)
    return d.klaar()


# ---------------- plekken onder water ----------------
def bodem(d, y, c, rand, zak=0, golf=3):
    """Een eigen bodemvlak met lichte golvende rand (geen gele zandschijf meer, ronde 2)."""
    s = d.s
    pts = [d.P(x, y + zak + golf * math.sin(x / 260 * 2 * math.pi * 2.5)) for x in range(0, 261, 2)]
    d.dr.polygon([(p[0], p[1] - 2.2 * s) for p in pts] + [d.P(260, 262), d.P(0, 262)], fill=rand)
    d.dr.polygon(pts + [d.P(260, 262), d.P(0, 262)], fill=c)


GRIJS, GRIJS_L, GRIJS_D = (170, 170, 170), WIT, (85, 85, 85)


def plek(d, dd, dier, hx, hy, m, held=True, zak=0, nacht=False, stand='hold'):
    """Eigen plek per dier, drie tot vijf dingen, alles binnen de ronde rand; held vooraan."""
    if dier == 'shrimp':   # kiezelstrandje onder een steiger: grijze kiezelbank, twee palen met een dwarsbalk, een touw
        bodem(d, 224, GRIJS_D, GRIJS, zak)
        for i, x in enumerate(range(10, 260, 15)):
            d.rondje(x, 238 + zak + 5 * (i % 2), 6.5, 4.6, GRIJS if i % 3 else (255, 170, 170), WIT, dikte=1)
        for px in (36, 224):
            staaf(d, (px, 132 + zak), (px, 236 + zak), 12, HOUT, HOUT_L, 1.8)
            for yy in (176, 204): d.rondje(px, yy + zak, 6, 2, (85, 170, 85))      # aangroei op de paal
        if held:
            surfplank(d, hx + m * 1.25, hy + 4, m * .8, staand=True)
            d.dier(hx, hy, m, SHRIMP)
    elif dier == 'starfish':   # getijdenpoel: ring van grijze rotsen om een kom licht water, mossels op de rand
        bodem(d, 218, GRIJS_D, GRIJS, zak)
        d.rondje(130, 246 + zak, 96, 20, (0, 170, 170), WIT, dikte=2)              # de poel
        d.rondje(130, 250 + zak, 80, 12, (85, 255, 255))
        for x, y, rx, ry in [(22, 220, 26, 20), (238, 218, 26, 22), (40, 244, 16, 10), (222, 244, 16, 10)]:
            d.rondje(x, y + zak, rx, ry, GRIJS, WIT, glans=WIT)
        for x, y in [(14, 202), (28, 200), (244, 200), (232, 204)]:
            d.rondje(x, y + zak, 5, 3, DONKER, (85, 85, 255), dikte=1.1)
        if held:
            telescoop(d, hx + m * 1.5, hy + m * .45, hoek=-20, k=1.45 * m / 40, nacht=nacht, poten=False)
            d.dier(hx, hy, m, STAR)
    elif dier == 'lobster':   # tuin: groen gazon, wit tuinhekje, twee bloempotten op de bodem
        bodem(d, 222, (0, 170, 85), GROEN_L, zak)
        for x in range(14, 252, 16):
            if 70 < x < 196 and held: continue          # hekje opzij: de held en zijn hartje staan vrij
            e = 12 if stand == 'eind' else 0
            d.blob([(x - 4, 224 + zak), (x - 4, 196 + zak + e), (x, 191 + zak + e), (x + 4, 196 + zak + e), (x + 4, 224 + zak)], WIT, GRIJS_D, 1)
        for yy in (202, 216):
            for x0, x1 in ((6, 74), (190, 254)) if held else ((6, 254),):
                ee = 8 if stand == 'eind' else 0
                d.dr.rectangle([d.P(x0, yy + zak + ee), d.P(x1, yy + 3 + zak + ee)], fill=WIT)
        bloempot(d, 44, 238 + zak, 1.0); bloempot(d, 214, 240 + zak, .9)
        if held:
            zeegras_hart(d, hx + m * 1.55, hy - m * .2, m * .62)
            d.dier(hx, hy, m, LOBSTER)
    elif dier == 'seal':   # onder het ijs: donkere ijsrand bovenin, een kleine schots, donkere stenen bodem
        s = d.s
        ijs, ijs_r = ((0, 85, 170), (85, 170, 255)) if not nacht else ((0, 0, 170), (85, 85, 255))
        pts = [(x, 14 + 4 * math.sin(x / 9) + 3 * math.sin(x / 23)) for x in range(0, 261, 3)]
        d.dr.polygon([d.P(x, y + 2) for x, y in pts] + [d.P(260, 0), d.P(0, 0)], fill=ijs_r)
        d.dr.polygon([d.P(x, y) for x, y in pts] + [d.P(260, 0), d.P(0, 0)], fill=ijs)
        if stand != 'eind': ijsschots(d, 206, 22, 20, 5)   # kleine schots in de ijsrand
        bodem(d, 226, (0, 85, 85), (85, 170, 170), zak)
        for x, y, r_ in [(24, 236, 9), (56, 244, 6), (206, 242, 7), (236, 234, 10)]:
            d.rondje(x, y + zak, r_, r_ * .7, GRIJS_D, GRIJS, dikte=1.1)
        if held:
            dx_, dy_ = hx + m * 1.35, hy - m * .7
            d.dr.line([d.P(dx_, dy_ - 20), d.P(dx_, dy_ - 10)], fill=WIT, width=max(1, round(1.2 * d.s)))
            dobber(d, dx_, dy_, 1.25)
            visje(d, dx_ + 4, dy_ + 18, 1.0, links=True)
            d.dier(hx, hy, m, SEAL)
    elif dier == 'otter':   # kelpwoud: donkergroene bodem, hoge kelplinten met blaasjes aan beide kanten
        bodem(d, 228, GROEN_D, KELP, zak)
        for x0, b, h in [(14, 9, 150), (34, 8, 112), (54, 7, 80), (208, 7, 86), (228, 8, 120), (248, 9, 156)]:
            top = 236 + zak - h
            kelplint(d, x0, 240 + zak, x0 + (6 if x0 < 130 else -6), top, buig=5, b=b * .75)
            for i in range(3):
                yy = 236 + zak - h * (.3 + i * .25); sg = 1 if x0 < 130 else -1
                d.blob([(x0, yy), (x0 + sg * 11, yy - 7), (x0 + sg * 3, yy - 2)], KELP, KELP_L, 1)
                d.rondje(x0 + sg * 4, yy + 3, 2.2, 2.2, (255, 255, 85))
        if held:
            lint_vast(d, hx + 6, 248, hx + 2, hy + m * .35, buig=6, b=5)
            d.dier(hx, hy, m, OTTER)
            bx, by = hx + 2, hy + m * .38
            for sg in (-1, 1):
                d.blob([(bx, by), (bx + sg * 10, by - 6), (bx + sg * 10, by + 6)], KELP, KELP_L, 1.2)
            d.rondje(bx, by, 3, 3, KELP_L)


def hold(D_, am, dd, nacht, dier):
    v._KAP['y'] = 139
    d = Doek(D_, am)
    hx, hy, m = {'shrimp': (110, 184, 44), 'starfish': (112, 188, 40), 'lobster': (104, 186, 42),
                 'seal': (116, 192, 38), 'otter': (114, 190, 42)}[dier]
    v3.onder(d, dd, nacht, xo=hx + 6, xh=hx + 8)
    plek(d, dd, dier, hx, hy, m, nacht=nacht)
    stofjes(d, dd)
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 117, '61 bpm · round 2', 18, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht, dier):
    v._KAP['y'] = 140
    d = Doek(D_, am)
    hx, hy, m = {'shrimp': (112, 194, 38), 'starfish': (112, 196, 37), 'lobster': (106, 196, 36),
                 'seal': (118, 200, 33), 'otter': (116, 198, 36)}[dier]
    v3.onder(d, dd, nacht, xo=hx + 6, xh=hx + 8)
    plek(d, dd, dier, hx, hy, m, zak=6, nacht=nacht, stand='menu')
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
    """Opbouw van v32-eind: kop en tijden tot y 70, held links en vriend in belletje rechts, naam van 150 tot 196."""
    v._KAP['y'] = 72
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    v.bundel(d, dd, nacht, xo=184, xh=184, yh=136)
    plek(d, dd, dier, 0, 0, 0, held=False, zak=24, nacht=nacht, stand='eind')
    vriend, naam = VRIEND[dier]
    stofjes(d, dd)
    for x, y, k in [(228, 76, 7), (236, 140, 5)]: fonkel(d, x, y, k)
    bx, by, brx, bry = 186, 108, 36, 32
    kring(d, dd, bx, by, 40)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 3.6, 3.6, WIT)
    d.dier(bx, by + 1, 26, vriend)
    hart = [(132 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 94 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 18, '3 rounds done', 27, GEEL)
    d.tekst(130, 46, '1:20   1:45   1:58', 22, WIT)
    if dier == 'shrimp':
        surfplank(d, 106, 112, 26, staand=True); d.dier(72, 118, 28, SHRIMP)
    elif dier == 'starfish':
        telescoop(d, 104, 126, hoek=-30, k=.8, nacht=nacht, poten=False); d.dier(72, 116, 27, STAR)
    elif dier == 'lobster':
        zeegras_hart(d, 104, 108, 14); d.dier(70, 118, 28, LOBSTER)
    elif dier == 'seal':
        d.dr.line([d.P(104, 78), d.P(104, 96)], fill=WIT, width=max(1, round(1.2 * d.s))); dobber(d, 104, 104, 1.0)
        visje(d, 110, 122, .8); d.dier(70, 120, 26, SEAL)
    elif dier == 'otter':
        d.dier(76, 116, 30, OTTER); schelp(d, 80, 112, 1.0); steentje(d, 92, 118, .9)
    d.tekst(130, 150, 'new friend', 18, WIT, False)
    d.tekst(130, 166, naam, 32 if len(naam) < 9 else 29, GEEL)
    stippen(d.dr, 130 * d.s, 212 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def scherm(naam, dier):
    def kap(f):
        def g(D_, am, dd, n):
            v._KAP['y'] = 140; return f(D_, am, dd, n)
        return g
    if naam == 'in': return kap(lambda D_, am, dd, n: adem(D_, am, dd, n, dier))
    if naam == 'uit': return kap(lambda D_, am, dd, n: adem(D_, am, dd, n, dier, top=170, woord='breathe out', getal='9', fase='uit'))
    if naam == 'calm': return kap(lambda D_, am, dd, n: adem(D_, am, dd, n, dier, top=146, woord='breathe out', getal='5', onder='4-7-8 · 2 of 4', fase='calm'))
    return lambda D_, am, dd, n: {'hold': hold, 'menu': menu, 'eind': eind}[naam](D_, am, dd, n, dier)


NAMEN = v.NAMEN
DIEREN = ['shrimp', 'starfish', 'lobster', 'seal', 'otter']

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
