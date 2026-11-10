# Ontwerpblad Ebb v1 (Mila, 10 nov run 15): ALLE schermen in de nieuwe stijl, op 454 en 260 px.
# Harde regels (Thijs 20:20 NL): alles in het midden, symmetrisch, inhoud binnen de veilige cirkel (80% van D).
# Alleen MIP-kleuren (kanalen 00, 55, AA, FF), geen verloop. Alle maten als deel van D.
# Gebruik: python3 ebb_blad.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dieren_richting_daan as dr

ZWART=(0,0,0); NACHT=(0,0,85); DIEP=(0,0,170); MID=(0,85,170); TURK=(0,170,255); ZEE=(0,170,170)
LICHT=(0,255,255); SCHUIM=(85,255,255); ZACHT=(85,170,170); BEL=(85,170,255); WIT=(255,255,255)
KORAAL=(255,85,85); LKORAAL=(255,170,170); GEEL=(255,255,170); RING=(0,85,85); BOUT=(85,170,170); GRIJS=(85,85,85)
FONT=None

def f(px, zwaar=False):
    return ImageFont.truetype(FONT, max(8, int(px)))

def golf(D, peil, amp, n=2, fase=0.0):
    """Golfrand, symmetrisch om het midden (cosinus rond x = D/2). peil = y van de waterlijn."""
    pts=[(x, peil + amp*math.cos(2*math.pi*n*(x-D/2)/D + fase)) for x in range(0, D+1, 2)]
    return pts

def water(d, D, peil, kleur, amp=None, n=2, schuim=True):
    amp = D*0.022 if amp is None else amp
    g = golf(D, peil, amp, n)
    d.polygon(g + [(D, D), (0, D)], fill=kleur)
    if schuim: d.line(g, fill=SCHUIM, width=max(2, round(D/110)))
    return g

def rand(d, D):
    """De patrijspoort: ring met acht bouten, buiten de veilige cirkel. Herkenbaar Ebb op elk scherm."""
    w = max(3, round(D*0.035))
    d.ellipse([-D*0.5, -D*0.5, D*1.5, D*1.5], outline=ZWART, width=round(D*0.5))   # het scherm is rond
    d.ellipse([0, 0, D-1, D-1], outline=RING, width=w)
    for k in range(8):
        a = math.pi/8 + k*math.pi/4; r = D/2 - w/2 - 0.5
        x = D/2 + r*math.cos(a); y = D/2 + r*math.sin(a); b = max(1.5, D*0.009)
        d.ellipse([x-b, y-b, x+b, y+b], fill=BOUT)

def tekst(d, xy, t, px, kleur, anker='mm'):
    d.text(xy, t, font=f(px), fill=kleur, anchor=anker)

def getal_gesplitst(im, D, t, px, y, peil_pts, boven=WIT, onder=NACHT):
    """Groot getal dat door de waterlijn snijdt: boven het water wit, in het water nachtblauw.
    In Monkey C: twee keer drawText met setClip boven en onder de golf (rechthoeken per strook van 4 px)."""
    laag = Image.new('L', (D, D), 0); ImageDraw.Draw(laag).text((D/2, y), t, font=f(px), fill=255, anchor='mm')
    masker_water = Image.new('L', (D, D), 0); ImageDraw.Draw(masker_water).polygon(peil_pts + [(D, D), (0, D)], fill=255)
    from PIL import ImageChops
    onder_m = ImageChops.multiply(laag, masker_water); boven_m = ImageChops.subtract(laag, masker_water)
    im.paste(Image.new('RGB', (D, D), boven), (0, 0), boven_m.point(lambda v: 255 if v > 127 else 0))
    im.paste(Image.new('RGB', (D, D), onder), (0, 0), onder_m.point(lambda v: 255 if v > 127 else 0))

def bel(d, x, y, r, kleur=BEL):
    d.ellipse([x-r, y-r, x+r, y+r], outline=kleur, width=max(1, round(r/3)))

# ---------------- walvis v3: Daans richting v2 plus glans op de kop, blaasgat en waterlijnen ----------------
def walvis3(d, cx, cy, e, golfjes=True):
    dr.walvis(d, cx, cy, e)
    _, (mx, my, b, h) = dr.walvis_delen()
    T = lambda x, y: (cx + (x-mx)*e, cy + (y-my)*e)
    # glans op de kop (lichte boog), alleen als hij groot genoeg is om te lezen
    if e >= 2.0:
        pts = [T(-10.6+i*0.55, -3.2 - 1.6*math.sin(i/8*math.pi)) for i in range(9)]
        d.line(pts, fill=LKORAAL, width=max(2, round(e*0.55)))
    if golfjes:   # twee waterlijnen achter de staart: hij zwemt
        for k, (x0, y0, L) in enumerate([(14.0, 1.8, 4.0), (16.0, -0.6, 3.0)]):
            a = T(x0, y0); z = T(x0+L, y0)
            d.line([a, z], fill=BEL, width=max(1, round(e*0.45)))

def kwal(d, cx, cy, s):
    d.pieslice([cx-s, cy-s*0.9, cx+s, cy+s*0.9], 180, 360, fill=KORAAL)
    d.rectangle([cx-s, cy-1, cx+s, cy+s*0.12], fill=KORAAL)
    for i in (-0.6, 0, 0.6):
        x = cx + i*s
        d.line([(x, cy), (x+s*0.15, cy+s*0.45), (x-s*0.1, cy+s*0.8), (x+s*0.1, cy+s*1.1)], fill=KORAAL, width=max(2, round(s/6)))
    r = max(1.2, s*0.14); d.ellipse([cx-s*0.35-r, cy-s*0.35-r, cx-s*0.35+r, cy-s*0.35+r], fill=NACHT)
    d.ellipse([cx+s*0.35-r, cy-s*0.35-r, cx+s*0.35+r, cy-s*0.35+r], fill=NACHT)

def vis(d, cx, cy, s, kleur=KORAAL):
    d.ellipse([cx-s, cy-s*0.6, cx+s*0.7, cy+s*0.6], fill=kleur)
    d.polygon([(cx+s*0.5, cy), (cx+s*1.1, cy-s*0.55), (cx+s*1.1, cy+s*0.55)], fill=kleur)
    r = max(1.2, s*0.14); d.ellipse([cx-s*0.6-r, cy-s*0.15-r, cx-s*0.6+r, cy-s*0.15+r], fill=NACHT)

# ---------------- de tien schermen ----------------
def leeg(D):
    im = Image.new('RGB', (D, D), ZWART); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, D-1, D-1], fill=ZWART)
    return im, d

def s_menu(D):
    im, d = leeg(D)
    water(d, D, D*0.80, NACHT, amp=D*0.015, n=2)            # laag tij onderin: je staat aan de kust
    tekst(d, (D/2, D*0.20), 'Ebb', D*0.10, LICHT)
    # vorige en volgende, klein en gedimd, precies in het midden
    tekst(d, (D/2, D*0.33), 'Calm', D*0.065, GRIJS)
    # geselecteerd: pil, symmetrisch, past binnen de veilige cirkel
    pw, ph = D*0.62, D*0.20; y = D*0.50
    d.rounded_rectangle([D/2-pw/2, y-ph/2, D/2+pw/2, y+ph/2], radius=ph/2, fill=MID)
    tekst(d, (D/2, y-D*0.028), 'Rounds', D*0.085, WIT)
    tekst(d, (D/2, y+D*0.050), '3 x 30 breaths', D*0.050, SCHUIM)
    tekst(d, (D/2, D*0.67), 'Box', D*0.065, ZACHT)
    # drie stippen als plaats in de lijst (geen schuifbalk aan de zijkant)
    for i, k in enumerate((-1, 0, 1)):
        r = D*0.008; x = D/2 + k*D*0.03; yy = D*0.875
        d.ellipse([x-r, yy-r, x+r, yy+r], fill=SCHUIM if k == -1 else ZACHT)
    rand(d, D); return im

def s_ademen(D):
    im, d = leeg(D)
    g = water(d, D, D*0.46, TURK, n=2)
    tekst(d, (D/2, D*0.19), 'in', D*0.085, ZACHT)
    getal_gesplitst(im, D, '23', D*0.34, D*0.47, g)
    d = ImageDraw.Draw(im)
    tekst(d, (D/2, D*0.72), 'of 30  ·  round 2', D*0.058, NACHT)
    rand(d, D); return im

def diepte_banden(d, D, top):
    # drie banden zonder verloop: hoe dieper, hoe donkerder
    water(d, D, top, MID, amp=D*0.015, n=2)
    water(d, D, D*0.50, DIEP, amp=D*0.012, n=3, schuim=False)
    water(d, D, D*0.78, NACHT, amp=D*0.010, n=3, schuim=False)

def s_duiken(D):
    im, d = leeg(D)
    diepte_banden(d, D, D*0.10)
    tekst(d, (D/2, D*0.22), '94 m', D*0.065, SCHUIM)
    tekst(d, (D/2, D*0.44), '1:34', D*0.30, WIT)
    kwal(d, D/2, D*0.70, D*0.065)
    for s in (-1, 1):   # belletjes in paren, gespiegeld
        bel(d, D/2 + s*D*0.25, D*0.60, D*0.020); bel(d, D/2 + s*D*0.29, D*0.47, D*0.013); bel(d, D/2 + s*D*0.24, D*0.36, D*0.009)
    rand(d, D); return im

def s_walvis(D):
    im, d = leeg(D)
    diepte_banden(d, D, D*0.10)
    tekst(d, (D/2, D*0.22), '183 m', D*0.065, SCHUIM)
    tekst(d, (D/2, D*0.44), '3:03', D*0.30, WIT)
    walvis3(d, D/2, D*0.72, D*1.25/100, golfjes=False)
    rand(d, D); return im

def s_boven(D):
    im, d = leeg(D)
    # zon die opkomt achter de golf: je bent boven
    zr = D*0.13; d.ellipse([D/2-zr, D*0.66-zr, D/2+zr, D*0.66+zr], fill=GEEL)
    g = water(d, D, D*0.62, TURK, n=2)
    tekst(d, (D/2, D*0.19), 'breathe in', D*0.075, GEEL)
    tekst(d, (D/2, D*0.37), '15', D*0.24, WIT)
    tekst(d, (D/2, D*0.77), 'held 1:34', D*0.060, NACHT)
    rand(d, D); return im

def s_rustig(D):
    im, d = leeg(D)
    g = water(d, D, D*0.56, ZEE, n=2)
    tekst(d, (D/2, D*0.19), 'hold', D*0.085, ZACHT)
    getal_gesplitst(im, D, '7', D*0.34, D*0.47, g)
    d = ImageDraw.Draw(im)
    tekst(d, (D/2, D*0.75), '4-7-8', D*0.065, NACHT)
    rand(d, D); return im

def profiel_lijn(L, R, opp, diepten, schaal):
    """Doorlopend duikprofiel zoals een duikcomputer: oppervlakte, afdalen, bodem, opstijgen, oppervlakte."""
    n = len(diepten); breed = (R-L)/n; pts = []
    for i, dp in enumerate(diepten):
        x0 = L + i*breed
        for k in range(25):
            t = k/24
            # 15% oppervlakte, dan een zachte kom (cos), dan 15% oppervlakte
            if t < 0.15 or t > 0.85: y = opp
            else:
                u = (t-0.15)/0.70; y = opp + dp*schaal*(0.5-0.5*math.cos(2*math.pi*u))**0.35
            pts.append((x0 + t*breed, y))
    return pts

def s_today(D):
    im, d = leeg(D)
    tekst(d, (D/2, D*0.19), 'today', D*0.070, ZACHT)
    tekst(d, (D/2, D*0.27), '3 rounds', D*0.050, WIT)
    opp = D*0.36; L, R = D*0.15, D*0.85                 # symmetrisch: 15% marge links en rechts
    diepten = [0.63, 1.00, 0.81]; schaal = D*0.30
    pts = profiel_lijn(L, R, opp, diepten, schaal)
    # vlak in drie diepteband-tinten, zonder verloop (zoals het duikscherm)
    vlak = Image.new('L', (D, D), 0); ImageDraw.Draw(vlak).polygon(pts + [(R, opp), (L, opp)], fill=255)
    for kleur, y0 in ((MID, opp), (DIEP, opp + schaal*0.45), (NACHT, opp + schaal*0.80)):
        band = Image.new('L', (D, D), 0); ImageDraw.Draw(band).rectangle([0, y0, D, D], fill=255)
        from PIL import ImageChops
        im.paste(Image.new('RGB', (D, D), kleur), (0, 0), ImageChops.multiply(vlak, band))
    d = ImageDraw.Draw(im)
    d.line(pts, fill=TURK, width=max(2, round(D/150)))
    d.line([(L, opp), (R, opp)], fill=SCHUIM, width=max(2, round(D/110)))
    xm = L + (R-L)/2; y1 = opp + schaal; r = D*0.022
    d.ellipse([xm-r, y1-r, xm+r, y1+r], fill=KORAAL)
    tekst(d, (D/2, D*0.78), '2:08 new best', D*0.062, KORAAL)
    rand(d, D); return im

def s_weken(D):
    im, d = leeg(D)
    tekst(d, (D/2, D*0.19), '8 weeks', D*0.070, ZACHT)
    L, R, top, bod = D*0.16, D*0.84, D*0.35, D*0.66      # symmetrisch, ver binnen de rand
    # voorbeeld: langzaam stijgende inhoudtijd met golfjes (zo ziet een echt getij eruit)
    best = []
    for i in range(56):
        v = 0.30 + 0.55*min(i, 48)/48 - 0.012*max(0, i-48) + 0.06*math.sin(i*0.45)
        best.append(None if i in (9, 10, 23, 37, 38) else min(1, v))
    hoog = max(b for b in best if b); best = [b/hoog if b else None for b in best]
    dx = (R-L)/55; Y = lambda v: bod - v*(bod-top)
    gem = []
    for i in range(56):
        w = [b for b in best[max(0, i-6):i+1] if b]; gem.append(sum(w)/len(w)*0.80)
    poly = [(L+i*dx, Y(g)) for i, g in enumerate(gem)]
    d.polygon(poly + [(R, bod), (L, bod)], fill=DIEP)
    d.line(poly, fill=MID, width=max(2, round(D/150)))
    seg = []
    for i, b in enumerate(best + [None]):
        if b is None:
            if len(seg) > 1: d.line(seg, fill=SCHUIM, width=max(2, round(D/110)), joint='curve')
            seg = []; continue
        seg.append((L+i*dx, Y(b)))
    d.line([(L, bod), (R, bod)], fill=MID, width=max(1, round(D/230)))
    for w in range(9):  # weekstreepjes, ook op beide uiteinden: het kader is symmetrisch
        x = L + w*7*dx if w < 8 else R
        d.line([(x, bod), (x, bod+D*0.018)], fill=ZACHT, width=max(1, round(D/230)))
    i = max(range(56), key=lambda k: best[k] or 0); r = D*0.020
    d.ellipse([L+i*dx-r, Y(1.0)-r, L+i*dx+r, Y(1.0)+r], fill=KORAAL)
    tekst(d, (D/2, D*0.765), 'best 2:08', D*0.070, WIT)
    tekst(d, (D/2, D*0.845), '44 days', D*0.048, ZACHT)
    rand(d, D); return im

def s_zeelog(D):
    im, d = leeg(D)
    tekst(d, (D/2, D*0.19), 'sea log', D*0.070, ZACHT)
    tekst(d, (D/2, D*0.265), '3 of 4 met', D*0.048, SCHUIM)
    # 2 x 2 rooster, symmetrisch: elk dier in een eigen patrijspoortje, tijd eronder
    vakken = [(-1, -1, 'vis', '1:00'), (1, -1, 'kwal', '1:30'), (-1, 1, 'schildpad', '2:00'), (1, 1, 'walvis', '3:00')]
    for sx, sy, dier, t in vakken:
        cx = D/2 + sx*D*0.15; cy = D*0.50 + sy*D*0.13 - D*0.02; r = D*0.085
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=NACHT, outline=MID, width=max(2, round(D/150)))
        if dier == 'vis': vis(d, cx, cy, r*0.55)
        elif dier == 'kwal': kwal(d, cx, cy+r*0.05, r*0.45)
        elif dier == 'schildpad': dr.schildpad(d, cx, cy, r*0.78/9)
        else:   # nog niet ontmoet: silhouet en een vraagteken
            tekst(d, (cx, cy), '?', r*1.1, MID)
        tekst(d, (cx, cy + r + D*0.032), t, D*0.050, WIT if dier != 'walvis' else ZACHT)
    rand(d, D); return im

def s_instellingen(D):
    im, d = leeg(D)
    tekst(d, (D/2, D*0.20), 'settings', D*0.070, ZACHT)
    tekst(d, (D/2, D*0.33), 'Rounds  3', D*0.060, GRIJS)
    pw, ph = D*0.62, D*0.17; y = D*0.50
    d.rounded_rectangle([D/2-pw/2, y-ph/2, D/2+pw/2, y+ph/2], radius=ph/2, fill=MID)
    tekst(d, (D/2, y-D*0.022), 'Breaths', D*0.070, WIT)
    tekst(d, (D/2, y+D*0.043), '< 30 >', D*0.050, SCHUIM)
    tekst(d, (D/2, D*0.66), 'Buzz  on', D*0.060, ZACHT)
    tekst(d, (D/2, D*0.75), 'My pattern', D*0.060, ZACHT)
    rand(d, D); return im

def s_veilig(D):
    im, d = leeg(D)
    water(d, D, D*0.82, NACHT, amp=D*0.015, n=2)
    # waarschuwingsteken in koraal, gecentreerd
    s = D*0.09; y = D*0.22
    d.polygon([(D/2, y-s*0.75), (D/2+s*0.85, y+s*0.65), (D/2-s*0.85, y+s*0.65)], fill=KORAAL)
    tekst(d, (D/2, y+s*0.12), '!', s*0.95, NACHT)
    for i, t in enumerate(['Never in water.', 'Never driving.', 'Sit or lie down.']):
        tekst(d, (D/2, D*(0.40 + i*0.09)), t, D*0.068, WIT if i < 2 else ZACHT)
    pw, ph = D*0.36, D*0.11; yb = D*0.70
    d.rounded_rectangle([D/2-pw/2, yb-ph/2, D/2+pw/2, yb+ph/2], radius=ph/2, fill=MID)
    tekst(d, (D/2, yb), 'OK', D*0.065, WIT)
    rand(d, D); return im

def s_icoon(D):
    """Grote walvis v3 in de patrijspoort (loep, icoon, kaart 2)."""
    im, d = leeg(D)
    c = D/2; R = D*0.47; r = D*0.38
    d.ellipse([c-R, c-R, c+R, c+R], fill=(0, 85, 85)); d.ellipse([c-r, c-r, c+r, c+r], fill=DIEP)
    _, (mx, my, b, h) = dr.walvis_delen()
    e = (2*r*0.70)/b
    walvis3(d, c, c, e, golfjes=False)
    for k in range(8):
        a = math.pi/8 + k*math.pi/4; bx = c+R*0.9*math.cos(a); by = c+R*0.9*math.sin(a); q = D*0.018
        d.ellipse([bx-q, by-q, bx+q, by+q], fill=BOUT)
    return im

SCHERMEN = [('1 menu', s_menu), ('2 ademen', s_ademen), ('3 duiken', s_duiken), ('3b walvis 3:03', s_walvis),
            ('4 boven', s_boven), ('5 rustig 4-7-8', s_rustig), ('6 today', s_today), ('7 8 weeks', s_weken),
            ('8 sea log', s_zeelog), ('9 settings', s_instellingen), ('10 veiligheid', s_veilig)]

# ---------------- nameten: midden en veilige cirkel ----------------
def meet(im, D):
    """Horizontaal zwaartepunt van alles wat geen achtergrond is (binnen de ring), en het verste punt van
    tekst en figuren (wit, koraal, geel, schuim-tekst) vanaf het midden, als deel van de straal."""
    px = im.load(); som = 0; n = 0; verst = 0; c = D/2; xs = []
    figuur = {WIT, KORAAL, LKORAAL, GEEL}
    for y in range(D):
        for x in range(D):
            r = math.hypot(x+0.5-c, y+0.5-c)
            if r > D*0.46: continue
            p = px[x, y]
            if p != ZWART and p != RING and p != BOUT: som += x+0.5; n += 1; xs.append(x)
            if p in figuur: verst = max(verst, r/(D/2))
    kader = (min(xs)+max(xs)+1)/2 - c if xs else 0
    return (som/n - c) if n else 0, verst, kader

def maak(uit):
    os.makedirs(uit, exist_ok=True)
    rapport = []
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = fn(D); im.save(f'{uit}/ebb-blad-{naam.split()[0]}-{D}.png')
            dx, verst, kader = meet(im, D)
            rapport.append((D, naam, dx, verst, kader))
    s_icoon(560).save(f'{uit}/ebb-walvis-v3-patrijspoort.png')
    # het blad: rij 454, rij 260, en de walvis groot
    gap = 24; kol = 6
    W = gap + kol*(454+gap); rij454 = (len(SCHERMEN)+kol-1)//kol
    H = 90 + rij454*(454+60) + 2*(260+56) + 40
    blad = Image.new('RGB', (W, H), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 26), 'Ebb ontwerpblad v1 (Mila): alle schermen, 454 px en 260 px op ware grootte, alles in het midden',
           font=f(36), fill=(220, 230, 240))
    y = 90
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, kol); x = gap + k*(454+gap); yy = y + r*(454+60)
        blad.paste(fn(454), (x, yy)); d.text((x, yy+460), naam, font=f(26), fill=(170, 190, 210))
    k = len(SCHERMEN) % kol
    blad.paste(s_icoon(454), (gap + k*(454+gap), y + (rij454-1)*(454+60)))
    d.text((gap + k*(454+gap), y + (rij454-1)*(454+60)+460), 'walvis v3 (icoon en loep)', font=f(26), fill=(170, 190, 210))
    y += rij454*(454+60)
    per = 9
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, per); x = gap + k*(260+40); yy = y + r*(260+56)
        blad.paste(fn(260), (x, yy)); d.text((x, yy+262), naam, font=f(22), fill=(170, 190, 210))
    blad.save(f'{uit}/ebb-ontwerpblad-v1.png')
    return rapport

if __name__ == '__main__':
    FONT = sys.argv[2]
    for D, naam, dx, verst, kader in maak(sys.argv[1]):
        print(f'{D:4d}  {naam:16s}  zwaartepunt x {dx:+6.2f} px  kader x {kader:+5.1f} px  verste tekst/figuur {verst*100:4.1f}% van de straal')
