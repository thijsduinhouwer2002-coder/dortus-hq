# Mila 10 nov: hoe een bladzijde van het Heldenboek in het paneel staat, op ware grootte (schaal 3, strook 120 px).
# Alleen een voorbeeld voor Olaf (kern/tekst.gd tekent het echt); letters hier DejaVu, in het spel de letter van het paneel.
import os
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
D = os.path.join(R, "ontwerp", "steam", "mila")
S = 3
def k(n): return Image.open(os.path.join(K, n)).convert("RGBA")
paneel, boek, lijf, soort, hoeden, wapens = k("paneel.png"), k("boek.png"), k("held_lijf_kleuren.png"), k("held_soort.png"), k("held_hoeden.png"), k("held_wapens.png")

def negen(w, h):   # 9-slice rand 4, in spelpixels
    o = Image.new("RGBA", (w, h))
    for (sx, sw, dx, dw) in [(0, 4, 0, 4), (4, 4, 4, w - 8), (8, 4, w - 4, 4)]:
        for (sy, sh, dy, dh) in [(0, 4, 0, 4), (4, 4, 4, h - 8), (8, 4, h - 4, 4)]:
            o.alpha_composite(paneel.crop((sx, sy, sx + sw, sy + sh)).resize((dw, dh), Image.NEAREST), (dx, dy))
    return o

def blad(soort_i, kleur, hoed, wapen, naam, regel, stempels, nr):
    W, Hh = 96, 32
    p = negen(W, Hh)
    held = lijf.crop((0, kleur * 16, 16, kleur * 16 + 16))
    if soort_i >= 0: held.alpha_composite(soort.crop((0, soort_i * 16, 16, soort_i * 16 + 16)))
    held.alpha_composite(hoeden.crop((hoed * 16, 0, hoed * 16 + 16, 16)))
    if wapen >= 0: held.alpha_composite(wapens.crop((wapen * 16, 0, wapen * 16 + 16, 16)))
    p.alpha_composite(held, (5, 11))
    for i, st in enumerate(stempels):
        f = st if st else 2
        p.alpha_composite(boek.crop((f * 8, 0, f * 8 + 8, 8)), (24 + i * 10, 20))
    p.alpha_composite(boek.crop((64, 0, 72, 8)), (W - 21, 20))
    p.alpha_composite(boek.crop((72, 0, 80, 8)), (W - 11, 20))
    p.alpha_composite(boek.crop((8, 0, 16, 8)), (W - 11, 3))
    g = p.resize((W * S, Hh * S), Image.NEAREST)
    d = ImageDraw.Draw(g)
    f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
    f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    d.text((24 * S, 4 * S), naam, font=f1, fill=(243, 226, 192))
    d.text((24 * S, 11 * S), regel, font=f2, fill=(240, 180, 60))
    d.text(((W - 30) * S, 21 * S), nr, font=f2, fill=(200, 178, 150))
    return g

a = blad(0, 2, 0, 0, "The Knight", "Weak to: Spike Pit", [0, 4, 0], "2/5")
b = blad(2, 0, 1, 1, "The Wizard", "First: Mira. Gloop got her.", [3, 0, 5], "4/5")
c = blad(-1, 3, 4, -1, "Crown", "First worn by Kees.", [6, 0, 0], "5/10")
uit = Image.new("RGBA", (a.width + 24, a.height * 3 + 48), (0x1d, 0x14, 0x26, 255))
for i, x in enumerate([a, b, c]):
    uit.alpha_composite(x, (12, 12 + i * (a.height + 12)))
uit.save(os.path.join(D, "boek-bladzijde-3x.png"))
