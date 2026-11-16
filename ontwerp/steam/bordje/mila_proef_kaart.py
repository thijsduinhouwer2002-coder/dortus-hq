"""Proef wachtkaartje op de echte strook (Mila 16 nov), precies zoals het spel het zou tekenen uit de twee bladen.
Bordje: cel 'leeg' + cijfers zoals in mila_proef.py. Kaartje: cel 'kaart1' (plus en één cijfer) of 'kaart2' (twee
cijfers), met hetzelfde anker_x en nul_y als het bordje: kaartcel links = bordcel links + (anker_bord - anker_kaart) / px
spelpixels, boven = bordcel boven + (nul_y_bord - nul_y_kaart) spelpixels. Cijfer k0..k9 op dezelfde plek als de
kaartcel; bij twee cijfers de eenheden 4 spelpixels naar rechts.
    python3 mila_proef_kaart.py <map met holbord.png, holkaart.png, sprites.json> <strook-120.png> <uit-stam>"""
import sys, json, os
from PIL import Image, ImageDraw
map_, strook = sys.argv[1], Image.open(sys.argv[2]).convert("RGBA")
info = json.load(open(os.path.join(map_, "sprites.json")))
B, Kt = info["holbord"], info["holkaart"]
K = 3   # schermpixels per spelpixel op strook 120
def cellen(sp, naam):
    blad = Image.open(os.path.join(map_, naam + ".png")).convert("RGBA"); cw, ch = sp["cel_px"]; px = sp["px"]
    return {f: blad.crop((i * cw, 0, (i + 1) * cw, ch)).resize((cw * K // px, ch * K // px), Image.LANCZOS)
            for i, f in enumerate(sp["frames"])}
cb, ck = cellen(B, "holbord"), cellen(Kt, "holkaart")
TOP, X0 = 600, 4 * K
Y0 = TOP - round(B["top"][0] * K)        # bovenkant plank op de vensterrand
dx = (B["anker_x"] - Kt["anker_x"]) / B["px"]; dy = B["nul_y"][0] - Kt["nul_y"][0]
def beeld(niv, deel, wacht):
    s = strook.copy()
    s.alpha_composite(cb["leeg"], (X0, Y0))
    t = str(niv)
    for ch, o in zip(t, [0] if len(t) == 1 else [-2.5, 2.5]):
        s.alpha_composite(cb["c" + ch], (X0 + round(o * K), Y0))
    d = ImageDraw.Draw(s); mid = X0 + B["cel_px"][0] * K / B["px"] / 2; by = Y0 + 11 * K
    x0, x1 = round(mid - 5.5 * K), round(mid + 5.5 * K)
    d.rectangle((x0, by, x1 - 1, by + K - 1), fill=(78, 40, 28)); n = round((x1 - x0) * deel)
    if n: d.rectangle((x0, by, x0 + n - 1, by + K - 1), fill=(255, 224, 122))
    if wacht:
        kx, ky = X0 + round(dx * K), Y0 + round(dy * K); w = str(wacht)
        s.alpha_composite(ck["kaart1" if len(w) == 1 else "kaart2"], (kx, ky))
        for i, ch in enumerate(w):
            s.alpha_composite(ck["k" + ch], (kx + 4 * K * i, ky))
    return s.crop((0, TOP, 360, TOP + 120))
outs = [beeld(12, 1.0, 7), beeld(16, 1.0, 10), beeld(6, 1.0, 1), beeld(9, 0.4, 0)]
ware = Image.new("RGB", (360 * len(outs) + 10 * (len(outs) - 1), 120), (60, 60, 60))
for i, o in enumerate(outs): ware.paste(o, (i * 370, 0))
ware.save(sys.argv[3] + "-1x.png")
z = Image.new("RGB", (3 * 130 * 4 + 20, 120 * 4), (60, 60, 60))
for i, o in enumerate(outs[:3]): z.paste(o.crop((0, 0, 130, 120)).resize((520, 480), Image.NEAREST), (i * 530, 0))
z.save(sys.argv[3] + "-4x.png")
