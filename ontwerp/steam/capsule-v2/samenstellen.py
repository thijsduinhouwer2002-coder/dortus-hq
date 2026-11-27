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
if os.environ.get("GLOED", "0") == "1":
    # v6: zachte gloed om het felle licht (fakkels, ring, goud) en een warme kleurtoon met lichte vignet,
    # zodat het minder als kaal plastic leest (Gemini 27 nov: "refine the lighting").
    import numpy as np
    a = np.asarray(beeld.convert("RGB")).astype(np.float32) / 255.0
    lum = a.max(axis=2, keepdims=True)
    hel = np.clip((lum - float(os.environ.get("GLOEDDREMPEL", "0.8"))) / 0.2, 0, 1) * a
    hi = Image.fromarray((hel * 255).astype(np.uint8))
    g1 = np.asarray(hi.filter(ImageFilter.GaussianBlur(6 * k))).astype(np.float32) / 255.0
    g2 = np.asarray(hi.filter(ImageFilter.GaussianBlur(22 * k))).astype(np.float32) / 255.0
    a = 1 - (1 - a) * (1 - float(os.environ.get("GLOEDK", "0.35")) * (g1 + g2) / 2 * 2)
    # warm in de lichten, iets koeler in de schaduw
    w = np.array([1.03, 1.0, 0.94], np.float32); c = np.array([0.96, 0.99, 1.04], np.float32)
    a = a * (lum * w + (1 - lum) * c)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    v = ((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.55) / (H * 0.85)) ** 2
    a = a * (1 - float(os.environ.get("VIGNET", "0.18")) * np.clip(v, 0, 1))[..., None]
    beeld = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).convert("RGBA")
d = ImageDraw.Draw(beeld)

# taakbalk onderaan (v3, Daan #236 M3: hoger, knoppen groter, Hats-knop opgelicht als open app, en een muispijl,
# zodat "dit is je bureaublad" ook zonder ondertitel leest)
TB = int(float(os.environ.get("TB", "40")) * k)
balk = Image.new("RGBA", (W, TB), (24, 28, 40, 242))
beeld.alpha_composite(balk, (0, H - TB))
d.line([(0, H - TB), (W, H - TB)], fill=(70, 80, 104), width=max(1, int(1 * k)))
knop = int(24 * k); y0 = H - TB + (TB - knop) // 2
kleuren = [(77, 148, 240), (240, 196, 72), (110, 200, 130), (230, 108, 90)]
ik = int(32 * k)   # Hats-knop groter dan de rest
n = len(kleuren); gap = int(12 * k); x0 = W // 2 - (n * knop + n * gap + ik) // 2
for i, c in enumerate(kleuren):
    x = x0 + i * (knop + gap)
    d.rounded_rectangle([x, y0, x + knop, y0 + knop], radius=int(5 * k), fill=c)
    d.rounded_rectangle([x + int(6 * k), y0 + int(6 * k), x + knop - int(6 * k), y0 + knop - int(6 * k)], radius=int(2 * k), fill=(255, 255, 255, 120))
xi = x0 + n * (knop + gap); yi = H - TB + (TB - ik) // 2 - int(1 * k)
gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
dg.rounded_rectangle([xi - int(5 * k), H - TB + int(2 * k), xi + ik + int(5 * k), H - int(2 * k)], radius=int(7 * k), fill=(120, 190, 255, 90))
beeld.alpha_composite(gl)
ico = Image.open(os.path.join(HIER, "..", "icoon", "icoon-tegel-256.png")).convert("RGBA").resize((ik, ik), Image.LANCZOS)
beeld.alpha_composite(ico, (xi, yi))
d.rounded_rectangle([xi + int(6 * k), H - int(4 * k), xi + ik - int(6 * k), H - int(1.5 * k)], radius=int(1 * k), fill=(140, 210, 255))

fk = ImageFont.truetype(os.path.join(HIER, "..", "capsule-3d", "LilitaOne-Regular.ttf"), int(15 * k))
d.text((W - int(16 * k), H - TB // 2), "11:21", font=fk, fill=(230, 236, 248), anchor="rm")
d.rounded_rectangle([int(14 * k), y0, int(14 * k) + knop, y0 + knop], radius=int(5 * k), fill=(70, 78, 100))
for dx in (0, 1):
    for dy in (0, 1):
        q = int(5 * k); xx = int(14 * k) + int(5 * k) + dx * (q + int(2 * k)); yy = y0 + int(5 * k) + dy * (q + int(2 * k))
        d.rectangle([xx, yy, xx + q, yy + q], fill=(200, 210, 230))

# muispijl in de lucht: klassieke pijl, wit met donkere rand
mx, my, ms = float(os.environ.get("MX", "462")) * k, float(os.environ.get("MY", "62")) * k, float(os.environ.get("MS", "1.45")) * k
pijl = [(0, 0), (0, 17), (4, 13), (7, 20), (10, 19), (7, 12), (12, 12)]
pts = [(mx + x * ms, my + y * ms) for x, y in pijl]
sch = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sch)
ds.polygon([(x + 2 * k, y + 2 * k) for x, y in pts], fill=(0, 0, 0, 90))
sch = sch.filter(ImageFilter.GaussianBlur(1.5 * k)); beeld.alpha_composite(sch)
d.polygon(pts, fill=(255, 255, 255), outline=(20, 20, 28), width=max(1, int(1.4 * k)))

# valstreepjes boven de held (Pillow, zodat ze niet als stokjes door hem heen steken).
# v4 (Daan #243 kan 2): drie in plaats van vier, elk een andere lengte, dunner en spits naar boven, iets schuin
# mee met de val, zodat ze als beweging lezen en niet als kaarsjes.
for (x, y0s, l) in [(float(v) for v in t.split(":")) for t in os.environ.get("STREEP", "522:166:30,566:172:18,612:196:12").split(",")]:
    yb = (y0s + l) * k; yt = y0s * k; xb = x * k; xt = xb - 0.12 * l * k   # top iets naar links: schuin mee
    bw = 1.5 * k
    d.polygon([(xt - 0.25 * k, yt), (xt + 0.25 * k, yt), (xb + bw, yb - bw), (xb, yb), (xb - bw, yb - bw)], fill=(255, 250, 236, 235))
    d.ellipse([xb - bw, yb - 2 * bw, xb + bw, yb], fill=(255, 250, 236, 235))

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
if os.environ.get("RECHTS2X"):   # uitsnede midden en rechts op 2x, om zelf te kijken
    beeld.crop((int(470 * k), 0, W, H)).save(os.environ["RECHTS2X"])
beeld.resize((920, 430), Image.LANCZOS).save(uit)
beeld.resize((460, 215), Image.LANCZOS).save(uit.replace(".png", "-460.png"))
print("klaar", uit)
