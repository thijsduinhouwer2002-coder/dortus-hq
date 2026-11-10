# Mila 10 nov run 11: walvis en schildpad v2 voor Ebb (keuring 1, moet 3 en 4). Alleen MIP-kleuren.
# Coordinaten in eenheden van D/100 rond het midden van het dier, zodat Gijs ze in Teken.mc kan overnemen
# (punt * D / 100). Proef op 454 en 260 px, ware maat en vergroot.
#   python3 ebb_dieren2.py <uit.png>
import sys
from PIL import Image, ImageDraw

KORAAL, NAVY, BEL = (0xFF, 0x55, 0x55), (0x00, 0x00, 0x55), (0x55, 0xAA, 0xFF)

# walvis: platte buik, bolle rug, stompe kop links (zwemt naar links), liggende V-staart rechts, spuitje boven de kop
WALVIS_LIJF = [(-11, 0), (-11, -2.2), (-9, -4.2), (-5, -5), (1, -4.4), (6, -2.6), (9, -1.2), (11, -0.6),
               (11, 0.6), (9, 1.2), (5, 1.6), (-9, 1.6), (-11, 0.8)]
WALVIS_STAART = [(10, 0), (14.5, -3.6), (13.4, 0), (14.5, 3.0)]
WALVIS_VIN = [(-4, 1.4), (-1, 1.4), (-2.6, 3.4)]
WALVIS_OOG = (-8.2, -1.2, 0.7)              # x, y, straal, in NAVY
WALVIS_SPUIT = [((-7, -6), (-8.6, -8.6)), ((-6.4, -6.2), (-6.4, -9.2)), ((-5.8, -6), (-4.2, -8.6))]  # lijnen in BEL
WALVIS_MOND = ((-11, 0.2), (-7.4, 0.6))     # lijn in NAVY

# schildpad: kop links, schild als halve ovaal met twee naden, peddels schuin naar achteren
SCHILD = (-5.5, -4.5, 5.5, 2.5)             # ellips, koepel: hoger dan breed is niet nodig, wel groot
SCHILD_NADEN = [((-1.8, -4.2), (-1.8, 1.6)), ((1.8, -4.2), (1.8, 1.6)), ((-5.2, -1.0), (-1.8, -1.0)), ((1.8, -1.0), (5.2, -1.0))]
SCHILD_KOP = [(-5.0, -2.0), (-7.6, -2.4), (-8.8, -1.0), (-7.6, 0.4), (-5.0, 0.2)]
PEDDELS = [[(-3.6, 1.6), (-1.4, 2.0), (-0.4, 4.6), (-2.6, 4.2)],    # voor onder, vast aan het schild
           [(3.2, 1.8), (4.8, 1.2), (6.4, 3.0), (4.6, 3.4)],         # achter onder
           [(5.2, -1.4), (6.2, -0.6), (7.4, -0.8), (6.4, -1.8)]]     # staartje
SCHILD_OOG = (-7.2, -1.2, 0.55)

def teken(d, cx, cy, D, wat):
    D = D * (1.5 if wat == 'walvis' else 1.25)   # walvis is het grootste dier (3:00), schildpad iets groter dan het visje
    P = lambda pts: [(cx + x * D / 100, cy + y * D / 100) for x, y in pts]
    w = max(1, round(D / 200))
    if wat == "walvis":
        d.polygon(P(WALVIS_STAART), fill=KORAAL)
        d.polygon(P(WALVIS_LIJF), fill=KORAAL)
        d.polygon(P(WALVIS_VIN), fill=NAVY)
        d.line(P(WALVIS_MOND), fill=NAVY, width=w)
        x, y, r = WALVIS_OOG; d.ellipse([cx + (x - r) * D / 100, cy + (y - r) * D / 100, cx + (x + r) * D / 100, cy + (y + r) * D / 100], fill=NAVY)
        for a, b in WALVIS_SPUIT: d.line(P([a, b]), fill=BEL, width=w + 1)
    else:
        for p in PEDDELS: d.polygon(P(p), fill=KORAAL)
        d.polygon(P(SCHILD_KOP), fill=KORAAL)
        x0, y0, x1, y1 = SCHILD
        d.ellipse([cx + x0 * D / 100, cy + y0 * D / 100, cx + x1 * D / 100, cy + y1 * D / 100], fill=KORAAL)
        for a, b in SCHILD_NADEN: d.line(P([a, b]), fill=NAVY, width=w)
        x, y, r = SCHILD_OOG; d.ellipse([cx + (x - r) * D / 100, cy + (y - r) * D / 100, cx + (x + r) * D / 100, cy + (y + r) * D / 100], fill=NAVY)

def scherm(D, wat, tijd):
    im = Image.new("RGB", (D, D), (0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([0, 0, D - 1, D - 1], fill=NAVY)
    teken(d, D * 0.58, D * 0.74, D, wat)
    d.text((D * 0.30, D * 0.40), tijd, fill=(255, 255, 255))
    return im

if __name__ == "__main__":
    vakken = [scherm(454, "walvis", "3:03"), scherm(454, "schildpad", "2:03"), scherm(260, "walvis", "3:03"), scherm(260, "schildpad", "2:03")]
    zoom = []
    for wat in ("walvis", "schildpad"):
        z = Image.new("RGB", (454, 454), NAVY); teken(ImageDraw.Draw(z), 227, 240, 454 * 2, wat); zoom.append(z)
    W = 454 * 2 + 260 * 2 + 454 * 2 + 50
    out = Image.new("RGB", (W, 474), (40, 40, 40)); x = 10
    for v in vakken + zoom:
        out.paste(v, (x, 10)); x += v.width + 10
    out.save(sys.argv[1])
