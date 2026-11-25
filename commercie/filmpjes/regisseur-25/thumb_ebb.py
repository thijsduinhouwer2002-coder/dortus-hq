# Regisseur 26 nov 2026: nieuw eerste beeld voor het Ebb-filmpje (issue #71).
# Rechters in ronde 1 en 2: "childish", "unclear if it's a Garmin watch app", "show it running on a watch".
# Dus: het echte simulatorbeeld met het horloge erom (Garmin fenix 8 47 mm uit de Connect IQ-simulator),
# groot op een rustige donkere achtergrond, weinig tekst, het dier hooguit klein.
# Gebruik: python3 thumb_ebb.py <map met schermen *.png> <uitmap>
import sys, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

W, H = 1080, 1920
F_ZWAAR = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
F_BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
F_MED = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"


def horloge(pad):
    im = Image.open(pad).convert("RGB").crop((0, 30, 713, 940))
    a = np.asarray(im).astype(int)
    wit = (a.min(axis=2) >= 238)
    # alleen het wit dat aan de rand vastzit is achtergrond (vulling vanaf de randen)
    from collections import deque
    h, w = wit.shape
    bg = np.zeros_like(wit)
    q = deque([(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)] + [(0, x) for x in range(0, w, 7)] + [(h - 1, x) for x in range(0, w, 7)])
    while q:
        y, x = q.popleft()
        if 0 <= y < h and 0 <= x < w and wit[y, x] and not bg[y, x]:
            bg[y, x] = True
            q.extend(((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)))
    m = Image.fromarray(((~bg) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1))
    im.putalpha(m)
    return im.crop(im.getbbox())


def achtergrond():
    y = np.linspace(0, 1, H)[:, None, None]
    top, bodem = np.array([8, 30, 58]), np.array([2, 8, 20])
    a = top * (1 - y) + bodem * y
    a = np.repeat(a, W, axis=1)
    # zachte blauwe gloed achter het horloge
    yy, xx = np.mgrid[0:H, 0:W]
    g = np.exp(-(((xx - W / 2) / 520) ** 2 + ((yy - 1010) / 560) ** 2))
    a = a + g[..., None] * np.array([0, 70, 120])
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def midden(d, y, tekst, font, kleur):
    b = d.textbbox((0, 0), tekst, font=font)
    d.text(((W - (b[2] - b[0])) / 2 - b[0], y), tekst, font=font, fill=kleur)


def maak(scherm, kop, onder, uit):
    bg = achtergrond().convert("RGBA")
    hor = horloge(scherm)
    s = 1000 / hor.width
    hor = hor.resize((int(hor.width * s), int(hor.height * s)), Image.LANCZOS)
    schaduw = Image.new("RGBA", bg.size, (0, 0, 0, 0))
    sm = Image.new("L", bg.size, 0)
    hx, hy = (W - hor.width) // 2, 1010 - hor.height // 2
    sm.paste(hor.split()[3], (hx + 10, hy + 30))
    sm = sm.filter(ImageFilter.GaussianBlur(30)).point(lambda v: v * 0.7)
    schaduw.putalpha(sm)
    bg = Image.alpha_composite(bg, schaduw)
    bg.alpha_composite(hor, (hx, hy))
    d = ImageDraw.Draw(bg)
    y = 120
    for r in kop:
        midden(d, y, r, ImageFont.truetype(F_ZWAAR, 96), (255, 255, 255))
        y += 112
    y = 1600
    for r, kl in onder:
        midden(d, y, r, ImageFont.truetype(F_BOLD, 60), kl)
        y += 78
    bg.convert("RGB").save(uit, quality=92)


if __name__ == "__main__":
    bron, uit = sys.argv[1], sys.argv[2]
    os.makedirs(uit, exist_ok=True)
    blauw = (120, 220, 255)
    maak(os.path.join(bron, "ademen-in.png"), ["Breathe with", "your eyes closed?"],
         [("Follow the buzz on your Garmin", (255, 255, 255)), ("Ebb on Connect IQ", blauw)],
         os.path.join(uit, "ebb-eerste-beeld-ogen-dicht.jpg"))
    maak(os.path.join(bron, "inhouden-2-30.png"), ["How long can", "you hold?"],
         [("Breath hold training on Garmin", (255, 255, 255)), ("Ebb on Connect IQ", blauw)],
         os.path.join(uit, "ebb-eerste-beeld-hold.jpg"))
