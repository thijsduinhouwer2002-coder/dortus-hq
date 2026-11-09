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
    return (f'{clip}<path d="{buiten}" fill="{LILA}"/>'
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
    """Lichtbundel: het licht uit de deur valt naar voren over de vloer (vanaf de voet van de D)."""
    vy = y + 560*s
    a, b = x + 150*s, x + 470*s
    return (f'<path d="M{a:.1f},{vy:.1f} L{b:.1f},{vy:.1f} L{b+breed*0.55:.1f},{h_tot} L{a-breed:.1f},{h_tot} Z" fill="url(#vloer)"/>'
            f'<ellipse cx="{(a+b)/2:.1f}" cy="{vy+8*s:.1f}" rx="{200*s:.1f}" ry="{14*s:.1f}" fill="{GOUD}" fill-opacity="0.22"/>')

def dobbel(cx, cy, z, kleur=CREME):
    """Dobbelsteen (Rollwright) op de vloer, schuin."""
    r = z*0.18
    ogen = "".join(f'<circle cx="{cx+dx*z*0.27:.1f}" cy="{cy+dy*z*0.27:.1f}" r="{z*0.085:.1f}" fill="{NACHT}"/>' for dx,dy in ((-1,-1),(0,0),(1,1)))
    return (f'<ellipse cx="{cx+z*0.15:.1f}" cy="{cy+z*0.55:.1f}" rx="{z*0.6:.1f}" ry="{z*0.12:.1f}" fill="#000" fill-opacity="0.35"/>'
            f'<g transform="rotate(-14 {cx:.1f} {cy:.1f})"><rect x="{cx-z/2:.1f}" y="{cy-z/2:.1f}" width="{z:.1f}" height="{z:.1f}" rx="{r:.1f}" fill="{kleur}"/>{ogen}</g>')

def kroon(cx, cy, z):
    """Kroontje (een hoed uit Het Hol) op de vloer."""
    w, h = z, z*0.62
    x0, y0 = cx - w/2, cy - h/2
    pts = [(0,1),(0,0.25),(0.25,0.6),(0.5,0),(0.75,0.6),(1,0.25),(1,1)]
    d = "M" + " L".join(f"{x0+px*w:.1f},{y0+py*h:.1f}" for px,py in pts) + " Z"
    return (f'<ellipse cx="{cx:.1f}" cy="{cy+h*0.62:.1f}" rx="{w*0.62:.1f}" ry="{z*0.1:.1f}" fill="#000" fill-opacity="0.35"/>'
            f'<path d="{d}" fill="{GOUD}" stroke="#b9792a" stroke-width="{z*0.05:.1f}" stroke-linejoin="round"/>'
            f'<circle cx="{cx:.1f}" cy="{y0+h*0.72:.1f}" r="{z*0.07:.1f}" fill="#e2475b"/>')

def haakjes(cx, cy, z):
    """Accolades (de tools voor programmeurs) op de vloer."""
    return (f'<ellipse cx="{cx:.1f}" cy="{cy+z*0.42:.1f}" rx="{z*0.55:.1f}" ry="{z*0.09:.1f}" fill="#000" fill-opacity="0.35"/>'
            f'<text x="{cx:.1f}" y="{cy+z*0.33:.1f}" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="bold" font-size="{z:.1f}" fill="{LILA}">{{}}</text>')

def spullen(dx, dy, s):
    """Wat er uit de deur rolt: een kroontje, een dobbelsteen en accolades, in het licht op de vloer."""
    vy = dy + 560*s
    return (kroon(dx - 20*s, vy + 170*s, 120*s) + dobbel(dx + 250*s, vy + 215*s, 95*s) + haakjes(dx + 470*s, vy + 110*s, 100*s))

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

if __name__ == "__main__":
    schrijf("merkteken", 1024, 1024, avatar())
    for m in (512, 184):
        subprocess.run(["rsvg-convert", f"{UIT}/merkteken.svg", "-w", str(m), "-o", f"{UIT}/avatar-{m}.png"], check=True)
    os.replace(f"{UIT}/merkteken.png", f"{UIT}/avatar-1024.png")
    schrijf("merkteken-klein", 1024, 1024, avatar(klein=True), png=False)
    for m in (32, 16):
        subprocess.run(["rsvg-convert", f"{UIT}/merkteken-klein.svg", "-w", str(m), "-o", f"{UIT}/avatar-{m}.png"], check=True)

    # Steam: logo bovenaan de ontwikkelaarspagina (doorzichtig)
    schrijf("steam-logo-1200x460", 1200, 460, woord(70, 90, 280))
    # Steam: kop achter de naam (donker, rustig links, licht rechts)
    schrijf("steam-kop-1500x220", 1500, 220, kamer(1500, 220, 1160, 24, 0.27))
    # Steam: achtergrond van de hele ontwikkelaarspagina
    schrijf("steam-achtergrond-1920", 1920, 1200, kamer(1920, 1200, 1250, 140, 0.9, 0.8, True))
    # dortus.com deelplaatje en GitHub social preview
    for naam, w, h in (("og-1200x630", 1200, 630), ("social-1280x640", 1280, 640)):
        sc = h / 1000
        inhoud = (kamer(w, h, w - 560*sc*1.1, 110*sc, 0.95*sc*1.1, 1.0, True)
                  + woord(80*sc, 260*sc, 250*sc)
                  + f'<text x="{80*sc:.1f}" y="{640*sc:.1f}" font-family="Inter" font-weight="500" font-size="{44*sc:.1f}" fill="{LILA}">Small games and focused tools</text>'
                  + f'<text x="{80*sc:.1f}" y="{700*sc:.1f}" font-family="Inter" font-weight="500" font-size="{44*sc:.1f}" fill="{LILA}">from the Netherlands</text>')
        schrijf(naam, w, h, inhoud)
