# Winkelbeelden Ebb (Connect IQ Store), Mila 10 nov 2026. Stijl: patrijspoort, vlakke MIP-tinten, koraal alleen voor dieren.
#   python3 maak_winkel_mila.py icoon <uit.png>
#   python3 maak_winkel_mila.py kaart <simulator.png> "<kop>" "<koraalwoord>" "<ondertekst>" <uit.png>
#   python3 maak_winkel_mila.py poster <simulator.png> <uit.png>
# <simulator.png> is een schermafbeelding uit de simulator (met menubalk en witte rand), zoals op de tak schermen.
# Letters: Barlow Condensed (OFL), zelfde familie als de cijfers in de app. Alles eerlijk: het horloge is de echte opname.
import math, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HIER = os.path.dirname(os.path.abspath(__file__))
NACHT, DIEP, MIDDEN, ONDIEP, SCHUIM = (0, 0, 0), (0x00, 0x00, 0x55), (0x00, 0x00, 0xAA), (0x00, 0x55, 0xAA), (0x55, 0xFF, 0xFF)
TEAL, BEL, KORAAL, WIT = (0x00, 0xAA, 0xAA), (0x55, 0xAA, 0xFF), (0xFF, 0x55, 0x55), (255, 255, 255)

def letter(dikte, maat):
    return ImageFont.truetype(os.path.join(HIER, f"barlow-condensed-{dikte}.woff"), maat)

# walvis in D/100 rond zijn midden (zelfde vorm als ontwerp/garmin/bron/ebb_dieren2.py)
WALVIS_LIJF = [(-11, 0), (-11, -2.2), (-9, -4.2), (-5, -5), (1, -4.4), (6, -2.6), (9, -1.2), (11, -0.6),
               (11, 0.6), (9, 1.2), (5, 1.6), (-9, 1.6), (-11, 0.8)]
WALVIS_STAART = [(10, 0), (14.5, -3.6), (13.4, 0), (14.5, 3.0)]
WALVIS_VIN = [(-4, 1.4), (-1, 1.4), (-2.6, 3.4)]

def walvis(d, cx, cy, s, achter=DIEP):
    P = lambda pts: [(cx + x * s, cy + y * s) for x, y in pts]
    d.polygon(P(WALVIS_STAART), fill=KORAAL)
    d.polygon(P(WALVIS_LIJF), fill=KORAAL)
    d.polygon(P(WALVIS_VIN), fill=achter)
    d.line(P([(-11, 0.2), (-7.4, 0.6)]), fill=achter, width=max(2, int(s * 0.35)))
    r = 0.75 * s; ox, oy = cx - 8.2 * s, cy - 1.2 * s
    d.ellipse([ox - r, oy - r, ox + r, oy + r], fill=achter)
    for a, b in [((-7, -6), (-8.6, -8.8)), ((-6.4, -6.2), (-6.4, -9.6)), ((-5.8, -6), (-4.2, -8.8))]:
        d.line(P([a, b]), fill=BEL, width=max(3, int(s * 0.6)))

def golf(y0, amp, w, fase=0.0, perioden=1.5):
    return [(x, y0 + amp * math.sin(2 * math.pi * perioden * x / w + fase)) for x in range(0, w + 1, 4)]

def icoon(uit):
    N = 2000                                   # groot tekenen, dan verkleinen: zachte randen
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c, R, r = N / 2, N * 0.49, N * 0.385       # ring buiten en binnen
    d.ellipse([c - R, c - R, c + R, c + R], fill=(0x1c, 0x24, 0x30))
    d.ellipse([c - R + 18, c - R + 18, c + R - 18, c + R - 18], fill=(0x2c, 0x38, 0x48))
    for i in range(8):                         # bouten van de patrijspoort
        a = math.pi / 8 + i * math.pi / 4
        bx, by, br = c + math.cos(a) * (R + r) / 2, c + math.sin(a) * (R + r) / 2, N * 0.03
        d.ellipse([bx - br, by - br, bx + br, by + br], fill=(0x9f, 0xb3, 0xc8))
        d.ellipse([bx - br * 0.45, by - br * 0.45 - br * 0.25, bx + br * 0.45, by + br * 0.45 - br * 0.25], fill=(0xd8, 0xe4, 0xf0))
    glas = Image.new("RGBA", (N, N), (0, 0, 0, 0)); g = ImageDraw.Draw(glas)
    g.rectangle([0, 0, N, N], fill=NACHT)
    for (y0, kl, amp, f) in [(0.30, ONDIEP, 26, 0.6), (0.50, MIDDEN, 20, 2.2), (0.68, DIEP, 16, 4.0)]:
        lijn = golf(N * y0, amp, N, f)
        g.polygon(lijn + [(N, N), (0, N)], fill=kl)
    g.line(golf(N * 0.30, 26, N, 0.6), fill=SCHUIM, width=22)
    for bx, by, br in [(0.36, 0.44, 24), (0.40, 0.37, 15), (0.63, 0.47, 18)]:
        g.ellipse([N * bx - br, N * by - br, N * bx + br, N * by + br], outline=BEL, width=9)
    walvis(g, N * 0.47, N * 0.66, N * 0.0215, achter=DIEP)
    masker = Image.new("L", (N, N), 0)
    ImageDraw.Draw(masker).ellipse([c - r, c - r, c + r, c + r], fill=255)
    im.paste(glas, (0, 0), masker)
    d.ellipse([c - r, c - r, c + r, c + r], outline=(0x0c, 0x10, 0x18), width=16)
    im.resize((500, 500), Image.LANCZOS).save(uit, optimize=True)
    print(uit, os.path.getsize(uit))

def horloge(pad, hoogte):
    """Simulatorbeeld zonder balken, wit rond het horloge doorzichtig, op hoogte."""
    w = Image.open(pad).convert("RGBA")
    w = w.crop((6, 30, w.width - 6, w.height - 30))
    for hoek in [(4, 4), (w.width - 4, 4), (4, w.height - 4), (w.width - 4, w.height - 4)]:
        ImageDraw.floodfill(w, hoek, (0, 0, 0, 0), thresh=60)
    # zwarte simulatorstroken (sommige horloges) ook weg
    px = w.load()
    for y in range(w.height):
        for x in list(range(0, 12)) + list(range(w.width - 12, w.width)):
            if px[x, y][:3] == (0, 0, 0): px[x, y] = (0, 0, 0, 0)
    bbox = w.getbbox(); w = w.crop(bbox)
    s = hoogte / w.height
    return w.resize((int(w.width * s), hoogte), Image.LANCZOS)

def zee(im, water_y):
    """Zee over de onderkant: het horloge zakt met zijn band in het water (getekend na het horloge)."""
    W, H = im.size; d = ImageDraw.Draw(im)
    lijn = golf(water_y, H * 0.014, W, 0.8)
    d.polygon(lijn + [(W, H), (0, H)], fill=DIEP)
    d.line(lijn, fill=SCHUIM, width=max(3, W // 200))
    for bx, by, br in [(0.10, 0.06, 0.014), (0.14, 0.10, 0.008), (0.88, 0.05, 0.011), (0.91, 0.11, 0.006)]:
        x, y, r = W * bx, water_y + H * by, H * br
        d.ellipse([x - r, y - r, x + r, y + r], outline=BEL, width=max(2, W // 330))

def kop_met_koraal(d, W, y, tekst, koraal, font):
    """Kop gecentreerd; het koraalwoord (als het erin staat) in koraal."""
    tw = d.textlength(tekst, font=font); x = (W - tw) / 2
    if koraal and koraal in tekst:
        i = tekst.index(koraal)
        for deel, kl in [(tekst[:i], WIT), (koraal, KORAAL), (tekst[i + len(koraal):], WIT)]:
            d.text((x, y), deel, font=font, fill=kl); x += d.textlength(deel, font=font)
    else:
        d.text((x, y), tekst, font=font, fill=WIT)

def kaart(sim, kop, koraal, onder, uit, W=800, H=800):
    im = Image.new("RGB", (W, H), NACHT); d = ImageDraw.Draw(im)
    kop_met_koraal(d, W, H * 0.04, kop, koraal, letter(800, int(H * 0.11)))
    d.text((W / 2, H * 0.185), onder, font=letter(500, int(H * 0.045)), fill=TEAL, anchor="mt")
    top, h = int(H * 0.26), int(H * 0.80)
    w = horloge(sim, h)
    im.paste(w, ((W - w.width) // 2, top), w)
    zee(im, top + h * 0.845)
    bewaar(im, uit)

def poster(sim, uit, W=1000, H=1000):
    im = Image.new("RGB", (W, H), NACHT); d = ImageDraw.Draw(im)
    d.text((W / 2, H * 0.035), "Hold your breath.", font=letter(800, int(H * 0.115)), fill=WIT, anchor="mt")
    kop_met_koraal(d, W, H * 0.13, "Meet the whale.", "whale", letter(800, int(H * 0.115)))
    d.text((W / 2, H * 0.272), "Breath-hold rounds  ·  calm breathing  ·  your sea log", font=letter(500, int(H * 0.04)), fill=TEAL, anchor="mt")
    top, h = int(H * 0.335), int(H * 0.72)
    w = horloge(sim, h)
    im.paste(w, ((W - w.width) // 2, top), w)
    zee(im, top + h * 0.79)     # poster: de kast zakt een stukje in zee, zodat de regel eronder helemaal in het water staat
    d = ImageDraw.Draw(im)
    d.text((W / 2, H * 0.985), "One payment  ·  no subscription  ·  no account", font=letter(700, int(H * 0.034)), fill=WIT, anchor="mb")
    bewaar(im, uit)

def bewaar(im, uit, grens=150_000):
    for kleuren in (256, 200, 160, 128, 96):
        im.quantize(colors=kleuren, method=Image.Quantize.FASTOCTREE).save(uit, optimize=True)
        if os.path.getsize(uit) < grens: break
    print(uit, im.size, os.path.getsize(uit))

if __name__ == "__main__":
    a = sys.argv
    if a[1] == "icoon": icoon(a[2])
    elif a[1] == "kaart": kaart(a[2], a[3], a[4], a[5], a[6])
    elif a[1] == "poster": poster(a[2], a[3])
