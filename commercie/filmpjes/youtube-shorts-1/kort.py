#!/usr/bin/env python3
"""YouTube Shorts reeks 1 (21 nov 2026, opdracht hoofdchat ±12:45 NL): 8 staande filmpjes (1080x1920, 10 tot 25 s),
elk één gewricht of één ding met één belofte, uit echte opnames in Blender 5.3.0:
  pro3   opname-ruw.mkv en film.json uit release youtube-pro-3 (liggend 1920x1080, Pro 1.1, grijze figuur)
  pro    opname.py met CJ_SOORT=pro (staand 1080x1920, Pro 1.1.0, lichtblauwe figuur)
  gratis opname.py met CJ_SOORT=gratis (staand 1080x1920, gratis 0.1.1, zandkleurige figuur)
    python3 kort.py <map pro3> <map pro> <map gratis> <uitmap>
Beeld: de echte opname over het hele scherm (staand) of op dezelfde achtergrond (liggend, met de verloopkleuren van
het kijkvenster erboven en eronder), haak bovenaan vanaf het eerste beeld, onderaan het meetadres en de zin over
printen. Het script kleurt niets in de opname. Geluid: commercie/filmpjes/geluid/geluid.py (met code gemaakt).
Getallen in beeld komen uit film.json van de opnames, met de waarde uit de proef als terugval.
Uit: short-<nr>-<naam>-geluid.mp4 per filmpje, overzicht-<nr>.jpg (4 beelden per filmpje), metingen.json."""
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
    (1, "rig-to-parts"): (
        [("pro3", "rig", 120, None, "breed", 1.0), ("pro3", "druk", 20, None, "breed", 1.0),
         ("pro3", "lijst", 0, 45, "breed", 1.0), ("pro3", "bogen", 0, 270, "breed", 1.0)],
        [("One click:", f"rig to {N_EXPORT} printable parts", 0, 3.4),
         (f"{N_GEW} joints: hinges", "and ball joints", 3.4, 7.5),
         ("Every joint shows", "its range in degrees", 7.5, 99)],
        [("klik", 2.7)], ONDER_PRO),
    (2, "knee-120"): (
        [("pro3", "buig", 14, None, "knie", 1.0), ("pro3", "rood", 0, None, "knie", 1.0)],
        [("His knee stops", f"at {K_STOP}°", 0, 3.0),
         ("Range read", "from his rig", 3.0, 7.4),
         (f"Past {K_STOP}°:", "the arc turns red", 7.4, 99)],
        [("buig", 0.3, 4.6), ("zoef", 7.5, 1.4)], ONDER_PRO),
    (3, "elbow-140"): (
        [("pro", "elleboog", 6, None, "staand", 1.0), ("pro", "elleboog_rood", 0, None, "staand", 1.0)],
        [("His elbow stops", f"at {E_STOP}°", 0, 4.9),
         (f"Past {E_STOP}°: red,", "and it says how far", 4.9, 99)],
        [("buig", 0.2, 3.5), ("zoef", 5.0, 1.2)], ONDER_PRO),
    (4, "shoulder-ball"): (
        [("pro", "schouder", 0, None, "staand", 1.0), ("pro", "schouder_dicht", 0, None, "staand", 1.0)],
        [("Ball joint shoulder", "for a 3D printed figure", 0, 4.0),
         ("Ball and socket,", "cut from the figure itself", 4.0, 7.3),
         (f"Bends ±{S_GRENS}°,", "shown before you print", 7.3, 99)],
        [("zoef", 0.1, 1.0), ("klik", 4.1)], ONDER_PRO),
    (5, "degrees"): (
        [("pro3", "bogen", 30, 240, "breed", 1.0), ("pro3", "lijst", 30, 240, "lijst", 1.0)],
        [("Every joint shows", "how far it bends", 0, 7.0),
         ("From your rig,", "mirrored, or a preset", 7.0, 99)],
        [("klik", 7.0)], ONDER_PRO),
    (6, "pose"): (
        [("pro", "pose", 6, None, "staand", 1.0), ("pro", "pose_rond", 0, None, "staand", 1.0)],
        [("Bend knees and elbows", "of a rigged figure", 0, 3.0),
         ("Check the whole figure", "before you print", 3.0, 99)],
        [("buig", 0.2, 2.4)], ONDER_PRO),
    (7, "exploded"): (
        [("pro3", "uitelkaar", 30, None, "breed", 1.0), ("pro3", "export", 30, None, "breed", 1.0)],
        [("Exploded view:", f"{N_EXPORT} printable parts", 0, 5.0),
         ("Hinges at elbows, knees,", "balls at shoulders, hips, neck", 5.0, 10.0),
         ("Export every part", "as STL or 3MF", 10.0, 99)],
        [("zoef", 0.1, 1.0), ("klik", 11.0)], ONDER_PRO),
    (8, "free-neck"): (
        [("gratis", "heel", 0, None, "staand", 1.0), ("gratis", "cursor", 0, None, "staand", 1.0),
         ("gratis", "plaats", 0, None, "staand", 1.0), ("gratis", "bereik", 4, None, "staand", 1.0),
         ("gratis", "bereik_rood", 0, None, "staand", 1.0), ("gratis", "bereik_rond", 0, None, "staand", 1.0)],
        [("Free Blender add-on:", "ball joint in the neck", 0, 2.5),
         ("3D cursor on the neck,", "then Place joint", 2.5, 5.5),
         (FIT.split(": ")[0] + ":", FIT.split(": ")[1], 5.5, 8.4),
         (f"Bends ±{N_GRENS}°,", "red past that", 8.4, 99)],
        [("klik", 2.5), ("buig", 8.6, 1.6), ("zoef", 10.6, 1.0)], ONDER_GRATIS),
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
