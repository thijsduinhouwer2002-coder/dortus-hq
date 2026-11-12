# Werelden v5: eigen lucht per familie (Mila, run 52, 12 nov). Punt 4 van de hoofdchat (05:15 NL):
# breathe in was bij alle 25 dezelfde lucht. Nu: elke familie een eigen luchtkleur en een luchtdetail, geen nieuw tekenwerk per dier.
# Alleen overdag op de ademschermen (in, uit, Calm). Nacht volgt de nachtregel (ebb-nachtregel-v1.json), onder water blijft gelijk.
# Gebruik: python3 werelden_v5_lucht.py <uitmap>
import sys, os, math, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w
import werelden_v3 as v3
from werelden_v21 import WIT, ZON, DAG
from PIL import Image

# MIP: boven (waar de tekst staat, wit haalt daar minstens 4,5) en band boven de horizon. AMOLED: drie stappen.
FAMILIE = {
    'krab':     dict(boven=(0, 85, 170), band=(0, 170, 255), am=[(0, 30, 95), (0, 75, 165), (0, 165, 250)], detail='geen'),
    'strand':   dict(boven=(0, 85, 255), band=(85, 170, 255), am=[(0, 40, 120), (0, 80, 210), (90, 180, 255)], detail='zeilboot', knik=.66),
    'vliegers': dict(boven=(0, 85, 170), band=(85, 170, 255), am=[(0, 35, 90), (0, 85, 170), (110, 185, 255)], detail='wind'),
    'huisjes':  dict(boven=(85, 0, 170), band=(255, 85, 85), am=[(40, 0, 90), (100, 20, 160), (255, 110, 90)], detail='avondzon'),
    'koud':     dict(boven=(0, 85, 170), band=(170, 255, 255), am=[(0, 40, 100), (0, 85, 160), (190, 245, 255)], detail='sneeuw', knik=.74),
    'licht':    dict(boven=(0, 0, 170), band=(255, 255, 170), am=[(10, 0, 80), (40, 20, 170), (255, 240, 160)], detail='stralen'),   # run 54: band licht geel in plaats van roze (roze kwal viel weg, hoofdchat 06:00 punt 3)
}
ORANJE, ROOD = (255, 170, 0), (255, 0, 0)


def zon(d, kleur=ZON, x=40, y=86, r=14):
    if d.am: d.gloed_ellips(x, y, r + 6, r + 6, (255, 255, 170), .35)
    d.rondje(x, y, r, r, kleur, WIT, glans=WIT, dikte=2)


def detail(d, soort, top):
    if soort == 'geen':
        zon(d)
    elif soort == 'zeilboot':          # zon, en een bootje met wit zeil ver op de horizon
        zon(d)
        hx, hy = 60, top - 3
        d.blob([(hx - 9, hy - 3), (hx + 9, hy - 3), (hx + 6, hy + 1), (hx - 6, hy + 1)], ROOD, WIT, 1)
        d.blob([(hx - 1, hy - 4), (hx - 1, hy - 20), (hx + 9, hy - 5)], WIT)
        d.blob([(hx - 3, hy - 4), (hx - 3, hy - 15), (hx - 9, hy - 5)], (255, 255, 170))
    elif soort == 'wind':              # zon en drie witte windkrullen
        zon(d)
        for x0, y0, L in [(14, 120, 22), (64, 124, 20)]:
            pts = [(x0 + t, y0 + 2.2 * math.sin(t / L * 2 * math.pi)) for t in range(0, L + 1, 2)]
            d.dr.line([d.P(*p) for p in pts], fill=WIT, width=max(1, round(1.5 * d.s)))
            a = math.radians(0)
            ex, ey = pts[-1]
            for k in range(10):    # krulletje aan het eind
                t = k / 9 * 1.6 * math.pi
                d.rondje(ex + 3.5 * math.sin(t), ey - 3.5 + 3.5 * math.cos(t), .75, .75, WIT)
    elif soort == 'avondzon':          # grote oranje zon half in de zee
        x, y, r = 46, top - 6, 18
        if d.am: d.gloed_ellips(x, y, r + 8, r + 8, (255, 200, 120), .4)
        d.rondje(x, y, r, r, ORANJE, (255, 255, 85), dikte=2)
        for dy in (-9, -2):
            d.dr.rectangle([d.P(x - r - 3, y + dy), d.P(x + r + 3, y + dy + 1.6)], fill=FAMILIE['huisjes']['band'])
    elif soort == 'sneeuw':            # bleke kleine zon en sneeuwvlokjes
        zon(d, (255, 255, 170), r=11)
        for x, y in [(22, 62), (238, 60), (28, 116), (66, 110), (232, 112), (196, 102)]:
            for a in (0, 60, 120):
                t = math.radians(a)
                d.dr.line([d.P(x - 4 * math.cos(t), y - 4 * math.sin(t)), d.P(x + 4 * math.cos(t), y + 4 * math.sin(t))], fill=WIT, width=max(1, round(1.5 * d.s)))
    elif soort == 'stralen':           # zon met acht gele stralen
        x, y, r = 40, 86, 12
        for k in range(8):
            t = math.radians(k * 45)
            p = [(x + (r + 4) * math.cos(t - .18), y + (r + 4) * math.sin(t - .18)),
                 (x + (r + 12) * math.cos(t), y + (r + 12) * math.sin(t)),
                 (x + (r + 4) * math.cos(t + .18), y + (r + 4) * math.sin(t + .18))]
            d.blob(p, ZON)
        zon(d, r=r)


def maak_lucht(fam):
    F = FAMILIE[fam]
    oud = v3.lucht

    def lucht(d, dd, nacht, top):
        if nacht:
            return oud(d, dd, nacht, top)
        if d.am:
            a, b, c = F['am']
            k = F.get('knik', .55)
            d.verloop(0, top * k, a, b); d.verloop(top * k, top, b, c)
        else:
            d.verloop(0, top, F['boven'], F['band'], [(top - 28, F['band'])])
        detail(d, F['detail'], top)
    return lucht, oud


DIEREN = {'strand': ['shrimp', 'starfish', 'lobster', 'seal', 'otter'], 'vliegers': ['ray', 'manta', 'dolphin', 'swordfish'],
          'huisjes': ['fish', 'octopus', 'eel', 'puffer', 'cucumber'], 'koud': ['whale', 'orca', 'narwhal', 'squid'],
          'licht': ['jelly', 'seahorse', 'sunfish', 'shark']}
ADEM = ['in', 'uit', 'calm']


def beelden(uit):
    os.makedirs(uit, exist_ok=True)
    alles = {}
    for fam, dieren in DIEREN.items():
        mod = importlib.import_module(f'werelden_v4_{fam}')
        nieuw, oud = maak_lucht(fam)
        v3.lucht = nieuw
        try:
            for dier in dieren:
                for naam in ADEM:
                    for D_, am in ((454, True), (260, False)):
                        im = mod.scherm(naam, dier)(D_, am, DAG, False)
                        im.save(os.path.join(uit, f'{dier}-{naam}-dag-{D_}.png')); alles[(dier, naam, D_)] = im
        finally:
            v3.lucht = oud
    return alles


if __name__ == '__main__':
    uit = sys.argv[1]
    alles = beelden(uit)
    # eenheidsblad breathe in, families onder elkaar
    for D_, k in ((260, 1), (454, 1)):
        W = D_ * k; g = 8
        rijen = list(DIEREN.items())
        ov = Image.new('RGB', (5 * W + 6 * g, len(rijen) * W + (len(rijen) + 1) * g), (30, 30, 30))
        for j, (fam, dieren) in enumerate(rijen):
            for i, dier in enumerate(dieren):
                ov.paste(alles[(dier, 'in', D_)].resize((W, W), Image.NEAREST), (g + i * (W + g), g + j * (W + g)))
        ov.save(os.path.join(uit, f'eenheid-families-in-dag-{D_}-{k}x.png'))
