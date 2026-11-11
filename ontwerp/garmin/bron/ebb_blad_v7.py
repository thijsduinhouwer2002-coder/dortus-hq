# Ontwerpblad Ebb v7 (Mila, 11 nov run 26): alleen dieren, sea log en tekst, zoals de keuring van blad v6 vraagt
# (ontwerp/garmin/ebb-blad-v6-keuring-drie.md, "Voor Mila"). Schermen zonder dieren bouwt Gijs nu uit v6.
# Bouwt op ebb_blad_v6.py en ebb_dieren_v7.py: alleen wat verandert staat hier.
# Gebruik: python3 ebb_blad_v7.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
from ebb_blad_v3 import *
import ebb_blad_v4 as v4
from ebb_blad_v4 import dagstippen
import ebb_blad_v5 as v5
from ebb_blad_v5 import LICHTCYAAN, regel_hart_ronde, veilig, instel
import ebb_blad_v6 as v6
from ebb_blad_v6 import (duik_zee6, BELLEN, einde_zee, einde_kop6, mmss, OCHTEND, AVOND, met_strook, tekst_r, knop,
                         s_menu6, s_ademen6, s_boven6, s_veilig_a, s_veilig_c)
import ebb_dieren_v7 as dv7          # na v6 importeren: zet v3.dier_beeld op v7 (stickerrand)
from ebb_dieren_v7 import ALLE
from PIL import Image, ImageDraw
import numpy as np
dier = v3.dier

def teken7(fn, D):
    dv7.D_NU = D*SS if amo(D) else D
    return teken(fn, D)

def dier_vak(im, soort, x, y, w, h, kleur=None, hoek=0):
    """Dier op zijn kader in een vak van w bij h: zelfde passende maat voor elk dier (punt 1), oog volgt het vak."""
    s = dv7.maat_voor_vak(soort, w, h)
    laag, _, _ = dv7.dier_beeld(soort, s, kleur, hoek, oog_s=min(w, h)*0.75)
    l, t, r, b = laag.getbbox()
    im.paste(laag, (int(round(x - (l + r)/2)), int(round(y - (t + b)/2))), laag)

# ---------------- punt 7: trilteken wit, "time to breathe" zonder haakjes ----------------
def s_duik7(D, sec, ronde, bpm, hoek):
    im = leeg(D); duik_zee6(im, D, sec); d = ImageDraw.Draw(im)
    if sec < 180:
        tekst(d, D, (D/2, D*0.200), 'hold', D*0.085, SCHUIM)
    else:
        px = D*0.072; tekst(d, D, (D/2, D*0.225), 'time to breathe', px, WIT)
        v6.trilboog(d, D, D/2, D*0.225, f(max(px, MIN*D)).getlength('time to breathe'), WIT)
    tekst(d, D, (D/2, D*0.295), 'press  START  to breathe' if D < 300 else 'press START to breathe', D*0.056, LICHTCYAAN)
    tekst(d, D, (D/2, D*0.455), f'{sec//60}:{sec%60:02d}', D*0.28, WIT)
    bellen(d, D, BELLEN[sec])
    dier_vak(im, 'pad', D/2, D*0.665, D*0.20, D*0.12, hoek=hoek)
    d = ImageDraw.Draw(im)
    regel_hart_ronde(d, D, D*0.815, bpm, ronde)
    rand(im, D); return im
def s_duik_b(D): return s_duik7(D, 105, 2, 61, 0)
def s_duik_c(D): return s_duik7(D, 184, 3, 57, -2)

# ---------------- punt 7: start ----------------
def s_start7(D):
    im = leeg(D)
    zee(im, D, [(D*0.80, W1), (D*0.88, W2)], amp=D*0.010)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.235), '3 rounds · 30 breaths', D*0.066, TITEL)
    tekst(d, D, (D/2, D*0.385), 'Sit or', D*0.12, WIT)
    tekst(d, D, (D/2, D*0.49), 'lie down', D*0.12, WIT)
    v4.pil(d, D, 0.655, 0.40, 0.13)
    tekst(d, D, (D/2, D*0.655), 'Start', D*0.080, WIT)
    rand(im, D); return im

# ---------------- punt 8: uitleg bij de eerste Rounds ----------------
def s_uitleg7(D):
    im = leeg(D)
    zee(im, D, [(D*0.80, W1), (D*0.88, W2)], amp=D*0.010)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'how it works', D*0.075, TITEL)
    for k, t in enumerate(['30 deep breaths,', 'then hold while', 'the sea gets dark.', 'START: breathe again.']):
        tekst(d, D, (D/2, D*(0.315 + 0.082*k)), t, D*0.068, WIT if k < 3 else LICHTCYAAN)
    tekst(d, D, (D/2, D*0.645), 'BACK stops', D*0.068, LICHTCYAAN)
    v4.pil(d, D, 0.745, 0.30, 0.11)
    tekst(d, D, (D/2, D*0.745), 'Next', D*0.068, WIT)
    rand(im, D); return im

# ---------------- punt 4: staven op 260 minstens 3:1 (W0 in plaats van W1) ----------------
def staaf_kleur(D): return W0 if not amo(D) else AM[W0]
def s_today7(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'today', D*0.085, TITEL)
    sessies = [('7:40', OCHTEND), ('21:15', AVOND)]
    L, R, bod, hoog = D*0.20, D*0.80, D*0.62, D*0.27
    gat = D*0.08; kol = (R - L - gat)/6; bw = kol*0.62
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m)
    for si, (_, tijden) in enumerate(sessies):
        for j, sec in enumerate(tijden):
            xm = L + (si*3 + j + 0.5)*kol + si*gat; yt = bod - hoog*sec/200
            md.rounded_rectangle([xm-bw/2, yt, xm+bw/2, bod], radius=bw*0.30, fill=255)
    im.paste(Image.new('RGB', (D, D), staaf_kleur(D)), (0, 0), m)
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    d.line([(L - D*0.01, bod), (R + D*0.01, bod)], fill=SCHUIM, width=lw)
    for si, (klok, _) in enumerate(sessies):
        tekst(d, D, (L + (si*3 + 1.5)*kol + si*gat, bod + D*0.055), klok, D*0.062, LICHTCYAAN)
    tot = OCHTEND + AVOND
    tekst(d, D, (D/2, D*0.775), f'6 holds · avg {mmss(sum(tot)//len(tot))}', D*0.072, WIT)
    rand(im, D); return im

def s_weken7(D):
    WEKEN = v6.WEKEN
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), '8 weeks', D*0.085, TITEL)
    L, R, top, bod = D*0.20, D*0.80, D*0.33, D*0.58
    kol = (R-L)/8; bw = kol*0.66; hoog = 7
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m)
    for i, n in enumerate(WEKEN):
        if n:
            xm = L + (i+0.5)*kol; md.rounded_rectangle([xm-bw/2, bod - (bod-top)*n/hoog, xm+bw/2, bod], radius=bw*0.30, fill=255)
    im.paste(Image.new('RGB', (D, D), staaf_kleur(D)), (0, 0), m)
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    d.line([(L, bod), (R, bod)], fill=SCHUIM, width=lw)
    for i, n in enumerate(WEKEN):
        xm = L + (i+0.5)*kol
        if n: tekst(d, D, (xm, bod - (bod-top)*n/hoog - D*0.045), str(n), D*0.066, WIT)
        else:
            rr = D*0.013; d.ellipse([xm-rr, bod-D*0.03-rr, xm+rr, bod-D*0.03+rr], fill=W1 if not amo(D) else AM[W1])
    tekst(d, D, (D/2, D*0.665), 'sessions per week', D*0.066, LICHTCYAAN)
    tekst(d, D, (D/2, D*0.750), 'avg hold 1:41', D*0.075, WIT)
    rand(im, D); return im

# ---------------- punt 5: eindscherm, nieuw dier groter, stippen met label, rustdag ----------------
def stippen_label(d, D, y, n):
    dagstippen(d, D, y, n)
    tekst(d, D, (D/2, y + D*0.062), f'{n} days in a row', D*0.060, LICHTCYAAN)

def s_einde7(D):
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop6(d, D, [mmss(s) for s in OCHTEND])
    bellen(d, D, [(0.21, 0.56, 0.011), (0.18, 0.51, 0.006), (0.81, 0.58, 0.010), (0.84, 0.53, 0.006)])
    dier_vak(im, 'ster', D/2, D*0.465, D*0.26, D*0.24)     # beloningsmoment: 1,6 keer zo groot als in v6
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.660), 'new friend: Starfish', D*0.075, GEEL)
    stippen_label(d, D, D*0.745, 4)
    rand(im, D); return im

def s_einde_gewoon7(D):
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop6(d, D, [mmss(s) for s in AVOND])
    dier_vak(im, 'clown', D/2, D*0.465, D*0.22, D*0.15, kleur='hint')
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.632), 'next: Clownfish, 1 more', D*0.070, WIT)
    stippen_label(d, D, D*0.700, 4)
    tekst(d, D, (D/2, D*0.822), '1 rest day is fine', D*0.060, WIT)
    rand(im, D); return im

# ---------------- punt 8: eindscherm van Calm (telt mee als sessie, zoals de code) ----------------
def s_calm_einde7(D):
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.165), 'calm done', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.245), '4 min · 12 breaths', D*0.066, WIT)
    bellen(d, D, [(0.30, 0.50, 0.010), (0.70, 0.44, 0.008)])
    dier_vak(im, 'pad', D/2, D*0.465, D*0.22, D*0.15, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.640), 'counts as a session', D*0.070, WIT)
    stippen_label(d, D, D*0.720, 5)
    rand(im, D); return im

# ---------------- punt 3 en 9: sea log in week 3 (12 sessies, beste reeks 3 dagen) ----------------
SESSIES_NU = 12; REEKS_NU = 3
SCHEMA = v6.SCHEMA
def heb(n):
    dr = SCHEMA[n]
    if dr == 'bonus': return False
    return (int(dr[:-1]) <= SESSIES_NU) if dr.endswith('x') else (int(dr[:-1]) <= REEKS_NU)
GEVONDEN = {n for n in range(25) if heb(n)}
def eis(n):
    naam = ALLE[n][1]; dr = SCHEMA[n]
    if n in GEVONDEN: return naam, ('found' if dr == 'bonus' else (f'after {dr[:-1]} sessions' if dr.endswith('x') else f'{dr[:-1]} days in a row'))
    if dr == 'bonus': return 'Bonus', 'a surprise'
    if dr.endswith('x'):
        k = int(dr[:-1]); m = k - SESSIES_NU
        return naam, (f'at {k} sessions' if m > 9 else f'{m} more session' + ('s' if m > 1 else ''))
    m = int(dr[:-1]) - REEKS_NU
    return naam, f'{m} more day{"s" if m > 1 else ""} in a row'

def s_rooster7(D, pagina, kies, extra_dx):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.140), 'sea log', D*0.075, TITEL)              # één vaste kop op alle bladen
    tekst(d, D, (D/2, D*0.212), f'{len(GEVONDEN)} of 24', D*0.060, LICHTCYAAN)
    rooster = leeg(D); rd = ImageDraw.Draw(rooster)
    xs = (-0.235, 0, 0.235); ys = (0.335, 0.475, 0.615)
    n_op = min(9, 25 - pagina*9)
    for i in range(n_op):
        n = pagina*9 + i; soort = ALLE[n][0]; r_, k_ = divmod(i, 3)
        rij_n = min(3, n_op - r_*3)
        x = D/2 + (xs[k_] + (3 - rij_n)*0.1175)*D; y = ys[r_]*D
        if n == kies:
            rr = D*0.012; rd.ellipse([x-rr, y+D*0.068-rr, x+rr, y+D*0.068+rr], fill=SCHUIM)
        dier_vak(rooster, soort, x, y, D*0.17, D*0.105, kleur=None if n in GEVONDEN else 'silhouet')
        rd = ImageDraw.Draw(rooster)
    a = np.array(rooster).astype(float).sum(axis=2); xs_ = np.arange(D)[None, :] + 0.5
    # v7.1: optisch centreren op de vorm: elk dier telt even zwaar, gevonden of silhouet (een gekleurd dier is niet "zwaarder"
    # dan een silhouet met rand). Zwaartepunt van alle niet-zwarte pixels van het raster in het midden, hoogstens 8 px op 260.
    m = (a > 0).astype(float)
    dx = 0 if m.sum() == 0 else (m*xs_).sum()/m.sum() - D/2
    dx = max(-D*0.031, min(D*0.031, dx)) + extra_dx*D/260
    im.paste(rooster, (int(round(-dx)), 0), Image.fromarray((a > 0).astype('uint8')*255))
    d = ImageDraw.Draw(im)
    naam, wat = eis(kies)
    tekst(d, D, (D/2, D*0.735), naam, D*0.072, WIT)
    tekst(d, D, (D/2, D*0.808), wat, D*0.060, LICHTCYAAN)
    for k in range(3):   # bladstippen in plaats van "1 / 3"
        rr = D*0.010; x = D/2 + (k-1)*D*0.04; y = D*0.875
        d.ellipse([x-rr, y-rr, x+rr, y+rr], fill=SCHUIM if k == pagina else (W1 if not amo(D) else AM[W1]))
    rand(im, D); return im
def s_rooster_1(D): return s_rooster7(D, 0, 6, 0)     # Starfish: reeksdier, nog niet gevonden
def s_rooster_2(D): return s_rooster7(D, 1, 10, 0)     # Eel: 2 more sessions
def s_rooster_3(D): return s_rooster7(D, 2, 23, 0)     # Whale: at 50 sessions

# ---------------- punt 7: 8c is een knop, met hoe je kiest ----------------
def s_zeelog7(D):
    im = leeg(D)
    zee(im, D, [(D*0.30, W2), (D*0.75, W3)], amp=D*0.010, schuim=False)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.16), 'sea log', D*0.075, TITEL)
    bellen(d, D, [(0.27, 0.44, 0.010), (0.74, 0.38, 0.007)])
    dier_vak(im, 'pad', D/2, D*0.405, D*0.28, D*0.17, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.575), 'Turtle · 3 days in a row', D*0.068, WIT)
    knop(d, D, 0.685, 0.56, 0.12, True)
    tekst(d, D, (D/2, D*0.685), 'swim with me', D*0.068, WIT)
    tekst(d, D, (D/2, D*0.790), 'START picks', D*0.060, LICHTCYAAN)
    rand(im, D); return im

# ---------------- punt 6: settings ----------------
def s_instel_a(D): return instel(D, 'Rounds  3', 'Breathing pace', '15 per min', ['Breaths  30', 'Buzz every 30 s  on'])
def s_instel_b(D): return instel(D, 'Buzz on last 3 breaths  on', 'Touch lock', 'on', ['Ebb makes no sound', 'Safety info'])

SCHERMEN = [('1 menu', s_menu6), ('1b start', s_start7), ('1c eerste keer', s_uitleg7), ('2 ademen', s_ademen6),
            ('3b hold 1:45', s_duik_b), ('3c hold 3:04', s_duik_c), ('4 herstel', s_boven6), ('6 today', met_strook(s_today7)),
            ('6b einde met dier', s_einde7), ('6c einde zonder dier', s_einde_gewoon7), ('6d einde calm', s_calm_einde7), ('7 8 weeks', met_strook(s_weken7)),
            ('8 sea log 1 van 3', s_rooster_1), ('8b sea log 2 van 3', s_rooster_2), ('8d sea log 3 van 3', s_rooster_3), ('8c sea log dier', s_zeelog7),
            ('9 settings', met_strook(s_instel_a)), ('9b settings', met_strook(s_instel_b)), ('10 veilig 1', met_strook(s_veilig_a)), ('10c veilig 3', met_strook(s_veilig_c))]

def vorm_x(im, D):
    """Zwaartepunt van alles wat niet zwart is binnen 0,44 R (ring en water niet; silhouetten tellen wel mee, anders dan optisch_x)."""
    a = np.array(im).astype(int); m = a.sum(axis=2) > 0
    for c in (RING, W1, W2):
        m &= ~((a[:, :, 0] == c[0]) & (a[:, :, 1] == c[1]) & (a[:, :, 2] == c[2]))
    y, x = np.mgrid[0:D, 0:D]; m &= np.hypot(x+0.5-D/2, y+0.5-D/2) < D*0.44
    ys, xs = np.nonzero(m)
    return xs.mean() + 0.5 - D/2

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []; beelden = {}
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = teken7(fn, D); beelden[(naam, D)] = im; im.save(f'{uit}/ebb-v7-{naam.split()[0]}-{D}.png')
            if D == 260:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px   optisch x {optisch_x(im, D):+5.1f} px   vorm x {vorm_x(im, D):+5.1f} px   buiten MIP {niet_mip(im)}   tekst tot {tekst_r(im, D):.2f} R')
    klein = sorted({(t, p) for D, t, p in v3.LOG if D == 260}, key=lambda z: z[1])[:6]
    rap.append('kleinste tekst op 260: ' + ', '.join(f'"{t}" {p} px' for t, p in klein))
    gap = 30; cel_b = 454 + 24 + 260; kol = 4; cel_h = 454 + 64
    rijen = (len(SCHERMEN) + kol - 1)//kol
    blad = Image.new('RGB', (gap + kol*(cel_b + gap), 110 + rijen*(cel_h + gap)), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 30), 'Ebb blad v7 (Mila): dieren als stickers, sea log in week 3, tekstpunten. Links 454 AMOLED, rechts 260 MIP, ware grootte',
           font=f(44), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        blad.paste(beelden[(naam, 454)], (x, y)); blad.paste(beelden[(naam, 260)], (x+478, y+194))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v7.png')
    return rap

if __name__ == '__main__':
    v3.FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v7.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
