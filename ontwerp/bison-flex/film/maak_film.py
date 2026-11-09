# Bison & Flex: filmpje (Daan, 9 nov 2026). Zet de echte IDE-beelden van Jet
# (film-run 42554632237) als kaarten op de achtergrond van de poster, met koppen,
# kaders en de boog als lagen. Alles in een IDE-venster is een echte opname.
# Gebruik: python3 -I maak_film.py <map met beelden van Jet> <uitvoermap>
import sys, os, math, subprocess
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Tekst met doorzichtigheid mengt in Pillow niet vanzelf op een RGBA-doek: teken hem op een eigen laag.
_orig_text = ImageDraw.ImageDraw.text
def _text(self, xy, text, fill=None, font=None, anchor=None, **kw):
    im = getattr(self, "_image", None)
    if im is None or im.mode != "RGBA" or not isinstance(fill, tuple) or len(fill) < 4 or fill[3] >= 255:
        return _orig_text(self, xy, text, fill=fill, font=font, anchor=anchor, **kw)
    a = fill[3] / 255.0
    if a <= 0: return
    l, t, r, b = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox(xy, text, font=font, anchor=anchor)
    l, t = int(l) - 4, int(t) - 4; r, b = int(r) + 4, int(b) + 4
    o = Image.new("RGBA", (r - l, b - t), (0, 0, 0, 0))
    _orig_text(ImageDraw.Draw(o), (xy[0] - l, xy[1] - t), text, fill=fill[:3] + (255,), font=font, anchor=anchor, **kw)
    o.putalpha(o.getchannel("A").point(lambda v: int(v * a)))
    ox, oy = max(0, l), max(0, t)
    im.alpha_composite(o, (ox, oy), (ox - l, oy - t))
ImageDraw.ImageDraw.text = _text
def bd(im):
    """tekenen dat mengt met wat eronder ligt (voor vormen op het dekkende doek)"""
    d = ImageDraw.Draw(im); d.draw = Image.core.draw(im.im, 1); return d

SRC, OUT = sys.argv[1], sys.argv[2]
ICON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icoon-240.png")
os.makedirs(OUT + "/frames", exist_ok=True)
W, H, FPS = 1920, 1080, 30
FD = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(FD + "Inter-%s.otf" % w, s)
ORANJE, BLAUW, WIT, GRIJS = (255, 138, 61), (88, 146, 255), (240, 242, 246), (165, 170, 182)
MONO = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 30)

def ease(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)
def ease_out(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def lerp(a, b, t): return a + (b - a) * t

# ---------- achtergrond (zoals de poster) ----------
def achtergrond(w, h):
    bg = Image.new("RGB", (w, h), (15, 17, 26))
    glow = Image.new("RGB", (w, h), (0, 0, 0)); d = ImageDraw.Draw(glow)
    d.ellipse((w * 0.62, -h * 0.55, w * 1.35, h * 0.55), fill=(120, 60, 25))
    d.ellipse((-w * 0.3, h * 0.55, w * 0.35, h * 1.5), fill=(25, 50, 110))
    glow = glow.filter(ImageFilter.GaussianBlur(w / 9))
    bg = Image.blend(bg, Image.eval(glow, lambda v: v), 0.0)
    from PIL import ImageChops
    bg = ImageChops.add(bg, glow)
    d = ImageDraw.Draw(bg); step = int(w / 64)
    for x in range(step // 2, w, step):
        for y in range(step // 2, h, step):
            d.point((x, y), fill=(32, 35, 48))
    return bg
BG1 = achtergrond(W, H)
BG2 = achtergrond(W * 2, H * 2)

# ---------- kaarten ----------
TB = 46  # hoogte titelbalk bij schaal 1
def badge(letter, kleur, s):
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, s - 1, s - 1), radius=s // 5, fill=kleur)
    f = font("Bold", int(s * 0.7)); d.text((s / 2, s / 2 + 1), letter, font=f, fill=(255, 255, 255), anchor="mm")
    return im

def kaart(bron, crop, schaal, titel, letter, f=1.0):
    """bron: pad, crop: (x0,y0,x1,y1) in bronpixels, schaal: bron -> scherm (bij f=1)."""
    im = Image.open(bron).convert("RGB").crop(crop)
    bw, bh = int((crop[2] - crop[0]) * schaal), int((crop[3] - crop[1]) * schaal)
    im = im.resize((bw, bh), Image.LANCZOS)
    tb = int(TB * f); r = int(18 * f)
    c = Image.new("RGBA", (bw, bh + tb), (43, 45, 48, 255))
    c.paste(im, (0, tb)); d = ImageDraw.Draw(c)
    d.line((0, tb - 1, bw, tb - 1), fill=(30, 31, 34), width=max(1, int(f)))
    bs = int(26 * f); c.alpha_composite(badge(letter, ORANJE if letter == "Y" else BLAUW, bs), (int(18 * f), (tb - bs) // 2))
    d.text((int(56 * f), tb // 2), titel, font=font("Medium", int(21 * f)), fill=(220, 223, 228), anchor="lm")
    m = Image.new("L", c.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, c.size[0] - 1, c.size[1] - 1), radius=r, fill=255)
    c.putalpha(m)
    return c

def plak(canvas, c, xy, alpha=1.0, schaduw=True):
    x, y = int(xy[0]), int(xy[1])
    if alpha <= 0: return
    if schaduw:
        s = Image.new("RGBA", (c.size[0] + 160, c.size[1] + 160), (0, 0, 0, 0))
        sm = Image.new("L", s.size, 0); ImageDraw.Draw(sm).rounded_rectangle((80, 95, 80 + c.size[0], 95 + c.size[1]), radius=24, fill=int(150 * alpha))
        sm = sm.filter(ImageFilter.GaussianBlur(28)); s.putalpha(sm)
        canvas.alpha_composite(s, (x - 80, y - 80))
    if alpha < 1:
        c = c.copy(); a = c.getchannel("A").point(lambda v: int(v * alpha)); c.putalpha(a)
    canvas.alpha_composite(c, (x, y))

def punt(cardxy, crop, schaal, p, f=1.0):
    """bronpunt -> schermpunt"""
    return (cardxy[0] + (p[0] - crop[0]) * schaal, cardxy[1] + TB * f + (p[1] - crop[1]) * schaal)

# ---------- lagen ----------
def kader(canvas, box, kleur, sterkte=1.0, f=1.0):
    if sterkte <= 0: return
    x0, y0, x1, y1 = box; p = 6 * f
    m = int(50 * f); ox, oy = int(x0 - m), int(y0 - m)
    g = Image.new("RGBA", (int(x1 - x0) + 2 * m, int(y1 - y0) + 2 * m), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    d.rounded_rectangle((x0 - p - ox, y0 - p - oy, x1 + p - ox, y1 + p - oy), radius=10 * f, outline=kleur + (int(230 * sterkte),), width=int(9 * f))
    g = g.filter(ImageFilter.GaussianBlur(10 * f)); canvas.alpha_composite(g, (max(0, ox), max(0, oy)), (max(0, -ox), max(0, -oy)))
    d = bd(canvas)
    d.rounded_rectangle((x0 - p, y0 - p, x1 + p, y1 + p), radius=10 * f, outline=kleur + (int(255 * sterkte),), width=max(2, int(3.5 * f)))

def boog(canvas, a, b, t, f=1.0, buig=0.35):
    """getekende boog van a naar b, t = 0..1 hoe ver hij is"""
    if t <= 0: return
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    c = (mx + dy * buig, my - dx * buig)
    n = 90; pts = []
    for i in range(int(n * t) + 1):
        u = i / n
        pts.append(((1 - u) ** 2 * a[0] + 2 * (1 - u) * u * c[0] + u * u * b[0], (1 - u) ** 2 * a[1] + 2 * (1 - u) * u * c[1] + u * u * b[1], u))
    g = Image.new("RGBA", canvas.size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    def kl(u): return tuple(int(lerp(BLAUW[k], ORANJE[k], u)) for k in range(3))
    for i in range(1, len(pts)):
        d.line((pts[i - 1][0], pts[i - 1][1], pts[i][0], pts[i][1]), fill=kl(pts[i][2]) + (255,), width=int(14 * f))
    bb = g.getbbox()
    if bb:
        bb = (max(0, bb[0] - int(60 * f)), max(0, bb[1] - int(60 * f)), min(canvas.size[0], bb[2] + int(60 * f)), min(canvas.size[1], bb[3] + int(60 * f)))
        canvas.alpha_composite(g.crop(bb).filter(ImageFilter.GaussianBlur(14 * f)), bb[:2])
    d = ImageDraw.Draw(canvas)
    for i in range(1, len(pts)):
        d.line((pts[i - 1][0], pts[i - 1][1], pts[i][0], pts[i][1]), fill=kl(pts[i][2]) + (255,), width=int(5 * f))
    hx, hy, hu = pts[-1]
    if t < 1:
        r = 11 * f; h = Image.new("RGBA", canvas.size, (0, 0, 0, 0)); hd = ImageDraw.Draw(h)
        hd.ellipse((hx - 3 * r, hy - 3 * r, hx + 3 * r, hy + 3 * r), fill=kl(hu) + (200,))
        bb = (int(max(0, hx - 6 * r)), int(max(0, hy - 6 * r)), int(min(canvas.size[0], hx + 6 * r)), int(min(canvas.size[1], hy + 6 * r)))
        canvas.alpha_composite(h.crop(bb).filter(ImageFilter.GaussianBlur(12 * f)), bb[:2])
        d.ellipse((hx - r * 0.6, hy - r * 0.6, hx + r * 0.6, hy + r * 0.6), fill=(255, 255, 255, 255))
    else:  # pijlpunt
        u = 0.97; px = (1 - u) ** 2 * a[0] + 2 * (1 - u) * u * c[0] + u * u * b[0]; py = (1 - u) ** 2 * a[1] + 2 * (1 - u) * u * c[1] + u * u * b[1]
        ang = math.atan2(b[1] - py, b[0] - px); L = 22 * f
        d.polygon([b, (b[0] - L * math.cos(ang - 0.45), b[1] - L * math.sin(ang - 0.45)), (b[0] - L * math.cos(ang + 0.45), b[1] - L * math.sin(ang + 0.45))], fill=ORANJE + (255,))

def rijk(d, xy, delen, f, alpha=255):
    x, y = xy
    for tekst, kleur in delen:
        d.text((x, y), tekst, font=f, fill=kleur + (alpha,))
        x += d.textlength(tekst, font=f)
    return x

def pil(canvas, xy, tekst, soort, alpha=1.0, schaal=1.0):
    d = bd(canvas); f = font("Bold", int(24 * schaal))
    w = d.textlength(tekst, font=f) + 30 * schaal; h = 42 * schaal; x, y = xy
    if soort == "pro":
        d.rounded_rectangle((x, y, x + w, y + h), radius=10 * schaal, fill=(255, 138, 61, int(255 * alpha)))
        d.text((x + w / 2, y + h / 2 + 1), tekst, font=f, fill=(25, 18, 10, int(255 * alpha)), anchor="mm")
    else:
        d.rounded_rectangle((x, y, x + w, y + h), radius=10 * schaal, outline=(150, 220, 170, int(255 * alpha)), width=int(2 * schaal))
        d.text((x + w / 2, y + h / 2 + 1), tekst, font=f, fill=(150, 220, 170, int(255 * alpha)), anchor="mm")
    return x + w

def toets(canvas, xy, tekst, alpha=1.0, ingedrukt=False):
    d = bd(canvas); w = d.textlength(tekst, font=MONO) + 40; x, y = xy; off = 4 if ingedrukt else 0
    d.rounded_rectangle((x, y + 6, x + w, y + 62), radius=10, fill=(150, 155, 165, int(255 * alpha)))
    d.rounded_rectangle((x, y + off, x + w, y + 56 + off), radius=10, fill=(245, 246, 248, int(255 * alpha)))
    d.text((x + w / 2, y + 28 + off), tekst, font=MONO, fill=(30, 32, 38, int(255 * alpha)), anchor="mm")
    return x + w

def kop(canvas, delen, alpha, dy=0, grootte=64, xy=(110, 60)):
    if alpha <= 0: return
    d = ImageDraw.Draw(canvas); rijk(d, (xy[0], xy[1] + dy), delen, font("Bold", grootte), int(255 * alpha))

def klik(canvas, p, t):
    """kring die uitdijt bij de klik, t = 0..1"""
    if t <= 0 or t >= 1: return
    d = bd(canvas); r = 10 + 60 * ease_out(t); a = int(255 * (1 - t))
    d.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), outline=(255, 255, 255, a), width=4)

def nummer(p): return "%s/%s" % (SRC, p)

# ---------- scène 1 en 2: haak en kop (op dubbele grootte, voor de camerabeweging) ----------
L_CROP = (80, 455, 2100, 1000); Y_CROP = (80, 390, 1720, 790); K = 1.16  # 4k -> 2x canvas
L_NUM4 = (1510, 782, 1510 + 66, 782 + 62); Y_NUM4 = (410, 658, 410 + 66, 658 + 62)
kaartL = kaart(nummer("4k/scene4/0001.png"), L_CROP, K, "calc.l", "L", 2)
kaartY = kaart(nummer("4k/scene4/0005.png"), Y_CROP, K, "calc.y", "Y", 2)
POS_L = (220, 1320); POS_Y = (1900, 760)
def nb(box, pos, crop):
    a = punt(pos, crop, K, box[:2], 2); b = punt(pos, crop, K, box[2:], 2)
    return (a[0] / 1, a[1], b[0], b[1])
def haak(t):
    cv = BG2.copy().convert("RGBA")
    plak(cv, kaartY, POS_Y); plak(cv, kaartL, POS_L)
    bl = nb(L_NUM4, POS_L, L_CROP); by = nb(Y_NUM4, POS_Y, Y_CROP)
    kader(cv, bl, ORANJE, ease_out(t / 0.15), 2)
    a = ((bl[0] + bl[2]) / 2, bl[1] - 14); b = ((by[0] + by[2]) / 2, by[3] + 16)
    boog(cv, a, b, ease((t - 0.05) / 0.75), 2, buig=-0.28)
    kader(cv, by, ORANJE, ease_out((t - 0.75) / 0.2), 2)
    u = (t - 0.8) / 0.45
    if 0 < u < 1:
        cx, cy = (by[0] + by[2]) / 2, (by[1] + by[3]) / 2; r = 40 + 260 * ease_out(u)
        d = bd(cv); d.ellipse((cx - r, cy - r * 0.62, cx + r, cy + r * 0.62), outline=ORANJE + (int(220 * (1 - u)),), width=int(8 * (1 - u)) + 2)
    return cv, (a, b)
def scene12(fi, t):
    cv, (a, b) = haak(t)
    # kop en onderregel verschijnen vanaf 1,5 s
    ka = ease((t - 1.55) / 0.45)
    kop(cv, [("Your ", WIT), ("grammar", ORANJE), (" and ", WIT), ("scanner,", BLAUW)], ka, dy=40 * (1 - ka), grootte=150, xy=(220, 160))
    kop(cv, [("finally connected.", WIT)], ka, dy=40 * (1 - ka), grootte=150, xy=(220, 340))
    sa = ease((t - 1.9) / 0.4); d = ImageDraw.Draw(cv)
    rijk(d, (224, 560), [("Click from ", GRIJS), ("return NUM;", WIT), (" straight to its ", GRIJS), ("%token", WIT), (".", GRIJS)], font("Medium", 54), int(255 * sa))
    # camera: begint dichtbij de boog, trekt terug naar het hele beeld
    z = lerp(1.55, 1.0, ease((t - 0.9) / 1.0))
    cx = lerp((a[0] + b[0]) / 2, W, ease((t - 0.9) / 1.0)); cy = lerp((a[1] + b[1]) / 2, H, ease((t - 0.9) / 1.0))
    vw, vh = 2 * W / z, 2 * H / z
    x0 = min(max(0, cx - vw / 2), 2 * W - vw); y0 = min(max(0, cy - vh / 2), 2 * H - vh)
    return cv.crop((int(x0), int(y0), int(x0 + vw), int(y0 + vh))).resize((W, H), Image.LANCZOS)

# ---------- scène 3: gratis ----------
S3_CROP = (40, 130, 1180, 770); S3_K = 1.32; S3_POS = (110, 150)
S3Z_CROP = (380, 560, 1180, 800); S3Z_K = 2.0; S3Z_POS = (110, 290)
s3z = kaart(nummer("scene3/0011.png"), S3Z_CROP, S3Z_K, "calc.y", "Y")
s3 = {i: kaart(nummer("scene3/%04d.png" % i), S3_CROP, S3_K, "calc.y", "Y") for i in range(1, 12)}
S3_SEQ = [(1, 0.35), (2, 0.25), (3, 0.2), (4, 0.15), (5, 0.12), (6, 0.12), (7, 0.12), (8, 0.12), (10, 0.12), (11, 0.95)]
def kopregel(cv, tekst, soort, alpha, dy):
    d = ImageDraw.Draw(cv); f = font("Bold", 56)
    x = 110; y = 52 + dy
    d.text((x, y), tekst, font=f, fill=WIT + (int(255 * alpha),))
    x += d.textlength(tekst, font=f) + 26
    pil(cv, (x, y + 10), soort.upper(), soort, alpha)
def kies(seq, t):
    acc = 0
    for i, dur in seq:
        acc += dur
        if t < acc: return i
    return seq[-1][0]
def scene3(t, dur):
    cv = BG1.copy().convert("RGBA"); i = kies(S3_SEQ, t)
    inn = ease_out(t / 0.3)
    plak(cv, s3[i], (S3_POS[0], S3_POS[1] + 40 * (1 - inn)), inn)
    kopregel(cv, "Colors, structure and syntax errors", "free", ease(t / 0.3), 20 * (1 - ease(t / 0.3)))
    if i == 11:  # inzoomen op de melding (zelfde echte beeld, uitgesneden)
        tt = t - (dur - 0.95); u = ease_out(tt / 0.25)
        cv = BG1.copy().convert("RGBA")
        kopregel(cv, "Colors, structure and syntax errors", "free", 1.0, 0)
        plak(cv, s3z, (S3Z_POS[0], S3Z_POS[1] + 30 * (1 - u)), u)
        p = punt(S3Z_POS, S3Z_CROP, S3Z_K, (705, 717))
        kader(cv, (p[0] - 124, p[1] - 30, p[0] + 124, p[1] + 34), (255, 90, 90), ease_out(tt / 0.25) * 0.9)
    return cv

# ---------- scène 4: Ctrl + Click (4k) ----------
S4_CROP = (80, 380, 2080, 1240); S4_K = 0.82; S4_POS = (140, 175)
S4Y_CROP = (80, 300, 2300, 1460)
s4 = {i: kaart(nummer("4k/scene4/%04d.png" % i), S4_CROP, S4_K, "calc.l" if i <= 4 else "calc.y", "L" if i <= 4 else "Y") for i in range(1, 7)}
def scene4(t, dur):
    cv = BG1.copy().convert("RGBA")
    if t < 0.5: i = 1
    elif t < 1.45: i = 3
    else: i = 5
    if i == 5:
        u = ease_out((t - 1.45) / 0.3)
        plak(cv, s4[5], (S4_POS[0] + 60 * (1 - u), S4_POS[1]), u)
        p0 = punt(S4_POS, S4_CROP, S4_K, (410, 658)); p1 = punt(S4_POS, S4_CROP, S4_K, (476, 720))
        kader(cv, (p0[0], p0[1], p1[0], p1[1]), ORANJE, ease_out((t - 1.6) / 0.3))
    else:
        inn = ease_out(t / 0.3)
        plak(cv, s4[i], (S4_POS[0], S4_POS[1] + 40 * (1 - inn)), inn)
        p0 = punt(S4_POS, S4_CROP, S4_K, (1510, 782)); p1 = punt(S4_POS, S4_CROP, S4_K, (1576, 844))
        if i == 3:
            kader(cv, (p0[0], p0[1], p1[0], p1[1]), BLAUW, ease_out((t - 0.5) / 0.25))
            klik(cv, ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), (t - 1.1) / 0.35)
    ka = ease(t / 0.3)
    d = ImageDraw.Draw(cv); f = font("Bold", 56)
    x = rijk(d, (110, 52 + 20 * (1 - ka)), [("Jump to the ", WIT), ("%token", ORANJE)], f, int(255 * ka))
    pil(cv, (x + 26, 62 + 20 * (1 - ka)), "PRO", "pro", ka)
    # toetsen rechtsonder
    ta = ease((t - 0.35) / 0.25); ing = 0.5 <= t < 1.45
    x = toets(cv, (1340, 960), "Ctrl", ta, ing); d.text((x + 22, 990), "+", font=font("Bold", 36), fill=WIT + (int(255 * ta),), anchor="mm")
    toets(cv, (x + 44, 960), "Click", ta, 1.1 <= t < 1.3)
    return cv

# ---------- scène 5: hernoemen ----------
S5_CROP = (40, 280, 1200, 700); S5_K = 1.45; S5_POS = (110, 170)
s5 = {i: kaart(nummer("scene5/%04d.png" % i), S5_CROP, S5_K, "calc.y", "Y") for i in range(1, 8)}
# eindbeeld: twee kaarten uit hetzelfde gesplitste venster (beeld 9)
S5L_CROP = (40, 230, 880, 510); S5Y_CROP = (965, 300, 1480, 880); S5S_K = 1.3
s5L = kaart(nummer("scene5/0009.png"), S5L_CROP, S5S_K, "calc.l", "L")
s5Y = kaart(nummer("scene5/0009.png"), S5Y_CROP, S5S_K, "calc.y", "Y")
S5L_POS = (100, 430); S5Y_POS = (1215, 170)
S5_SEQ = [(1, 0.35), (2, 0.14), (3, 0.14), (4, 0.14), (5, 0.14), (6, 0.14), (7, 0.45)]
def scene5(t, dur):
    cv = BG1.copy().convert("RGBA"); d = ImageDraw.Draw(cv)
    if t < 1.5:
        i = kies(S5_SEQ, t); inn = ease_out(t / 0.3)
        plak(cv, s5[i], (S5_POS[0], S5_POS[1] + 40 * (1 - inn)), inn)
        if i == 7: klik(cv, punt(S5_POS, S5_CROP, S5_K, (905, 627)), (t - 1.2) / 0.3)
    else:
        u = ease_out((t - 1.5) / 0.35)
        plak(cv, s5Y, (S5Y_POS[0] + 80 * (1 - u), S5Y_POS[1]), u)
        plak(cv, s5L, (S5L_POS[0] - 80 * (1 - u), S5L_POS[1]), u)
        g = ease_out((t - 1.85) / 0.3) * (1 - 0.45 * ease((t - 2.6) / 0.6))  # laag van Daan: kort oplichten
        for pos, crop, p, w in [(S5L_POS, S5L_CROP, (755, 391), 66), (S5Y_POS, S5Y_CROP, (1125, 329), 66), (S5Y_POS, S5Y_CROP, (1092, 856), 66)]:
            a = punt(pos, crop, S5S_K, p); b = punt(pos, crop, S5S_K, (p[0] + w, p[1] + 31))
            kader(cv, (a[0], a[1], b[0], b[1]), BLAUW if crop is S5L_CROP else ORANJE, g)
        la = punt(S5L_POS, S5L_CROP, S5S_K, (755 + 33, 391)); la = (la[0], la[1] - 10)
        ya = punt(S5Y_POS, S5Y_CROP, S5S_K, (1125, 329 + 15)); ya = (ya[0] - 14, ya[1])
        yb = punt(S5Y_POS, S5Y_CROP, S5S_K, (1092, 856 + 15)); yb = (yb[0] - 14, yb[1])
        boog(cv, la, ya, ease((t - 1.9) / 0.45), 1, buig=0.25)
        boog(cv, (la[0], la[1] + 50), yb, ease((t - 2.0) / 0.45), 1, buig=-0.25)
    ka = ease(t / 0.3)
    x = rijk(d, (110, 52 + 20 * (1 - ka)), [("Rename once. ", WIT), ("Both files follow.", ORANJE)], font("Bold", 56), int(255 * ka))
    pil(cv, (x + 26, 62 + 20 * (1 - ka)), "PRO", "pro", ka)
    if t < 1.5:
        ta = ease((t - 0.1) / 0.25); toets(cv, (1500, 960), "Shift+F6", ta, 0.1 <= t < 0.3)
    return cv

# ---------- scène 6: ongebruikte regel ----------
S6_CROP = (40, 430, 1100, 800); S6_K = 1.6; S6_POS = (110, 200)
s6 = {i: kaart(nummer("scene6/%04d.png" % i), S6_CROP, S6_K, "calc.y", "Y") for i in range(1, 5)}
S6_SEQ = [(1, 0.3), (2, 0.5), (3, 0.5), (4, 0.4)]
def scene6(t, dur):
    cv = BG1.copy().convert("RGBA"); i = kies(S6_SEQ, t); inn = ease_out(t / 0.25)
    plak(cv, s6[i], (S6_POS[0], S6_POS[1] + 40 * (1 - inn)), inn)
    ka = ease(t / 0.25); d = ImageDraw.Draw(cv)
    x = rijk(d, (110, 52 + 20 * (1 - ka)), [("Unused rules, ", WIT), ("caught.", ORANJE)], font("Bold", 56), int(255 * ka))
    pil(cv, (x + 26, 62 + 20 * (1 - ka)), "PRO", "pro", ka)
    if i == 3: toets(cv, (1500, 960), "Alt+Enter", 1.0, True)
    return cv

# ---------- scène 7: eindkaart ----------
ICO = Image.open(ICON).convert("RGBA").resize((200, 200), Image.LANCZOS)
def scene7(t, dur):
    cv = BG1.copy().convert("RGBA"); d = ImageDraw.Draw(cv)
    a = ease(t / 0.4); s = lerp(0.85, 1.0, ease_out(t / 0.5))
    ic = ICO.resize((int(200 * s), int(200 * s)), Image.LANCZOS); al = ic.getchannel("A").point(lambda v: int(v * a)); ic.putalpha(al)
    cv.alpha_composite(ic, (W // 2 - ic.size[0] // 2, 250 - ic.size[1] // 2 + 20))
    d.text((W / 2, 440), "Bison & Flex for JetBrains IDEs", font=font("Bold", 76), fill=WIT + (int(255 * a),), anchor="mm")
    b = ease((t - 0.3) / 0.4)
    f = font("Medium", 34)
    zin1 = "Free: colors, structure and syntax errors"
    zin2 = "Pro: jump, rename and unused-code warnings across grammar and scanner"
    d.text((W / 2, 560), zin1, font=f, fill=GRIJS + (int(255 * b),), anchor="mm")
    d.text((W / 2, 612), zin2, font=f, fill=GRIJS + (int(255 * b),), anchor="mm")
    c = ease((t - 0.6) / 0.4)
    d.text((W / 2, 760), "dortus.com/bison-flex", font=font("SemiBold", 44), fill=ORANJE + (int(255 * c),), anchor="mm")
    return cv

SCENES = [(scene12, 3.3), (scene3, 2.6), (scene4, 3.1), (scene5, 3.2), (scene6, 1.7), (scene7, 2.1)]
n = 0; vorige = None
for si, (fn, dur) in enumerate(SCENES):
    nf = int(round(dur * FPS))
    for k in range(nf):
        t = k / FPS
        im = fn(n, t) if fn is scene12 else fn(t, dur)
        im = im.convert("RGB")
        # korte overvloeier naar de volgende scène (laatste 5 beelden)
        if si < len(SCENES) - 1 and k >= nf - 5:
            nxt = SCENES[si + 1][0]; tt = 0.0
            nim = (nxt(n, tt) if nxt is scene12 else nxt(tt, SCENES[si + 1][1])).convert("RGB")
            im = Image.blend(im, nim, (k - (nf - 5) + 1) / 6)
        im.save("%s/frames/%04d.png" % (OUT, n)); n += 1
print("beelden", n, "=", n / FPS, "s")
