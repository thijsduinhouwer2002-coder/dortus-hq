# Contrast van elke tekstregel op de onderwaterschermen (onderwater v1): tekst in sleutelkleur geeft het masker; per regel de tekstkleur tegen
# de slechtste achtergrondpixel in een rand van 3 px eromheen (beeld zonder tekst, na nachtregel bij nacht).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import onderwater_v1 as S, krab_keuring2 as K, werelden_v21 as w
from PIL import ImageChops, ImageFilter
def lum(c):
    f = lambda v: (v / 255) / 12.92 if v / 255 <= .03928 else ((v / 255 + .055) / 1.055) ** 2.4
    return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2])
def cr(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True); return (x + .05) / (y + .05)
laag = 99; slecht = 0
for D_, am in ((260, False), (454, True)):
    K.OMTREK['modus'] = 'wit' if am else 'donker1'
    for naam, fn, nacht in S.VOORBEELDEN:
        regels = []
        oud = w.tekst
        def rec(dr, x, y, t, font, c): regels.append((t, c)); oud(dr, x, y, t, font, c)
        w.tekst = rec; fn(D_, am); w.tekst = oud
        kaal = K.zonder_tekst(lambda: fn(D_, am))
        if nacht: kaal = K.nachtregel(kaal, kaal, am)
        # (tekst wordt in de nachtregel niet gedimd; de achtergrond wel)
        for i, (t, c) in enumerate(regels):
            teller = {'n': 0}
            def een(dr, x, y, tt, font, cc):
                if teller['n'] == i: oud(dr, x, y, tt, font, (255, 0, 255))
                teller['n'] += 1
            w.tekst = een; sl = fn(D_, am); w.tekst = oud
            mk = ImageChops.difference(sl, K.zonder_tekst(lambda: fn(D_, am))).convert('L').point(lambda v: 255 if v > 40 else 0)
            ring = ImageChops.subtract(mk.filter(ImageFilter.MaxFilter(7)), mk.filter(ImageFilter.MaxFilter(3)))
            px, rp = kaal.load(), ring.load()
            zelf = {c, K.nacht_pixel(c, am)}   # de uurstreepjes hebben de kleur van hun label: geen achtergrond
            m = min([cr(c, px[x, y]) for y in range(D_) for x in range(D_) if rp[x, y] and px[x, y] not in zelf] or [99])
            laag = min(laag, m)
            if m < 4.5: slecht += 1; print('te laag', D_, naam, t, round(m, 2))
print('laagste', round(laag, 2), 'te laag', slecht)
