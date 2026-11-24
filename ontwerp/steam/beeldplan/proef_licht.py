"""Proefbeeld Hats: hetzelfde hol, maar met licht, diepte, glans en stof.
Alleen 2D-bewerkingen die Godot ook kan (CanvasModulate, PointLight2D, glow, deeltjes).
Gebruik: python3 proef_licht.py <bron.png> <uit.png>"""
import sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw

bron, uit = sys.argv[1], sys.argv[2]
im = Image.open(bron).convert("RGB").crop((0, 340, 960, 680))
S = 2
im = im.resize((im.width * S, im.height * S), Image.LANCZOS)
a = np.asarray(im).astype(np.float32) / 255.0
H, W, _ = a.shape
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

# 1. Donker en koel als basis (CanvasModulate), maar daglicht door het gras bovenin elke rij
amb = np.zeros_like(a) + np.array([0.34, 0.33, 0.48])
for top in (10, 180):                       # bovenkant van elke rij in de crop (1x)
    t = np.clip(1 - (yy / S - (top + 30)) / 22.0, 0, 1) * ((yy / S >= top - 12) & (yy / S < top + 160))
    amb = amb * (1 - t[..., None]) + t[..., None] * 1.0   # gras: gewoon daglicht
amb = np.clip(amb, 0, 1.0)

# 2. Lichtpoelen (PointLight2D): fakkels warm, schat goud, Gloop muntgroen, kristal koel
def poel(x, y, r, kleur, kracht):
    d2 = ((xx - x * S) ** 2 + ((yy - y * S) * 1.25) ** 2) / (r * S) ** 2
    return np.exp(-d2)[..., None] * np.array(kleur) * kracht

lichten = [
    (160, 122, 80, (1.0, 0.62, 0.30), 0.80),   # fakkel rij 1 links
    (465, 73, 95, (1.0, 0.62, 0.30), 0.65),    # nis met fakkel
    (848, 73, 95, (1.0, 0.62, 0.30), 0.65),
    (395, 300, 110, (1.0, 0.75, 0.35), 0.55),  # schat
    (290, 285, 75, (0.55, 1.0, 0.8), 0.30),    # Gloop
    (437, 265, 55, (1.0, 0.62, 0.30), 0.50),   # fakkel bij de schat
    (862, 150, 55, (0.55, 0.80, 1.0), 0.55),   # kristal
    (352, 113, 30, (1.0, 0.85, 0.4), 0.30),    # munten
    (736, 113, 30, (1.0, 0.85, 0.4), 0.30),
    (95, 282, 30, (1.0, 0.85, 0.4), 0.30),
]
L = amb.copy()
for l in lichten:
    L += poel(*l)
out = a * L

# 3. Contactschaduw: zachte donkere band op de vloerlijn van elke rij
for vloer in (148, 318):
    band = np.exp(-((yy - vloer * S) / (5 * S)) ** 2)[..., None]
    out *= 1 - 0.35 * band

# 4. Vignet per rij (diepte naar de randen)
vig = 1 - 0.35 * (np.abs(xx - W / 2) / (W / 2)) ** 2.2
out *= vig[..., None]

# 5. Glow (WorldEnvironment glow): heldere delen gaan zacht gloeien
out = np.clip(out, 0, 1)
helder = np.clip((out.max(axis=2) - 0.80) / 0.20, 0, 1)[..., None] * out
gl = Image.fromarray((helder * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(9 * S))
out = np.clip(out + np.asarray(gl).astype(np.float32) / 255 * 0.55, 0, 1)

# UI-paneel blijft zoals het is (licht hoort niet op de interface)
x0, y0, x1, y1 = 508 * S, 274 * S, 953 * S, 338 * S
out[y0:y1, x0:x1] = a[y0:y1, x0:x1]
beeld = Image.fromarray((out * 255).astype(np.uint8)).convert("RGBA")

# 6. Stof in het licht (GPUParticles2D) en twinkels op goud
rng = np.random.default_rng(7)
laag = Image.new("RGBA", beeld.size, (0, 0, 0, 0))
dr = ImageDraw.Draw(laag)
for (x, y, r, kleur, k) in lichten[:6]:
    for _ in range(int(22 * k)):
        px = x * S + rng.normal(0, r * S * 0.45); py = y * S + rng.normal(0, r * S * 0.30)
        rr = rng.uniform(0.8, 2.0) * S / 2
        al = int(rng.uniform(70, 170))
        dr.ellipse((px - rr, py - rr, px + rr, py + rr), fill=(255, 225, 170, al))
laag = laag.filter(ImageFilter.GaussianBlur(0.6 * S))
beeld = Image.alpha_composite(beeld, laag)
dr = ImageDraw.Draw(beeld)
def twinkel(x, y, n):
    x, y = x * S, y * S
    for w, al in ((n, 120), (n * 0.45, 255)):
        dr.line((x - w, y, x + w, y), fill=(255, 250, 220, al), width=max(1, S // 2 + (al > 200)))
        dr.line((x, y - w, x, y + w), fill=(255, 250, 220, al), width=max(1, S // 2 + (al > 200)))
for (x, y, n) in [(346, 106, 9), (731, 106, 9), (92, 276, 8), (385, 288, 11), (412, 298, 7), (420, 280, 6), (860, 140, 8), (294, 196, 7)]:
    twinkel(x, y, n * S / 2)

beeld.convert("RGB").save(uit)
print("klaar", uit, beeld.size)
