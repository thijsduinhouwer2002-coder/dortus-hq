# Menu v4 (Mila, run 54, 12 nov): punt 1 en 2 van de hoofdchat (06:00).
#  1. De gekozen knop is gevuld zoals Resume op het pauzescherm: overdag cyaan 00FFFF met donkere tekst 000055,
#     bij nacht 0055AA met rand 55AAFF en witte tekst. De andere knop: donker vlak met dunne blauwe rand en witte tekst.
#     Eén regel voor alle menu's (ook pauze en instellingen).
#  2. Voetregel "Sea log · Settings · Today" gemeten tegen de echte achtergrond (na de nachtregel); moet minstens 4,5.
# De knoppen horen bij de uitzondering van de nachtregel (zoals de tekst): ze zijn al in nachtkleuren getekend.
# Gebruik: python3 menu_v4.py <uitmap>
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import krab_keuring2 as K
import werelden_v21 as w
from PIL import Image, ImageChops, ImageFilter

v3 = K.v3
WIT, GEEL = (255, 255, 255), (255, 255, 170)
CYAAN, INKT = (0, 255, 255), (0, 0, 85)
_tekst_echt = w.tekst


def knop(d, y, t, gekozen, nacht):
    """Zelfde regel als Resume (onderwater_v1.pauze). Alleen tekenen als de tekst ook getekend wordt (masker van de nachtregel)."""
    if w.tekst is not _tekst_echt:
        return
    s = d.s
    if gekozen:
        fill, rand, tk = ((0, 85, 170), (85, 170, 255), WIT) if nacht else (CYAAN, None, INKT)
    else:
        fill = ((0, 30, 60) if not nacht else (0, 0, 40)) if d.am else (0, 0, 85)
        rand, tk = ((0, 85, 170) if nacht else (0, 170, 255)), WIT
    d.dr.rounded_rectangle([64 * s, y * s, 196 * s, (y + 28) * s], radius=14 * s, fill=fill,
                           outline=rand, width=round(2 * s) if rand else 0)
    d.tekst(130, y + 2, t, 20, tk)


def menu(D_, am, dd, nacht, wereld, gekozen=0):
    d = w.Doek(D_, am)
    if wereld == 'krab':
        v3.onder(d, dd, nacht); w.wereld_onder(d, dd, held_y=186, held_maat=38, spiegel=True, anem_dy=10)
    elif wereld == 'schild':
        v3.onder(d, dd, nacht, xo=120, xh=124); v3.wereld_schild(d, dd, hx=132, hy=192, m=42, spiegel=True, zak=18)
    else:
        v3.onder(d, dd, nacht, xo=142, xh=144); v3.wereld_clown(d, dd, hx=140, hy=199, m=38, zak=6, nacht=nacht, adx=16, ak=.78, takje=False)
    v3.stofjes(d, dd)
    d.tekst(130, 16, 'Ebb', 25, GEEL)
    for i, (y, t) in enumerate([(52, 'Rounds'), (86, 'Calm 4-7-8')]):
        knop(d, y, t, i == gekozen, nacht)
    d.tekst(130, 118, 'Sea log  ·  Settings  ·  Today', 16, GEEL, False)
    return d.klaar()


def maak(D_, am, nacht, wereld='krab', gekozen=0):
    dd = w.NACHT if nacht else w.DAG
    f = lambda: menu(D_, am, dd, nacht, wereld, gekozen)
    im = f()
    if not nacht:
        return im
    return K.nachtregel(im, K.zonder_tekst(f), am)


def lum(c):
    g = lambda v: (v / 255) / 12.92 if v / 255 <= .03928 else ((v / 255 + .055) / 1.055) ** 2.4
    return .2126 * g(c[0]) + .7152 * g(c[1]) + .0722 * g(c[2])


def cr(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)


def meet_voet(D_, am, nacht, wereld='krab'):
    """Voetregel: GEEL tegen de lichtste achtergrondpixel in een ring van 2 tot 3 px rond de letters (beeld zonder tekst, na de regel)."""
    dd = w.NACHT if nacht else w.DAG
    oud = w.Doek.tekst
    def alleen_voet(self, x, y, s, maat, c, dik=True):
        if s.startswith('Sea log'): oud(self, x, y, s, maat, (255, 0, 255), dik)
    kaal = K.zonder_tekst(lambda: menu(D_, am, dd, nacht, wereld))
    w.Doek.tekst = alleen_voet; sl = menu(D_, am, dd, nacht, wereld); w.Doek.tekst = oud
    mk = ImageChops.difference(sl, kaal).convert('L').point(lambda v: 255 if v > 40 else 0)
    if nacht: kaal = K.nachtregel(kaal, kaal, am)
    ring = ImageChops.subtract(mk.filter(ImageFilter.MaxFilter(7)), mk.filter(ImageFilter.MaxFilter(3)))
    px, rp = kaal.load(), ring.load()
    return min(cr(GEEL, px[x, y]) for y in range(D_) for x in range(D_) if rp[x, y])


if __name__ == '__main__':
    uit = sys.argv[1]; os.makedirs(uit, exist_ok=True)
    K.zet_band()
    b = []
    for wereld in ('krab', 'schild', 'clown'):
        for nacht in (False, True):
            for D_, am in ((260, False), (454, True)):
                K.OMTREK['modus'] = 'wit' if am else 'donker1'
                im = maak(D_, am, nacht, wereld)
                im.save(os.path.join(uit, f'menu-{wereld}-{"nacht" if nacht else "dag"}-{D_}.png'))
                if wereld == 'krab': b.append(im.resize((260, 260), Image.LANCZOS) if D_ == 454 else im)
                print(wereld, 'nacht' if nacht else 'dag', D_, 'voetregel contrast', round(meet_voet(D_, am, nacht, wereld), 2))
    ov = Image.new('RGB', (4 * 260 + 5 * 8, 260 + 16), (30, 30, 30))
    for i, im in enumerate(b): ov.paste(im, (8 + i * 268, 8))
    ov.resize((ov.width * 2, ov.height * 2), Image.NEAREST).save(os.path.join(uit, 'overzicht-menu-krab-2x.png'))
