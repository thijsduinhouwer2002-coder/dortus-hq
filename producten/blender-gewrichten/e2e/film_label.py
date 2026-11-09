"""Vervangt de Blender-stempel 'Exploded view' door een nette Inter-label.
Gebruik: python3 label.py <map met frames> <eerste> <laatste> <schone frame>"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
d, a, b, schoon = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
BOX = (0, 0, 360, 64)
src = Image.open(f"{d}/{schoon:04d}.png").convert("RGB").crop(BOX)
font = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Medium.otf", 30)
n = b - a + 1
for k, i in enumerate(range(a, b + 1)):
    im = Image.open(f"{d}/{i:04d}.png").convert("RGB")
    im.paste(src, BOX[:2])
    # zacht in en uit (4 beelden)
    al = min(1.0, (k + 1) / 4, (n - k) / 4)
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    g = ImageDraw.Draw(lay)
    x, y = 96, 72
    tekst = "Exploded view"
    w = g.textlength(tekst, font=font)
    g.rounded_rectangle((x - 18, y - 12, x + 26 + w + 18, y + 46), radius=29,
                        fill=(20, 22, 28, int(200 * al)), outline=(255, 255, 255, int(28 * al)), width=1)
    g.ellipse((x - 2, y + 11, x + 12, y + 25), fill=(62, 207, 142, int(255 * al)))
    g.text((x + 26, y - 2), tekst, font=font, fill=(236, 238, 241, int(255 * al)))
    im = Image.alpha_composite(im.convert("RGBA"), lay).convert("RGB")
    im.save(f"{d}/{i:04d}.png")
print("klaar", n, "beelden")
