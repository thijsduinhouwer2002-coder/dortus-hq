# Gebruik: cd bron; python3 meet_v4_licht.py
# Contrast (lichtste achtergrond in het vak van elke tekstregel, eis 4,5) en veilige zone (6/260 tussen tekst en dier plus grapvoorwerp)
# voor de familie licht (kwal, zeepaardje, maanvis, haai). Kopie van meet_contrast_v32 en toets_veilige_zone_v32.
# Ook: op 260 (MIP) alleen de 64 kleuren.
import sys; sys.path.insert(0, '.')
import werelden_v4_licht as L4, werelden_v21 as w, werelden_v3 as v3
from PIL import ImageChops
MARGE = 6
vakken = []
def nep(self, x, y, s, maat, c, dik=True):
    f = w.f(w.FS if dik else w.FM, round(maat * self.s)); l, t, r, b = f.getbbox(s)
    ww = self.dr.textlength(s, font=f); X = x * self.s - ww / 2; Y = y * self.s
    K = self.k; vakken.append((s, c, (int(X/K), int((Y + t)/K), int((X + ww)/K), int((Y + b)/K))))
w.Doek.tekst = nep
def Lum(c):
    r = [(v_/255)/12.92 if v_/255 <= 0.03928 else ((v_/255+0.055)/1.055)**2.4 for v_ in c[:3]]
    return 0.2126*r[0]+0.7152*r[1]+0.0722*r[2]
# held-groep: alle grapvoorwerpen en het dier
NAMEN_H = ['held_jelly', 'held_seahorse', 'held_sunfish', 'held_shark', 'regenwolk', 'handvat', 'paal', 'zonnebril', 'bril_aan_koord',
           'tandenborstel', 'poetsvisje']
echt = {n: getattr(L4, n) for n in NAMEN_H}
echt_dk, echt_dier = v3.dier_kantel, w.Doek.dier
HELD0 = dict(L4.HELD)
def zonder_held(aan):
    for n, fn in echt.items(): setattr(L4, n, (lambda *a, **k: None) if aan else fn)
    L4.HELD.update({k: ((lambda *a, **kw: None) if aan else fn) for k, fn in HELD0.items()})
    v3.dier_kantel = (lambda *a, **k: None) if aan else echt_dk
    w.Doek.dier = (lambda *a, **k: None) if aan else echt_dier
MIP = {0, 85, 170, 255}
slecht = fout = kleur = 0; krap = []
for dier in L4.DIEREN:
  for nacht in (False, True):
    dd = w.NACHT if nacht else w.DAG
    for D_, am in ((454, True), (260, False)):
        k = D_ / 260
        for naam in L4.NAMEN:
            vakken.clear(); zonder_held(False); a = L4.scherm(naam, dier)(D_, am, dd, nacht).convert('RGB'); vk = list(vakken)
            px = a.load(); tag0 = f'{dier} {naam} {"nacht" if nacht else "dag"} {D_}'
            for s, c, (x0, y0, x1, y1) in vk:
                if x1 <= x0 or y1 <= y0: continue
                hi = max(Lum(px[x, y]) for x in range(max(0, x0), min(D_, x1)) for y in range(max(0, y0), min(D_, y1)))
                kk = (Lum(c) + .05) / (hi + .05)
                if kk < 4.5: slecht += 1; print(f'CONTRAST {tag0}: "{s}" {kk:.1f}')
            if not am:
                bad = [c for n_, c in a.getcolors(1 << 16) if any(ch not in MIP for ch in c)]
                if bad: kleur += 1; print(f'KLEUR {tag0}: {len(bad)} kleuren buiten de 64, bv {bad[:3]}')
            vakken.clear(); zonder_held(True); b = L4.scherm(naam, dier)(D_, am, dd, nacht).convert('RGB'); zonder_held(False)
            mk = ImageChops.difference(a, b).convert('L').point(lambda q: 255 if q > 24 else 0)
            pm = mk.load(); pts = [(x, y) for y in range(D_) for x in range(D_) if pm[x, y]]
            for s, c, (x0, y0, x1, y1) in vk:
                if not pts: break
                dmin = min(max(x0 - x, 0, x - x1) ** 2 + max(y0 - y, 0, y - y1) ** 2 for x, y in pts) ** .5 / k
                tag = f'{tag0}: "{s}" {dmin:.1f}'
                if dmin < MARGE: fout += 1; print('TE DICHT', tag)
                elif dmin < MARGE + 4: krap.append(tag)
print('krap (binnen marge + 4):', len(krap)); [print('  ', t) for t in krap[:16]]
print('regels onder 4,5:', slecht)
print(f'regels te dicht bij dier of grap (marge {MARGE}/260):', fout)
print('MIP-schermen met kleuren buiten de 64:', kleur)
