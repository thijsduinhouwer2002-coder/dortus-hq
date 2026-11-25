"""Echte schermopname voor de sale-Shorts van issue #75 (Regisseur run 29, 25 nov 2026).

Wens Thijs 25 nov 11:25: het moet eruitzien alsof iemand het op zijn eigen pc opnam. Daarom anders dan regisseur-14:
- Geen losse schermafdrukken per beeld meer. De workflow neemt het hele X-scherm op met ffmpeg x11grab (30 beelden per
  seconde, echte muispijl met -draw_mouse). Dit script speelt alleen de gebruiker, in echte tijd.
- De muis glijdt in een eigen proces (glij.py, 90 keer per seconde), dus hij springt niet als Blender traag tekent.
- De Bend-schuif wordt echt versleept (muisknop omlaag, slepen, los), niet door het script gezet. Eerst een korte
  sleep om de maat van de schuif te meten, dan tot de stop, dan voorbij de stop (rood), dan terug.
- Geen studio-renders (het eerste beeld komt uit release regisseur-14/24, al gerenderd).
Verder het verloop van regisseur-14 (robot van studio-3, echte klik op de robot, Figure from rig, onderbeen, knie,
Exploded view, export), met Click Joints Pro 1.2.8 (de versie die kopers in de sale krijgen).
Tijden: film.json "delen" en "kliks" in wandkloktijd (time.time()); de workflow schrijft de starttijd van ffmpeg in
start.txt, zodat de montage weet op welke seconde van de opname elk deel begint.
    blender --gpu-backend opengl start.blend --python echt_opname.py -- <map> <betaalde zip>"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
R14 = os.path.abspath(os.path.join(HIER, "..", "regisseur-14", "opname.py"))
GLIJ = os.path.join(HIER, "glij.py")
r14 = open(R14, encoding="utf-8").read()

HULP = r'''
from scherm_basis import xdo  # noqa: E402
film["kliks"] = []
film["echt"] = True
GLIJ = GLIJ_PAD


def neem(houd=1):
    """Echte tijd: een stilstand van houd beelden is houd/30 seconde wachten (het scherm wordt toch opgenomen)."""
    if houd > 2:
        time.sleep(houd / 30.0)


def deel(naam):
    film["delen"][naam] = round(time.time(), 3)
    log(f"deel {naam} {time.time():.3f}")
'''

STUK_MUIS = r'''def stuk(stappen, doe):
    """Echte tijd: stappen/30 seconde lang, zo vaak als Blender tekent."""
    duur = stappen / 30.0
    t0 = time.time()
    while True:
        t = min(1.0, (time.time() - t0) / duur)
        doe(zacht(t))
        if t >= 1.0:
            break
        yield 0.001
    yield 0.001


def _glij(x, y, duur, boog=1.0):
    return subprocess.Popen(["python3", GLIJ, str(MUIS["x"]), str(MUIS["y"]), str(int(x)), str(int(y)),
                             f"{duur:.3f}", str(boog)])


def muis_naar(x, y, stappen=18, doe=None, duur=None, boog=1.0):
    """Echte muis glijdt in een eigen proces; duur naar de afstand zoals een hand (0,3 tot 1,1 s)."""
    if duur is None:
        afstand = math.hypot(x - MUIS["x"], y - MUIS["y"])
        duur = stappen / 30.0 if stappen >= 60 else max(0.3, min(1.1, 0.28 + afstand / 1800.0))
    p = _glij(x, y, duur, boog)
    t0 = time.time()
    while True:
        t = min(1.0, (time.time() - t0) / duur)
        if doe is not None:
            doe(zacht(t))
        if t >= 1.0:
            break
        yield 0.001
    p.wait()
    MUIS["x"], MUIS["y"] = int(x), int(y)
    yield 0.15


def sleep_tot(doel, rand_x, snelheid=330.0):
    """Echt slepen tot de waarde van Bend het doel haalt: knop omlaag, de muis glijdt rustig naar rand_x, en zodra
    Blender het doel laat zien stopt de hand en laat los. Nodig omdat de schuif van Blender niet overal even snel gaat
    (lokale proeven 25 nov: eerste sleep 6,9 px per graad, de volgende 4,7)."""
    wm = bpy.context.window_manager
    yield 0.8
    yield from muis_naar(MUIS["x"] + 6 * (1 if rand_x > MUIS["x"] else -1), MUIS["y"], duur=0.2, boog=0.0)
    omhoog = doel > float(wm.cj_scharnier_pose)
    xdo("mousedown", "1")
    film["kliks"].append(round(time.time(), 3))
    yield 0.15
    duur = max(0.4, abs(rand_x - MUIS["x"]) / snelheid)
    p = _glij(rand_x, MUIS["y"], duur, 0.0)
    t0 = time.time()
    while p.poll() is None and time.time() - t0 < duur + 1.0:
        v = float(wm.cj_scharnier_pose)
        if (omhoog and v >= doel) or (not omhoog and v <= doel):
            p.terminate()
            break
        yield 0.001
    p.wait()
    r = subprocess.run(["xdotool", "getmouselocation", "--shell"], capture_output=True, text=True).stdout
    w = dict(x.split("=", 1) for x in r.split() if "=" in x)
    MUIS["x"], MUIS["y"] = int(w.get("X", MUIS["x"])), int(w.get("Y", MUIS["y"]))
    yield 0.25
    xdo("mouseup", "1")
    yield 0.25
    return float(wm.cj_scharnier_pose)


def typ_waarde(w, x):
    """Echt typen in de schuif: klik (zonder slepen opent Blender het getal), alles kiezen, getal typen, Enter."""
    wm = bpy.context.window_manager
    yield 0.5
    yield from muis_naar(x, MUIS["y"], duur=0.35, boog=0.0)
    yield 0.25
    klik()
    yield 0.5
    xdo("key", "ctrl+a")
    yield 0.2
    xdo("type", "--delay", "110", f"{w:g}")
    yield 0.4
    xdo("key", "Return")
    yield 0.4
    return float(wm.cj_scharnier_pose)


def sleep_schuif(x1, duur):
    """Echt slepen: knop omlaag, zacht naar x1 (zelfde hoogte), even vasthouden, los. Eerst 0,8 s rust en een
    klein schuifje van de muis: een tweede druk vlak na het loslaten telt anders als dubbelklik en dan opent Blender
    het getal om te typen (lokale proef 25 nov: tweede sleep bleef op 77 in plaats van 120)."""
    yield 0.8
    yield from muis_naar(MUIS["x"] + 6, MUIS["y"], duur=0.2, boog=0.0)
    xdo("mousedown", "1")
    film["kliks"].append(round(time.time(), 3))
    yield 0.15
    yield from muis_naar(x1, MUIS["y"], duur=duur, boog=0.0)
    yield 0.2
    xdo("mouseup", "1")
    yield 0.25


'''

KLIK_OUD = '''def klik():
    xdo("click", "1")
    MUIS["klik"] = 1'''
KLIK_NIEUW = '''def klik():
    xdo("click", "1")
    MUIS["klik"] = 1
    film["kliks"].append(round(time.time(), 3))'''

SCHUIF_BEGIN = "    yield from muis_naar(sx0, schuif[1], 22)\n"
SCHUIF_EIND = "doe=lambda t: buig(b, stop + VOORBIJ - (stop + VOORBIJ - 70.0) * t))\n"
SCHUIF_NIEUW = r'''    wm = bpy.context.window_manager
    z = rect("UI")
    links, midden = z[0] + 70, z[0] + z[2] // 2
    yield from muis_naar(links, schuif[1], 22)
    s = math.floor(stop * 10) / 10
    neem_m(12)
    # een echte sleep vanaf 0 (die gaat altijd goed: drie proeven 54,4 tot 54,7 graden), daarna typen: de schuif van
    # Blender gaat bij een tweede sleep niet even snel (proeven 25 nov), typen geeft de stop precies
    yield from sleep_schuif(links + s * 0.5 * (z[2] - 140) / 150.0, 1.1)
    v1 = float(wm.cj_scharnier_pose)
    neem_m(12)
    v2 = yield from typ_waarde(s, midden)
    log(f"KORT schuif {v1:.1f} dan {v2:.1f} (doel {s:.1f})")
    if abs(v2 - s) > 1.0:
        log(f"KORT vangnet schuif: {v2:.1f} in plaats van {s:.1f}, script zet de stand")
        buig(b, s)
    deel("knie_stop")
    neem_m(45)
    film["metingen"]["knie_pose_stop"] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    film["metingen"]["schuif_stop"] = round(v2, 1)
    deel("knie_rood")
    v3 = yield from typ_waarde(round(stop + 15.0), midden)
    neem_m(60)
    film["metingen"]["knie_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
    film["metingen"]["knie_pose_rood"] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    film["metingen"]["schuif_rood"] = round(v3, 1)
    v4 = yield from typ_waarde(70, midden)
    log(f"KORT schuif rood {v3:.1f}, terug {v4:.1f}")
'''



GEEN_RENDER = '''

def renders(p):
    log("KORT render overgeslagen (regisseur-26: eerste beeld uit release regisseur-14 en -24)")
    yield 0.1
'''

PATCH = f'''
_r26 = {{"HULP": {HULP!r}, "STUK_MUIS": {STUK_MUIS!r}, "KLIK_OUD": {KLIK_OUD!r}, "KLIK_NIEUW": {KLIK_NIEUW!r},
        "SB": {SCHUIF_BEGIN!r}, "SE": {SCHUIF_EIND!r}, "SN": {SCHUIF_NIEUW!r}, "GR": {GEEN_RENDER!r},
        "GLIJ": {GLIJ!r}}}
_oud = "from scherm_basis import xdo  # noqa: E402\\n"
assert src.count(_oud) == 1
src = src.replace(_oud, _r26["HULP"].replace("GLIJ_PAD", repr(_r26["GLIJ"])))
_i, _j = src.index("def stuk(stappen, doe):"), src.index("def klik():")
src = src[:_i] + _r26["STUK_MUIS"] + src[_j:]
assert src.count(_r26["KLIK_OUD"]) == 1
src = src.replace(_r26["KLIK_OUD"], _r26["KLIK_NIEUW"])
_i = src.index(_r26["SB"]); _j = src.index(_r26["SE"]) + len(_r26["SE"])
src = src[:_i] + _r26["SN"] + src[_j:]
_oud = "\\nrenders = renders_robot\\n"
assert src.count(_oud) == 1
src = src.replace(_oud, "\\nrenders = renders_robot\\n" + _r26["GR"])
'''

_haak = 'g = {"__name__": "__main__", "__file__": BRON}'
assert r14.count(_haak) == 1
r14 = r14.replace(_haak, PATCH + _haak)
r14 = r14.replace("HIER = os.path.dirname(os.path.abspath(__file__))", f"HIER = {os.path.dirname(R14)!r}", 1)
exec(compile(r14, R14, "exec"), {"__name__": "__main__", "__file__": R14})   # noqa: S102 (eigen code uit de repo)
