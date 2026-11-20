#!/usr/bin/env python3
"""Twee staande filmpjes (TikTok, 1080x1920, 10 tot 20 s) uit de opname van opname.py (20 nov 2026, opdracht
hoofdchat 14:45 NL). Bouwt voort op commercie/filmpjes/youtube-pro/kort_figuur.py (Chris).
    python3 kort.py <map met opname-ruw.mkv en film.json> <uitmap>
Beeld: het kijkvenster van de echte Blender (vierkant 1080x1080 uit het scherm) in het midden, haak boven vanaf de
eerste seconde, dortus.com/tt en "Measured in Blender, not print tested by us yet." onder, binnen de veilige zone van
TikTok (niets belangrijks in de onderste 300 px en de rechter 140 px). Het script kleurt niets.
Geluid: functies uit commercie/filmpjes/geluid/geluid.py.
Uit: click-joints-pro-tt-<naam>-geluid.mp4 per filmpje en tt-overzicht.jpg (4 beelden per filmpje)."""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "geluid"))
import geluid as g  # noqa: E402
import numpy as np  # noqa: E402

IN, UIT = Path(sys.argv[1]), Path(sys.argv[2])
UIT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
film = json.loads((IN / "film.json").read_text())
FPS, D, MT = film["fps"], film["delen"], film.get("metingen", {})
VOLG = sorted(D, key=lambda k: D[k])
BG, LICHT, GRIJS, MINT = "0x23262D", "0xF1F3F7", "0xC9CDD8", "0x3BE6B0"
KX = int(os.environ.get("KORT_KX", "500"))   # vierkant van 960 px uit het scherm (x 500 tot 1460, y 40 tot 1000), zonder menubalk en zijbalk, vergroot naar 1080
STOP = int(round(MT.get("knie_stop", 120)))
N_GEW = MT.get("gewrichten", 9)


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
            f":x=(940-text_w)/2+20:y={y}{extra}")


def ff(*a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)


def deel_eind(deel):
    i = VOLG.index(deel)
    return D[VOLG[i + 1]] if i + 1 < len(VOLG) else film["n"] + 1


def tussen(a, b):
    return f":enable='between(t,{a},{b})'"


# naam: (stukken [(deel, van, tot, vertraging)], boventeksten [(regel1, regel2, a, b)], geluid)
FILMPJES = {
    "rig-naar-figuur": (
        [("rig", 120, None, 1.0), ("druk", 0, None, 1.0), ("lijst", 0, 30, 1.0), ("bogen", 0, 300, 1.0)],
        [("One button:", "rig to printable figure", 0, 4.4),
         (f"{N_GEW} joints, each with", "its range in degrees", 4.4, 99)],
        [("klik", 3.5)]),
    "knie-stop": (
        [("druk", 15, None, 1.0), ("lijst", 0, 30, 1.0), ("buig", 20, None, 1.0), ("rood", 0, None, 1.0)],
        [("One button:", "rig to printable figure", 0, 2.0),
         ("Bend the knee:", f"it stops at {STOP}°", 2.0, 9.0),
         (f"Past {STOP}°", "the arc turns red", 9.0, 99)],
        [("klik", 1.0), ("buig", 2.0, 5.0), ("klik", 7.0), ("zoef", 9.1, 1.5)]),
}
ONDER = [("dortus.com/tt", 64, MINT, 1430, VET), ("Click Joints Pro for Blender", 40, LICHT, 1515, GEW),
         ("Measured in Blender, not print tested by us yet.", 30, GRIJS, 1570, GEW)]

meting, plaatjes = {}, []
for naam, (stukken, boven, klanken) in FILMPJES.items():
    delen = []
    for i, (deel, van, tot, traag) in enumerate(stukken):
        eerste = D[deel] + van
        laatste = min(deel_eind(deel), D[deel] + tot) if tot is not None else deel_eind(deel)
        uit = TMP / f"{naam}{i}.mp4"
        ff("-i", str(IN / "opname-ruw.mkv"),
           "-vf", f"trim=start_frame={eerste - 1}:end_frame={laatste - 1},crop=960:960:{KX}:40,scale=1080:1080:flags=lanczos,"
                  f"setpts={traag}*(PTS-STARTPTS),fps={FPS},format=yuv420p",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", str(uit))
        delen.append(uit)
    lijst = TMP / f"{naam}.txt"
    lijst.write_text("".join(f"file '{p}'\n" for p in delen))
    vierkant = TMP / f"{naam}-vk.mp4"
    ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c", "copy", str(vierkant))
    vf = [f"pad=1080:1920:0:300:color={BG}"]
    for r1, r2, a, b in boven:
        vf += [dt(r1, 66, LICHT, 100, extra=tussen(a, b)), dt(r2, 60, MINT, 190, extra=tussen(a, b))]
    vf += [dt(t, s, c, y, f) for t, s, c, y, f in ONDER]
    stil = TMP / f"{naam}-stil.mp4"
    ff("-i", str(vierkant), "-vf", ",".join(vf) + ",format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
       "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", str(stil))
    duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(stil)], capture_output=True, text=True).stdout)
    buf = g.bed_joints(duur)
    g.plak(buf, 0.05, g.tik())
    for _r1, _r2, a, _b in boven[1:]:
        g.plak(buf, a, g.tik())
    for k in klanken:
        if k[0] == "klik":
            g.plak(buf, k[1], g.klik())
        elif k[0] == "buig":
            g.plak(buf, k[1], g.buig(k[2]))
        elif k[0] == "zoef":
            g.plak(buf, k[1], g.zoef(k[2]))
    n_in, n_uit = int(0.1 * g.SR), int(1.0 * g.SR)
    buf[:n_in] *= np.linspace(0, 1, n_in)
    buf[-n_uit:] *= np.linspace(1, 0, n_uit)
    st = np.stack([buf, np.concatenate([np.zeros(12), buf[:-12]])], axis=1)
    st = st / (np.abs(st).max() + 1e-9) * 0.7
    wav = TMP / f"{naam}.wav"
    g.schrijf_wav(wav, st)
    mp4 = UIT / f"click-joints-pro-tt-{naam}-geluid.mp4"
    ff("-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
       "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
       "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4))
    meting[naam] = round(duur, 2)
    p = TMP / f"{naam}-ov.jpg"
    ff("-i", str(mp4), "-vf", f"fps=4/{duur:.3f},scale=270:-1,tile=4x1", "-frames:v", "1", str(p))
    plaatjes.append(p)
    print(f"klaar: {mp4.name} {duur:.1f} s")

ff(*sum((["-i", str(p)] for p in plaatjes), []), "-filter_complex",
   "".join(f"[{i}:v]" for i in range(len(plaatjes))) + f"vstack=inputs={len(plaatjes)}",
   str(UIT / "tt-overzicht.jpg"))
(UIT / "tt-metingen.json").write_text(json.dumps({"duur_s": meting}, indent=1))
