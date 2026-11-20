#!/usr/bin/env python3
"""Lange YouTube-uitleg "Rig to printable figure in Blender" (Click Joints Pro 1.1) in elkaar zetten.
20 nov 2026, opdracht hoofdchat 14:45 NL. Bouwt voort op commercie/filmpjes/youtube-pro/maak.py (Chris).
    python3 maak.py <map met opname-ruw.mkv en film.json van opname.py> <uitmap>
Uit: click-joints-pro-rig-to-figure-geluid.mp4 (1920x1080, 30 fps, H.264, AAC), hoofdstukken.txt, metingen.json,
overzicht.jpg (12 beelden). Beeld: de echte opname, een onderschrift per stuk, hoofdstukkaarten, vergrote stukken van
de echte zijbalk (knop en lijst), begin- en eindkaart in de huisstijl (Inter, #23262D, mint #3BE6B0).
Geluid: zelf gemaakt met commercie/filmpjes/geluid/geluid.py (sinustonen en ruis, geen muziek van een ander, geen stem).
Getallen in beeld komen uit film.json (gemeten door de add-on in de opname), niet uit dit script."""
import json
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
ZX, ZY, ZW, ZH = film.get("zijbalk") or [1500, 0, 420, 1050]
NAAM = "click-joints-pro-rig-to-figure"
RUW = IN / "opname-ruw.mkv"   # de hele opname, beeld 1 = b00001.png van opname.py


def font(stijl):
    r = subprocess.run(["fc-match", "-f", "%{file}", f"Inter:style={stijl}"], capture_output=True, text=True)
    return r.stdout.strip() or "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


VET, GEW = font("Bold"), font("Regular")
BG, LICHT, GRIJS, MINT = "0x23262D", "0xF1F3F7", "0xC9CDD8", "0x3BE6B0"
n_tekst = [0]


def tf(tekst):
    n_tekst[0] += 1
    p = TMP / f"t{n_tekst[0]}.txt"
    p.write_text(tekst, encoding="utf-8")
    return str(p)


def ff(*a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)


def enc(uit):
    return ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), str(uit)]


def dt(tekst, grootte, kleur, x, y, fnt=None, extra=""):
    return (f"drawtext=fontfile='{fnt or VET}':textfile='{tf(tekst)}':fontsize={grootte}:fontcolor={kleur}"
            f":x={x}:y={y}{extra}")


def tussen(a, b):
    return f":enable='between(t,{a},{b})'"


# Getallen uit de opname (film.json), met wat het paneel liet zien als terugval
N_GEW = MT.get("gewrichten", 9)
STOP = int(round(MT.get("knie_stop", 120)))
VOORBIJ = int(round(MT.get("knie_pose_rood", STOP + 12) - STOP))
N_EXPORT = len(MT.get("export", {}).get("bestanden", [])) or 10
REGELS = MT.get("regels", [])


def graad(naam, val):
    for r in REGELS:
        if r.startswith(naam + " "):
            try:
                return r.split("·")[2].strip().split("–")[1].rstrip("°")
            except IndexError:
                pass
    return str(val)


L_KNIE, L_ELL = graad("Left knee", 120), graad("Left elbow", 140)

# Vergrote stukken van de zijbalk: (x, y binnen de zijbalk, breedte, hoogte, schaal, plek x, plek y)
ZOOM = {
    "knop": (0, 30, ZW - 40, 130, 1.8, 60, 330),
    "lijst": (0, 300, ZW - 40, 330, 1.5, 40, 200),
    "presets": (0, 30, ZW - 40, 200, 1.6, 60, 300),
    "hinge": (0, 0, ZW - 40, 0, 1.6, 60, 300),
    "export": (0, 0, ZW - 40, 0, 1.6, 60, 300),
}
ZOOM.update(json.loads((HIER / "zoom.json").read_text()) if (HIER / "zoom.json").exists() else {})


def zoomfilter(sleutel, bron, doel, tijd=None):
    x, y, w, h, s, px, py = ZOOM[sleutel]
    if not h:
        return None
    w2, h2 = int(w * s) // 2 * 2, int(h * s) // 2 * 2
    en = tussen(*tijd) if tijd else ""
    return (f"[{bron}]split[{doel}a][{doel}b];[{doel}b]crop={w}:{h}:{ZX + x}:{ZY + y},scale={w2}:{h2}:flags=lanczos,"
            f"pad={w2 + 8}:{h2 + 8}:4:4:color={MINT}[{doel}z];[{doel}a][{doel}z]overlay=x={px}:y={py}{en}[{doel}]")


def stuk(naam, deel, van=0, tot=None, traag=1.0, onder=(), hoofdstuk="", zooms=(), extra_vf=(), houd=0.0, omgekeerd=False):
    """Een stuk opname: beelden van deel `deel` (van/tot binnen het deel), met onderschriften [(tekst, a, b)] en
    vergrotingen [(sleutel, (a, b))]. Geeft (bestand, duur)."""
    i = VOLG.index(deel)
    eind = D[VOLG[i + 1]] if i + 1 < len(VOLG) else film["n"] + 1
    eerste = D[deel] + van
    laatste = min(eind, D[deel] + tot) if tot is not None else eind
    n = laatste - eerste
    duur = n / FPS * traag + houd
    keten = [f"[0:v]trim=start_frame={eerste - 1}:end_frame={laatste - 1},setpts={traag}*(PTS-STARTPTS)" + (",reverse" if omgekeerd else "")
             + (f",tpad=stop_mode=clone:stop_duration={houd}" if houd else "") + f",fps={FPS}[v0]"]
    laatst = "v0"
    for k, (sl, tijd) in enumerate(zooms):
        z = zoomfilter(sl, laatst, f"z{k}", tijd)
        if z:
            keten.append(z)
            laatst = f"z{k}"
    vf = list(extra_vf)
    for tekst, a, b in onder:
        vf.append(dt(tekst, 44, LICHT, 60, "h-118", extra=f":box=1:boxcolor={BG}@0.88:boxborderw=22" + tussen(a, b)))
    if hoofdstuk:
        vf.append(dt(hoofdstuk, 34, MINT, 60, 50, extra=f":box=1:boxcolor={BG}@0.80:boxborderw=14"))
    keten.append(f"[{laatst}]" + (",".join(vf) + "," if vf else "") + "format=yuv420p[uit]")
    uit = TMP / f"{naam}.mp4"
    ff("-i", str(RUW), "-filter_complex", ";".join(keten), "-map", "[uit]", "-t", f"{duur:.3f}", *enc(uit))
    return uit, duur


def kaart(naam, regels, duur):
    f = ",".join(dt(t, s, c, "(w-text_w)/2", y, VET if v else GEW) for t, s, c, y, v in regels)
    uit = TMP / f"{naam}.mp4"
    ff("-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:r={FPS}:d={duur}", "-vf", f + ",format=yuv420p", *enc(uit))
    return uit


KAART_S = 3.5
vak = f":box=1:boxcolor={BG}@0.85:boxborderw=18"
klein = f":box=1:boxcolor={BG}@0.80:boxborderw=12"
stukken, tijd, hoofdstukken = [], 0.0, [("0:00", "What it does")]
geluid = {"tik": [], "klik": [], "buig": [], "zoef": []}


def voeg(s, duur, tikken=()):
    global tijd
    stukken.append(s)
    for t in tikken:
        geluid["tik"].append(tijd + t)
    tijd += duur


def hoofdstuk(nr, titel):
    hoofdstukken.append((f"{int(tijd // 60)}:{int(tijd % 60):02d}", titel))
    voeg(kaart(f"k{nr}", [(str(nr), 90, MINT, 380, True), (titel, 80, LICHT, 500, True)], KAART_S), KAART_S, (0.0,))


# 0 haak: knop, de bogen verschijnen, rustig rond; titel links
titel = [dt("Rig to printable", 84, LICHT, 60, 60, extra=vak), dt("figure in Blender", 84, LICHT, 60, 160, extra=vak),
         dt("One button: a hinge with an end stop", 40, GRIJS, 60, 290, GEW, vak),
         dt("at every elbow and knee, a ball joint", 40, GRIJS, 60, 345, GEW, vak),
         dt("at shoulders, hips and neck.", 40, GRIJS, 60, 400, GEW, vak),
         dt("Click Joints Pro 1.1, recorded in Blender 5.3. Measured in Blender, not print tested by us yet.", 30,
            GRIJS, 60, "h-80", GEW, klein)]
s1, d1 = stuk("haak1", "druk", extra_vf=titel)
s2, d2 = stuk("haak2", "lijst", 0, 60, extra_vf=titel)
s3, d3 = stuk("haak3", "bogen", 0, 210, extra_vf=titel)
voeg(s1, d1, (0.05,))
geluid["klik"].append(tijd)
voeg(s2, d2)
voeg(s3, d3)

# 1 rig
hoofdstuk(1, "Start with a rigged figure")
s, d = stuk("rig", "rig", traag=1.25, hoofdstuk="1  Start with a rigged figure",
            onder=[("Start with your rigged figure. This one: 220 mm, 20 bones, one solid mesh.", 0, 99)])
voeg(s, d, (0.05,))
s, d = stuk("druk", "druk", houd=1.5, hoofdstuk="1  Start with a rigged figure", zooms=[("knop", None)],
            onder=[("Open the Figure joints panel and press Figure from rig.", 0, 99)])
voeg(s, d, (0.05,))
geluid["klik"].append(tijd - 0.1)

# 2 one button
hoofdstuk(2, "One button, every joint")
s, d = stuk("lijst", "lijst", traag=1.5, hoofdstuk="2  One button, every joint",
            zooms=[("lijst", (0, 8)), ("presets", (8, 12.1))],
            onder=[(f"{N_GEW} joints from one button. Elbows and knees: hinge. Shoulders, hips, neck: ball.", 0, 4),
                   ("The list shows each range and where it came from: from rig, mirror or preset.", 4, 8),
                   ("No rig? Put the 3D cursor on a joint and pick the body part.", 8, 99)])
voeg(s, d, (0.05, 4.0, 8.0))

# 3 ranges
hoofdstuk(3, "Every range in degrees")
s, d = stuk("bogen", "bogen", traag=1.25, hoofdstuk="3  Every range in degrees",
            onder=[("Next to every joint you see how far it bends, in degrees.", 0, 6),
                   (f"Left knee {L_KNIE}° and left elbow {L_ELL}° come from Limit Rotation in the rig.", 6, 99)])
voeg(s, d, (0.05, 6.0))

# 4 bend
hoofdstuk(4, "Bend to the stop")
s, d = stuk("buig", "buig", hoofdstuk="4  Bend to the stop", zooms=[("hinge", None)],
            onder=[(f"Drag Bend: the right knee stops at {STOP}°, mirrored from the left side of the rig.", 0, 99)])
geluid["buig"].append((tijd + 0.7, 5.0))
geluid["klik"].append(tijd + 0.7 + 5.0)
voeg(s, d, (0.05,))

# 5 past the stop
hoofdstuk(5, "Past the stop")
s, d = stuk("rood", "rood", hoofdstuk="5  Past the stop", zooms=[("hinge", None)],
            onder=[(f"Push past {STOP}° and the arc turns red, with how far you went.", 0, 99)])
geluid["zoef"].append((tijd + 0.1, 1.5))
voeg(s, d, (0.05,))
s, d = stuk("terug", "terug", hoofdstuk="5  Past the stop", zooms=[("hinge", None)],
            onder=[("Back inside the range, the red is gone.", 2.0, 99)])
voeg(s, d, (2.0,))

# 6 exploded
hoofdstuk(6, "Exploded view")
s, d = stuk("uitelkaar", "uitelkaar", traag=1.25, hoofdstuk="6  Exploded view",
            onder=[("Exploded view pulls every part apart, so you see each joint before you print.", 0, 7.5),
                    ("Clearance is 0.2 mm by default. You can change it.", 7.5, 99)])
geluid["zoef"].append((tijd + 0.2, 2.0))
voeg(s, d, (0.05, 7.5))

# 7 export
hoofdstuk(7, "Export STL or 3MF")
s, d = stuk("export", "export", houd=2.0, hoofdstuk="7  Export STL or 3MF", zooms=[("export", None)],
            onder=[(f"Export as STL or 3MF. Here: {N_EXPORT} parts as 3MF files, one click.", 0, 99)])
geluid["klik"].append(tijd + 1.5)
voeg(s, d, (0.05,))

# 8 good to know
hoofdstuk(8, "Good to know")
s, d = stuk("goed", "bogen", traag=1.0, omgekeerd=True, hoofdstuk="8  Good to know",
            onder=[("Works best on figures with separate arms and legs, about 200 mm tall or more.", 0, 5),
                   ("Measured in Blender, not print tested by us yet. Print a test joint first.", 5, 99)])
voeg(s, d, (0.05, 5.0))

hoofdstukken.append((f"{int(tijd // 60)}:{int(tijd % 60):02d}", "Where to get it"))
EIND_S = 16.0
voeg(kaart("eind", [("Click Joints Pro", 100, LICHT, 290, True),
                    ("Rig to printable figure, in Blender.", 50, GRIJS, 430, False),
                    ("dortus.com/yt", 84, MINT, 560, True),
                    ("Link in the description.", 40, GRIJS, 690, False),
                    ("Measured in Blender, not print tested by us yet.", 34, GRIJS, 800, False)], EIND_S), EIND_S, (0.0,))

lijst = TMP / "lijst.txt"
lijst.write_text("".join(f"file '{p}'\n" for p in stukken))
stil = TMP / f"{NAAM}.mp4"
ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
   "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(stil))
duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(stil)],
                            capture_output=True, text=True).stdout)

buf = g.bed_joints(duur)
for s in geluid["tik"]:
    g.plak(buf, s, g.tik())
for s, d in geluid["buig"]:
    g.plak(buf, s, g.buig(d))
for s, d in geluid["zoef"]:
    g.plak(buf, s, g.zoef(d))
for s in geluid["klik"]:
    g.plak(buf, s, g.klik())
n_in, n_uit = int(0.3 * g.SR), int(1.5 * g.SR)
buf[:n_in] *= np.linspace(0, 1, n_in)
buf[-n_uit:] *= np.linspace(1, 0, n_uit)
st = np.stack([buf, np.concatenate([np.zeros(12), buf[:-12]])], axis=1)
st = st / (np.abs(st).max() + 1e-9) * 0.7
wav = TMP / "geluid.wav"
g.schrijf_wav(wav, st)
mp4 = UIT / f"{NAAM}-geluid.mp4"
ff("-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
   "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
   "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4))

(UIT / "hoofdstukken.txt").write_text("".join(f"{t} {n}\n" for t, n in hoofdstukken))
(UIT / "metingen.json").write_text(json.dumps({"duur_s": round(duur, 2), "metingen": MT}, indent=1))
stap = duur / 12
ff("-i", str(mp4), "-vf", f"fps=1/{stap:.3f},scale=480:-1,tile=4x3", "-frames:v", "1", str(UIT / "overzicht.jpg"))
print(f"klaar: {mp4} {duur:.1f} s")
print((UIT / "hoofdstukken.txt").read_text())
