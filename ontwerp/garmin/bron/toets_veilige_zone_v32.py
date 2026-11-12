# Gebruik: cd bron; python3 toets_veilige_zone_v32.py
# Toets veilige zone (hoofdchat 12 nov 04:05): geen dier en geen grapvoorwerp (slipper, meeuw, ballen, mutsje)
# mag binnen MARGE van een tekstregel of cijfer komen, op geen enkel scherm (in, uit en calm zijn de drie standen van het dobberen).
# Werkwijze: teken elk scherm zonder tekst (tekst wordt alleen opgemeten), en nog eens zonder de held-groep.
# Wat verschilt is de held-groep. Daarna per tekstvak de kleinste afstand tot een pixel van de held-groep.
import sys; sys.path.insert(0, '.')
import werelden_v32 as v, werelden_v21 as w, werelden_v3 as v3
from PIL import ImageChops
MARGE = 6            # in 1/260 D: lucht tussen tekst en held, ook voor de grotere systeemletter van de FR255
vakken = []
def nep(self, x, y, s, maat, c, dik=True):
    f = w.f(w.FS if dik else w.FM, round(maat * self.s)); l, t, r, b = f.getbbox(s)
    ww = self.dr.textlength(s, font=f); X = x * self.s - ww / 2; Y = y * self.s
    K = self.k; vakken.append((s, (int(X/K), int((Y + t)/K), int((X + ww)/K), int((Y + b)/K))))
w.Doek.tekst = nep
HELD = ['slipper', 'bandje', 'meeuw', 'jongleer', 'clownshoed', 'dier_kantel', 'spat']
echt = {(m.__name__, n): getattr(m, n) for m in (w, v3, v) for n in HELD if hasattr(m, n)}
echt_dier = w.Doek.dier
def zonder_held(aan):
    for (mn, n), fn in echt.items():
        mod = {'werelden_v21': w, 'werelden_v3': v3, 'werelden_v32': v}[mn]
        setattr(mod, n, (lambda *a, **k: (lambda *b, **c: (-99, -99))) if aan else fn)
    w.Doek.dier = (lambda *a, **k: None) if aan else echt_dier
fout = 0; krap = []
for wereld in ['krab', 'schild', 'clown']:
  for nacht in (False, True):
    dd = v.NACHT if nacht else v.DAG
    for D_, am in ((454, True), (260, False)):
        k = D_ / 260
        for naam in v.NAMEN:
            vakken.clear(); zonder_held(False); a = v.scherm(naam, wereld)(D_, am, dd, nacht).convert('RGB')
            vk = list(vakken); vakken.clear(); zonder_held(True); b = v.scherm(naam, wereld)(D_, am, dd, nacht).convert('RGB')
            zonder_held(False)
            mk = ImageChops.difference(a, b).convert('L').point(lambda q: 255 if q > 24 else 0)
            px = mk.load(); pts = [(x, y) for y in range(0, D_, 1) for x in range(0, D_, 1) if px[x, y]]
            for s, (x0, y0, x1, y1) in vk:
                if not pts: break
                dmin = min(max(x0 - x, 0, x - x1) ** 2 + max(y0 - y, 0, y - y1) ** 2 for x, y in pts) ** .5 / k
                tag = f'{wereld} {naam} {"nacht" if nacht else "dag"} {D_}: "{s}" {dmin:.1f}'
                if dmin < MARGE: fout += 1; print('TE DICHT', tag)
                elif dmin < MARGE + 4: krap.append(tag)
print('krap (binnen marge + 4):', len(krap)); [print('  ', t) for t in krap[:12]]
print(f'regels te dicht bij de held (marge {MARGE}/260):', fout)
