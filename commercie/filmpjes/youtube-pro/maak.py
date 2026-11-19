#!/usr/bin/env python3
"""YouTube-video 1 van Click Joints Pro in elkaar zetten (Chris, 19 nov 2026).
    python3 maak.py <map met beelden/ en film.json van opname.py> <uitmap>
Uit: click-joints-pro-uitleg-2-geluid.mp4 (1920x1080, 30 fps, H.264, AAC), hoofdstukken.txt (voor de
beschrijving), overzicht.jpg (12 beelden voor de keuring).
Beeld: de echte opname met een onderschrift per deel, korte hoofdstukkaarten, begin- en eindkaart in de
huisstijl van de demofilm (Inter, #23262D, mint #3BE6B0). Geluid: zelf gemaakt met de functies uit
commercie/filmpjes/geluid/geluid.py (sinustonen en ruis, geen muziek van een ander, geen stem)."""
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
FPS = film["fps"]
D = film["delen"]
ST = film.get("standen", {})


def font(stijl):
    r = subprocess.run(["fc-match", "-f", "%{file}", f"Inter:style={stijl}"], capture_output=True, text=True)
    return r.stdout.strip() or "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


VET, GEW = font("Bold"), font("Regular")
BG, LICHT, GRIJS, MINT = "0x23262D", "0xF1F3F7", "0xC9CDD8", "0x3BE6B0"
n_tekst = [0]


def tf(tekst):
    """Tekst via een bestand, dan hoeven dubbele punten en graden niet ontsnapt te worden."""
    n_tekst[0] += 1
    p = TMP / f"t{n_tekst[0]}.txt"
    p.write_text(tekst, encoding="utf-8")
    return str(p)


def graden(sleutel, val):
    return f"{int(round(ST.get(sleutel, val)))}°"


g115, g90, g135 = graden("115", 115), graden("90", 90), graden("135", 135)
# (deel, onderschrift, hoofdstuk links boven)
DELEN = [
    ("haak", "Click Joints Pro: a print-ready hinge with a real end stop.", ""),
    ("heel", "Start with one solid part, like this leg.", "1  Place a hinge"),
    ("knop", "Pick the end stop: 90°, 115° or 135°. Click Place hinge.", "1  Place a hinge"),
    ("rond", "One click: the part is cut in two, with a hinge between them.", "1  Place a hinge"),
    ("buig", f"Drag Bend. The arc shows the real range: it stops at {g115}.", "2  Bend to the stop"),
    ("rood", "Push past the stop: the arc turns red and shows how far you went.", "3  Past the stop"),
    ("terug", "Back inside the range, the red is gone.", "3  Past the stop"),
    ("stand90", f"The same knee with 90°: the arc ends at {g90}, red past it.", "4  90°, 115° or 135°"),
    ("stand135", f"With 135° it bends to {g135}, red past it.", "4  90°, 115° or 135°"),
    ("kogel", "Ball joints with the green fit band are in Pro too.", "5  Ball joints too"),
]
VOLG = [d for d, _, _ in DELEN] + ["eind"]
KAART_VOOR = {"heel": "1  Place a hinge", "buig": "2  Bend to the stop", "rood": "3  Past the stop",
              "stand90": "4  90°, 115° or 135°", "kogel": "5  Ball joints too"}
KAART_S, HAAK_BEELDEN = 3.5, 210   # YouTube-hoofdstukken minstens 10 s
# Keuring Daan 19 nov (moet 2): het onderschrift van "terug" pas als het rood weg is. De schuif gaat in de
# eerste 60 beelden (2 s) terug; daarna is het rood gemeten weg (rood_na_terug 0). Dus vanaf 2,1 s.
TEKST_VANAF = {"terug": 2.1}
# Keuring Daan (moet 3): het stilstaande been van 9 s naar 3 s, door elk derde beeld te nemen (sneller rond).
VERSNEL = {"heel": 3}


def ff(*a):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True)


def enc(uit):
    return ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), str(uit)]


def dt(tekst, grootte, kleur, x, y, fnt=None, extra=""):
    return (f"drawtext=fontfile='{fnt or VET}':textfile='{tf(tekst)}':fontsize={grootte}:fontcolor={kleur}"
            f":x={x}:y={y}{extra}")


def kaart(naam, regels, duur):
    """Effen kaart; regels = [(tekst, grootte, kleur, y, vet)]."""
    f = ",".join(dt(t, s, c, "(w-text_w)/2", y, VET if v else GEW) for t, s, c, y, v in regels)
    uit = TMP / f"{naam}.mp4"
    ff("-f", "lavfi", "-i", f"color=c={BG}:s=1920x1080:r={FPS}:d={duur}", "-vf", f + ",format=yuv420p",
       *enc(uit))
    return uit


def opname(deel, onder, hoofdstuk):
    van, tot = D[deel], D[VOLG[VOLG.index(deel) + 1]]
    aan = f":enable='gte(t,{TEKST_VANAF[deel]})'" if deel in TEKST_VANAF else ""
    f = [dt(onder, 46, LICHT, 60, "h-120", extra=f":box=1:boxcolor={BG}@0.88:boxborderw=22{aan}")]
    if deel in VERSNEL:
        k = VERSNEL[deel]
        f.insert(0, f"select='not(mod(n,{k}))',setpts=N/{FPS}/TB")
    if hoofdstuk:
        f.append(dt(hoofdstuk, 34, MINT, 60, 50, extra=f":box=1:boxcolor={BG}@0.80:boxborderw=14"))
    vf = ",".join(f)
    uit = TMP / f"{deel}.mp4"
    if deel == "knop":   # de knop uit de zijbalk 2x vergroot ernaast, met een mint rand (zoals maak_film.sh)
        kx, ky = 1555, 785
        ff("-framerate", str(FPS), "-start_number", str(van), "-i", str(IN / "beelden" / "b%05d.png"),
           "-frames:v", str(tot - van), "-filter_complex",
           f"[0:v]split[a][b];[b]crop=316:70:{kx}:{ky},scale=632:140:flags=lanczos,pad=640:148:4:4:color={MINT}[z];"
           f"[a][z]overlay=x=840:y=210,{vf},format=yuv420p", *enc(uit))
    else:
        ff("-framerate", str(FPS), "-start_number", str(van), "-i", str(IN / "beelden" / "b%05d.png"),
           "-frames:v", str(tot - van), "-vf", vf + ",format=yuv420p", *enc(uit))
    return uit, (tot - van) / FPS / VERSNEL.get(deel, 1)


def haak():
    """Keuring Daan (moet 3): geen stilstaande titel. Open met de buig naar de stop (deel buig, 7 s) met de
    titel en de drie standen eroverheen."""
    van = D["buig"]
    n = min(HAAK_BEELDEN, D["rood"] - van)
    vak = f":box=1:boxcolor={BG}@0.85:boxborderw=20"
    vf = ",".join([dt("Click Joints Pro", 96, LICHT, 60, 60, extra=vak),
                   dt("A hinge for 3D prints that stops where you want", 44, GRIJS, 60, 210, GEW, vak),
                   dt("90°  ·  115°  ·  135°", 60, MINT, 60, 300, extra=vak),
                   dt("Recorded in Blender 5.3. Measured in Blender, not printed yet.", 32, GRIJS, 60, "h-90",
                      GEW, f":box=1:boxcolor={BG}@0.80:boxborderw=14")])
    uit = TMP / "begin.mp4"
    ff("-framerate", str(FPS), "-start_number", str(van), "-i", str(IN / "beelden" / "b%05d.png"),
       "-frames:v", str(n), "-vf", vf + ",format=yuv420p", *enc(uit))
    return uit, n / FPS


stukken, tijd, hoofdstukken, geluid = [], 0.0, [("0:00", "What it does")], {"tik": [], "klik": [], "buig": [], "zoef": []}
s, BEGIN_S = haak()
stukken.append(s)
geluid["buig"].append((1.0 / FPS, 6.0))
geluid["klik"].append(6.0)
tijd += BEGIN_S
for deel, onder, hst in DELEN:
    if deel in KAART_VOOR:
        hoofdstukken.append((f"{int(tijd // 60)}:{int(tijd % 60):02d}", KAART_VOOR[deel].split("  ", 1)[1]))
        nr, titel = KAART_VOOR[deel].split("  ", 1)
        stukken.append(kaart(f"k{deel}", [(nr, 90, MINT, 380, True), (titel, 80, LICHT, 500, True)], KAART_S))
        geluid["tik"].append(tijd)
        tijd += KAART_S
    s, duur = opname(deel, onder, hst)
    stukken.append(s)
    geluid["tik"].append(tijd + 0.05)
    if deel == "knop":
        geluid["klik"].append(tijd + 0.1)
    if deel in ("haak", "buig"):
        geluid["buig"].append((tijd + 1.0 / FPS, 2.0 if deel == "haak" else 6.0))
    if deel.startswith("stand"):
        geluid["buig"].append((tijd + 1.5, 5.0))
        geluid["klik"].append(tijd + 1.5 + 5.0 + 3.0)   # het moment van de stop
    if deel == "buig":
        geluid["klik"].append(tijd + 6.0)
    if deel in ("rood",):
        geluid["zoef"].append((tijd + 1.5, 2.0))
    tijd += duur
hoofdstukken.append((f"{int(tijd // 60)}:{int(tijd % 60):02d}", "Where to get it"))
EIND_S = max(14.0, min(20.0, 121.0 - tijd))   # eindscherm 14 tot 20 s; video daardoor minstens 2:00 (opdracht)
stukken.append(kaart("eind", [("Click Joints Pro", 100, LICHT, 300, True),
                              ("Hinges with an end stop, ball joints, STL and 3MF.", 48, GRIJS, 450, False),
                              ("dortus.com/click-joints", 72, MINT, 580, True),
                              ("Free version: extensions.blender.org", 40, GRIJS, 720, False),
                              ("Measured in Blender, not printed yet.", 34, GRIJS, 800, False)], EIND_S))
tijd += EIND_S

lijst = TMP / "lijst.txt"
lijst.write_text("".join(f"file '{p}'\n" for p in stukken))
stil = UIT / "click-joints-pro-uitleg-2.mp4"
ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
   "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(stil))
duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(stil)],
                            capture_output=True, text=True).stdout)

# Geluid: rustige warme toon, tik bij elke nieuwe tekst, klik bij scharnier en stop, oplopende toon bij buigen.
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
# Keuring Daan (kan 3): naar -14 LUFS zoals YouTube, met een begrenzer op -1,5 dB piek.
mp4 = UIT / "click-joints-pro-uitleg-2-geluid.mp4"
ff("-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
   "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
   "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2", "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4))
stil.unlink()

(UIT / "hoofdstukken.txt").write_text("".join(f"{t} {n}\n" for t, n in hoofdstukken))
(UIT / "metingen.json").write_text(json.dumps({"duur_s": round(duur, 2), "standen": ST,
                                               "metingen": film.get("metingen", {})}, indent=1))
stap = duur / 12
ff("-i", str(mp4), "-vf", f"fps=1/{stap:.3f},scale=480:-1,tile=4x3", "-frames:v", "1", str(UIT / "overzicht.jpg"))
print(f"klaar: {mp4} {duur:.1f} s")
print((UIT / "hoofdstukken.txt").read_text())
