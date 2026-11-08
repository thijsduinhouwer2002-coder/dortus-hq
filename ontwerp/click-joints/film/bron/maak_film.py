"""Zet het filmpje van Click Joints in elkaar uit de lagen van Daan en de beelden uit Blender.

Gebruik: python3 maak_film.py draaiboek.json uit.mp4
draaiboek.json: {"fps": 30, "lagen": "..", "scenes": [
  {"beeld": "map/met/frames" of "los.png", "duur": 3.5, "kop": "kop1", "zoom": [1.0, 1.06], "uitsnede": [0, 0, 1920, 885],
   "klik": [x, y, t]}   # klik: plek in het Blender-beeld (pixels van de uitsnede) en moment in seconden
  , {"eind": true, "duur": 3.5}]}
Een map met frames wordt over de duur uitgesmeerd (frame i op tijd i/fps, laatste frame blijft staan).
Regels (Daan): kop van de eerste scene staat meteen; bij een wissel (0,3 s) gaat de oude kop in de eerste helft weg
en komt de nieuwe in de tweede helft op; eindkaart komt in 0,4 s op.
Let op: het pad bij lagen en de beeldpaden gelden vanaf de map van draaiboek.json.
"""
import json, os, subprocess, sys, tempfile, pathlib
from PIL import Image, ImageDraw

boek = json.load(open(sys.argv[1])); uit = sys.argv[2]
basis = pathlib.Path(sys.argv[1]).parent
lagen = (basis / boek.get("lagen", "..")).resolve()
FPS = boek.get("fps", 30)
KX, KY, KW, KH = 110, 236, 1700, 784
bg = Image.open(lagen / "bg.png").convert("RGBA")
rand = Image.open(lagen / "rand.png").convert("RGBA")
masker = Image.open(lagen / "masker.png").convert("L").crop((KX, KY, KX + KW, KY + KH))
eind = Image.open(lagen / "eind.png").convert("RGBA")
koppen = {k: Image.open(lagen / f"{k}.png").convert("RGBA") for k in ("kop1", "kop2", "kop3", "kop4")}


def bronnen(sc):
    p = (basis / sc["beeld"]).resolve()
    if p.is_dir():
        return [Image.open(f).convert("RGB") for f in sorted(p.glob("*.png"))]
    return [Image.open(p).convert("RGB")]


def kaartbeeld(img, sc, t):
    x0, y0, x1, y1 = sc.get("uitsnede", [0, 0, img.width, img.height])
    z0, z1 = sc.get("zoom", [1.0, 1.0]); a = t / sc["duur"]; z = z0 + (z1 - z0) * (a * a * (3 - 2 * a))
    cx, cy = sc.get("zoompunt", [(x0 + x1) / 2, (y0 + y1) / 2])
    w, h = (x1 - x0) / z, (y1 - y0) / z
    # zelfde verhouding als de kaart
    if w / h > KW / KH: w = h * KW / KH
    else: h = w * KH / KW
    l = min(max(cx - w / 2, x0), x1 - w); o = min(max(cy - h / 2, y0), y1 - h)
    return img.crop((int(l), int(o), int(l + w), int(o + h))).resize((KW, KH), Image.LANCZOS), (l, o, w / KW)


def klikring(beeld, sc, t, geo):
    if "klik" not in sc: return
    x, y, tk = sc["klik"]; d = t - tk
    if d < -0.6 or d > 0.7: return
    l, o, s = geo; px, py = (x - l) / s, (y - o) / s
    dr = ImageDraw.Draw(beeld, "RGBA")
    # pijltje schuift in, ring groeit na de klik
    if d < 0: px2, py2 = px + 60 * (-d / 0.6), py + 40 * (-d / 0.6)
    else: px2, py2 = px, py
    pijl = [(px2, py2), (px2, py2 + 30), (px2 + 8, py2 + 23), (px2 + 14, py2 + 36), (px2 + 19, py2 + 34), (px2 + 13, py2 + 21), (px2 + 23, py2 + 21)]
    dr.polygon(pijl, fill=(255, 255, 255, 255), outline=(20, 20, 24, 255))
    if d >= 0:
        r = 10 + 60 * d / 0.7; alfa = int(230 * (1 - d / 0.7))
        dr.ellipse((px - r, py - r, px + r, py + r), outline=(59, 230, 176, alfa), width=4)


def kop_laag(naam, a):
    k = koppen[naam].copy()
    if a < 1: k.putalpha(k.getchannel("A").point(lambda v: int(v * a)))
    return k


def scene_frame(sc, s, bron):
    """Beeld zonder kop (de kop gaat er apart overheen, zodat twee koppen nooit door elkaar lopen)."""
    if sc.get("eind"):
        return eind.copy()
    t = s / FPS
    i = min(s, len(bron) - 1) if len(bron) > 1 else 0
    kb, geo = kaartbeeld(bron[i], sc, t)
    kb = kb.convert("RGBA"); klikring(kb, sc, t, geo)
    f = bg.copy(); f.paste(kb, (KX, KY), masker); f.alpha_composite(rand)
    return f


with tempfile.TemporaryDirectory() as tmp:
    n = 0; vorige = None; vorige_kop = None
    for nr, sc in enumerate(boek["scenes"]):
        bron = None if sc.get("eind") else bronnen(sc)
        stappen = int(round(sc["duur"] * FPS)); over = 0.4 if sc.get("eind") else 0.3
        kop = sc.get("kop")
        for s in range(stappen):
            t = s / FPS; basis_fr = scene_frame(sc, s, bron); fr = basis_fr.copy()
            overgang = vorige is not None and t < over
            if overgang:
                fr = Image.blend(vorige, basis_fr, t / over)
            # kop: eerste scene staat meteen; bij een wissel eerst de oude weg, dan de nieuwe erin
            if overgang and t < over / 2:
                if vorige_kop: fr.alpha_composite(kop_laag(vorige_kop, 1 - t / (over / 2)))
            elif kop:
                a = 1.0 if (nr == 0 or not overgang) else (t - over / 2) / (over / 2)
                fr.alpha_composite(kop_laag(kop, min(1.0, a)))
            fr.convert("RGB").save(f"{tmp}/{n:05d}.png"); n += 1
        vorige = basis_fr; vorige_kop = kop
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/%05d.png",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", uit], check=True)
print(f"{uit}: {n} frames, {n / FPS:.1f} s")
