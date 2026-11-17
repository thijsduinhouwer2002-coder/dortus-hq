# Reeks datawijzerplaten, stijlproef 5 "Tij" (Mila, 16 nov 2026). Zelfde als proef 4, met de moet van Daan
# (16 nov 23:30): tussen BB-getal en golftop (of bootje) altijd ruimte, minstens 4 px op 208 (dus S*4/208),
# en het bootje vaart nooit onder het getal. Regel: (1) het bootje blijft rechts van het getal (links grens =
# rechterkant getal + marge); (2) komt water of zeil toch te dicht, dan schuift het getal omhoog, tot vlak
# onder de velden; (3) is dat niet genoeg, dan zakt het plafond voor die stand (alleen bij 100, nooit zichtbaar
# anders dan "vol").  python3 stijl_proef_v5.py
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import stijl_proef_v3 as P
import stijl_proef_v4 as V4
HIER = P.HIER

BB_Y = 0.632                  # voorkeursplek BB-getal (midden)
IKOON_Y, VELD_Y = 0.478, 0.54
P.TOP = 0.715                 # plafond iets lager dan proef 4 (0.70): bij 100 geeft dat de ruimte
LOG = []

def ruimte(S): return max(4, S * 4 / 208)

def plaat(S, thema, hist, t=0.0, log=False):
    zb, zo, uur, mn, tekst, zwak, boot = P.THEMAS[thema]
    im = Image.new('RGB', (S, S), (0, 0, 0)); d = ImageDraw.Draw(im); c = S / 2
    batt = hist[-1]; g = ruimte(S)
    # eerst het getal: maat en plek
    fb = P.f(S * 0.11); dik = max(1, max(2, S // 120) - 1); gk = max(12, S * 0.05)
    # Daan 17 nov 00:35 (kan): rand om het getal een tikje dunner, oogde op 3x als sticker. 1 px tot 359, 2 px vanaf 360.
    bw = d.textlength(f'{batt}', font=fb); groep = bw + gk * 0.25 + gk
    gx0, gx1 = c - groep / 2 - dik, c + groep / 2 + dik
    nx, ny = c - groep / 2 + bw / 2, S * BB_Y
    bb = d.textbbox((nx, ny), f'{batt}', font=fb, anchor='mm')
    onder0 = bb[3] + dik; boven0 = bb[1] - dik
    veld_onder = d.textbbox((c, S * VELD_Y), '8.4K', font=P.f(S * 0.065, 800), anchor='mm')[3]
    max_omhoog = max(0, boven0 - (veld_onder + S * 0.012))
    # bootje: nooit onder het getal, dus links grens = rechterkant getal + halve romp + marge
    s = S * 0.05; min_x = gx1 + s * 1.1 + g
    nu_x = max(S * P.NU_X, min_x)
    while True:
        pts = P.lijn(S, hist, nu_x, t); by = P.hoogte(pts, nu_x)
        romp, zeil, m0, m1 = P.boot_punten(S, nu_x, by + (S * 0.012 if batt < 10 else 0), -22 if batt < 10 else 0)
        if P.past(S, romp + zeil + [m1]) or nu_x <= min_x: break
        nu_x = max(min_x, nu_x - S * 0.01)
    # wat ligt er onder het getal? water binnen de breedte van het getal, en het bootje als het daar komt
    obst = [y for x, y in pts if gx0 - g <= x <= gx1 + g]
    obst += [y for x, y in romp + zeil + [m1] if gx0 - g <= x <= gx1 + g]
    top = (min(obst) if obst else S) - max(2, S // 110) / 2  # halve dikte van de waterlijn telt mee
    tekort = onder0 + g - top
    schuif = min(max(0, tekort), max_omhoog)
    ny -= schuif
    rest = top - (onder0 - schuif)
    if log: LOG.append(f'{S:>3} {thema:<5} {batt:>3}: ruimte getal-golf {rest:5.1f} px (eis {g:.1f}), getal {schuif:4.1f} px omhoog')
    for i, off in enumerate(P.BANDEN):
        kl = P.lerp(zb, zo, i / (len(P.BANDEN) - 1))
        d.polygon([(x, y + S * off) for x, y in pts] + [(S, S), (0, S)], fill=kl)
    lijnkl = tuple(min(255, v + 70) for v in zb)
    d.line(pts, fill=lijnkl, width=max(2, S // 110), joint='curve')
    d.polygon(romp, fill=boot); d.line([m0, m1], fill=boot, width=max(2, S // 150)); d.polygon(zeil, fill=mn)
    P.rand_tekst(d, (nx, ny), f'{batt}', fb, (255, 255, 255), P.lerp(zo, (0, 0, 0), 0.4), dik)
    V4.golfje(d, nx + bw / 2 + gk * 0.75, ny + S * 0.004, gk, lijnkl)
    d.text((c, S * 0.13), 'MON 16', font=P.f(S * 0.065, 700), fill=tekst, anchor='mm')
    ft = P.f(S * 0.30); x = c - d.textlength('7:42', font=ft) / 2; y = S * 0.30
    for deel, kl in (('7', uur), (':', zwak), ('42', mn)):
        d.text((x, y), deel, font=ft, fill=kl, anchor='lm'); x += d.textlength(deel, font=ft)
    ik = max(12, S * 0.04)
    for k, (tek, val) in enumerate([(P.hart, '58'), (P.bliksem, '24'), (P.voet, '8.4K')]):
        gx = c + (k - 1) * S * 0.22
        tek(d, gx, S * IKOON_Y, ik, mn if tek is P.hart else tekst)
        d.text((gx, S * VELD_Y), val, font=P.f(S * 0.065, 800), fill=tekst, anchor='mm')
    m = Image.new('L', (S, S), 0); ImageDraw.Draw(m).ellipse([0, 0, S - 1, S - 1], fill=255)
    out = Image.new('RGB', (S, S), (40, 40, 40)); out.paste(im, (0, 0), m)
    return out

if __name__ == '__main__':
    ST = P.STANDEN
    for S in (208, 218, 240, 260, 280, 390, 416, 454):
        for k, (th, h, lab) in enumerate(ST): plaat(S, th, h, k, log=True)
    W = 6 * 464 + 10
    blad = Image.new('RGB', (W, 454 + 300 + 80), (30, 30, 30)); d = ImageDraw.Draw(blad)
    for k, (th, h, lab) in enumerate(ST):
        x = 10 + k * 464
        blad.paste(plaat(454, th, h, k), (x, 10))
        d.text((x + 227, 484), f'{th}, {lab}', font=P.f(24, 600), fill=(220, 220, 220), anchor='mm')
        blad.paste(plaat(260, th, h, k), (x + 97, 510))
    d.text((W / 2, 805), 'proef 5: altijd ruimte tussen getal en golf (4 px op 208), bootje nooit onder het getal   boven 454, onder 260 (1x)', font=P.f(22, 500), fill=(160, 160, 160), anchor='mm')
    blad.save(os.path.join(HIER, 'stijlproef-v5-tij.png'))
    for S, naam in ((208, '208'), (260, '260')):
        u = Image.new('RGB', (3 * S * 3 + 40, 3 * S + 20), (30, 30, 30))
        for k, i in enumerate((0, 2, 3)):
            u.paste(plaat(S, ST[i][0], ST[i][1], i).resize((3 * S, 3 * S), Image.NEAREST), (10 + k * (3 * S + 10), 10))
        u.save(os.path.join(HIER, f'stijlproef-v5-{naam}-3x.png'))
    open(os.path.join(HIER, 'ruimte-v5.txt'), 'w').write('\n'.join(LOG) + '\n')
    print('\n'.join(l for l in LOG if l.startswith('208') or l.startswith('454')))
