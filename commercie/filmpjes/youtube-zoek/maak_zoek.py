#!/usr/bin/env python3
"""Drie lange YouTube-video's op zoekvragen, geknipt uit de echte opname van youtube-pro-3 (Click Joints Pro 1.1).
21 nov 2026, opdracht hoofdchat 12:35 NL (YouTube als zoekmotor). Chris. Helpers gelijk aan youtube-pro-3/maak.py.
    python3 maak_zoek.py <map met opname-ruw.mkv en film.json> <uitmap> [a|b|c|abc]
Zoekvragen (YouTube-suggesties, curl suggestqueries 21 nov 2026, GEZIEN):
  a  "how to make articulated 3d prints in blender"
  b  "blender hinge 3d print"
  c  "blender split model for 3d printing"
Opbouw per video: titel = de zoekvraag, eerst het antwoord in drie regels, dan de stappen in de echte opname,
dan "goed om te weten" en een eindkaart met dortus.com/yt. Click Joints is het middel, niet het onderwerp.
Uit per video: zoek-<x>-...-geluid.mp4 (1920x1080), zoek-<x>-hoofdstukken.txt, zoek-<x>-overzicht.jpg.
Getallen in beeld komen uit film.json (gemeten door de add-on in de opname)."""
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
KEUZE = sys.argv[3] if len(sys.argv) > 3 else "abc"
UIT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
film = json.loads((IN / "film.json").read_text())
FPS, D, MT = film["fps"], film["delen"], film.get("metingen", {})
VOLG = sorted(D, key=lambda k: D[k])
ZX, ZY, ZW, ZH = film.get("zijbalk") or [1500, 0, 420, 1050]
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
# Plekken gemeten op beelden 200, 240, 960 en 1700 van opname 2 (run 44749515895); x en y binnen de zijbalk.
ZOOM = {
    "knop": (5, 744, 360, 160, 1.8, 60, 330),      # Figure joints met de knop Figure from rig
    "lijst": (5, 706, 360, 300, 1.5, 40, 250),     # 9 joints · 2 rig · 2 mirror · 5 preset en de lijst
    "presets": (5, 590, 360, 120, 1.8, 40, 330),   # Or put the 3D cursor on a joint, then: Shoulder ... Neck
    "hinge": (5, 336, 360, 140, 1.6, 40, 300),     # blok Hinge met Bends 0° to 120° en de Bend-schuif
    "export": (5, 524, 360, 200, 1.6, 40, 330),    # 3 Fit and export, 3MF, Export 3MF
}


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
        vf.append(dt(tekst, 40, LICHT, 60, "h-112", extra=f":box=1:boxcolor={BG}@0.88:boxborderw=22" + tussen(a, b)))
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
VOET = "Shown with Click Joints Pro 1.1 in Blender 5.3. Measured in Blender, not print tested by us yet."


class Film:
    """Houdt per video de stukken, de tijd, de hoofdstukken en het geluid bij."""

    def __init__(self, x, naam):
        self.x, self.naam = x, naam
        self.stukken, self.tijd = [], 0.0
        self.hoofdstukken = [("0:00", "The short answer")]
        self.geluid = {"tik": [], "klik": [], "buig": [], "zoef": []}
        self.nr = 0

    def voeg(self, s, duur, tikken=()):
        self.stukken.append(s)
        self.geluid["tik"] += [self.tijd + t for t in tikken]
        self.tijd += duur

    def stuk(self, naam, deel, **kw):
        return stuk(f"{self.x}_{naam}", deel, **kw)

    def hoofdstuk(self, titel):
        self.nr += 1
        self.hoofdstukken.append((f"{int(self.tijd // 60)}:{int(self.tijd % 60):02d}", titel))
        k = kaart(f"{self.x}_k{self.nr}", [(str(self.nr), 90, MINT, 380, True), (titel, 80, LICHT, 500, True)], KAART_S)
        self.voeg(k, KAART_S, (0.0,))
        return f"{self.nr}  {titel}"

    def haak(self, deel, titel2, antwoord, **kw):
        """Eerst het antwoord: titel (de zoekvraag) en drie regels over de echte opname, links in beeld."""
        vf = [dt(titel2[0], 80, LICHT, 60, 60, extra=vak), dt(titel2[1], 80, LICHT, 60, 160, extra=vak),
              dt("The short answer:", 40, MINT, 60, 290, extra=vak)]
        for i, regel in enumerate(antwoord):
            vf.append(dt(regel, 40, LICHT, 60, 360 + i * 62, GEW, vak))
        vf.append(dt(VOET, 30, GRIJS, 60, "h-80", GEW, klein))
        s, d = self.stuk("haak", deel, extra_vf=vf, **kw)
        self.voeg(s, d, (0.05,))

    def goed(self, regels):
        h = self.hoofdstuk("Good to know")
        n = len(regels)
        onder = [(t, i * 10 / n, (i + 1) * 10 / n if i < n - 1 else 99) for i, t in enumerate(regels)]
        s, d = self.stuk("goed", "bogen", omgekeerd=True, hoofdstuk=h, onder=onder)
        self.voeg(s, d, tuple(a for _, a, _ in onder))

    def eind(self, onderwerp):
        self.hoofdstukken.append((f"{int(self.tijd // 60)}:{int(self.tijd % 60):02d}", "Where to get it"))
        k = kaart(f"{self.x}_eind", [("Click Joints Pro", 100, LICHT, 290, True),
                                     (onderwerp, 50, GRIJS, 430, False),
                                     ("dortus.com/yt", 84, MINT, 560, True),
                                     ("Link in the description.", 40, GRIJS, 690, False),
                                     ("Measured in Blender, not print tested by us yet.", 34, GRIJS, 800, False)], 12.0)
        self.voeg(k, 12.0, (0.0,))

    def klaar(self):
        lijst = TMP / f"{self.x}_lijst.txt"
        lijst.write_text("".join(f"file '{p}'\n" for p in self.stukken))
        stil = TMP / f"{self.naam}.mp4"
        ff("-f", "concat", "-safe", "0", "-i", str(lijst), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(stil))
        duur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     str(stil)], capture_output=True, text=True).stdout)
        buf = g.bed_joints(duur)
        for s in self.geluid["tik"]:
            g.plak(buf, s, g.tik())
        for s, d in self.geluid["buig"]:
            g.plak(buf, s, g.buig(d))
        for s, d in self.geluid["zoef"]:
            g.plak(buf, s, g.zoef(d))
        for s in self.geluid["klik"]:
            g.plak(buf, s, g.klik())
        n_in, n_uit = int(0.3 * g.SR), int(1.5 * g.SR)
        buf[:n_in] *= np.linspace(0, 1, n_in)
        buf[-n_uit:] *= np.linspace(1, 0, n_uit)
        st = np.stack([buf, np.concatenate([np.zeros(12), buf[:-12]])], axis=1)
        st = st / (np.abs(st).max() + 1e-9) * 0.7
        wav = TMP / f"{self.x}_geluid.wav"
        g.schrijf_wav(wav, st)
        mp4 = UIT / f"{self.naam}-geluid.mp4"
        ff("-i", str(stil), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
           "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-ac", "2",
           "-t", f"{duur:.3f}", "-movflags", "+faststart", str(mp4))
        (UIT / f"zoek-{self.x}-hoofdstukken.txt").write_text("".join(f"{t} {n}\n" for t, n in self.hoofdstukken))
        stap = duur / 12
        ff("-i", str(mp4), "-vf", f"fps=1/{stap:.3f},scale=480:-1,tile=4x3", "-frames:v", "1",
           str(UIT / f"zoek-{self.x}-overzicht.jpg"))
        print(f"klaar: {mp4} {duur:.1f} s")
        print((UIT / f"zoek-{self.x}-hoofdstukken.txt").read_text())
        return duur


def stappen_figuur(f, h, rig_tekst, lijst_tekst):
    """Rig, knop, lijst: het knippen op elk gewricht."""
    s, d = f.stuk("rig", "rig", hoofdstuk=h, onder=[(rig_tekst, 0, 99)])
    f.voeg(s, d, (0.05,))
    s, d = f.stuk("druk", "druk", houd=1.5, hoofdstuk=h, zooms=[("knop", None)],
                  onder=[("Click Joints Pro does the cutting: press Figure from rig.", 0, 99)])
    f.voeg(s, d, (0.05,))
    f.geluid["klik"].append(f.tijd - 0.1)
    s, d = f.stuk("lijst", "lijst", traag=1.25, hoofdstuk=h, zooms=[("lijst", None)],
                  onder=[(lijst_tekst, 0, 99)])
    f.voeg(s, d, (0.05,))


def buig(f, h, tekst):
    s, d = f.stuk("buig", "buig", hoofdstuk=h, zooms=[("hinge", None)], onder=[(tekst, 0, 99)])
    f.geluid["buig"].append((f.tijd + 0.7, 5.0))
    f.geluid["klik"].append(f.tijd + 5.7)
    f.voeg(s, d, (0.05,))


def rood(f, h):
    s, d = f.stuk("rood", "rood", hoofdstuk=h, zooms=[("hinge", None)],
                  onder=[(f"Push past {STOP}°: the arc turns red and shows how far you went.", 0, 99)])
    f.geluid["zoef"].append((f.tijd + 0.1, 1.5))
    f.voeg(s, d, (0.05,))
    s, d = f.stuk("terug", "terug", hoofdstuk=h, zooms=[("hinge", None)],
                  onder=[("Back inside the range, the red is gone.", 2.0, 99)])
    f.voeg(s, d, (2.0,))


def uitelkaar(f, h, regels, tot=None):
    s, d = f.stuk("uitelkaar", "uitelkaar", tot=tot, hoofdstuk=h, onder=regels)
    f.geluid["zoef"].append((f.tijd + 0.2, 2.0))
    f.voeg(s, d, tuple(a for _, a, _ in regels))


def export(f, h):
    s, d = f.stuk("export", "export", houd=2.0, hoofdstuk=h, zooms=[("export", None)],
                  onder=[(f"Export every part as STL or 3MF. Here: {N_EXPORT} parts as 3MF.", 0, 99)])
    f.geluid["klik"].append(f.tijd + 1.5)
    f.voeg(s, d, (0.05,))


GOED = ["Best on figures with separate arms and legs, about 200 mm tall.",
        "Measured in Blender, not print tested by us yet.",
        "Print a test joint first: every printer is different."]
RIG = "A rigged figure, 220 mm tall, 20 bones: the bones show where it bends."
LIJST = f"{N_GEW} joints: hinges at elbows and knees, ball joints at shoulders, hips and neck."


def video_a():
    f = Film("a", "zoek-a-articulated-3d-prints-blender")
    f.haak("uitelkaar", ("How to make articulated", "3D prints in Blender"),
           ["1  Cut the model where it bends.", "2  Put a joint in every cut, with clearance.",
            "3  Check the fit, export every part, print."])
    stappen_figuur(f, f.hoofdstuk("Cut where it bends"), RIG, LIJST)
    h = f.hoofdstuk("A joint in every cut")
    s, d = f.stuk("bogen", "bogen", hoofdstuk=h,
                  onder=[("Each joint shows how far it bends, in degrees.", 0, 5),
                         (f"Left knee {L_KNIE}°, left elbow {L_ELL}°: taken from the rig.", 5, 99)])
    f.voeg(s, d, (0.05, 5.0))
    buig(f, h, f"Hinges get an end stop: drag Bend and the knee stops at {STOP}°.")
    h = f.hoofdstuk("Check the fit and export")
    uitelkaar(f, h, [("Exploded view: every part and every joint before you print.", 0, 6),
                     ("Clearance is 0.2 mm by default. You can change it.", 6, 99)])
    export(f, h)
    f.goed(GOED)
    f.eind("Articulated 3D prints, in Blender.")
    return f.klaar()


def video_b():
    f = Film("b", "zoek-b-blender-hinge-3d-print")
    f.haak("buig", ("Blender hinge", "for 3D printing"),
           ["1  Cut the part where it should bend.", "2  Put a hinge in the cut, with clearance.",
            "3  Give it an end stop, so it stops where it should."], traag=1.4)
    stappen_figuur(f, f.hoofdstuk("Place the hinges"), "A rigged figure, 220 mm tall: elbows and knees get a hinge.",
                   "Each hinge gets a range: from your rig, mirrored, or a preset.")
    h = f.hoofdstuk("The end stop")
    s, d = f.stuk("bogen", "bogen", hoofdstuk=h,
                  onder=[("Next to every hinge: how far it bends, in degrees.", 0, 5),
                         (f"Left knee 0 to {L_KNIE}°, left elbow 0 to {L_ELL}°, from Limit Rotation.", 5, 99)])
    f.voeg(s, d, (0.05, 5.0))
    buig(f, h, f"Drag Bend: the right knee stops at {STOP}° (mirrored from the left).")
    rood(f, f.hoofdstuk("Past the stop"))
    h = f.hoofdstuk("Check and export")
    uitelkaar(f, h, [("Exploded view: see each hinge before you print. Clearance 0.2 mm.", 0, 99)], tot=200)
    export(f, h)
    f.goed(GOED)
    f.eind("A hinge with an end stop, in Blender.")
    return f.klaar()


def video_c():
    f = Film("c", "zoek-c-blender-split-model-3d-printing")
    f.haak("uitelkaar", ("Split a model for", "3D printing in Blender"),
           ["1  Split where the model bends, not just anywhere.", "2  Put a joint in every cut, so it moves.",
            "3  Export each part as its own STL or 3MF."])
    stappen_figuur(f, f.hoofdstuk("Split at the joints"), RIG, LIJST)
    h = f.hoofdstuk("See every part")
    uitelkaar(f, h, [("Exploded view: every part pulled apart, each with its joint.", 0, 6),
                     ("Clearance is 0.2 mm by default. You can change it.", 6, 99)])
    export(f, f.hoofdstuk("Export each part"))
    h = f.hoofdstuk("Make it move")
    buig(f, h, f"The parts still move: the knee hinge bends to {STOP}° and stops.")
    f.goed(["Already split with another tool? Put the 3D cursor on a joint and cut there."] + GOED[1:])
    f.eind("Split for printing. Make it move.")
    return f.klaar()


for x, fn in (("a", video_a), ("b", video_b), ("c", video_c)):
    if x in KEUZE:
        fn()
