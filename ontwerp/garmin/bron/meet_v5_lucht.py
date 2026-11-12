# Meet het contrast van de tekst op de nieuwe familieluchten (werelden v5): per scherm de slechtste
# achtergrondpixel direct rond de tekst (3 px rand), tegen de tekstkleur. Eis 4,5.
import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import werelden_v21 as w, werelden_v3 as v3
import werelden_v5_lucht as L
from PIL import ImageChops, ImageFilter
def lum(c):
    def f(v):
        v /= 255; return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2])
def cr(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + .05) / (lb + .05)
slecht = 0; laagste = 99
for fam, dieren in L.DIEREN.items():
    mod = importlib.import_module(f'werelden_v4_{fam}'); nieuw, oud = L.maak_lucht(fam); v3.lucht = nieuw
    for dier in dieren:
        for naam in L.ADEM:
            for D_, am in ((454, True), (260, False)):
                f = mod.scherm(naam, dier)
                a = f(D_, am, w.DAG, False); o = w.tekst; w.tekst = lambda *x, **k: None
                b = f(D_, am, w.DAG, False); w.tekst = o
                mk = ImageChops.difference(a, b).convert('L').point(lambda v: 255 if v > 40 else 0)
                ring = ImageChops.subtract(mk.filter(ImageFilter.MaxFilter(7)), mk.filter(ImageFilter.MaxFilter(3)))
                # tekstkleur: helderste pixel in het tekstvak per regel is wit of geel; neem wit (strengst voor lichte luchten)
                px = b.load(); rp = ring.load(); slechtst = 99
                for y in range(0, int(D_ * .45)):   # alleen de lucht (tekst onder water is al gemeten in meet_v4)
                    for x in range(0, D_, 2):
                        if rp[x, y]:
                            slechtst = min(slechtst, cr((255, 255, 255), px[x, y]))
                laagste = min(laagste, slechtst)
                if slechtst < 4.5: slecht += 1; print('te laag', fam, dier, naam, D_, round(slechtst, 2))
    v3.lucht = oud
print('laagste', round(laagste, 2), 'te laag', slecht)
