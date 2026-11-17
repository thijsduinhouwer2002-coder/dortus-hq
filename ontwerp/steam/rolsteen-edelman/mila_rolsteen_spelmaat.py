"""Rolsteen op spelmaat in de echte opname (Mila, 17 nov). Strook: schermen/steam-hol-duur/main-koper-1-1920x1080/strook-10min.png
(1920, spel op 3x). Held zonder hoed is daar 31 px, steen 0,9 daarvan = 28 px doorsnee. Renders: rolsteen.py 600x600, schaal 1,7."""
import sys
from PIL import Image
S = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/s/'
strook = Image.open(S + 'strook.png').convert('RGBA')
PX_PER_EENHEID = 600 / 1.7
DOORSNEE = 28
VLOER = 1024


def steen(stand):
    r = Image.open(S + f'p2-{stand}.png').convert('RGBA')
    r = r.crop(r.getbbox())
    f = DOORSNEE / PX_PER_EENHEID
    return r.resize((max(1, round(r.width * f)), max(1, round(r.height * f))), Image.LANCZOS)


def plaats(im, stand, cx, spiegel=False):
    s = steen(stand)
    if spiegel:
        s = s.transpose(Image.FLIP_LEFT_RIGHT)
    im.alpha_composite(s, (int(cx - s.width / 2), VLOER - s.height))
    return s.size


uit = {}
for stand in ('klaar', 'niet_klaar'):
    im = strook.copy()
    print(stand, plaats(im, stand, 1125))
    uit[stand] = im
# kaart: boven 4x uitvergroot, onder ware grootte
X0, Y0, X1, Y1 = 1040, 955, 1220, 1035
w, h = (X1 - X0), (Y1 - Y0)
kaart = Image.new('RGB', (2 * w * 4 + 30, h * 4 + h + 40), (24, 22, 28))
for k, stand in enumerate(('klaar', 'niet_klaar')):
    c = uit[stand].crop((X0, Y0, X1, Y1)).convert('RGB')
    kaart.paste(c.resize((w * 4, h * 4), Image.NEAREST), (10 + k * (w * 4 + 10), 10))
    kaart.paste(c, (10 + k * (w * 4 + 10) + w * 2 - w // 2, h * 4 + 25))
kaart.save(S + 'rolsteen-spelmaat-4x.png')
# heel de gang op ware grootte: niet klaar links tegen de wand (gespiegeld), klaar rechts bij de val
gang = strook.copy()
plaats(gang, 'niet_klaar', 214, spiegel=True)
plaats(gang, 'klaar', 1125)
gang.crop((0, 940, 1440, 1040)).convert('RGB').save(S + 'rolsteen-gang-1x.png')
