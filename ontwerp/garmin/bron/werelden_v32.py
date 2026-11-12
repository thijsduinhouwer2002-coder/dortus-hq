# Blad werelden v3.2 (Mila, run 49, 12 nov): antwoord op de vier punten van Gijs (run 52, echte beelden krab v2.2).
#  (a) AMOLED overdag onder water: de bundel valt niet meer licht achter de bovenste tekst. Boven de onderste tekstregel
#      (plus 4) is de bundel EEN vaste tint 087898 (10 procent licht over 00698C): wit 5,1 en geel 4,9 op 1. Pas daaronder
#      de drie tinten zoals nu. Leest als een spot op de held: het licht wordt sterker waar het de held raakt.
#  (b) MIP nacht onder water: geen zwart meer. Bovenin raster 000055/0000AA, onder de golf vlak 000055,
#      verre ruggen 0000AA, nabije ruggen 5500AA (paars, los van de rotsen 5555AA).
#  (c) Cijfers: een eigen cijferletter op de maat van het blad (56/260), de held blijft waar hij is.
#  (d) Eindscherm: een indeling die past met de grotere systeemletter van de FR255
#      (kop en tijden tot y 70, "new friend" plus naam 46 hoog van y 150 tot 196, held en belletje ertussen).
# Leunt op werelden_v21 en werelden_v3; zelfde coordinaten in 1/260 D.   python3 werelden_v32.py <uitmap>
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
import werelden_v3 as v3
from werelden_v21 import Doek, DAG, NACHT, WIT, GEEL, ROZE, SLIP, D, bellen, fonkel, stofjes, kring, slipper, bandje
from blad_v9 import stippen
from PIL import Image, ImageDraw

# (b) nachtkleuren MIP onder water
NACHT['mip_water'] = [(0, 0, 85), (0, 0, 85)]
NACHT['mip_boven'] = (0, 0, 170)
NACHT['mip_verder'] = (0, 0, 170)
NACHT['mip_ver'] = (85, 0, 170)

BUNDEL_BOVEN = .10       # dekking van de ene tint boven de tekst (087898 over 00698C)
_KAP = {'y': 140}        # y onder de onderste tekstregel, per scherm gezet


def bundel(d, dd, nacht, xo=118, xh=112, yh=236):
    """(a) Bundel in twee delen: boven _KAP een tint, eronder drie tinten. MIP: geen bundel (zoals v2.2)."""
    if not d.am: return
    kap = _KAP['y']
    top_b, onder_b = 26, 96
    def vlak(k): return [d.P(xo - top_b * k, 0), d.P(xo + top_b * k, 0), d.P(xh + onder_b / 2 * k, yh), d.P(xh - onder_b / 2 * k, yh)]
    def boven(ld, v):
        ld.polygon(v, fill=255); ld.rectangle([0, kap * d.s, d.N, d.N], fill=0)
    def onder(ld, v):
        ld.polygon(v, fill=255); ld.rectangle([0, 0, d.N, kap * d.s], fill=0)
    d.tint(lambda ld: boven(ld, vlak(1.45)), dd['licht'], BUNDEL_BOVEN if not nacht else .07)
    totaal = .34 if not nacht else .22; a = 1 - (1 - totaal) ** (1 / 3)
    for k in (1.45, 1.2, .95):
        d.tint(lambda ld, k=k: onder(ld, vlak(k)), dd['licht'], a)


w.bundel = bundel
_hold_v3 = v3.hold


def hold(D_, am, dd, nacht, wereld):
    _KAP['y'] = 117 + 22      # onder "61 bpm · round 2"
    return _hold_v3(D_, am, dd, nacht, wereld)


def menu(D_, am, dd, nacht, wereld):
    _KAP['y'] = 140
    return v3.menu(D_, am, dd, nacht, wereld)


def eind(D_, am, dd, nacht, wereld='krab'):
    """(d) Eindscherm met ruimte voor de grotere systeemletter: kop en tijden tot y 70, held en belletje van y 74 tot 146,
    "new friend" en de naam van y 150 tot 196, stipjes op 210. Letters hier bewust op de FR255-maat (46 hoog voor de twee regels)."""
    _KAP['y'] = 72
    d = Doek(D_, am); w.water_onder(d, dd, nacht, stralen=0, raster_y=146)
    bundel(d, dd, nacht, xo=184, xh=184, yh=136)          # licht op de nieuwe vriend, stopt boven de naam
    if wereld == 'krab':
        w.wereld_onder(d, dd, held=False, zak=24, met_slipper=False, anem_dy=16, anem_dx=-10); naam = 'Shrimp'; vriend = D[1]
    elif wereld == 'schild':
        v3.wereld_schild(d, dd, held=False, zak=14); naam = 'Jellyfish'; vriend = v3.KWAL
    else:
        v3.wereld_clown(d, dd, held=False, zak=20, huis=False, takje=False); naam = 'Seahorse'; vriend = v3.PAARD
    stofjes(d, dd)
    for x, y, k in [(228, 76, 7), (236, 140, 5)]: fonkel(d, x, y, k)
    bx, by, brx, bry = 186, 108, 36, 32
    kring(d, dd, bx, by, 40)
    d.rondje(bx, by, brx, bry, (0, 85, 170), (0, 255, 255), dikte=2.4)
    d.rondje(bx - .62 * brx, by - .5 * bry, 3.6, 3.6, WIT)
    d.dier(bx, by + 1, 27 if vriend is v3.PAARD else 28, vriend)
    hart = [(132 + 6 * math.sin(t / 20 * 2 * math.pi) ** 3, 94 - (5 * math.cos(t / 20 * 2 * math.pi) - 2 * math.cos(2 * t / 20 * 2 * math.pi) - math.cos(3 * t / 20 * 2 * math.pi))) for t in range(20)]
    d.blob(hart, ROZE, WIT, 1.6)
    d.tekst(130, 18, '3 rounds done', 27, GEEL)
    d.tekst(130, 46, '1:20   1:45   1:58', 22, WIT)
    if wereld == 'krab':
        r = slipper(d, 72, 134, 1.1 * SLIP, hoek=-6)
        d.dier(78, 114, 31); bandje(d, r, 1.1 * SLIP)
    elif wereld == 'schild':
        v3.dier_kantel(d, 78, 116, 33, v3.SCHILD, 6); v3.blad_in_bek(d, 78 - .86 * 33, 114, .75)
    else:
        v3.anemoon(d, 86, 142, .7); v3.dier_kantel(d, 76, 112, 27, v3.CLOWN, 0); v3.clownshoed(d, 76, 112, 27)
        v3.anemoon(d, 102, 144, .7, voor=True); v3.jongleer(d, 64, 98, 18, .75, nacht)
    d.tekst(130, 150, 'new friend', 18, WIT, False)
    d.tekst(130, 166, naam, 32 if len(naam) < 9 else 29, GEEL)
    stippen(d.dr, 130 * d.s, 212 * d.s, 3, 1, max(2, round(3.5 * d.s)), round(13 * d.s))
    return d.klaar()


def adem_kap(naam, wereld):
    f = v3.scherm(naam, wereld)
    def g(D_, am, dd, n):
        _KAP['y'] = 140; return f(D_, am, dd, n)
    return g


def scherm(naam, wereld):
    if naam == 'hold': return lambda D_, am, dd, n: hold(D_, am, dd, n, wereld)
    if naam == 'menu': return lambda D_, am, dd, n: menu(D_, am, dd, n, wereld)
    if naam == 'eind': return lambda D_, am, dd, n: eind(D_, am, dd, n, wereld)
    return adem_kap(naam, wereld)


NAMEN = ['in', 'uit', 'calm', 'hold', 'menu', 'eind']

if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    welke = sys.argv[2:] or ['krab', 'schild', 'clown']
    for wereld in welke:
        rij = {}
        for nacht in (False, True):
            dd = NACHT if nacht else DAG
            for D_, am in ((454, True), (260, False)):
                for naam in NAMEN:
                    im = scherm(naam, wereld)(D_, am, dd, nacht)
                    im.save(os.path.join(uit, f'{wereld}-{naam}-{"nacht" if nacht else "dag"}-{D_}.png')); rij[(naam, nacht, D_)] = im
        for D_, k in ((454, 1), (260, 2), (260, 1)):
            g = 12 * k; W = D_ * k; n = len(NAMEN)
            ov = Image.new('RGB', (n * W + (n + 1) * g, 2 * W + 3 * g), (30, 30, 30))
            for j, nacht in enumerate((False, True)):
                for i, naam in enumerate(NAMEN):
                    ov.paste(rij[(naam, nacht, D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
            ov.save(os.path.join(uit, f'overzicht-{wereld}-{D_}-{k}x.png'))
