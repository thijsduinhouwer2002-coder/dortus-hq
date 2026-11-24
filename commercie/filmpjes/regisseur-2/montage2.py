#!/usr/bin/env python3
"""Uitlegfilmpje met voice-over waarbij het beeld precies op de stem valt (opdracht hoofdchat 23 nov 2026 ±11:45 NL).

Regisseur 2 (23 nov 2026): kopie van ../stem/montage.py met een nieuwe vorm "groot" (Short 1080x1920): het beeld
vult bijna het hele scherm (venster 1040 breed, 1230 hoog in plaats van 980x860), label en kop klein bovenaan,
en GROTE ondertitels (2 tot 4 woorden tegelijk, wit met donkere rand, getallen geel) die met de stem meelopen.
Het hook-beeld (scène 1) zoomt duidelijk in (1,00 naar 1,18), zodat er vanaf beeld 1 beweging is (les van Iris,
23 nov: de best bekeken Shorts bewegen vanaf 0,5 s). De vormen staand en liggend werken nog als in het origineel.

    python3 montage2.py <script.json> <bronmap> <uitmap> [groot|staand|liggend]

Werkwijze (beeld volgt stem, niet andersom):
1. stem.py maakt per zin de audio en meet de lengte (open stem Kokoro, of ElevenLabs als die sleutel er is).
2. De tijdlijn: zin i begint op het eind van zin i-1 plus PAUZE; de scène van zin i begint LEAD seconden vóór de stem.
3. Per beeld: een lichte achtergrond met zachte kleurvlakken, het Blender-scherm in een net venster met zachte schaduw,
   bij elke nieuwe zin een zoom naar het deel van het scherm waar de zin over gaat; links boven een label in een
   gekleurde pil, een grote vette kop en de gesproken zin als regel eronder. Eindbeeld: icoon, titel en één zin.
4. Geluid: de stem duidelijk boven een zachte eigen ondergrond (commercie/filmpjes/geluid/geluid.py), met een zacht
   tikje bij elke muisklik in beeld. Geen muziek van anderen.
Bron: een ruwe opname met film.json (opname-ruw.mkv, X-scherm 2160x1920, delen en muis per beeld), zoals
commercie/filmpjes/youtube-shorts-4/opname.py die maakt, plus de renders render-N.png.
Uit: <naam>-<vorm>.mp4, <naam>-<vorm>-script.json (zinnen met tijden), <naam>-<vorm>.srt, overzicht-<vorm>.jpg."""
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "stem"))
sys.path.insert(0, str(HIER.parent / "geluid"))
import geluid as g  # noqa: E402
import stem  # noqa: E402

FPS = 30
PAUZE = 0.35     # stilte tussen twee zinnen (s)
LEAD = 0.10      # het beeld wisselt zo veel eerder dan de stem begint (s)
START = 0.15     # eerste zin begint na zo veel (s)
NASLEEP = 1.8    # eindbeeld blijft na de laatste zin zo lang staan (s)
ZOOM = 0.55      # duur van de zoom naar het nieuwe deel bij elke zin (s)
FADE = 0.22      # label, kop en zin komen in zo veel seconden op
SW, SH = 2160, 1920

INKT, ZACHT, ACHTER = (23, 32, 51), (74, 85, 104), (238, 242, 246)
KLEUR = {"oranje": (232, 119, 46), "groen": (18, 150, 128), "blauw": (61, 107, 224), "rood": (214, 58, 52)}
NADRUK = (255, 176, 32)


def font(stijl, grootte):
    r = subprocess.run(["fc-match", "-f", "%{file}", f"Inter:style={stijl}"], capture_output=True, text=True)
    pad = r.stdout.strip()
    try:
        return ImageFont.truetype(pad, grootte)
    except OSError:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", grootte)


# ---------- vormen ----------

VORMEN = {
    "staand": {
        "W": 1080, "H": 1920,
        "venster": (50, 640, 1030, 1500), "balk": 46,
        "tekst_x": 60, "tekst_w": 960, "pil_y": 168, "kop": 88, "zin": 40, "pil": 28,
        "inzet": (150, 1478, 930),         # x0, y-onder, x1: kaartje onder in het venster
        "print": (540, 1538, 30),          # midden-x, y, grootte (boven de strook van de Shorts-speler)
        "render": (60, 640, 1020, 1500),
    },
    "groot": {
        "W": 1080, "H": 1920,
        "venster": (20, 340, 1060, 1570), "balk": 40,
        "tekst_x": 48, "tekst_w": 984, "pil_y": 78, "kop": 72, "zin": 0, "pil": 26,
        "inzet": (150, 1548, 930),
        "print": (540, 1600, 30),
        "render": (0, 330, 1080, 1580),
        "ondertitel": (540, 1395, 80),     # midden-x, midden-y, grootte: over het onderste deel van het beeld
    },
    "liggend": {
        "W": 1920, "H": 1080,
        "venster": (70, 90, 1250, 990), "balk": 42,
        "tekst_x": 1320, "tekst_w": 540, "pil_y": 250, "kop": 68, "zin": 32, "pil": 24,
        "inzet": (1320, 900, 1860),
        "print": (1590, 1020, 22),
        "render": (90, 90, 1230, 990),
    },
}


def wikkel(tekst, fnt, breed):
    regels, regel = [], ""
    for w in tekst.split():
        p = (regel + " " + w).strip()
        if fnt.getlength(p) <= breed or not regel:
            regel = p
        else:
            regels.append(regel)
            regel = w
    if regel:
        regels.append(regel)
    return regels


def achtergrond(V):
    W, H = V["W"], V["H"]
    im = Image.new("RGB", (W, H), ACHTER)
    vlak = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(vlak)
    s = W / 1080 if W < H else H / 1080
    for (fx, fy, r, kl) in [(0.05, 0.08, 420, (255, 206, 170, 150)), (1.0, 0.42, 460, (164, 232, 214, 150)),
                            (0.12, 0.93, 400, (212, 203, 250, 140)), (0.85, 0.02, 260, (196, 214, 255, 120))]:
        cx, cy, rr = fx * W, fy * H, r * s
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=kl)
    vlak = vlak.filter(ImageFilter.GaussianBlur(160 * s))
    im.paste(vlak, (0, 0), vlak)
    return im


def schaduw(im, box, straal, verschuif=18, blur=38, sterk=60):
    x0, y0, x1, y1 = box
    sch = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).rounded_rectangle((x0, y0 + verschuif, x1, y1 + verschuif), straal, fill=(20, 30, 50, sterk))
    sch = sch.filter(ImageFilter.GaussianBlur(blur))
    im.paste(sch, (0, 0), sch)


def basis(V, script):
    """Achtergrond, schaduw en venster (zonder inhoud) plus de printzin: voor alle scènes met het scherm gelijk."""
    im = achtergrond(V)
    x0, y0, x1, y1 = V["venster"]
    schaduw(im, V["venster"], 26)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x0, y0, x1, y1), 26, fill=(255, 255, 255), outline=(214, 220, 230), width=2)
    b = V["balk"]
    for i, kl in enumerate([(255, 97, 89), (255, 189, 46), (40, 201, 65)]):
        cx, cy = x0 + 30 + i * 26, y0 + b // 2
        d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=kl)
    f = font("Medium", 20 if V["W"] < V["H"] else 18)
    titel = script.get("venster", "Blender 5.3 with Click Joints Pro")   # tip-reeks: "Blender 5.3" (geen add-on)
    d.text(((x0 + x1) / 2 - f.getlength(titel) / 2, y0 + b / 2 - 11), titel, font=f, fill=(120, 128, 142))
    return im


def printzin(im, V, tekst):
    cx, y, gr = V["print"]
    f = font("Medium", gr)
    ImageDraw.Draw(im).text((cx - f.getlength(tekst) / 2, y), tekst, font=f, fill=(84, 96, 116))


def tekstlaag(V, sc):
    """Label in een pil, grote vette kop en de gesproken zin, als RGBA-laag."""
    laag = Image.new("RGBA", (V["W"], V["H"]), (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    x, y, w = V["tekst_x"], V["pil_y"], V["tekst_w"]
    if sc.get("label"):
        fp = font("Bold", V["pil"])
        tek = sc["label"]
        sp = 2.2
        tw = sum(fp.getlength(c) + sp for c in tek) - sp
        ph = int(V["pil"] * 2.1)
        d.rounded_rectangle((x, y, x + tw + 2 * V["pil"] * 0.95, y + ph), ph // 2, fill=KLEUR.get(sc.get("kleur"), KLEUR["blauw"]))
        cx = x + V["pil"] * 0.95
        for c in tek:
            d.text((cx, y + ph / 2 - V["pil"] * 0.62), c, font=fp, fill=(255, 255, 255))
            cx += fp.getlength(c) + sp
        y += ph + int(V["pil"] * 1.1)
    if sc.get("kop"):
        # "groot": de hook in de eerste 1,5 s (recept v3), kop 1,4 keer zo groot
        gk = int(V["kop"] * (1.4 if sc.get("groot") else 1))
        fk = font("ExtraBold", gk)
        for r in wikkel(sc["kop"], fk, w):
            d.text((x - 3, y), r, font=fk, fill=INKT)
            y += int(gk * 1.08)
        y += int(gk * 0.22)
    if not V["zin"]:
        return laag
    fz = font("Medium", V["zin"])
    for r in wikkel(sc["tekst"], fz, w):
        d.text((x, y), r, font=fz, fill=ZACHT)
        y += int(V["zin"] * 1.35)
    return laag


def eindkaart(V, script, bron):
    e = script["eind"]
    im = achtergrond(V)
    W, H = V["W"], V["H"]
    d = ImageDraw.Draw(im)
    staand = W < H
    logo = Image.open(HIER.parents[2] / e.get("icoon", "ontwerp/click-joints/icoon.png")).convert("RGBA")  # icoon: pad vanaf de repo (Click Cuts, run 18)
    ls = 210 if staand else 170
    logo = logo.resize((ls, ls), Image.LANCZOS)
    fk, fz, fa = font("ExtraBold", 92 if staand else 76), font("Medium", 40 if staand else 32), font("Bold", 40 if staand else 32)
    if staand:
        cx, y = W // 2, 230
        schaduw(im, (cx - ls // 2, y, cx + ls // 2, y + ls), 40, 12, 24, 50)
        im.paste(logo, (cx - ls // 2, y), logo)
        y += ls + 50
        d.text((cx - fk.getlength(e["titel"]) / 2, y), e["titel"], font=fk, fill=INKT)
        y += 120
        for r in wikkel(e["zin"], fz, 880):
            d.text((cx - fz.getlength(r) / 2, y), r, font=fz, fill=ZACHT)
            y += 54
        vak = (140, y + 30, 940, 1390)
    else:
        cx, y = 1380, 200
        im.paste(logo, (cx - ls // 2, y), logo)
        y += ls + 40
        d.text((cx - fk.getlength(e["titel"]) / 2, y), e["titel"], font=fk, fill=INKT)
        y += 100
        for r in wikkel(e["zin"], fz, 760):
            d.text((cx - fz.getlength(r) / 2, y), r, font=fz, fill=ZACHT)
            y += 44
        vak = (120, 80, 820, 1000)
    plak_render(im, bron / e["render"], vak)
    # meetadres in een pil
    a = e["adres"]
    aw = fa.getlength(a) + 70
    ay = 1420 if staand else y + 50
    acx = W // 2 if staand else cx
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((acx - aw / 2, ay, acx + aw / 2, ay + 76 if staand else ay + 64), 40, fill=KLEUR["groen"])
    d.text((acx - fa.getlength(a) / 2, ay + (14 if staand else 12)), a, font=fa, fill=(255, 255, 255))
    printzin(im, V, script["printzin"])
    return im


def plak_render(im, pad, vak, zoom=1.0):
    r = Image.open(pad).convert("RGBA")
    r = r.crop(r.getchannel("A").getbbox())
    x0, y0, x1, y1 = vak
    s = min((x1 - x0) / r.width, (y1 - y0) / r.height) * zoom
    r = r.resize((max(1, int(r.width * s)), max(1, int(r.height * s))), Image.LANCZOS)
    px, py = int((x0 + x1) / 2 - r.width / 2), int((y0 + y1) / 2 - r.height / 2)
    # zachte schaduw op de vloer
    sch = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sch).ellipse((px + r.width * 0.15, py + r.height - 18, px + r.width * 0.85, py + r.height + 22),
                                fill=(20, 30, 50, 60))
    sch = sch.filter(ImageFilter.GaussianBlur(16))
    im.paste(sch, (0, 0), sch)
    im.paste(r, (px, py), r)


# ---------- grote ondertitels (vorm groot) ----------

def gewicht(w):
    """Hoe lang de stem ongeveer over een woord doet, in tekens van de uitspraak (getallen en mm duren langer)."""
    k = w.strip(".,:;?!")
    if any(c.isdigit() for c in k):
        return 4 + 6 * len([c for c in k if c.isdigit() or c == "."])
    if k.lower() == "mm":
        return 12
    return len(k) + 2


def brokken(tekst, max_tekens=16, max_woorden=3):
    """Zin in stukjes van 2 tot 3 woorden, met per stuk het aandeel in de spreektijd (0 tot 1)."""
    ws = tekst.split()
    groepen, g = [], []
    for w in ws:
        if g and (len(" ".join(g + [w])) > max_tekens or len(g) >= max_woorden):
            groepen.append(g)
            g = []
        g.append(w)
        if w[-1] in ".?!:" and len(g) >= 1:
            groepen.append(g)
            g = []
    if g:
        groepen.append(g)
    tot = sum(gewicht(w) for w in ws)
    uit, acc = [], 0.0
    for g in groepen:
        uit.append((" ".join(g), acc / tot))
        acc += sum(gewicht(w) for w in g)
    return uit


def ondertitel_laag(V, tekst):
    cx, cy, gr = V["ondertitel"]
    laag = Image.new("RGBA", (V["W"], V["H"]), (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    f = font("ExtraBold", gr)
    regels = wikkel(tekst, f, 940)
    lh = int(gr * 1.12)
    y = cy - lh * len(regels) / 2
    for r in regels:
        x = cx - f.getlength(r) / 2
        for w in r.split(" "):
            kl = (255, 214, 64) if any(c.isdigit() for c in w) else (255, 255, 255)
            d.text((x, y), w, font=f, fill=kl, stroke_width=9, stroke_fill=(16, 20, 30))
            x += f.getlength(w + " ")
        y += lh
    return laag


def ondertitels_maken(V, script, tl):
    """Per scène een lijst (begintijd in s, laag). Het stuk blijft staan tot het volgende komt."""
    uit = []
    for s, t in zip(script["scenes"], tl):
        if s["beeld"].get("eindkaart"):
            uit.append([])
            continue
        lengte = t["stem_eind"] - t["stem_start"]
        uit.append([(t["stem_start"] + aandeel * lengte - 0.04, ondertitel_laag(V, stuk))
                    for stuk, aandeel in brokken(s["tekst"])])
    return uit


def plak_ondertitel(im, onder, tijd):
    """im is RGBA; tijd in s vanaf het begin van de film."""
    huidig = None
    for t0, laag in onder:
        if tijd >= t0:
            huidig = laag
    if huidig is not None:
        im.alpha_composite(huidig)
    return im


_VOL = {}


def vol_beeld(pad, W, H, zoom, focus):
    """Render die het hele beeld vult (cover), ingezoomd rond focus (fractie van breedte en hoogte)."""
    if pad not in _VOL:
        _VOL[pad] = Image.open(pad).convert("RGB")
    r = _VOL[pad]
    s = max(W / r.width, H / r.height) * zoom
    bw, bh = W / s, H / s
    fx, fy = focus[0] * r.width, focus[1] * r.height
    x0 = min(max(0, fx - bw / 2), r.width - bw)
    y0 = min(max(0, fy - bh / 2), r.height - bh)
    return r.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + bw, y0 + bh))


# ---------- muis ----------

def pijl(schaal=1.9):
    pts = [(0, 0), (0, 17), (4, 13), (7, 20), (10, 19), (7, 12), (12, 12)]
    n = int(24 * schaal)
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    p = [(x * schaal + 2, y * schaal + 2) for x, y in pts]
    d.polygon(p, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    d.line(p + [p[0]], fill=(0, 0, 0, 255), width=3)
    return im


PIJL = pijl()


def kring(r):
    n = 2 * r + 8
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse((4, 4, n - 4, n - 4), outline=(255, 210, 63, 235), width=6)
    return im


KRINGEN = [kring(r) for r in range(14, 62, 6)]


# ---------- tijdlijn ----------

def tijdlijn(script, duren):
    sc = script["scenes"]
    t = START
    uit = []
    for i, (s, d) in enumerate(zip(sc, duren)):
        uit.append({"nr": i + 1, "tekst": s["tekst"], "stem_start": round(t, 3), "stem_eind": round(t + d, 3),
                    "scene_start": 0.0 if i == 0 else round(t - LEAD, 3)})
        t += d + PAUZE
    for i in range(len(uit) - 1):
        uit[i]["scene_eind"] = uit[i + 1]["scene_start"]
    uit[-1]["scene_eind"] = round(uit[-1]["stem_eind"] + NASLEEP, 3)
    return uit


def zacht(u):
    u = min(1.0, max(0.0, u))
    return u * u * (3 - 2 * u)


def meng(a, b, u):
    return [a[k] + (b[k] - a[k]) * u for k in range(3)]


ASPECT_REF = 976 / 812   # uitsneden in het script zijn op het staande venster gemaakt: de hoogte blijft gelijk


def rect_van(u, aspect):
    cx, cy, w = u
    w = w / ASPECT_REF * aspect
    w = min(w, SW, SH * aspect)
    h = w / aspect
    x0 = min(max(0, cx - w / 2), SW - w)
    y0 = min(max(0, cy - h / 2), SH - h)
    return (x0, y0, x0 + w, y0 + h)


# ---------- hoofdwerk ----------

def main():
    script = json.loads(Path(sys.argv[1]).read_text())
    bron, uitmap = Path(sys.argv[2]), Path(sys.argv[3])
    vorm = sys.argv[4] if len(sys.argv) > 4 else "staand"
    V = VORMEN[vorm]
    uitmap.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    film = json.loads((bron / "film.json").read_text())
    delen, muis = film["delen"], film.get("muis", [])

    # 1. stem per zin (hergebruik als een andere vorm hem al maakte)
    zmap = uitmap / "zinnen"
    info_pad = zmap / "stem.json"
    if info_pad.exists() and json.loads(info_pad.read_text()).get("teksten") == [s["tekst"] for s in script["scenes"]]:
        z = json.loads(info_pad.read_text())
        zinnen, info = z["zinnen"], z["info"]
    else:
        zinnen, info = stem.maak_zinnen(script["scenes"], zmap)
        info_pad.write_text(json.dumps({"teksten": [s["tekst"] for s in script["scenes"]], "zinnen": zinnen,
                                        "info": info}, indent=1, ensure_ascii=False))
    tl = tijdlijn(script, [z["duur"] for z in zinnen])
    duur = tl[-1]["scene_eind"]
    N = int(round(duur * FPS))

    # 2. vaste lagen
    W, H = V["W"], V["H"]
    vx0, vy0, vx1, vy1 = V["venster"]
    cx0, cy0, cx1, cy1 = vx0 + 2, vy0 + V["balk"], vx1 - 2, vy1 - 2
    cw, ch = cx1 - cx0, cy1 - cy0
    aspect = cw / ch
    b_scherm = basis(V, script)
    printzin(b_scherm, V, script["printzin"])
    b_leeg = achtergrond(V)
    printzin(b_leeg, V, script["printzin"])
    hoek = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(hoek).rounded_rectangle((0, -40, cw - 1, ch - 1), 24, fill=255)
    lagen = [tekstlaag(V, s) for s in script["scenes"]]
    groot = "ondertitel" in V
    onders = ondertitels_maken(V, script, tl) if groot else [[] for _ in script["scenes"]]
    eind = eindkaart(V, script, bron)

    enc = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                            "-pix_fmt", "yuv420p", str(tmp / "stil.mp4")], stdin=subprocess.PIPE)
    kliks = []
    # begin_uitsnede (run 19): het eerste beeld meteen dichtbij, niet vanaf het hele scherm inzoomen (kan Iris bij cc-fit)
    vorige_u = list(script["scenes"][0].get("beeld", {}).get("begin_uitsnede", [SW / 2, SH / 2, SW]))
    for i, (s, t) in enumerate(zip(script["scenes"], tl)):
        b = s["beeld"]
        f0, f1 = int(round(t["scene_start"] * FPS)), int(round(t["scene_eind"] * FPS))
        n = f1 - f0
        laag = lagen[i]
        if "render" in b or b.get("eindkaart"):
            for k in range(n):
                tt = k / FPS
                if b.get("eindkaart"):
                    im = eind.copy()
                    a = zacht(tt / 0.35)
                    if a < 1:
                        im = Image.blend(b_leeg, im, a)
                elif groot:
                    # vorm groot: de render vult het hele beeld (1080x1920), langzaam inzoomen op het midden
                    zm = 1.0 + (0.18 if i == 0 else 0.07) * zacht(k / max(1, n - 1))
                    im = vol_beeld(bron / b["render"], W, H, zm, b.get("focus", [0.5, 0.47])).convert("RGBA")
                    a = 1.0 if i == 0 else zacht(tt / FADE)
                    if a < 1:
                        laag2 = laag.copy()
                        laag2.putalpha(laag.getchannel("A").point(lambda v, a=a: int(v * a)))
                        im.alpha_composite(laag2, (0, int(14 * (1 - a))))
                    else:
                        im.alpha_composite(laag)
                    plak_ondertitel(im, onders[i], t["scene_start"] + tt)
                    im = im.convert("RGB")
                else:
                    im = b_leeg.copy()
                    zm = (0.18 if (groot and i == 0) else 0.07) * zacht(k / max(1, n - 1))
                    plak_render(im, bron / b["render"], V["render"], zoom=1.0 + zm)
                    im = im.convert("RGBA")
                    a = 1.0 if i == 0 else zacht(tt / FADE)
                    if a < 1:
                        laag2 = laag.copy()
                        laag2.putalpha(laag.getchannel("A").point(lambda v, a=a: int(v * a)))
                        im.alpha_composite(laag2, (0, int(14 * (1 - a))))
                    else:
                        im.alpha_composite(laag)
                    plak_ondertitel(im, onders[i], t["scene_start"] + tt)
                    im = im.convert("RGB")
                enc.stdin.write(im.tobytes())
            vorige_u = [SW / 2, SH / 2, SW]
            continue
        d0 = delen[b["deel"]]
        eerste = d0 + b.get("van", 0)
        laatste = d0 + b["tot"] if "tot" in b else min(v for v in delen.values() if v > d0)
        S = laatste - eerste
        snel = min(1.5, max(0.4, S / n))
        if S / n > 1.5:
            print(f"let op: scène {i + 1} toont {int(n * 1.5)} van {S} bronbeelden")
        dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(bron / "opname-ruw.mkv"), "-vf",
                                f"trim=start_frame={eerste - 1}:end_frame={laatste - 1},setpts=PTS-STARTPTS",
                                "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL)
        sleutels = b["uitsnede"]
        huidig, gelezen, src = -1, 0, None
        laatste_klik = -99
        gezien_klik = set()
        nad = 0
        for k in range(n):
            tt = k / FPS
            want = min(S - 1, int(k * snel))
            while huidig < want:
                buf = dec.stdout.read(SW * SH * 3)
                if len(buf) < SW * SH * 3:
                    break
                src = buf
                huidig += 1
            bronbeeld = eerste + huidig
            m = muis[bronbeeld - 1] if 0 <= bronbeeld - 1 < len(muis) else None
            if m and m[2] and bronbeeld not in gezien_klik:
                gezien_klik.add(bronbeeld)
                laatste_klik = bronbeeld
                kliks.append(t["scene_start"] + tt)
            # uitsnede: eerst van de vorige naar de eerste sleutel (zoom), dan eventueel langzaam naar de tweede
            if tt < ZOOM:
                u = meng(vorige_u, sleutels[0], zacht(tt / ZOOM))
            elif len(sleutels) > 1:
                u = meng(sleutels[0], sleutels[1], zacht((tt - ZOOM) / max(0.01, n / FPS - ZOOM)))
            else:
                u = sleutels[0]
            r = rect_van(u, aspect)
            beeld = Image.frombuffer("RGB", (SW, SH), src, "raw", "RGB", 0, 1)
            inh = beeld.resize((cw, ch), Image.BICUBIC, box=r)
            sx = cw / (r[2] - r[0])
            d = ImageDraw.Draw(inh, "RGBA")
            if b.get("nadruk"):
                lo, hi = b.get("nadruk_bron", [0, 10 ** 9])
                nad = nad + 1 if lo <= bronbeeld <= hi else 0
                a = zacht(nad / 6) if i == 0 or tt >= ZOOM * 0.6 else 0.0
                if a > 0:
                    for (hx0, hy0, hx1, hy1) in b["nadruk"]:
                        p = [(hx0 - r[0]) * sx - 8, (hy0 - r[1]) * sx - 8, (hx1 - r[0]) * sx + 8, (hy1 - r[1]) * sx + 8]
                        d.rounded_rectangle(p, 12, fill=NADRUK + (int(38 * a),), outline=NADRUK + (int(255 * a),), width=5)
            if m:
                px, py = (m[0] - r[0]) * sx, (m[1] - r[1]) * sx
                if -10 < px < cw and -10 < py < ch:
                    j = bronbeeld - laatste_klik
                    if 0 <= j < len(KRINGEN):
                        kr = KRINGEN[j]
                        inh.paste(kr, (int(px - kr.width / 2), int(py - kr.height / 2)), kr)
                    inh.paste(PIJL, (int(px - 2), int(py - 2)), PIJL)
            im = b_scherm.copy()
            im.paste(inh, (cx0, cy0), hoek)
            if b.get("inzet"):
                ix0, iy0, ix1, iy1 = b["inzet"]
                kx0, konder, kx1 = V["inzet"]
                kw = kx1 - kx0
                kh = int(kw * (iy1 - iy0) / (ix1 - ix0))
                kaart = beeld.resize((kw, kh), Image.BICUBIC, box=(ix0, iy0, ix1, iy1))
                ky = konder - kh
                a = zacht((tt - 0.15) / 0.3)
                if i > 0 and script["scenes"][i - 1]["beeld"].get("inzet"):
                    a = 1.0
                if a > 0:
                    lg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                    schaduw(lg, (kx0, ky, kx1, konder), 18, 10, 22, 90)
                    msk = Image.new("L", (kw, kh), 0)
                    ImageDraw.Draw(msk).rounded_rectangle((0, 0, kw - 1, kh - 1), 16, fill=255)
                    lg.paste(kaart, (kx0, ky), msk)
                    ImageDraw.Draw(lg).rounded_rectangle((kx0 - 3, ky - 3, kx1 + 3, konder + 3), 18,
                                                         outline=(255, 255, 255, 255), width=5)
                    if a < 1:
                        lg.putalpha(lg.getchannel("A").point(lambda v, a=a: int(v * a)))
                    im = im.convert("RGBA")
                    im.alpha_composite(lg)
            im = im.convert("RGBA")
            a = 1.0 if i == 0 else zacht(tt / FADE)
            if a < 1:
                laag2 = laag.copy()
                laag2.putalpha(laag.getchannel("A").point(lambda v, a=a: int(v * a)))
                im.alpha_composite(laag2, (0, int(14 * (1 - a))))
            else:
                im.alpha_composite(laag)
            plak_ondertitel(im, onders[i], t["scene_start"] + tt)
            enc.stdin.write(im.convert("RGB").tobytes())
        dec.stdout.close()
        dec.wait()
        vorige_u = list(sleutels[-1])
        print(f"scène {i + 1}: {t['scene_start']:.2f} tot {t['scene_eind']:.2f} s, bron {eerste} tot {laatste}, snelheid {snel:.2f}")
    enc.stdin.close()
    enc.wait()

    # 3. geluid: stem boven een zachte eigen ondergrond
    SR = g.SR
    n_a = int(round(duur * SR))
    spraak = np.zeros(n_a, np.float32)
    for z, t in zip(zinnen, tl):
        x, sr = stem.lees_wav(z["wav"])
        x = np.interp(np.arange(int(len(x) * SR / sr)) * sr / SR, np.arange(len(x)), x).astype(np.float32)
        g.plak(spraak, t["stem_start"], x * 0.9)
    bed = g.bed_joints(duur).astype(np.float32)
    bed = bed / (np.abs(bed).max() + 1e-9)
    # ondergrond zacht onder de stem (ducking): -27 dB tijdens spraak, -20 dB in de pauzes
    act = np.zeros(n_a, np.float32)
    for t in tl:
        act[int(t["stem_start"] * SR):int(t["stem_eind"] * SR)] = 1
    k = int(0.25 * SR)
    act = np.convolve(act, np.ones(k) / k, mode="same")
    bed *= (10 ** (-20 / 20)) * (1 - act) + (10 ** (-27 / 20)) * act
    effect = np.zeros(n_a, np.float32)
    for kt in kliks:
        g.plak(effect, kt, g.klik() * 1.2)
    mix = spraak + bed + effect
    n_in, n_uit = int(0.05 * SR), int(1.2 * SR)
    mix[:n_in] *= np.linspace(0, 1, n_in)
    mix[-n_uit:] *= np.linspace(1, 0, n_uit)
    st = np.stack([mix, mix], axis=1)
    st = st / (np.abs(st).max() + 1e-9) * 0.8
    g.schrijf_wav(tmp / "mix.wav", st)
    naam = f"{script['naam']}-{vorm}"
    mp4 = uitmap / f"{naam}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(tmp / "stil.mp4"), "-i", str(tmp / "mix.wav"),
                    "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2", "-t", f"{duur:.3f}",
                    "-movflags", "+faststart", str(mp4)], check=True)

    # 4. script met tijden
    (uitmap / f"{naam}-script.json").write_text(json.dumps(
        {"film": mp4.name, "duur_s": round(duur, 2), "vorm": vorm, "stem": info, "pauze_s": PAUZE, "lead_s": LEAD,
         "kliks_s": [round(k, 2) for k in kliks], "zinnen": tl}, indent=1, ensure_ascii=False))

    def ts(x):
        return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(round((x % 1) * 1000)) % 1000:03d}"
    (uitmap / f"{naam}.srt").write_text("".join(
        f"{t['nr']}\n{ts(t['stem_start'])} --> {ts(t['stem_eind'])}\n{t['tekst']}\n\n" for t in tl))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp4), "-vf",
                    f"fps=8/{duur:.3f},scale={480 if vorm == 'liggend' else 270}:-1,tile=8x1", "-frames:v", "1",
                    str(uitmap / f"overzicht-{vorm}.jpg")], check=True)
    print(f"klaar: {mp4} {duur:.2f} s, stem {info['soort']} {info.get('stemnaam')}")


if __name__ == "__main__":
    main()
