# Gloop op je pols: voorstel icoon (winkel 500x500 en launcher op horlogemaat), Mila 16 nov 2026.
# Alleen uit dezelfde renders als de kit: Gloop slokt een held, toren van hoeden loopt boven de rand uit.
#   python3 gloop_spel_icoon.py <rendermap> <uitmap>
import sys, os, random
from PIL import Image, ImageDraw, ImageFilter
R, UIT = sys.argv[1], sys.argv[2]
sys.argv = ["x", R, os.path.join(UIT, "_kit")]
import gloop_spel_kit as k
import gloop_spel_v2 as v2

def icoon(N, variant):
    W = int(N * 1.75)              # Gloop = 0.34 W, dus ±0.6 N breed: ruimte voor de toren
    sl, _ = k.slok_sprite(W)
    rust = k.v2.schaal(k.v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-rust-h0.png")).convert("RGBA")), W * k.GLOOP_B)
    hap_h = k.v2.schaal(k.v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-hap-h0.png")).convert("RGBA")), W * k.GLOOP_B).height
    H = v2.hoeden()
    im = Image.new("RGBA", (N, N), (226, 140, 70, 255))
    # warme grot met lichtbundel schuin van linksboven (zelfde als het spel)
    lam = Image.new("L", (N, N), 0); d = ImageDraw.Draw(lam)
    d.line([(N * -0.1, N * -0.1), (N * 0.45, N * 0.8)], fill=255, width=int(N * 0.28))
    lam = lam.filter(ImageFilter.GaussianBlur(N * 0.03))
    im = Image.composite(Image.new("RGBA", (N, N), (246, 190, 120, 255)), im, lam)
    ImageDraw.Draw(im).ellipse([-0.2 * N, 0.86 * N, 1.2 * N, 1.4 * N], fill=(110, 46, 26, 255))
    cx, voet = N * 0.44, N * 0.96
    gx = int(cx - rust.width / 2)
    if variant == "slok":
        im.alpha_composite(sl, (gx, int(voet - hap_h)))
    else:
        im.alpha_composite(rust, (gx, int(voet - rust.height)))
    # toren: helm, kroon, puntmuts, koksmuts, emmer ... tot boven de rand
    rij = [0, 4, 1, 5, 9, 7, 2] if variant == "slok" else [4, 1, 5, 9, 7, 2, 6]
    y = voet - rust.height + rust.height * k.KRUIN
    x = gx + rust.width * 0.53
    rnd = random.Random(3)
    for i in rij:
        h = k.los_weg(k.v2.schaal(H[i], W * 0.16)).rotate(rnd.uniform(-9, 9), expand=True, resample=Image.BICUBIC)
        top = y - h.height * 0.78
        im.alpha_composite(h, (int(x - h.width / 2), int(top)))
        y = top + h.height * 0.22
        x += 0.035 * rust.width   # toren helt steeds verder naar rechts: hij gaat zo om
    return im

os.makedirs(UIT, exist_ok=True)
for var in ("slok", "rust"):
    big = icoon(1000, var)
    big.resize((500, 500), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"icoon-500-{var}.png"))
    # launcher: strakker (Gloop groter, onderste hoeden): op 40 px moet het oog het herkenbare zijn
    strak = big.crop((40, 200, 840, 1000))
    for n in (40, 60, 80):
        strak.resize((n, n), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"launcher-{n}-{var}.png"))
import shutil; shutil.rmtree(os.path.join(UIT, "_kit"), ignore_errors=True)
print("klaar")
