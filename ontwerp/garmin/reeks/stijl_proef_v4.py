# Reeks datawijzerplaten, stijlproef 4 "Tij" (Mila, 16 nov 2026). Zelfde als proef 3, met de moet van Daan
# (16 nov 22:45): het batterijtje naast het BB-getal las als de accu van het horloge. Nu een eigen teken:
# een golfje (zegt: dit getal is de zee). En de kans: het getal staat vast, net boven het plafond links,
# zodat het niet de hele dag met de waterlijn meespringt.  python3 stijl_proef_v4.py
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import stijl_proef_v3 as P
HIER = P.HIER

BB_Y = 0.638                  # vaste plek BB-getal (midden), net boven het plafond (0.70); getal + golfje samen gecentreerd
IKOON_Y, VELD_Y = 0.478, 0.54 # velden iets omhoog (was 0.502 en 0.565) zodat het BB-getal lucht heeft

def golfje(d, x, y, k, kl):
    """twee golven boven elkaar, k = breedte in px. Geen batterijvorm."""
    w = max(2, round(k * 0.17))
    for dy in (-k * 0.19, k * 0.19):
        pts = [(x - k / 2 + k * i / 16, y + dy - k * 0.13 * math.sin(i / 16 * 2 * math.pi * 1.5)) for i in range(17)]
        d.line(pts, fill=kl, width=w, joint='curve')

def plaat(S, thema, hist, t=0.0):
    zb, zo, uur, mn, tekst, zwak, boot = P.THEMAS[thema]
    im = Image.new('RGB', (S, S), (0, 0, 0)); d = ImageDraw.Draw(im); c = S / 2
    batt = hist[-1]
    nu_x = S * P.NU_X
    while True:
        pts = P.lijn(S, hist, nu_x, t); by = P.hoogte(pts, nu_x)
        romp, zeil, m0, m1 = P.boot_punten(S, nu_x, by + (S * 0.012 if batt < 10 else 0), -22 if batt < 10 else 0)
        if P.past(S, romp + zeil + [m1]) or nu_x < c: break
        nu_x -= S * 0.01
    for i, off in enumerate(P.BANDEN):
        kl = P.lerp(zb, zo, i / (len(P.BANDEN) - 1))
        d.polygon([(x, y + S * off) for x, y in pts] + [(S, S), (0, S)], fill=kl)
    lijnkl = tuple(min(255, v + 70) for v in zb)
    d.line(pts, fill=lijnkl, width=max(2, S // 110), joint='curve')
    d.polygon(romp, fill=boot); d.line([m0, m1], fill=boot, width=max(2, S // 150)); d.polygon(zeil, fill=mn)
    # Body Battery: vaste plek, wit met donkere rand, golfje in de kleur van de waterlijn ernaast
    fb = P.f(S * 0.11); dik = max(2, S // 120); gk = max(12, S * 0.05)
    bw = d.textlength(f'{batt}', font=fb); groep = bw + gk * 0.25 + gk
    nx, ny = c - groep / 2 + bw / 2, S * BB_Y
    P.rand_tekst(d, (nx, ny), f'{batt}', fb, (255, 255, 255), P.lerp(zo, (0, 0, 0), 0.4), dik)
    golfje(d, nx + bw / 2 + gk * 0.75, ny + S * 0.004, gk, lijnkl)
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
    W = 6 * 464 + 10
    blad = Image.new('RGB', (W, 454 + 300 + 80), (30, 30, 30)); d = ImageDraw.Draw(blad)
    for k, (th, h, lab) in enumerate(ST):
        x = 10 + k * 464
        blad.paste(plaat(454, th, h, k), (x, 10))
        d.text((x + 227, 484), f'{th}, {lab}', font=P.f(24, 600), fill=(220, 220, 220), anchor='mm')
        blad.paste(plaat(260, th, h, k), (x + 97, 510))
    d.text((W / 2, 805), 'proef 4: golfje in plaats van batterij, BB-getal vast en midden boven het plafond   boven 454, onder 260 (1x)', font=P.f(22, 500), fill=(160, 160, 160), anchor='mm')
    blad.save(os.path.join(HIER, 'stijlproef-v4-tij.png'))
    u = Image.new('RGB', (3 * 260 * 3 + 40, 3 * 260 + 20), (30, 30, 30))
    for k, i in enumerate((0, 2, 3)):
        u.paste(plaat(260, ST[i][0], ST[i][1], i).resize((780, 780), Image.NEAREST), (10 + k * 790, 10))
    u.save(os.path.join(HIER, 'stijlproef-v4-260-3x.png')); print('klaar')
