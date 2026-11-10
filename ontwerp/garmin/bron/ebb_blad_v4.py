# Ontwerpblad Ebb v4 (Mila, 10 nov run 21): volgt besluit 22:53 (dieren voor trouw, geen meters, geen doelring,
# nieuw dier pas aan het eind, menu met twee gelijke keuzes, 8 weeks met gemiddelde en dagen per week,
# live hartslag klein op het duikscherm, instellingen voor tempo en tik).
# Bouwt voort op ebb_blad_v3.py (zelfde zee, letters, dieren, meting).
# Gebruik: python3 ebb_blad_v4.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
from ebb_blad_v3 import *
from PIL import Image, ImageDraw
import ebb_dieren_v4 as dv4   # alle 24 dieren (zet v3.dier_beeld om)
from ebb_dieren_v4 import ALLE
dier = v3.dier

HART = (255, 85, 85)

def hart(d, D, x, y, s, kleur=HART):
    """Klein hartje: twee rondjes en een punt."""
    r = s*0.30
    d.ellipse([x-s*0.5, y-s*0.35, x-s*0.5+2*r, y-s*0.35+2*r], fill=kleur)
    d.ellipse([x+s*0.5-2*r, y-s*0.35, x+s*0.5, y-s*0.35+2*r], fill=kleur)
    d.polygon([(x-s*0.5, y-s*0.05), (x+s*0.5, y-s*0.05), (x, y+s*0.48)], fill=kleur)

def hartslag(d, D, y, bpm):
    """Live hartslag klein: hartje plus getal, samen gecentreerd."""
    px = max(D*0.068, MIN*D); fn = f(px); w = fn.getlength(str(bpm)); s = px*0.62; gap = px*0.18
    x0 = D/2 - (s + gap + w)/2
    hart(d, D, x0 + s/2, y, s)
    d.fontmode = 'L' if amo(D) else '1'
    d.text((x0 + s + gap, y), str(bpm), font=fn, fill=WIT, anchor='lm')
    v3.LOG.append((D if not amo(D) else D//SS, str(bpm), int(round(px if not amo(D) else px/SS))))

def omlijnd(d, D, y, w, h, kleur=W1):
    lw = max(2, round(D/130))
    k = kleur if not amo(D) else AM[kleur]
    d.rounded_rectangle([D/2-w*D/2, y*D-h*D/2, D/2+w*D/2, y*D+h*D/2], radius=h*D/2, outline=k, width=lw)

# ---------------- 1 menu: twee gelijke keuzes ----------------
def s_menu(D):
    im = leeg(D)
    s = D*0.10; wx = D/2 + WX*D
    dier(im, 'walvis', wx, D*0.875, s)
    d = ImageDraw.Draw(im); spuit(d, D, wx - 0.36*s, D*0.875 - 0.42*s, s)
    zee(im, D, [(D*0.882, W1), (D*0.945, W2)], amp=D*0.008)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.165), 'Ebb', D*0.10, TITEL)
    # twee pillen van dezelfde maat; de gekozen is gevuld, de andere omlijnd
    pil(d, D, 0.345, 0.60, 0.15)
    tekst(d, D, (D/2, D*0.345), 'Rounds  3 x 30', D*0.080, WIT)
    omlijnd(d, D, 0.515, 0.60, 0.15)
    tekst(d, D, (D/2, D*0.515), 'Calm  4-7-8', D*0.080, WIT)
    tekst(d, D, (D/2, D*0.660), 'Sea log  ·  Settings', D*0.066, GRIJS)
    rand(im, D); return im

# ---------------- 3 duiken: geen meters, geen ring; de zee wordt donkerder; je maatje zwemt mee ----------------
def duik_zee_t(im, D, sec):
    k = min(1, sec/180)
    zee(im, D, [(D*0.12, W0), (D*(0.19 - 0.04*k), W1), (D*(0.62 - 0.30*k), W2), (D*(0.90 - 0.32*k), W3)], amp=D*0.014, stralen=True)

def s_duik4(D, sec, soort, s, bpm, onder=None, hoek=0):
    im = leeg(D); duik_zee_t(im, D, sec); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.235), 'hold', D*0.085, SCHUIM)
    tekst(d, D, (D/2, D*0.43), f'{sec//60}:{sec%60:02d}', D*0.30, WIT)
    bellen(d, D, [(0.31, 0.64, 0.014), (0.28, 0.59, 0.008), (0.69, 0.62, 0.010), (0.72, 0.58, 0.006)])
    cx = D/2 + (WX*D if soort == 'walvis' else 0)
    dier(im, soort, cx, D*0.665, s*D, hoek=hoek)
    d = ImageDraw.Draw(im)
    if onder:
        tekst(d, D, (D/2, D*0.835), onder, D*0.068, GEEL)
    else:
        hartslag(d, D, D*0.835, bpm)
    rand(im, D); return im
def s_duik_vroeg(D): return s_duik4(D, 48, 'kwal', 0.085, 64)
def s_duik_laat(D):  return s_duik4(D, 154, 'kwal', 0.085, 58)
def s_duik_3min(D):  return s_duik4(D, 184, 'kwal', 0.085, 56, onder='breathe when ready')

# ---------------- 6 today: tijden zichtbaar, geen beloning ----------------
def s_today(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'today', D*0.085, TITEL)
    opp = D*0.33; L, R = D*0.17, D*0.83; breed = (R-L)/3
    tijden = [('1:20', 80), ('1:45', 105), ('2:08', 128)]; maxdiep = D*0.27
    zeevlak = Image.new('L', (D, D), 0); zd = ImageDraw.Draw(zeevlak); lijnen = []
    for i, (_, sec) in enumerate(tijden):
        x0 = L + i*breed; dp = maxdiep*sec/128; m = breed*0.16
        pts = [(x0+m*0.5, opp)] + [(x0+m*0.5 + (breed*0.30)*t, opp + dp*(math.sin(t*math.pi/2))) for t in [k/8 for k in range(1, 9)]]
        pts += [(x0+breed-m*0.5 - (breed*0.30)*t, opp + dp*(math.sin(t*math.pi/2))) for t in [k/8 for k in range(8, 0, -1)]] + [(x0+breed-m*0.5, opp)]
        zd.polygon(pts, fill=255); lijnen.append(pts)
    vlak(im, D, zeevlak, opp, opp + maxdiep, ((W1, opp), (W2, opp + maxdiep*0.40), (W3, opp + maxdiep*0.78)))
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    for pts in lijnen: d.line(pts, fill=W0 if not amo(D) else AM[W0], width=lw)
    d.line([(L, opp), (R, opp)], fill=SCHUIM, width=lw)
    for i, (t, sec) in enumerate(tijden):
        tekst(d, D, (L + (i+0.5)*breed, opp + maxdiep + D*0.065), t, D*0.070, WIT)
    tekst(d, D, (D/2, D*0.80), 'avg 1:44', D*0.068, GRIJS)
    rand(im, D); return im

# ---------------- 6b einde sessie: nieuw dier voor trouw ----------------
def dagstippen(d, D, y, n_vol, n=7):
    r = D*0.016; gap = D*0.052; x0 = D/2 - gap*(n-1)/2
    for i in range(n):
        x = x0 + i*gap
        if i < n_vol: d.ellipse([x-r, y-r, x+r, y+r], fill=SCHUIM)
        else: d.ellipse([x-r, y-r, x+r, y+r], outline=(W0 if not amo(D) else AM[W0]), width=max(1, round(D/150)))

def s_einde(D):
    im = leeg(D)
    zee(im, D, [(D*0.12, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=False, stralen=True)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'new friend', D*0.080, TITEL)
    bellen(d, D, [(0.27, 0.40, 0.012), (0.24, 0.35, 0.007), (0.74, 0.50, 0.010), (0.77, 0.45, 0.006)])
    dier(im, 'pad', D/2, D*0.425, D*0.16, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.615), 'Turtle', D*0.095, WIT)
    tekst(d, D, (D/2, D*0.705), '3 days in a row', D*0.068, GEEL)
    dagstippen(d, D, D*0.795, 3)
    rand(im, D); return im

# ---------------- 7 8 weeks: gemiddelde per sessie per week plus dagen per week ----------------
WEKEN = [(62, 2), (70, 3), (66, 2), (81, 4), (88, 5), (85, 3), (97, 5), (104, 5)]   # (gemiddelde s, dagen)
def s_weken(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), '8 weeks', D*0.085, TITEL)
    L, R, top, bod = D*0.20, D*0.80, D*0.30, D*0.58
    kol = (R-L)/8; bw = kol*0.70; hoog = 110
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m); kop = []
    for i, (sec, _) in enumerate(WEKEN):
        xm = L + (i+0.5)*kol; yt = bod - (bod-top)*sec/hoog
        md.rounded_rectangle([xm-bw/2, yt, xm+bw/2, bod], radius=bw*0.35, fill=255)
        kop.append((xm, yt))
    vlak(im, D, m, top, bod, ((W0, top), (W1, top + (bod-top)*0.35), (W2, top + (bod-top)*0.80)))
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    for i, (xm, yt) in enumerate(kop):   # schuimrandje op elke kolom, deze week wit
        d.line([(xm-bw/2+bw*0.2, yt+lw/2), (xm+bw/2-bw*0.2, yt+lw/2)], fill=WIT if i == 7 else SCHUIM, width=lw)
    d.line([(L, bod), (R, bod)], fill=W1 if not amo(D) else AM[W1], width=lw)
    for i, (_, dagen) in enumerate(WEKEN):   # dagen per week als cijfer onder de kolom
        tekst(d, D, (L + (i+0.5)*kol, bod + D*0.055), str(dagen), D*0.062, WIT if i == 7 else GRIJS)
    tekst(d, D, (D/2, D*0.735), 'avg 1:44', D*0.085, WIT)
    tekst(d, D, (D/2, D*0.825), '5 days this week', D*0.068, GRIJS)
    rand(im, D); return im

# ---------------- 8 sea log: verzamelen over weken (24 dieren) ----------------
def s_zeelog(D):
    im = leeg(D)
    zee(im, D, [(D*0.30, W2), (D*0.75, W3)], amp=D*0.010, schuim=False)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.16), 'sea log', D*0.080, TITEL)
    # 24 stippen in twee rijen: gevonden = schuim, nog niet = open ring
    r = D*0.011; gap = D*0.040; y0 = D*0.245
    for rij in range(2):
        for i in range(12):
            x = D/2 + (i-5.5)*gap; y = y0 + rij*gap*0.95; k = rij*12 + i
            if k < 7: d.ellipse([x-r, y-r, x+r, y+r], fill=SCHUIM)
            else: d.ellipse([x-r, y-r, x+r, y+r], outline=(W0 if not amo(D) else AM[W0]), width=max(1, round(D/200)))
    bellen(d, D, [(0.30, 0.50, 0.010), (0.70, 0.44, 0.007)])
    dier(im, 'ster', D/2, D*0.465, D*0.10)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.625), 'Starfish', D*0.085, WIT)
    tekst(d, D, (D/2, D*0.705), '4 days in a row', D*0.068, GRIJS)
    tekst(d, D, (D/2, D*0.800), '7 of 24', D*0.068, SCHUIM)
    rand(im, D); return im

def s_zeelog_open(D):
    """Een dier dat je nog niet hebt: silhouet plus hoe je het krijgt (eerlijk, geen raadsel)."""
    im = leeg(D)
    zee(im, D, [(D*0.30, W2), (D*0.75, W3)], amp=D*0.010, schuim=False)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.16), 'sea log', D*0.080, TITEL)
    wx, wy, ws = D/2 + WX*D, D*0.46, D*0.12
    k = max(1, round(D/260))
    for ox, oy in ((-k,0),(k,0),(0,-k),(0,k),(-k,-k),(k,k),(-k,k),(k,-k)):
        dier(im, 'walvis', wx+ox, wy+oy, ws, kleur=SCHUIM)
    dier(im, 'walvis', wx, wy, ws, kleur=W2 if not amo(D) else AM[W2])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.625), '?', D*0.085, SCHUIM)
    tekst(d, D, (D/2, D*0.705), '50 sessions', D*0.068, GRIJS)
    tekst(d, D, (D/2, D*0.800), 'no. 24', D*0.068, GRIJS)
    rand(im, D); return im

# ---------------- 9 instellingen: tempo erbij ----------------
def s_instellingen(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'settings', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.330), 'Breaths 30', D*0.068, GRIJS)
    pil(d, D, 0.505, 0.64, 0.25)
    tekst(d, D, (D/2, D*0.448), 'Pace', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.565), 'normal', D*0.072, SCHUIM)
    pijltjes(d, D, D/2 - D*0.135, D*0.565, SCHUIM); pijltjes(d, D, D/2 + D*0.135, D*0.565, SCHUIM)
    tekst(d, D, (D/2, D*0.670), 'Hold tick on', D*0.068, GRIJS)
    tekst(d, D, (D/2, D*0.765), 'Last 3 buzz on', D*0.068, GRIJS)
    rand(im, D); return im

# ---------------- 6b/6c einde sessie ----------------
def einde_kop(d, D):
    tekst(d, D, (D/2, D*0.175), 'session done', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.265), '1:20 · 1:45 · 2:08', D*0.066, GRIJS)

def s_einde(D):
    im = leeg(D)
    zee(im, D, [(D*0.12, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=False, stralen=True)
    d = ImageDraw.Draw(im); einde_kop(d, D)
    bellen(d, D, [(0.29, 0.44, 0.011), (0.26, 0.40, 0.006), (0.72, 0.47, 0.009)])
    dier(im, 'pad', D/2, D*0.445, D*0.135, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.615), 'new friend: Turtle', D*0.080, WIT)
    tekst(d, D, (D/2, D*0.700), '3 days in a row', D*0.068, GEEL)
    dagstippen(d, D, D*0.790, 3)
    rand(im, D); return im

def s_einde_gewoon(D):
    """De meeste sessies: geen nieuw dier. Dan reeks plus wie er hierna komt (op trouw, niet op inhoudtijd)."""
    im = leeg(D)
    zee(im, D, [(D*0.12, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=False, stralen=True)
    d = ImageDraw.Draw(im); einde_kop(d, D)
    tekst(d, D, (D/2, D*0.375), '4 days in a row', D*0.085, WIT)
    dagstippen(d, D, D*0.465, 4)
    ws = D*0.075; k = max(1, round(D/260))
    for ox, oy in ((-k,0),(k,0),(0,-k),(0,k)):
            dier(im, 'clown', D/2+ox, D*0.595+oy, ws, kleur=SCHUIM)
    dier(im, 'clown', D/2, D*0.595, ws, kleur=W2 if not amo(D) else AM[W2])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.745), 'Clownfish in 2 sessions', D*0.068, GRIJS)
    rand(im, D); return im

# ---------------- 8 sea log als verzamelboek: 12 per pagina ----------------
def s_rooster(D, pagina, gevonden=7, kies=6):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.165), 'sea log', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.245), f'{gevonden} of 24', D*0.066, GRIJS)
    xs = (-0.30, -0.10, 0.10, 0.30); ys = (0.385, 0.535, 0.685)
    opp = (D*0.072)**2*0.55
    for i in range(12):
        n = pagina*12 + i; soort = ALLE[n][0]; r_, k_ = divmod(i, 4)
        x, y = D/2 + xs[k_]*D, ys[r_]*D
        sc = v3.schaal_voor_gewicht(soort, opp)
        if n == kies:   # cursor: ring in schuim om het gekozen dier
            rr = D*0.072; lw = max(2, round(D/130)); d.ellipse([x-rr, y-rr, x+rr, y+rr], outline=SCHUIM, width=lw)
        if n < gevonden: dier(im, soort, x, y, sc)
        else: dier(im, soort, x, y, sc, kleur=W1 if not amo(D) else AM[W1])
        d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.815), f'{pagina+1} / 2', D*0.066, GRIJS)
    rand(im, D); return im
def s_rooster1(D): return s_rooster(D, 0)
def s_rooster2(D): return s_rooster(D, 1, kies=-1)

SCHERMEN = [('1 menu', s_menu), ('2 ademen', v3.s_ademen), ('3 duiken 0:48', s_duik_vroeg), ('3b duiken 2:34', s_duik_laat),
            ('3c na 3 min', s_duik_3min), ('4 boven', v3.s_boven), ('5 rustig 4-7-8', v3.s_rustig), ('6 today', s_today),
            ('6b einde met dier', s_einde), ('6c einde zonder dier', s_einde_gewoon), ('7 8 weeks', s_weken),
            ('8 sea log blad 1', s_rooster1), ('8b sea log blad 2', s_rooster2), ('8c sea log dier', s_zeelog),
            ('9 settings', s_instellingen), ('10 veiligheid', v3.s_veilig)]

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []; beelden = {}
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = teken(fn, D); beelden[(naam, D)] = im; im.save(f'{uit}/ebb-v4-{naam.split()[0]}-{D}.png')
            if D == 260:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px   optisch x {optisch_x(im, D):+5.1f} px   pixels buiten MIP {niet_mip(im)}')
            else:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px   kleuren {kleuren(im)}')
    klein = sorted({(t, p) for D, t, p in v3.LOG if D == 260}, key=lambda z: z[1])[:6]
    rap.append('kleinste tekst op 260: ' + ', '.join(f'"{t}" {p} px' for t, p in klein))
    gap = 30; cel_b = 454 + 24 + 260; kol = 4; cel_h = 454 + 64
    rijen = (len(SCHERMEN) + kol - 1)//kol
    W = gap + kol*(cel_b + gap); H = 110 + rijen*(cel_h + gap)
    blad = Image.new('RGB', (W, H), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 30), 'Ebb blad v4.1 (Mila): dieren voor trouw, geen meters, geen doelring. Links 454 AMOLED, rechts 260 MIP, ware grootte',
           font=f(44), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        blad.paste(beelden[(naam, 454)], (x, y)); blad.paste(beelden[(naam, 260)], (x+478, y+194))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v4.png')
    return rap

if __name__ == '__main__':
    v3.FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v4.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
