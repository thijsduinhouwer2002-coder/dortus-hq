#!/usr/bin/env python3
"""YouTube Shorts reeks 4 (recept v2, herstel na keuring reeks 3, opdracht hoofdchat 22 nov ±01:25 NL): 3 staande Shorts
van 40 tot 60 s, elk met een eigen eerste beeld: een render uit de opname (render-N.png, EEVEE door de camera, wat de
3D-weergave laat zien) met een langzame zoom. Basis reeks 3 (opdracht hoofdchat 22 nov 2026 ±00:05 NL):
uit één echte opname in Blender 5.3.0 met Click Joints Pro 1.1.0 (opname.py, breed X-scherm 2160x1920).
    python3 kort.py <map met opname-ruw.mkv en film.json> <uitmap>
Per beeld: boven de echte 3D-weergave met menubalk (links 1080x1180 van het scherm), onder het echte paneel van Click
Joints (1080x740 uit de zijbalk, hoogte per deel waar de knop of schuif staat). De muis: een pijltje op de plek die
opname.py per beeld opschreef (de X-schermafbeelding toont de muis niet), met een kringetje bij een klik.
Eerste beeld van elke Short = het eindresultaat (figuur in pose of uit elkaar). Grote ondertitels (3 tot 6 woorden)
met ffmpeg drawtext; geluid met commercie/filmpjes/geluid/geluid.py (met code gemaakt, geen stem, geen muziek).
Het script kleurt niets in de opname. Uit: short-<nr>-<naam>-geluid.mp4, overzicht-<nr>.jpg, metingen.json."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "geluid"))
import geluid as g  # noqa: E402

BRON = Path(sys.argv[1])
UIT = Path(sys.argv[2])
UIT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
FILM = json.loads((BRON / "film.json").read_text())
MT = FILM.get("metingen", {})
FPS = 30
SW, SH = 2160, 1920          # X-scherm van de opname
BOVEN_H, ONDER_H = 1180, 740  # weergave boven, paneel onder
ZB = (FILM.get("vlakken", {}).get("heel", {}).get("zijbalk") or [1078, 107, 1082, 1768])
LICHT, MINT, GEEL, GRIJS = "0xFFFFFF", "0x3BE6B0", "0xFFD23F", "0xC9CDD8"
PRINT = "Measured in Blender, not print tested by us yet."


def font(stijl):
    r = subprocess.run(["fc-match", "-f", "%{file}", f"Inter:style={stijl}"], capture_output=True, text=True)
    return r.stdout.strip() or "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


VET, GEW = font("ExtraBold"), font("Regular")
n_tekst = [0]


def tf(tekst):
    n_tekst[0] += 1
    p = TMP / f"t{n_tekst[0]}.txt"
    p.write_text(tekst, encoding="utf-8")
    return str(p)


def dt(tekst, grootte, kleur, y, fnt=None, extra=""):
    return (f"drawtext=fontfile='{fnt or VET}':textfile='{tf(tekst)}':fontsize={grootte}:fontcolor={kleur}"
            f":x=(1080-text_w)/2:y={y}:borderw=6:bordercolor=0x000000@0.85{extra}")


def tussen(a, b):
    return f":enable='gte(t,{a})*lt(t,{b})'"


def deel_eind(deel):
    d = FILM["delen"]
    volg = sorted(d, key=lambda k: d[k])
    i = volg.index(deel)
    return d[volg[i + 1]] if i + 1 < len(volg) else FILM["n"] + 1


# ---------- muis ----------

def pijl(schaal=2.2):
    """Gewone muispijl (wit met zwarte rand) als RGBA-array."""
    pts = [(0, 0), (0, 17), (4, 13), (7, 20), (10, 19), (7, 12), (12, 12)]
    from PIL import Image, ImageDraw
    n = int(24 * schaal)
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    p = [(x * schaal + 2, y * schaal + 2) for x, y in pts]
    d.polygon(p, fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    d.line(p + [p[0]], fill=(0, 0, 0, 255), width=3)
    return np.asarray(im).astype(np.float32) / 255.0


def kring(r):
    from PIL import Image, ImageDraw
    n = 2 * r + 8
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse((4, 4, n - 4, n - 4), outline=(255, 210, 63, 230), width=6)
    return np.asarray(im).astype(np.float32) / 255.0


PIJL = pijl()
KRINGEN = [kring(r) for r in range(14, 62, 6)]   # 8 beelden na een klik


def plak_rgba(doel, spr, x, y):
    h, w = spr.shape[:2]
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(doel.shape[1], x + w), min(doel.shape[0], y + h)
    if x0 >= x1 or y0 >= y1:
        return
    s = spr[y0 - y:y1 - y, x0 - x:x1 - x]
    a = s[..., 3:4]
    vak = doel[y0:y1, x0:x1].astype(np.float32)
    doel[y0:y1, x0:x1] = (vak * (1 - a) + s[..., :3] * 255.0 * a).astype(np.uint8)


def naar_short(mx, my, py):
    """X-schermpunt naar punt in de Short, of None als het buiten beide uitsneden valt."""
    if mx < 1080 and my < BOVEN_H:
        return mx, my
    if ZB[0] + 1 <= mx < ZB[0] + 1 + 1080 and py <= my < py + ONDER_H:
        return mx - (ZB[0] + 1), my - py + BOVEN_H
    return None


def paneel_y(deel):
    y = FILM.get("paneel_y", {}).get(deel)
    if y is None:
        return ZB[1]
    return int(max(ZB[1], min(SH - ONDER_H, y - 180)))


# ---------- in elkaar zetten ----------

def achtergrond():
    y = np.linspace(0, 1, 1920)[:, None, None]
    boven, onder = np.array([0xF1, 0xF5, 0xFB], np.float32), np.array([0xD5, 0xDF, 0xEC], np.float32)
    return np.broadcast_to(boven * (1 - y) + onder * y, (1920, 1080, 3)).astype(np.float32)


def render_beelden(pad, n):
    """n beelden 1080x1920: de render (RGBA) op de achtergrond, zoom van 1,00 naar 1,06 rond het figuur."""
    from PIL import Image
    im = Image.open(pad).convert("RGBA")
    if im.size != (1080, 1920):
        im = im.resize((1080, 1920), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255.0
    if pad.name == "render-3.png":   # dichtbij: de benen lopen door tot onderaan; zacht laten vervagen boven de ondertitel
        a = a.copy()
        y = np.arange(1920)[:, None]
        a[..., 3] *= np.clip((1250 - y) / 200.0, 0.0, 1.0)
    vol = (achtergrond() * (1 - a[..., 3:4]) + a[..., :3] * 255.0 * a[..., 3:4]).astype(np.uint8)
    basis = Image.fromarray(vol)
    cx, cy = 540, 1920 * 0.31
    for i in range(n):
        z = 1.0 + 0.06 * i / max(1, n - 1)
        b, h = 1080 / z, 1920 / z
        x0, y0 = cx - b / 2, cy - h * 0.31
        yield np.asarray(basis.resize((1080, 1920), Image.BICUBIC, box=(x0, y0, x0 + b, y0 + h)))


def stukken_naar_video(nr, stukken, uit):
    """stukken: [(deel, van, tot, traag, paneel_deel)] -> stille mp4 1080x1920 met muis. Geeft klikmomenten (s)."""
    enc = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                            "-pix_fmt", "yuv420p", str(uit)], stdin=subprocess.PIPE)
    muis = FILM.get("muis", [])
    kliks, t_uit = [], 0
    begin = []
    for deel, van, tot, traag, pdeel, _tekst in stukken:
        begin.append(t_uit / FPS)
        if deel.startswith("@"):   # stilstaande render met een langzame zoom, op een effen achtergrond
            for o in render_beelden(BRON / deel[1:], tot - van):
                enc.stdin.write(o.tobytes())
                t_uit += 1
            continue
        d0 = FILM["delen"][deel]
        eerste = d0 + van
        laatste = min(deel_eind(deel), d0 + tot) if tot is not None else deel_eind(deel)
        py0 = paneel_y(pdeel or deel)
        # in deel knie is het hoofdpaneel eerst dicht: bovenaan tot de klik op de kop (eerste klik in de zijbalk)
        wissel = 0
        if deel == "knie":
            wissel = next((i + 1 for i in range(d0 - 1, min(len(muis), deel_eind(deel) - 1))
                           if muis[i][2] and muis[i][0] >= ZB[0]), 0) + 14
        dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(BRON / "opname-ruw.mkv"), "-vf",
                                f"trim=start_frame={eerste - 1}:end_frame={laatste - 1},setpts=PTS-STARTPTS",
                                "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        n = eerste
        laatste_klik = -99
        while True:
            buf = dec.stdout.read(SW * SH * 3)
            if len(buf) < SW * SH * 3:
                break
            src = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3)
            py = ZB[1] if n < wissel else py0
            out = np.empty((1920, 1080, 3), np.uint8)
            out[:BOVEN_H] = src[:BOVEN_H, :1080]
            out[BOVEN_H:] = src[py:py + ONDER_H, ZB[0] + 1:ZB[0] + 1 + 1080]
            out[BOVEN_H - 3:BOVEN_H + 3] = (59, 230, 176)
            m = muis[n - 1] if 0 <= n - 1 < len(muis) else None
            if m and m[2]:
                laatste_klik = n
            herhaal = max(1, int(round(traag)))
            for k in range(herhaal):
                o = out.copy() if herhaal > 1 else out
                if m:
                    p = naar_short(m[0], m[1], py)
                    if p:
                        i = n - laatste_klik
                        if 0 <= i < len(KRINGEN):
                            kr = KRINGEN[i]
                            plak_rgba(o, kr, p[0] - kr.shape[1] // 2, p[1] - kr.shape[0] // 2)
                        plak_rgba(o, PIJL, p[0] - 2, p[1] - 2)
                if m and m[2] and k == 0:
                    kliks.append(t_uit / FPS)
                enc.stdin.write(o.tobytes())
                t_uit += 1
            n += 1
        dec.wait()
    enc.stdin.close()
    enc.wait()
    return kliks, t_uit / FPS, begin


K_STOP = int(round(MT.get("knie_stop", 120)))
N_GEW = MT.get("gewrichten", 9)
N_EXPORT = len([b for b in MT.get("export", []) if b.endswith(".3mf")]) or 10

# nr, naam: stukken [(deel, van, tot, traag, paneeldeel, tekst)]; deel "@render-N.png" = stilstaande render (van..tot =
# aantal beelden). tekst (regel1, regel2[, y]) staat vanaf het begin van dat stuk tot de volgende tekst (None: de vorige
# blijft). traag 2 = elk beeld twee keer (halve snelheid).
H = 90    # eerste beeld: 3 s render
YH = 1280  # ondertitel onder de render (niets van het figuur erachter)
VOORBIJ = int(round(MT.get("knie_pose_rood", K_STOP + 12) - K_STOP))
SHORTS = {
    (1, "make-poseable"): [
        ("@render-1.png", 0, H, 1, None, ("Make your character", "poseable for 3D printing", YH)),
        ("heel", 0, None, 1, "knop", ("1. Select your", "rigged character")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("2. Press", "Figure from rig")),
        ("lijst", 0, None, 1, "lijst", (f"{N_GEW} joints, each", "with its range")),
        ("knie", 0, None, 1, None, ("3. Bend the knee", "to its end stop")),
        ("knie_stop", 0, None, 1, "knie", None),
        ("knie_rood", 0, 96, 1, "knie", ("Past the stop: red arc", f"and +{VOORBIJ}° past limit")),
        ("knie_rood", 96, None, 1, "knie", None),
        ("pose", 0, None, 1, "knie", ("Pose the rest", "of the figure")),
        ("uitelkaar", 0, 168, 1, None, ("4. Exploded view:", "see the ball joints")),
        ("export", 0, None, 1, None, ("5. Export every part", "as 3MF")),
        ("held", 0, 120, 1, "held", ("Print a test joint", "first")),
    ],
    (2, "knee-bend"): [
        ("@render-2.png", 0, H, 1, None, ("How far can", "this knee bend?", YH)),
        ("heel", 0, None, 2, "knop", ("Our rig: knee limit", f"{K_STOP}° (Limit Rotation)")),
        ("kies", 0, None, 2, "knop", None),
        ("knop", 0, None, 2, "knop", ("Press", "Figure from rig")),
        ("lijst", 0, 100, 2, "lijst", ("Left knee:", f"0 to {K_STOP}° from rig")),
        ("lijst", 100, None, 2, "lijst", ("Right knee:", "mirrored from the left")),
        ("knie", 0, None, 1, None, ("Bend it with", "the Bend slider")),
        ("knie_stop", 0, None, 2, "knie", (f"Slider at {K_STOP}°:", "the end stop")),
        ("knie_rood", 0, 96, 2, "knie", (f"Past {K_STOP}°: red arc", f"and +{VOORBIJ}° past limit")),
        ("knie_rood", 96, None, 2, "knie", ("Check every joint", "before you print")),
    ],
    (3, "printable-parts"): [
        ("@render-3.png", 0, H, 1, None, ("Your character as", "printable parts", YH)),
        ("heel", 0, None, 1, "knop", ("Select the", "rigged figure")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("Press", "Figure from rig")),
        ("lijst", 0, 100, 1, "lijst", ("Cut into parts", f"with {N_GEW} joints")),
        ("uitelkaar", 0, 168, 2, None, ("Exploded view:", "ball and socket")),
        ("uitelkaar", 168, None, 2, None, ("Same at", "the hip")),
        ("export", 0, None, 2, None, ("Pick 3MF,", "then Export")),
        ("@render-4.png", 0, 105, 1, None, ("One 3MF file", "per part", YH)),
    ],
}

meting = {}
for (nr, naam), stukken in SHORTS.items():
    rauw = TMP / f"{nr}-rauw.mp4"
    kliks, duur, begin = stukken_naar_video(nr, stukken, rauw)
    teksten = []
    for s, t0 in zip(stukken, begin):
        if s[5] is not None:
            if teksten:
                teksten[-1][3] = round(t0, 2)
            teksten.append([s[5][0], s[5][1], round(t0, 2), 99, s[5][2] if len(s[5]) > 2 else 935])
    vf = []
    for r1, r2, a, b, y in teksten:
        vf += [f"drawbox=x=0:y={y - 10}:w=1080:h=200:color=black@0.45:t=fill:enable='gte(t,{a})*lt(t,{b})'",
               dt(r1, 74, LICHT, y, extra=tussen(a, b)), dt(r2, 74, GEEL, y + 90, extra=tussen(a, b))]
    # printzin en meetadres boven de onderste 15% (daar legt de Shorts-speler titel en kanaal overheen). Bij het scherm
    # staat de printzin in de strook net boven het paneel (niet over de Bend-schuif), bij een render onder de ondertitel.
    eind = begin[1:] + [duur]
    rr = [(round(b0, 2), round(e0, 2)) for s, b0, e0 in zip(stukken, begin, eind) if s[0].startswith("@")]
    bij_render = "+".join(f"between(t,{a},{b - 0.001})" for a, b in rr) or "0"
    vf += [f"drawbox=x=0:y=1135:w=1080:h=44:color=black@0.55:t=fill:enable='not({bij_render})'",
           dt(PRINT, 30, LICHT, 1142, GEW, extra=f":enable='not({bij_render})'"),
           f"drawbox=x=0:y=1550:w=1080:h=44:color=black@0.55:t=fill:enable='{bij_render}'",
           dt(PRINT, 30, LICHT, 1557, GEW, extra=f":enable='{bij_render}'"),
           f"drawbox=x=0:y=1480:w=1080:h=56:color=black@0.55:t=fill:enable='gte(t,{duur - 5})'",
           dt("dortus.com/yt", 42, MINT, 1486, VET, extra=tussen(duur - 5, 99))]
    stil = TMP / f"{nr}-stil.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(rauw), "-vf", ",".join(vf) + ",format=yuv420p",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-an", str(stil)], check=True)
    duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(stil)], capture_output=True, text=True).stdout)
    buf = g.bed_joints(duur)
    for _r1, _r2, a, _b, _y in teksten[1:]:
        if a < duur:
            g.plak(buf, a, g.tik())
    for k in kliks:
        g.plak(buf, k, g.klik())
    n_in, n_uit = int(0.05 * g.SR), int(1.0 * g.SR)
    buf[:n_in] *= np.linspace(0, 1, n_in)
    buf[-n_uit:] *= np.linspace(1, 0, n_uit)
    st = np.stack([buf, np.concatenate([np.zeros(12), buf[:-12]])], axis=1)
    st = st / (np.abs(st).max() + 1e-9) * 0.7
    wav = TMP / f"{nr}.wav"
    g.schrijf_wav(wav, st)
    mp4 = UIT / f"short-{nr}-{naam}-geluid.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac",
                    "-b:a", "160k", "-ac", "2", "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4)], check=True)
    meting[f"{nr}-{naam}"] = {"duur_s": round(duur, 2), "kliks_s": [round(k, 2) for k in kliks],
                              "teksten": [[r1, r2, a, b] for r1, r2, a, b, _y in teksten],
                              "stukken": [list(s[:5]) for s in stukken]}
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp4), "-vf", f"fps=6/{duur:.3f},scale=270:-1,tile=6x1",
                    "-frames:v", "1", str(UIT / f"overzicht-{nr}.jpg")], check=True)
    print(f"klaar: {mp4.name} {duur:.1f} s")

(UIT / "metingen.json").write_text(json.dumps({"shorts": meting, "opname": MT}, indent=1, ensure_ascii=False))
