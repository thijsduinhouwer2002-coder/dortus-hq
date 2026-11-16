# Mila, 16 nov 2026: DOELBEELD, geen winkelbeeld. Laat zien hoe vol het hol moet ogen (bericht hoofdchat 09:45 NL).
# Basis: echte opname week 160 (zaad 2, run 43741619098, beeld 1000). Erbij geplakt: alleen stukken die AL in het spel zitten
# (deco.png en heldenbladen uit producten/steam-hol/godot/kunst/3d), op spelmaat, op plekken waar het spel ze ook kan zetten
# (vloer y 152, plafond van de gang y 96). Het spel zet ze nu nog niet zo dicht: zie LEESMIJ.md hier.
import sys, os
from PIL import Image
import numpy as np
from scipy import ndimage
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
K3 = os.path.join(REPO, 'producten/steam-hol/godot/kunst/3d')
bron = os.path.join(REPO, 'ontwerp/steam/winkelpagina/bron/opnames/week160-zaad2-run43741619098-f1000.png')
s = Image.open(bron).convert('RGBA')
bg = Image.new('RGBA', s.size, (0x2a, 0x1c, 0x36, 255)); bg.alpha_composite(s); s = bg
deco = Image.open(os.path.join(K3, 'deco.png')).convert('RGBA')
a = np.array(deco); col = (a[:, :, 3] > 10).any(0); l, n = ndimage.label(col)
namen = ['fakkel', 'ladder', 'paddenstoel', 'lichtzwam', 'ton', 'krat', 'schedel', 'kristal', 'spinrag', 'stut', 'vaandel',
         'bloemen', 'struik', 'steen', 'bordje', 'vliegenzwam']
stuk = {}
for i in range(1, n + 1):
    xs = np.nonzero(l == i)[0]; x0, x1 = xs.min(), xs.max() + 1
    ys = np.nonzero((a[:, x0:x1, 3] > 10).any(1))[0]
    stuk[namen[i - 1]] = deco.crop((x0, ys.min(), x1, ys.max() + 1))
SCH = 0.85
def zet(naam, x, y, hangend=False, sch=SCH):
    im = stuk[naam]; im = im.resize((round(im.width * sch), round(im.height * sch)), Image.LANCZOS)
    p = (round(x - im.width / 2), y if hangend else y - im.height)
    s.alpha_composite(im, p)
def held(blad, frame, x, y=153, spiegel=False):
    b = Image.open(os.path.join(K3, blad)).convert('RGBA'); w = b.width // 5
    im = b.crop((frame * w, 0, (frame + 1) * w, b.height))
    if spiegel: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    bb = im.getbbox(); im = im.crop(bb)
    s.alpha_composite(im, (round(x - im.width / 2), y - im.height))
V = 152; P = 96
# meer kamers boven de gang (het spel kent kamers op elke kolom zodra je ze graaft; nu staan er maar drie)
from PIL import ImageDraw
kamer = s.crop((448, 47, 562, 95)); km = Image.new('L', kamer.size, 0)
ImageDraw.Draw(km).rounded_rectangle((1, 1, kamer.width - 2, kamer.height - 2), radius=22, fill=255)
for kx, inhoud in [(250, ['schedel', 'ton']), (640, ['krat', 'paddenstoel']), (1010, ['kristal', 'lichtzwam'])]:
    s.paste(kamer, (kx, 47), km)
    # het kistje uit de bronkamer overdekken met de kamerkleur is niet nodig: elke kamer heeft er een
    zet(inhoud[0], kx + 45, 90, sch=0.7); zet(inhoud[1], kx + 75, 90, sch=0.7)
# vloer van de gang: elke vrije tegel iets (nu: hooguit één per twee tegels, en vaak niets)
for naam, x in [('ton', 200), ('paddenstoel', 245), ('schedel', 420), ('krat', 465),
                ('ton', 655), ('schedel', 800), ('paddenstoel', 840), ('krat', 905), ('kristal', 1000)]:
    zet(naam, x, V)
# plafond van de gang: spinrag, vaandel, stut
for naam, x in [('spinrag', 300), ('vaandel', 680), ('stut', 870), ('spinrag', 940)]:
    zet(naam, x, P, hangend=True)
# EIGEN GEZICHT: begraven hoeden in de aardwand (nog niet in het spel; voorstel). Elke held die Gloop at, laat een hoed
# achter die in de wand blijft steken. 3D-renders, zie ontwerp/steam/hoedenwand/.
from PIL import ImageEnhance
hb = Image.open(os.path.join(K3, 'hoeden.png')).convert('RGBA'); hw = hb.width // 10
WAND = os.path.join(REPO, 'ontwerp/steam/hoedenwand/renders')
def begraaf(i, x, y, hoek, breed=50):
    # 3D-render uit ontwerp/steam/hoedenwand/hoedenwand.py (hoek staat vast in de render; hier alleen plek en maat)
    h = Image.open(os.path.join(WAND, f'wand-{i}.png')).convert('RGBA'); h = h.crop(h.getbbox())
    h = h.resize((breed, round(h.height * breed / h.width)), Image.LANCZOS)
    s.alpha_composite(h, (round(x - h.width / 2), round(y - h.height * 0.6)))
for i, x, y, hoek in [(4, 412, 72, 20), (7, 600, 66, -25), (1, 800, 78, 15), (8, 975, 62, -10), (3, 1160, 66, 30),
                      (0, 1440, 74, -20), (9, 1570, 56, 25), (5, 1700, 78, -15), (2, 215, 66, 10)]:
    begraaf(i, x, y, hoek)
# twee helden er extra bij (bard en heks lopen naar binnen), naast Wout
held('bard.png', 1, 505)
held('heks.png', 0, 330)
s.convert('RGB').save(os.path.join(os.path.dirname(__file__), 'doelbeeld-strook-vol.png'))
# winkelvorm zoals scherm 1: twee rijen van de strook boven elkaar, 2,7x
W, H = 1920, 1080
def rij(x0, x1):
    c = s.crop((x0, 0, x1, 160)); z = W / (x1 - x0); return c.resize((W, round(160 * z)), Image.LANCZOS).convert('RGB')
r1 = rij(40, 750); r2 = rij(750, 1460)
im = Image.new('RGB', (W, H), (0x1a, 0x12, 0x22))
im.paste(r1, (0, 0)); im.paste(r2, (0, r1.height + 4))
# rest: het kaartje uit dezelfde opname
k = s.crop((1460, 90, 1920, 160)); z = (H - r1.height * 2 - 8) / 70
k = k.resize((round(k.width * z), H - r1.height * 2 - 8), Image.LANCZOS).convert('RGB')
im.paste(k, ((W - k.width) // 2, r1.height * 2 + 8))
im.save(os.path.join(os.path.dirname(__file__), 'doelbeeld-vol-1920.png'))
