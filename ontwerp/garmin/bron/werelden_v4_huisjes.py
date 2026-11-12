# Werelden v4, familie huisjes (agent voor Mila, run 50, 12 nov 2026): Fish, Octopus, Eel, Pufferfish, Sea cucumber.
# Zelfde opzet als krab, schildpad en clownvis (werelden_v32): lucht, zee, water, bundel, stofjes en tekst komen uit v21/v3/v32.
# Per dier een eigen plek onder water en een eigen grapvoorwerp (lijst versie 2 in ebb-werelden-v3.md):
#  - fish:     zandvlakte met een groene fles / boven water dobbert hij in de fles, de kurk wipt omhoog bij inademen;
#              onder water is de fles op het zand zijn huis en ligt de kurk ernaast
#  - octopus:  badje op pootjes dat op de bodem is gezakt / hij neemt een bad met een geel badeendje;
#              onder water drijft het eendje boven hem aan het oppervlak
#  - eel:      zand vol gaatjes / hij heeft een idee: een lampje boven zijn kop, aan bij inademen; onder water uit
#  - puffer:   zandbodem met een schelp / hij is een ballon aan een touwtje (hoogte volgt de adem, de sticker groeit niet);
#              onder water zit het touwtje aan de schelp vastgeknoopt
#  - cucumber: een schelp als bedje / hij slaapt altijd: kussen, slaapmuts en drie z'en; onder water een plukje kelp als deken
# Coordinaten in 1/260 D.   python3 werelden_v4_huisjes.py <uitmap> [dier ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
import werelden_v3 as v3
import werelden_v32 as v32          # zet de v32-bundel en nachtkleuren
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ROZE, ZAND, ZAND_DONKER, D, fonkel, stofjes, kring
from blad_v9 import stippen
from PIL import Image

FISH, OCTO, EEL, PUFF, CUKE = D[0], D[9], D[10], D[8], D[24]
DONKER = (0, 0, 85)
GLAS, GLAS_R = (170, 255, 170), (0, 170, 85)
KURK, KURK_R = (170, 85, 0), (85, 0, 0)
EEND, OR = (255, 255, 0), (255, 170, 0)
BLAUW_L = (85, 170, 255)
GRAS, GRAS_L = (0, 170, 85), (85, 255, 85)
# voor de veilige-zone-toets: met ZONDER_HELD aan tekent geen enkel grapvoorwerp
ZONDER_HELD = [False]
ZONDER_DIER = [False]     # alleen de sticker weg (meting: breedte van de held)


def held(fn):
    def g(*a, **k):
        if ZONDER_HELD[0]: return None
        return fn(*a, **k)
    g.__name__ = fn.__name__
    return g


def R(cx, cy, hoek, m=1.0):
    """Punt t.o.v. (cx, cy) in eenheden m, gekanteld; + = neus omhoog (zoals v3.clownshoed)."""
    a = math.radians(hoek)
    return lambda dx, dy: (cx + (dx * math.cos(a) - dy * math.sin(a)) * m, cy + (dx * math.sin(a) + dy * math.cos(a)) * m)


def lijn(d, pts, c, b):
    d.dr.line([d.P(*p) for p in pts], fill=c, width=max(1, round(b * d.s)), joint='curve')


@held
def kantel(d, cx, cy, maat, wie, hoek):
    if ZONDER_DIER[0]: return
    v3.dier_kantel(d, cx, cy, maat, wie, hoek)


@held
def golfje(d, hx, y0, breed, nacht):
    """Golfje voor de buik (zoals bij de schildpad): hij drijft IN het water, niet erop."""
    zk = ((0, 85, 175) if not nacht else (0, 75, 150)) if d.am else ((0, 85, 170) if not nacht else (0, 0, 170))
    pts = [(x, y0 + 1.8 * math.sin((x - hx) / 7)) for x in range(int(hx - breed), int(hx + breed) + 1, 2)]
    d.blob(pts + [(hx + breed * .9, y0 + 8), (hx - breed * .9, y0 + 8)], zk)
    lijn(d, pts, WIT, 1.6)


# ---------------- grapvoorwerpen ----------------
def fles_punten():
    pts = [(1.0 + .3 * math.cos(math.radians(t)), .72 * math.sin(math.radians(t))) for t in range(-90, 91, 15)]
    pts += [(-1.0, .72), (-1.28, .62), (-1.45, .32), (-1.82, .28), (-1.84, .38), (-1.98, .38),
            (-1.98, -.38), (-1.84, -.38), (-1.82, -.28), (-1.45, -.32), (-1.28, -.62), (-1.0, -.72)]
    return pts


@held
def fles_achter(d, f):
    pts = fles_punten()
    d.blob([f(*p) for p in pts], GLAS_R, WIT, 1.4)
    d.blob([f(x * .93 - .04, y * .84) for x, y in pts], GLAS)


@held
def fles_voor(d, f, k):
    """Glimlijnen over de vis heen: hij zit IN de fles."""
    lijn(d, [f(-.75, -.5), f(-.2, -.6), f(.6, -.58)], WIT, max(1.4, .07 * k))
    lijn(d, [f(.78, -.38), f(.95, -.15)], WIT, max(1.2, .06 * k))


@held
def kurk(d, x, y, k, hoek=0, pop=False):
    f = R(x, y, hoek, k)
    d.blob([f(-1, -.75), f(1, -.9), f(1.1, .9), f(-1, .75)], KURK, KURK_R, 1.2)
    lijn(d, [f(-.4, -.55), f(-.4, .55)], (255, 170, 85), .9)
    if pop:      # plopje: drie streepjes rond de kurk
        for a in (-150, -110, -70):
            r1, r2 = 1.5 * k, 2.2 * k
            lijn(d, [(x + r1 * math.cos(math.radians(a)), y + r1 * math.sin(math.radians(a))),
                     (x + r2 * math.cos(math.radians(a)), y + r2 * math.sin(math.radians(a)))], WIT, 1.4)


def fles_met_vis(d, cx, cy, k, m, hoek, nacht=False, kurk_stand=None):
    """Vis in de fles. kurk_stand: 'in' (wipt omhoog), 'calm' (net los), 'uit' (in de hals), None (geen kurk)."""
    f = R(cx, cy, hoek, k)
    fles_achter(d, f)
    vx, vy = f(.12, .02)
    kantel(d, vx, vy, m, FISH, hoek)
    fles_voor(d, f, k)
    if kurk_stand == 'uit':
        kurk(d, *f(-2.08, 0), .17 * k, hoek + 90)
    elif kurk_stand == 'calm':
        kurk(d, *f(-2.35, -.32), .17 * k, hoek + 60)
    elif kurk_stand == 'in':
        kurk(d, *f(-2.4, -.42), .17 * k, hoek + 25, pop=True)


@held
def eend(d, x, y, k=1.0):
    """Geel badeendje, kijkt naar links."""
    d.blob([(x - 6 * k, y - 1 * k), (x + 2 * k, y - 3 * k), (x + 7 * k, y - 6 * k), (x + 8 * k, y - 1 * k),
            (x + 5 * k, y + 4 * k), (x - 4 * k, y + 4 * k)], EEND, DONKER, 1.0)
    d.rondje(x - 3 * k, y - 6 * k, 3.6 * k, 3.4 * k, EEND, DONKER, dikte=1.0)
    d.blob([(x - 6 * k, y - 7 * k), (x - 10.5 * k, y - 5.6 * k), (x - 6 * k, y - 4.4 * k)], OR)
    d.rondje(x - 4 * k, y - 7 * k, .8 * k, .8 * k, (0, 0, 0))
    lijn(d, [(x + 0 * k, y), (x + 4 * k, y + 1 * k)], OR, 1.0)


@held
def badje(d, f, voeten=True, voor=True):
    """Wit badje met een lichtblauwe rand; f in eenheden van het dier."""
    if voeten:
        for sx in (-.95, .95):
            p = f(sx, .86); d.rondje(p[0], p[1], 3.2, 3.2, OR, DONKER, dikte=1.0)
    d.blob([f(-1.38, .06), f(1.38, .06), f(1.3, .45), f(1.05, .78), f(-1.05, .78), f(-1.3, .45)], WIT, DONKER, 1.4)
    d.blob([f(-1.5, -.02), f(1.5, -.02), f(1.5, .14), f(-1.5, .14)], (170, 255, 255), DONKER, 1.2)
    # schuim op de rand
    for dx, dy, r_ in [(-1.25, -.1, .16), (-1.02, -.16, .2), (-.8, -.08, .14), (.62, -.1, .15)]:
        p = f(dx, dy); q = f(dx + r_, dy)
        rr = math.hypot(q[0] - p[0], q[1] - p[1])
        d.rondje(p[0], p[1], rr, rr, WIT, BLAUW_L, dikte=1.0)


def bad_met_octo(d, cx, cy, m, hoek, eend_k=1.4, voeten=True, met_eend=True, op=.32):
    f = R(cx, cy, hoek, m)
    kantel(d, *f(0, -op), m, OCTO, hoek)
    badje(d, f, voeten)
    if met_eend:
        ex, ey = f(1.12, -.06)
        eend(d, ex, ey - 4 * eend_k, eend_k)


@held
def lampje(d, x, y, k, stand, nacht=False):
    """Lampje van een idee: 'aan' (felgeel met stralen), 'half' (lichtgeel, zonder stralen), 'uit' (grijs)."""
    if stand == 'aan':
        if d.am: d.gloed_ellips(x, y, 14 * k, 14 * k, (255, 255, 85), .35)
        for i in range(7):
            a = math.radians(-180 + i * 30)
            lijn(d, [(x + 11 * k * math.cos(a), y + 11 * k * math.sin(a)), (x + 16 * k * math.cos(a), y + 16 * k * math.sin(a))], (255, 255, 85), 2.2 * k)
    c = {'aan': (255, 255, 85), 'half': (255, 255, 170), 'uit': (170, 170, 170)}[stand]
    d.blob([(x - 3.4 * k, y + 5 * k), (x + 3.4 * k, y + 5 * k), (x + 3 * k, y + 10.5 * k), (x - 3 * k, y + 10.5 * k)], (170, 170, 170), DONKER, 1.0)
    lijn(d, [(x - 3.2 * k, y + 7.4 * k), (x + 3.2 * k, y + 7.4 * k)], (85, 85, 85), 1.0)
    d.rondje(x, y, 7 * k, 7 * k, c, WIT if stand != 'uit' else DONKER, dikte=1.3)
    d.rondje(x - 2.6 * k, y - 2.6 * k, 1.5 * k, 1.5 * k, WIT)
    lijn(d, [(x - 2.4 * k, y + 4.4 * k), (x - 1.2 * k, y + 1 * k), (x, y + 2.6 * k), (x + 1.2 * k, y + 1 * k), (x + 2.4 * k, y + 4.4 * k)], (170, 85, 0) if stand != 'uit' else (85, 85, 85), 1.0)


@held
def touwtje(d, pts):
    lijn(d, pts, DONKER, 2.8); lijn(d, pts, WIT, 1.5)


@held
def knoopje(d, x, y, k=1.0):
    d.blob([(x - 3 * k, y + 4 * k), (x, y - 1 * k), (x + 3 * k, y + 4 * k)], (255, 85, 85), WIT, 1.0)


@held
def schelp(d, x, y, k=1.0, c=(255, 170, 170), rib=(255, 85, 170)):
    """Kamschelp: waaier met ribben, scharnier onderaan."""
    pts = [(x + 12 * k * math.cos(math.radians(a)), y - 2 * k + 10 * k * math.sin(math.radians(a))) for a in range(-180, 1, 15)]
    d.blob(pts + [(x + 3 * k, y + 5 * k), (x - 3 * k, y + 5 * k)], c, WIT, 1.2)
    for a in (-150, -120, -90, -60, -30):
        lijn(d, [(x, y + 3 * k), (x + 10 * k * math.cos(math.radians(a)), y - 2 * k + 8 * k * math.sin(math.radians(a)))], rib, max(1, .9 * k))


def kussen_rand(x0, y0, x1, y1, bol, n=8):
    """Rand van een kussen: vier spitse punten, de zijden bollen tussen de punten naar buiten."""
    hoeken = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]; pts = []
    for i in range(4):
        (ax, ay), (bx, by) = hoeken[i], hoeken[(i + 1) % 4]
        nx, ny = (by - ay), -(bx - ax); L = math.hypot(nx, ny); nx, ny = nx / L, ny / L
        for j in range(n):
            t = j / n; b = bol * math.sin(math.pi * t) ** .6
            pts.append((ax + (bx - ax) * t - nx * b, ay + (by - ay) * t - ny * b))
    return pts


@held
def kussen(d, f):
    """Echt kussen: bijna vierkant met vier punten, een naad rondom en een knoopje in het midden."""
    d.blob([f(*p) for p in kussen_rand(-1.25, -.05, 1.25, 1.15, .16)], WIT, BLAUW_L, 1.6)
    lijn(d, [f(*p) for p in kussen_rand(-1.0, .14, 1.0, .96, .1)] + [f(-1.0, .14)], (85, 170, 255), 1.0)
    p = f(0, .55); d.rondje(p[0], p[1], 1.8, 1.8, BLAUW_L)


@held
def slaapmuts(d, f, m):
    """Slappe slaapmuts: lichtblauw met een witte rand, punt hangt naar achteren, witte pompon."""
    d.blob([f(-1.08, -.32), f(-.86, -.86), f(-.45, -1.05), f(-.05, -.9), f(.18, -.62), f(.0, -.66), f(-.3, -.72), f(-.42, -.4)], BLAUW_L, WIT, 1.4)
    for dx, dy in ((-.78, -.7), (-.5, -.84), (-.2, -.82)):
        p = f(dx, dy); d.rondje(p[0], p[1], .045 * m, .045 * m, (255, 255, 170))
    d.blob([f(-1.14, -.28), f(-.42, -.36), f(-.4, -.5), f(-1.1, -.44)], WIT)
    p = f(.18, -.58); d.rondje(p[0], p[1], .11 * m, .11 * m, WIT, DONKER, dikte=1.0)


@held
def zzz(d, lijst):
    for x, y, s in lijst:
        pts = [(x - s, y - s), (x + s, y - s), (x - s, y + s), (x + s, y + s)]
        lijn(d, pts, DONKER, 4.4 * s / 6 + 1.6); lijn(d, pts, WIT, 2.4 * s / 6 + .6)


@held
def kelpdeken(d, x0, x1, y, dik):
    """Plukje kelp als deken: een golvend groen blad over zijn rug, kop vrij."""
    n = 14
    boven = [(x0 + (x1 - x0) * i / n, y - dik / 2 + 1.6 * math.sin(i * 1.3)) for i in range(n + 1)]
    onder_ = [(x0 + (x1 - x0) * i / n, y + dik / 2 + 1.8 * math.sin(i * 1.1 + 1)) for i in range(n, -1, -1)]
    d.blob(boven + onder_, GRAS, GRAS_L, 1.4)
    lijn(d, [(x0 + 4, y), (x1 - 4, y + 1)], (0, 85, 0), 1.0)


def bedschelp(d, cx, cy, k):
    """Open schelp als bedje (plek, staat stil): roze waaier met ribben."""
    pts = [(cx + 64 * k * math.cos(math.radians(a)), cy + 30 * k * math.sin(math.radians(a))) for a in range(0, 181, 12)]
    pts = [(cx - 66 * k, cy - 6 * k)] + [(cx + 66 * k, cy - 6 * k)] + pts
    d.blob(pts, (255, 170, 170), WIT, 1.6)
    for i in range(9):
        a = math.radians(20 + i * 17.5)
        lijn(d, [(cx, cy + 30 * k), (cx + 60 * k * math.cos(a), cy - 4 * k + 30 * k * math.sin(a) * .2)], (255, 85, 170), 1.4)
    d.blob([(cx - 66 * k, cy - 8 * k), (cx + 66 * k, cy - 8 * k), (cx + 66 * k, cy - 2 * k), (cx - 66 * k, cy - 2 * k)], (255, 85, 170), WIT, 1.2)


# ---------------- plekken ----------------
def zandvlakte(d, dd, zak=0, hx=124, ruggen=((60, 196, 90, 18), (210, 192, 80, 22))):
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in ruggen:
        d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-60 * s, (206 + zak) * s, 320 * s, 340 * s], fill=ZAND_DONKER)
    d.dr.ellipse([-50 * s, (210 + zak) * s, 310 * s, 340 * s], fill=ZAND if not d.am else (235, 225, 150))
    if d.am: d.gloed_ellips(hx, 230 + zak, 52, 10, WIT, .4)


def schaduw(d, x, y, rx):
    if d.am: d.gloed_ellips(x, y, rx, 4.5, (90, 80, 40), .45, groei=.25)
    else: d.rondje(x, y, rx * .95, 4, ZAND_DONKER)


def steentje(d, x, y, rx=5, ry=3, c=(170, 170, 255)):
    d.rondje(x, y, rx, ry, c, WIT, dikte=1.2)


def gaatje(d, x, y, rx=8, ry=3.2):
    d.rondje(x, y, rx + 1.4, ry + 1.2, ZAND_DONKER)
    d.rondje(x, y + .6, rx, ry, (85, 85, 0))


def zee_egel(d, x, y, r_=6):
    for i in range(12):
        a = math.radians(-180 + i * 16.4)
        lijn(d, [(x, y), (x + r_ * 1.7 * math.cos(a), y + r_ * 1.5 * math.sin(a))], (85, 0, 170), 1.4)
    d.rondje(x, y, r_, r_ * .8, (85, 0, 170), (170, 85, 255), dikte=1.2)


def kiezelbodem(d, dd, zak=0, hx=124):
    """Bodem van ronde kiezels (fles-wereld): grijsblauw met lichte keien, geen zand."""
    s = d.s
    verder = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else dd['mip_verder']
    for cx, cy, rx, ry in ((60, 196, 90, 18), (210, 192, 80, 22)):
        d.rondje(cx, cy + zak, rx, ry, verder)
    d.dr.ellipse([-60 * s, (206 + zak) * s, 320 * s, 340 * s], fill=(170, 170, 255) if not d.am else (150, 160, 220))
    d.dr.ellipse([-50 * s, (210 + zak) * s, 310 * s, 340 * s], fill=(85, 85, 170) if not d.am else (80, 90, 160))
    kl = [(170, 170, 255), (170, 170, 170), (255, 170, 170), (255, 255, 170), (170, 255, 255)]
    for i, (x, y, r_) in enumerate([(30, 222, 6), (46, 232, 4.5), (62, 222, 3.6), (40, 244, 5), (70, 240, 6.5), (98, 236, 4),
                                    (112, 246, 5.5), (150, 238, 4.5), (170, 248, 6), (190, 232, 5.5), (210, 222, 4.4),
                                    (222, 238, 6), (232, 226, 3.6), (196, 246, 3.8), (86, 250, 4.4), (136, 252, 4)]):
        d.rondje(x, y + zak, r_, r_ * .7, kl[i % 5], WIT, dikte=1.0)
    if d.am: d.gloed_ellips(hx, 230 + zak, 52, 10, WIT, .3)


def schim_kleur(d, nacht):
    return ((0, 30, 75) if not nacht else (0, 0, 40)) if d.am else ((0, 0, 85) if not nacht else (0, 0, 0))


def fles_ver(d, dd, nacht, x, y, k):
    """Een tweede, lege fles ver weg op de bodem: alleen een schim."""
    c = schim_kleur(d, nacht)
    f = R(x, y, -10, k)
    d.blob([f(*p) for p in fles_punten()], c)


def tuinalen(d, dd, nacht, zak=0):
    """Ver weg meer aaltjes die uit hun gaatje steken: donkere schimmen, links en rechts (niet achter tekst)."""
    c = schim_kleur(d, nacht)
    for x, h, b in [(22, 18, 1), (34, 24, -1), (46, 16, 1), (206, 20, -1), (220, 26, 1), (236, 16, -1)]:
        y0 = 200 + zak
        pts = [(x + b * 3 * math.sin(t * 2.2), y0 - h * t) for t in [i / 8 for i in range(9)]]
        lijn(d, pts, c, 3.6)
        hx_, hy_ = pts[-1]
        d.rondje(hx_ - b * 1.6, hy_, 2.6, 2.2, c)


def vlaggetjes(d, x0, y0, x1, y1, zakking):
    """Kermis: een lijn met vlaggetjes tussen twee ronde stenen."""
    for x, y in ((x0, y0), (x1, y1)):
        d.rondje(x, y + 6, 13, 10, (85, 85, 170), (170, 170, 255), glans=(170, 170, 255), dikte=1.6)
    kl = [(255, 0, 0), (255, 255, 0), (0, 170, 255), (255, 85, 170), (85, 255, 85)]
    n = 16; pts = []
    for i in range(n + 1):
        t = i / n; pts.append((x0 + (x1 - x0) * t, y0 - 4 + (y1 - y0) * t + zakking * 4 * t * (1 - t)))
    lijn(d, pts, WIT, 1.2)
    for i in range(1, n, 1):
        (ax, ay), (bx, by) = pts[i], pts[i + 1] if i + 1 <= n else pts[i]
        mx = (ax + bx) / 2
        d.blob([(ax + 1, ay), (bx - 1, by), (mx, (ay + by) / 2 + 8)], kl[i % 5], WIT, .9)


def plek_onder(d, dd, dier, zak=0, held_=True, nacht=False, eind=False):
    """Plek en held onder water; eind=True: alleen de plek (held wordt apart links getekend)."""
    hx = 124
    if dier == 'fish': kiezelbodem(d, dd, zak, hx)
    else: zandvlakte(d, dd, zak, hx)
    if dier == 'fish':
        fles_ver(d, dd, nacht, 44, 196 + zak, 9)
        if held_:
            schaduw(d, 120, 222 + zak, 58)
            fles_met_vis(d, 126, 190 + zak, 40, 34, -4)
            kurk(d, 196, 226 + zak, 6.6, 80)
    elif dier == 'octopus':
        steentje(d, 44, 226 + zak, 6, 3.6); steentje(d, 214, 232 + zak, 5, 3, (255, 170, 170))
        zee_egel(d, 60, 236 + zak, 4.4)
        if held_:
            cy = 204 + zak * .3
            schaduw(d, 128, cy + 34, 58)
            bad_met_octo(d, 128, cy, 42, -4, met_eend=False, op=.56)
    elif dier == 'eel':
        tuinalen(d, dd, nacht, zak)
        for x, y, rx in [(52, 226, 7), (206, 230, 7), (92, 240, 6), (164, 242, 5.5), (34, 216, 5), (226, 220, 5), (128, 232, 5)]:
            gaatje(d, x, y + zak, rx, rx * .4)
        steentje(d, 226, 214 + zak, 4, 2.6, (255, 170, 170))
        if held_:
            tx, ty = 172, 214 + zak
            gaatje(d, tx, ty, 11, 4.4)
            schaduw(d, 118, 216 + zak, 50)
            kantel(d, 122, 200 + zak, 46, EEL, -6)
            lampje(d, 90, 170 + zak, 1.0, 'uit', nacht)
            # zandlip voor het gaatje: zijn staart zit in het zand
            d.blob([(tx - 13, ty + .6), (tx + 13, ty + .6), (tx + 11, ty + 4), (tx - 11, ty + 4)], ZAND if not d.am else (235, 225, 150))
    elif dier == 'puffer':
        vlaggetjes(d, 52, 202 + zak, 210, 200 + zak, 16)
        if held_:
            sx, sy = 160, 228 + zak
            schaduw(d, 124, 222 + zak, 34)
            touwtje(d, [(122, 214 + zak), (128, 218 + zak), (138, 222 + zak), (150, 224 + zak), (sx, sy - 2)])
            schelp(d, sx, sy, 1.15)
            kantel(d, 122, 180 + zak, 40, PUFF, 0)
            knoopje(d, 122, 210 + zak, 1.0)
    elif dier == 'cucumber':
        steentje(d, 44, 226 + zak, 6, 3.6); steentje(d, 218, 230 + zak, 4.4, 2.8, (255, 170, 170))
        if not eind:
            bedschelp(d, 128, 212 + zak, .95)
        if held_:
            kantel(d, 124, 196 + zak, 40, CUKE, 0)
            kelpdeken(d, 128, 172, 200 + zak, 18)
            slaapmuts(d, R(124, 196 + zak, 0, 40), 40)
            zzz(d, [(168, 178 + zak, 3.4), (181, 170 + zak, 4.4), (196, 160 + zak, 5.4)])


# ---------------- boven water ----------------
def adem(D_, am, dd, nacht, dier, top=134, woord='breathe in', getal='12', onder='round 2 · 18 left', fase='in'):
    v32._KAP['y'] = 140
    d = Doek(D_, am)
    v3.lucht(d, dd, nacht, top)
    v3.zee(d, nacht, top)
    v3.volgende_vriend(d, nacht, top, x=74 if dier in ('puffer',) else 196)
    hoek = {'in': 8, 'calm': 3, 'uit': 0}[fase]
    dy = 0 if top < 140 else -4
    if dier == 'fish':
        hx = {'in': 190, 'calm': 180, 'uit': 134}[fase]; y = top + dy - 2; k = 30
        fles_met_vis(d, hx, y, k, 26, hoek, nacht, kurk_stand=fase)
        golfje(d, hx - 6, y + 12, 62, nacht)
    elif dier == 'octopus':
        hx = {'in': 180, 'calm': 176, 'uit': 130}[fase]; y = top + dy - 10; m = 30
        bad_met_octo(d, hx, y, m, hoek, 1.5, voeten=False)
        golfje(d, hx, y + 18, 46, nacht)
    elif dier == 'eel':
        hx = {'in': 190, 'calm': 180, 'uit': 134}[fase]; y = top + dy - 2; m = 36
        kantel(d, hx, y, m, EEL, hoek)
        golfje(d, hx, y + 9, 42, nacht)
        f = R(hx, y, hoek, m)
        lx, ly = f(-.28, -1.08)
        lampje(d, lx, ly, 1.2, {'in': 'aan', 'calm': 'half', 'uit': 'uit'}[fase], nacht)
    elif dier == 'puffer':
        hx = {'in': 192, 'calm': 180, 'uit': 134}[fase]; m = 28
        sprong = {'in': 26, 'calm': 18, 'uit': 12}[fase]
        y = top + dy - sprong - 12
        f = R(hx, y, hoek, m)
        bx, by = f(0, .86)
        wy = top + dy + 12
        touwtje(d, [(bx, by + 2), (bx + 3, by + (wy - by) * .35), (bx - 3, by + (wy - by) * .7), (bx + 1, wy)])
        golfje(d, bx, wy - 2, 9, nacht)
        kantel(d, hx, y, m, PUFF, hoek)
        knoopje(d, bx, by - 1, .9)
    elif dier == 'cucumber':
        hx = {'in': 180, 'calm': 176, 'uit': 130}[fase]; y = top + dy - 14; m = 28
        f = R(hx, y, hoek, m)
        kussen(d, R(hx, y + .32 * m, hoek, m))
        kantel(d, hx, y, m, CUKE, hoek)
        slaapmuts(d, f, m)
        golfje(d, hx, y + 34, 50, nacht)
        zzz(d, [f(.5, -1.05) + (3.4,), f(1.0, -1.4) + (4.6,), f(1.6, -1.75) + (5.8,)])
    v3.tekst_adem(d, top, woord, getal, onder)
    return d.klaar()


# ---------------- onder water ----------------
@held
def eend_oppervlak(d, x, y, k=1.3):
    """Het badeendje drijft boven aan het oppervlak: een witte golflijn onder hem."""
    pts = [(x - 16 + i * 2, y + 3 + 1.4 * math.sin(i * .9)) for i in range(17)]
    eend(d, x, y, k)
    lijn(d, pts, WIT, 1.6)


def hold(D_, am, dd, nacht, dier):
    v32._KAP['y'] = 139
    d = Doek(D_, am)
    v3.onder(d, dd, nacht, xo=126, xh=128)
    plek_onder(d, dd, dier, nacht=nacht)
    if dier == 'octopus': eend_oppervlak(d, 214, 92, 1.3)
    stofjes(d, dd)
    d.tekst(130, 24, 'hold', 24, GEEL)
    d.tekst(130, 48, 'press START to breathe', 14, WIT, False)
    d.tekst(130, 58, '1:45', 58, WIT)
    d.tekst(130, 117, '61 bpm · round 2', 18, WIT, False)
    return d.klaar()


def menu(D_, am, dd, nacht, dier):
    v32._KAP['y'] = 140
    d = Doek(D_, am)
    v3.onder(d, dd, nacht, xo=126, xh=128)
    plek_onder(d, dd, dier, zak=8, nacht=nacht)
    if dier == 'octopus': eend_oppervlak(d, 222, 72, 1.2)
    stofjes(d, dd); s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t in [(52, 'Rounds'), (86, 'Calm 4-7-8')]:
        fill = ((0, 30, 60) if dd is DAG else (0, 0, 50)) if am else (0, 0, 85)
        d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                               outline=WIT if t == 'Rounds' else (0, 170, 255), width=round(2.4 * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


VRIEND = {'fish': (D[1], 'Shrimp'), 'octopus': (D[10], 'Eel'), 'eel': (D[11], 'Ray'), 'puffer': (D[9], 'Octopus'), 'cucumber': (D[0], 'Fish')}


def held_eind(d, dier, nacht):
    if dier == 'fish':
        fles_met_vis(d, 82, 118, 24, 21, 4, nacht, kurk_stand=None); kurk(d, 108, 140, 4.6, 80)
    elif dier == 'octopus':
        bad_met_octo(d, 80, 118, 25, 0, 1.0)
    elif dier == 'eel':
        kantel(d, 84, 122, 30, EEL, 4); lampje(d, 70, 92, .9, 'uit', nacht)
    elif dier == 'puffer':
        kantel(d, 76, 104, 25, PUFF, 0); touwtje(d, [(76, 125), (80, 132), (88, 138), (94, 140)]); knoopje(d, 76, 124, .8); schelp(d, 98, 142, .8)
    elif dier == 'cucumber':
        bedschelp(d, 80, 132, .5); kantel(d, 78, 120, 28, CUKE, 0); kelpdeken(d, 82, 104, 124, 12)
        slaapmuts(d, R(78, 120, 0, 28), 28); zzz(d, [(98, 100, 2.8), (106, 92, 3.6)])


def eind(D_, am, dd, nacht, dier):
    v32._KAP['y'] = 72
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    v32.bundel(d, dd, nacht, xo=184, xh=184, yh=136)
    plek_onder(d, dd, dier, zak=14, held_=False, nacht=nacht, eind=True)
    vriend, naam = VRIEND[dier]
    stofjes(d, dd)
    for x, y, k in [(228, 76, 7), (236, 140, 5)]: fonkel(d, x, y, k)
    bx, by, brx, bry = 186, 108, 36, 32
    kring(d, dd, bx, by, 40)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 3.6, 3.6, WIT)
    d.dier(bx, by + 1, 28, vriend)
    hart = [(132 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 94 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 18, '3 rounds done', 27, GEEL)
    d.tekst(130, 46, '1:20   1:45   1:58', 22, WIT)
    held_eind(d, dier, nacht)
    d.tekst(130, 150, 'new friend', 18, WIT, False)
    d.tekst(130, 166, naam, 32 if len(naam) < 9 else 29, GEEL)
    stippen(d.dr, 130 * d.s, 212 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def scherm(naam, dier):
    if naam == 'in': return lambda D_, am, dd, n: adem(D_, am, dd, n, dier)
    if naam == 'uit': return lambda D_, am, dd, n: adem(D_, am, dd, n, dier, top=170, woord='breathe out', getal='9', fase='uit')
    if naam == 'calm': return lambda D_, am, dd, n: adem(D_, am, dd, n, dier, top=146, woord='breathe out', getal='5', onder='4-7-8 · 2 of 4', fase='calm')
    return lambda D_, am, dd, n: {'hold': hold, 'menu': menu, 'eind': eind}[naam](D_, am, dd, n, dier)


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']
DIEREN = ['fish', 'octopus', 'eel', 'puffer', 'cucumber']

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for dier in (sys.argv[2:] or DIEREN):
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
