"""Zet de Blender-render (render_hoofdbeeld.py) op een oranje vlak met naam en één belofte, 1200 x 600.
Ook een proefblad op 600 x 300. Letter: Inter Display (OFL), uit het systeem.
    python3 maak_hoofdbeeld.py <fig.png> <uitmap>
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

fig_pad, uitmap = sys.argv[1], sys.argv[2]
W, H = 1200, 600
F = "/usr/share/fonts/opentype/inter/"
ORANJE_BOVEN, ORANJE_ONDER = (255, 122, 36), (240, 84, 16)
INKT = (20, 20, 26)

# Achtergrond: oranje met een zachte verloop van boven naar onder
bg = Image.new("RGB", (W, H))
d = ImageDraw.Draw(bg)
for y in range(H):
    t = y / (H - 1)
    d.line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(ORANJE_BOVEN, ORANJE_ONDER)))
# Licht vlak achter de figuur, zodat hij loskomt
gloed = Image.new("L", (W, H), 0)
ImageDraw.Draw(gloed).ellipse([760, 40, 1180, 640], fill=90)
gloed = gloed.filter(ImageFilter.GaussianBlur(70))
bg = Image.composite(Image.new("RGB", (W, H), (255, 170, 90)), bg, gloed)

# Figuur: doorzichtige randen eraf, schalen op 600 hoog (voeten net boven de rand)
fig = Image.open(fig_pad).convert("RGBA")
fig = fig.crop(fig.getbbox())
schaal = 585 / fig.height
fig = fig.resize((round(fig.width * schaal), round(fig.height * schaal)), Image.LANCZOS)
x = 975 - fig.width // 2
bg = bg.convert("RGBA")
bg.alpha_composite(fig, (x, H - fig.height - 8))

d = ImageDraw.Draw(bg)
links = 64
f_naam = ImageFont.truetype(F + "InterDisplay-Black.otf", 104)
f_pro = ImageFont.truetype(F + "InterDisplay-Black.otf", 104)
f_belofte = ImageFont.truetype(F + "InterDisplay-Bold.otf", 46)
f_klein = ImageFont.truetype(F + "InterDisplay-SemiBold.otf", 28)

d.text((links, 92), "Click Joints", font=f_naam, fill=INKT)
# "PRO" als wit blok, zodat het in de kleine weergave ook leesbaar is
y_pro = 206
pro_b = d.textbbox((0, 0), "Pro", font=f_pro)
bw, bh = pro_b[2] - pro_b[0], pro_b[3] - pro_b[1]
d.rounded_rectangle([links, y_pro, links + bw + 44, y_pro + bh + 40], radius=18, fill=INKT)
d.text((links + 22 - pro_b[0], y_pro + 20 - pro_b[1]), "Pro", font=f_pro, fill=(255, 255, 255))

d.text((links, 380), "Turn your rig into a", font=f_belofte, fill=(255, 255, 255))
d.text((links, 434), "poseable 3D print", font=f_belofte, fill=(255, 255, 255))
d.text((links, 522), "Add-on for Blender", font=f_klein, fill=INKT)

os.makedirs(uitmap, exist_ok=True)
groot = bg.convert("RGB")
groot.save(os.path.join(uitmap, "0-hoofdbeeld-pro.png"), optimize=True)
groot.resize((600, 300), Image.LANCZOS).save(os.path.join(uitmap, "0-hoofdbeeld-pro-600.png"), optimize=True)
print("klaar", groot.size)
