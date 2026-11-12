# Onderwaterachtergrond voor startscherm, pauze en sea log (Mila, run 53, 12 nov). Opdracht hoofdchat 05:15 NL.
# Een "thuis" onder water dat bij alle werelden past: zelfde water, oppervlak en stofjes als hold, maar een lage, rustige
# bodem zonder held (de tekst en keuzes hebben de ruimte), met het eigen dier klein onderin als vaste gast.
# Pauze: het water staat stil (geen lichtbundel, de belletjes hangen stil op één hoogte): "the sea waits".
# Nacht: zelfde scherm door de nachtregel (ebb-nachtregel-v1.json).   python3 onderwater_v1.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import krab_keuring2 as K
import werelden_v21 as w
import horloge_sim as h
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL
from blad_v13 import kader
from PIL import Image, ImageDraw, ImageChops

ZAND, ZAND_D = (255, 255, 170), (170, 170, 85)
RUG_DAG, RUG_NACHT = (0, 85, 170), (0, 0, 170)
KELP, KELP_L = (0, 170, 85), (85, 255, 170)


def bodem(d, dd, y=214, nacht=False):
    """Lage bodem: twee verre ruggen, een zandrand met twee kiezels, links en rechts een pluk kelp."""
    ver = tuple((a + b) // 2 for a, b in zip(dd['ver'], dd['zee_top'])) if d.am else (dd['mip_verder'])
    for cx, cy, rx, ry in [(30, y + 4, 70, 22), (230, y, 64, 26)]:
        d.rondje(cx, cy, rx, ry, ver)
    d.golf(y + 10, 262, (85, 85, 170) if nacht else ZAND, 2, 2, .6)   # bij nacht koel blauwgrijs zand, dan de nachtregel
    d.dr.line([d.P(x, y + 10 + 2 * math.sin(x / 260 * 2 * math.pi * 2 + .6)) for x in range(0, 261, 2)], fill=WIT, width=max(1, round(1.2 * d.s)))
    for x, yy, r in [(96, y + 22, 3.5), (168, y + 20, 2.6)]:
        d.rondje(x, yy, r * 1.3, r, ZAND_D, WIT, dikte=1)
    for x0, kant in [(32, 1), (230, -1)]:
        for i, (dx, L) in enumerate([(0, 46), (8, 34), (-7, 28)]):
            pts = [(x0 + dx + kant * 5 * math.sin(t / 10), y + 12 - t) for t in range(0, L, 3)]
            for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
                d.dr.line([d.P(xa, ya), d.P(xb, yb)], fill=KELP, width=max(2, round(4 * d.s)))
            xb, yb = pts[-1]; d.rondje(xb, yb, 2.4, 2.4, KELP_L)


def achtergrond(d, dd, nacht, stil=False, bodem_y=214):
    w.water_onder(d, dd, nacht, stralen=0, raster_y=146)   # geen lichtbundel: achter menu en tekst haalde geel daar maar 4,27
    bodem(d, dd, bodem_y, nacht)
    if stil:   # pauze: belletjes hangen stil op een rij
        w.bellen(d, [(34, 150, 3), (48, 150, 2), (212, 150, 2.4), (226, 150, 3.2)], (170, 255, 255))
    else:
        w.stofjes(d, dd)


def dier_klein(d, nr, cx, cy, maat, spiegel=False):
    d.dier(cx, cy, maat, w.D[nr])


def start(D_, am, dd, nacht, nr=3):
    """Startscherm (eerste keer, of als er nog geen wereld is): menu op het thuiswater, eigen dier onderin midden."""
    d = Doek(D_, am); achtergrond(d, dd, nacht); s = d.s
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for y, t, gekozen in [(52, 'Rounds', True), (86, 'Calm 4-7-8', False)]:
        fill = ((0, 30, 60) if dd is DAG else (0, 0, 50)) if am else (0, 0, 85)
        d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                               outline=WIT if gekozen else (0, 170, 255), width=round((3.2 if gekozen else 2) * s))
        d.tekst(130, y + 2, t, 20, WIT)
    d.tekst(130, 120, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    dier_klein(d, nr, 130, 196, 30)
    w.bellen(d, [(150, 172, 2.2), (156, 162, 1.6)], (170, 255, 255))
    return d.klaar()


def pauze(D_, am, dd, nacht, keuze=0, nr=3):
    """Pauzemenu v10 op het thuiswater: water staat stil, gekozen regel in een pil van schuim, eigen dier wijst aan."""
    d = Doek(D_, am); achtergrond(d, dd, nacht, stil=True, bodem_y=226); s = d.s
    d.tekst(130, 16, 'paused', 26, (85, 170, 255) if nacht else (0, 255, 255))
    d.tekst(130, 46, 'round 2 · 1:12', 17, WIT, False)
    for i, (y, t) in enumerate([(98, 'Resume'), (134, 'Save'), (170, 'Discard')]):
        if i == keuze:
            d.dr.rounded_rectangle([75 * s, (y - 2) * s, 185 * s, (y + 30) * s], radius=16 * s, fill=(0, 255, 255))
            d.tekst(130, y, t, 24, (0, 0, 85))
            dier_klein(d, nr, 58, y + 14, 18)
        else:
            d.tekst(130, y, t, 24, WIT)
    d.tekst(130, 204, 'the sea waits', 15, (85, 170, 255) if nacht else (0, 255, 255), False)
    return d.klaar()


def sealog(D_, am, dd, nacht, gevonden=(0, 1, 2, 4, 5, 6, 7, 9), pagina=0, kies=1):
    """Sea log: 2 rijen van 3 belletjes op het thuiswater. Gevonden: het dier; nog niet: een schaduw."""
    d = Doek(D_, am); achtergrond(d, dd, nacht, bodem_y=222); s = d.s
    d.tekst(130, 16, 'sea log', 24, GEEL)
    d.tekst(130, 42, f'{len(gevonden)} of 24', 16, WIT, False)
    for i in range(6):
        nr = pagina * 6 + i
        cx, cy = 76 + (i % 3) * 54, 92 + (i // 3) * 58
        r = 23
        rand = WIT if i == kies else (0, 170, 255)
        d.rondje(cx, cy, r + (2.6 if i == kies else 1.6), r + (2.6 if i == kies else 1.6), rand)
        d.rondje(cx, cy, r, r, (0, 30, 60) if am and dd is DAG else ((0, 0, 50) if am else (0, 0, 85)))
        d.rondje(cx - .62 * r, cy - .5 * r, 3, 3, WIT)
        if nr in gevonden:
            d.dier(cx, cy + 1, 23, w.D[nr])
        else:
            m = round(23 * d.D / 260); wie = w.D[nr]
            _, _, ox, oy = kader(wie, m)
            lag = Image.new('RGB', (d.D, d.D), (1, 2, 3)); ld = ImageDraw.Draw(lag)
            h.silhouet(ld, wie, round(cx * d.D / 260 - ox), round((cy + 1) * d.D / 260 - oy), m)
            mk = ImageChops.difference(lag, Image.new('RGB', (d.D, d.D), (1, 2, 3))).convert('L').point(lambda v: 255 if v else 0)
            d.im.paste(lag.resize((d.N, d.N), Image.NEAREST), (0, 0), mk.resize((d.N, d.N), Image.NEAREST))
    naam = w.D[pagina * 6 + kies]['naam'] if 'naam' in w.D[pagina * 6 + kies] else ''
    d.tekst(130, 182, naam if (pagina * 6 + kies) in gevonden else '?', 18, WIT)
    for k in range(4):
        d.rondje(112 + k * 12, 210, 2.6, 2.6, (0, 255, 255) if k == pagina else (0, 0, 85), (0, 255, 255), dikte=1)
    return d.klaar()


SCHERMEN = [('start', start), ('pauze', pauze), ('sealog', sealog)]
VOORBEELDEN = [(f'{n}-{"nacht" if nacht else "dag"}', (lambda fn, nacht: (lambda D_, am: fn(D_, am, NACHT if nacht else DAG, nacht)))(fn, nacht), nacht)
               for n, fn in SCHERMEN for nacht in (False, True)]


def met_nacht(fn, am):
    a = fn(); b = K.zonder_tekst(fn)
    oud = w.tekst
    w.tekst = lambda dr, x, y, t, font, c: oud(dr, x, y, t, font, (255, 0, 255))
    try: sleutel = fn()
    finally: w.tekst = oud
    return K.nachtregel_masker(a, b, sleutel, am)


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    for D_, am in ((260, False), (454, True)):
        K.OMTREK['modus'] = 'wit' if am else 'donker1'
        rij = {}
        for nacht in (False, True):
            dd = NACHT if nacht else DAG
            for naam, fn in SCHERMEN:
                f = lambda: fn(D_, am, dd, nacht)
                im = met_nacht(f, am) if nacht else f()
                im.save(os.path.join(uit, f'{naam}-{"nacht" if nacht else "dag"}-{D_}.png')); rij[(naam, nacht)] = im
        k = 2 if D_ == 260 else 1; W = D_ * k; g = 10
        ov = Image.new('RGB', (3 * (W + g) + g, 2 * (W + g) + g), (30, 30, 30))
        for j, nacht in enumerate((False, True)):
            for i, (naam, _) in enumerate(SCHERMEN):
                ov.paste(rij[(naam, nacht)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
        ov.save(os.path.join(uit, f'overzicht-onderwater-{D_}-{k}x.png'))
