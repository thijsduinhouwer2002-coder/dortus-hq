# Ebb dieren v4 (Mila, 10 nov run 21): zes nieuwe zeedieren in dezelfde stijl als v3
# (gevulde vlakken, lijf / licht / donker in MIP-kleuren, hetzelfde oog), plus het blad met alle tien.
# Gebruik: python3 ebb_dieren_v4.py <uitmap> <font>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
from ebb_blad_v3 import bez, ellips, leeg, rand, zee, W1, W2, W3, SCHUIM, GRIJS, WIT, teken, niet_mip
from PIL import Image, ImageDraw

v3.TINT.update({
    'krab':   ((255,85,0),   (255,170,85),  (170,0,0)),
    'paard':  ((255,170,0),  (255,255,85),  (170,85,0)),
    'octo':   ((170,85,255), (255,170,255), (85,0,170)),
    'ster':   ((255,170,85), (255,255,170), (255,85,0)),
    'kogel':  ((255,255,85), (255,255,170), (170,170,0)),
    'komkom': ((170,85,85),  (255,170,170), (85,0,0)),
    'clown':  ((255,85,0),   (255,255,255), (0,0,0)),
    'rog':    ((85,170,170), (170,255,255), (0,85,85)),
    'dolfijn':((85,170,255), (170,255,255), (0,85,170)),
    'zeehond':((170,170,170),(255,255,255), (85,85,85)),
    'inktvis':((255,170,255),(255,255,255), (170,85,170)),
    'kreeft': ((170,0,0),    (255,85,85),   (85,0,0)),
    'otter':  ((170,85,0),   (255,170,85),  (85,0,0)),
    'garnaal':((255,170,170),(255,255,255), (255,85,85)),
    'maanvis':((170,170,255),(255,255,255), (85,85,170)),
    'haai':   ((85,85,170),  (255,255,255), (0,0,85)),
    'zwaard': ((85,85,255),  (255,255,255), (0,0,85)),
    'manta':  ((85,85,85),   (255,255,255), (0,0,0)),
    'orka':   ((0,0,0),      (255,255,255), (85,85,85)),
    'narwal': ((170,170,255),(255,255,255), (85,85,170)),
    'reuzeninkt': ((170,0,85), (255,85,170), (85,0,0)),
})
_oud = v3.dier_delen

def poot(x0, y0, x1, y1, x2, y2, b):
    """Dikke gebogen poot: bezier-as met breedte b, rond eind."""
    as_ = bez((x0,y0),(x1,y1),(x2,y2),10); l, r = [], []
    for i in range(len(as_)):
        a, c = as_[max(0,i-1)], as_[min(len(as_)-1,i+1)]
        dx, dy = c[0]-a[0], c[1]-a[1]; n = math.hypot(dx, dy) or 1
        w = b*(1-0.35*i/(len(as_)-1))
        l.append((as_[i][0]-dy/n*w/2, as_[i][1]+dx/n*w/2)); r.append((as_[i][0]+dy/n*w/2, as_[i][1]-dx/n*w/2))
    return l + r[::-1]

def nieuwe_delen(soort):
    if soort == 'krab':
        lijf = ellips(0, 0.12, 0.70, 0.42)
        buik = ellips(0, 0.22, 0.52, 0.22, 0, 180)
        poten = []
        for k in (-1, 1):
            for j, dy in enumerate((0.10, 0.25, 0.38)):
                poten.append((poot(k*0.55, dy, k*0.90, dy-0.05, k*1.0, dy+0.30, 0.09), 'donker'))
        scharen = []
        for k in (-1, 1):
            arm = poot(k*0.45, -0.10, k*0.70, -0.40, k*0.72, -0.62, 0.12)
            schaar = ellips(k*0.74, -0.78, 0.24, 0.20)
            kerf = [(k*0.74, -0.80), (k*0.66, -1.02), (k*0.86, -1.00)]
            scharen += [(arm, 'lijf'), (schaar, 'lijf'), (kerf, 'zwart')]
        steel = [(-0.30,-0.18),(-0.22,-0.18),(-0.22,-0.42),(-0.30,-0.42), (0.22,-0.18),(0.30,-0.18),(0.30,-0.42),(0.22,-0.42)]
        return poten + scharen + [(steel[:4],'lijf'), (steel[4:],'lijf'), (lijf,'lijf'), (buik,'licht')], [(-0.26,-0.46), (0.26,-0.46)]
    if soort == 'paard':
        # zeepaardje rechtop: kop met snuit links, buik rond, staart krult rechtsonder
        kop = ellips(0.05, -0.62, 0.26, 0.24)
        snuit = [(-0.12,-0.70),(-0.52,-0.66),(-0.54,-0.56),(-0.12,-0.52)]
        lijf = bez((0.25,-0.50),(0.55,-0.05),(0.20,0.35),10) + bez((0.20,0.35),(0.0,0.55),(0.10,0.75),6) \
             + bez((0.10,0.75),(0.40,1.0),(0.42,0.75),6) + bez((0.42,0.75),(0.40,0.62),(0.25,0.66),4) \
             + bez((0.25,0.66),(-0.15,0.40),(-0.25,0.05),8) + bez((-0.25,0.05),(-0.25,-0.35),(-0.10,-0.48),6)
        buik = bez((-0.20,0.0),(-0.22,0.30),(0.05,0.42),6) + bez((0.05,0.42),(0.02,0.10),(-0.05,-0.30),6)
        kam = [(0.18,-0.84),(0.26,-0.98),(0.32,-0.80),(0.42,-0.90),(0.40,-0.66)]
        vin = [(0.34,-0.10),(0.62,-0.02),(0.58,0.18),(0.30,0.14)]
        return [(vin,'licht'), (lijf,'lijf'), (buik,'licht'), (kam,'donker'), (snuit,'lijf'), (kop,'lijf')], [(-0.02,-0.66)]
    if soort == 'octo':
        kop = ellips(0, -0.22, 0.62, 0.60, 180, 360, 40) + [(0.62,-0.22),(0.58,0.05),(-0.58,0.05),(-0.62,-0.22)]
        armen = []
        for k, (x0, x2) in enumerate(((-0.50,-0.95),(-0.18,-0.40),(0.18,0.40),(0.50,0.95))):
            armen.append((poot(x0, 0.0, x0*1.1, 0.55, x2, 0.62 + 0.12*(k in (1,2)), 0.22), 'lijf'))
        vlekken = [(ellips(-0.28,-0.52,0.09,0.07),'licht'), (ellips(0.30,-0.56,0.07,0.06),'licht'), (ellips(0.05,-0.70,0.06,0.05),'licht')]
        mond = ellips(0, 0.04, 0.10, 0.06)
        return armen + [(kop,'lijf')] + vlekken + [(mond,'donker')], [(-0.24,-0.22), (0.24,-0.22)]
    if soort == 'ster':
        pts = []; pi = []
        for i in range(10):
            a = math.radians(-90 + i*36); r = 0.95 if i % 2 == 0 else 0.42
            pts.append((r*math.cos(a), 0.05 + r*math.sin(a)))
            pi.append((r*0.55*math.cos(a), 0.05 + r*0.55*math.sin(a)))
        stip = [(ellips(0.60*math.cos(math.radians(-90+i*72)), 0.05+0.60*math.sin(math.radians(-90+i*72)), 0.06, 0.06), 'donker') for i in range(5)]
        return [(pts,'lijf'), (pi,'licht')] + stip, [(-0.17,-0.02), (0.17,-0.02)]
    if soort == 'kogel':
        stekels = []
        for i in range(14):
            a = math.radians(i*360/14 + 8); b = 0.10
            stekels.append(([(0.62*math.cos(a-b), 0.62*math.sin(a-b)), (0.92*math.cos(a), 0.92*math.sin(a)), (0.62*math.cos(a+b), 0.62*math.sin(a+b))], 'donker'))
        lijf = ellips(0, 0, 0.72, 0.70)
        buik = ellips(0, 0.05, 0.62, 0.55, 15, 165)
        staart = [(0.66,0),(0.98,-0.24),(0.94,0.24)]
        mond = ellips(-0.70, 0.12, 0.08, 0.07)
        return [(staart,'donker')] + stekels + [(lijf,'lijf'), (buik,'licht'), (mond,'donker')], [(-0.34,-0.18)]
    if soort == 'komkom':
        # zeekomkommer: lang en zacht, met bobbels, slaperige ogen (de grap: komt terug na een pauze)
        lijf = ellips(0, 0.05, 0.98, 0.36)
        buik = ellips(0, 0.12, 0.88, 0.22, 0, 180)
        bobbels = [(ellips(x, -0.26 + 0.04*abs(x), 0.09, 0.07), 'donker') for x in (-0.50, -0.20, 0.10, 0.40, 0.66)]
        voeljes = [(ellips(-0.98 + 0.06*k, -0.10 - 0.10*k, 0.06, 0.06), 'licht') for k in range(3)]
        return [(lijf,'lijf'), (buik,'licht')] + bobbels + voeljes, [(-0.66,-0.04)]
    if soort == 'clown':
        lijf = ellips(-0.18, 0, 0.74, 0.48)
        staart = [(0.40,0),(0.92,-0.40),(0.82,0),(0.92,0.40)]
        banden = []
        for xc, w in ((-0.52, 0.10), (-0.08, 0.12), (0.36, 0.08)):
            pts = [(x, y) for x, y in ellips(-0.18, 0, 0.74, 0.48, 0, 360, 60) if abs(x - xc) <= w]
            band = sorted([p for p in pts if p[1] < 0], key=lambda q: q[0]) + sorted([p for p in pts if p[1] >= 0], key=lambda q: -q[0])
            banden.append((band, 'licht'))
        vin = bez((-0.40,-0.40),(-0.05,-0.75),(0.25,-0.38),6)
        return [(staart,'lijf'), (vin,'lijf'), (lijf,'lijf')] + banden, [(-0.66,-0.10)]
    if soort == 'rog':
        lijf = bez((-0.95,0.05),(-0.45,-0.55),(0.0,-0.30),8) + bez((0.0,-0.30),(0.45,-0.55),(0.95,0.05),8) \
             + bez((0.95,0.05),(0.40,0.20),(0.10,0.40),6) + bez((-0.10,0.40),(-0.40,0.20),(-0.95,0.05),6)
        staart = [(-0.04,0.36),(0.04,0.36),(0.02,1.0),(-0.02,1.0)]
        buik = ellips(0, 0.05, 0.40, 0.20, 0, 180)
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht')], [(-0.18,-0.12), (0.18,-0.12)]
    if soort == 'dolfijn':
        lijf = bez((-1.0,0.02),(-0.55,-0.42),(0.35,-0.30),10) + bez((0.35,-0.30),(0.70,-0.18),(0.82,-0.05),6) \
             + bez((0.82,-0.05),(0.60,0.22),(0.10,0.25),6) + bez((0.10,0.25),(-0.50,0.25),(-1.0,0.10),8)
        buik = bez((-0.95,0.10),(-0.40,0.0),(0.30,0.16),6) + bez((0.30,0.16),(-0.40,0.27),(-0.95,0.12),6)
        vin = [(-0.10,-0.34),(0.12,-0.68),(0.22,-0.30)]
        staart = [(0.78,-0.08),(1.05,-0.34),(1.0,-0.04),(1.08,0.22)]
        flip = [(-0.30,0.18),(-0.10,0.48),(0.0,0.20)]
        return [(staart,'lijf'), (vin,'donker'), (flip,'donker'), (lijf,'lijf'), (buik,'licht')], [(-0.58,-0.12)]
    if soort == 'zeehond':
        lijf = bez((-0.80,-0.10),(-0.70,-0.55),(-0.30,-0.40),8) + bez((-0.30,-0.40),(0.40,-0.10),(0.95,0.20),8) \
             + bez((0.95,0.20),(0.40,0.45),(-0.30,0.35),8) + bez((-0.30,0.35),(-0.85,0.25),(-0.80,-0.10),6)
        buik = ellips(-0.10, 0.25, 0.50, 0.12)
        flip = [(-0.20,0.30),(0.05,0.62),(0.12,0.30)]
        staart = [(0.85,0.18),(1.05,0.0),(1.05,0.38)]
        neus = ellips(-0.86, -0.10, 0.06, 0.05)
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht'), (flip,'donker'), (neus,'donker')], [(-0.58,-0.24)]
    if soort == 'inktvis':
        kap = [(0,-1.0),(0.30,-0.60),(0.34,0.10),(-0.34,0.10),(-0.30,-0.60)]
        vinnen = [(-0.30,-0.70),(-0.55,-0.55),(-0.32,-0.40)], [(0.30,-0.70),(0.55,-0.55),(0.32,-0.40)]
        armen = [(poot(x, 0.05, x*1.2, 0.45, x*1.6, 0.85, 0.11), 'lijf') for x in (-0.25, -0.08, 0.08, 0.25)]
        glans = ellips(-0.12, -0.50, 0.06, 0.16)
        return armen + [(vinnen[0],'donker'), (vinnen[1],'donker'), (kap,'lijf'), (glans,'licht')], [(-0.13,-0.10), (0.13,-0.10)]
    if soort == 'kreeft':
        lijf = ellips(0, 0.05, 0.30, 0.55)
        staart = [(-0.20,0.50),(0.20,0.50),(0.30,0.95),(0,0.85),(-0.30,0.95)]
        ringen = [([(-0.28,y),(0.28,y),(0.28,y+0.04),(-0.28,y+0.04)],'donker') for y in (0.15, 0.32)]
        scharen = []
        for k in (-1, 1):
            scharen.append((poot(k*0.22, -0.30, k*0.55, -0.40, k*0.55, -0.70, 0.12), 'lijf'))
            scharen.append((ellips(k*0.58, -0.82, 0.22, 0.18), 'licht'))
            scharen.append(([(k*0.56,-0.84),(k*0.46,-1.04),(k*0.66,-1.02)], 'zwart'))
        voel = [(poot(k*0.08, -0.45, k*0.30, -0.90, k*0.15, -1.10, 0.04), 'donker') for k in (-1, 1)]
        return voel + scharen + [(staart,'lijf'), (lijf,'lijf')] + ringen, [(-0.13,-0.30), (0.13,-0.30)]
    if soort == 'otter':
        # zeeotter op de rug, pootjes op de buik (houdt een schelp vast)
        lijf = ellips(0.05, 0.10, 0.88, 0.34)
        buik = ellips(0.05, 0.02, 0.70, 0.16, 180, 360)
        kop = ellips(-0.72, -0.12, 0.30, 0.28)
        snuit = ellips(-0.84, -0.04, 0.14, 0.10)
        schelp = ellips(-0.22, -0.28, 0.14, 0.10)
        pootjes = [ellips(-0.32, -0.22, 0.07, 0.06), ellips(-0.10, -0.22, 0.07, 0.06)]
        staart = [(0.85,0.0),(1.08,-0.10),(1.05,0.10),(0.85,0.22)]
        neus = ellips(-0.97, -0.08, 0.06, 0.05)
        return [(staart,'donker'), (lijf,'lijf'), (kop,'licht'), (neus,'donker'), (schelp,'licht'),
                (pootjes[0],'donker'), (pootjes[1],'donker')], [(-0.74,-0.20)]
    if soort == 'garnaal':
        lijf = bez((-0.70,-0.10),(-0.20,-0.55),(0.50,-0.20),10) + bez((0.50,-0.20),(0.80,0.10),(0.55,0.45),6) \
             + bez((0.55,0.45),(0.35,0.20),(0.20,0.10),4) + bez((0.20,0.10),(-0.30,0.15),(-0.70,0.10),8)
        segs = [([(x,-0.38+abs(x)*0.3),(x+0.05,-0.38+abs(x)*0.3),(x+0.05,0.12),(x,0.12)],'donker') for x in (-0.15, 0.10, 0.32)]
        staart = [(0.55,0.40),(0.85,0.55),(0.40,0.65)]
        voel = [(poot(-0.65,-0.10,-0.95,-0.60,-0.60,-0.95,0.035),'donker'), (poot(-0.60,-0.05,-1.0,-0.30,-1.05,-0.70,0.035),'donker')]
        pootjes = [(poot(x,0.10,x-0.05,0.30,x-0.12,0.42,0.05),'donker') for x in (-0.40,-0.20,0.0)]
        return voel + pootjes + [(staart,'lijf'), (lijf,'lijf')] + segs, [(-0.48,-0.18)]
    if soort == 'maanvis':
        lijf = ellips(0, 0, 0.62, 0.62)
        vin_b = [(0.05,-0.55),(0.28,-1.0),(0.42,-0.50)]; vin_o = [(0.05,0.55),(0.28,1.0),(0.42,0.50)]
        staart = [(0.55,-0.40),(0.78,-0.30),(0.78,0.30),(0.55,0.40)]
        buik = ellips(0, 0.10, 0.50, 0.42, 20, 160)
        mond = ellips(-0.60, 0.05, 0.06, 0.05)
        return [(vin_b,'donker'), (vin_o,'donker'), (staart,'donker'), (lijf,'lijf'), (buik,'licht'), (mond,'donker')], [(-0.30,-0.15)]
    if soort == 'haai':
        lijf = bez((-1.0,0.05),(-0.60,-0.40),(0.30,-0.25),10) + bez((0.30,-0.25),(0.65,-0.15),(0.80,-0.02),6) \
             + bez((0.80,-0.02),(0.50,0.25),(0.0,0.25),6) + bez((0.0,0.25),(-0.60,0.25),(-1.0,0.05),8)
        buik = bez((-0.95,0.08),(-0.40,0.02),(0.30,0.15),6) + bez((0.30,0.15),(-0.40,0.27),(-0.95,0.10),6)
        vin = [(-0.20,-0.32),(0.0,-0.80),(0.20,-0.28)]
        staart = [(0.75,-0.05),(1.05,-0.50),(0.98,-0.02),(1.02,0.30)]
        flip = [(-0.40,0.20),(-0.15,0.52),(-0.05,0.22)]
        kieuw = [([(x,-0.08),(x+0.03,-0.08),(x+0.03,0.10),(x,0.10)],'donker') for x in (-0.50,-0.42)]
        lach = bez((-0.92,0.10),(-0.80,0.18),(-0.66,0.10),5) + bez((-0.66,0.10),(-0.80,0.14),(-0.92,0.12),5)
        return [(staart,'lijf'), (vin,'lijf'), (flip,'donker'), (lijf,'lijf'), (buik,'licht')] + kieuw + [(lach,'donker')], [(-0.70,-0.10)]
    if soort == 'zwaard':
        lijf = ellips(0, 0, 0.60, 0.26)
        zwaard = [(-0.55,-0.04),(-1.15,0.02),(-0.55,0.06)]
        buik = ellips(0, 0.06, 0.52, 0.16, 0, 180)
        zeil = bez((-0.30,-0.20),(-0.10,-0.85),(0.35,-0.22),8)
        staart = [(0.55,0),(0.95,-0.45),(0.80,0),(0.95,0.45)]
        return [(staart,'donker'), (zeil,'donker'), (zwaard,'donker'), (lijf,'lijf'), (buik,'licht')], [(-0.36,-0.06)]
    if soort == 'manta':
        lijf = bez((-1.0,0.0),(-0.50,-0.45),(-0.12,-0.25),8) + [(-0.18,-0.50),(-0.06,-0.30),(0.06,-0.30),(0.18,-0.50)] \
             + bez((0.12,-0.25),(0.50,-0.45),(1.0,0.0),8) + bez((1.0,0.0),(0.40,0.12),(0.10,0.35),6) + bez((-0.10,0.35),(-0.40,0.12),(-1.0,0.0),6)
        staart = [(-0.03,0.30),(0.03,0.30),(0.02,0.95),(-0.02,0.95)]
        buik = ellips(0, 0.05, 0.36, 0.16, 0, 180)
        vlek = [ellips(-0.45,-0.12,0.08,0.05), ellips(0.45,-0.12,0.08,0.05)]
        return [(staart,'lijf'), (lijf,'lijf'), (buik,'licht'), (vlek[0],'licht'), (vlek[1],'licht')], [(-0.16,-0.14), (0.16,-0.14)]
    if soort == 'orka':
        lijf = bez((-1.0,0.05),(-0.70,-0.40),(0.30,-0.28),10) + bez((0.30,-0.28),(0.65,-0.15),(0.78,0.0),6) \
             + bez((0.78,0.0),(0.40,0.30),(-0.20,0.30),6) + bez((-0.20,0.30),(-0.80,0.30),(-1.0,0.05),8)
        buik = bez((-0.95,0.12),(-0.40,0.05),(0.20,0.18),6) + bez((0.20,0.18),(-0.40,0.32),(-0.95,0.16),6)
        oogvlek = ellips(-0.52, -0.14, 0.14, 0.07)
        vin = [(-0.10,-0.34),(0.05,-0.95),(0.22,-0.30)]
        staart = [(0.72,-0.04),(1.05,-0.35),(0.98,0.0),(1.05,0.30)]
        flip = [(-0.45,0.22),(-0.25,0.58),(-0.10,0.26)]
        return [(staart,'lijf'), (vin,'lijf'), (flip,'lijf'), (lijf,'lijf'), (buik,'licht'), (oogvlek,'licht')], [(-0.50,-0.14)]
    if soort == 'narwal':
        lijf = bez((-0.85,0.0),(-0.75,-0.40),(0.10,-0.30),10) + bez((0.10,-0.30),(0.60,-0.15),(0.75,0.0),6) \
             + bez((0.75,0.0),(0.40,0.30),(-0.20,0.30),6) + bez((-0.20,0.30),(-0.80,0.28),(-0.85,0.0),8)
        buik = ellips(-0.10, 0.14, 0.55, 0.12)
        tand = [(-0.80,-0.14),(-1.25,-0.42),(-0.78,-0.06)]
        vlek = [(ellips(x, -0.12 + 0.03*k, 0.05, 0.04), 'donker') for k, x in enumerate((-0.20, 0.05, 0.30, 0.50))]
        staart = [(0.70,-0.04),(1.02,-0.32),(0.95,0.0),(1.02,0.28)]
        flip = [(-0.40,0.22),(-0.22,0.52),(-0.10,0.24)]
        return [(staart,'lijf'), (flip,'donker'), (tand,'licht'), (lijf,'lijf'), (buik,'licht')] + vlek, [(-0.58,-0.10)]
    if soort == 'reuzeninkt':
        delen, ogen = nieuwe_delen('inktvis')
        return delen + [(poot(-0.30,0.05,-0.80,0.60,-0.55,1.05,0.07),'donker'), (poot(0.30,0.05,0.80,0.60,0.55,1.05,0.07),'donker')], ogen
    return _oud(soort)

SLAPERIG = {'komkom'}
def dier_beeld(soort, s, kleur_override=None, hoek=0):
    delen, ogen = nieuwe_delen(soort)
    lijf, licht, donker = v3.TINT[soort]
    if kleur_override: lijf = licht = donker = kleur_override
    W = int(s*2.8) + 4; c = W/2
    im = Image.new('RGBA', (W, W), (0,0,0,0)); d = ImageDraw.Draw(im)
    rol = {'lijf': lijf, 'licht': licht, 'donker': donker, 'zwart': (0,0,0)}
    if hoek:
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    for pts, r in delen:
        d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=(rol[r] if not kleur_override or r != 'zwart' else (0,0,0)) + (255,))
    if not kleur_override:
        for ox, oy in ogen:
            R = max(2.0, 0.13*s); p = max(1.2, 0.07*s); x, y = c + ox*s, c + oy*s
            d.ellipse([x-R, y-R, x+R, y+R], fill=WIT + (255,))
            d.ellipse([x-p-R*0.3, y-p, x+p-R*0.3, y+p], fill=W3 + (255,))
            if soort in SLAPERIG:   # ooglid half dicht
                d.chord([x-R, y-R, x+R, y+R], 180, 360, fill=donker + (255,))
            elif s >= 30:
                g = max(1, 0.035*s); d.ellipse([x-R*0.55-g, y-R*0.5-g, x-R*0.55+g, y-R*0.5+g], fill=WIT + (255,))
    import numpy as np
    a = np.array(im)[:, :, 3] > 0; ys, xs = np.nonzero(a)
    return im, (xs.mean() + 0.5, ys.mean() + 0.5), a.sum()

v3.dier_delen = nieuwe_delen
v3.dier_beeld = dier_beeld

ALLE = [('vis','Fish'), ('garnaal','Shrimp'), ('kwal','Jellyfish'), ('pad','Turtle'), ('krab','Crab'), ('paard','Seahorse'),
        ('ster','Starfish'), ('clown','Clownfish'), ('kogel','Pufferfish'), ('octo','Octopus'), ('inktvis','Squid'), ('rog','Ray'),
        ('zeehond','Seal'), ('dolfijn','Dolphin'), ('zwaard','Swordfish'), ('otter','Sea otter'), ('manta','Manta'), ('haai','Shark'),
        ('maanvis','Sunfish'), ('orka','Orca'), ('narwal','Narwhal'), ('reuzeninkt','Giant squid'), ('komkom','Sea cucumber'), ('walvis','Whale')]
RESERVE = [('kreeft','Lobster')]

def dier_scherm(soort, naam):
    def fn(D):
        im = leeg(D)
        zee(im, D, [(D*0.12, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=False, stralen=True)
        opp = (D*0.17)**2*0.55
        s = v3.schaal_voor_gewicht(soort, opp)
        laag, (zx, zy), _ = dier_beeld(soort, s, hoek=(-6 if soort == 'pad' else 0))
        im.paste(laag, (int(round(D/2 - zx)), int(round(D*0.45 - zy))), laag)
        d = ImageDraw.Draw(im)
        v3.tekst(d, D, (D/2, D*0.73), naam, D*0.095, WIT)
        rand(im, D); return im
    return fn

if __name__ == '__main__':
    v3.FONT = sys.argv[2]; uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    from ebb_blad_v3 import f
    gap = 24; cel = 454 + 16 + 260; kol = 6; rijen = (len(ALLE)+kol-1)//kol
    blad = Image.new('RGB', (gap + kol*(cel+gap), 100 + rijen*(454+60+gap)), (14,16,24)); d = ImageDraw.Draw(blad)
    d.text((gap, 28), f'Ebb dieren v4 (Mila): alle 24 in de volgorde van de sea log, zelfde stijl, links 454 AMOLED, rechts 260 MIP', font=f(44), fill=(220,230,240))
    rap = []
    for i, (soort, naam) in enumerate(ALLE):
        r, k = divmod(i, kol); x = gap + k*(cel+gap); y = 100 + r*(454+60+gap)
        a = teken(dier_scherm(soort, naam), 454); b = teken(dier_scherm(soort, naam), 260)
        a.save(f'{uit}/dier-{soort}-454.png'); b.save(f'{uit}/dier-{soort}-260.png')
        blad.paste(a, (x, y)); blad.paste(b, (x+470, y+194))
        d.text((x, y+460), f'{i+1}. {naam}', font=f(30), fill=(170,190,210))
        rap.append(f'{naam:14s} pixels buiten MIP op 260: {niet_mip(b)}')
    blad.save(f'{uit}/../ebb-dieren-v4.png'); print('\n'.join(rap))
