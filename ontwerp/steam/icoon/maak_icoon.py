"""App-icoon van Het Hol (Daan, 14 nov 2026).

Bron: gloop-kroon-1024-render.png, gemaakt met
  GLOOP_ICOON=1 <venv>/bin/python producten/steam-hol/modellen/gloop.py <uit.png> 1 2 1024 1024 48
(Gloop versie 1 met alleen de kroon). Dit script snijdt hem strak bij en legt hem op een tegel.

Draai: python3 maak_icoon.py   (schrijft in deze map)
  icoon-tegel-256.png, icoon-vrij-256.png, hol.ico (16 tot 256, tegel), proef-taakbalk.png
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

HIER = os.path.dirname(os.path.abspath(__file__))
PRUIM_L, PRUIM, PRUIM_D, GOUD = (0x6a, 0x45, 0x75), (0x3a, 0x24, 0x40), (0x24, 0x16, 0x2b), (0xf2, 0xb6, 0x32)


def gloop_strak():
    im = Image.open(os.path.join(HIER, "gloop-kroon-1024-render.png")).convert("RGBA")
    a = im.getchannel("A")
    # schaduw van de vloer weg: alleen wat bijna dicht is hoort bij Gloop
    harde = a.point(lambda v: 255 if v > 200 else 0)
    bbox = harde.getbbox()
    a2 = a.point(lambda v: 0 if v < 140 else v)
    im.putalpha(a2)
    return im.crop(bbox)


def tegel(n=1024):
    t = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    # verloop van pruim licht (boven) naar pruim donker (onder) met warme gloed achter Gloop
    bg = Image.new("RGB", (n, n))
    px = bg.load()
    for y in range(n):
        for x in range(n):
            dx, dy = (x - n * 0.5) / n, (y - n * 0.62) / n
            d = min(1.0, (dx * dx + dy * dy) ** 0.5 * 1.7)
            f = y / n
            base = [PRUIM_L[i] * (1 - f) + PRUIM_D[i] * f for i in range(3)]
            gl = max(0.0, 1 - d) ** 2 * 0.55
            px[x, y] = tuple(int(base[i] * (1 - gl) + GOUD[i] * gl * 0.75 + base[i] * gl * 0.25) for i in range(3))
    masker = Image.new("L", (n, n), 0)
    ImageDraw.Draw(masker).rounded_rectangle((0, 0, n - 1, n - 1), radius=int(n * 0.22), fill=255)
    t.paste(bg, (0, 0), masker)
    return t, masker


def leg_op(t, g, breedte, onder):
    n = t.size[0]
    w = int(n * breedte); h = int(g.size[1] * w / g.size[0])
    gg = g.resize((w, h), Image.LANCZOS)
    x = (n - w) // 2; y = int(n * onder) - h
    # zachte schaduw onder Gloop
    sch = Image.new("RGBA", t.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse((x + w * 0.1, y + h * 0.9, x + w * 0.9, y + h * 1.04), fill=(20, 8, 24, 150))
    t.alpha_composite(sch.filter(ImageFilter.GaussianBlur(n * 0.02)))
    t.alpha_composite(gg, (x, y))
    return t


def klein(im, s):
    k = im.resize((s, s), Image.LANCZOS)
    if s <= 32:
        k = ImageEnhance.Sharpness(k).enhance(1.6)
    return k


g = gloop_strak()
t, masker = tegel()
t = leg_op(t, g, 0.86, 0.93)
# knip alles wat buiten de tegel valt (kroon mag niet over de rand)
a = Image.composite(t.getchannel("A"), Image.new("L", t.size, 0), masker); t.putalpha(a)
# klein (16 en 24 px, moet van de frisse kijker): Gloop groter in de tegel, groen voller
tk, mk = tegel()
tk = leg_op(tk, ImageEnhance.Color(g).enhance(1.3), 1.0, 1.04)
tk.putalpha(Image.composite(tk.getchannel("A"), Image.new("L", tk.size, 0), mk))
vrij = leg_op(Image.new("RGBA", (1024, 1024), (0, 0, 0, 0)), g, 0.96, 0.99)

klein(t, 256).save(os.path.join(HIER, "icoon-tegel-256.png"))
klein(vrij, 256).save(os.path.join(HIER, "icoon-vrij-256.png"))
klein(t, 512).save(os.path.join(HIER, "icoon-tegel-512.png"))
maten = [16, 24, 32, 48, 64, 128, 256]
# ico: 16 en 24 uit de kleine tegel, de rest uit de gewone
beelden = {s: klein(tk if s <= 24 else t, s) for s in maten}
beelden[256].save(os.path.join(HIER, "hol.ico"), sizes=[(s, s) for s in maten],
                  append_images=[beelden[s] for s in maten if s != 256])
klein(tk, 256).save(os.path.join(HIER, "icoon-klein-bron-256.png"))
klein(t, 184).convert("RGB").save(os.path.join(HIER, "steam-community-184.jpg"), quality=95)

# proef: op ware grootte in een lichte en een donkere taakbalk, naast het Godot-icoon dat er nu staat
proef = Image.new("RGB", (560, 260), (255, 255, 255))
d = ImageDraw.Draw(proef)
for rij, (kleur, tekst) in enumerate([((243, 243, 243), "licht"), ((32, 32, 32), "donker")]):
    y0 = 20 + rij * 120
    d.rectangle((0, y0, 560, y0 + 96), fill=kleur)
    xx = 16
    for s in (16, 24, 32, 48):
        for bron in ((tk if s <= 24 else t), vrij):
            proef.paste(klein(bron, s), (xx, y0 + (96 - s) // 2), klein(bron, s))
            xx += s + 14
        xx += 18
proef.save(os.path.join(HIER, "proef-taakbalk.png"))
print("klaar")
