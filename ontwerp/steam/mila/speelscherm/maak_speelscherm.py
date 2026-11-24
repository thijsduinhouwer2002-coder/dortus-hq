"""Speelscherm 1920x1080 zoals Rusty's scherm 1: licht bureaublad, werkvenster, het hol als strook onderin.
Mila 24 nov 2026, issue 6. Alles uit code: achtergrond hier met Pillow, de strook is de Blender-render van hol.py
op ware grootte (1920 breed, geen opschaling). Gebruik: python3 maak_speelscherm.py <strook.png> <uit.png> [strookhoogte]
"""
import sys, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

STROOK, UIT = sys.argv[1], sys.argv[2]
SH = int(sys.argv[3]) if len(sys.argv) > 3 else 320
W, H, TB = 1920, 1080, 48
LET = "/home/claude/dortus-hq/producten/steam-hol/godot/kunst/letters/Fredoka.ttf"
INTER = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
random.seed(3)

def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

# lucht: helder blauw boven naar zacht perzik bij de horizon
bg = Image.new("RGB", (W, H))
px = bg.load()
for y in range(H):
    t = y / H
    c = mix((86, 160, 236), (190, 222, 250), min(1, t * 1.3)) if t < 0.75 else mix((190, 222, 250), (255, 222, 196), (t - 0.75) / 0.25)
    for x in range(W):
        px[x, y] = c
# wolken: zachte witte bollen, vervaagd
wl = Image.new("L", (W, H), 0); d = ImageDraw.Draw(wl)
for (cx, cy, s) in [(1350, 210, 1.2), (420, 330, 0.9), (1700, 470, 0.7), (900, 150, 0.6), (250, 560, 0.6)]:
    for k in range(9):
        r = random.uniform(40, 90) * s
        x = cx + random.uniform(-160, 160) * s; y = cy + random.uniform(-25, 25) * s
        d.ellipse((x - r * 1.6, y - r, x + r * 1.6, y + r * 0.7), fill=255)
wl = wl.filter(ImageFilter.GaussianBlur(14))
bg.paste(Image.new("RGB", (W, H), (255, 255, 255)), (0, 0), wl.point(lambda v: int(v * 0.85)))
# heuvels achter de strook: twee lagen, achterste blauwgroen, voorste fris groen
for (basis, amp, kleur, f) in [(H - TB - SH - 70, 50, (122, 186, 140), 0.004), (H - TB - SH - 18, 34, (98, 176, 92), 0.007)]:
    hl = Image.new("L", (W, H), 0); dh = ImageDraw.Draw(hl)
    pts = [(x, basis - amp * math.sin(x * f + basis) - amp * 0.4 * math.sin(x * f * 2.7)) for x in range(0, W + 8, 8)]
    dh.polygon(pts + [(W, H), (0, H)], fill=255)
    bg.paste(Image.new("RGB", (W, H), kleur), (0, 0), hl.filter(ImageFilter.GaussianBlur(1.2)))

dr = ImageDraw.Draw(bg, "RGBA")
f_ic = ImageFont.truetype(INTER, 15)
# bureaubladpictogrammen links boven: eenvoudige mappen en een document
iconen = [("Projects", (240, 196, 80)), ("Notes.txt", (245, 245, 245)), ("Hats of the Fallen", None), ("Recycle Bin", (200, 214, 230))]
icoon = Image.open("/home/claude/dortus-hq/ontwerp/steam/icoon/icoon-tegel-256.png").convert("RGBA").resize((64, 64), Image.LANCZOS)
for i, (naam, k) in enumerate(iconen):
    x, y = 40, 36 + i * 116
    if k is None:
        bg.paste(icoon, (x + 8, y), icoon)
    else:
        dr.rounded_rectangle((x + 10, y + 6, x + 70, y + 60), 8, fill=(*k, 255), outline=(0, 0, 0, 40))
    tw = dr.textlength(naam, font=f_ic)
    dr.text((x + 40 - tw / 2 + 1, y + 72), naam, font=f_ic, fill=(0, 0, 0, 120))
    dr.text((x + 40 - tw / 2, y + 71), naam, font=f_ic, fill=(255, 255, 255, 255))

# werkvenster: een eenvoudige teksteditor, zodat je ziet dat het spel naast je werk loopt
vx0, vy0, vx1, vy1 = 600, 120, 1500, H - TB - SH - 70
sch = Image.new("L", (W, H), 0); ImageDraw.Draw(sch).rounded_rectangle((vx0 + 6, vy0 + 14, vx1 + 6, vy1 + 18), 12, fill=90)
bg.paste(Image.new("RGB", (W, H), (20, 30, 50)), (0, 0), sch.filter(ImageFilter.GaussianBlur(18)))
dr = ImageDraw.Draw(bg, "RGBA")
dr.rounded_rectangle((vx0, vy0, vx1, vy1), 10, fill=(250, 250, 252, 255), outline=(0, 0, 0, 50))
dr.rounded_rectangle((vx0, vy0, vx1, vy0 + 40), 10, fill=(236, 238, 242, 255)); dr.rectangle((vx0, vy0 + 30, vx1, vy0 + 40), fill=(236, 238, 242, 255))
dr.text((vx0 + 18, vy0 + 11), "Notes.txt", font=ImageFont.truetype(INTER, 16), fill=(40, 40, 50, 255))
for j, x in enumerate((vx1 - 120, vx1 - 80, vx1 - 40)):
    dr.line((x - 7, vy0 + 20, x + 7, vy0 + 20), fill=(60, 60, 70, 255), width=2) if j == 0 else dr.rectangle((x - 6, vy0 + 14, x + 6, vy0 + 26), outline=(60, 60, 70, 255), width=2) if j == 1 else (dr.line((x - 6, vy0 + 14, x + 6, vy0 + 26), fill=(60, 60, 70, 255), width=2), dr.line((x - 6, vy0 + 26, x + 6, vy0 + 14), fill=(60, 60, 70, 255), width=2))
f_tx = ImageFont.truetype(INTER, 19)
regels = ["To do today", "", "- answer emails", "- finish the report draft", "- lunch at 12:30", "- check the dungeon at the bottom of the screen",
          "", "Ideas", "- more spikes near the treasure?", "- the knight keeps coming back..."]
for j, r in enumerate(regels):
    dr.text((vx0 + 30, vy0 + 64 + j * 32), r, font=f_tx, fill=(30, 32, 40, 255))
dr.line((vx0 + 30, vy0 + 64 + len(regels) * 32 + 2, vx0 + 30, vy0 + 64 + len(regels) * 32 + 24), fill=(30, 32, 40, 255), width=2)

# de strook: ware grootte als de render precies 1920 breed is
st = Image.open(STROOK).convert("RGBA")
if st.size != (W, SH):
    st = st.resize((W, SH), Image.LANCZOS)
    print("let op: strook geschaald van", Image.open(STROOK).size)
bg.paste(st, (0, H - TB - SH), st)

# taakbalk: neutraal, donker, eenvoudige vormen (geen merken)
dr = ImageDraw.Draw(bg, "RGBA")
dr.rectangle((0, H - TB, W, H), fill=(32, 34, 42, 255))
cx = W // 2 - 4 * 44
for i, k in enumerate([(90, 160, 240), (240, 196, 80), (120, 200, 140), (230, 110, 90), (200, 200, 210)]):
    x = cx + i * 48
    dr.rounded_rectangle((x, H - TB + 10, x + 28, H - TB + 38), 6, fill=(*k, 255))
tb_ic = icoon.resize((30, 30), Image.LANCZOS)
x = cx + 5 * 48; bg.paste(tb_ic, (x, H - TB + 9), tb_ic)
dr.rounded_rectangle((x + 6, H - 5, x + 24, H - 3), 1, fill=(140, 190, 255, 255))
f_kl = ImageFont.truetype(INTER, 15)
dr.text((W - 90, H - TB + 7), "11:21 AM", font=f_kl, fill=(240, 240, 245, 255))
dr.text((W - 92, H - TB + 26), "Tue 24 Nov", font=f_kl, fill=(200, 200, 210, 255))
bg.save(UIT)
print("klaar", UIT)
