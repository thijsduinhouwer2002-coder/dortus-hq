#!/usr/bin/env python3
"""YouTube Shorts reeks 3 (recept v2, opdracht hoofdchat 22 nov 2026 ±00:05 NL): 4 staande Shorts van 40 tot 60 s
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

# nr, naam: stukken [(deel, van, tot, traag, paneeldeel, tekst)]; tekst (regel1, regel2) staat vanaf het begin van
# dat stuk tot de volgende tekst (None: de vorige blijft staan). traag 2 = elk beeld twee keer (halve snelheid).
H = 75   # haak: 2,5 s eindresultaat
SHORTS = {
    (1, "make-poseable"): [
        ("held", 20, 20 + H, 1, "knie", ("Make your character", "poseable for 3D printing")),
        ("heel", 0, None, 1, "knop", ("1. Select your", "rigged character")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("2. Press", "Figure from rig")),
        ("lijst", 0, None, 1, "lijst", (f"{N_GEW} joints, each", "with its range")),
        ("knie", 0, None, 1, None, ("3. Bend the knee", "to its end stop")),
        ("knie_rood", 0, None, 1, "knie", ("Past the stop", "it turns red")),
        ("pose", 0, None, 1, "knie", ("Pose the rest", "of the figure")),
        ("uitelkaar", 0, None, 1, None, ("4. Exploded view:", "see the ball joints")),
        ("export", 0, None, 1, None, ("5. Export every part", "as 3MF")),
        ("held", 0, None, 1, "held", ("Ready to slice", "and test print")),
    ],
    (2, "knee-bend"): [
        ("held", 60, 60 + H, 1, "knie", ("How far can", "this knee bend?")),
        ("heel", 0, None, 1, "knop", ("A rig with", f"Limit Rotation {K_STOP}°")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("Press", "Figure from rig")),
        ("lijst", 0, 100, 2, "lijst", ("Left knee:", f"0 to {K_STOP}° from rig")),
        ("lijst", 100, None, 1, "lijst", ("Right knee:", "mirrored from the left")),
        ("knie", 0, None, 1, None, ("Bend it", "in the panel")),
        ("knie_rood", 0, None, 2, "knie", (f"It stops at {K_STOP}°,", "past that: red")),
        ("pose", 0, None, 1, "knie", ("Same check", "for every joint")),
        ("held", 0, None, 1, "held", ("Check the pose", "before you print")),
    ],
    (3, "posable-toy"): [
        ("held", 70, 70 + H, 1, "knie", ("Turn your rigged character", "into a posable toy")),
        ("heel", 0, None, 1, "knop", ("Start with", "a rigged figure")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("One button:", "Figure from rig")),
        ("lijst", 0, 60, 1, "lijst", ("Hinges at elbows", "and knees")),
        ("lijst", 60, 140, 1, "lijst", ("Ball joints at shoulders,", "hips and neck")),
        ("knie", 0, None, 1, None, ("Bend a knee", "to its end stop")),
        ("pose", 0, None, 2, "knie", ("Pose it", "right in Blender")),
        ("uitelkaar", 0, None, 2, None, ("Exploded view:", "the ball joint inside")),
        ("held", 0, None, 2, "held", ("Print a test joint", "first")),
    ],
    (4, "printable-parts"): [
        ("held", 105, 105 + H, 1, "knie", ("Your character as", "printable parts")),
        ("heel", 0, None, 1, "knop", ("Select the", "rigged figure")),
        ("kies", 0, None, 1, "knop", None),
        ("knop", 0, None, 2, "knop", ("Press", "Figure from rig")),
        ("lijst", 0, None, 1, "lijst", ("Cut into parts", f"with {N_GEW} joints")),
        ("pose", 0, None, 1, "knie", ("Each joint", "shows its range")),
        ("uitelkaar", 0, None, 2, None, ("Exploded view:", "ball and socket")),
        ("export", 0, None, 2, None, ("Pick 3MF,", "then Export")),
        ("held", 0, None, 2, "knie", (f"{N_EXPORT} files", "ready to slice")),
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
            teksten.append([s[5][0], s[5][1], round(t0, 2), 99])
    vf = [f"drawbox=x=0:y=965:w=1080:h=200:color=black@0.45:t=fill"]
    for r1, r2, a, b in teksten:
        vf += [dt(r1, 74, LICHT, 975, extra=tussen(a, b)), dt(r2, 74, GEEL, 1065, extra=tussen(a, b))]
    vf += [dt(PRINT, 28, GRIJS, 1880, GEW), dt("dortus.com/yt", 34, MINT, 1835, VET, extra=tussen(duur - 5, 99))]
    stil = TMP / f"{nr}-stil.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(rauw), "-vf", ",".join(vf) + ",format=yuv420p",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-an", str(stil)], check=True)
    duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(stil)], capture_output=True, text=True).stdout)
    buf = g.bed_joints(duur)
    for _r1, _r2, a, _b in teksten[1:]:
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
                              "teksten": [[r1, r2, a, b] for r1, r2, a, b in teksten],
                              "stukken": [list(s[:5]) for s in stukken]}
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp4), "-vf", f"fps=6/{duur:.3f},scale=270:-1,tile=6x1",
                    "-frames:v", "1", str(UIT / f"overzicht-{nr}.jpg")], check=True)
    print(f"klaar: {mp4.name} {duur:.1f} s")

(UIT / "metingen.json").write_text(json.dumps({"shorts": meting, "opname": MT}, indent=1, ensure_ascii=False))
