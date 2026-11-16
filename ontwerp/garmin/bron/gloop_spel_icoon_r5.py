# Gloop op je pols: icoon ronde 5 (Mila, 16 nov 2026). Donkere warme grot zoals de randen van het spel,
# de schuine lichtbundel uit het spel, Gloop groot en lichtgevend, drie hoeden met elk een eigen omtrek
# (kroon, hoge hoed, puntmuts) en een donkere rand ertussen; de bovenste staat scheef net binnen het vak.
#   python3 gloop_spel_icoon_r5.py <rendermap> <uitmap>
import sys, os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
R, UIT = sys.argv[1], sys.argv[2]
sys.argv = ["x", R, os.path.join(UIT, "_kit")]
import gloop_spel_kit as k
import gloop_spel_v2 as v2

MINT = (120, 255, 200)
RAND = (22, 12, 7)
FEL = False   # variant C: zwartere grot, fellere oranje bundel (twee kijkers: bruin verdwijnt tussen felle buren)


def met_rand(im, dik):
    a = im.getchannel("A").point(lambda v: 255 if v > 60 else 0)
    pad = Image.new("L", (im.width + 2 * dik, im.height + 2 * dik), 0); pad.paste(a, (dik, dik))
    groot = pad.filter(ImageFilter.MaxFilter(2 * dik + 1)).filter(ImageFilter.GaussianBlur(1))
    uit = Image.new("RGBA", pad.size, RAND + (0,)); uit.putalpha(groot)
    uit.alpha_composite(im, (dik, dik))
    return uit


def achter(N):
    im = Image.new("RGBA", (N, N), (0, 0, 0, 255))
    # bijna zwart bruin, warmer naar onder het midden (waar Gloop staat)
    gl = Image.new("L", (N, N), 0)
    ImageDraw.Draw(gl).ellipse([-0.25 * N, 0.25 * N, 1.1 * N, 1.5 * N], fill=255)
    gl = gl.filter(ImageFilter.GaussianBlur(N * 0.18))
    mid, rand = ((90, 34, 10), (8, 4, 3)) if FEL else ((66, 34, 18), (16, 9, 6))
    im = Image.composite(Image.new("RGBA", (N, N), mid + (255,)), Image.new("RGBA", (N, N), rand + (255,)), gl)
    # schuine lichtbundel van linksboven, zoals in het spel
    lam = Image.new("L", (N, N), 0); d = ImageDraw.Draw(lam)
    # de bundel valt precies achter de toren: de donkere hoge hoed steekt af tegen het licht
    d.polygon([(N * 0.18, -10), (N * 0.62, -10), (N * 0.86, N * 1.05), (N * 0.30, N * 1.05)], fill=110)
    d.polygon([(N * 0.28, -10), (N * 0.50, -10), (N * 0.70, N * 1.05), (N * 0.44, N * 1.05)], fill=160)
    lam = lam.filter(ImageFilter.GaussianBlur(N * 0.035))
    if FEL:   # spotlicht: oranje bundel, met een witgele kern achter de toren
        im = Image.composite(Image.new("RGBA", (N, N), (255, 140, 40, 255)), im, lam.point(lambda v: min(255, int(v * 1.1))))
        kern = Image.new("L", (N, N), 0)
        ImageDraw.Draw(kern).ellipse([N * 0.22, N * 0.02, N * 0.72, N * 0.62], fill=255)
        kern = kern.filter(ImageFilter.GaussianBlur(N * 0.10))
        im = Image.composite(Image.new("RGBA", (N, N), (255, 226, 150, 255)), im, kern.point(lambda v: int(v * 0.85)))
    else:
        im = Image.composite(Image.new("RGBA", (N, N), (255, 214, 160, 255)), im, lam.point(lambda v: int(v * 0.62)))
    # stofjes in de bundel
    d2 = ImageDraw.Draw(im)
    for x, y, r in [(0.30, 0.08, 5), (0.62, 0.22, 4), (0.36, 0.30, 3), (0.70, 0.42, 4), (0.27, 0.18, 3)]:
        d2.ellipse([x * N - r, y * N - r, x * N + r, y * N + r], fill=(255, 220, 160, 200))
    return im


def icoon(N, gb=0.60, cx=0.43, hw=None, hb=0.56, hoeken=(-6, 8, 22), schuif=(0.0, 0.03, 0.05), licht=0, voet=1.03, rij=(4, 7, 1)):
    im = achter(N)
    rust = v2.schaal(v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-rust-h0.png")).convert("RGBA")), N * gb)
    gx, gy = int(N * cx - rust.width / 2), int(N * voet - rust.height)
    # mintgloed achter Gloop: hij geeft licht in de donkere grot
    a = Image.new("L", (N, N), 0); a.paste(rust.getchannel("A"), (gx, gy))
    a = a.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(N * 0.05)).point(lambda v: int(v * 0.75))
    im = Image.composite(Image.new("RGBA", (N, N), MINT + (255,)), im, a)
    im.alpha_composite(met_rand(rust, int(N * 0.006)), (gx - int(N * 0.006), gy - int(N * 0.006)))
    H = v2.hoeden()
    y = gy + rust.height * k.KRUIN
    x0 = gx + rust.width * 0.52
    import numpy as np
    from scipy import ndimage
    top = y
    tl = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    for n, (i, hoek) in enumerate(zip(rij, hoeken)):
        h = v2.schaal(H[i], (N * hw if hw else rust.width * hb) * (1.0 if i != 1 else 0.95))
        if i == 4 and licht:   # kroon feller goud: blinde kijker las hem klein als mandje
            from PIL import ImageEnhance
            a_ = h.getchannel("A"); h = ImageEnhance.Brightness(ImageEnhance.Color(h.convert("RGB")).enhance(1.25)).enhance(1.3).convert("RGBA"); h.putalpha(a_)
        # alleen het grootste stuk: bij de hoge hoed zat de steel van de pan nog in de uitsnede
        al = np.array(h.getchannel("A")) > 40; lab, cnt = ndimage.label(al)
        if cnt > 1:
            groot = 1 + int(np.argmax(ndimage.sum(al, lab, range(1, cnt + 1))))
            arr = np.array(h); arr[..., 3] = np.where(lab == groot, arr[..., 3], 0); h = v2.bijsnijden(Image.fromarray(arr))
        h = met_rand(h, int(N * 0.011))
        w0, h0 = h.size
        A0 = np.array(h.getchannel("A")) > 100
        c = w0 // 2
        onder0 = np.where(A0[:, c - 3:c + 4].any(1))[0].max()
        # bovenvlak: bij de kroon de band onder de punten (de volgende hoed zakt tussen de punten)
        boven0 = np.where(A0[:, c - 3:c + 4].any(1))[0].min() + (0.38 * h0 if i == 4 else 0.02 * h0)
        hr = h.rotate(-hoek, expand=True, resample=Image.BICUBIC)
        import math
        t = math.radians(-hoek)
        def draai(px, py):
            dx, dy = px - w0 / 2, py - h0 / 2
            return hr.width / 2 + dx * math.cos(t) + dy * math.sin(t), hr.height / 2 - dx * math.sin(t) + dy * math.cos(t)
        ox, oy = draai(c, onder0)
        bx, by = draai(c, boven0)
        x = x0 + schuif[n] * rust.width
        px, py = int(x - ox), int(y - oy)
        tl.alpha_composite(hr, (px, py))
        top = py + np.where((np.array(hr.getchannel("A")) > 100).any(1))[0].min()
        x0, y = px + bx - schuif[n] * rust.width, py + by
    if licht:
        # lichte rand om de hele toren (warm wit): de zwarte hoge hoed valt anders weg in de donkere grot;
        # tussen de hoeden blijft de donkere rand
        ra = tl.getchannel("A").point(lambda v: 255 if v > 60 else 0).filter(ImageFilter.MaxFilter(2 * int(N * licht) + 1)).filter(ImageFilter.GaussianBlur(1.5))
        rl = Image.new("RGBA", (N, N), (255, 236, 200, 0)); rl.putalpha(ra)
        im.alpha_composite(rl)
    im.alpha_composite(tl)
    return im, top


if __name__ == "__main__":
    os.makedirs(UIT, exist_ok=True)
    big, top = icoon(1000, gb=0.50, cx=0.44, hw=0.37, hoeken=(-8, 10, 26), schuif=(0.0, 0.05, 0.07), licht=0.008, voet=1.05)
    print("top bovenste hoed", top)
    big.resize((500, 500), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, "icoon-500-r5.png"))
    FEL = True
    fel, _ = icoon(1000, gb=0.50, cx=0.44, hw=0.37, hoeken=(-8, 10, 26), schuif=(0.0, 0.05, 0.07), licht=0.008, voet=1.05)
    fel.resize((500, 500), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, "icoon-500-r5-kroon-onder.png"))
    for n in (40, 60, 80):
        fel.resize((n, n), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"launcher-{n}-r5-fel.png"))
    # variant D: kroon bovenop (zijn punten lezen als silhouet tegen het licht), hoge hoed balanceert op de punt van de puntmuts
    om, top = icoon(1000, gb=0.50, cx=0.44, hw=0.33, hoeken=(-6, 14, 30), schuif=(0.0, 0.0, 0.06), licht=0.008, voet=1.07, rij=(1, 7, 4))
    print("top D", top)
    om.resize((500, 500), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, "icoon-500-r5-kroon-boven.png"))
    for n in (40, 60, 80):
        om.resize((n, n), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"launcher-{n}-r5-kroon-boven.png"))
    strak = big   # hele icoon: met de grote Gloop leest het oog ook op 40 px, en de toren blijft heel
    for n in (40, 60, 80):
        strak.resize((n, n), Image.LANCZOS).convert("RGB").save(os.path.join(UIT, f"launcher-{n}-r5.png"))
    import shutil; shutil.rmtree(os.path.join(UIT, "_kit"), ignore_errors=True)
    print("klaar")
