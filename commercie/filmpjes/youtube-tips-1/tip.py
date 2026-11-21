#!/usr/bin/env python3
"""Tip-Shorts reeks 1 (21 nov 2026, Chris, opdracht hoofdchat ±17:58 NL en Afkijker ±19:05 NL).
Vorm afgekeken van Malikose: de echte Blender-UI staand, kijkvenster boven, paneel van de add-on onder, één techniek
stap voor stap, 25 tot 45 s. Uit de echte opname in Blender 5.3.0 met Click Joints Pro 1.1 (opname-ruw.mkv uit
release youtube-pro-3, liggend 1920x1080, zijbalk op x 1527). Het script knipt, snijdt bij en zet tekst; bogen,
getallen, rood, knoppen en lijst komen van de add-on.
    python3 tip.py <map pro3> <uitmap>"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "geluid"))
import geluid as g  # noqa: E402
import numpy as np  # noqa: E402

BRON = Path(sys.argv[1])
UIT = Path(sys.argv[2])
UIT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
FILM = json.loads((BRON / "film.json").read_text())
MT = FILM.get("metingen", {})
FPS = 30
BG = "0x1D2027"
LICHT, GRIJS, MINT = "0xF1F3F7", "0xC9CDD8", "0x3BE6B0"

# Indeling 1080x1920: tekstband 0-230, kijkvenster 230-1150, paneel 1170-1672, voet 1700-1800.
KV = "crop=1100:937:420:60,scale=1080:920:flags=lanczos"
ZX, ZB, SCHAAL = 1535, 344, 2.6          # zijbalk: x, breedte zonder tabbladen, vergroting
PH = 193                                 # hoogte paneelstuk in opnamepixels (193*2.6 = 502)
# y van het paneelstuk in de opname (zijbalk begint op y 34), per stand van het paneel (zelf gemeten in zij5.jpg)
PANEEL = {"knop": 34 + 745, "lijst": 34 + 715, "scharnier": 34 + 335, "uitelkaar": 34 + 425, "export": 34 + 520}


def font(stijl):
    r = subprocess.run(["fc-match", "-f", "%{file}", f"Inter:style={stijl}"], capture_output=True, text=True)
    return r.stdout.strip() or "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


VET, GEW = font("Bold"), font("Regular")
n_tekst = [0]


def tf(tekst):
    n_tekst[0] += 1
    p = TMP / f"t{n_tekst[0]}.txt"
    p.write_text(tekst, encoding="utf-8")
    return str(p)


def dt(tekst, grootte, kleur, y, fnt=None, extra=""):
    return (f"drawtext=fontfile='{fnt or VET}':textfile='{tf(tekst)}':fontsize={grootte}:fontcolor={kleur}"
            f":x=(1080-text_w)/2:y={y}:shadowcolor=0x000000@0.75:shadowx=3:shadowy=3{extra}")


def ff(*a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)


def tussen(a, b):
    return f":enable='gte(t,{a})*lt(t,{b})'"


def deel_eind(deel):
    d = FILM["delen"]
    volg = sorted(d, key=lambda k: d[k])
    i = volg.index(deel)
    return d[volg[i + 1]] if i + 1 < len(volg) else FILM["n"] + 1


K_STOP = int(round(MT.get("knie_stop", 120)))
N_GEW = MT.get("gewrichten", 9)
N_DELEN = len(MT.get("export", {}).get("bestanden", [])) or 10
PRINT = "Measured in Blender, not print tested by us yet."

# naam: (stukken [(deel, van, tot, paneel, traag)], teksten [(regel1, regel2, a, b)], klanken)
TIPS = {
    (1, "split-printable-parts"): (
        [("rig", 120, None, "knop", 1.0), ("druk", 0, None, "knop", 1.5), ("lijst", 0, None, "lijst", 1.0),
         ("uitelkaar", 30, None, "uitelkaar", 1.0), ("export", 0, None, "export", 1.2)],
        [("Split a figure into", "printable parts", 0, 3.2),
         ("1. Rigged figure:", "click Figure from rig", 3.2, 6.5),
         (f"2. {N_GEW} joints cut in:", "hinges and ball joints", 6.5, 13.0),
         ("3. Exploded view:", "check every part", 13.0, 24.5),
         (f"4. Export 3MF:", f"{N_DELEN} parts, one file each", 24.5, 99)],
        [("klik", 4.6), ("zoef", 13.2, 1.4), ("klik", 26.0)]),
    (2, "check-bend-before-print"): (
        [("bogen", 0, None, "lijst", 1.0), ("buig", 0, None, "scharnier", 1.2),
         ("rood", 0, None, "scharnier", 1.4), ("terug", 0, None, "scharnier", 1.3)],
        [("Check if a joint bends", "too far before you print", 0, 3.4),
         ("1. Every joint shows", "its range in degrees", 3.4, 10.0),
         ("2. Show bend range,", f"drag Bend to {K_STOP}°", 10.0, 19.2),
         (f"3. Past {K_STOP}°:", "the arc turns red", 19.2, 26.2),
         ("4. Back inside the stop:", "red is gone", 26.2, 99)],
        [("buig", 10.2, 8.5), ("zoef", 19.3, 1.4), ("klik", 26.3)]),
}

meting = {}
for (nr, naam), (stukken, boven, klanken) in TIPS.items():
    delen = []
    for i, (deel, van, tot, paneel, traag) in enumerate(stukken):
        d0 = FILM["delen"][deel]
        eerste = d0 + van
        laatste = min(deel_eind(deel), d0 + tot) if tot is not None else deel_eind(deel)
        py = PANEEL[paneel]
        pw, ph = int(ZB * SCHAAL), int(PH * SCHAAL)
        fc = (f"[0:v]trim=start_frame={eerste - 1}:end_frame={laatste - 1},setpts=PTS-STARTPTS,split[a][b];"
              f"[a]{KV}[kv];[b]crop={ZB}:{PH}:{ZX}:{py},scale={pw}:{ph}:flags=lanczos[pa];"
              f"color=c={BG}:s=1080x1920:r={FPS}[bg];[bg][kv]overlay=0:230:shortest=1[t1];"
              f"[t1][pa]overlay={(1080 - pw) // 2}:1170,drawbox=x={(1080 - pw) // 2 - 3}:y=1167:w={pw + 6}:h={ph + 6}"
              f":color=0x3A3F4B:t=3,setpts={traag}*(PTS-STARTPTS),fps={FPS},format=yuv420p[v]")
        uit = TMP / f"{nr}-{i}.mp4"
        ff("-i", str(BRON / "opname-ruw.mkv"), "-filter_complex", fc, "-map", "[v]",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", str(uit))
        delen.append(uit)
    lijst = TMP / f"{nr}.txt"
    lijst.write_text("".join(f"file '{p}'\n" for p in delen))
    rauw = TMP / f"{nr}-rauw.mp4"
    ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c", "copy", str(rauw))
    vf = []
    for r1, r2, a, b in boven:
        vf += [dt(r1, 66, LICHT, 50, extra=tussen(a, b)), dt(r2, 60, MINT, 134, extra=tussen(a, b))]
    vf += [dt("Blender 5.3 + Click Joints Pro", 34, GRIJS, 1702, GEW), dt(PRINT, 28, GRIJS, 1752, GEW)]
    stil = TMP / f"{nr}-stil.mp4"
    ff("-i", str(rauw), "-vf", ",".join(vf) + ",format=yuv420p", "-c:v", "libx264", "-preset", "medium",
       "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", str(stil))
    duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(stil)], capture_output=True, text=True).stdout)
    buf = g.bed_joints(duur)
    g.plak(buf, 0.05, g.tik())
    for _r1, _r2, a, _b in boven[1:]:
        if a < duur:
            g.plak(buf, a, g.tik())
    for k in klanken:
        if k[1] >= duur:
            continue
        if k[0] == "klik":
            g.plak(buf, k[1], g.klik())
        elif k[0] == "buig":
            g.plak(buf, k[1], g.buig(min(k[2], duur - k[1])))
        elif k[0] == "zoef":
            g.plak(buf, k[1], g.zoef(min(k[2], duur - k[1])))
    n_in, n_uit = int(0.05 * g.SR), int(0.8 * g.SR)
    buf[:n_in] *= np.linspace(0, 1, n_in)
    buf[-n_uit:] *= np.linspace(1, 0, n_uit)
    st = np.stack([buf, np.concatenate([np.zeros(12), buf[:-12]])], axis=1)
    st = st / (np.abs(st).max() + 1e-9) * 0.7
    wav = TMP / f"{nr}.wav"
    g.schrijf_wav(wav, st)
    mp4 = UIT / f"tip-{nr}-{naam}-geluid.mp4"
    ff("-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
       "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
       "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4))
    meting[f"{nr}-{naam}"] = {"duur_s": round(duur, 2), "teksten": [list(t) for t in boven],
                              "stukken": [list(s) for s in stukken]}
    ff("-i", str(mp4), "-vf", f"fps=6/{duur:.3f},scale=270:-1,tile=6x1", "-frames:v", "1",
       str(UIT / f"overzicht-tip-{nr}.jpg"))
    print(f"klaar: {mp4.name} {duur:.1f} s")

(UIT / "metingen.json").write_text(json.dumps({"tips": meting, "pro3": MT}, indent=1))
