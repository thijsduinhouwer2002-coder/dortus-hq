"""Proef: de vier begraven stukken gedempt in de dichte aarde (Mila, 16 nov 2026).
Dempen: kleur 45 procent minder verzadigd en richting de aardekleur, een donker holletje eromheen (het gat waarin
het ligt), en kruimels aarde over de bovenrand, zodat ze in de grond zitten en niet erop plakken.
Uit: proef-4x.png (bladpixels) en proef-1x.png (spelpixels, ware grootte), en proef-1x-strook-3x.png om te kijken.
Gebruik: python3 leg_in_aarde.py <hol_proef.png> <stukken-4x.png>
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
hol, stuk = Image.open(sys.argv[1]).convert('RGBA'), Image.open(sys.argv[2]).convert('RGBA')
tegel = hol.crop((76, 14, 140, 70))                     # dichte aarde uit het echte 3D-stuk, zonder bovenrand
B, H = 64 * 30, 64 * 3                                  # 30 cellen breed, 3 rijen
veld = Image.new('RGBA', (B, H))
for x in range(0, B, tegel.width):
    for y in range(0, H, tegel.height): veld.paste(tegel, (x, y))
aarde = np.asarray(tegel, dtype=np.float32)[..., :3].reshape(-1, 3).mean(0)
rng = np.random.default_rng(7)

def demp(vak):
    a = np.asarray(vak, dtype=np.float32) / 255
    rgb, al = a[..., :3], a[..., 3:]
    grijs = rgb.mean(-1, keepdims=True)
    rgb = rgb * 0.65 + grijs * 0.35                     # minder verzadigd
    rgb = rgb * 0.72 + (aarde / 255) * 0.28             # richting de aarde
    rgb *= 0.88
    # kruimels: de bovenste rand van het stuk wordt hier en daar aarde
    ys = np.argmax(al[..., 0] > 0.5, axis=0)
    ruis = rng.random(al.shape[:2])
    yy = np.arange(al.shape[0])[:, None]
    kruim = (yy < ys[None, :] + 3) & (ruis < 0.4) & (al[..., 0] > 0.5)
    rgb[kruim] = rgb[kruim] * 0.25 + (aarde / 255) * 0.85
    return Image.fromarray((np.dstack([np.clip(rgb, 0, 1), al]) * 255).astype(np.uint8))

def holletje(vak):
    al = vak.split()[3].filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(3))
    zwart = Image.new('RGBA', vak.size, (40, 18, 16, 0)); zwart.putalpha(al.point(lambda v: int(v * 0.55)))
    return zwart

PLEK = [(3, 1, 0), (11, 2, 1), (18, 1, 2), (26, 0, 3)]   # (cel, rij, welk stuk): ver uit elkaar
for cel, rij, i in PLEK:
    vak = stuk.crop((i * 64, 0, i * 64 + 64, 64))
    veld.alpha_composite(holletje(vak), (cel * 64, rij * 64))
    veld.alpha_composite(demp(vak), (cel * 64, rij * 64))
veld.save('proef-4x.png')
klein = veld.resize((B // 4, H // 4), Image.LANCZOS); klein.save('proef-1x.png')
klein.resize((B // 4 * 3, H // 4 * 3), Image.NEAREST).save('proef-1x-strook-3x.png')
# naast elkaar: elk stuk op 4x, en dezelfde op 1x vergroot
rij = Image.new('RGBA', (4 * 136, 136), (30, 30, 30, 255))
for k, (cel, r, i) in enumerate(PLEK):
    y0 = min(max(0, r * 64 - 16), H - 96); rij.paste(veld.crop((cel * 64 - 16, y0, cel * 64 + 80, y0 + 96)).resize((128, 128)), (k * 136 + 4, 4))
rij.save('proef-stukken-4x.png'); print('klaar')
