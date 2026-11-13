"""Capsule-proef 2 (Daan, 13 nov 2026): close-up 6 (breed) + 3D-titel + strookje boven een taakbalk.
Draai: python3 maak_capsule_proef.py  (leest winkel-closeup-proef5.png, titel-3d-v1.png, ../hol-3d/ronde4-ware-grootte.png)
"""
from PIL import Image, ImageDraw, ImageFilter
W, H = 1232, 706
BAND = 168                      # onderste band: bureaublad met het echte strookje en een taakbalk
TB = 40                         # hoogte taakbalk
scene = Image.open("winkel-closeup-proef6-breed.png").convert("RGBA")   # al op 1232 x 538 gerenderd
doek = Image.new("RGBA", (W, H), (0, 0, 0, 255))
doek.alpha_composite(scene, (0, 0))

# titel linksboven op de lege wand
t = Image.open("titel-3d-v1.png").convert("RGBA")
t = t.crop(t.split()[3].getbbox())
tw = 330; t = t.resize((tw, int(t.height * tw / t.width)), Image.LANCZOS)
schaduw = Image.new("RGBA", t.size, (0, 0, 0, 0)); schaduw.putalpha(t.split()[3].point(lambda a: int(a * 0.55)))
schaduw = schaduw.filter(ImageFilter.GaussianBlur(10))
doek.alpha_composite(schaduw, (26, 18)); doek.alpha_composite(t, (18, 8))

# onderste band: bureaublad (zachte gradient), strookje op ware grootte boven een neutrale taakbalk
band = Image.new("RGBA", (W, BAND), (0, 0, 0, 255))
d = ImageDraw.Draw(band)
for y in range(BAND):
    f = y / BAND
    d.line([(0, y), (W, y)], fill=(int(28 + 20 * f), int(40 + 22 * f), int(70 + 28 * f), 255))
strook = Image.open("../hol-3d/ronde4-ware-grootte.png").convert("RGBA")
sx = W - strook.width - 24
band.alpha_composite(strook, (sx, BAND - TB - strook.height))
d.rectangle([0, BAND - TB, W, BAND], fill=(22, 22, 30, 255))
d.line([(0, BAND - TB), (W, BAND - TB)], fill=(60, 60, 75, 255))
# generieke pictogrammen (geen merk), midden
for i in range(6):
    x = W // 2 - 3 * 34 + i * 34
    d.rounded_rectangle([x, BAND - TB + 8, x + 24, BAND - 8], 6, fill=[(90, 140, 220), (240, 190, 70), (110, 200, 140), (200, 110, 120), (150, 150, 170), (120, 120, 200)][i] + (255,))
d.text((W - 70, BAND - TB + 13), "09:41", fill=(200, 200, 210, 255))
# zachte overgang tussen scène en band
over = Image.new("RGBA", (W, 26), (0, 0, 0, 0)); od = ImageDraw.Draw(over)
for y in range(26):
    od.line([(0, y), (W, y)], fill=(28, 40, 70, int(255 * y / 26)))
doek.alpha_composite(over, (0, H - BAND - 26))
doek.alpha_composite(band, (0, H - BAND))
doek.convert("RGB").save("capsule-main-proef2.png")
doek.convert("RGB").resize((462, int(462 * H / W)), Image.LANCZOS).save("capsule-main-proef2-klein.png")
print("klaar")
