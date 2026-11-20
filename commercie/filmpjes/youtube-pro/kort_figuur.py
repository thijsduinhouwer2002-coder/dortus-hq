#!/usr/bin/env python3
"""Kopie van kort.py voor opname_figuur.py (Chris, 20 nov 2026). Oorspronkelijk: korte staande filmpjes (TikTok, Shorts) uit dezelfde opname als YouTube Pro 1 (Chris, 19 nov 2026,
vraag Roep-Maker 20:35 NL). Elk filmpje is één idee, 10 tot 20 s, 1080x1920, met eigen geluid.
    python3 kort.py <map met beelden/ en film.json van opname.py> <uitmap>
Beeld: het kijkvenster van de echte Blender (vierkant 1080x1080 uit het scherm, zonder zijbalk) in het midden,
een korte zin boven, dortus.com/tt en "Measured in Blender, not printed yet." onder, binnen de veilige zone
van TikTok (niets in de onderste 300 px en de rechter 140 px). Het script kleurt niets: rood, boog en
groene pasband komen van de add-on. Geluid: functies uit commercie/filmpjes/geluid/geluid.py.
Uit: click-joints-pro-kort-<naam>-geluid.mp4 per filmpje en kort-overzicht.jpg (4 beelden per filmpje)."""
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
FPS, D, ST = film["fps"], film["delen"], film.get("standen", {})
VOLG = sorted(D, key=lambda k: D[k])
BG, LICHT, GRIJS, MINT = "0x23262D", "0xF1F3F7", "0xC9CDD8", "0x3BE6B0"
KX, KY = 100, 0          # vierkant uit het scherm: x 100 tot 1180 (zijbalk begint rond 1540)


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
    # midden van de veilige breedte (0 tot 940), zodat de knoppen van TikTok rechts niets afdekken
    return (f"drawtext=fontfile='{fnt or VET}':textfile='{tf(tekst)}':fontsize={grootte}:fontcolor={kleur}"
            f":x=(940-text_w)/2+20:y={y}{extra}")


def ff(*a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)


def deel_eind(deel):
    i = VOLG.index(deel)
    return D[VOLG[i + 1]] if i + 1 < len(VOLG) else film["n"]


def g_(k, val):
    return f"{int(round(ST.get(k, val)))}°"


# naam: (bovenzin 1, bovenzin 2, stukken [(deel, vanaf beeld, tot beeld of None, vertraging)], geluid)
# Beeldnummers binnen een deel volgen opname.py (stuk(...) en neem(...)).
FILMPJES = {
    # stand90: 45 stil, 150 buigen, 90 stil, 30 voorbij, 75 stil (zelfde voor stand135)
    "stop-90-135": ("Pick where your hinge stops", f"{g_('90', 90)} or {g_('135', 135)}",
                    [("stand90", 35, 325, 1.0), ("stand135", 35, 325, 1.0)],
                    [("buig", 0.33, 5.0), ("klik", 5.33), ("buig", 10.0, 5.0), ("klik", 15.0)]),
    # buig: 180 buigen, 150 stil; rood: 45 camera, 60 voorbij, 150 stil; terug: 60 terug, 120 stil
    "rood-voorbij-stop": ("Bend past the stop", "and the arc turns red",
                          [("buig", 0, 200, 1.0), ("rood", 0, 210, 1.0), ("terug", 0, 120, 1.0)],
                          [("buig", 0.2, 6.0), ("klik", 6.0), ("zoef", 8.2, 2.0)]),
    # kogel: 180 rond, 30 stil; 1,5x vertraagd zodat het rustig blijft en boven 10 s komt
    "kogel-pasband": ("Ball joint for 3D printing", "the green band shows the fit",
                      [("kogel", 0, None, 1.5)],
                      [("klik", 0.3)]),
}
# KORT_SET=figuur: filmpjes uit opname_figuur.py (20 nov 2026). Beeldnummers volgen dat script.
# rig: 120 rond + 30 stil; knop: 30 stil + 120 rond + 30 stil; buig: 120 + 60 stil; uitelkaar: 240 rond + 30 stil.
if True:  # kopie van kort.py met de filmpjes van opname_figuur.py (zo draait youtube-pro-1 niet opnieuw)
    KX = int(os.environ.get("KORT_KX", "230"))
    FILMPJES = {
        "figuur-uit-rig": ("One button turns your rig", "into printable joints",
                           [("rig", 30, 150, 1.0), ("knop", 0, 180, 1.0), ("buig", 0, 180, 1.0)],
                           [("klik", 4.0), ("buig", 10.0, 4.0)]),
        "uit-elkaar": ("Exploded view", "see every joint before you print",
                       [("uitelkaar", 0, None, 1.4)],
                       [("zoef", 0.3, 2.0)]),
    }
ONDER = [("dortus.com/tt", 64, MINT, 1430, VET), ("Click Joints Pro for Blender", 40, LICHT, 1515, GEW),
         ("Measured in Blender, not printed yet.", 32, GRIJS, 1570, GEW)]

meting = {}
plaatjes = []
for naam, (boven1, boven2, stukken, klanken) in FILMPJES.items():
    delen = []
    for i, (deel, van, tot, traag) in enumerate(stukken):
        eerste = D[deel] + van
        laatste = min(deel_eind(deel), D[deel] + tot) if tot is not None else deel_eind(deel)
        uit = TMP / f"{naam}{i}.mp4"
        ff("-framerate", str(FPS), "-start_number", str(eerste), "-i", str(IN / "beelden" / "b%05d.png"),
           "-vf", f"trim=end_frame={laatste - eerste},crop=1080:1080:{KX}:{KY},"
                  f"setpts={traag}*(PTS-STARTPTS),fps={FPS},format=yuv420p",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", str(uit))
        delen.append(uit)
    lijst = TMP / f"{naam}.txt"
    lijst.write_text("".join(f"file '{p}'\n" for p in delen))
    vierkant = TMP / f"{naam}-vk.mp4"
    ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c", "copy", str(vierkant))
    vf = ",".join([f"pad=1080:1920:0:300:color={BG}",
                   dt(boven1, 60, LICHT, 110), dt(boven2, 56, MINT, 200, GEW)]
                  + [dt(t, s, c, y, f) for t, s, c, y, f in ONDER])
    stil = TMP / f"{naam}-stil.mp4"
    ff("-i", str(vierkant), "-vf", vf + ",format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
       "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", str(stil))
    duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(stil)], capture_output=True, text=True).stdout)
    buf = g.bed_joints(duur)
    g.plak(buf, 0.05, g.tik())
    for k in klanken:
        if k[0] == "klik":
            g.plak(buf, k[1], g.klik())
        elif k[0] == "buig":
            g.plak(buf, k[1], g.buig(k[2]))
        elif k[0] == "zoef":
            g.plak(buf, k[1], g.zoef(k[2]))
    n_in, n_uit = int(0.2 * g.SR), int(1.0 * g.SR)
    buf[:n_in] *= np.linspace(0, 1, n_in)
    buf[-n_uit:] *= np.linspace(1, 0, n_uit)
    st = np.stack([buf, np.concatenate([np.zeros(12), buf[:-12]])], axis=1)
    st = st / (np.abs(st).max() + 1e-9) * 0.7
    wav = TMP / f"{naam}.wav"
    g.schrijf_wav(wav, st)
    mp4 = UIT / f"click-joints-pro-kort-{naam}-geluid.mp4"
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
   str(UIT / "kort-overzicht.jpg"))
(UIT / "kort-metingen.json").write_text(json.dumps({"duur_s": meting, "standen": ST}, indent=1))
