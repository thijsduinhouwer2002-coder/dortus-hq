# Ontwerpblad Ebb v8 (Mila, 11 nov run 28): alleen de dieren-schermen, voor "Voor Mila" punt 4 en 5 in
# ontwerp/garmin/ebb-bouw-1-keuring-drie.md. Bouwt op ebb_blad_v7.py en ebb_dieren_v8.py.
# - Sea log: keuzestip vast 3 px onder het gekozen dier (gemeten aan de onderkant van het dier, niet aan het vak);
#   niet-actieve bladstippen 00AAFF; blad 3 (7 dieren) raster lager, zodat het midden van het raster gelijk ligt met blad 1 en 2.
# - Verhaallijn in één volgorde (A, B, C, D), zie VERHAAL hieronder; elk getal volgt het dierenschema en "hoogstens één nieuw dier
#   per sessie, laagste nummer eerst".
# Gebruik: python3 ebb_blad_v8.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
from ebb_blad_v3 import *
import ebb_blad_v7 as b7
from ebb_blad_v7 import ALLE, SCHEMA, mmss, OCHTEND, AVOND, einde_zee, einde_kop6, bellen, dagstippen, LICHTCYAAN
import ebb_dieren_v8 as dv8
from PIL import Image, ImageDraw
import numpy as np

def teken8(fn, D):
    dv8.D_NU = D*SS if amo(D) else D
    return teken(fn, D)

def dier_vak(im, soort, x, y, w, h, kleur=None, hoek=0):
    """Zelfde als v7, met de dieren van v8. Geeft de onderkant van het getekende dier terug (voor de keuzestip)."""
    s = dv8.maat_voor_vak(soort, w, h)
    laag, _, _ = dv8.dier_beeld(soort, s, kleur, hoek, oog_s=min(w, h)*0.75)
    l, t, r, b = laag.getbbox()
    top = int(round(y - (t + b)/2))
    im.paste(laag, (int(round(x - (l + r)/2)), top), laag)
    return top + b
b7.dier_vak = dier_vak

# ---------------- verhaal: één gebruiker, één volgorde ----------------
# A. 6c, dag 3 avond: sessie 11, reeks 3, 7 gevonden. Geen nieuw dier. "next: Starfish, 1 more day" (nr. 7, 4 dagen op rij).
# B. 6b, dag 4 ochtend: sessie 12, reeks 4. Starfish (4d) en Octopus (12x) halen allebei hun drempel; hoogstens één per sessie,
#    laagste nummer eerst: "new friend: Starfish". 8 gevonden.
# C. sea log na B: "8 of 24". Blad 1 Pufferfish "1 more day in a row" (5d), blad 2 Octopus "next session", blad 3 Whale "at 50 sessions".
# D. 6d, dag 4 avond, Calm telt als sessie 13: "new friend: Octopus".
SESSIES_NU = 12; REEKS_NU = 4
WACHT = {9}          # Octopus: drempel gehaald, komt de volgende sessie
def heb(n):
    dr = SCHEMA[n]
    if dr == 'bonus' or n in WACHT: return False
    return (int(dr[:-1]) <= SESSIES_NU) if dr.endswith('x') else (int(dr[:-1]) <= REEKS_NU)
GEVONDEN = {n for n in range(25) if heb(n)}
def eis(n):
    naam = ALLE[n][1]; dr = SCHEMA[n]
    if n in WACHT: return naam, 'next session'
    if n in GEVONDEN: return naam, ('found' if dr == 'bonus' else (f'after {dr[:-1]} sessions' if dr.endswith('x') else f'{dr[:-1]} days in a row'))
    if dr == 'bonus': return 'Bonus', 'a surprise'
    if dr.endswith('x'):
        k = int(dr[:-1]); m = k - SESSIES_NU
        return naam, (f'at {k} sessions' if m > 9 else f'{m} more session' + ('s' if m > 1 else ''))
    m = int(dr[:-1]) - REEKS_NU
    return naam, f'{m} more day{"s" if m > 1 else ""} in a row'

def stippen_label(d, D, y, n):
    dagstippen(d, D, y, n)
    tekst(d, D, (D/2, y + D*0.062), f'{n} days in a row', D*0.060, LICHTCYAAN)

def s_einde8(D):       # B: dag 4 ochtend, sessie 12
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop6(d, D, [mmss(s) for s in OCHTEND])
    bellen(d, D, [(0.21, 0.56, 0.011), (0.18, 0.51, 0.006), (0.81, 0.58, 0.010), (0.84, 0.53, 0.006)])
    dier_vak(im, 'ster', D/2, D*0.465, D*0.26, D*0.24)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.660), 'new friend: Starfish', D*0.075, GEEL)
    stippen_label(d, D, D*0.745, 4)
    rand(im, D); return im

def s_einde_gewoon8(D):   # A: dag 3 avond, sessie 11, het volgende dier is de Starfish (reeksdier, laagste nummer)
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop6(d, D, [mmss(s) for s in AVOND])
    dier_vak(im, 'ster', D/2, D*0.465, D*0.20, D*0.15, kleur='silhouet')
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.632), 'next: Starfish, 1 more day', D*0.070, WIT)
    stippen_label(d, D, D*0.715, 3)
    # Daan L2: "1 rest day is fine" alleen als je gisteren rustte; op dag 3 van een reeks dus niet (één regel minder)
    rand(im, D); return im

def s_calm_einde8(D):     # D: dag 4 avond, Calm telt als sessie 13: de Octopus komt
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.165), 'calm done', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.245), '4 min · 12 breaths', D*0.066, WIT)
    bellen(d, D, [(0.30, 0.50, 0.010), (0.70, 0.44, 0.008)])
    dier_vak(im, 'octo', D/2, D*0.455, D*0.24, D*0.20)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.640), 'new friend: Octopus', D*0.070, GEEL)
    stippen_label(d, D, D*0.720, 4)
    rand(im, D); return im

def s_rooster8(D, pagina, kies):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.140), 'sea log', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.212), f'{len(GEVONDEN)} of 24', D*0.060, LICHTCYAAN)
    rooster = leeg(D); rd = ImageDraw.Draw(rooster)
    xs = (-0.235, 0, 0.235)
    n_op = min(9, 25 - pagina*9); rijen = (n_op + 2)//3
    y0 = 0.475 - (rijen - 1)*0.07          # blad 3: raster om hetzelfde midden als blad 1 en 2 (lager dan in v7)
    stip = None
    for i in range(n_op):
        n = pagina*9 + i; soort = ALLE[n][0]; r_, k_ = divmod(i, 3)
        rij_n = min(3, n_op - r_*3)
        x = D/2 + (xs[k_] + (3 - rij_n)*0.1175)*D; y = (y0 + r_*0.14)*D
        onder = dier_vak(rooster, soort, x, y, D*0.17, D*0.105, kleur=None if n in GEVONDEN else 'silhouet')
        if n == kies: stip = (x, onder)
    if stip:   # keuzestip: vast 3 px (op 260) onder de onderkant van het gekozen dier
        rr = D*0.012; x, onder = stip; yc = onder + 3*D/260 + rr
        rd = ImageDraw.Draw(rooster); rd.ellipse([x-rr, yc-rr, x+rr, yc+rr], fill=SCHUIM)
    a = np.array(rooster).astype(float).sum(axis=2); xs_ = np.arange(D)[None, :] + 0.5
    m = (a > 0).astype(float)
    dx = 0 if m.sum() == 0 else (m*xs_).sum()/m.sum() - D/2
    dx = max(-D*0.031, min(D*0.031, dx))
    im.paste(rooster, (int(round(-dx)), 0), Image.fromarray((a > 0).astype('uint8')*255))
    d = ImageDraw.Draw(im)
    naam, wat = eis(kies)
    tekst(d, D, (D/2, D*0.735), naam, D*0.072, WIT)
    tekst(d, D, (D/2, D*0.808), wat, D*0.060, LICHTCYAAN)
    for k in range(3):   # niet-actieve bladstippen 00AAFF (keuring punt 4)
        rr = D*0.010; x = D/2 + (k-1)*D*0.04; y = D*0.875
        d.ellipse([x-rr, y-rr, x+rr, y+rr], fill=SCHUIM if k == pagina else (W0 if not amo(D) else AM[W0]))
    rand(im, D); return im
def s_rooster_1(D): return s_rooster8(D, 0, 8)     # Pufferfish: 1 more day in a row (5d)
def s_rooster_2(D): return s_rooster8(D, 1, 9)     # Octopus: next session
def s_rooster_3(D): return s_rooster8(D, 2, 23)    # Whale: at 50 sessions

SCHERMEN = [('A 6c dag 3 avond', s_einde_gewoon8), ('B 6b dag 4 ochtend', s_einde8),
            ('C sea log 1', s_rooster_1), ('C sea log 2', s_rooster_2), ('C sea log 3', s_rooster_3),
            ('D 6d dag 4 avond calm', s_calm_einde8)]

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []; beelden = {}
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = teken8(fn, D); beelden[(naam, D)] = im
            tag = naam.split()[0] + ('' if 'sea log' not in naam else naam.split()[-1])
            im.save(f'{uit}/ebb-v8-{tag}-{D}.png')
            if D == 260:
                rap.append(f'{D:4d}  {naam:24s} kader x {kader_x(im, D):+5.1f} px   vorm x {b7.vorm_x(im, D):+5.1f} px   buiten MIP {niet_mip(im)}   tekst tot {b7.tekst_r(im, D):.2f} R')
    gap = 30; cel_b = 454 + 24 + 260; kol = 3; cel_h = 454 + 64
    rijen = (len(SCHERMEN) + kol - 1)//kol
    import omtrek_toets_v8  # noqa: maakt omtrek-260.png (alle 25 als omtrek, zonder naam, geschud)
    om = Image.open(os.path.join(uit, '..', 'dieren8', 'omtrek-260.png'))
    extra = om.height*3 + 90
    blad = Image.new('RGB', (gap + kol*(cel_b + gap), 110 + rijen*(cel_h + gap) + extra), (14, 16, 24)); d = ImageDraw.Draw(blad)
    y_om = 110 + rijen*(cel_h + gap)
    d.text((gap, y_om), 'Alle 25 als omtrek (niet gevonden), zonder naam, geschud: links ware grootte op 260, rechts 3 keer. Sleutel: dieren8/omtrek-sleutel.txt',
           font=f(32), fill=(220, 230, 240))
    blad.paste(om, (gap, y_om + 60)); blad.paste(om.resize((om.width*3, om.height*3), Image.NEAREST), (gap + om.width + 60, y_om + 60))
    d.text((gap, 30), 'Ebb blad v8 (Mila): dieren v8 en de sea log, één verhaal van links naar rechts (A dag 3, B en C dag 4, D dag 4 avond)',
           font=f(36), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        blad.paste(beelden[(naam, 454)], (x, y)); blad.paste(beelden[(naam, 260)], (x+478, y+194))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v8.png')
    return rap

if __name__ == '__main__':
    v3.FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v8.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
