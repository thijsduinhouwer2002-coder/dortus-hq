#!/usr/bin/env python3
"""YouTube Shorts reeks 2 (21 nov 2026, Chris, vaste aanvoer voor de Shorts-motor, opdracht hoofdchat ±12:50 NL):
3 nieuwe staande filmpjes (1080x1920) uit dezelfde echte opnames in Blender 5.3.0 als reeks 1, met andere stukken
of een andere belofte (varianten zoals Cleave doet). Kopie van youtube-shorts-1/kort.py; alleen SHORTS verschilt,
zodat reeks 1 niet opnieuw draait.
    python3 kort.py <map pro3> <map pro> <map gratis> <uitmap>
De mappen bevatten opname-ruw.mkv en film.json uit de releases youtube-pro-3 en youtube-shorts-1."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "geluid"))
import geluid as g  # noqa: E402
import numpy as np  # noqa: E402

BRON = {"pro3": Path(sys.argv[1]), "pro": Path(sys.argv[2]), "gratis": Path(sys.argv[3])}
UIT = Path(sys.argv[4])
UIT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
FILM = {k: json.loads((p / "film.json").read_text()) for k, p in BRON.items()}
FPS = 30
BG, BOVEN, ONDER = "0x23262D", "0x2B2F38", "0x1D2027"
LICHT, GRIJS, MINT, ROOD = "0xF1F3F7", "0xC9CDD8", "0x3BE6B0", "0xFF6B6B"


def mt(bron, sleutel, terug):
    return FILM[bron].get("metingen", {}).get(sleutel, terug)


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


def dt(tekst, grootte, kleur, y, fnt=None, extra="", schaduw=True):
    s = ":shadowcolor=0x000000@0.75:shadowx=3:shadowy=3" if schaduw else ""
    return (f"drawtext=fontfile='{fnt or VET}':textfile='{tf(tekst)}':fontsize={grootte}:fontcolor={kleur}"
            f":x=(1080-text_w)/2:y={y}{s}{extra}")


def ff(*a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)


def tussen(a, b):
    return f":enable='gte(t,{a})*lt(t,{b})'"   # eind niet meegerekend: nooit twee teksten tegelijk op de grens


def deel_eind(bron, deel):
    d = FILM[bron]["delen"]
    volg = sorted(d, key=lambda k: d[k])
    i = volg.index(deel)
    return d[volg[i + 1]] if i + 1 < len(volg) else FILM[bron]["n"] + 1


# Beeldvormen: van een opnamebeeld naar 1080x1920
VORM = {
    # staande opname: kop (menubalk) en statusbalk eraf, iets vergroot, over het hele scherm
    "staand": "crop=1080:1840:0:48,scale=1127:1920:flags=lanczos,crop=1080:1920:23:0",
    # liggende opname (youtube-pro-3): kijkvenster zonder menubalk en zijbalk, 1:1, met de verloopkleuren erom
    "breed": f"crop=1080:1014:420:36,pad=1080:1920:0:330:color={BOVEN},drawbox=x=0:y=1344:w=1080:h=576:color={ONDER}:t=fill",
    # liggende opname, dichtbij de rechterknie (knie, boog, getal en rood)
    "knie": f"crop=600:600:560:378,scale=1080:1080:flags=lanczos,pad=1080:1920:0:330:color={BOVEN},"
            f"drawbox=x=0:y=1410:w=1080:h=510:color={ONDER}:t=fill",
    # liggende opname: de lijst met gewrichten uit de echte zijbalk, 3 keer vergroot
    "lijst": f"crop=360:300:1532:740,scale=1080:900:flags=lanczos,pad=1080:1920:0:420:color={BG}",
}

PRINT = "Measured in Blender, not print tested by us yet."
ONDER_PRO = [("dortus.com/yt", 64, MINT, 1372, VET), ("Click Joints Pro for Blender", 40, LICHT, 1452, GEW),
             (PRINT, 30, GRIJS, 1505, GEW)]
ONDER_GRATIS = [("Free: Click Joints on extensions.blender.org", 40, MINT, 1380, VET),
                ("More (hinges with end stops): dortus.com/yt", 34, LICHT, 1440, GEW), (PRINT, 30, GRIJS, 1490, GEW)]

E_STOP = int(round(mt("pro", "elleboog_stop", 140)))
E_VOORBIJ = int(round(mt("pro", "elleboog_pose_rood", E_STOP + 12) - E_STOP))
K_STOP = int(round(mt("pro3", "knie_stop", 120)))
S_GRENS = int(mt("pro", "schouder_grens", 20))
N_GRENS = int(mt("gratis", "nek_grens", 20))
N_EXPORT = len(mt("pro3", "export", {}).get("bestanden", [])) or 10
N_GEW = mt("pro3", "gewrichten", 9)
FIT = {"groen": "Green ring: good fit", "geel": "Yellow ring: tight fit", "oranje": "Yellow ring: tight fit"}.get(
    mt("gratis", "passing", "groen"), "Ring shows the fit")

# nr, naam: (stukken [(bron, deel, van, tot, vorm, traag)], teksten [(regel1, regel2, a, b)], klanken, onder)
SHORTS = {
    (9, "rig-to-poseable"): (
        [("pro", "heel", 0, None, "staand", 1.0), ("pro", "knop", 0, None, "staand", 1.0),
         ("pro", "pose_rond", 0, None, "staand", 1.0)],
        [("Rigged character", "to poseable 3D print", 0, 2.5),
         ("One button:", "Figure from rig", 2.5, 4.8),
         ("Hinges and ball joints,", "cut from the figure", 4.8, 9.0),
         ("Check the pose", "before you print", 9.0, 99)],
        [("klik", 2.6), ("zoef", 9.0, 1.2)], ONDER_PRO),
    (10, "knee-too-far"): (
        [("pro3", "buig", 14, None, "knie", 1.0), ("pro3", "rood", 0, None, "knie", 1.0),
         ("pro3", "terug", 0, None, "knie", 1.0)],
        [("How far can a", "printed knee bend?", 0, 3.0),
         (f"Stop at {K_STOP}°,", "read from his rig", 3.0, 7.6),
         (f"Past {K_STOP}°:", "the arc turns red", 7.6, 12.6),
         ("Back inside the stop:", "red is gone", 12.6, 99)],
        [("buig", 0.3, 4.6), ("zoef", 7.7, 1.4), ("klik", 12.7)], ONDER_PRO),
    (11, "hinge-or-ball"): (
        [("pro", "elleboog", 6, None, "staand", 1.0), ("pro", "schouder", 0, None, "staand", 1.0)],
        [("Hinge or ball joint?", "For a printed figure", 0, 2.6),
         ("Elbows: hinge", f"with a stop at {E_STOP}°", 2.6, 5.3),
         ("Shoulders: ball joint,", f"±{S_GRENS}° each way", 5.3, 99)],
        [("buig", 2.7, 2.4), ("zoef", 5.4, 1.0)], ONDER_PRO),
}

meting = {}
for (nr, naam), (stukken, boven, klanken, onder) in SHORTS.items():
    delen = []
    for i, (bron, deel, van, tot, vorm, traag) in enumerate(stukken):
        d0 = FILM[bron]["delen"][deel]
        eerste = d0 + van
        laatste = min(deel_eind(bron, deel), d0 + tot) if tot is not None else deel_eind(bron, deel)
        uit = TMP / f"{nr}-{i}.mp4"
        ff("-i", str(BRON[bron] / "opname-ruw.mkv"),
           "-vf", f"trim=start_frame={eerste - 1}:end_frame={laatste - 1},{VORM[vorm]},"
                  f"setpts={traag}*(PTS-STARTPTS),fps={FPS},format=yuv420p",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", str(uit))
        delen.append(uit)
    lijst = TMP / f"{nr}.txt"
    lijst.write_text("".join(f"file '{p}'\n" for p in delen))
    rauw = TMP / f"{nr}-rauw.mp4"
    ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c", "copy", str(rauw))
    vf = [f"drawbox=x=0:y=150:w=1080:h=210:color=black@0.35:t=fill"]
    for r1, r2, a, b in boven:
        vf += [dt(r1, 70, LICHT, 168, extra=tussen(a, b)), dt(r2, 62, MINT, 258, extra=tussen(a, b))]
    vf += [f"drawbox=x=0:y=1355:w=1080:h=200:color=black@0.30:t=fill"]
    vf += [dt(t, s, c, y, f) for t, s, c, y, f in onder]
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
    mp4 = UIT / f"short-{nr}-{naam}-geluid.mp4"
    ff("-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
       "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
       "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4))
    meting[f"{nr}-{naam}"] = {"duur_s": round(duur, 2), "teksten": [[r1, r2, a, b] for r1, r2, a, b in boven],
                              "stukken": [[b, d, v, t, vo] for b, d, v, t, vo, _tr in stukken]}
    ff("-i", str(mp4), "-vf", f"fps=4/{duur:.3f},scale=270:-1,tile=4x1", "-frames:v", "1",
       str(UIT / f"overzicht-{nr}.jpg"))
    print(f"klaar: {mp4.name} {duur:.1f} s")

(UIT / "metingen.json").write_text(json.dumps({"shorts": meting, "pro": FILM["pro"].get("metingen", {}),
                                               "gratis": FILM["gratis"].get("metingen", {}),
                                               "pro3": FILM["pro3"].get("metingen", {})}, indent=1))
