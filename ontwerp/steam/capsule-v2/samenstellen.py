"""Zet de header samen (Mila, 27 nov 2026, issue #30): bureaublad erachter, Blender-render erop, taakbalk en ondertitel.

    python3 samenstellen.py <render.png (RGBA, 2x)> <uit.png> [ondertitel]
Het bureaublad is dezelfde rustige lucht met heuvels als op ons speelscherm dat blind won (wolken en heuvels
wazig, zodat het hol scherp vooraan staat). De taakbalk onderaan met een paar app-knopjes en het icoon van Hats
zegt zonder uitleg: dit spel woont onderaan je scherm. Alles getekend met Pillow, geen foto, geen AI.
"""
import sys, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HIER = os.path.dirname(os.path.abspath(__file__))
src, uit = sys.argv[1], sys.argv[2]
ONDER = sys.argv[3] if len(sys.argv) > 3 else "Your taskbar has a basement now"
r = Image.open(src).convert("RGBA")
W, H = r.size
k = W / 920.0
random.seed(3)

# lucht: verloop van diep naar licht blauw
lucht = Image.new("RGB", (W, H))
d = ImageDraw.Draw(lucht)
for y in range(H):
    t = min(1.0, y / (H * 0.45))
    c = tuple(int(a + (b - a) * t) for a, b in zip((74, 150, 232), (170, 214, 248)))
    d.line([(0, y), (W, y)], fill=c)
# wolken: zachte witte bollen, wazig
wl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dw = ImageDraw.Draw(wl)
for cx, cy, s in [(150, 40, 1.0), (520, 30, 1.3), (800, 70, 0.9), (380, 120, 0.7), (690, 150, 0.8)]:
    for i in range(7):
        rx = (40 + random.uniform(0, 30)) * s * k; ry = rx * 0.55
        x = cx * k + random.uniform(-70, 70) * s * k; y = cy * k + random.uniform(-10, 12) * s * k
        dw.ellipse([x - rx, y - ry, x + rx, y + ry], fill=(255, 255, 255, 200))
wl = wl.filter(ImageFilter.GaussianBlur(9 * k))
lucht.paste(wl, (0, 0), wl)
# heuvels achter de graslijn, wazig
hv = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dh = ImageDraw.Draw(hv)
for kleur, basis, amp, fase in [((122, 196, 120), 150, 26, 0.3), ((96, 176, 98), 168, 20, 1.7)]:
    pts = [(0, H)]
    for x in range(0, W + 1, 8):
        import math
        y = (basis - amp * (0.6 * math.sin(x / (W / 2.3) + fase) + 0.4 * math.sin(x / (W / 5.1) + 2 * fase))) * k
        pts.append((x, y))
    pts.append((W, H)); dh.polygon(pts, fill=kleur + (255,))
hv = hv.filter(ImageFilter.GaussianBlur(4 * k))
lucht.paste(hv, (0, 0), hv)

beeld = lucht.convert("RGBA")
beeld.alpha_composite(r)
d = ImageDraw.Draw(beeld)

# taakbalk onderaan
TB = int(30 * k)
balk = Image.new("RGBA", (W, TB), (24, 28, 40, 238))
beeld.alpha_composite(balk, (0, H - TB))
knop = int(18 * k); y0 = H - TB + (TB - knop) // 2
kleuren = [(77, 148, 240), (240, 196, 72), (110, 200, 130), (230, 108, 90)]
n = len(kleuren) + 1; gap = int(8 * k); x0 = W // 2 - (n * knop + (n - 1) * gap) // 2
for i, c in enumerate(kleuren):
    x = x0 + i * (knop + gap)
    d.rounded_rectangle([x, y0, x + knop, y0 + knop], radius=int(4 * k), fill=c)
ico = Image.open(os.path.join(HIER, "..", "icoon", "icoon-tegel-256.png")).convert("RGBA").resize((knop + int(2 * k), knop + int(2 * k)), Image.LANCZOS)
xi = x0 + len(kleuren) * (knop + gap) - int(1 * k)
beeld.alpha_composite(ico, (xi, y0 - int(1 * k)))
d.rounded_rectangle([xi + int(4 * k), H - int(4 * k), xi + knop - int(2 * k), H - int(2 * k)], radius=int(1 * k), fill=(140, 200, 255))

fk = ImageFont.truetype(os.path.join(HIER, "..", "capsule-3d", "LilitaOne-Regular.ttf"), int(12 * k))
d.text((W - int(14 * k), H - TB // 2), "11:21", font=fk, fill=(230, 236, 248), anchor="rm")
d.rounded_rectangle([int(12 * k), y0, int(12 * k) + knop, y0 + knop], radius=int(4 * k), fill=(70, 78, 100))
# ondertitel: donker pilletje onder de titel, in de aarde
if ONDER:
    f = ImageFont.truetype(os.path.join(HIER, "..", "capsule-3d", "LilitaOne-Regular.ttf"), int(float(os.environ.get("OT_MAAT", "29")) * k))
    tx, ty = float(os.environ.get("OT_X", "26")) * k, float(os.environ.get("OT_Y", "210")) * k
    bb = d.textbbox((0, 0), ONDER, font=f)
    pw, ph = bb[2] - bb[0], bb[3] - bb[1]
    px, py = int(14 * k), int(8 * k)
    d.rounded_rectangle([tx, ty, tx + pw + 2 * px, ty + ph + 2 * py], radius=int((ph + 2 * py) / 2), fill=(46, 22, 18, 235), outline=(255, 210, 58), width=max(1, int(2 * k)))
    d.text((tx + px - bb[0], ty + py - bb[1]), ONDER, font=f, fill=(255, 244, 222))

beeld = beeld.convert("RGB")
beeld.resize((920, 430), Image.LANCZOS).save(uit)
beeld.resize((460, 215), Image.LANCZOS).save(uit.replace(".png", "-460.png"))
print("klaar", uit)
