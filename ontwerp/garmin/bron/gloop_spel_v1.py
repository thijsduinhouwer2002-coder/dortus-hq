# Gloop op je pols, voorstel v1 (Mila, 16 nov 2026).
# Drie sleutelbeelden van een éénknopsspel ("Hat Tower"): een held valt in het hol, jij drukt,
# Gloop hapt en de hoed vliegt op zijn toren; de toren wordt hoger dan je horloge.
# Alles komt uit de echte modellen van Het Hol (gloop.py, held.py, hoeden.py), gerenderd met bpy.
# Uit: per beeld een AMOLED-versie (454x454, fenix 8 / venu) en een MIP-versie (260x260, FR255,
# 64 kleuren: elk kanaal 0, 85, 170 of 255, zonder dithering), plus een blad op ware grootte.
#   python3 gloop_spel_v1.py <rendermap> <uitmap>
import sys, os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

R, UIT = sys.argv[1], sys.argv[2]
os.makedirs(UIT, exist_ok=True)
FONT = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
SPEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../producten/steam-hol/godot/kunst/3d")
HOEDNAMEN = ["helm", "puntmuts", "kap", "pet", "kroon", "koksmuts", "emmer", "hoge_hoed", "pan", "veermuts"]


def bijsnijden(im):
    return im.crop(im.getbbox())


def hoeden():
    blad = Image.open(os.path.join(R, "hoeden-alle.png")).convert("RGBA")
    w = blad.width // 10
    lijst = [bijsnijden(blad.crop((i * w, 0, (i + 1) * w, blad.height))) for i in range(10)]
    spel = Image.open(os.path.join(SPEL, "hoeden.png")).convert("RGBA")
    lijst[0] = bijsnijden(spel.crop((0, 0, 63, spel.height)))   # helm zilver zoals in het spel
    return lijst


def zonder_schaduw(im):
    # de vloerschaduw van de render leest in de lucht als een stok onder de held: weg ermee
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a < 235 and r + g + b < 200:
                px[x, y] = (0, 0, 0, 0)
    return bijsnijden(im)


def schaal(im, breed):
    return im.resize((max(1, round(breed)), max(1, round(im.height * breed / im.width))), Image.LANCZOS)


def achtergrond(N, schacht=True):
    # aarde van Het Hol: warm donker, lichter naar het midden, een gegraven schacht bovenin
    im = Image.new("RGBA", (N, N), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    for y in range(N):
        t = y / N
        c = (int(46 + 30 * t), int(30 + 16 * t), int(24 + 8 * t))
        d.line([(0, y), (N, y)], fill=c + (255,))
    if schacht:
        sw = int(N * 0.30)
        x0 = N // 2 - sw // 2
        lam = Image.new("L", (N, N), 0)
        ImageDraw.Draw(lam).rounded_rectangle([x0, -20, x0 + sw, int(N * 0.62)], radius=sw // 2, fill=255)
        lam = lam.filter(ImageFilter.GaussianBlur(N * 0.02))
        licht = Image.new("RGBA", (N, N), (125, 88, 40, 255))   # valt op MIP tussen bruin en olijf, niet roze
        im = Image.composite(licht, im, lam)
    # gang onderin waar Gloop zit
    vloer = int(N * 0.86)
    d = ImageDraw.Draw(im)
    d.ellipse([int(-0.1 * N), vloer - int(N * 0.05), int(1.1 * N), vloer + int(N * 0.25)], fill=(38, 24, 19, 255))
    # muntjes rond Gloop (zitten in het spel: schatkamer)
    rnd = random.Random(4)
    for _ in range(9):
        x = rnd.choice([rnd.uniform(0.12, 0.3), rnd.uniform(0.7, 0.88)]) * N
        y = vloer + rnd.uniform(-0.01, 0.03) * N
        r = N * 0.022
        d.ellipse([x - r, y - r * 0.6, x + r, y + r * 0.6], fill=(214, 160, 40, 255), outline=(120, 80, 20, 255))
    return im


def toren(im, gloop, hoedlijst, N, cx, voet_y, gloop_breed, kantelzaad=1, extra=None):
    g = schaal(gloop, gloop_breed)
    gx, gy = int(cx - g.width / 2), int(voet_y - g.height)
    im.alpha_composite(g, (gx, gy))
    rnd = random.Random(kantelzaad)
    y = gy + g.height * 0.30          # kruin van Gloop (lijf staat laag in het beeld)
    x = cx + g.width * 0.03
    stuk = []
    for i, h in enumerate(hoedlijst):
        hb = schaal(h, gloop_breed * rnd.uniform(0.40, 0.48)).rotate(rnd.uniform(-12, 12), expand=True, resample=Image.BICUBIC)
        y_top = y - hb.height * 0.78
        stuk.append((hb, int(x - hb.width / 2), int(y_top)))
        y = y_top + hb.height * 0.22
        x += rnd.uniform(-0.06, 0.06) * gloop_breed
    for hb, hx, hy in stuk:
        im.alpha_composite(hb, (hx, hy))
    return y, x


def tekst(d, xy, s, maat, N, kleur=(255, 255, 255), anker="mm", rand=True):
    f = ImageFont.truetype(FONT, max(8, int(maat * N)))
    if rand:
        d.text(xy, s, font=f, fill=kleur, anchor=anker, stroke_width=max(2, int(N * 0.012)), stroke_fill=(30, 18, 12))
    else:
        d.text(xy, s, font=f, fill=kleur, anchor=anker)


def teller(im, n, N, hoed):
    d = ImageDraw.Draw(im)
    h = schaal(hoed, N * 0.09)
    s = str(n)
    f = ImageFont.truetype(FONT, int(N * 0.11))
    tw = d.textlength(s, font=f)
    x0 = int(N / 2 - (tw + h.width + N * 0.02) / 2)
    im.alpha_composite(h, (x0, int(N * 0.115 - h.height / 2)))
    tekst(d, (x0 + h.width + N * 0.02, N * 0.115), s, 0.11, N, (255, 214, 90), anker="lm")


def rond(im, N):
    m = Image.new("L", (N * 4, N * 4), 0)
    ImageDraw.Draw(m).ellipse([0, 0, N * 4 - 1, N * 4 - 1], fill=255)
    m = m.resize((N, N), Image.LANCZOS)
    out = Image.new("RGBA", (N, N), (0, 0, 0, 255))
    out.paste(im, (0, 0), m)
    return out


def mip(im):
    pal = Image.new("P", (1, 1))
    kl = [(r, g, b) for r in (0, 85, 170, 255) for g in (0, 85, 170, 255) for b in (0, 85, 170, 255)]
    pal.putpalette([c for k in kl for c in k] + [0] * (768 - 192))
    # vaste 4x4-Bayer in plaats van Floyd-Steinberg: rustige vaste patronen, geen kleurruis op de aarde
    bayer = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
    src = im.convert("RGB"); w, h = src.size; px = src.load()
    out = Image.new("RGB", (w, h)); po = out.load()
    for y in range(h):
        for x in range(w):
            t = (bayer[y % 4][x % 4] + 0.5) / 16 - 0.5
            po[x, y] = tuple(max(0, min(255, int(round((v + t * 85) / 85)) * 85)) for v in px[x, y])
    return out


def beeld(nr, N):
    H = hoeden()
    gl = {s: Image.open(os.path.join(R, f"gloop-{s}-h0.png")).convert("RGBA") for s in ("rust", "hap", "blij")}
    gl = {k: bijsnijden(v) for k, v in gl.items()}
    held_v = bijsnijden(Image.open(os.path.join(R, "held-vallen.png")).convert("RGBA"))
    held_s = zonder_schaduw(Image.open(os.path.join(R, "held-schrik.png")).convert("RGBA"))
    im = achtergrond(N)
    d = ImageDraw.Draw(im)
    cx, voet = N / 2, N * 0.90
    gb = N * 0.40
    if nr == 1:   # de held valt: "!" en zijn pan zit nog op zijn hoofd
        toren(im, gl["rust"], [H[4], H[1]], N, cx, voet, gb * 0.92, 1)
        hv = schaal(held_s, N * 0.15).rotate(-12, expand=True, resample=Image.BICUBIC)
        hx, hy = int(cx - hv.width / 2 - N * 0.02), int(N * 0.17)
        im.alpha_composite(hv, (hx, hy))
        tekst(d, (hx + hv.width + N * 0.035, hy + N * 0.08), "!", 0.11, N, (255, 230, 80))
        teller(im, 2, N, H[0])
    elif nr == 2:   # druk: HAP. De held is op, zijn pan vliegt naar de toren
        top_y, top_x = toren(im, gl["hap"], [H[4], H[1]], N, cx, voet, gb * 0.92, 1)
        pan = schaal(H[0], N * 0.16).rotate(-24, expand=True, resample=Image.BICUBIC)
        px, py = int(top_x - pan.width / 2 + N * 0.06), int(top_y - pan.height - N * 0.04)
        for k in range(3):   # drie korte vliegstreepjes
            yy = py + pan.height * (0.35 + 0.2 * k)
            d.line([(px - N * 0.10, yy + N * 0.03), (px - N * 0.02, yy)], fill=(255, 245, 220), width=max(2, int(N * 0.01)))
        im.alpha_composite(pan, (px, py))
        tekst(d, (N * 0.25, N * 0.56), "HAP!", 0.10, N, (255, 255, 255))
        tekst(d, (px + pan.width + N * 0.07, py + pan.height * 0.5), "+1", 0.07, N, (255, 214, 90))
        teller(im, 3, N, H[0])
    else:   # de toren wordt hoger dan je horloge
        rij = [H[i % 10] for i in (0, 4, 1, 8, 6, 2, 7, 5, 3, 9, 0, 6, 4, 8, 1, 7)]
        toren(im, gl["blij"], rij, N, cx, voet, gb * 0.85, 3)
        f = ImageFont.truetype(FONT, int(N * 0.055))
        d.rounded_rectangle([N * 0.08, N * 0.40, N * 0.36, N * 0.58], radius=int(N * 0.03), fill=(255, 244, 220))
        d.text((N * 0.22, N * 0.455), "23 hats", font=f, fill=(60, 30, 20), anchor="mm")
        d.text((N * 0.22, N * 0.525), "too tall!", font=ImageFont.truetype(FONT, int(N * 0.042)), fill=(150, 60, 30), anchor="mm")
    return rond(im, N)


if __name__ == "__main__":
    groot = []
    for nr in (1, 2, 3):
        a = beeld(nr, 454); a.convert("RGB").save(os.path.join(UIT, f"amoled-454-beeld{nr}.png"))
        m = rond(mip(beeld(nr, 260)).convert("RGBA"), 260); m.convert("RGB").save(os.path.join(UIT, f"mip-260-beeld{nr}.png"))
        groot.append((a, m))
    # blad: boven AMOLED 454 op ware pixels, midden MIP 260 vergroot naar 454, onder MIP 260 op 1x
    B = Image.new("RGB", (3 * 474 + 20, 474 + 474 + 300), (24, 20, 26))
    for i, (a, m) in enumerate(groot):
        B.paste(a.convert("RGB"), (20 + i * 474, 20))
        B.paste(m.resize((454, 454), Image.NEAREST).convert("RGB"), (20 + i * 474, 494))
        B.paste(m.convert("RGB"), (20 + i * 474 + 97, 494 + 474 + 10))
    B.save(os.path.join(UIT, "blad-gloop-spel-v1.png"))
    print("klaar", UIT)
