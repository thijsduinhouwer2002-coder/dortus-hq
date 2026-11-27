"""Opmaak van het Printables-hoofdbeeld (issue #297): render + ronde inzet van één kniegewricht + één regel tekst.

    python3 opmaak.py <beeld.png> <inzet.png> <beeld.json> <uit.jpg> <fontmap>

fontmap: Bricolage-800.ttf en Inter-700.ttf (OFL, uit @fontsource). Omgeving: OP_TEKST, OP_GEWRICHT (naam in de json),
OP_X, OP_Y, OP_R (midden en straal van de inzet in px op 2000x1500).
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BEELD, INZET, META, UIT, FONTS = sys.argv[1:6]
E = os.environ.get
W, H = 2000, 1500
DONKER = (38, 30, 52)

beeld = Image.open(BEELD).convert("RGB").resize((W, H), Image.LANCZOS)
meta = json.load(open(META))
X, Y, R = int(E("OP_X", "1440")), int(E("OP_Y", "800")), int(E("OP_R", "400"))
g = E("OP_GEWRICHT", "rechterknie")
px, py = meta["pix"][g]
px, py = px + int(E("OP_DX", "0")), py + int(E("OP_DY", "0"))

# lijntje van het gewricht naar de rand van de inzet
d = ImageDraw.Draw(beeld)
import math
hoek = math.atan2(py - Y, px - X)
rx, ry = X + R * math.cos(hoek), Y + R * math.sin(hoek)
d.line([(px, py), (rx, ry)], fill=DONKER, width=5)
d.ellipse([px - 26, py - 26, px + 26, py + 26], outline=DONKER, width=5)

# zachte schaduw onder de inzet
sch = Image.new("L", (W, H), 0)
ImageDraw.Draw(sch).ellipse([X - R + 10, Y - R + 24, X + R + 10, Y + R + 24], fill=90)
sch = sch.filter(ImageFilter.GaussianBlur(28))
beeld = Image.composite(Image.new("RGB", (W, H), (90, 80, 100)), beeld, sch)

# de inzet zelf (uitsnede uit het midden van de inzetrender)
iz = Image.open(INZET).convert("RGB")
s = float(E("OP_SNEDE", "1.0"))
w = int(iz.width * s)
cx, cy = [float(v) for v in E("OP_SNEDE_MIDDEN", "0.5,0.5").split(",")]
l, t = int(iz.width * cx - w / 2), int(iz.height * cy - w / 2)
iz = iz.crop((l, t, l + w, t + w)).resize((2 * R, 2 * R), Image.LANCZOS)
masker = Image.new("L", (2 * R * 4, 2 * R * 4), 0)
ImageDraw.Draw(masker).ellipse([0, 0, 2 * R * 4 - 1, 2 * R * 4 - 1], fill=255)
masker = masker.resize((2 * R, 2 * R), Image.LANCZOS)
beeld.paste(iz, (X - R, Y - R), masker)
ring = Image.new("RGBA", (2 * R * 4 + 80, 2 * R * 4 + 80), (0, 0, 0, 0))
ImageDraw.Draw(ring).ellipse([20, 20, 2 * R * 4 + 59, 2 * R * 4 + 59], outline=(*DONKER, 255), width=24)
ring = ring.resize((2 * R + 20, 2 * R + 20), Image.LANCZOS)
beeld.paste(ring, (X - R - 10, Y - R - 10), ring)

# één regel tekst
d = ImageDraw.Draw(beeld)
f = ImageFont.truetype(os.path.join(FONTS, "Bricolage-800.ttf"), int(E("OP_MAAT", "74")))
tekst = E("OP_TEKST", "Ball joints in your own figure")
tb = d.textbbox((0, 0), tekst, font=f)
tx = int(E("OP_TX", str(X - (tb[2] - tb[0]) // 2)))
ty = int(E("OP_TY", "150"))
d.text((tx, ty), tekst, font=f, fill=DONKER)
if E("OP_ONDER"):
    f2 = ImageFont.truetype(os.path.join(FONTS, "Inter-700.ttf"), int(E("OP_MAAT2", "40")))
    tb2 = d.textbbox((0, 0), E("OP_ONDER"), font=f2)
    d.text((X - (tb2[2] - tb2[0]) // 2, ty + (tb[3] - tb[1]) + 26), E("OP_ONDER"), font=f2, fill=(96, 84, 112))
beeld.save(UIT, quality=92)
print("klaar", UIT)
