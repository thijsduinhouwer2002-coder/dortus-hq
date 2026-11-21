"""Zet de Blender-render (render_hoofdbeeld.py) op een oranje vlak met naam en één belofte, in drie maten:
- 0-hoofdbeeld-pro.png        1200 x 600  (Superhive, uitgelicht beeld)
- 0-hoofdbeeld-pro-1005.png   1005 x 565  (Gumroad, omslag op de productpagina)
- 0-hoofdbeeld-pro-vierkant.png 600 x 600 (Gumroad, zoeken, Discover en profiel)
Plus proefbladen op kleine maat en naast elkaar, om in de rijtjes te keuren.
Letter: Inter Display (OFL), uit het systeem.
    python3 maak_hoofdbeeld.py <fig.png> <uitmap>
"""
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

fig_pad, uitmap = sys.argv[1], sys.argv[2]
F = "/usr/share/fonts/opentype/inter/"
ORANJE_BOVEN, ORANJE_ONDER = (255, 122, 36), (240, 84, 16)
INKT = (20, 20, 26)
WIT = (255, 255, 255)

FIG = Image.open(fig_pad).convert("RGBA")
# Bijsnijden op duidelijke dekking: de schaduwvanger laat ver weg een vage waas achter die anders meetelt.
FIG = FIG.crop(FIG.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox())


def zachte_schaduw(fig):
    """Daan kan 1 (versie 2): de schaduwvloer had harde randen, want de render en het bijsnijden kappen hem af
    als rechthoek. De figuur zelf (dekking > 250, plus 4 px rand voor de zachte kanten) blijft zoals hij is.
    Van de schaduw blijft alleen het deel dicht bij de figuur over (contactschaduw), dat zacht uitloopt, en
    onderaan loopt hij naar nul voor de rand van de render."""
    a = fig.getchannel("A")
    W, H = fig.size
    vast = a.point(lambda v: 255 if v > 250 else 0)
    figuur = vast.filter(ImageFilter.MaxFilter(9))
    dichtbij = vast.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(22))
    onder = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(onder)
    for k in range(60):
        d.line([(0, H - 1 - k), (W, H - 1 - k)], fill=round(255 * (k / 60) ** 1.5))
    # De render heeft ±145 px boven de voeten een schaduwband met een harde bovenrand: laat die van 0 naar vol
    # lopen tussen 150 en 80 px boven de onderkant van de voeten.
    voet = vast.getbbox()[3]
    for y in range(0, voet - 80):
        t = min(max((y - (voet - 150)) / 70, 0), 1)
        d.line([(0, y), (W, y)], fill=round(255 * t * t))
    zacht = ImageChops.multiply(ImageChops.multiply(Image.composite(Image.new("L", (W, H), 0), a, figuur), dichtbij), onder)
    fig.putalpha(ImageChops.lighter(Image.composite(a, Image.new("L", (W, H), 0), figuur), zacht))
    return fig


FIG = zachte_schaduw(FIG)


def vlak(W, H, gloed_box):
    bg = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(ORANJE_BOVEN, ORANJE_ONDER)))
    gloed = Image.new("L", (W, H), 0)
    ImageDraw.Draw(gloed).ellipse(gloed_box, fill=90)
    gloed = gloed.filter(ImageFilter.GaussianBlur(H // 9))
    return Image.composite(Image.new("RGB", (W, H), (255, 170, 90)), bg, gloed).convert("RGBA")


def zet_figuur(bg, hoogte, midden_x, onder):
    """Figuur op hoogte px, voeten `onder` px boven de onderrand (Daan kan 2)."""
    s = hoogte / FIG.height
    f = FIG.resize((round(FIG.width * s), hoogte), Image.LANCZOS)
    bg.alpha_composite(f, (round(midden_x - f.width / 2), bg.height - hoogte - onder))
    return f.width


def pro_blok(d, x, y, grootte):
    f = ImageFont.truetype(F + "InterDisplay-Black.otf", grootte)
    b = d.textbbox((0, 0), "Pro", font=f)
    bw, bh = b[2] - b[0], b[3] - b[1]
    pad_x, pad_y = round(grootte * 0.21), round(grootte * 0.19)
    d.rounded_rectangle([x, y, x + bw + 2 * pad_x, y + bh + 2 * pad_y], radius=round(grootte * 0.17), fill=INKT)
    d.text((x + pad_x - b[0], y + pad_y - b[1]), "Pro", font=f, fill=WIT)


def breed(W, H):
    """Liggend (1200 x 600 en 1005 x 565): tekst links, figuur rechts zo groot als past."""
    s = H / 600
    bg = vlak(W, H, [W - round(470 * s), round(20 * s), W - round(10 * s), H + round(40 * s)])
    breedte = zet_figuur(bg, round(560 * s), W - round(235 * s), round(22 * s))
    d = ImageDraw.Draw(bg)
    x = round(60 * s)
    d.text((x, round(84 * s)), "Click Joints", font=ImageFont.truetype(F + "InterDisplay-Black.otf", round(104 * s)), fill=INKT)
    pro_blok(d, x, round(200 * s), round(104 * s))
    f_b = ImageFont.truetype(F + "InterDisplay-Bold.otf", round(46 * s))
    d.text((x, round(376 * s)), "Turn your rig into a", font=f_b, fill=WIT)
    d.text((x, round(430 * s)), "poseable 3D print", font=f_b, fill=WIT)
    d.text((x, round(518 * s)), "Add-on for Blender", font=ImageFont.truetype(F + "InterDisplay-SemiBold.otf", round(28 * s)), fill=INKT)
    return bg.convert("RGB"), breedte


def vierkant(W=600):
    """Vierkant (600 x 600): naam in drie regels links boven, figuur rechts over bijna de hele hoogte."""
    H = W
    bg = vlak(W, H, [round(W * 0.42), round(H * 0.02), W + round(W * 0.1), H + round(H * 0.08)])
    breedte = zet_figuur(bg, round(H * 0.93), round(W * 0.71), round(H * 0.03))
    d = ImageDraw.Draw(bg)
    x = round(W * 0.06)
    f_n = ImageFont.truetype(F + "InterDisplay-Black.otf", round(W * 0.135))
    d.text((x, round(H * 0.07)), "Click", font=f_n, fill=INKT)
    d.text((x, round(H * 0.215)), "Joints", font=f_n, fill=INKT)
    pro_blok(d, x, round(H * 0.385), round(W * 0.135))
    f_b = ImageFont.truetype(F + "InterDisplay-Bold.otf", round(W * 0.052))
    for i, regel in enumerate(("Turn your rig", "into a poseable", "3D print")):
        d.text((x, round(H * (0.66 + i * 0.068))), regel, font=f_b, fill=WIT)
    return bg.convert("RGB"), breedte


os.makedirs(uitmap, exist_ok=True)
for naam, (beeld, bw) in {
    "0-hoofdbeeld-pro.png": breed(1200, 600),
    "0-hoofdbeeld-pro-1005.png": breed(1005, 565),
    "0-hoofdbeeld-pro-vierkant.png": vierkant(600),
}.items():
    beeld.save(os.path.join(uitmap, naam), optimize=True)
    print(f"{naam}: {beeld.size}, figuur {bw} px breed ({100 * bw / beeld.width:.0f}% van de breedte)")
groot = Image.open(os.path.join(uitmap, "0-hoofdbeeld-pro.png"))
groot.resize((600, 300), Image.LANCZOS).save(os.path.join(uitmap, "0-hoofdbeeld-pro-600.png"), optimize=True)
