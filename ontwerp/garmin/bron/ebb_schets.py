# Mila 10 nov: schets van de schermen van Ebb (Garmin), op 260 en 454 px, alleen MIP-kleuren (64 kleuren, geen verloop,
# geen zachte randen), zodat Gijs het 1 op 1 kan nabouwen met dc.fillPolygon / fillCircle / drawText.
# Alle maten zijn een deel van de diameter D, dus gelijk op elk horloge. Gebruik: python3 ebb_schets.py <uitmap>
import math, sys, os
from PIL import Image, ImageDraw, ImageFont

ZWART = (0, 0, 0)
WIT = (255, 255, 255)
SCHUIM = (0x55, 0xFF, 0xFF)       # rand van de golf
DIEPTE = [(0x00, 0xAA, 0xAA),     # aan de oppervlakte en 0 tot 15 s
          (0x00, 0x55, 0xAA),     # 15 tot 30 s
          (0x00, 0x00, 0xAA),     # 30 tot 45 s
          (0x00, 0x00, 0x55)]     # 45 s en dieper
ZACHT = (0x55, 0xAA, 0xAA)        # kleine tekst
BEL = (0x55, 0xAA, 0xFF)
KORAAL = (0xFF, 0x55, 0x55)       # alleen dieren en een nieuw record
LICHT = (0xFF, 0xFF, 0xAA)        # lichtpuntje bij de diepste ronde

def letter(px, vet=True):
    f = "/usr/share/fonts/opentype/inter/Inter-Bold.otf" if vet else "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
    return ImageFont.truetype(f, max(8, int(px)))

def golf(D, peil, fase, amp=0.025, golven=2.5):
    """Punten van de waterlijn: peil = hoogte van het water als deel van D vanaf de onderkant."""
    y0 = D * (1 - peil)
    pts = []
    for x in range(0, D + 1, 2):
        pts.append((x, y0 + D * amp * math.sin(2 * math.pi * golven * x / D + fase)))
    return pts

def water(d, D, peil, kleur, fase=0.0):
    pts = golf(D, peil, fase)
    d.polygon(pts + [(D, D), (0, D)], fill=kleur)
    d.line(pts, fill=SCHUIM, width=max(2, D // 110))

def bellen(d, D, lijst):
    for (x, y, r) in lijst:
        d.ellipse((x * D - r * D, y * D - r * D, x * D + r * D, y * D + r * D), outline=BEL, width=max(1, D // 180))

def midden_tekst(d, D, y, tekst, px, kleur, vet=True):
    f = letter(px, vet)
    w = d.textlength(tekst, font=f)
    d.text(((D - w) / 2, y * D), tekst, font=f, fill=kleur, anchor="la")

def kwal(d, D, cx, cy, s):
    """Kwal van ±0,12 D: koepel en drie slierten, in koraal. Zwemt in 6 s van rechts naar links."""
    r = s * D
    d.pieslice((cx * D - r, cy * D - r, cx * D + r, cy * D + r), 180, 360, fill=KORAAL)
    for i in (-1, 0, 1):
        x = cx * D + i * r * 0.6
        pts = [(x + (r * 0.12 if k % 2 else -r * 0.12), cy * D + k * r * 0.28) for k in range(5)]
        d.line(pts, fill=KORAAL, width=max(2, D // 130))

def scherm_ademen(D):
    im = Image.new("RGB", (D, D), ZWART); d = ImageDraw.Draw(im)
    water(d, D, 0.58, DIEPTE[0], 0.8)
    midden_tekst(d, D, 0.13, "in", D * 0.075, ZACHT, False)
    midden_tekst(d, D, 0.38, "23", D * 0.30, WIT)
    midden_tekst(d, D, 0.73, "of 30 · round 2", D * 0.06, WIT, False)
    return im

def scherm_duiken(D):
    im = Image.new("RGB", (D, D), ZWART); d = ImageDraw.Draw(im)
    # 1:34 ingehouden: het hele scherm is water in de diepste tint, de oppervlakte is een smalle streep bovenaan
    water(d, D, 0.93, DIEPTE[3], 2.0)
    bellen(d, D, [(0.30, 0.62, 0.018), (0.33, 0.52, 0.012), (0.70, 0.40, 0.015), (0.68, 0.30, 0.009)])
    kwal(d, D, 0.76, 0.66, 0.06)
    midden_tekst(d, D, 0.30, "1:34", D * 0.27, WIT)
    midden_tekst(d, D, 0.62, "94 m", D * 0.075, ZACHT, False)
    return im

def scherm_boven(D):
    im = Image.new("RGB", (D, D), ZWART); d = ImageDraw.Draw(im)
    # herstel: diep inademen en 15 s vast. Het water schiet omhoog met een plons belletjes
    water(d, D, 0.80, DIEPTE[0], 4.0)
    bellen(d, D, [(0.22, 0.20, 0.022), (0.30, 0.12, 0.014), (0.50, 0.08, 0.018), (0.70, 0.13, 0.012), (0.78, 0.22, 0.020)])
    midden_tekst(d, D, 0.30, "12", D * 0.30, WIT)
    midden_tekst(d, D, 0.66, "hold · recover", D * 0.065, WIT, False)
    return im

def scherm_profiel(D, record=True):
    im = Image.new("RGB", (D, D), ZWART); d = ImageDraw.Draw(im)
    midden_tekst(d, D, 0.12, "today", D * 0.06, ZACHT, False)
    tijden = [72, 98, 131]                     # s per ronde
    opp = 0.32 * D; bodem = 0.70 * D; diepst = max(tijden)
    x0, x1 = 0.16 * D, 0.84 * D
    d.line((x0 - 0.04 * D, opp, x1 + 0.04 * D, opp), fill=ZACHT, width=max(1, D // 160))
    n = len(tijden); w = (x1 - x0) / n
    tip_beste = None
    for i, t in enumerate(tijden):
        a, b = x0 + i * w, x0 + (i + 1) * w
        y = opp + (bodem - opp) * t / diepst
        tip = ((a + b) / 2, y)
        d.polygon([(a, opp), tip, (b, opp)], fill=DIEPTE[1 + min(2, i)])
        d.line([(a, opp), tip, (b, opp)], fill=SCHUIM, width=max(2, D // 110))
        if t == diepst: tip_beste = tip
    r = D * 0.022
    kleur = KORAAL if record else LICHT
    d.ellipse((tip_beste[0] - r, tip_beste[1] - r, tip_beste[0] + r, tip_beste[1] + r), fill=kleur)
    f = letter(D * 0.07)
    d.text((tip_beste[0] - r * 1.6, tip_beste[1] - D * 0.01), "2:11", font=f, fill=kleur, anchor="rm")
    midden_tekst(d, D, 0.83, "new best" if record else "3 rounds", D * 0.06, kleur if record else ZACHT, False)
    return im

def scherm_week(D):
    im = Image.new("RGB", (D, D), ZWART); d = ImageDraw.Draw(im)
    midden_tekst(d, D, 0.12, "8 weeks", D * 0.06, ZACHT, False)
    import random
    r = random.Random(4)
    dagen = []
    for i in range(56):
        if r.random() < 0.18: dagen.append(None); continue
        dagen.append(70 + i * 1.2 + 9 * math.sin(i / 2.2) + r.uniform(-3, 3))
    x0, x1, top, bodem = 0.10 * D, 0.90 * D, 0.30 * D, 0.72 * D
    lo, hi = 40, 150
    Y = lambda v: bodem - (bodem - top) * (v - lo) / (hi - lo)
    # gemiddelde als schaduw: water onder een lijn door het voortschrijdend gemiddelde
    gem = []
    for i in range(56):
        vs = [v for v in dagen[max(0, i - 6):i + 1] if v]
        gem.append((x0 + (x1 - x0) * i / 55, Y(sum(vs) / len(vs)) if vs else bodem))
    d.polygon(gem + [(x1, bodem), (x0, bodem)], fill=DIEPTE[2])
    stuk = []
    for i, v in enumerate(dagen + [None]):
        if v is None:
            if len(stuk) > 1: d.line(stuk, fill=SCHUIM, width=max(2, D // 110))
            stuk = []; continue
        stuk.append((x0 + (x1 - x0) * i / 55, Y(v)))
    midden_tekst(d, D, 0.77, "best 2:31", D * 0.07, WIT)
    return im

def horloge(im):
    """Rond masker en een donkere rand, alleen voor de presentatie."""
    D = im.size[0]; rand = D // 12
    uit = Image.new("RGB", (D + 2 * rand, D + 2 * rand), (0x2a, 0x25, 0x31))
    d = ImageDraw.Draw(uit)
    d.ellipse((rand // 3, rand // 3, D + 2 * rand - rand // 3, D + 2 * rand - rand // 3), fill=(0x55, 0x55, 0x55))
    d.ellipse((rand - 3, rand - 3, rand + D + 3, rand + D + 3), fill=(0x11, 0x11, 0x11))
    m = Image.new("L", (D, D), 0); ImageDraw.Draw(m).ellipse((0, 0, D - 1, D - 1), fill=255)
    uit.paste(im, (rand, rand), m)
    return uit

if __name__ == "__main__":
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    schermen = [("1-ademen", scherm_ademen), ("2-duiken", scherm_duiken), ("3-boven", scherm_boven),
                ("4-profiel", scherm_profiel), ("5-week", scherm_week)]
    for D in (260, 454):
        rij = [horloge(f(D)) for _, f in schermen]
        for (naam, _), im in zip(schermen, rij):
            im.save(f"{uit}/ebb-{naam}-{D}.png")
        w = sum(i.size[0] for i in rij) + 20 * (len(rij) + 1)
        blad = Image.new("RGB", (w, rij[0].size[1] + 40), (0x2a, 0x25, 0x31))
        x = 20
        for i in rij:
            blad.paste(i, (x, 20)); x += i.size[0] + 20
        blad.save(f"{uit}/ebb-schets-{D}.png")
