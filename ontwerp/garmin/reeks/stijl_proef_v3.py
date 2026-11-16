# Reeks datawijzerplaten, stijlproef 3 "Tij" (Mila, 16 nov 2026). De waterlijn is het verloop van je
# Body Battery van de laatste uren (links = toen, bij het bootje = nu). Rechts van het bootje ligt de zee
# vlak op het nu. Zonder geschiedenis: de vlakke golvende zee van proef 2.
# Moets van Daan (16 nov 21:45): icoontjes van minstens 8 px op 260, bootje altijd binnen de cirkel,
# plafond bij 100 en kleinste zee bij 0, lijn ook met 1 tot 2 uur, geen pijltje (de lijn zegt het al).
# Zee als 4 getekende banden die de waterlijn volgen, geen plaatje. Nep-gegevens.  python3 stijl_proef_v3.py
import math, os
from PIL import Image, ImageDraw, ImageFont
HIER = os.path.dirname(os.path.abspath(__file__))
LET = os.path.join(HIER, 'BigShouldersDisplay.ttf')

def f(s, w=900):
    ft = ImageFont.truetype(LET, max(6, int(s)))
    try: ft.set_variation_by_axes([w])
    except Exception: pass
    return ft

THEMAS = {  # zee boven, zee onder, uren, minuten, tekst, zwak, boot
    'Dusk':  ((255, 140, 60), (110, 25, 40), (255, 238, 214), (255, 170, 80), (255, 226, 190), (150, 104, 76), (255, 246, 230)),
    'Tide':  ((40, 200, 220), (8, 36, 84), (225, 248, 255), (60, 220, 230), (200, 236, 245), (80, 128, 150), (255, 255, 255)),
    'Kelp':  ((150, 210, 60), (18, 56, 28), (236, 244, 220), (170, 225, 70), (220, 232, 200), (110, 132, 84), (255, 250, 230)),
    'Night': ((90, 110, 255), (18, 10, 56), (240, 240, 255), (150, 160, 255), (220, 220, 245), (110, 110, 160), (255, 220, 120)),
}

# Maten als deel van de schermbreedte S (zelfde getallen gaan naar het blad voor Gijs)
TOP, BODEM = 0.70, 0.895      # waterhoogte bij 100 en bij 0 (plafond en kleinste zee)
NU_X = 0.70                   # waar "nu" (het bootje) staat, schuift naar links als het niet past
LINKS_X = 0.04                # begin van de lijn (de rand snijdt hem af, dat geeft niets)
BANDEN = (0.0, 0.035, 0.08, 0.14)
VEILIG = 0.475                # straal waarbinnen het bootje moet blijven

def lerp(a, b, k): return tuple(int(a[i] * (1 - k) + b[i] * k) for i in range(3))

def niveau(S, b): return S * (BODEM - (BODEM - TOP) * max(0, min(100, b)) / 100)

def lijn(S, hist, nu_x, t):
    """punten van de waterlijn, hooguit 64. hist = waarden van oud naar nieuw (laatste = nu)."""
    x0 = S * LINKS_X
    if len(hist) < 2:  # vlakke zee met golfje
        y = niveau(S, hist[-1])
        return [(x0 + (S - x0) * i / 40, y + S * 0.012 * math.sin(i / 40 * 2 * math.pi * 2.2 + t)) for i in range(41)]
    n = 48; pts = []
    for i in range(n + 1):  # tijd uitgerekt over de breedte, zacht tussen de meetpunten (cosinus)
        u = i / n * (len(hist) - 1); a = int(u); b = min(a + 1, len(hist) - 1); k = (1 - math.cos((u - a) * math.pi)) / 2
        pts.append((x0 + (nu_x - x0) * i / n, niveau(S, hist[a] * (1 - k) + hist[b] * k)))
    y = pts[-1][1]
    pts += [(nu_x + (S - nu_x) * i / 6, y + S * 0.006 * math.sin(i * 1.6 + t)) for i in range(1, 7)]
    return pts

def hoogte(pts, x):
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        if ax <= x <= bx: return ay + (by - ay) * (x - ax) / max(1e-6, bx - ax)
    return pts[-1][1]

def boot_punten(S, bx, by, hoek=0.0):
    """hoek in graden: bij bijna lege batterij ligt het bootje scheef aan de grond (de grap)."""
    s = S * 0.05; a = math.radians(hoek)
    r = lambda px, py: (bx + px * math.cos(a) - py * math.sin(a), by + px * math.sin(a) + py * math.cos(a))
    romp = [r(-s, -s * 0.15), r(s, -s * 0.15), r(s * 0.6, s * 0.35), r(-s * 0.6, s * 0.35)]
    zeil = [r(s * 0.08, -s * 1.45), r(s * 0.08, -s * 0.35), r(s * 0.85, -s * 0.35)]
    return romp, zeil, r(0, -s * 0.15), r(0, -s * 1.5)

def past(S, pts):
    c = S / 2
    return all(math.hypot(x - c, y - c) <= S * VEILIG for x, y in pts)

# icoontjes, maat k = hoogte in px
def hart(d, x, y, k, kl):
    r = k * 0.28
    d.ellipse([x - 2 * r, y - k * 0.42, x, y - k * 0.42 + 2 * r], fill=kl)
    d.ellipse([x, y - k * 0.42, x + 2 * r, y - k * 0.42 + 2 * r], fill=kl)
    d.polygon([(x - 2 * r + 0.3, y - k * 0.1), (x + 2 * r - 0.3, y - k * 0.1), (x, y + k * 0.5)], fill=kl)
def bliksem(d, x, y, k, kl):  # breed en kort, zodat hij op 260 geen streepje wordt
    d.polygon([(x + k * 0.05, y - k * 0.5), (x + k * 0.4, y - k * 0.5), (x + k * 0.12, y - k * 0.08), (x + k * 0.38, y - k * 0.08),
               (x - k * 0.2, y + k * 0.55), (x - k * 0.02, y + k * 0.1), (x - k * 0.3, y + k * 0.1)], fill=kl)
def voet(d, x, y, k, kl):  # twee schoenzolen schuin achter elkaar, met een gat tussen bal en hak
    for dx, dy in ((-0.26, 0.08), (0.24, -0.1)):
        cx, cy = x + k * dx, y + k * dy
        d.ellipse([cx - k * 0.2, cy - k * 0.45, cx + k * 0.2, cy + k * 0.12], fill=kl)
        d.ellipse([cx - k * 0.15, cy + k * 0.2, cx + k * 0.15, cy + k * 0.45], fill=kl)
def batterij(d, x, y, k, kl, vul):
    w = max(1, round(k * 0.13))
    d.rectangle([x - k * 0.55, y - k * 0.3, x + k * 0.45, y + k * 0.3], outline=kl, width=w)
    d.rectangle([x + k * 0.45, y - k * 0.12, x + k * 0.6, y + k * 0.12], fill=kl)
    if vul > 0: d.rectangle([x - k * 0.55 + 2 * w, y - k * 0.3 + 2 * w, x - k * 0.55 + 2 * w + (k - 4 * w) * vul / 100, y + k * 0.3 - 2 * w], fill=kl)

def rand_tekst(d, xy, s, font, kl, rand, dik):
    d.text(xy, s, font=font, fill=kl, anchor='mm', stroke_width=dik, stroke_fill=rand)

def plaat(S, thema, hist, t=0.0):
    zb, zo, uur, mn, tekst, zwak, boot = THEMAS[thema]
    im = Image.new('RGB', (S, S), (0, 0, 0)); d = ImageDraw.Draw(im); c = S / 2
    batt = hist[-1]
    # waar staat nu: zo ver rechts als het bootje binnen de veilige cirkel past
    nu_x = S * NU_X
    while True:
        pts = lijn(S, hist, nu_x, t); by = hoogte(pts, nu_x)
        romp, zeil, m0, m1 = boot_punten(S, nu_x, by + (S * 0.012 if batt < 10 else 0), -22 if batt < 10 else 0)
        if past(S, romp + zeil + [m1]) or nu_x < c: break
        nu_x -= S * 0.01
    # zee: 4 banden die de waterlijn volgen
    for i, off in enumerate(BANDEN):
        kl = lerp(zb, zo, i / (len(BANDEN) - 1))
        d.polygon([(x, y + S * off) for x, y in pts] + [(S, S), (0, S)], fill=kl)
    d.line(pts, fill=tuple(min(255, v + 70) for v in zb), width=max(2, S // 110), joint='curve')
    # bootje op het nu
    d.polygon(romp, fill=boot); d.line([m0, m1], fill=boot, width=max(2, S // 150)); d.polygon(zeil, fill=mn)
    # Body Battery: getal met donkere rand, in de zee als er plek is, anders erboven
    nx = c - S * 0.13; wy = hoogte(pts, nx); fb = f(S * 0.11); dik = max(1, S // 120)
    if S * 0.955 - wy > S * 0.15: ny = wy + S * 0.095
    else: ny = wy - S * 0.07
    ny = min(ny, S * 0.86)
    rand_tekst(d, (nx, ny), f'{batt}', fb, (255, 255, 255), lerp(zo, (0, 0, 0), 0.4), dik)
    bw = d.textlength(f'{batt}', font=fb)
    ik = max(9, S * 0.042)
    batterij(d, nx + bw / 2 + ik * 0.85, ny, ik, (255, 255, 255), batt)
    # tijd en datum
    d.text((c, S * 0.13), 'MON 16', font=f(S * 0.065, 700), fill=tekst, anchor='mm')
    ft = f(S * 0.30); x = c - d.textlength('7:42', font=ft) / 2; y = S * 0.30
    for deel, kl in (('7', uur), (':', zwak), ('42', mn)):
        d.text((x, y), deel, font=ft, fill=kl, anchor='lm'); x += d.textlength(deel, font=ft)
    # drie velden met icoontjes (op 260 minstens 9 px hoog)
    ik = max(12, S * 0.04)
    for k, (tek, val) in enumerate([(hart, '58'), (bliksem, '24'), (voet, '8.4K')]):
        gx = c + (k - 1) * S * 0.22
        tek(d, gx, S * 0.502, ik, mn if tek is hart else tekst)
        d.text((gx, S * 0.565), val, font=f(S * 0.065, 800), fill=tekst, anchor='mm')
    m = Image.new('L', (S, S), 0); ImageDraw.Draw(m).ellipse([0, 0, S - 1, S - 1], fill=255)
    out = Image.new('RGB', (S, S), (40, 40, 40)); out.paste(im, (0, 0), m)
    return out

# standen om te toetsen
NACHT = [62, 58, 52, 47, 44, 52, 66, 80, 88, 85, 78, 72]          # 12 metingen (±6 uur): slaap, dan zakken
STANDEN = [
    ('Dusk', NACHT, '72, ±6 uur gegevens'),
    ('Tide', [41, 38, 35], '35, maar 1,5 uur'),
    ('Kelp', [80, 86, 93, 98, 100, 100], '100, plafond'),
    ('Night', [30, 22, 15, 9, 4, 2], '2, kleinste zee'),
    ('Tide', [55], '55, geen geschiedenis'),
    ('Night', [12, 12], '12, vlak 1 uur'),
]

if __name__ == '__main__':
    W = 6 * 464 + 10
    blad = Image.new('RGB', (W, 454 + 300 + 80), (30, 30, 30)); d = ImageDraw.Draw(blad)
    for k, (th, h, lab) in enumerate(STANDEN):
        x = 10 + k * 464
        blad.paste(plaat(454, th, h, k), (x, 10))
        d.text((x + 227, 484), f'{th}, {lab}', font=f(24, 600), fill=(220, 220, 220), anchor='mm')
        blad.paste(plaat(260, th, h, k), (x + 97, 510))
    d.text((W / 2, 805), 'boven: AMOLED 454   onder: 260 op ware grootte (1x)', font=f(22, 500), fill=(160, 160, 160), anchor='mm')
    blad.save(os.path.join(HIER, 'stijlproef-v3-tij.png'))
    # uitsnede 260 op 3x, om de icoontjes te keuren
    u = Image.new('RGB', (3 * 260 * 3 + 40, 3 * 260 + 20), (30, 30, 30))
    for k, i in enumerate((0, 2, 3)):
        u.paste(plaat(260, STANDEN[i][0], STANDEN[i][1], i).resize((780, 780), Image.NEAREST), (10 + k * 790, 10))
    u.save(os.path.join(HIER, 'stijlproef-v3-260-3x.png')); print('klaar')
