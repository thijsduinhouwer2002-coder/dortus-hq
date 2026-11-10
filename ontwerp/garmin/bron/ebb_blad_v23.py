# Ontwerpblad Ebb v2.3 (Mila, 10 nov run 19): na de vierde frisse keuring (v2.2, 6/10, elf moet-punten).
# Twee gezichten van dezelfde app:
#  - 454 (AMOLED): echte verlopen in de zee, zachte randen, zachte letters, lichtstralen onder water.
#    Getekend op 3x en verkleind (zoals het horloge met setAntiAlias en verloop-bitmaps tekent).
#  - 260 (MIP): strak, harde vlakken, alleen MIP-kleuren, geen dithering langs de golfranden.
# Alle maten als deel van D.
# Gebruik: python3 ebb_blad_v23.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter

ZWART=(0,0,0); WIT=(255,255,255); GRIJS=(170,170,170); SCHUIM=(85,255,255); RING=(0,85,85)
W0=(0,170,255); W1=(0,85,170); W2=(0,0,170); W3=(0,0,85)          # MIP-waterschaal
AM = {W0: (40,195,255), W1: (0,105,205), W2: (8,40,155), W3: (2,10,62)}   # AMOLED: dezelfde vier, rijker, als verloop
GEEL=(255,255,170); KORAAL=(255,85,85)
GOUD=(255,170,0)       # record
ORANJE=(255,85,0)      # voortgang naar het volgende dier (moet-punt 2)
TITEL = SCHUIM
MIN = 20/260           # kleinste letter: 20 px op 260 = 14 px kapitaalhoogte (moet-punt 7)
SS = 3                 # AMOLED: op 3x tekenen, dan verkleinen
FONT = None
LOG = []

def amo(D): return D >= 300
def f(px): return ImageFont.truetype(FONT, int(round(px)))

def tekst(d, D, xy, t, px, kleur, anker='mm'):
    px = max(px, MIN*D)
    LOG.append((D if not amo(D) else D//SS, t, int(round(px if not amo(D) else px/SS))))
    d.fontmode = 'L' if amo(D) else '1'
    d.text(xy, t, font=f(px), fill=kleur, anchor=anker)

def getal_eenheid(d, D, y, getal, px, eenheid, upx, kleur):
    """Groot getal met een kleine eenheid erachter ("15 s"), samen gecentreerd (moet-punt 5)."""
    upx = max(upx, MIN*D); fg, fu = f(px), f(upx)
    wg = fg.getlength(getal); wu = fu.getlength(eenheid); gap = px*0.06
    x0 = D/2 - (wg + gap + wu)/2; yb = y + px*0.36
    d.fontmode = 'L' if amo(D) else '1'
    d.text((x0, yb), getal, font=fg, fill=kleur, anchor='ls')
    d.text((x0 + wg + gap, yb), eenheid, font=fu, fill=GRIJS, anchor='ls')
    LOG.append((D if not amo(D) else D//SS, eenheid, int(round(upx if not amo(D) else upx/SS))))

# ---------------- water ----------------
def golf(D, peil, amp, n=2, fase=0.0):
    return [(x, peil + amp*math.cos(2*math.pi*n*(x-D/2)/D + fase)) for x in range(0, D+1, 2)]

def masker_onder(D, pts):
    m = Image.new('L', (D, D), 0); ImageDraw.Draw(m).polygon(pts + [(D, D), (0, D)], fill=255); return m

def verloop(D, stops):
    """Verticaal verloop: stops = [(y, kleur)], daartussen lineair."""
    ys = np.arange(D)[:, None].astype(float)
    pos = [s[0] for s in stops]; out = np.zeros((D, 1, 3))
    for c in range(3):
        out[:, :, c] = np.interp(ys, pos, [s[1][c] for s in stops])
    return Image.fromarray(np.repeat(out, D, axis=1).astype('uint8'))

def zee(im, D, banden, amp=None, n=2, schuim=True, stralen=False):
    """banden = [(peil, kleur), ...] van boven naar beneden.
    MIP: harde vlakken, geen dithering (moet-punt 1). AMOLED: één doorlopend verloop door de vier tinten,
    zachte golflijnen tussen de lagen, een gloed onder het schuim en (onder water) lichtstralen."""
    amp = D*0.018 if amp is None else amp
    golven = [golf(D, p, amp*(1 if k == 0 else 0.6), n if k == 0 else n+1, 0 if k == 0 else 0.8*k) for k, (p, _) in enumerate(banden)]
    eerste = golven[0]
    if not amo(D):
        for g, (_, kleur) in zip(golven, banden):
            im.paste(Image.new('RGB', (D, D), kleur), (0, 0), masker_onder(D, g))
        if schuim: ImageDraw.Draw(im).line(eerste, fill=SCHUIM, width=max(2, round(D/150)))
        return eerste
    stops = [(p - amp*0.6, AM[c]) for p, c in banden]
    laatste = AM[banden[-1][1]]
    stops.append((max(stops[-1][0] + 1, D), tuple(int(v*0.55) for v in laatste)))
    stops = [(stops[0][0] - 1, stops[0][1])] + stops
    water = verloop(D, stops)
    # zachte grens tussen de lagen: een iets lichtere golflijn, vervaagd
    lijn = Image.new('L', (D, D), 0); ld = ImageDraw.Draw(lijn)
    for g in golven[1:]: ld.line(g, fill=70, width=round(D/120))
    lijn = lijn.filter(ImageFilter.GaussianBlur(D/180))
    water = Image.composite(Image.new('RGB', (D, D), (120, 200, 255)), water, lijn)
    if stralen:   # lichtstralen van boven, heel zacht
        st = Image.new('L', (D, D), 0); sd = ImageDraw.Draw(st)
        for x0, b, a in ((0.30, 0.05, 34), (0.47, 0.035, 26), (0.62, 0.06, 30), (0.78, 0.03, 22)):
            sd.polygon([(x0*D, 0), ((x0+b)*D, 0), ((x0+b+0.16)*D, D), ((x0+0.16)*D, D)], fill=a)
        st = st.filter(ImageFilter.GaussianBlur(D/60))
        st = ImageChops.multiply(st, verloop(D, [(0, (255,)*3), (D*0.75, (0,)*3)]).convert('L'))
        water = Image.composite(Image.new('RGB', (D, D), (170, 230, 255)), water, st)
    im.paste(water, (0, 0), masker_onder(D, eerste).filter(ImageFilter.GaussianBlur(D/400)))
    if schuim:
        gloed = Image.new('L', (D, D), 0); ImageDraw.Draw(gloed).line(eerste, fill=150, width=round(D/40))
        gloed = gloed.filter(ImageFilter.GaussianBlur(D/80))
        im.paste(Image.new('RGB', (D, D), (120, 230, 255)), (0, 0), gloed)
        ImageDraw.Draw(im).line(eerste, fill=(200, 255, 255), width=max(2, round(D/150)))
    return eerste

def vlak(im, D, masker, y0, y1, banden_mip):
    """Gevuld grafiekvlak: MIP harde banden, AMOLED verloop van W1 naar W3."""
    if amo(D):
        im.paste(verloop(D, [(y0, AM[W0]), (y0 + (y1-y0)*0.25, AM[W1]), (y1, AM[W3])]), (0, 0), masker)
    else:
        for kleur, yb in banden_mip:
            band = Image.new('L', (D, D), 0); ImageDraw.Draw(band).rectangle([0, yb, D, D], fill=255)
            im.paste(Image.new('RGB', (D, D), kleur), (0, 0), ImageChops.multiply(masker, band))

def rand(im, D):
    d = ImageDraw.Draw(im)
    d.ellipse([-D*0.5, -D*0.5, D*1.5, D*1.5], outline=ZWART, width=round(D*0.5))
    d.ellipse([0, 0, D-1, D-1], outline=RING, width=max(2, round(D/150)))

def leeg(D): return Image.new('RGB', (D, D), ZWART)

# ---------------- dieren ----------------
# Eén stijl: gevulde vlakken, lijf in eigen tint, licht deel een tint lichter, donker deel een tint donkerder,
# hetzelfde oog. Schildpad nu groen (moet-punt 8): schild groen, huid geelgroen, geen stippen.
TINT = {'walvis': ((255,85,85), (255,170,170), (170,0,0)),
        'vis':    ((255,170,85), (255,255,170), (255,85,0)),
        'kwal':   ((255,85,170), (255,170,255), (170,0,85)),
        'pad':    ((0,170,85),  (170,255,85),  (0,85,0))}

def bez(p0, p1, p2, n=10):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]

def ellips(cx, cy, rx, ry, a0=0, a1=360, n=40):
    return [(cx + rx*math.cos(math.radians(a0 + (a1-a0)*i/n)), cy + ry*math.sin(math.radians(a0 + (a1-a0)*i/n))) for i in range(n+1)]

def walvis_h(u): return 0.40/0.62 * (u**0.18) * ((1-u)**0.85) + 0.05*u

def walvis_lijf():
    top, bod = [], []
    for i in range(41):
        u = i/40; x = -1 + 1.75*u; h = walvis_h(u)
        top.append((x, -h*1.15)); bod.append((x, h*0.85))
    return top + bod[::-1]

def walvis_buik():
    boven, onder = [], []
    for i in range(41):
        u = i/40; x = -1 + 1.75*u; h = walvis_h(u)*0.85; yb = 0.10 + 0.04*u
        if h > yb + 0.01: boven.append((x, yb)); onder.append((x, h))
    return boven + onder[::-1]

def tentakel(x0, y0, lengte, breed, golfjes, fase):
    """Zachte, taps toelopende arm met een rond eind (kwal in dezelfde ronde stijl, moet-punt 8)."""
    n = 14; l, r = [], []
    for i in range(n+1):
        t = i/n; x = x0 + 0.07*math.sin(fase + t*golfjes*math.pi); y = y0 + t*lengte; w = breed*(1 - 0.55*t)
        l.append((x - w/2, y)); r.append((x + w/2, y))
    xe, ye = l[-1][0] + (r[-1][0]-l[-1][0])/2, l[-1][1]; we = (r[-1][0]-l[-1][0])/2
    return l + ellips(xe, ye, we, we, 180, 0, 8) + r[::-1]

def dier_delen(soort):
    if soort == 'walvis':
        lijf = walvis_lijf()
        staart = [(0.66,-0.06),(0.84,-0.12),(0.98,-0.36),(1.06,-0.33),(0.95,-0.02),(1.06,0.24),(0.99,0.28),(0.84,0.09),(0.66,0.07)]
        vin = bez((-0.42,0.24),(-0.14,0.26),(0.02,0.50),6) + bez((0.02,0.50),(-0.08,0.54),(-0.34,0.38),4)
        bek = bez((-0.99,0.06),(-0.85,0.16),(-0.66,0.06),6) + bez((-0.66,0.06),(-0.70,0.13),(-0.99,0.12),6)
        return [(staart,'lijf'), (lijf,'lijf'), (walvis_buik(),'licht'), (vin,'lijf'), (bek,'donker')], [(-0.62,-0.12)]
    if soort == 'vis':
        lijf = ellips(-0.22, 0, 0.78, 0.50)
        staart = [(0.40,0),(1.0,-0.48),(0.86,0),(1.0,0.48)]
        buik = ellips(-0.22, 0, 0.78, 0.50, 20, 160)
        vin = bez((-0.35,-0.42),(0.0,-0.78),(0.30,-0.40),6)
        return [(staart,'donker'), (lijf,'lijf'), (buik,'licht'), (vin,'donker')], [(-0.62,-0.10)]
    if soort == 'kwal':
        # ronde kap met een golvende onderrand, vier zachte armen, een glans linksboven
        kap = ellips(0, 0.02, 0.80, 0.80, 180, 360, 50)
        onder = []
        for i in range(25):
            t = i/24; x = 0.80 - 1.60*t; onder.append((x, 0.02 + 0.07*abs(math.sin(t*4*math.pi))))
        kap = kap + onder
        armen = [(tentakel(x0, 0.04, 0.80 + 0.10*(k % 2), 0.17, 1.6, k*1.3), 'donker') for k, x0 in enumerate((-0.48, -0.16, 0.16, 0.48))]
        glans = ellips(-0.38, -0.46, 0.15, 0.09)
        return armen + [(kap,'lijf'), (glans,'licht')], [(-0.28,-0.22), (0.28,-0.22)]
    if soort == 'pad':
        schild = ellips(0.08, 0.10, 0.62, 0.72, 180, 360) + [(0.70,0.10),(-0.54,0.10)]
        rand_ = [(-0.56,0.04),(0.72,0.04),(0.70,0.12),(-0.54,0.12)]
        buik = [(-0.56,0.12),(0.72,0.12),(0.62,0.26),(-0.46,0.26)]
        kop = ellips(-0.74, -0.02, 0.27, 0.22)
        voor = bez((-0.42,0.14),(-0.10,0.26),(0.02,0.58),6) + bez((0.02,0.58),(-0.14,0.62),(-0.46,0.30),4)
        achter = bez((0.46,0.16),(0.74,0.22),(0.86,0.44),5) + bez((0.86,0.44),(0.64,0.46),(0.40,0.26),4)
        staartje = [(0.66,0.10),(0.92,0.16),(0.66,0.22)]
        return [(achter,'licht'), (voor,'licht'), (staartje,'licht'), (kop,'licht'), (schild,'lijf'), (rand_,'donker'), (buik,'licht')], [(-0.80,-0.06)]

def dier_beeld(soort, s, kleur_override=None, hoek=0):
    delen, ogen = dier_delen(soort)
    if hoek:
        ca, sa = math.cos(math.radians(-hoek)), math.sin(math.radians(-hoek))
        R_ = lambda pts: [(x*ca - y*sa, x*sa + y*ca) for x, y in pts]
        delen = [(R_(p), r) for p, r in delen]; ogen = R_(ogen)
    lijf, licht, donker = TINT[soort]
    if kleur_override: lijf = licht = donker = kleur_override
    W = int(s*2.8) + 4; c = W/2
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
    laag, (zx, zy), _ = dier_beeld(soort, s, kleur, hoek)
    im.paste(laag, (int(round(cx - zx)), int(round(cy - zy))), laag)
    return laag, (zx, zy)

def schaal_voor_gewicht(soort, oppervlak):
    _, _, a1 = dier_beeld(soort, 40)
    return 40*math.sqrt(oppervlak/a1)

WX = -0.012   # walvissen iets naar links: de omtrek oogt anders rechts (kan-punt 2)

def spuit(d, D, x, y, s):
    for dx, dy, r in ((-0.22, -0.30, 0.10), (0.0, -0.42, 0.12), (0.22, -0.30, 0.10)):
        cx, cy = x + dx*s, y + dy*s; R = r*s
        d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=SCHUIM)

def bellen(d, D, lijst):
    for x, y, r in lijst:
        R = r*D; w = max(1, round(R/3))
        d.ellipse([x*D-R, y*D-R, x*D+R, y*D+R], outline=(85,170,255) if not amo(D) else (150,215,255), width=w)

def voortgang(d, D, frac, vol=False):
    """Moet-punt 2: donker spoor rondom, oranje boog erop, witte stip aan het eind. Vol = hele ring."""
    w = max(4, round(D/75)); m = max(2, round(D/150)) + w/2 + 2
    bb = [m, m, D-1-m, D-1-m]
    d.arc([m-2, m-2, D+1-m, D+1-m], 0, 360, fill=ZWART, width=w+4)
    d.arc(bb, 0, 360, fill=(0, 40, 70) if amo(D) else W3, width=w)
    if vol:
        d.arc(bb, 0, 360, fill=ORANJE, width=w); return
    d.arc(bb, -90, -90 + 360*frac, fill=ORANJE, width=w)
    rr = (D-1-2*m)/2
    for t in (60, 90, 120, 180):   # een streepje per dier: vis, kwal, schildpad, walvis (bovenaan)
        a = math.radians(-90 + 360*t/180)
        d.line([(D/2 + (rr-w*1.2)*math.cos(a), D/2 + (rr-w*1.2)*math.sin(a)), (D/2 + (rr+w*0.5)*math.cos(a), D/2 + (rr+w*0.5)*math.sin(a))], fill=WIT, width=max(2, round(w*0.5)))
    a = math.radians(-90 + 360*frac)
    x, y = D/2 + rr*math.cos(a), D/2 + rr*math.sin(a); R = w*1.05
    d.ellipse([x-R-2, y-R-2, x+R+2, y+R+2], fill=ZWART); d.ellipse([x-R, y-R, x+R, y+R], fill=WIT)

def pil(d, D, y, w, h, kleur=W1):
    d.rounded_rectangle([D/2-w*D/2, y*D-h*D/2, D/2+w*D/2, y*D+h*D/2], radius=h*D/2, fill=kleur if not amo(D) else AM[kleur])

# ---------------- schermen ----------------
def s_menu(D):
    im = leeg(D)
    s = D*0.11; wx = D/2 + WX*D
    dier(im, 'walvis', wx, D*0.865, s)
    d = ImageDraw.Draw(im)
    spuit(d, D, wx - 0.36*s, D*0.865 - 0.42*s, s)
    zee(im, D, [(D*0.872, W1), (D*0.94, W2)], amp=D*0.008)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.19), 'Ebb', D*0.11, TITEL)
    tekst(d, D, (D/2, D*0.335), 'Calm · 4-7-8', D*0.068, GRIJS)       # moet-punt 9: Box eruit, Calm met patroon
    pil(d, D, 0.495, 0.64, 0.22)
    tekst(d, D, (D/2, D*0.465), 'Rounds', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.550), '3 x 30', D*0.068, SCHUIM)
    tekst(d, D, (D/2, D*0.655), 'Sea log', D*0.068, GRIJS)
    rand(im, D); return im

def s_ademen(D):
    im = leeg(D)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'in', D*0.095, TITEL)                   # wisselt in / out (moet-punt 5)
    tekst(d, D, (D/2, D*0.41), '23', D*0.32, WIT)
    tekst(d, D, (D/2, D*0.80), 'breath 23 of 30', D*0.068, WIT)
    tekst(d, D, (D/2, D*0.875), 'round 2', D*0.068, WIT)
    rand(im, D); return im

def duik_zee(im, D, meter=94):
    k = min(1, meter/183)
    zee(im, D, [(D*0.12, W0), (D*(0.19 - 0.04*k), W1), (D*(0.62 - 0.30*k), W2), (D*(0.90 - 0.32*k), W3)], amp=D*0.014, stralen=True)

def s_duik(D, diepte, tijd, soort, s, bel, hoek=0, sec=0, vorig=0, volgend=0, onder=None):
    im = leeg(D); duik_zee(im, D, int(diepte.split()[0])); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.255), diepte, D*0.085, SCHUIM)
    tekst(d, D, (D/2, D*0.44), tijd, D*0.30, WIT)
    bellen(d, D, bel)
    cx = D/2 + (WX*D if soort == 'walvis' else 0)
    dier(im, soort, cx, D*(0.675 if onder else 0.700), s*D, hoek=hoek)
    d = ImageDraw.Draw(im)
    voortgang(d, D, min(1, sec/180), vol=not volgend)
    if onder:   # twee regels, anders raakt de tekst de ring
        tekst(d, D, (D/2, D*0.815), onder[0], D*0.075, WIT)
        tekst(d, D, (D/2, D*0.885), onder[1], D*0.068, WIT)
    else:
        tekst(d, D, (D/2, D*0.865), f'next {volgend//60}:{volgend%60:02d}', D*0.068, WIT)
    rand(im, D); return im
def s_duiken(D): return s_duik(D, '94 m', '1:34', 'kwal', 0.085, [(0.33, 0.62, 0.016), (0.30, 0.565, 0.009), (0.65, 0.64, 0.011), (0.68, 0.60, 0.006)], sec=94, vorig=90, volgend=120)
def s_walvis(D): return s_duik(D, '183 m', '3:03', 'walvis', 0.135, [(0.30, 0.66, 0.010), (0.27, 0.615, 0.016), (0.31, 0.575, 0.007)], hoek=9, onder=('whale found', '4 of 4'))   # moet-punt 3
def s_schildpad(D): return s_duik(D, '123 m', '2:03', 'pad', 0.105, [(0.33, 0.66, 0.009), (0.30, 0.62, 0.014), (0.68, 0.64, 0.007)], hoek=-6, sec=123, vorig=120, volgend=180)

def s_boven(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    zr = D*0.12
    if amo(D):   # zon met een zachte gloed
        gl = Image.new('L', (D, D), 0); ImageDraw.Draw(gl).ellipse([D/2-zr*1.9, D*0.66-zr*1.9, D/2+zr*1.9, D*0.66+zr*1.9], fill=90)
        im.paste(Image.new('RGB', (D, D), (255, 200, 90)), (0, 0), gl.filter(ImageFilter.GaussianBlur(D/30)))
    d.ellipse([D/2-zr, D*0.66-zr, D/2+zr, D*0.66+zr], fill=GEEL)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'breathe in', D*0.085, TITEL)
    getal_eenheid(d, D, D*0.39, '15', D*0.26, 's', D*0.10, WIT)       # seconden duidelijk (moet-punt 5)
    tekst(d, D, (D/2, D*0.80), 'held 1:34', D*0.068, WIT)
    rand(im, D); return im

def s_rustig(D):
    im = leeg(D)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'hold', D*0.090, TITEL)
    getal_eenheid(d, D, D*0.41, '7', D*0.32, 's', D*0.11, WIT)
    tekst(d, D, (D/2, D*0.80), 'Calm 4-7-8', D*0.068, WIT)
    rand(im, D); return im

def s_today(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'today', D*0.085, TITEL)
    opp = D*0.33; L, R = D*0.17, D*0.83; breed = (R-L)/3
    tijden = [('1:20', 80), ('1:45', 105), ('2:08', 128)]; maxdiep = D*0.27   # oplopend, record als laatste ronde
    zeevlak = Image.new('L', (D, D), 0); zd = ImageDraw.Draw(zeevlak)
    lijnen = []
    for i, (_, sec) in enumerate(tijden):
        x0 = L + i*breed; dp = maxdiep*sec/128; m = breed*0.16
        pts = [(x0+m*0.5, opp)] + [(x0+m*0.5 + (breed*0.30)*t, opp + dp*(math.sin(t*math.pi/2))) for t in [k/8 for k in range(1, 9)]]
        pts += [(x0+breed-m*0.5 - (breed*0.30)*t, opp + dp*(math.sin(t*math.pi/2))) for t in [k/8 for k in range(8, 0, -1)]] + [(x0+breed-m*0.5, opp)]
        zd.polygon(pts, fill=255); lijnen.append(pts)
    vlak(im, D, zeevlak, opp, opp + maxdiep, ((W1, opp), (W2, opp + maxdiep*0.40), (W3, opp + maxdiep*0.78)))
    d = ImageDraw.Draw(im)
    lw = max(2, round(D/150))
    for pts in lijnen: d.line(pts, fill=W0 if not amo(D) else AM[W0], width=lw)
    d.line([(L, opp), (R, opp)], fill=SCHUIM, width=lw)
    for i, (t, sec) in enumerate(tijden):
        xm = L + (i+0.5)*breed
        tekst(d, D, (xm, opp + maxdiep + D*0.065), t, D*0.070, GOUD if sec == 128 else WIT)
    rr = D*0.022; xm = L + 2.5*breed; yb = opp + maxdiep
    d.ellipse([xm-rr, yb-rr, xm+rr, yb+rr], fill=GOUD)
    tekst(d, D, (D/2, D*0.80), 'new best', D*0.068, GOUD)
    rand(im, D); return im

def s_weken(D):
    """Moet-punt 4: de lijn eindigt rechts in de gouden stip van vandaag (2:08, gelijk aan today)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), '8 weeks', D*0.085, TITEL)
    L, R, top, bod = D*0.18, D*0.80, D*0.36, D*0.64
    best = []
    for i in range(56):
        v = 0.30 + 0.56*(i/55)**0.8 + 0.05*math.sin(i*0.55)
        best.append(None if i in (9, 10, 23, 37, 38) else v)
    best[55] = max(b for b in best if b) + 0.06
    hoog = best[55]; best = [b/hoog if b else None for b in best]
    dx = (R-L)/55; Y = lambda v: bod - v*(bod-top)
    vul = []
    for i, b in enumerate(best):
        if b is None:
            l = next(best[j] for j in range(i, -1, -1) if best[j]); r = next(best[j] for j in range(i, 56) if best[j]); b = (l+r)/2
        vul.append((L+i*dx, Y(b)))
    m = Image.new('L', (D, D), 0); ImageDraw.Draw(m).polygon(vul + [(R, bod), (L, bod)], fill=255)
    vlak(im, D, m, top, bod, ((W1, top),))
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    seg = []
    for i, b in enumerate(best + [None]):
        if b is None:
            if len(seg) > 1: d.line(seg, fill=SCHUIM, width=lw, joint='curve')
            seg = []; continue
        seg.append((L+i*dx, Y(b)))
    d.line([(L, bod), (R, bod)], fill=W1 if not amo(D) else AM[W1], width=lw)
    for w in range(9):
        x = L + w*(R-L)/8
        d.line([(x, bod), (x, bod+D*0.02)], fill=GRIJS, width=max(1, round(D/230)))
    r = D*0.024; px_, py_ = R, Y(1.0)
    d.ellipse([px_-r-2, py_-r-2, px_+r+2, py_+r+2], fill=ZWART); d.ellipse([px_-r, py_-r, px_+r, py_+r], fill=GOUD)
    tekst(d, D, (D/2, D*0.755), 'best 2:08 today', D*0.085, GOUD)
    tekst(d, D, (D/2, D*0.845), 'up from 1:05', D*0.068, GRIJS)   # schaal: waar je begon (keuring 5, punt 5)
    rand(im, D); return im, (px_, py_, r)

def s_weken_beeld(D): return s_weken(D)[0]

def s_zeelog(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'sea log', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.27), '3 of 4 found', D*0.068, GRIJS)
    kol = D*0.215; y1 = D*0.425; opp = (D*0.105)**2*0.55
    for k, (soort, t) in enumerate((('vis', '1:00'), ('kwal', '1:30'), ('pad', '2:00'))):
        x = D/2 + (k-1)*kol
        dier(im, soort, x, y1, schaal_voor_gewicht(soort, opp))
        tekst(ImageDraw.Draw(im), D, (x, D*0.545), t, D*0.070, WIT)
    # verborgen walvis: precies dezelfde walvis als silhouet met cyaan rand en een "?" op zijn lijf (moet-punt 8)
    wx, wy, ws = D/2 + WX*D, D*0.675, D*0.105
    k = max(1, round(D/260))
    for ox, oy in ((-k,0),(k,0),(0,-k),(0,k),(-k,-k),(k,k),(-k,k),(k,-k)):
        dier(im, 'walvis', wx+ox, wy+oy, ws, kleur=SCHUIM)
    _, (zx, zy) = dier(im, 'walvis', wx, wy, ws, kleur=W1 if not amo(D) else AM[W1])
    d = ImageDraw.Draw(im)
    tekst(d, D, (wx - ws*0.15, wy - ws*0.02), '?', D*0.085, SCHUIM)
    tekst(d, D, (D/2, D*0.80), 'next 3:00', D*0.070, GRIJS)
    rand(im, D); return im

def pijltjes(d, D, x, y, kleur):
    a = D*0.022    # moet-punt 7: groter (11 px hoog op 260, was 7)
    d.polygon([(x, y-a*1.6), (x+a*0.95, y-a*0.35), (x-a*0.95, y-a*0.35)], fill=kleur)
    d.polygon([(x, y+a*1.6), (x+a*0.95, y+a*0.35), (x-a*0.95, y+a*0.35)], fill=kleur)

def s_instellingen(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'settings', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.330), 'Rounds 3', D*0.068, GRIJS)
    pil(d, D, 0.505, 0.64, 0.25)
    tekst(d, D, (D/2, D*0.448), 'Breaths', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.565), '30', D*0.072, SCHUIM)
    pijltjes(d, D, D/2 - D*0.09, D*0.565, SCHUIM); pijltjes(d, D, D/2 + D*0.09, D*0.565, SCHUIM)
    tekst(d, D, (D/2, D*0.670), 'Buzz on', D*0.068, GRIJS)
    tekst(d, D, (D/2, D*0.765), 'My pattern', D*0.068, GRIJS)
    rand(im, D); return im

def s_veilig(D):
    """Moet-punt 10: de regel voluit, het blok lager. Geen START-boog meer (moet-punt 11: nergens)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    s = D*0.065; y = D*0.215
    d.polygon([(D/2, y-s*0.78), (D/2+s*0.88, y+s*0.66), (D/2-s*0.88, y+s*0.66)], fill=KORAAL)
    tekst(d, D, (D/2, y+s*0.14), '!', s*0.95, W3)
    for k, regel in enumerate(('Never hold your', 'breath in water', 'or while driving.')):
        tekst(d, D, (D/2, D*(0.37 + 0.083*k)), regel, D*0.075, WIT)
    tekst(d, D, (D/2, D*0.635), 'Sit. Stop if dizzy.', D*0.072, GEEL)
    pil(d, D, 0.765, 0.30, 0.11)
    tekst(d, D, (D/2, D*0.765), 'OK', D*0.072, WIT)
    rand(im, D); return im

def s_beloning(D):
    """Moet-punt 6: "turtle found" en "held 2:03"."""
    im = leeg(D)
    zee(im, D, [(D*0.12, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=False, stralen=True)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.22), 'new friend', D*0.085, TITEL)
    bellen(d, D, [(0.27, 0.40, 0.012), (0.24, 0.35, 0.007), (0.74, 0.55, 0.010), (0.77, 0.50, 0.006)])
    dier(im, 'pad', D/2, D*0.465, D*0.17, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.665), 'turtle found', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.77), 'held 2:03 · 3 of 4', D*0.068, WIT)
    rand(im, D); return im

def s_icoon(D):
    """Icoon: walvis in de patrijspoort, vier grote bouten (kan-punt 4: leest op 40 tot 70 px)."""
    im = leeg(D); d = ImageDraw.Draw(im)
    c = D/2; R = D*0.48; r = D*0.425
    d.ellipse([c-R, c-R, c+R, c+R], fill=(0, 120, 120) if amo(D) else RING)
    binnen = Image.new('RGB', (D, D), ZWART)
    zee(binnen, D, [(D*0.06, W0), (D*0.30, W1), (D*0.62, W2), (D*0.80, W3)], amp=D*0.014, stralen=True)
    m = Image.new('L', (D, D), 0); ImageDraw.Draw(m).ellipse([c-r, c-r, c+r, c+r], fill=255)
    im.paste(binnen, (0, 0), m)
    dier(im, 'walvis', c + WX*D, c + D*0.03, r*0.74)
    d = ImageDraw.Draw(im)
    for k in range(0):
        a = math.pi/4 + k*math.pi/2; bx = c+(R+r)/2*math.cos(a); by = c+(R+r)/2*math.sin(a); q = D*0.028
        d.ellipse([bx-q, by-q, bx+q, by+q], fill=(85,170,170))
    return im

SCHERMEN = [('1 menu', s_menu), ('2 ademen', s_ademen), ('3 duiken', s_duiken), ('3b walvis 3:03', s_walvis), ('3c schildpad 2:03', s_schildpad),
            ('3d nieuw dier', s_beloning), ('4 boven', s_boven), ('5 rustig 4-7-8', s_rustig), ('6 today', s_today), ('7 8 weeks', s_weken_beeld),
            ('8 sea log', s_zeelog), ('9 settings', s_instellingen), ('10 veiligheid', s_veilig)]

def teken(fn, D):
    if amo(D):
        return fn(D*SS).resize((D, D), Image.LANCZOS)
    return fn(D)

# ---------------- nameten ----------------
def kader_x(im, D):
    a = np.array(im).astype(int); y, x = np.mgrid[0:D, 0:D]
    r = np.hypot(x+0.5-D/2, y+0.5-D/2)
    niet = (a.sum(axis=2) > 40) & (r < D*0.47)
    xs = np.nonzero(niet.any(axis=0))[0]
    return (xs.min() + xs.max() + 1)/2 - D/2

def optisch_x(im, D):
    """Zwaartepunt van de voorgrond (alles behalve zwart, water, ring en voortgangsspoor). Alleen op 260 (harde kleuren)."""
    a = np.array(im).astype(int)
    achter = [ZWART, W0, W1, W2, W3, RING, ORANJE]
    m = np.ones(a.shape[:2], bool)
    for c in achter: m &= ~((a[:, :, 0] == c[0]) & (a[:, :, 1] == c[1]) & (a[:, :, 2] == c[2]))
    y, x = np.mgrid[0:D, 0:D]; m &= np.hypot(x+0.5-D/2, y+0.5-D/2) < D*0.44
    ys, xs = np.nonzero(m)
    return xs.mean() + 0.5 - D/2

def niet_mip(im):
    a = np.array(im).reshape(-1, 3)
    return int((~np.isin(a, [0, 85, 170, 255]).all(axis=1)).sum())

def kleuren(im): return len(set(map(tuple, np.array(im).reshape(-1, 3))))

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []; beelden = {}
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = teken(fn, D); beelden[(naam, D)] = im; im.save(f'{uit}/ebb-v23-{naam.split()[0]}-{D}.png')
            if D == 260:
                rap.append(f'{D:4d}  {naam:18s} kader x {kader_x(im, D):+5.1f} px   optisch x {optisch_x(im, D):+5.1f} px   pixels buiten MIP {niet_mip(im)}')
            else:
                rap.append(f'{D:4d}  {naam:18s} kader x {kader_x(im, D):+5.1f} px   kleuren {kleuren(im)} (verloop en zachte randen)')
    ic = teken(s_icoon, 560); ic.save(f'{uit}/ebb-v23-icoon-560.png')
    for z in (70, 40): ic.resize((z, z), Image.LANCZOS).save(f'{uit}/ebb-v23-icoon-{z}.png')
    klein = sorted({(t, p) for D, t, p in LOG if D == 260}, key=lambda z: z[1])[:6]
    rap.append('kleinste tekst op 260: ' + ', '.join(f'"{t}" {p} px' for t, p in klein))
    fk = f(20); bb = fk.getbbox('H'); rap.append(f'kapitaalhoogte bij 20 px: {bb[3]-bb[1]} px')
    # het blad
    gap = 30; cel_b = 454 + 24 + 260; kol = 4; cel_h = 454 + 64
    cellen = SCHERMEN + [('icoon (560, 70 en 40 px)', None)]
    rijen = (len(cellen) + kol - 1)//kol
    W = gap + kol*(cel_b + gap); H = 110 + rijen*(cel_h + gap)
    blad = Image.new('RGB', (W, H), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 30), 'Ebb blad v2.3 (Mila): links 454 px AMOLED (verloop, zachte randen), rechts 260 px MIP (harde vlakken), ware grootte',
           font=f(44), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(cellen):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        if fn:
            blad.paste(beelden[(naam, 454)], (x, y)); blad.paste(beelden[(naam, 260)], (x+478, y+194))
        else:
            blad.paste(ic.resize((454, 454), Image.LANCZOS), (x, y))
            blad.paste(ic.resize((70, 70), Image.LANCZOS), (x+478, y+194)); blad.paste(ic.resize((40, 40), Image.LANCZOS), (x+578, y+209))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v2.3.png')
    return rap

if __name__ == '__main__':
    FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v23.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
