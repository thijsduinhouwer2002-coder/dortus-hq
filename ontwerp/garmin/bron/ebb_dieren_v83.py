# Ebb dieren v8.3 (Mila, 11 nov run 31): "Voor Mila" in ontwerp/garmin/ebb-bouw-3-keuring-drie.md.
# Bouwt op ebb_dieren_v82.py. Alleen wat verandert staat hier.
# 1. Ogen: in de data blijft het oog een punt; hoe het horloge het tekent staat in horloge_sim.py (oog_modus 'v83').
#    Acht dieren kregen een ander oogpunt, zodat het zwarte oog op een lichte plek valt (zie OOG_NIEUW en OOG_SCHUIF).
# 2. Kogelvis: 14 dunne stekels werden op 260 een harige ring. Nu een bolle vis met 6 korte dikke stekels (alleen boven en onder), een
#    waaierstaart, een vinnetje, getuite lippen als kenmerk (zodat ook het silhouet een vis met een tuitmond is).
# 3. Narwal: de draai op de tand las op 260 als "zzz" (slapen); tand nu glad, de lange tand is zelf het kenmerk.
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_dieren_v82 as dv82
import ebb_dieren_v8 as dv8
import ebb_blad_v3 as v3
from ebb_blad_v3 import ellips, bez
from ebb_dieren_v4 import poot

# Narwal: wit lijf met witte tand las in de frisse toets als "witte vis met lange snuit". Nu een gevlekte grijsblauwe rug
# (5555AA met lichte vlekken AAAAFF) en witte buik, zodat de witte tand los van de kop staat en als hoorn leest.
v3.TINT['narwal'] = ((85, 85, 170), (255, 255, 255), (170, 170, 255))

_oud = dv8.delen_v8   # is na het importeren van v8.2 al delen_v82

def delen_v83(soort):
    if soort == 'komkom':
        # frisse toets: "blok met bobbels" en de voelers lazen als een walvisfontein. Nu een lange worst (1,3 keer zo lang),
        # puntige bulten op de rug, voetjes eronder, en de voelers als bloemetje vooruit aan de kop in plaats van omhoog.
        K = 1.30
        lijf = bez((-0.70,0.06),(-0.70,-0.30),(-0.10,-0.28),8) + bez((-0.10,-0.28),(0.62,-0.26),(0.70,0.04),8) \
             + bez((0.70,0.04),(0.66,0.28),(0.0,0.28),8) + bez((0.0,0.28),(-0.70,0.30),(-0.70,0.06),8)
        lijf = [(x*K, y) for x, y in lijf]
        buik = [(x*K, y) for x, y in bez((-0.58,0.14),(0.0,0.08),(0.58,0.14),6) + bez((0.58,0.14),(0.0,0.30),(-0.58,0.14),6)]
        bult = [([(x-0.09,-0.24),(x,-0.44),(x+0.09,-0.24)], 'donker') for x in (-0.44, -0.12, 0.20, 0.52)]
        voet = [(ellips(x, 0.32, 0.06, 0.07), 'donker') for x in (-0.60, -0.30, 0.0, 0.30, 0.60)]
        kroon = []
        for a_ in (150, 180, 210):
            r_ = math.radians(a_); x0, y0 = -0.86 + 0.04*math.cos(r_), -0.04 + 0.04*math.sin(r_)
            x1, y1 = -0.86 + 0.20*math.cos(r_), -0.04 + 0.20*math.sin(r_)
            kroon.append((poot(x0, y0, (x0+x1)/2, (y0+y1)/2, x1, y1, 0.045), 'donker'))
            kroon.append((ellips(x1, y1, 0.065, 0.065), 'donker'))
        lach = bez((-0.76,0.10),(-0.66,0.18),(-0.54,0.10),4) + bez((-0.54,0.10),(-0.66,0.14),(-0.76,0.10),4)
        return voet + kroon + bult + [(lijf,'lijf'), (buik,'licht'), (lach,'zwart')], [(-0.60,-0.08)]
    if soort == 'otter':
        # frisse toets: "bruine klodder, vreemd ding op de buik". Voeten en staart nu in de lijfkleur (donkerbruin viel weg),
        # de schelp 1,6 keer zo groot zonder ribbels, met de pootjes erop: het otterteken (drijven op de rug met een schelp).
        delen, ogen = _oud(soort)
        uit = []
        for i, (pts, r) in enumerate(delen):
            if i in (0, 1, 2): r = 'lijf'
            if i in (10, 11): continue          # ribbels op de schelp: op 260 een donkere V, weg
            if r == 'muts_k':
                pts = [(-0.02 + (x + 0.02)*1.6, -0.06 + (y + 0.06)*1.6) for x, y in pts]
            uit.append((pts, r))
        return uit, ogen
    if soort == 'kogel':
        # bolle vis die naar links kijkt: grote waaierstaart rechts, korte dikke stekels alleen boven en onder
        X = -0.12
        lijf = ellips(X, 0.0, 0.62, 0.56)
        stekels = []
        for hoek in (-135, -95, -55, 135, 95, 55):
            a = math.radians(hoek); b = 0.24
            stekels.append(([(X + 0.56*math.cos(a-b), 0.50*math.sin(a-b)), (X + 0.86*math.cos(a), 0.80*math.sin(a)),
                             (X + 0.56*math.cos(a+b), 0.50*math.sin(a+b))], 'donker'))
        staart = [(0.40,-0.06),(1.00,-0.46),(0.88,0.0),(1.00,0.46),(0.40,0.06)]
        buik = ellips(X - 0.02, 0.20, 0.50, 0.32, 15, 165)
        vin = [(0.00,0.04),(0.26,-0.10),(0.24,0.18)]
        lippen = [(-0.70,0.00),(-0.92,-0.06),(-0.96,0.10),(-0.92,0.24),(-0.70,0.18)]
        return [(staart,'donker')] + stekels + [(lippen,'donker_k'), (lijf,'lijf'), (buik,'licht'), (vin,'donker')], [(-0.40,-0.16)]
    delen, ogen = _oud(soort)
    if soort == 'narwal':
        # de draai op de tand (drie schuine streepjes) las op 260 als "zzz", dus een slapend dier; tand nu glad
        delen = [(p, r) for p, r in delen if r != 'donker_k']
    if soort in OOG_NIEUW: return delen, OOG_NIEUW[soort]
    if soort in OOG_SCHUIF: return delen, [(x + dx/90, y + dy/90) for (x, y), (dx, dy) in zip(ogen, OOG_SCHUIF[soort])]
    return delen, ogen

# Ogen die met het zwarte oog van v8.3 wegvielen (gemeten met meet_ogen_v83.py: de ring van 1 px rond het oog moet
# voor minstens 75% 3:1 tegen zwart halen, op alle maten van de app). Krab: van de dunne steeltjes op het schild.
# Orka: in de witte oogvlek. De rest: een paar 1/90 opgeschoven naar de dichtstbijzijnde lichte plek.
OOG_NIEUW = {'krab': [(-0.22, -0.02), (0.22, -0.02)], 'orka': [(-0.50, -0.12)]}
OOG_SCHUIF = {'haai': [(4, 8)], 'clown': [(-12, 4)], 'kreeft': [(4, 4), (-4, 4)], 'garnaal': [(-2, -4)],
              'zwaard': [(2, 6)], 'aal': [(10, 2)]}

dv8.delen_v8 = delen_v83
v3.dier_delen = delen_v83
ALLE = dv8.ALLE
dier_beeld = dv8.dier_beeld
ROL_V8 = dv8.ROL_V8
