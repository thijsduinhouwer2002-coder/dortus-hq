"""Maatschets Hol 2.0 (Sanne, #371). Geen nieuwe kunst: bestaande renders en een spelbeeld
verkleind met nearest en op 32 kleuren gezet, alleen om de MAAT te laten zien."""
from PIL import Image, ImageDraw, ImageFont
import os, random
R = os.path.dirname(os.path.abspath(__file__)); HOL = os.path.dirname(R); REPO = os.path.dirname(os.path.dirname(HOL))
random.seed(7)
spel = Image.open(f"{HOL}/bewijs-strook-hoger/minuut1-std-200-ware-maat.png").convert("RGBA").crop((0, 780, 1920, 1080))
def stuk(box, f):
    s = spel.crop(box); s = s.resize((max(1, round(s.width*f)), max(1, round(s.height*f))), Image.LANCZOS)
    al = s.split()[3].point(lambda v: 255 if v > 110 else 0)
    q = s.convert("RGB").quantize(6, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGBA"); q.putalpha(al); return q
def frame(p, i, h):
    im = Image.open(f"{HOL}/godot/kunst/3d/{p}").convert("RGBA"); a = im.split()[3]; w, hh = im.size
    cols = [any(a.getpixel((x, y)) > 0 for y in range(hh)) for x in range(w)]
    runs = []; s = None
    for x, c in enumerate(cols):
        if c and s is None: s = x
        if not c and s is not None: runs.append((s, x)); s = None
    x0, x1 = runs[i]; f = im.crop((x0, 0, x1, hh)); f = f.crop(f.getbbox())
    return f.resize((max(1, round(f.width*h/f.height)), h), Image.LANCZOS)
def tegel(dst, src, box):
    x0, y0, x1, y1 = box
    for y in range(y0, y1, src.height):
        for x in range(x0, x1, src.width):
            t = src.crop((0, 0, min(src.width, x1-x), min(src.height, y1-y))); dst.alpha_composite(t, (x, y))

W, H = 1920, 120
hol = Image.new("RGBA", (W, H), (0, 0, 0, 0))
# lagen: tuin 0-22, maaiveld 22-26, verdieping 1 26-70, balk 70-74, verdieping 2 74-118, rand 118-120
gras = stuk((720, 56, 930, 96), 0.45); tegel(hol, gras, (0, 4, W, 26))
aarde = stuk((1000, 96, 1120, 128), 0.4)
muur = stuk((880, 178, 1190, 226), 0.4)
for y0, y1 in ((26, 70), (74, 118)):
    tegel(hol, aarde, (0, y0, W, y1))
d = ImageDraw.Draw(hol)
# kamers per verdieping: (x0, x1), muur van de gang erin
kamers = {26: [(40, 300), (330, 640), (700, 980), (1040, 1400), (1460, 1880)], 74: [(120, 520), (560, 900), (960, 1300), (1360, 1700)]}
for y0, lijst in kamers.items():
    for x0, x1 in lijst:
        tegel(hol, muur, (x0, y0+4, x1, y0+44))
        d.rectangle((x0, y0+40, x1, y0+43), fill=(74, 52, 38, 255))
        d.rectangle((x0-3, y0+2, x0-1, y0+43), fill=(92, 66, 44, 255)); d.rectangle((x1+1, y0+2, x1+3, y0+43), fill=(92, 66, 44, 255))
d.rectangle((0, 70, W, 73), fill=(70, 48, 34, 255)); d.rectangle((0, 118, W, 119), fill=(50, 36, 28, 255))
# ladders (tuin naar 1, 1 naar 2)
lad = stuk((255, 85, 312, 245), 0.3)
for x, y in ((310, 6), (1010, 6), (540, 52), (1330, 52)):
    hol.alpha_composite(lad, (x, y))
# fakkels, goud, luiken, struiken
fak = stuk((340, 160, 380, 205), 0.35); goud = stuk((1330, 192, 1435, 240), 0.3)
luik = stuk((560, 218, 640, 246), 0.35); stru = stuk((648, 54, 712, 92), 0.35); bloem = stuk((1370, 64, 1420, 92), 0.35)
for x in (60, 400, 760, 1100, 1500, 180, 620, 1020, 1420): hol.alpha_composite(fak, (x, 30 if x not in (180, 620, 1020, 1420) else 78))
hol.alpha_composite(goud, (1590, 104)); hol.alpha_composite(goud, (1180, 56))
for x in (450, 840, 1250, 1720): hol.alpha_composite(luik, (x, 61))
for x in (720, 820, 1120, 1240, 1640, 1780): hol.alpha_composite(luik, (x, 109))
for x in range(30, W, 140): hol.alpha_composite(stru if (x//140) % 2 else bloem, (x+random.randint(0, 40), 6))
# Gloop 20 px op de troon (verdieping 2), helden 16 px
def retro(sp, n=10):
    al = sp.split()[3].point(lambda v: 255 if v > 110 else 0)
    q = sp.convert("RGB").quantize(n, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGBA"); q.putalpha(al); return q
gl = retro(frame("gloop.png", 0, 20)); hol.alpha_composite(gl, (1566, 98))
helden = ["held0.png", "held1.png", "held2.png", "dief.png", "bard.png", "heks.png"]
plek = [(200, 6), (700, 6), (1300, 6), (500, 54), (880, 54), (1270, 54), (1720, 54), (640, 102), (1000, 102), (1440, 102)]
for i, (x, y) in enumerate(plek):
    hol.alpha_composite(retro(frame(helden[i % len(helden)], (i*3) % 12, 16)), (x, y))
hol.save(f"{R}/hol2-maatschets-120-1x.png")

# bureaublad met taakbalk eromheen (1920 x 1080 op 100%, taakbalk 48)
def scherm(strook, sh):
    s = Image.new("RGBA", (W, 1080), (86, 140, 205, 255))
    s.alpha_composite(spel.crop((0, 0, W, 52)).resize((W, 140)), (0, 1080-48-sh-140+40))
    s.alpha_composite(strook, (0, 1080-48-sh)); ImageDraw.Draw(s).rectangle((0, 1032, W, 1080), fill=(32, 36, 44, 255))
    return s

# ontwerpblad
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f1 = ImageFont.truetype(F.replace("Sans", "Sans-Bold"), 30); f2 = ImageFont.truetype(F, 22)
rusty = Image.open(f"{REPO}/organisatie/lat/beelden/hats/rusty-bureaublad-van-thijs-28nov.png").convert("RGBA").crop((0, 360, 1013, 586))
rusty = rusty.resize((W, round(rusty.height*W/1013)), Image.LANCZOS)
nu200 = spel.crop((0, 40, W, 252))
nu96 = Image.new("RGBA", (W, 96)); nu96.alpha_composite(Image.open(f"{HOL}/bewijs-fps-12/eerste-start-96-links.png").convert("RGBA"), (0, 0)); nu96.alpha_composite(Image.open(f"{HOL}/bewijs-fps-12/eerste-start-96-rechts.png").convert("RGBA"), (960, 0))
zoom = hol.crop((1180, 0, 1660, 120)).resize((1920, 480), Image.NEAREST)
zoomnu = spel.crop((1000, 40, 1480, 252)).resize((1920, 848), Image.NEAREST)
blokken = [
    ("1. Rusty's Retirement (beeld van Thijs, 28 nov), ware verhouding", "strook ±27% van het scherm (±156 van 570 px), 5 rijen dingen, figuur ±8 tot 12% van de strook (GEZIEN, eigen meting)", rusty),
    ("2. Hats nu, 200 px (oude standaard)", "strook 18% van 1080, Gloop ±100 px = ±50% van de strook, 1 gang (GEZIEN)", nu200),
    ("3. Hats nu, 96 px (standaard sinds #372)", "strook 9%, alles kleiner maar nog steeds 1 gang: kleiner maakt het hol niet groter (GEZIEN)", nu96),
    ("4. Hol 2.0 maatschets, 120 px, ware maat (schets uit bestaande kunst)", "tuin 22 + 2 verdiepingen van 44 px, Gloop 20 px (17%), helden 16 px (13%), 6 tot 10 kleuren per ding: 10 helden en 9 kamers in beeld", hol),
    ("5. Hol 2.0 vier keer vergroot (stuk rechts: troon van Gloop onderaan)", "zo zie je de pixels; Mila tekent de echte kunst op deze maat (direct klein renderen, geen anti-aliasing)", zoom),
    ("6. Ter vergelijking: Hats nu, zelfde stuk vier keer vergroot", "Gloop alleen vult al de hele strook", zoomnu.crop((0, 0, 1920, 848))),
]
hoogte = sum(60 + 30 + b[2].height + 30 for b in blokken) + 120
blad = Image.new("RGBA", (W, hoogte), (24, 22, 28, 255)); dd = ImageDraw.Draw(blad)
dd.text((30, 30), "Hats: ontwerpblad Hol 2.0, maat (Sanne, 28 nov, issue #371)", font=ImageFont.truetype(F.replace("Sans", "Sans-Bold"), 40), fill=(255, 214, 120))
y = 110
for kop, sub, img in blokken:
    dd.text((30, y), kop, font=f1, fill=(240, 240, 240)); dd.text((30, y+40), sub, font=f2, fill=(190, 190, 200)); y += 90
    bg = Image.new("RGBA", img.size, (96, 150, 210, 255)); bg.alpha_composite(img); blad.alpha_composite(bg, (0, y)); y += img.height + 30
blad.convert("RGB").save(f"{R}/hol2-ontwerpblad.jpg", quality=90)
scherm(hol, 120).convert("RGB").save(f"{R}/hol2-op-scherm-1080.png")
print("klaar", blad.size)
