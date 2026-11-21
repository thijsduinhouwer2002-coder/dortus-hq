# Scherm 1 met pijl (CONCEPT, Sanne 21 nov 2026; 21 nov laat: woorden weg na keuring Iris, Valve-regel geen tekst op schermen). Bron: schermen-steam/2-bureaublad.png, niets aan het beeld zelf veranderd.
from PIL import Image, ImageDraw, ImageFont
import math, sys
bron = 'schermen-steam/2-bureaublad.png'
uit = sys.argv[1] if len(sys.argv) > 1 else 'concept-21nov/1-bureaublad-pijl.png'
S = 2  # tekenen op 2x voor gladde randen
im = Image.open(bron).convert('RGBA')
W, H = im.size
laag = Image.new('RGBA', (W*S, H*S), (0, 0, 0, 0))
d = ImageDraw.Draw(laag)
# gebogen pijl uit het lege bureaublad naar de troon van Gloop (punt boven de graslijn, ±y 745)
start = (1460, 430); ctrl = (1090, 440); eind = (1030, 750)
pts = []
for i in range(41):
    t = i/40
    x = (1-t)**2*start[0] + 2*(1-t)*t*ctrl[0] + t**2*eind[0]
    y = (1-t)**2*start[1] + 2*(1-t)*t*ctrl[1] + t**2*eind[1]
    pts.append((x*S, y*S))
dikte = 16*S
for kleur, dx, dy in (((0, 0, 0, 110), 4*S, 5*S), ((255, 255, 255, 255), 0, 0)):
    d.line([(x+dx, y+dy) for x, y in pts[:-3]], fill=kleur, width=dikte, joint='curve')
    # pijlpunt in de richting van het laatste stuk
    (x1, y1), (x2, y2) = pts[-6], pts[-1]
    a = math.atan2(y2-y1, x2-x1)
    L, B = 62*S, 40*S
    tip = (x2+dx, y2+dy)
    links = (x2 - L*math.cos(a) + B*math.sin(a) + dx, y2 - L*math.sin(a) - B*math.cos(a) + dy)
    rechts = (x2 - L*math.cos(a) - B*math.sin(a) + dx, y2 - L*math.sin(a) + B*math.cos(a) + dy)
    d.polygon([tip, links, rechts], fill=kleur)
laag = laag.resize((W, H), Image.LANCZOS)
Image.alpha_composite(im, laag).convert('RGB').save(uit)
print(uit)
