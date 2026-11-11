# Ebb dieren v6 (Mila, 11 nov run 24): moet-punten 6, 7 en 8 van de keuring van blad v5 (drie beoordelaars).
# Bouwt op ebb_dieren_v5.py (zelfde tekenregel, zelfde oog). Alleen wat verandert staat hier.
# - Kleuren met minstens 3:1 op 0000AA en 000055: manta AAAAAA, reuzeninktvis AA55FF, zeeotter FFAA55, orka met dikkere lichte rand.
# - Walvis blauw, met fontein, en groter; narwal wit met donkere vlekken, ronde kop, lange rechte slagtand, geen rugvin
#   (zwaardvis heeft zeil en zwaard: nu duidelijk anders); zeekomkommer zonder mutsje; reuzeninktvis groter dan inktvis.
# - Niet gevonden: egaal silhouet 0000AA met dunne rand 0055FF, geen ogen of strepen; het nummer staat erop (blad_v6).
# Gijs: na het ja van Thijs je maak_dieren_data.py op delen_v6 / TINT / RAND van dit bestand zetten.
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
import ebb_dieren_v5 as dv5
from ebb_blad_v3 import bez, ellips, WIT, W3
from PIL import Image, ImageDraw
import numpy as np

v3.TINT.update({
    'manta':      ((170,170,170), (255,255,255), (85,85,85)),
    'reuzeninkt': ((170,85,255),  (255,170,255), (85,0,170)),
    'otter':      ((255,170,85),  (255,255,170), (170,85,0)),
    'walvis':     ((85,170,255),  (170,255,255), (0,85,170)),
    'narwal':     ((255,255,255), (255,255,255), (85,85,170)),
    'kreeft':     ((255,85,85),   (255,170,170), (170,0,0)),     # lichter: haalt 3:1 op 0000AA
})
RAND = dict(dv5.RAND); RAND.update({'orka': (170,170,255), 'manta': (85,85,85), 'kreeft': (255,170,170)})
DIK = {'orka'}                           # rand 2 px, ook op 260
GROTER = {'walvis': 1.30, 'reuzeninkt': 1.25, 'orka': 1.10, 'haai': 1.10, 'otter': 1.15, 'zeehond': 1.10}   # zeldzaam = groter, in de sea log en op 6b
SIL = (0,0,170); SIL_RAND = (0,85,255)

def delen_v6(soort):
    if soort == 'komkom':   # zonder mutsje (punt 8): zacht, bobbelig, pootjes, halfdichte ogen
        delen, ogen = dv5.delen_v5('komkom')
        return [p for p in delen if p[1] not in ('muts', 'witp')], ogen
    if soort == 'walvis':   # walvis met fontein: drie druppels en een boog boven de kop
        delen, ogen = dv5.delen_v5('walvis')
        fontein = [(-0.60,-0.30),(-0.66,-0.62),(-0.82,-0.82),(-0.70,-0.86),(-0.58,-0.68),(-0.46,-0.86),(-0.34,-0.82),(-0.50,-0.62),(-0.54,-0.30)]
        return delen + [(fontein, 'witp')], ogen
    if soort == 'narwal':   # ronde kop, geen rugvin, slagtand recht naar voren met ribbels
        lijf = bez((-0.70,0.02),(-0.72,-0.34),(-0.20,-0.32),10) + bez((-0.20,-0.32),(0.45,-0.26),(0.78,-0.02),8) \
             + bez((0.78,-0.02),(0.40,0.30),(-0.20,0.30),6) + bez((-0.20,0.30),(-0.70,0.32),(-0.70,0.02),8)
        buik = ellips(-0.10, 0.16, 0.50, 0.11)
        tand = [(-0.68,-0.10),(-1.30,-0.13),(-1.30,-0.09),(-0.68,-0.02)]
        ribbel = [(ellips(x, -0.11, 0.012, 0.035), 'donker') for x in (-0.82, -0.96, -1.10)]
        vlek = [(ellips(x, y, 0.06, 0.045), 'donker') for x, y in ((-0.15,-0.18), (0.10,-0.12), (0.34,-0.10), (0.02,0.02), (0.50,-0.02))]
        staart = [(0.70,-0.04),(1.02,-0.34),(0.94,0.0),(1.02,0.30)]
        flip = [(-0.38,0.20),(-0.22,0.50),(-0.08,0.22)]
        return [(staart,'donker'), (flip,'donker'), (tand,'licht'), (lijf,'lijf'), (buik,'licht')] + vlek + ribbel, [(-0.50,-0.10)]
    if soort == 'otter':    # zeeotter drijft op zijn rug: lang lijf, witte kop links, buik boven met witte schelp, voeten omhoog
        lijf = bez((-0.55,0.05),(-0.10,-0.30),(0.60,-0.10),8) + bez((0.60,-0.10),(0.80,0.0),(0.70,0.18),4) \
             + bez((0.70,0.18),(0.10,0.32),(-0.55,0.22),8)
        buik = bez((-0.45,-0.02),(0.05,-0.26),(0.55,-0.08),6) + bez((0.55,-0.08),(0.10,0.02),(-0.45,0.08),6)
        kop = ellips(-0.72, 0.02, 0.30, 0.27)
        gezicht = ellips(-0.76, 0.06, 0.21, 0.17)
        oor = [ellips(-0.90, -0.20, 0.07, 0.06), ellips(-0.56, -0.23, 0.07, 0.06)]
        neus = ellips(-0.92, 0.04, 0.06, 0.05)
        schelp = bez((-0.30,-0.22),(-0.12,-0.52),(0.06,-0.22),6)
        handen = [ellips(-0.32, -0.22, 0.08, 0.07), ellips(0.08, -0.22, 0.08, 0.07)]
        voet1 = [(0.50,-0.10),(0.62,-0.52),(0.74,-0.50),(0.66,-0.08)]
        voet2 = [(0.66,-0.04),(0.86,-0.42),(0.96,-0.36),(0.80,0.02)]
        staart = [(0.70,0.08),(1.08,0.04),(1.06,0.18),(0.72,0.20)]
        return [(staart,'donker'), (voet1,'donker'), (voet2,'donker'), (lijf,'lijf'), (buik,'licht'), (oor[0],'lijf'), (oor[1],'lijf'),
                (kop,'lijf'), (gezicht,'licht'), (neus,'zwart'), (schelp,'witp'), (handen[0],'donker'), (handen[1],'donker')], [(-0.70,-0.06)]
    if soort == 'zeehond':  # zeehond ligt: kop omhoog links, voorflipper naar beneden, gevorkte staartflippers, witte snor
        lijf = bez((-0.70,-0.30),(-0.40,-0.20),(0.10,-0.12),8) + bez((0.10,-0.12),(0.60,-0.06),(0.85,0.10),6) \
             + bez((0.85,0.10),(0.30,0.32),(-0.40,0.28),8) + bez((-0.40,0.28),(-0.80,0.20),(-0.70,-0.30),8)
        kop = ellips(-0.72, -0.30, 0.26, 0.22)
        snuit = ellips(-0.92, -0.24, 0.13, 0.10)
        neus = ellips(-1.02, -0.30, 0.05, 0.04)
        buik = bez((-0.70,0.10),(-0.10,0.12),(0.60,0.14),6) + bez((0.60,0.14),(0.00,0.30),(-0.70,0.20),6)
        flip = [(-0.35,0.18),(-0.20,0.55),(-0.02,0.50),(-0.10,0.18)]
        staart = [(0.78,0.06),(1.12,-0.18),(1.00,0.12),(1.14,0.36),(0.80,0.20)]
        vlek = [(ellips(x, y, 0.05, 0.04), 'donker') for x, y in ((-0.20,-0.10), (0.15,-0.04), (0.42,0.02))]
        snor = [(ellips(-0.88+dx, -0.18+dy, 0.025, 0.025), 'witp') for dx, dy in ((0,0), (0.07,0.02), (0.03,0.07))]
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht'), (flip,'donker'), (kop,'lijf'), (snuit,'licht'), (neus,'zwart')] + vlek + snor, [(-0.70,-0.38)]
    return dv5.delen_v5(soort)

def dier_beeld(soort, s, kleur_override=None, hoek=0):
    delen, ogen = delen_v6(soort)
    lijf, licht, donker = v3.TINT[soort]
    rol = {'lijf': lijf, 'licht': licht, 'donker': donker, 'zwart': (0,0,0), 'muts': dv5.MUTS, 'witp': WIT}
    stil = kleur_override == 'silhouet'
    if stil: rol = {k: SIL for k in rol}
    elif isinstance(kleur_override, dict): rol = dict(kleur_override)
    elif kleur_override: rol = {k: kleur_override for k in rol}
    if hoek:
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    W = int(s*2.8) + 8; c = W/2
    im = Image.new('RGBA', (W, W), (0,0,0,0)); d = ImageDraw.Draw(im)
    if stil:   # punt 6: één egaal vlak met alleen een buitenrand (geen binnenlijnen)
        for pts, r in delen:
            d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=(255,255,255,255))
        from PIL import ImageFilter
        a = im.split()[3]; k = max(2, round(s/30))
        groot = a.filter(ImageFilter.MaxFilter(2*k + 1))
        out = Image.new('RGBA', (W, W), (0,0,0,0))
        out.paste(Image.new('RGBA', (W, W), SIL_RAND + (255,)), (0, 0), groot)
        out.paste(Image.new('RGBA', (W, W), SIL + (255,)), (0, 0), a)
        m = np.array(out)[:, :, 3] > 0; ys, xs = np.nonzero(m)
        return out, (xs.mean() + 0.5, ys.mean() + 0.5), m.sum()
    if soort in RAND and not kleur_override:
        k = max(2, round(s/30)) if soort in DIK else max(1, round(s/45))
        rk = RAND[soort]
        for ox, oy in ((-k,0),(k,0),(0,-k),(0,k),(-k,-k),(k,k),(-k,k),(k,-k)) if soort in DIK else ((-k,0),(k,0),(0,-k),(0,k)):
            for pts, r in delen:
                d.polygon([(c + x*s + ox, c + y*s + oy) for x, y in pts], fill=rk + (255,))
    for pts, r in delen:
        d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=rol[r] + (255,))
    if not kleur_override:
        for ox, oy in ogen:
            R = max(2.0, 0.13*s); p = max(1.2, 0.07*s); x, y = c + ox*s, c + oy*s
            d.ellipse([x-R, y-R, x+R, y+R], fill=WIT + (255,))
            d.ellipse([x-p-R*0.3, y-p, x+p-R*0.3, y+p], fill=W3 + (255,))
            if soort in dv5.SLAPERIG:
                d.chord([x-R, y-R, x+R, y+R], 180, 360, fill=donker + (255,))
            elif s >= 30:
                g = max(1, 0.035*s); d.ellipse([x-R*0.55-g, y-R*0.5-g, x-R*0.55+g, y-R*0.5+g], fill=WIT + (255,))
    a = np.array(im)[:, :, 3] > 0; ys, xs = np.nonzero(a)
    return im, (xs.mean() + 0.5, ys.mean() + 0.5), a.sum()

v3.dier_delen = delen_v6
v3.dier_beeld = dier_beeld

# Volgorde v6: zeekomkommer is bonus nummer 25 (besluit hoofdchat 11 nov 00:55), walvis nummer 24, Lobster nummer 23.
_basis = [x for x in dv5.ALLE if x[0] not in ('komkom', 'walvis')]
ALLE = _basis + [('kreeft', 'Lobster'), ('walvis', 'Whale'), ('komkom', 'Sea cucumber')]   # Lobster (al getekend in v4) vult nr. 23
