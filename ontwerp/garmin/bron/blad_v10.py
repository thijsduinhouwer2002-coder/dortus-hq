# Blad v10 (run 34, 11 nov): "Voor Mila" uit keuring bouw 5.
# 1. sea complete als rustige groepsfoto (geen kluwen), fontein onder de kamlijn, met posities voor Gijs.
# 2. pauzemenu in Ebb-stijl (Resume, Save, Discard), je eigen dier wijst je keuze aan, de zee staat stil.
# Getekend met horloge_sim.py (nabootsing DierenData.mc) en Barlow Condensed (OFL).
import sys, os, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import horloge_sim as h
from blad_v9 import zee, rond, tekst, f, FM, FS, SCHUIM, LICHT, MIDDEN, DIEP, NACHT, WIT, GEEL, D
from PIL import Image, ImageDraw
B = os.path.dirname(os.path.abspath(__file__)); G = os.path.join(B, '..')
uit = os.path.join(G, 'blad10'); os.makedirs(uit, exist_ok=True)

def zee_stil(im, top, D_):
    """Zee zonder golf: platte kamlijn. Zo zie je dat alles stilstaat (pauze)."""
    dr = ImageDraw.Draw(im); b = D_ - top
    dr.rectangle([0, top, D_, D_], fill=MIDDEN)
    dr.rectangle([0, top, D_, top + max(2, D_ // 100)], fill=SCHUIM)
    dr.rectangle([0, round(D_ * 0.8), D_, D_], fill=NACHT)   # menu staat op één tint; alleen onderin de diepte

# ---------- 1. sea complete: groepsfoto ----------
# Alles in 1/260 van de diameter (x vanaf het midden, y vanaf de bovenkant), keer D/260 voor elk horloge.
ZEE_SC = 58           # kamlijn
WALVIS = (0, 100, 32)  # x, y, maat (op 454: maat 56)
BEL = ((0, 71, 3), (-6, 64, 2), (5, 62, 2))   # fontein: drie belletjes, alle drie onder de kamlijn
# Groepsfoto: naast de walvis 2 + 2, dan rijen van 7, 6 en 6 (de ronde vorm volgt het scherm).
RIJEN = ((100, (-86, -58, 58, 86)),
         (136, (-87, -58, -29, 0, 29, 58, 87)),
         (160, (-76, -47, -18, 18, 47, 76)),
         (188, (-72, -45, -17, 17, 45, 72)))
VRIEND = 11            # maat op 260 (op 454: 19)

def vriend_maat(D_):   # 218: 8, 240: 9, 260: 11, 280: 11, 360: 15, 390: 16, 416: 17, 454: 19
    return math.floor(VRIEND * D_ / 260) - (1 if D_ < 250 else 0)   # de stickerrand is altijd 2 px, dus onder 250 een maat kleiner
def walvis_maat(D_): return round(WALVIS[2] * D_ / 260)   # 260: 32, 416: 51, 454: 56

def plekken():
    p = []
    for y, xs in RIJEN:
        for x in xs: p.append((x, y))
    return p   # 23 plekken, dier nr 1 tot 23 op volgorde (links naar rechts, boven naar onder)

def sea_complete(D_, weken=12):
    s = D_ / 260; im = Image.new('RGB', (D_, D_)); c = D_ // 2
    zee(im, round(ZEE_SC * s), D_); dr = ImageDraw.Draw(im)
    for dx, dy, r in BEL:
        x, y, rr = c + dx * s, dy * s, max(2, round(r * s))
        dr.ellipse([x - rr, y - rr, x + rr, y + rr], outline=SCHUIM, width=max(1, round(s)))
    wx, wy, wm = WALVIS
    h.teken(dr, D[23], c + round(wx * s), round(wy * s), walvis_maat(D_))
    m = vriend_maat(D_)
    for nr, (x, y) in enumerate(plekken()):
        h.teken(dr, D[nr], c + round(x * s), round(y * s), m)
    tekst(dr, c, 18 * s, 'sea complete', f(FS, round(25 * s)), GEEL)
    tekst(dr, c, 206 * s, '24 of 24 friends', f(FM, round(17 * s)), SCHUIM)
    tekst(dr, c, 226 * s, f'{weken} weeks', f(FM, round(15 * s)), SCHUIM)
    return rond(im)

# ---------- 2. pauzemenu ----------
KEUZES = ('Resume', 'Save', 'Discard')
def pauze(D_, kies=0, dier=4, ronde=2, tijd='1:12'):
    s = D_ / 260; im = Image.new('RGB', (D_, D_)); c = D_ // 2
    zee_stil(im, round(84 * s), D_); dr = ImageDraw.Draw(im)
    tekst(dr, c, 24 * s, 'paused', f(FS, round(26 * s)), SCHUIM)
    tekst(dr, c, 56 * s, f'round {ronde}  ·  {tijd}', f(FM, round(17 * s)), WIT)
    fk = f(FS, round(24 * s))
    for i, k in enumerate(KEUZES):
        y = round((106 + i * 38) * s)            # middenlijn van de keuze
        w = dr.textlength(k, font=fk)
        if i == kies:
            pw, ph = round(110 * s), round(32 * s)
            dr.rounded_rectangle([c - pw // 2, y - ph // 2, c + pw // 2, y + ph // 2], radius=ph // 2, fill=SCHUIM)
            dr.text((c - w / 2, y), k, font=fk, fill=NACHT, anchor='lm')
            # je eigen dier zwemt naast je keuze (wijst hem aan)
            m = round(12 * D_ / 260)
            h.teken(dr, D[dier], c - pw // 2 - round(22 * s), y, m)
        else:
            dr.text((c - w / 2, y), k, font=fk, fill=WIT, anchor='lm')
    tekst(dr, c, 214 * s, 'the sea waits', f(FM, round(15 * s)), LICHT)
    return rond(im)

def groot(im, k): return im.resize((im.width * k, im.height * k), Image.NEAREST)

def overlap_check(D_):
    """Raken twee dieren in de groepsfoto elkaar (met 1 px marge)? En staat er een pixel buiten 0,85 R? Gemeten op pixels."""
    from PIL import ImageFilter, ImageChops
    s = D_ / 260; c = D_ // 2; m = vriend_maat(D_); R = 0.85 * D_ / 2; ms = []
    for nr, (x, y) in enumerate(plekken() + [(0, WALVIS[1])]):
        t = Image.new('RGB', (D_, D_))
        h.teken(ImageDraw.Draw(t), D[nr if nr < 23 else 23], c + round(x * s), round(y * s), m if nr < 23 else walvis_maat(D_))
        ms.append(t.convert('L').point(lambda v: 255 if v else 0))
    raak = [(i + 1, j + 1) for i in range(len(ms)) for j in range(i + 1, len(ms))
            if ImageChops.multiply(ms[i].filter(ImageFilter.MaxFilter(3)), ms[j]).getbbox()]
    rand = Image.new('L', (D_, D_), 255); ImageDraw.Draw(rand).ellipse([c - R, c - R, c + R, c + R], fill=0)
    buiten = sum(1 for mk in ms if ImageChops.multiply(mk, rand).getbbox())
    return raak, buiten

if __name__ == '__main__':
    for D_ in (218, 240, 260, 280, 360, 390, 416, 454):
        sea_complete(D_).save(os.path.join(uit, f'sea-complete-{D_}.png'))
        for k in range(3): pauze(D_, k).save(os.path.join(uit, f'pauze-{k + 1}-{D_}.png'))
        r, b = overlap_check(D_)
        print(D_, 'dieren die elkaar raken (1 px marge):', r, '; dieren met pixels buiten 0,85 R:', b)
