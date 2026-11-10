# Ontwerpblad Ebb v2 (Mila, 10 nov run 17): ronde 2 na de frisse keuring (5/10, tien moet-punten).
# Wat anders is dan v1: dunne ring zonder bouten, één waterschaal van 4 blauwtinten met dithering tussen de banden,
# getal nooit meer in de golf, kleinste tekst 12 px kapitaalhoogte op 260, grijs #AAAAAA, vier dieren in één stijl
# en optisch gecentreerd op hun zwaartepunt, sea log op gelijke kolommen en gelijk gewicht, today als drie U-duiken.
# Alleen MIP-kleuren (kanalen 00, 55, AA, FF). Alle maten als deel van D.
# Gebruik: python3 ebb_blad_v2.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageChops

ZWART=(0,0,0); WIT=(255,255,255); GRIJS=(170,170,170); SCHUIM=(85,255,255); RING=(0,85,85)
# één waterschaal, van ondiep naar diep (moet-punt 5)
W0=(0,170,255); W1=(0,85,170); W2=(0,0,170); W3=(0,0,85)
GEEL=(255,255,170); KORAAL=(255,85,85); DONKERROOD=(170,0,0)
GOUD=(255,170,0)       # record (keuring 2): rood alleen nog voor gevaar
HINT=(170,255,255)     # knophint bij START, telt niet mee in de midden-meting (hoort bij de knop, niet bij het scherm)
TITEL = SCHUIM          # één titelkleur voor alle fasewoorden en schermtitels (kan-punt 1)
MIN = 17/260            # kleinste letter: 17 px op 260 = 12 px kapitaalhoogte (moet-punt 2)
FONT = None
LOG = []                # (D, tekst, px) om na te meten

def f(px): return ImageFont.truetype(FONT, int(round(px)))

def tekst(d, D, xy, t, px, kleur, anker='mm'):
    px = max(px, MIN*D)
    LOG.append((D, t, int(round(px))))
    d.fontmode = '1'   # harde randen, zoals het horloge tekent (keuring 2, moet-punt 1)
    d.text(xy, t, font=f(px), fill=kleur, anchor=anker)

# ---------------- water ----------------
def golf(D, peil, amp, n=2, fase=0.0):
    return [(x, peil + amp*math.cos(2*math.pi*n*(x-D/2)/D + fase)) for x in range(0, D+1, 2)]

def masker_onder(D, pts):
    m = Image.new('L', (D, D), 0); ImageDraw.Draw(m).polygon(pts + [(D, D), (0, D)], fill=255); return m

def schaakbord(D, dichtheid):
    y, x = np.mgrid[0:D, 0:D]
    if dichtheid == 50: a = ((x + y) % 2 == 0)
    else: a = ((x % 2 == 0) & (y % 2 == 0))         # 25%
    return Image.fromarray((a*255).astype('uint8'))

def zee(im, D, banden, amp=None, n=2, schuim=True):
    """banden = [(peil, kleur), ...] van boven naar beneden. Tussen twee banden twee rijen dithering
    (25% en 50%), zodat de diepte zacht overloopt zonder verloop (kan-punt 2, alleen MIP-kleuren)."""
    amp = D*0.018 if amp is None else amp
    h = max(2, round(D/120))
    eerste = None
    for k, (peil, kleur) in enumerate(banden):
        g = golf(D, peil, amp*(1 if k == 0 else 0.6), n if k == 0 else n+1, 0 if k == 0 else 0.8*k)
        vol = Image.new('RGB', (D, D), kleur)
        if k > 0 and D < 300:   # dithering alleen op MIP; op AMOLED (454) vlakke banden, anders flikkert het
            for stap, dicht in ((2, 25), (1, 50)):
                gm = masker_onder(D, [(x, y - stap*h) for x, y in g])
                im.paste(vol, (0, 0), ImageChops.multiply(gm, schaakbord(D, dicht)))
        im.paste(vol, (0, 0), masker_onder(D, g))
        if k == 0: eerste = g
    if schuim: ImageDraw.Draw(im).line(eerste, fill=SCHUIM, width=max(2, round(D/150)))
    return eerste

def rand(im, D):
    """Dunne ring zonder bouten (moet-punt 4): 3 px op 454, 2 px op 260. Buiten de ring is het scherm zwart."""
    d = ImageDraw.Draw(im)
    d.ellipse([-D*0.5, -D*0.5, D*1.5, D*1.5], outline=ZWART, width=round(D*0.5))
    d.ellipse([0, 0, D-1, D-1], outline=RING, width=max(2, round(D/150)))

def leeg(D): return Image.new('RGB', (D, D), ZWART)

# ---------------- dieren: één stijl (moet-punt 6) ----------------
# Regels: gevulde vlakken, geen lijnen; lichaam in de eigen tint, buik een tint lichter, vin of poot een tint donkerder;
# hetzelfde oog bij elk dier (wit rondje 0,13 eenheid met nachtblauwe pupil, glansje linksboven);
# alle dieren kijken naar links; lengte 2 eenheden. Elk dier een eigen tint binnen koraal.
TINT = {'walvis': ((255,85,85), (255,170,170), (170,0,0)),
        'vis':    ((255,170,85), (255,255,170), (255,85,0)),
        'kwal':   ((255,85,170), (255,170,255), (170,0,85)),
        'pad':    ((255,85,0),  (255,170,85),  (170,0,0))}

def bez(p0, p1, p2, n=10):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]

def ellips(cx, cy, rx, ry, a0=0, a1=360, n=40):
    return [(cx + rx*math.cos(math.radians(a0 + (a1-a0)*i/n)), cy + ry*math.sin(math.radians(a0 + (a1-a0)*i/n))) for i in range(n+1)]

def walvis_h(u):
    # grote ronde kop voorop, dunne staartsteel achteraan (tekenfilmwalvis)
    return 0.40/0.62 * (u**0.18) * ((1-u)**0.85) + 0.05*u

def walvis_lijf():
    top, bod = [], []
    for i in range(41):
        u = i/40; x = -1 + 1.75*u; h = walvis_h(u)
        top.append((x, -h*1.15)); bod.append((x, h*0.85))
    return top + bod[::-1]

def walvis_buik():
    """Buik: het deel van het lijf onder een zachte lijn, in de lichte tint."""
    boven, onder = [], []
    for i in range(41):
        u = i/40; x = -1 + 1.75*u; h = walvis_h(u)*0.85; yb = 0.10 + 0.04*u
        if h > yb + 0.01: boven.append((x, yb)); onder.append((x, h))
    return boven + onder[::-1]

def dier_delen(soort):
    """Lijst van (veelhoek, rol) in eenheden; rol = 'lijf', 'licht', 'donker'. Plus ogen [(x, y)]."""
    if soort == 'walvis':
        lijf = walvis_lijf()
        staart = [(0.66,-0.06),(0.84,-0.12),(0.98,-0.36),(1.06,-0.33),(0.95,-0.02),(1.06,0.24),(0.99,0.28),(0.84,0.09),(0.66,0.07)]
        buik = walvis_buik()
        vin = bez((-0.42,0.24),(-0.14,0.26),(0.02,0.50),6) + bez((0.02,0.50),(-0.08,0.54),(-0.34,0.38),4)
        bek = bez((-0.99,0.06),(-0.85,0.16),(-0.66,0.06),6) + bez((-0.66,0.06),(-0.70,0.13),(-0.99,0.12),6)
        return [(staart,'lijf'), (lijf,'lijf'), (buik,'licht'), (vin,'lijf'), (bek,'donker')], [(-0.62,-0.12)]
    if soort == 'vis':
        lijf = ellips(-0.22, 0, 0.78, 0.50)
        staart = [(0.40,0),(1.0,-0.48),(0.86,0),(1.0,0.48)]
        buik = ellips(-0.22, 0, 0.78, 0.50, 20, 160)
        vin = bez((-0.35,-0.42),(0.0,-0.78),(0.30,-0.40),6)
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht'), (vin,'donker')], [(-0.62,-0.10)]
    if soort == 'kwal':
        kap = ellips(0, 0, 0.80, 0.78, 180, 360) + [(0.80,0.12),(-0.80,0.12)]
        rand_ = [(-0.80,0.0),(0.80,0.0),(0.80,0.16),(-0.80,0.16)]
        armen = []
        for x0 in (-0.48, 0.0, 0.48):
            l = [(x0-0.08+0.09*math.sin(t*2.6), 0.16+t) for t in [i/10*0.85 for i in range(11)]]
            r = [(x+0.16, y) for x, y in l]
            armen.append((l + r[::-1], 'donker'))
        return armen + [(kap,'lijf'), (rand_,'licht')], [(-0.28,-0.28), (0.28,-0.28)]
    if soort == 'pad':
        schild = ellips(0.08, 0.10, 0.62, 0.72, 180, 360) + [(0.70,0.10),(-0.54,0.10)]
        buik = [(-0.60,0.06),(0.76,0.06),(0.64,0.24),(-0.48,0.24)]
        kop = ellips(-0.74, -0.02, 0.26, 0.21)
        voor = bez((-0.42,0.14),(-0.10,0.26),(0.02,0.58),6) + bez((0.02,0.58),(-0.14,0.62),(-0.46,0.30),4)
        achter = bez((0.46,0.16),(0.74,0.22),(0.86,0.44),5) + bez((0.86,0.44),(0.64,0.46),(0.40,0.26),4)
        vlek = [ (ellips(x, y, r, r*0.85), 'licht') for x, y, r in ((0.08,-0.30,0.17),(-0.28,-0.12,0.12),(0.44,-0.12,0.12)) ]
        return [(achter,'donker'), (voor,'donker'), (kop,'lijf'), (schild,'lijf'), (buik,'licht')] + vlek, [(-0.80,-0.06)]

def dier_beeld(soort, s, kleur_override=None, hoek=0):
    """Tekent het dier op een eigen laag (RGBA) met schaal s px per eenheid. Geeft beeld en zwaartepunt."""
    delen, ogen = dier_delen(soort)
    if hoek:   # de punten draaien (niet het beeld), zo blijven de randen even strak als op het horloge
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    lijf, licht, donker = TINT[soort]
    if kleur_override: lijf = licht = donker = kleur_override
    W = int(s*2.6) + 4; c = W/2
    im = Image.new('RGBA', (W, W), (0,0,0,0)); d = ImageDraw.Draw(im)
    rol = {'lijf': lijf, 'licht': licht, 'donker': donker}
    for pts, r in delen:
        d.polygon([(c + x*s, c + y*s) for x, y in pts], fill=rol[r] + (255,))
    if not kleur_override:
        for ox, oy in ogen:
            R = max(2.0, 0.13*s); p = max(1.2, 0.07*s)
            x, y = c + ox*s, c + oy*s
            d.ellipse([x-R, y-R, x+R, y+R], fill=WIT + (255,))
            d.ellipse([x-p-R*0.3, y-p, x+p-R*0.3, y+p], fill=W3 + (255,))
            if s >= 30:
                g = max(1, 0.035*s); d.ellipse([x-R*0.55-g, y-R*0.5-g, x-R*0.55+g, y-R*0.5+g], fill=WIT + (255,))
    a = np.array(im)[:, :, 3] > 0
    ys, xs = np.nonzero(a)
    return im, (xs.mean() + 0.5, ys.mean() + 0.5), a.sum()

def dier(im, soort, cx, cy, s, kleur=None, hoek=0):
    """Plaatst het dier met zijn ZWAARTEPUNT op (cx, cy): optisch midden (moet-punt 7).
    hoek: houding in graden (positief = kop omlaag, dalen; negatief = kop omhoog, stijgen). Kan-punt 3."""
    laag, (zx, zy), _ = dier_beeld(soort, s, kleur, hoek)
    im.paste(laag, (int(round(cx - zx)), int(round(cy - zy))), laag)
    return laag, (zx, zy)

def schaal_voor_gewicht(soort, oppervlak):
    _, _, a1 = dier_beeld(soort, 40)
    return 40*math.sqrt(oppervlak/a1)

def spuit(d, D, x, y, s):
    """Waterstraal, alleen aan de oppervlakte (moet-punt 6): drie gevulde druppels."""
    for dx, dy, r in ((-0.22, -0.30, 0.10), (0.0, -0.42, 0.12), (0.22, -0.30, 0.10)):
        cx, cy = x + dx*s, y + dy*s; R = r*s
        d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=SCHUIM)

def bellen(d, D, lijst):
    """Belletjes in verschillende maten en niet gespiegeld (kan-punt 5). lijst = [(x, y, r)] als deel van D."""
    for x, y, r in lijst:
        R = r*D; w = max(1, round(R/3))
        d.ellipse([x*D-R, y*D-R, x*D+R, y*D+R], outline=(85,170,255), width=w)

# ---------------- schermen ----------------
def pil(d, D, y, w, h, kleur=W1):
    d.rounded_rectangle([D/2-w*D/2, y*D-h*D/2, D/2+w*D/2, y*D+h*D/2], radius=h*D/2, fill=kleur)

def startknop(d, D):
    """Garmin-hint bij de START-knop: korte boog rechtsboven op 30 graden, waar gebruikers hem kennen."""
    w = max(3, round(D/90)); m = w
    d.arc([m, m, D-1-m, D-1-m], -38, -22, fill=HINT, width=w)

def s_menu(D):
    im = leeg(D)
    s = D*0.11
    dier(im, 'walvis', D/2, D*0.865, s)                        # walvis komt boven in het lage tij, kleiner en lager
    d = ImageDraw.Draw(im)
    spuit(d, D, D/2 - 0.36*s, D*0.865 - 0.42*s, s)
    zee(im, D, [(D*0.872, W1), (D*0.94, W2)], amp=D*0.008)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.19), 'Ebb', D*0.11, TITEL)
    tekst(d, D, (D/2, D*0.335), 'Calm', D*0.066, GRIJS)
    pil(d, D, 0.495, 0.64, 0.22)
    tekst(d, D, (D/2, D*0.465), 'Rounds', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.550), '3 x 30', D*0.066, SCHUIM)
    tekst(d, D, (D/2, D*0.655), 'Box', D*0.066, GRIJS)
    startknop(d, D)
    rand(im, D); return im
def s_ademen(D):
    im = leeg(D)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'breathe in', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.41), '23', D*0.32, WIT)           # getal helemaal boven het water (moet-punt 1)
    tekst(d, D, (D/2, D*0.80), 'of 30 · round 2', D*0.066, WIT)
    rand(im, D); return im

def duik_zee(im, D, meter=94):
    # hoe dieper, hoe hoger de donkere banden: op 183 m is bijna alles nacht (keuring 3, moet-punt 1)
    k = min(1, meter/183)
    zee(im, D, [(D*0.12, W0), (D*(0.19 - 0.04*k), W1), (D*(0.62 - 0.30*k), W2), (D*(0.90 - 0.32*k), W3)], amp=D*0.014)

def s_duik(D, diepte, tijd, soort, s, bel, hoek=0, sec=0, vorig=0, volgend=0):
    im = leeg(D); duik_zee(im, D, int(diepte.split()[0])); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.255), diepte, D*0.085, SCHUIM)
    tekst(d, D, (D/2, D*0.44), tijd, D*0.30, WIT)
    bellen(d, D, bel)
    dier(im, soort, D/2, D*0.700, s*D, hoek=hoek)
    d = ImageDraw.Draw(im)
    # voortgang naar het volgende dier: dunne boog langs de rand, vanaf boven met de klok mee (keuring 2)
    w = max(3, round(D/110)); m = max(2, round(D/150)) + w/2 + 1
    if volgend:   # boog met een zwarte rand, zodat hij ook over de golf leest; bij alles gevonden geen boog
        frac = (sec - vorig)/(volgend - vorig)
        d.arc([m-1, m-1, D-m, D-m], -91, -89 + 360*frac, fill=ZWART, width=w+2)
        d.arc([m, m, D-1-m, D-1-m], -90, -90 + 360*frac, fill=SCHUIM, width=w)
    tekst(d, D, (D/2, D*0.865), f'next {volgend//60}:{volgend%60:02d}' if volgend else 'all found', D*0.066, SCHUIM)
    rand(im, D); return im
def s_duiken(D): return s_duik(D, '94 m', '1:34', 'kwal', 0.085, [(0.33, 0.62, 0.016), (0.30, 0.565, 0.009), (0.65, 0.64, 0.011), (0.68, 0.60, 0.006)], sec=94, vorig=90, volgend=120)
def s_walvis(D): return s_duik(D, '183 m', '3:03', 'walvis', 0.135, [(0.30, 0.66, 0.010), (0.27, 0.615, 0.016), (0.31, 0.575, 0.007)], hoek=9, sec=183, vorig=180, volgend=0)   # walvis daalt mee de diepte in
def s_schildpad(D): return s_duik(D, '123 m', '2:03', 'pad', 0.105, [(0.33, 0.66, 0.009), (0.30, 0.62, 0.014), (0.68, 0.64, 0.007)], hoek=-6, sec=123, vorig=120, volgend=180)   # schildpad zweeft omhoog

def s_boven(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    zr = D*0.12; d.ellipse([D/2-zr, D*0.66-zr, D/2+zr, D*0.66+zr], fill=GEEL)   # geel alleen voor de zon
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'breathe in', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.39), '15', D*0.26, WIT)
    tekst(d, D, (D/2, D*0.80), 'held 1:34', D*0.066, WIT)
    rand(im, D); return im

def s_rustig(D):
    im = leeg(D)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'hold', D*0.090, TITEL)
    tekst(d, D, (D/2, D*0.41), '7', D*0.32, WIT)
    tekst(d, D, (D/2, D*0.80), '4-7-8', D*0.066, WIT)
    rand(im, D); return im

def s_today(D):
    """Drie herkenbare duiken: een U met vlakke bodem, diepte = inhoudtijd, de tijd eronder (moet-punt 10)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'today', D*0.085, TITEL)
    opp = D*0.33; L, R = D*0.17, D*0.83; breed = (R-L)/3
    tijden = [('1:20', 80), ('2:08', 128), ('1:45', 105)]; maxdiep = D*0.27
    zeevlak = Image.new('L', (D, D), 0); zd = ImageDraw.Draw(zeevlak)
    lijnen = []
    for i, (_, sec) in enumerate(tijden):
        x0 = L + i*breed; dp = maxdiep*sec/128
        m = breed*0.16; r = breed*0.10
        pts = [(x0+m*0.5, opp)] + [(x0+m*0.5 + (breed*0.30)*t, opp + dp*(math.sin(t*math.pi/2))) for t in [k/8 for k in range(1, 9)]]
        pts += [(x0+breed-m*0.5 - (breed*0.30)*t, opp + dp*(math.sin(t*math.pi/2))) for t in [k/8 for k in range(8, 0, -1)]] + [(x0+breed-m*0.5, opp)]
        zd.polygon(pts, fill=255); lijnen.append(pts)
    for kleur, y0 in ((W1, opp), (W2, opp + maxdiep*0.40), (W3, opp + maxdiep*0.78)):
        band = Image.new('L', (D, D), 0); ImageDraw.Draw(band).rectangle([0, y0, D, D], fill=255)
        im.paste(Image.new('RGB', (D, D), kleur), (0, 0), ImageChops.multiply(zeevlak, band))
    d = ImageDraw.Draw(im)
    for pts in lijnen: d.line(pts, fill=W0, width=max(2, round(D/150)))
    d.line([(L, opp), (R, opp)], fill=SCHUIM, width=max(2, round(D/150)))
    for i, (t, sec) in enumerate(tijden):
        xm = L + (i+0.5)*breed
        tekst(d, D, (xm, opp + maxdiep + D*0.065), t, D*0.070, GOUD if sec == 128 else WIT)
    rr = D*0.018; xm = L + 1.5*breed; yb = opp + maxdiep
    d.ellipse([xm-rr, yb-rr, xm+rr, yb+rr], fill=GOUD)
    tekst(d, D, (D/2, D*0.80), 'new best', D*0.066, GOUD)
    rand(im, D); return im

def s_weken(D):
    """Eén lijn (beste per dag) met het getij eronder, de piek gemarkeerd en gelabeld (moet-punt 9)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), '8 weeks', D*0.085, TITEL)
    L, R, top, bod = D*0.18, D*0.82, D*0.36, D*0.64
    best = []
    for i in range(56):
        v = 0.30 + 0.62*min(i, 44)/44 - 0.020*max(0, i-44) + 0.05*math.sin(i*0.55)
        best.append(None if i in (9, 10, 23, 37, 38) else v)
    pk = max(range(56), key=lambda k: best[k] or 0); hoog = best[pk]
    best = [b/hoog if b else None for b in best]
    dx = (R-L)/55; Y = lambda v: bod - v*(bod-top)
    # het getij: één doorlopend vlak (gaten opgevuld met de buren), de lijn van je beste tijd heeft wel gaten
    vul = []
    for i, b in enumerate(best):
        if b is None:
            l = next(best[j] for j in range(i, -1, -1) if best[j]); r = next(best[j] for j in range(i, 56) if best[j]); b = (l+r)/2
        vul.append((L+i*dx, Y(b)))
    d.polygon(vul + [(R, bod), (L, bod)], fill=W1)   # W1 i.p.v. W2: beter contrast op zwart
    seg = []
    for i, b in enumerate(best + [None]):
        if b is None:
            if len(seg) > 1: d.line(seg, fill=SCHUIM, width=max(2, round(D/150)), joint='curve')
            seg = []; continue
        seg.append((L+i*dx, Y(b)))
    d.line([(L, bod), (R, bod)], fill=W1, width=max(2, round(D/150)))
    for w in range(9):
        x = L + w*(R-L)/8
        d.line([(x, bod), (x, bod+D*0.02)], fill=GRIJS, width=max(1, round(D/230)))
    r = D*0.022; px_, py_ = L+pk*dx, Y(1.0)
    d.ellipse([px_-r, py_-r, px_+r, py_+r], fill=GOUD)
    tekst(d, D, (D/2, D*0.755), 'best 2:08', D*0.085, GOUD)
    tekst(d, D, (D/2, D*0.845), 'longest hold per day', D*0.066, GRIJS)
    rand(im, D); return im, (px_, py_, r)

def s_weken_beeld(D): return s_weken(D)[0]

def s_zeelog(D):
    """Drie kolommen op gelijke afstand, drie dieren even zwaar (zelfde oppervlak), walvis groot eronder (moet-punt 8)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'sea log', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.27), '3 of 4 found', D*0.066, GRIJS)
    kol = D*0.215; y1 = D*0.425; opp = (D*0.105)**2*0.55
    for k, (soort, t) in enumerate((('vis', '1:00'), ('kwal', '1:30'), ('pad', '2:00'))):
        x = D/2 + (k-1)*kol
        dier(im, soort, x, y1, schaal_voor_gewicht(soort, opp))
        tekst(ImageDraw.Draw(im), D, (x, D*0.535), t, D*0.070, WIT)
    for ox, oy in ((-1,0),(1,0),(0,-1),(0,1),(-2,0),(2,0),(0,-2),(0,2))[:4 if D < 300 else 8]:   # cyaan rand: een lokkertje
        dier(im, 'walvis', D/2+ox, D*0.665+oy, D*0.105, kleur=SCHUIM)
    dier(im, 'walvis', D/2, D*0.665, D*0.105, kleur=W1)      # nog niet gezien: donkerblauw silhouet
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2 - D*0.02, D*0.665), '?', D*0.075, SCHUIM)
    tekst(d, D, (D/2, D*0.785), '3:00', D*0.070, GRIJS)
    rand(im, D); return im

def pijltjes(d, D, x, y, kleur):
    """Omhoog en omlaag (knoppen), geen links en rechts."""
    a = D*0.016
    d.polygon([(x, y-a*1.7), (x+a, y-a*0.3), (x-a, y-a*0.3)], fill=kleur)
    d.polygon([(x, y+a*1.7), (x+a, y+a*0.3), (x-a, y+a*0.3)], fill=kleur)

def s_instellingen(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'settings', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.330), 'Rounds 3', D*0.066, GRIJS)
    pil(d, D, 0.50, 0.64, 0.24)
    tekst(d, D, (D/2, D*0.465), 'Breaths', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.555), '30', D*0.066, SCHUIM)
    pijltjes(d, D, D/2 - D*0.075, D*0.555, SCHUIM); pijltjes(d, D, D/2 + D*0.075, D*0.555, SCHUIM)
    tekst(d, D, (D/2, D*0.670), 'Buzz on', D*0.066, GRIJS)
    tekst(d, D, (D/2, D*0.765), 'My pattern', D*0.066, GRIJS)
    startknop(d, D)
    rand(im, D); return im
def s_veilig(D):
    """Rustig: teken, twee regels, knop, geen golf (kan-punt 4)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    s = D*0.085; y = D*0.25
    d.polygon([(D/2, y-s*0.78), (D/2+s*0.88, y+s*0.66), (D/2-s*0.88, y+s*0.66)], fill=KORAAL)
    tekst(d, D, (D/2, y+s*0.14), '!', s*0.95, W3)
    tekst(d, D, (D/2, D*0.43), 'Never in water.', D*0.080, WIT)
    tekst(d, D, (D/2, D*0.53), 'Never driving.', D*0.080, WIT)
    pil(d, D, 0.69, 0.34, 0.12)
    tekst(d, D, (D/2, D*0.69), 'OK', D*0.075, WIT)
    startknop(d, D)
    rand(im, D); return im

def s_beloning(D):
    """Na de duik: nieuw dier. Het dier groot in het midden, de tijd, de stand in de sea log (keuring 2)."""
    im = leeg(D)
    zee(im, D, [(D*0.12, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=False)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.22), 'new friend', D*0.085, TITEL)
    bellen(d, D, [(0.27, 0.40, 0.012), (0.24, 0.35, 0.007), (0.74, 0.55, 0.010), (0.77, 0.50, 0.006)])
    dier(im, 'pad', D/2, D*0.465, D*0.17, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.665), 'turtle 2:03', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.77), '3 of 4 found', D*0.066, SCHUIM)
    rand(im, D); return im

def s_icoon(D):
    """Icoon en loep: walvis in de patrijspoort. Alleen hier de bouten (moet-punt 4)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    c = D/2; R = D*0.47; r = D*0.38
    d.ellipse([c-R, c-R, c+R, c+R], fill=RING)
    d.ellipse([c-r, c-r, c+r, c+r], fill=W2)
    # binnen de poort: een strook dieper water onderin, met dithering
    binnen = Image.new('RGB', (D, D), ZWART); zee(binnen, D, [(D*0.66, W3)], amp=D*0.012, schuim=False)
    m = Image.new('L', (D, D), 0); ImageDraw.Draw(m).ellipse([c-r, c-r, c+r, c+r], fill=255)
    zm = ImageChops.multiply(m, binnen.convert('L').point(lambda v: 255 if v > 0 else 0))
    im.paste(binnen, (0, 0), zm)
    dier(im, 'walvis', c, c, r*0.62)
    d = ImageDraw.Draw(im)
    for k in range(8):
        a = math.pi/8 + k*math.pi/4; bx = c+(R+r)/2*math.cos(a); by = c+(R+r)/2*math.sin(a); q = D*0.016
        d.ellipse([bx-q, by-q, bx+q, by+q], fill=(85,170,170))
    return im

SCHERMEN = [('1 menu', s_menu), ('2 ademen', s_ademen), ('3 duiken', s_duiken), ('3b walvis 3:03', s_walvis), ('3c schildpad 2:03', s_schildpad),
            ('3d nieuw dier', s_beloning), ('4 boven', s_boven), ('5 rustig 4-7-8', s_rustig), ('6 today', s_today), ('7 8 weeks', s_weken_beeld),
            ('8 sea log', s_zeelog), ('9 settings', s_instellingen), ('10 veiligheid', s_veilig)]

# ---------------- nameten ----------------
def kader_x(im, D):
    a = np.array(im).astype(int); y, x = np.mgrid[0:D, 0:D]
    r = np.hypot(x+0.5-D/2, y+0.5-D/2)
    hint = (a[:, :, 0] == HINT[0]) & (a[:, :, 1] == HINT[1]) & (a[:, :, 2] == HINT[2])
    niet = (a.sum(axis=2) > 0) & (r < D*0.47) & ~hint
    xs = np.nonzero(niet.any(axis=0))[0]
    return (xs.min() + xs.max() + 1)/2 - D/2

def optisch_x(im, D):
    """Zwaartepunt (x) van de voorgrond: alles behalve zwart, water, ring en knophint. Dat is wat het oog weegt."""
    a = np.array(im).astype(int)
    achter = [ZWART, W0, W1, W2, W3, RING, HINT]
    m = np.ones(a.shape[:2], bool)
    for c in achter: m &= ~((a[:, :, 0] == c[0]) & (a[:, :, 1] == c[1]) & (a[:, :, 2] == c[2]))
    ys, xs = np.nonzero(m)
    return xs.mean() + 0.5 - D/2

def niet_mip(im):
    a = np.array(im).reshape(-1, 3)
    return int((~np.isin(a, [0, 85, 170, 255]).all(axis=1)).sum())

def contrast(a, b):
    def L(c):
        v = [x/255 for x in c]; v = [x/12.92 if x <= 0.03928 else ((x+0.055)/1.055)**2.4 for x in v]
        return 0.2126*v[0] + 0.7152*v[1] + 0.0722*v[2]
    la, lb = sorted((L(a), L(b)), reverse=True); return (la+0.05)/(lb+0.05)

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = fn(D); im.save(f'{uit}/ebb-v2-{naam.split()[0]}-{D}.png')
            rap.append(f'{D:4d}  {naam:18s} kader x {kader_x(im, D):+5.1f} px   optisch x {optisch_x(im, D):+5.1f} px   pixels buiten MIP {niet_mip(im)}')
    s_icoon(560).save(f'{uit}/ebb-v2-icoon-560.png')
    # dieren: zwaartepunt t.o.v. de plek waar ze moeten staan (altijd 0 door dier()), en gewicht in de sea log
    for soort in ('vis', 'kwal', 'pad'):
        _, _, a = dier_beeld(soort, schaal_voor_gewicht(soort, (260*0.105)**2*0.55)); rap.append(f'sea log 260 {soort:5s} oppervlak {a} px')
    for D in (454, 260):
        _, (px_, py_, r) = s_weken(D)
        afst = D/2 - math.hypot(px_-D/2, py_-D/2) - r; rap.append(f'8 weeks {D}: piekstip {afst:.0f} px van de rand')
    klein = sorted({(t, p) for D, t, p in LOG if D == 260}, key=lambda z: z[1])[:6]
    rap.append('kleinste tekst op 260: ' + ', '.join(f'"{t}" {p} px' for t, p in klein))
    rap.append(f'contrast grijs #AAAAAA op zwart {contrast(GRIJS, ZWART):.1f}:1, W1 op zwart {contrast(W1, ZWART):.1f}:1, goud op zwart {contrast(GOUD, ZWART):.1f}:1, wit op W1 {contrast(WIT, W1):.1f}:1, schuim op W1 {contrast(SCHUIM, W1):.1f}:1, wit op W2 {contrast(WIT, W2):.1f}:1')
    # het blad
    gap = 30; cel_b = 454 + 24 + 260; kol = 4; cel_h = 454 + 64
    cellen = SCHERMEN + [('icoon (alleen hier bouten)', None)]
    rijen = (len(cellen) + kol - 1)//kol
    W = gap + kol*(cel_b + gap); H = 110 + rijen*(cel_h + gap)
    blad = Image.new('RGB', (W, H), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 30), 'Ebb blad v2.2 (Mila): links 454 px (AMOLED), rechts 260 px (MIP), ware grootte, harde randen zoals op het horloge',
           font=f(44), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(cellen):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        g = fn if fn else s_icoon
        blad.paste(g(454), (x, y)); blad.paste(g(260), (x+478, y+194))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v2.png')
    return rap

if __name__ == '__main__':
    FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v2.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
