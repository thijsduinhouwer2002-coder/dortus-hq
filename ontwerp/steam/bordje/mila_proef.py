"""Proef van het 3D-bordje op de echte strook (Mila 16 nov). Tekent zoals het spel het zou doen: cel 'leeg', dan de
cijfercellen op dezelfde plek (tientallen 2,5 spelpixels links, eenheden 2,5 rechts, één cijfer in het midden),
dan het balkje op rij 11 van de cel (de onderste rij van de lijst), x van -5,5 tot +5,5 rond het midden.
    python3 mila_proef.py <blad holbord.png> <strook-120.png> <uit-stam>"""
import sys
from PIL import Image, ImageDraw
blad = Image.open(sys.argv[1]).convert("RGBA"); strook = Image.open(sys.argv[2]).convert("RGBA")
PX, CEL, K = 4, (15, 18), 3          # bladpixels per spelpixel, cel in spelpixels, schermpixels per spelpixel (120)
cel = lambda i: blad.crop((i * CEL[0] * PX, 0, (i + 1) * CEL[0] * PX, CEL[1] * PX)).resize((CEL[0] * K, CEL[1] * K), Image.LANCZOS)
TOP, X0, Y0 = 600, 4 * K, 600 - 1 * K   # plank links op spelpixel 4, bovenkant plank op de vensterrand
def bord(niv, deel, wip=0):
    s = strook.copy(); y = Y0 - wip * K
    s.alpha_composite(cel(0), (X0, y))
    t = str(niv); offs = [0] if len(t) == 1 else [-2.5, 2.5]
    for ch, o in zip(t, offs):
        s.alpha_composite(cel(1 + int(ch)), (X0 + round(o * K), y))
    d = ImageDraw.Draw(s); mid = X0 + CEL[0] * K / 2; by = y + 11 * K
    x0, x1 = round(mid - 5.5 * K), round(mid + 5.5 * K)
    d.rectangle((x0, by, x1 - 1, by + K - 1), fill=(78, 40, 28)); n = round((x1 - x0) * deel)
    if n: d.rectangle((x0, by, x0 + n - 1, by + K - 1), fill=(255, 224, 122))
    return s.crop((0, TOP, 360, TOP + 120))
outs = [bord(5, 0.4), bord(12, 1.0), bord(47, 0.7), bord(9, 0.15, wip=2)]
W = 360; ware = Image.new("RGB", (W * len(outs) + 10 * (len(outs) - 1), 120), (60, 60, 60))
for k, o in enumerate(outs): ware.paste(o, (k * (W + 10), 0))
ware.save(sys.argv[3] + "-1x.png")
z = Image.new("RGB", (2 * 130 * 4 + 10, 120 * 4), (60, 60, 60))
for k, o in enumerate(outs[:2]): z.paste(o.crop((0, 0, 130, 120)).resize((520, 480), Image.NEAREST), (k * 530, 0))
z.save(sys.argv[3] + "-4x.png")
