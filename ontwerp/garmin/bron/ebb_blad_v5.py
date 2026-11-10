# Ontwerpblad Ebb v5 (Mila, 10 nov run 23): na de keuring van v4.1 door drie frisse beoordelaars (6/6/6)
# en de twee punten van Thijs (T1 eigen dier, T2 de zee wordt echt donkerder).
# Bouwt voort op ebb_blad_v4.py (zelfde zee, letters, dieren, meting).
# Gebruik: python3 ebb_blad_v5.py <uitmap> <pad naar BarlowCondensed-Medium.ttf>
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ebb_blad_v3 as v3
from ebb_blad_v3 import *
import ebb_blad_v4 as v4
from ebb_blad_v4 import hart, omlijnd, dagstippen, HART
from PIL import Image, ImageDraw
from ebb_dieren_v4 import ALLE
import ebb_dieren_v5   # V6: zeekomkommer, otter, zeehond, rog, manta, haai, orka, zwaardvis opnieuw (zet v3.dier_beeld om)
dier = v3.dier

SIL = (0, 85, 255)     # silhouet van een dier dat je nog niet hebt: 3,7:1 op zwart (V2), wel MIP
LICHTCYAAN = (170, 255, 255)
v3.GRIJS = LICHTCYAAN   # K3: ook de kleine "s" op 4 en 5 lichtcyaan in plaats van grijs

# ---------------- de zee wordt donkerder: zes vaste standen, elke 30 s een stap (T2) ----------------
ZEE_STAND = [
    [(0.12, W0), (0.19, W1), (0.62, W2), (0.90, W3)],   # 0:00
    [(0.12, W0), (0.16, W1), (0.50, W2), (0.78, W3)],   # 0:30
    [(0.12, W1), (0.40, W2), (0.68, W3)],               # 1:00
    [(0.12, W1), (0.26, W2), (0.52, W3)],               # 1:30
    [(0.12, W2), (0.40, W3)],                           # 2:00
    [(0.12, W2), (0.22, W3)],                           # 2:30, donkerst
]
def stand(sec):
    """Elke 30 s een stap donkerder; vanaf 3:00 terug naar stand 4 (iets lichter), zodat het water nooit aanmoedigt."""
    if sec >= 180: return 4
    return min(5, sec // 30)

def duik_zee5(im, D, sec):
    zee(im, D, [(D*p, c) for p, c in ZEE_STAND[stand(sec)]], amp=D*0.014, stralen=stand(sec) < 4)
    if amo(D):   # AMOLED: bovenop de banden ook het hele water per stap 10 % donkerder (stap 5 = 50 %)
        k = 1 - 0.10*stand(sec)
        im.paste(Image.eval(im, lambda v: int(v*k)), (0, 0))

def regel_hart_ronde(d, D, y, bpm, ronde):
    """Hartje + bpm en de ronde op één regel, samen gecentreerd (P3)."""
    px = max(D*0.068, MIN*D); fn = f(px); s = px*0.62; gap = px*0.18
    a = str(bpm); b = f'  ·  round {ronde}'
    wa, wb = fn.getlength(a), fn.getlength(b)
    x0 = D/2 - (s + gap + wa + wb)/2
    hart(d, D, x0 + s/2, y, s)
    d.fontmode = 'L' if amo(D) else '1'
    d.text((x0 + s + gap, y), a, font=fn, fill=WIT, anchor='lm')
    d.text((x0 + s + gap + wa, y), b, font=fn, fill=LICHTCYAAN, anchor='lm')
    v3.LOG.append((D if not amo(D) else D//SS, b.strip(), int(round(px if not amo(D) else px/SS))))

def trilicoon(d, D, x, y, s, kleur):
    """Horloge met twee trillijntjes links en rechts."""
    lw = max(2, round(D/150))
    d.rounded_rectangle([x-s*0.28, y-s*0.40, x+s*0.28, y+s*0.40], radius=s*0.10, outline=kleur, width=lw)
    for k in (-1, 1):
        for j in (0.48, 0.66):
            d.line([(x+k*s*j, y-s*0.22), (x+k*s*j, y+s*0.22)], fill=kleur, width=lw)

BELLEN = {30: [(0.30, 0.66, 0.012), (0.27, 0.61, 0.007)],
          105: [(0.70, 0.64, 0.013), (0.73, 0.59, 0.008), (0.68, 0.555, 0.005)],
          184: [(0.33, 0.60, 0.009), (0.69, 0.67, 0.011)]}

def s_duik5(D, sec, ronde, bpm, hoek):
    im = leeg(D); duik_zee5(im, D, sec); d = ImageDraw.Draw(im)
    if sec < 180:
        tekst(d, D, (D/2, D*0.225), 'hold', D*0.085, SCHUIM)
    else:   # na 3:00: bovenaan "time to breathe" met trilicoon, in wit (P4, M5)
        tekst(d, D, (D/2, D*0.225), 'time to breathe', D*0.080, WIT)   # het horloge trilt zacht; geen icoon (las als losse tekens)
    tekst(d, D, (D/2, D*0.42), f'{sec//60}:{sec%60:02d}', D*0.30, WIT)
    bellen(d, D, BELLEN[sec])
    dier(im, 'pad', D/2, D*0.655, D*0.10, hoek=hoek)    # je eigen dier (T1): hier de schildpad die je koos in de sea log
    d = ImageDraw.Draw(im)
    regel_hart_ronde(d, D, D*0.825, bpm, ronde)
    rand(im, D); return im
def s_duik_a(D): return s_duik5(D, 30, 1, 66, -4)
def s_duik_b(D): return s_duik5(D, 105, 2, 61, 3)
def s_duik_c(D): return s_duik5(D, 184, 3, 57, -2)

# ---------------- 1b: korte check bij elke start (S2) ----------------
def s_start(D):
    im = leeg(D)
    zee(im, D, [(D*0.80, W1), (D*0.88, W2)], amp=D*0.010)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'Rounds 3 x 30', D*0.075, TITEL)
    tekst(d, D, (D/2, D*0.38), 'Seated', D*0.12, WIT)
    tekst(d, D, (D/2, D*0.49), 'or lying?', D*0.12, WIT)
    v4.pil(d, D, 0.655, 0.40, 0.13)
    tekst(d, D, (D/2, D*0.655), 'Start', D*0.080, WIT)
    rand(im, D); return im

# ---------------- 2 ademen: geen dubbel getal (P8) ----------------
def s_ademen5(D):
    im = leeg(D)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'in', D*0.095, TITEL)
    tekst(d, D, (D/2, D*0.41), '23', D*0.32, WIT)
    tekst(d, D, (D/2, D*0.80), 'of 30  ·  round 2', D*0.068, WIT)
    rand(im, D); return im

# ---------------- 4 herstel: duidelijk als inhouden (P8), held = tijd uit de sessie (P6) ----------------
def s_boven5(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    zr = D*0.12
    if amo(D):
        gl = Image.new('L', (D, D), 0); ImageDraw.Draw(gl).ellipse([D/2-zr*1.9, D*0.66-zr*1.9, D/2+zr*1.9, D*0.66+zr*1.9], fill=90)
        im.paste(Image.new('RGB', (D, D), (255, 200, 90)), (0, 0), gl.filter(ImageFilter.GaussianBlur(D/30)))
    d.ellipse([D/2-zr, D*0.66-zr, D/2+zr, D*0.66+zr], fill=GEEL)
    zee(im, D, [(D*0.64, W0), (D*0.72, W1), (D*0.86, W2)])
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.175), 'big breath in, hold', D*0.075, TITEL)
    getal_eenheid(d, D, D*0.39, '15', D*0.26, 's', D*0.10, WIT)
    tekst(d, D, (D/2, D*0.80), 'round 2 held 1:45', D*0.068, WIT)
    rand(im, D); return im

# ---------------- 6 today: de hele dag (P7), niet dezelfde drie tijden als het eindscherm ----------------
def s_today5(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), 'today', D*0.085, TITEL)
    opp = D*0.36; L, R = D*0.17, D*0.83
    sessies = [('7:40', [80, 105, 184]), ('21:15', [75, 98, 112])]   # ochtend = 6b, avond = 6c
    maxdiep = D*0.25; breed = (R-L)/6; gat = D*0.07
    zeevlak = Image.new('L', (D, D), 0); zd = ImageDraw.Draw(zeevlak); lijnen = []
    for si, (_, tijden) in enumerate(sessies):
        for j, sec in enumerate(tijden):
            i = si*3 + j; x0 = L + i*breed + (gat if si else -gat)*0.5; dp = maxdiep*sec/184; m = breed*0.10
            pts = [(x0+m, opp)] + [(x0+m + (breed*0.40-m)*t, opp + dp*math.sin(t*math.pi/2)) for t in [k/8 for k in range(1, 9)]]
            pts += [(x0+breed-m - (breed*0.40-m)*t, opp + dp*math.sin(t*math.pi/2)) for t in [k/8 for k in range(8, 0, -1)]] + [(x0+breed-m, opp)]
            zd.polygon(pts, fill=255); lijnen.append(pts)
    vlak(im, D, zeevlak, opp, opp + maxdiep, ((W1, opp), (W2, opp + maxdiep*0.40), (W3, opp + maxdiep*0.78)))
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    for pts in lijnen: d.line(pts, fill=W0 if not amo(D) else AM[W0], width=lw)
    d.line([(L, opp), (R, opp)], fill=SCHUIM, width=lw)
    for si, (klok, _) in enumerate(sessies):
        tekst(d, D, (L + (si*3 + 1.5)*breed + (D*0.035 if si else -D*0.035), opp - D*0.05), klok, D*0.062, WIT)
    tekst(d, D, (D/2, D*0.715), '6 holds · deeper = longer', D*0.062, LICHTCYAAN)
    tekst(d, D, (D/2, D*0.795), 'avg 1:49', D*0.075, WIT)
    rand(im, D); return im

# ---------------- 6b en 6c: hetzelfde skelet (V4) ----------------
def einde_kop5(d, D, tijden=('1:20', '1:45', '3:04')):
    tekst(d, D, (D/2, D*0.150), '3 rounds done', D*0.075, TITEL)          # titel is meteen het label van de tijden (P8)
    xs = (-0.15, 0, 0.15)
    for k, t in enumerate(tijden):
        tekst(d, D, (D/2 + xs[k]*D, D*0.235), t, D*0.068, WIT)           # wit (V3), ruim boven de golf (M5)

def einde_zee(im, D):
    zee(im, D, [(D*0.355, W1), (D*0.62, W2), (D*0.84, W3)], amp=D*0.012, schuim=True, stralen=True)

def s_einde5(D):
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop5(d, D)
    stralenkrans(im, D, D/2, D*0.515)
    d = ImageDraw.Draw(im)
    bellen(d, D, [(0.22, 0.55, 0.012), (0.19, 0.50, 0.007), (0.80, 0.58, 0.010), (0.83, 0.52, 0.006), (0.25, 0.45, 0.005)])
    dier(im, 'ster', D/2, D*0.515, D*0.222)       # ±40 % van de breedte (V5, M4)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.728), 'new friend!', D*0.085, GEEL)
    tekst(d, D, (D/2, D*0.800), 'Starfish · 4 days in a row', D*0.066, WIT)
    dagstippen(d, D, D*0.862, 4)
    rand(im, D); return im

def stralenkrans(im, D, cx, cy):
    """Lichtkrans achter een nieuw dier: 12 smalle stralen. MIP harde 0x55AAFF, AMOLED zacht en vervaagd.
    Op het horloge draait hij langzaam (1 graad per beeld) zolang het scherm open is."""
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m); R = D*0.25
    for k in range(12):
        a = math.radians(k*30 + 8)
        md.polygon([(cx, cy), (cx + R*math.cos(a-0.09), cy + R*math.sin(a-0.09)), (cx + R*math.cos(a+0.09), cy + R*math.sin(a+0.09))], fill=255 if not amo(D) else 120)
    if amo(D): m = m.filter(ImageFilter.GaussianBlur(D/120))
    ImageDraw.Draw(m).rectangle([0, 0, D, D*0.375], fill=0); ImageDraw.Draw(m).rectangle([0, D*0.69, D, D], fill=0)   # niet achter de tekst   # alleen onder water, nooit door de tijden
    im.paste(Image.new('RGB', (D, D), (0, 85, 255) if not amo(D) else (170, 230, 255)), (0, 0), m)

def silhouet(im, D, soort, x, y, s):
    k = max(2, round(D/130))
    for ox, oy in ((-k,0),(k,0),(0,-k),(0,k),(-k,-k),(k,k),(-k,k),(k,-k)):
        dier(im, soort, x+ox, y+oy, s, kleur=LICHTCYAAN)
    dier(im, soort, x, y, s, kleur=ebb_dieren_v5.SPOOK if not amo(D) else {k: AM.get(v, v) for k, v in ebb_dieren_v5.SPOOK.items()})   # N2: vinnen, banden en oog blijven zichtbaar

def s_einde_gewoon5(D):
    """Zelfde plekken als 6b; het dier is hier het silhouet van wie morgen komt, los van de golf."""
    im = leeg(D); einde_zee(im, D)
    d = ImageDraw.Draw(im); einde_kop5(d, D, ('1:15', '1:38', '1:52'))   # de avondsessie van dezelfde dag
    silhouet(im, D, 'clown', D/2, D*0.545, D*0.17)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.728), 'next: Clownfish', D*0.075, WIT)
    tekst(d, D, (D/2, D*0.800), 'in 1 more session', D*0.066, LICHTCYAAN)
    dagstippen(d, D, D*0.862, 4)
    rand(im, D); return im

# ---------------- 7 8 weeks: staven = sessies per week (P5) ----------------
WEKEN = [0, 0, 0, 0, 0, 0, 3, 6]   # nieuwe gebruiker: 9 sessies in totaal (8 bij 6b, 9 na 6c), past bij 7 dieren (M1)
def s_weken5(D):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.18), '8 weeks', D*0.085, TITEL)
    L, R, top, bod = D*0.20, D*0.80, D*0.36, D*0.60
    kol = (R-L)/8; bw = kol*0.70; hoog = 7
    m = Image.new('L', (D, D), 0); md = ImageDraw.Draw(m); kop = []
    for i, n in enumerate(WEKEN):
        xm = L + (i+0.5)*kol; yt = bod - (bod-top)*n/hoog
        md.rounded_rectangle([xm-bw/2, yt, xm+bw/2, bod], radius=bw*0.35, fill=255); kop.append((xm, yt))
    vlak(im, D, m, top, bod, ((W0, top), (W1, top + (bod-top)*0.35), (W2, top + (bod-top)*0.80)))
    d = ImageDraw.Draw(im); lw = max(2, round(D/150))
    for i, (xm, yt) in enumerate(kop):
        d.line([(xm-bw/2+bw*0.2, yt+lw/2), (xm+bw/2-bw*0.2, yt+lw/2)], fill=WIT if i == 7 else SCHUIM, width=lw)
    d.line([(L, bod), (R, bod)], fill=W1 if not amo(D) else AM[W1], width=lw)
    for i, n in enumerate(WEKEN):
        xm = L + (i+0.5)*kol
        if n: tekst(d, D, (xm, bod - (bod-top)*n/hoog - D*0.045), str(n), D*0.062, WIT if i == 7 else LICHTCYAAN)
        else:
            rr = D*0.010; d.ellipse([xm-rr, bod+D*0.03-rr, xm+rr, bod+D*0.03+rr], fill=(0, 85, 170) if not amo(D) else AM[W1])
    tekst(d, D, (D/2, D*0.735), 'sessions per week', D*0.068, LICHTCYAAN)
    tekst(d, D, (D/2, D*0.815), 'avg hold 1:41', D*0.075, WIT)
    rand(im, D); return im

# ---------------- 8 sea log: 3 x 3 per blad, 3 bladen (V1, V2) ----------------
# (oude HINT-tabel weg: het schema staat alleen in SCHEMA)
def s_rooster5(D, pagina, gevonden=7, kies=3):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.135), 'sea log', D*0.075, TITEL)
    if kies >= gevonden:   # wat het gekozen silhouet vraagt, voluit, op de brede regel bovenaan (M3)
        tekst(d, D, (D/2, D*0.205), EIS[kies], D*0.060, WIT)
    else:
        tekst(d, D, (D/2, D*0.205), f'{gevonden} of 24', D*0.062, LICHTCYAAN)
    xs = (-0.25, 0, 0.25); ys = (0.37, 0.555, 0.74)
    opp = (D*0.112)**2*0.55
    for i in range(9):
        n = pagina*9 + i
        if n >= 24: continue
        soort = ALLE[n][0]; r_, k_ = divmod(i, 3)
        x, y = D/2 + xs[k_]*D, (ys[r_] + (0.09 if pagina == 2 else 0))*D
        sc = v3.schaal_voor_gewicht(soort, opp) * (1.15 if soort in ('haai', 'orka', 'manta', 'zwaard', 'walvis') else 1)   # zeldzaam = groter
        if n == kies:
            rr = D*0.098; lw = max(2, round(D/130)); d.ellipse([x-rr, y-rr, x+rr, y+rr], outline=SCHUIM, width=lw)
        if n < gevonden: dier(im, soort, x, y, sc)
        else: silhouet(im, D, soort, x, y, sc*0.92)
        d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.875), f'{pagina+1} / 3', D*0.058, LICHTCYAAN)
    rand(im, D); return im
def s_rooster_1(D): return s_rooster5(D, 0)
def s_rooster_2(D): return s_rooster5(D, 1, kies=9)
def s_rooster_3(D): return s_rooster5(D, 2, kies=22)
SESSIES_NU = 9
# Schema v5.3 (productkeuring): dagen op rij hoogstens 7, daarna alleen sessies, zodat wie 4 keer per week ademt alle 24 haalt
SCHEMA = ['1x', '2x', '2d', '3d', '4x', '6x', '4d', '10x', '5d', '12x', '14x', '16x', '6d', '18x', '20x',
          '22x', '7d', '25x', '28x', '32x', '36x', '42x', 'break', '50x']
def _eis(n):
    naam = ALLE[n][1]; drempel = SCHEMA[n]
    if drempel == 'break': return 'comes after a break'   # naam blijft een verrassing
    if drempel.endswith('x'): return f'{naam} · {int(drempel[:-1]) - SESSIES_NU} more sessions'
    return f'{naam} · {drempel[:-1]} days in a row'
EIS = {n: _eis(n) for n in range(24)}

# ---------------- 8c sea log, één dier: jouw maatje kiezen (T1), geen 24 stippen (V7) ----------------
def s_zeelog5(D):
    im = leeg(D)
    zee(im, D, [(D*0.30, W2), (D*0.75, W3)], amp=D*0.010, schuim=False)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.16), 'sea log', D*0.075, TITEL)
    bellen(d, D, [(0.29, 0.44, 0.010), (0.72, 0.38, 0.007)])
    dier(im, 'pad', D/2, D*0.415, D*0.15, hoek=-6)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.585), 'Turtle', D*0.090, WIT)
    tekst(d, D, (D/2, D*0.665), 'found: 3 days in a row', D*0.066, LICHTCYAAN)
    v4.pil(d, D, 0.775, 0.56, 0.11)
    tekst(d, D, (D/2, D*0.775), 'swims with you: on', D*0.066, WIT)   # toestand aan; START zet hem uit
    rand(im, D); return im

# ---------------- 9 instellingen: alles uit besluit punt 5, gewone woorden (P1) ----------------
def instel(D, boven, label, waarde, onder):
    im = leeg(D); d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.20), 'settings', D*0.085, TITEL)
    tekst(d, D, (D/2, D*0.330), boven, D*0.068, LICHTCYAAN)
    v4.pil(d, D, 0.505, 0.66, 0.25)
    tekst(d, D, (D/2, D*0.448), label, D*0.085, WIT)
    tekst(d, D, (D/2, D*0.565), waarde, D*0.072, SCHUIM)
    for k, t in enumerate(onder):
        tekst(d, D, (D/2, D*(0.680 + 0.090*k)), t, D*0.068, LICHTCYAAN)
    rand(im, D); return im
def s_instel_a(D): return instel(D, 'Rounds  3', 'Breathing pace', '10 per min', ['Breaths  30', 'Buzz every 30 s  on'])
def s_instel_b(D): return instel(D, 'Buzz last 3 breaths  on', 'Buzz only', 'on (no sound)', ['Touch lock  on', 'Safety info'])

# ---------------- 10 veiligheid: drie korte bladen, gelijk aan de code (S1) ----------------
def veilig(D, regels, geel, knop, driehoek=True):
    im = leeg(D); d = ImageDraw.Draw(im)
    if driehoek:
        s = D*0.055; y = D*0.165
        d.polygon([(D/2, y-s*0.78), (D/2+s*0.88, y+s*0.66), (D/2-s*0.88, y+s*0.66)], fill=KORAAL)
        tekst(d, D, (D/2, y+s*0.14), '!', s*0.95, W3)
    y0 = 0.30
    for k, r in enumerate(regels):
        tekst(d, D, (D/2, D*(y0 + 0.078*k)), r, D*0.070, WIT)
    if geel: tekst(d, D, (D/2, D*(y0 + 0.078*len(regels) + 0.01)), geel, D*0.070, GEEL)
    v4.pil(d, D, 0.79, 0.30, 0.11)
    tekst(d, D, (D/2, D*0.79), knop, D*0.068, WIT)
    rand(im, D); return im
def s_veilig_a(D): return veilig(D, ['Sit or lie down.', 'Never standing,', 'never in or near water,', 'never while driving.'], None, 'Next')
def s_veilig_b(D): return veilig(D, ['You can faint', 'without warning.', 'Never force a hold.', 'Stop if dizzy.'], None, 'Next')
def s_veilig_c(D): return veilig(D, ['Not if pregnant,', 'under 18, epilepsy,', 'heart or blood', 'pressure problems.'], 'Not a medical device.', 'OK')

def s_menu5(D):
    im = leeg(D)
    dier(im, 'pad', D/2, D*0.855, D*0.085, hoek=-4)      # je eigen dier ligt in het lage tij (M8), niet de onverdiende walvis
    zee(im, D, [(D*0.882, W1), (D*0.945, W2)], amp=D*0.008)
    d = ImageDraw.Draw(im)
    tekst(d, D, (D/2, D*0.165), 'Ebb', D*0.10, TITEL)
    v4.pil(d, D, 0.345, 0.60, 0.15)
    tekst(d, D, (D/2, D*0.345), 'Rounds  3 x 30', D*0.080, WIT)
    omlijnd(d, D, 0.515, 0.60, 0.15)
    tekst(d, D, (D/2, D*0.515), 'Calm  4-7-8', D*0.080, WIT)
    tekst(d, D, (D/2, D*0.660), 'Sea log  ·  Settings', D*0.066, LICHTCYAAN)
    rand(im, D); return im

SCHERMEN = [('1 menu', s_menu5), ('1b start', s_start), ('2 ademen', s_ademen5), ('3a hold 0:30', s_duik_a),
            ('3b hold 1:45', s_duik_b), ('3c hold 3:04', s_duik_c), ('4 herstel', s_boven5), ('5 rustig 4-7-8', v3.s_rustig),
            ('6 today', s_today5), ('6b einde met dier', s_einde5), ('6c einde zonder dier', s_einde_gewoon5), ('7 8 weeks', s_weken5),
            ('8 sea log 1 van 3', s_rooster_1),  ('8b sea log 2 van 3', s_rooster_2), ('8d sea log 3 van 3', s_rooster_3), ('8c sea log dier', s_zeelog5),
            ('9 settings', s_instel_a), ('9b settings', s_instel_b), ('10 veilig 1', s_veilig_a), ('10b veilig 2', s_veilig_b),
            ('10c veilig 3', s_veilig_c)]

def tekst_binnen(im, D):
    """Grootste afstand van een niet-water, niet-zwarte pixel tot het midden, als deel van de straal (veilige cirkel 0,80)."""
    a = np.array(im).astype(int); achter = [ZWART, W0, W1, W2, W3, RING, SIL, (85,170,255), GEEL] if not amo(D) else []
    m = a.sum(axis=2) > 0
    for c in achter: m &= ~((a[:, :, 0] == c[0]) & (a[:, :, 1] == c[1]) & (a[:, :, 2] == c[2]))
    y, x = np.mgrid[0:D, 0:D]; r = np.hypot(x+0.5-D/2, y+0.5-D/2)/(D/2)
    m &= r < 0.97
    return float(r[m].max()) if m.any() else 0

def strook(uit):
    """Zes zee-standen naast elkaar, op 260 (MIP), zodat je in één blik ziet dat het water elke 30 s donkerder wordt."""
    D = 260; gap = 16; W = gap + 7*(D + gap); im = Image.new('RGB', (W, D + 70), (14, 16, 24)); d = ImageDraw.Draw(im)
    for i, sec in enumerate((0, 30, 60, 90, 120, 150, 180)):
        s = leeg(D); duik_zee5(s, D, sec); rand(s, D)
        im.paste(s, (gap + i*(D+gap), 10))
        d.text((gap + i*(D+gap) + D/2, D + 40), f'{sec//60}:{sec%60:02d}' + ('+' if sec == 180 else ''), font=f(30), fill=(200, 220, 235), anchor='mm')
    im.save(f'{uit}/zee-standen-260.png')

def maak(uit):
    os.makedirs(uit, exist_ok=True); rap = []; beelden = {}
    for D in (454, 260):
        for naam, fn in SCHERMEN:
            im = teken(fn, D); beelden[(naam, D)] = im; im.save(f'{uit}/ebb-v5-{naam.split()[0]}-{D}.png')
            if D == 260:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px   optisch x {optisch_x(im, D):+5.1f} px   buiten MIP {niet_mip(im)}   verst {tekst_binnen(im, D):.2f} R')
            else:
                rap.append(f'{D:4d}  {naam:22s} kader x {kader_x(im, D):+5.1f} px')
    klein = sorted({(t, p) for D, t, p in v3.LOG if D == 260}, key=lambda z: z[1])[:6]
    rap.append('kleinste tekst op 260: ' + ', '.join(f'"{t}" {p} px' for t, p in klein))
    strook(uit)
    gap = 30; cel_b = 454 + 24 + 260; kol = 4; cel_h = 454 + 64
    rijen = (len(SCHERMEN) + kol - 1)//kol
    W = gap + kol*(cel_b + gap); H = 110 + rijen*(cel_h + gap)
    blad = Image.new('RGB', (W, H), (14, 16, 24)); d = ImageDraw.Draw(blad)
    d.text((gap, 30), 'Ebb blad v5 (Mila): je eigen dier zwemt mee, de zee wordt elke 30 s donkerder. Links 454 AMOLED, rechts 260 MIP, ware grootte',
           font=f(44), fill=(220, 230, 240))
    for i, (naam, fn) in enumerate(SCHERMEN):
        r, k = divmod(i, kol); x = gap + k*(cel_b + gap); y = 110 + r*(cel_h + gap)
        blad.paste(beelden[(naam, 454)], (x, y)); blad.paste(beelden[(naam, 260)], (x+478, y+194))
        d.text((x, y+462), naam, font=f(32), fill=(170, 190, 210))
    blad.save(f'{uit}/../ebb-blad-v5.png')
    # de drie inhoudschermen naast elkaar (T2)
    rij = Image.new('RGB', (3*454 + 4*30, 454 + 80), (14, 16, 24)); d = ImageDraw.Draw(rij)
    for i, naam in enumerate(('3a hold 0:30', '3b hold 1:45', '3c hold 3:04')):
        rij.paste(beelden[(naam, 454)], (30 + i*484, 20)); d.text((30 + i*484 + 227, 500), naam, font=f(32), fill=(200, 220, 235), anchor='mm')
    rij.save(f'{uit}/drie-holds-454.png')
    return rap

if __name__ == '__main__':
    v3.FONT = sys.argv[2]
    rap = maak(sys.argv[1])
    print('\n'.join(rap))
    with open(os.path.join(sys.argv[1], 'meting-v5.txt'), 'w') as fh: fh.write('\n'.join(rap) + '\n')
