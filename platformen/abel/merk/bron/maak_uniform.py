"""Uniform van Dortus (Mila). Maakt alle merkbeelden als SVG en zet ze om naar PNG met rsvg-convert.
Draai: python3 maak_uniform.py  (schrijft naar de map erboven)."""
import subprocess, os
UIT = os.path.dirname(os.path.abspath(__file__)) + "/.."
NACHT, PRUIM, LILA, LILA_D, CREME, GOUD, ORANJE = "#1d1426", "#3f2846", "#a58cff", "#6f55d9", "#fff4e0", "#ffd25c", "#ff9a3c"

DEFS = f"""<defs>
<radialGradient id="licht" cx="0.7" cy="0.5" r="0.75"><stop offset="0" stop-color="#fff6c9"/><stop offset="0.45" stop-color="{GOUD}"/><stop offset="1" stop-color="{ORANJE}"/></radialGradient>
<linearGradient id="straal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOUD}" stop-opacity="0.55"/><stop offset="1" stop-color="{GOUD}" stop-opacity="0"/></linearGradient>
<linearGradient id="vloer" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GOUD}" stop-opacity="0.5"/><stop offset="1" stop-color="{GOUD}" stop-opacity="0"/></linearGradient>
<linearGradient id="vloerdonker" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140d1a" stop-opacity="0.5"/><stop offset="1" stop-color="#0f0a14"/></linearGradient>
<radialGradient id="gloed" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{GOUD}" stop-opacity="0.35"/><stop offset="1" stop-color="{GOUD}" stop-opacity="0"/></radialGradient>
</defs>"""

_n = [0]
def deur(x, y, s, klein=False):
    """De D als deur op een kier, in een vak van 500 x 560 maal s, linksboven op x,y.
    Linkerkant recht met twee scharnieren (de twee bolletjes van het oude logo), binnenin licht,
    het deurblad staat op een kier."""
    t = 120 if not klein else 140           # dikte van de D
    _n[0] += 1; cid = f"opening{_n[0]}"
    def P(px, py): return f"{x+px*s:.1f},{y+py*s:.1f}"
    R = 280
    buiten = f"M{P(0,0)} H{x+220*s:.1f} A{R*s:.1f},{R*s:.1f} 0 0 1 {P(220,560)} H{P(0,560)[0:0]}{x:.1f} Z"
    ri = R - t
    binnen = f"M{P(t,t)} H{x+220*s:.1f} A{ri*s:.1f},{ri*s:.1f} 0 0 1 {P(220,560-t)} H{x+t*s:.1f} Z"
    # deurblad: draait om de linkerkant naar binnen, dus smaller en schuin
    bw = 112 if not klein else 62
    blad = f"M{P(t,t)} L{P(t+bw,t+30)} L{P(t+bw,560-t-30)} L{P(t,560-t)} Z"
    kant = f"M{P(t+bw-14,t+28)} L{P(t+bw,t+30)} L{P(t+bw,560-t-30)} L{P(t+bw-14,560-t-28)} Z"
    # licht valt op de binnenrand van de deurpost en over de vloer van de opening
    rand = f'<path d="{binnen}" fill="none" stroke="#ffcf8a" stroke-opacity="0.9" stroke-width="{10*s:.1f}"/>' if not klein else ""
    vloer = f'<path d="M{P(t+bw,560-t-30)} L{P(220+ri-30,560-t)} L{P(t,560-t)} Z" fill="#fff6c9" fill-opacity="0.55" clip-path="url(#{cid})"/>' if not klein else ""
    clip = f'<clipPath id="{cid}"><path d="{binnen}"/></clipPath>'
    knop = f'<circle cx="{x+(t+bw-30)*s:.1f}" cy="{y+300*s:.1f}" r="{(15 if not klein else 0)*s:.1f}" fill="{GOUD}"/>'
    sch = "".join(f'<rect x="{x-22*s:.1f}" y="{y+yy*s:.1f}" width="{44*s:.1f}" height="{70*s:.1f}" rx="{14*s:.1f}" fill="{GOUD}"/>' for yy in (90, 400)) if not klein else ""
    diepte = "" if klein else (f'<clipPath id="d{cid}"><path d="{buiten}"/></clipPath>'
              f'<path d="{buiten}" fill="none" stroke="#c9b9ff" stroke-width="{26*s:.1f}" clip-path="url(#d{cid})"/>'
              f'<path d="{binnen}" fill="none" stroke="{LILA_D}" stroke-width="{56*s:.1f}" clip-path="url(#d{cid})"/>')
    return (f'{clip}<path d="{buiten}" fill="{LILA}"/>{diepte}'
            f'<path d="{binnen}" fill="url(#licht)"/>{rand}'
            f'{vloer}<path d="{blad}" fill="{PRUIM}"/><path d="{kant}" fill="{NACHT}"/>{knop}{sch}')

def svg(w, h, inhoud):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{DEFS}{inhoud}</svg>'

def schrijf(naam, w, h, inhoud, png=True, uit=None):
    p = f"{UIT}/{naam}.svg"
    open(p, "w").write(svg(w, h, inhoud))
    if png:
        subprocess.run(["rsvg-convert", p, "-w", str(uit or w), "-o", f"{UIT}/{naam}.png"], check=True)
    return p

def avatar(klein=False):
    s = 1.15 if not klein else 1.4
    w, h = 500*s, 560*s
    return (f'<rect width="1024" height="1024" fill="{NACHT}"/>'
            f'<circle cx="540" cy="512" r="430" fill="url(#gloed)"/>'
            + deur(512 - w/2 + 18, 512 - h/2, s, klein))

def woord(x, y, hoogte, kleur=CREME, staart=True):
    """Het woordmerk: de deur-D en daarachter 'ortus'. hoogte = hoogte van de D in px; x,y linksboven."""
    s = hoogte / 560
    d = deur(x + 22*s, y, s)
    fs = hoogte * 1.02
    tekst = (f'<text x="{x + 535*s:.1f}" y="{y + hoogte:.1f}" font-family="Inter Display" font-weight="800" '
             f'font-size="{fs:.1f}" letter-spacing="{-0.02*fs:.1f}" fill="{kleur}">ortus</text>')
    return d + tekst

def straal(x, y, s, h_tot, breed):
    """Lichtbundel v2: het licht valt door de kier van de deur naar buiten. Smal onder de opening
    (tussen deurblad en boog), daarna breder over de vloer. Kern feller dan de rand."""
    vy = y + 560*s
    a, b = x + 236*s, x + 352*s              # onder de lichte opening, niet onder de hele D
    l, r = a - breed*0.95, b + breed*0.6
    kern_l, kern_r = a - breed*0.35, b + breed*0.2
    return (f'<path d="M{a:.1f},{vy:.1f} L{b:.1f},{vy:.1f} L{r:.1f},{h_tot} L{l:.1f},{h_tot} Z" fill="url(#vloer)"/>'
            f'<path d="M{a+10*s:.1f},{vy:.1f} L{b-10*s:.1f},{vy:.1f} L{kern_r:.1f},{h_tot} L{kern_l:.1f},{h_tot} Z" fill="url(#vloer)" opacity="0.55"/>'
            f'<ellipse cx="{(a+b)/2:.1f}" cy="{vy+6*s:.1f}" rx="{90*s:.1f}" ry="{12*s:.1f}" fill="#fff6c9" fill-opacity="0.45"/>')

def dobbel(cx, cy, z, kleur=CREME, stof=True):
    """Dobbelsteen (Rollwright) die nog nahuppelt: kubus met lichte bovenkant, schaduw en een stofwolkje erachter."""
    k = z*0.5; d = z*0.28                     # halve zijde, diepte van de bovenkant
    rot = -12
    puf = ""
    if stof:
        for i, (ox, oy, rr, op) in enumerate(((-1.25, 0.42, 0.22, 0.35), (-1.65, 0.36, 0.16, 0.25), (-1.95, 0.44, 0.11, 0.18), (-1.0, 0.5, 0.15, 0.3))):
            puf += f'<circle cx="{cx+ox*z:.1f}" cy="{cy+oy*z:.1f}" r="{rr*z:.1f}" fill="{CREME}" fill-opacity="{op}"/>'
    ogen = "".join(f'<circle cx="{cx+dx*z*0.24:.1f}" cy="{cy+d*0.5+dy*z*0.24:.1f}" r="{z*0.075:.1f}" fill="{NACHT}"/>' for dx,dy in ((-1,-1),(0,0),(1,1)))
    top_ogen = "".join(f'<ellipse cx="{cx+dx*z*0.2+d*0.3:.1f}" cy="{cy-k+d*0.05+dy*d*0.3:.1f}" rx="{z*0.06:.1f}" ry="{z*0.035:.1f}" fill="{NACHT}" fill-opacity="0.8"/>' for dx,dy in ((-1,-0.6),(1,0.6)))
    voor = f'M{cx-k:.1f},{cy-k+d:.1f} H{cx+k:.1f} V{cy+k+d*0.4:.1f} H{cx-k:.1f} Z'
    boven = f'M{cx-k:.1f},{cy-k+d:.1f} L{cx-k+d:.1f},{cy-k:.1f} H{cx+k+d:.1f} L{cx+k:.1f},{cy-k+d:.1f} Z'
    zij = f'M{cx+k:.1f},{cy-k+d:.1f} L{cx+k+d:.1f},{cy-k:.1f} V{cy+k:.1f} L{cx+k:.1f},{cy+k+d*0.4:.1f} Z'
    return (puf + f'<ellipse cx="{cx+z*0.12:.1f}" cy="{cy+k+d*0.55:.1f}" rx="{z*0.7:.1f}" ry="{z*0.12:.1f}" fill="#000" fill-opacity="0.4"/>'
            f'<g transform="rotate({rot} {cx:.1f} {cy:.1f})" stroke="#2a1d33" stroke-width="{z*0.035:.1f}" stroke-linejoin="round">'
            f'<path d="{voor}" fill="{kleur}"/><path d="{boven}" fill="#ffffff"/><path d="{zij}" fill="#d8c7b4"/>'
            f'<g stroke="none">{ogen}{top_ogen}</g></g>')

def kroon(cx, cy, z):
    """Kroontje (een hoed uit Het Hol), iets gekanteld omgevallen, met glans en drie steentjes."""
    w, h = z, z*0.62
    x0, y0 = cx - w/2, cy - h/2
    pts = [(0,1),(0,0.25),(0.25,0.6),(0.5,0),(0.75,0.6),(1,0.25),(1,1)]
    d = "M" + " L".join(f"{x0+px*w:.1f},{y0+py*h:.1f}" for px,py in pts) + " Z"
    band = f'<rect x="{x0:.1f}" y="{y0+h*0.72:.1f}" width="{w:.1f}" height="{h*0.28:.1f}" fill="#e8a93a"/>'
    glans = f'<path d="M{x0+w*0.08:.1f},{y0+h*0.45:.1f} L{x0+w*0.08:.1f},{y0+h*0.66:.1f}" stroke="#fff6c9" stroke-width="{z*0.07:.1f}" stroke-linecap="round"/>'
    punten = "".join(f'<circle cx="{x0+px*w:.1f}" cy="{y0+py*h:.1f}" r="{z*0.06:.1f}" fill="#fff0b0"/>' for px,py in ((0,0.25),(0.5,0),(1,0.25)))
    stenen = "".join(f'<circle cx="{x0+px*w:.1f}" cy="{y0+h*0.86:.1f}" r="{z*(0.075 if px==0.5 else 0.055):.1f}" fill="{c}"/>' for px,c in ((0.22,"#5ad1c0"),(0.5,"#e2475b"),(0.78,"#5ad1c0")))
    return (f'<ellipse cx="{cx:.1f}" cy="{cy+h*0.6:.1f}" rx="{w*0.66:.1f}" ry="{z*0.11:.1f}" fill="#000" fill-opacity="0.4"/>'
            f'<g transform="rotate(-9 {cx:.1f} {cy+h*0.5:.1f})"><clipPath id="kr{int(cx)}{int(cy)}"><path d="{d}"/></clipPath>'
            f'<path d="{d}" fill="{GOUD}"/><g clip-path="url(#kr{int(cx)}{int(cy)})">{band}</g>'
            f'<path d="{d}" fill="none" stroke="#8a5522" stroke-width="{z*0.045:.1f}" stroke-linejoin="round"/>{glans}{punten}{stenen}</g>')

def haakjes(cx, cy, z):
    """Accolades (de tools voor programmeurs): staan rechtop op de vloer, met donkere rand en schaduw."""
    t = (f'font-family="DejaVu Sans Mono" font-weight="bold" font-size="{z:.1f}" text-anchor="middle"')
    return (f'<ellipse cx="{cx:.1f}" cy="{cy+z*0.4:.1f}" rx="{z*0.58:.1f}" ry="{z*0.09:.1f}" fill="#000" fill-opacity="0.4"/>'
            f'<text x="{cx+z*0.04:.1f}" y="{cy+z*0.33+z*0.04:.1f}" {t} fill="{LILA_D}">{{}}</text>'
            f'<text x="{cx:.1f}" y="{cy+z*0.33:.1f}" {t} fill="{LILA}" stroke="#2a1d33" stroke-width="{z*0.025:.1f}">{{}}</text>'
            f'<text x="{cx-z*0.02:.1f}" y="{cy+z*0.33-z*0.02:.1f}" {t} fill="#c9b9ff" fill-opacity="0.45">{{}}</text>')

def spullen(dx, dy, s):
    """Wat er uit de deur rolt: een kroontje, een dobbelsteen en accolades, in het licht op de vloer."""
    vy = dy + 560*s
    return (kroon(dx + 40*s, vy + 175*s, 120*s) + dobbel(dx + 330*s, vy + 200*s, 88*s) + haakjes(dx + 520*s, vy + 140*s, 96*s))

def sterren(w, h, n, zaad=7, kleur=GOUD):
    import random
    r = random.Random(zaad); uit = ""
    for _ in range(n):
        uit += f'<circle cx="{r.uniform(0,w):.1f}" cy="{r.uniform(0,h):.1f}" r="{r.choice([1,1,1.5,2]):.1f}" fill="{kleur}" fill-opacity="{r.uniform(0.15,0.6):.2f}"/>'
    return uit

def kamer(w, h, dx, dy, s, licht=1.0, met_spullen=False):
    """Donkere kamer met een deur-D op een kier en het licht dat over de vloer valt."""
    vloer_y = dy + 560*s
    return (f'<rect width="{w}" height="{h}" fill="{NACHT}"/>'
            f'<rect y="{vloer_y:.1f}" width="{w}" height="{h-vloer_y:.1f}" fill="url(#vloerdonker)"/>'
            f'<circle cx="{dx+300*s:.1f}" cy="{dy+300*s:.1f}" r="{520*s:.1f}" fill="url(#gloed)" opacity="{licht}"/>'
            + straal(dx, dy, s, h, 700*s) + sterren(w, h*0.8, int(w*h/9000)) + deur(dx, dy, s)
            + (spullen(dx, dy, s) if met_spullen else ""))

def kop_v2(w=1500, h=220):
    """Steam-kop v2 (kan-punt 6 Daan): geen tweede D. De deur zit al in de avatar links; het licht uit die
    deur valt hier vanaf links over de vloer naar rechts, en daarin rollen de spullen.
    Avatar staat op 1920 breed op kop-x 150..335, op 1024 breed op 248..433 (gemeten door Abel), dus de bundel
    begint zacht rond x 300 en de spullen staan tussen x 600 en 1060 (op 1024 buiten het grijze verloop)."""
    vy = 138
    bundel = (f'<linearGradient id="kopbundel" x1="0" y1="0" x2="1" y2="0">'
              f'<stop offset="0" stop-color="{GOUD}" stop-opacity="0"/><stop offset="0.12" stop-color="{GOUD}" stop-opacity="0.5"/>'
              f'<stop offset="0.55" stop-color="{GOUD}" stop-opacity="0.28"/><stop offset="1" stop-color="{GOUD}" stop-opacity="0"/></linearGradient>')
    zacht = '<filter id="zacht" x="-0.1" y="-0.5" width="1.2" height="2"><feGaussianBlur stdDeviation="7"/></filter>'
    return (f'<defs>{bundel}{zacht}</defs><rect width="{w}" height="{h}" fill="{NACHT}"/>'
            f'<rect y="{vy}" width="{w}" height="{h-vy}" fill="url(#vloerdonker)"/>'
            f'<ellipse cx="380" cy="{vy}" rx="380" ry="110" fill="url(#gloed)" opacity="0.9"/>'
            f'<g filter="url(#zacht)"><path d="M230,{vy+10} L230,{vy+26} L1300,{h+30} L1300,{vy-16} Z" fill="url(#kopbundel)"/>'
            f'<path d="M260,{vy+15} L260,{vy+21} L1100,{vy+40} L1100,{vy+6} Z" fill="url(#kopbundel)" opacity="0.9"/></g>'
            + sterren(w, vy, 34, zaad=11)
            + kroon(650, vy + 20, 60) + dobbel(860, vy + 26, 46) + haakjes(1050, vy + 12, 54))

def achtergrond_v2(W=1920, H=1200):
    """Steam-achtergrond v2: Abels v1b (geen tweede D, het licht valt uit de D van het paginalogo) met de
    nieuwe smalle bundel, en alle drie de spullen terug in de kantlijn, elk in eigen licht."""
    s = 0.5; dx = 360 + LOGO_X + 22*s; dy = 106 + (460-280)/2 - 90   # D van het gecentreerde logo v2 (1200 breed, midden op 1920)
    return (f'<rect width="{W}" height="{H}" fill="{NACHT}"/>'
            f'<rect y="{dy+560*s:.0f}" width="{W}" height="{H-dy-560*s:.0f}" fill="url(#vloerdonker)"/>'
            f'<circle cx="960" cy="250" r="700" fill="url(#gloed)" opacity="0.45"/>'
            f'<circle cx="{dx+300*s:.0f}" cy="{dy+300*s:.0f}" r="460" fill="url(#gloed)" opacity="0.9"/>'
            + straal(dx, dy, s, H, 900) + sterren(W, H*0.8, int(W*H/9000))
            + f'<circle cx="230" cy="660" r="230" fill="url(#gloed)" opacity="0.9"/>'
            + f'<circle cx="1720" cy="600" r="190" fill="url(#gloed)" opacity="0.7"/>'
            + kroon(200, 560, 110) + dobbel(270, 740, 84) + haakjes(1720, 560, 96))

def woord_midden(w, h, hoogte):
    """Woordmerk precies in het midden van een doorzichtig vlak (kan-punt 8): breedte gemeten in een eerste render."""
    import tempfile
    t = tempfile.mktemp(suffix=".svg"); png = t + ".png"
    open(t, "w").write(svg(w, h, woord(0, 0, hoogte)))
    subprocess.run(["rsvg-convert", t, "-o", png], check=True)
    from PIL import Image
    bb = Image.open(png).getbbox()
    global LOGO_X
    LOGO_X = (w - (bb[2] - bb[0])) / 2 - bb[0]
    return woord(LOGO_X, (h - hoogte) / 2, hoogte)

if __name__ == "__main__":
    # v1 (avatars en merkteken) blijven zoals ze zijn; opnieuw maken kan met: python3 maak_uniform.py v1-avatars
    import sys
    if "v1-avatars" in sys.argv:
        schrijf("merkteken", 1024, 1024, avatar())
        for m in (512, 184):
            subprocess.run(["rsvg-convert", f"{UIT}/merkteken.svg", "-w", str(m), "-o", f"{UIT}/avatar-{m}.png"], check=True)
        os.replace(f"{UIT}/merkteken.png", f"{UIT}/avatar-1024.png")
        schrijf("merkteken-klein", 1024, 1024, avatar(klein=True), png=False)
        for m in (32, 16):
            subprocess.run(["rsvg-convert", f"{UIT}/merkteken-klein.svg", "-w", str(m), "-o", f"{UIT}/avatar-{m}.png"], check=True)
    # v2: alles met een lichtbundel of spullen, plus het logo in het midden
    schrijf("steam-logo-1200x460-v2", 1200, 460, woord_midden(1200, 460, 280))
    schrijf("steam-kop-1500x220-v2", 1500, 220, kop_v2())
    schrijf("steam-achtergrond-1920-v2", 1920, 1200, achtergrond_v2())
    for naam, w, h in (("og-1200x630-v2", 1200, 630), ("social-1280x640-v2", 1280, 640)):
        sc = h / 1000
        inhoud = (kamer(w, h, w - 600*sc*1.1, 90*sc, 0.95*sc*1.1, 1.0, True)
                  + woord(80*sc, 260*sc, 250*sc)
                  + f'<text x="{80*sc:.1f}" y="{640*sc:.1f}" font-family="Inter" font-weight="500" font-size="{44*sc:.1f}" fill="{LILA}">Small games and focused tools</text>'
                  + f'<text x="{80*sc:.1f}" y="{700*sc:.1f}" font-family="Inter" font-weight="500" font-size="{44*sc:.1f}" fill="{LILA}">from the Netherlands</text>')
        schrijf(naam, w, h, inhoud)
