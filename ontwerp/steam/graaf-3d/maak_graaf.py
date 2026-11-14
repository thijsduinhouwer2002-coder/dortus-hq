"""Graafmoment in de 3D-stijl (Daan, 14 nov 2026).

Maakt kunst/graaf_3d.png: 4 beelden van 64 x 64 bladpixels (16 x 16 spelpixels, 4 bladpixels per spelpixel,
zelfde maat als hol_proef.png), naast elkaar. Elk beeld is de aarde die nog over is in een net gegraven cel, met
een lichte rand waar hij afbreekt, steentjes die vallen en een stofwolkje. Het gat groeit vanuit het midden,
want de held graaft vanaf links of rechts en dat moet allebei kloppen.

Bron van de aarde: het echte 3D-stuk `aarde` uit godot/kunst/3d/hol_proef.png (Mila's hol.py via Brams pijplijn),
zodat de kleur en korrel precies gelijk zijn aan de cel ernaast. Steentjes zijn bolletjes met hetzelfde zachte licht
van linksboven als Gloop en de kist (3d-stijl.md).

Bram 14 nov 12:30 (kan van Daan 09:35: "rechte kant naast een gegraven buur, lichte rand om het gat"): het blad heeft
nu 4 rijen van elk 4 beelden (256 x 256). Rij 0 midden (zoals eerst: het gat groeit uit het midden), rij 1 open naar
links, rij 2 open naar rechts (het gat begint over de hele hoogte aan de kant van de gang die er al was, dus een rechte
kant naast de buur en geen aardkorst tussen twee open cellen), rij 3 open naar onder (een kamer boven de gang). Rondom
het gat loopt een smalle lichte breukrand in kiezelkleur (licht van linksboven blijft: de schaduwkant is minder licht).
hol.gd kiest de rij; een blad van 64 hoog (oud) geeft altijd rij 0.

Gebruik: python3 maak_graaf.py <hol_proef.png> <uitmap>
"""
import sys, math
import numpy as np
from PIL import Image, ImageFilter

S = 64
FRAMES = 4
OVER = [0.86, 0.58, 0.30, 0.10]      # deel aarde dat over is, zoals de oude stippen (hol.gd)


def ruis(seed, schaal):
    rng = np.random.default_rng(seed)
    n = S // schaal + 2
    g = rng.random((n, n))
    im = Image.fromarray((g * 255).astype(np.uint8)).resize((n * schaal, n * schaal), Image.BICUBIC)
    return np.asarray(im, dtype=np.float32)[:S, :S] / 255.0


def bol(r, kleur, licht=(-0.55, -0.6)):
    """Bolletje van straal r (bladpixels), zacht belicht van linksboven, met doorzichtige rand."""
    d = int(math.ceil(r * 2 + 2))
    yy, xx = np.mgrid[0:d, 0:d].astype(np.float32)
    c = (d - 1) / 2
    nx, ny = (xx - c) / r, (yy - c) / (r * 0.86)   # iets platter: een kluitje, geen knikker
    rr = nx * nx + ny * ny
    a = np.clip((1.0 - rr) * r * 3.0, 0, 1)
    nz = np.sqrt(np.clip(1 - rr, 0, 1))
    lam = np.clip((nx * licht[0] + ny * licht[1]) * 0.6 + nz * 0.7, 0, 1)   # bol: licht linksboven
    k = np.array(kleur, dtype=np.float32)[None, None, :] / 255.0
    rgb = k * (0.45 + 0.75 * lam[..., None])
    rgb += (np.clip(lam - 0.93, 0, 1) * 2.0)[..., None] * 0.25          # klein glimlicht
    out = np.dstack([np.clip(rgb, 0, 1), a])
    return out


def plak(doek, stuk, x, y):
    h, w = stuk.shape[:2]
    x0, y0 = int(round(x - w / 2)), int(round(y - h / 2))
    for yy in range(h):
        ty = y0 + yy
        if not 0 <= ty < S:
            continue
        for xx in range(w):
            tx = x0 + xx
            if not 0 <= tx < S:
                continue
            a = stuk[yy, xx, 3]
            if a <= 0:
                continue
            da = doek[ty, tx, 3]
            oa = a + da * (1 - a)
            doek[ty, tx, :3] = (stuk[yy, xx, :3] * a + doek[ty, tx, :3] * da * (1 - a)) / max(oa, 1e-6)
            doek[ty, tx, 3] = oa


KANTEN = ["midden", "links", "rechts", "onder"]   # rij in het blad


def afstand(kant, xx, yy):
    """Hoe ver een bladpixel van het begin van het gat ligt (klein = valt eerst weg)."""
    dx, dy = (xx - 31.5) / 32, (yy - 28) / 32
    if kant == "midden":
        # afstand tot het midden, iets lager (de vloer valt eerst weg)
        d = np.sqrt(dx * dx * 0.9 + dy * dy)
    elif kant in ("links", "rechts"):
        # vanaf de open kant over de hele hoogte; een beetje bol zodat het midden van de wand eerst wijkt
        u = xx / (S - 1) if kant == "links" else (S - 1 - xx) / (S - 1)
        d = u * 1.25 + dy * dy * 0.35
    else:
        # kamer boven de gang: vanaf de vloer omhoog, het midden eerst
        u = (S - 1 - yy) / (S - 1)
        d = u * 1.25 + dx * dx * 0.35
    return d + (ruis(3, 16) - 0.5) * 0.45 + (ruis(5, 8) - 0.5) * 0.10   # grove brokken, weinig fijne rafel


def maak(aarde):
    return np.concatenate([maak_rij(aarde, k) for k in KANTEN], 0)


def maak_rij(aarde, kant):
    aarde = aarde.astype(np.float32) / 255.0
    yy, xx = np.mgrid[0:S, 0:S].astype(np.float32)
    d = afstand(kant, xx, yy)
    gem = aarde[..., :3].reshape(-1, 3).mean(0)
    pix = aarde[..., :3].reshape(-1, 3)
    hel = pix.sum(1)
    kiezel = pix[hel >= np.quantile(hel, 0.97)].mean(0)   # de lichte kiezels in de aardtegel
    beelden = []
    rng = np.random.default_rng(11)
    stenen = [  # x, start y, eind y, straal, kleur-factor, vertraging
        (15, 14, 56, 5.0, 1.0, 0.00), (30, 20, 58, 3.6, 0.85, 0.15), (45, 12, 56, 4.4, 1.05, 0.05),
        (54, 24, 58, 3.0, 0.9, 0.30), (23, 26, 59, 2.6, 0.8, 0.35)]
    for i, over in enumerate(OVER):
        # drempel zo kiezen dat precies `over` van de cel aarde blijft
        drem = np.quantile(d, 1 - over)
        rest = (d >= drem).astype(np.float32)
        m = Image.fromarray((rest * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
        a = np.asarray(m, dtype=np.float32) / 255.0
        # rand: hoe dicht bij het gat (binnen ±5 bladpixels)
        gat = 1 - rest
        g5 = np.asarray(Image.fromarray((gat * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3.0)),
                        dtype=np.float32) / 255.0
        # licht van linksboven: rand die naar rechtsonder in het gat kijkt is licht, de andere kant donker
        gx = np.roll(g5, -2, 1) - np.roll(g5, 2, 1)
        gy = np.roll(g5, -2, 0) - np.roll(g5, 2, 0)
        licht = np.clip((gx * 0.7 + gy * 1.0) * 3.0, -1, 1)
        rgb = aarde[..., :3].copy()
        rand = np.clip(g5 * 2.2, 0, 1) * rest
        rgb = rgb * (1 - 0.30 * rand[..., None])                                   # dikte: de breuk is donkerder
        lip = np.clip(licht, 0, 1) * rand
        rgb = rgb * (1 - lip[..., None]) + kiezel * lip[..., None] * 0.95          # lichte breukrand in kiezelkleur
        rgb = rgb * (1 - 0.35 * (np.clip(-licht, 0, 1) * rand)[..., None])          # schaduwkant
        # smalle lichte rand rondom het gat (Daan 09:35), aan de schaduwkant zwakker zodat het licht linksboven blijft
        g1 = np.asarray(Image.fromarray((gat * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.4)),
                        dtype=np.float32) / 255.0
        zoom = np.clip(g1 * 3.0, 0, 1) * rest * (0.75 - 0.35 * np.clip(-licht, 0, 1))
        rgb = rgb * (1 - zoom[..., None]) + np.clip(kiezel * 1.15, 0, 1) * zoom[..., None]
        doek = np.dstack([np.clip(rgb, 0, 1), a])
        # stofwolkje achter de steentjes: warm, zacht, groeit en vervaagt
        f = (i + 0.5) / FRAMES
        stof = np.zeros((S, S, 4), np.float32)
        for (cx, cy, r0) in [(16, 58, 7), (48, 58, 7), (32, 54, 9)]:
            r = r0 + f * 12
            dd = np.sqrt((xx - cx) ** 2 + ((yy - cy) * 1.5) ** 2) / r
            stof[..., 3] = np.maximum(stof[..., 3], np.clip(1 - dd, 0, 1) ** 1.4 * 0.7 * (1 - f) ** 0.8)
        stof[..., :3] = np.clip(kiezel * 1.35 + 0.08, 0, 1)
        onder = stof
        # samen: stof achter, dan aarde, dan stenen
        out = onder.copy()
        aa = doek[..., 3:4]
        oa = aa + out[..., 3:4] * (1 - aa)
        out[..., :3] = (doek[..., :3] * aa + out[..., :3] * out[..., 3:4] * (1 - aa)) / np.maximum(oa, 1e-6)
        out[..., 3:4] = oa
        for (sx, sy0, sy1, r, kf, vt) in stenen:
            t = np.clip((i + 1) / FRAMES * 1.25 - vt, 0, 1)
            if t <= 0:
                continue
            sy = sy0 + (sy1 - sy0) * t * t
            kleur = np.clip(kiezel * kf * 0.95 * 255, 0, 255)
            schaduw = bol(r * 1.1, (20, 8, 24)); schaduw[..., 3] *= 0.45 * t
            plak(out, schaduw, sx + 1.2, sy + 1.5)
            plak(out, bol(r * 1.15, kleur), sx, sy)
        beelden.append(out)
    return np.concatenate(beelden, 1)


if __name__ == "__main__":
    bron = Image.open(sys.argv[1]).convert("RGBA")
    aarde = np.asarray(bron.crop((76, 4, 140, 68)))   # vak_px van `aarde` in sprites.json
    uit = sys.argv[2]
    blad = Image.fromarray((np.clip(maak(aarde), 0, 1) * 255).astype(np.uint8), "RGBA")
    blad.save(uit + "/graaf_3d.png")
    print("klaar", blad.size)
