# Ebb dieren v8.2 (Mila, 11 nov run 30): "Voor Mila" in ontwerp/garmin/ebb-bouw-2-keuring-drie.md.
# Bouwt op ebb_dieren_v8.py. Alleen wat verandert staat hier.
# 1. Zeeotter: op de rug drijvend, kop in profiel met snuit en oor, pootjes met schelp boven de buik, voeten omhoog, platte staart.
# 2. Narwal: lijf hoger (4 px op 260).
# 3. Dolfijn, zwaardvis en haai elk een eigen tint (en de haai niet meer gelijk aan de maanvis).
# 4. Zeepaardje voller in zijn vak: dikkere buik, lange snuit, grote rugvin, staart krult naar buiten.
# 5. Rog: ruitvorm met puntige vleugels en spitse snuit, staart met stekel; zandkleur zodat hij niet op de manta lijkt.
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
import ebb_dieren_v8 as dv8
from ebb_blad_v3 import bez, ellips
from ebb_dieren_v4 import poot

# Alleen MIP-kleuren (elk kanaal 0, 85, 170 of 255). (lijf, licht, donker)
v3.TINT.update({
    'dolfijn': ((85,170,255),  (170,255,255), (0,85,170)),     # hemelsblauw, lichte buik (blijft)
    'zwaard':  ((85,85,255),   (255,255,255), (170,170,255)),  # indigo met witte buik, lila zeil, zwaard en staart (3,0:1 op het lijf)
    'haai':    ((85,170,170),  (255,255,255), (0,85,85)),      # staalgrijs-groen, witte buik
    'otter':   ((170,85,0),    (255,255,170), (85,0,0)),       # bruin met roomkleurige snuit
    'rog':     ((170,170,85),  (255,255,170), (85,85,0)),      # zand
    'paard':   ((255,170,0),   (255,255,85),  (170,85,0)),     # oranje (blijft)
})

_oud = dv8.delen_v8

def delen_v82(soort):
    if soort == 'otter':
        # drijft op de rug als een bootje: kop omhoog links, voeten omhoog rechts, schelp op de buik
        lijf = bez((-0.46,-0.20),(0.05,0.10),(0.56,-0.24),10) + bez((0.56,-0.24),(0.80,-0.10),(0.66,0.14),5) \
             + bez((0.66,0.14),(0.10,0.52),(-0.50,0.18),10) + bez((-0.50,0.18),(-0.66,0.00),(-0.46,-0.20),5)
        borst = bez((-0.40,-0.10),(0.05,0.18),(0.50,-0.14),6) + bez((0.50,-0.14),(0.10,0.30),(-0.40,0.02),6)
        staart = [(0.60,-0.02),(0.84,-0.20),(0.90,-0.08),(0.66,0.12)]
        kop = ellips(-0.52, -0.40, 0.36, 0.33)
        snuit = ellips(-0.78, -0.30, 0.18, 0.14)
        neus = ellips(-0.94, -0.38, 0.07, 0.055)
        oor = ellips(-0.34, -0.70, 0.11, 0.10)
        voet1 = [(0.30,-0.12),(0.24,-0.60),(0.48,-0.66),(0.46,-0.12)]
        voet2 = [(0.48,-0.14),(0.58,-0.58),(0.78,-0.48),(0.60,-0.06)]
        schelp = bez((-0.24,-0.06),(-0.02,-0.56),(0.20,-0.06),6) + [(-0.02,0.0)]
        ribbel = [([(x-0.02,-0.08),(x+0.02,-0.08),(x*1.4+0.02,-0.34),(x*1.4-0.02,-0.34)], 'donker') for x in (-0.10, 0.06)]
        poot1 = ellips(-0.26, -0.10, 0.09, 0.08)
        poot2 = ellips(0.22, -0.10, 0.09, 0.08)
        return [(staart,'donker'), (voet1,'donker'), (voet2,'donker'), (lijf,'lijf'), (borst,'licht'), (oor,'lijf'),
                (kop,'lijf'), (snuit,'licht_k'), (neus,'zwart'), (schelp,'muts_k')] + ribbel + \
               [(poot1,'donker'), (poot2,'donker')], [(-0.56,-0.50)]
    if soort == 'narwal':
        delen, ogen = _oud('narwal')
        K = 1.30   # lijf, buik, vlekken en vinnen hoger; tand en draai blijven
        uit = []
        for pts, r in delen:
            if r == 'donker_k' or (r == 'licht' and min(x for x, _ in pts) < -1.0):
                uit.append((pts, r))
            else:
                uit.append(([(x, y*K) for x, y in pts], r))
        return uit, [(x, y*K) for x, y in ogen]
    if soort == 'paard':
        kop = ellips(0.10, -0.66, 0.27, 0.25)
        snuit = [(-0.08,-0.76),(-0.66,-0.70),(-0.68,-0.56),(-0.08,-0.54)]
        lijf = bez((0.30,-0.54),(0.78,-0.10),(0.34,0.34),10) + bez((0.34,0.34),(0.06,0.54),(0.14,0.72),6) \
             + bez((0.14,0.72),(0.40,0.98),(0.62,0.80),6) + bez((0.62,0.80),(0.70,0.58),(0.46,0.58),5) \
             + bez((0.46,0.58),(0.38,0.66),(0.44,0.72),3) + bez((0.44,0.72),(0.30,0.70),(0.28,0.62),3) \
             + bez((0.28,0.62),(-0.40,0.44),(-0.40,0.02),8) + bez((-0.40,0.02),(-0.36,-0.40),(-0.06,-0.52),6)
        buik = bez((-0.34,-0.02),(-0.36,0.34),(0.08,0.46),6) + bez((0.08,0.46),(-0.06,0.10),(-0.10,-0.34),6)
        ring = [([(-0.36+0.02*i, -0.18+0.15*i),(0.00, -0.12+0.15*i),(0.00, -0.09+0.15*i),(-0.36+0.02*i, -0.15+0.15*i)], 'donker') for i in range(4)]
        kam = [(0.20,-0.88),(0.28,-1.02),(0.36,-0.84),(0.48,-0.94),(0.46,-0.68)]
        vin = [(0.54,-0.20),(0.92,-0.16),(0.86,0.12),(0.50,0.10)]
        return [(vin,'licht'), (lijf,'lijf'), (buik,'licht')] + ring + [(kam,'donker'), (snuit,'lijf'), (kop,'lijf')], [(0.02,-0.70)]
    if soort == 'rog':
        # ruit: spitse snuit boven, vleugelpunten opzij, achterkant rond; bovenaanzicht
        schijf = bez((0.0,-0.62),(0.40,-0.40),(1.05,0.02),10) + bez((1.05,0.02),(0.55,0.20),(0.0,0.42),10) \
               + bez((0.0,0.42),(-0.55,0.20),(-1.05,0.02),10) + bez((-1.05,0.02),(-0.40,-0.40),(0.0,-0.62),10)
        midden = bez((0.0,-0.50),(0.26,-0.10),(0.0,0.34),6) + bez((0.0,0.34),(-0.26,-0.10),(0.0,-0.50),6)
        bekken = [[(k*0.08,0.32),(k*0.28,0.46),(k*0.10,0.52)] for k in (-1, 1)]
        staart = [(-0.04,0.40),(0.04,0.40),(0.02,1.02),(-0.02,1.02)]
        stekel = [(0.02,0.74),(0.14,0.66),(0.03,0.80)]
        stip = [(ellips(x, y, 0.06, 0.05), 'donker') for x, y in ((-0.50,0.04), (0.50,0.04), (-0.28,0.18), (0.28,0.18))]
        return [(staart,'donker'), (stekel,'donker'), (bekken[0],'lijf'), (bekken[1],'lijf'), (schijf,'lijf'), (midden,'licht')] + stip, \
               [(-0.13,-0.22), (0.13,-0.22)]
    return _oud(soort)

dv8.delen_v8 = delen_v82
v3.dier_delen = delen_v82
ALLE = dv8.ALLE
dier_beeld = dv8.dier_beeld
maat_voor_vak = dv8.maat_voor_vak
ROL_V8 = dv8.ROL_V8
