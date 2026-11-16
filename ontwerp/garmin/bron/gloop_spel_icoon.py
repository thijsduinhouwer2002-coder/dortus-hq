# Gloop op je pols: voorstel icoon (winkel 500x500 en launcher op horlogemaat), Mila 16 nov 2026.
# Alleen uit dezelfde renders als de kit: Gloop slokt een held, toren van hoeden loopt boven de rand uit.
#   python3 gloop_spel_icoon.py <rendermap> <uitmap>
import sys, os, random
from PIL import Image, ImageDraw, ImageFilter
R, UIT = sys.argv[1], sys.argv[2]
sys.argv = ["x", R, os.path.join(UIT, "_kit")]
import gloop_spel_kit as k
import gloop_spel_v2 as v2

ACHTER = {"oranje": ((255, 138, 30), (255, 200, 110), (150, 50, 20)), "paars": ((120, 60, 190), (170, 110, 235), (60, 25, 90)), "grot": ((226, 140, 70), (246, 190, 120), (110, 46, 26))}
KLEUR = "grot"


def icoon(N, variant):
    W = int(N * 1.9)              # Gloop = 0.34 W, dus ±0.6 N breed: ruimte voor de toren
    sl, _ = k.slok_sprite(W)
    rust = k.v2.schaal(k.v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-rust-h0.png")).convert("RGBA")), W * k.GLOOP_B)
    hap_h = k.v2.schaal(k.v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-hap-h0.png")).convert("RGBA")), W * k.GLOOP_B).height
    H = v2.hoeden()
    bg, licht, vloer = ACHTER[KLEUR]
    im = Image.new("RGBA", (N, N), bg + (255,))
    # warme grot met lichtbundel schuin van linksboven (zelfde als het spel)
    lam = Image.new("L", (N, N), 0); d = ImageDraw.Draw(lam)
    d.line([(N * -0.1, N * -0.1), (N * 0.45, N * 0.8)], fill=255, width=int(N * 0.28))
    lam = lam.filter(ImageFilter.GaussianBlur(N * 0.03))
    im = Image.composite(Image.new("RGBA", (N, N), licht + (255,)), im, lam)
    ImageDraw.Draw(im).ellipse([-0.2 * N, 0.86 * N, 1.2 * N, 1.4 * N], fill=vloer + (255,))
    cx, voet = N * 0.42, N * 1.03   # onderkant van Gloop valt weg: meer hoogte voor de toren
    gx = int(cx - rust.width / 2)
    if variant == "slok":
        im.alpha_composite(sl, (gx, int(voet - hap_h)))
    else:
        im.alpha_composite(rust, (gx, int(voet - rust.height)))
    # toren: helm, kroon, puntmuts, koksmuts, emmer ... tot boven de rand
    rij = [0, 4, 5, 1, 7] if variant == "slok" else [4, 5, 1, 7, 6]   # minder, grotere hoeden: kijker 05:05 zag een propje
    y = voet - rust.height + rust.height * k.KRUIN
    x = gx + rust.width * 0.53
    rnd = random.Random(3)
    for n, i in enumerate(rij):
        h = k.los_weg(k.v2.schaal(H[i], W * 0.165)).rotate(-5 - 6 * n, expand=True, resample=Image.BICUBIC)   # helt steeds meer: wiebelt
        top = y - h.height * 0.86
        im.alpha_composite(h, (int(x - h.width / 2), int(top)))
        y = top + h.height * 0.16
        x += 0.07 * rust.width   # toren helt steeds verder naar rechts: hij gaat zo om
    return im

os.makedirs(UIT, exist_ok=True)
for KLEUR in ("oranje", "paars"):
    for var in ("slok", "rust"):
        icoon(1000, var).resize((500, 500), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"icoon-500-{var}-{KLEUR}.png"))
KLEUR = "paars"   # blinde kijker 05:05: paars steekt af tussen de toppers (blauw, groen, oranje)
for var in ("slok", "rust"):
    big = icoon(1000, var)
    big.resize((500, 500), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"icoon-500-{var}.png"))
    # launcher: strakker (Gloop groter, onderste hoeden): op 40 px moet het oog het herkenbare zijn
    strak = big.crop((40, 200, 840, 1000))
    for n in (40, 60, 80):
        strak.resize((n, n), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"launcher-{n}-{var}.png"))
import shutil; shutil.rmtree(os.path.join(UIT, "_kit"), ignore_errors=True)
print("klaar")
