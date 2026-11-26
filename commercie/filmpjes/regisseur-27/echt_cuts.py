"""Echte schermopname voor de lanceer-Short van Click Cuts (issue #135, Regisseur, 26 nov 2026).

Wens Thijs 25 nov 11:25: alsof iemand het op zijn eigen pc opnam. Dit script speelt alleen de gebruiker in echte
tijd; ffmpeg x11grab neemt het scherm op (neem_op.sh van regisseur-26) en glij.py beweegt de echte X-muis.
Verloop (verhaal uit het hoofdbeeld): het paard van 520 mm staat naast een kader van 256 mm (bed van de Bambu Lab
A1), de gebruiker klikt het paard, kiest de printer in de lijst, klikt Split to fit, draait de weergave met de
middelste muisknop, opent More settings en scrolt naar de lijst met groene delen, en zoomt met het wiel in op een
snijvlak met pengaten en nummer. Knoppen vindt het script met tesseract (zoals reeks 4); mist een echte klik, dan
drukt het script de knop zelf in en schrijft "KORT vangnet" in het log.
Model: Horse Statue 01 van Poly Haven (CC0), zoals het hoofdbeeld. Niets gerenderd, alles solid in de viewport.
    blender --gpu-backend opengl start.blend --python echt_cuts.py -- <map> <click_cuts.zip> <modelmap>"""
import json
import math
import os
import subprocess
import sys
import time

import bmesh
import bpy
from mathutils import Matrix, Quaternion, Vector

a = sys.argv[sys.argv.index("--") + 1:]
MAP, ZIP, MODEL = a[0], a[1], a[2]
HIER = os.path.dirname(os.path.abspath(__file__))
GLIJ = os.path.join(HIER, "..", "regisseur-26", "glij.py")
HOOGTE = 520.0
UI = 2.0
BREED_ZIJBALK = 1080
film = {"delen": {}, "kliks": [], "metingen": {}, "echt": True}
MUIS = {"x": 540, "y": 1000}


def log(t):
    print(f"[cuts] {t}", flush=True)


def xdo(*args):
    subprocess.run(["xdotool", *args], capture_output=True, text=True)


def deel(naam):
    film["delen"][naam] = round(time.time(), 3)
    log(f"deel {naam} {time.time():.3f}")


def zacht(t):
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- scherm
def gebied_3d():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                return venster, gebied
    return None, None


def rect(soort="UI"):
    venster, gebied = gebied_3d()
    r = next(r for r in gebied.regions if r.type == soort)
    return [venster.x + r.x, venster.y + venster.height - (r.y + r.height), r.width, r.height]


def scherm_punt(p):
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    venster, gebied = gebied_3d()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    q = location_3d_to_region_2d(regio, gebied.spaces.active.region_3d, Vector(p))
    if q is None:
        return None
    return int(venster.x + regio.x + q.x), int(venster.y + venster.height - (regio.y + q.y))


def herteken():
    for w in bpy.context.window_manager.windows:
        for ar in w.screen.areas:
            ar.tag_redraw()


def ocr(tekst, vak=None, niet=None):
    """Plek (x, y) op het X-scherm van `tekst` volgens tesseract, of None (zelfde werkwijze als reeks 4)."""
    pad = "/tmp/cc_ocr.png"
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    vak = vak or rect("UI")
    x0, y0, b, h = vak
    subprocess.run(["convert", pad, "-crop", f"{b}x{h}+{x0}+{y0}", "+repage", "-colorspace", "Gray", "-threshold",
                    "65%", "-negate", "/tmp/cc_ocr_v.png"], capture_output=True)
    r = subprocess.run(["tesseract", "/tmp/cc_ocr_v.png", "stdout", "--psm", "11", "tsv"], capture_output=True,
                       text=True)
    regels = {}
    for regel in r.stdout.splitlines()[1:]:
        d = regel.split("\t")
        if len(d) == 12 and d[11].strip():
            woord = d[11].strip().lower().strip(".,:;(){}[]'\"")
            woord = {"al": "a1", "ai": "a1", "a]": "a1"}.get(woord, woord)   # tesseract leest A1 vaak als "al"
            w = (woord, int(d[6]), int(d[7]), int(d[8]), int(d[9]))
            regels.setdefault((d[2], d[3], d[4]), []).append(w)
    doel = tekst.lower().split()
    for ws in regels.values():
        ws.sort(key=lambda w: w[1])
        for i in range(len(ws) - len(doel) + 1):
            if all(ws[i + j][0] == doel[j] for j in range(len(doel))):
                if niet and i + len(doel) < len(ws) and ws[i + len(doel)][0] == niet:
                    continue
                s = ws[i:i + len(doel)]
                xa, xb = min(w[1] for w in s), max(w[1] + w[3] for w in s)
                ya, yb = min(w[2] for w in s), max(w[2] + w[4] for w in s)
                return x0 + (xa + xb) // 2, y0 + (ya + yb) // 2
    alles = " ".join(w[0] for ws in regels.values() for w in ws)
    log(f"KORT ocr niet gevonden: {tekst!r} ({alles[:300]})")
    return None


def zoek(tekst, keer=5, vak=None):
    for _ in range(keer):
        r = ocr(tekst, vak)
        if r:
            return r
        yield 0.6
    return None


# ---------------------------------------------------------------- muis
def muis_naar(x, y, duur=None, boog=1.0):
    """Echte muis glijdt in een eigen proces (90 keer per seconde); duur naar de afstand zoals een hand."""
    if duur is None:
        duur = max(0.35, min(1.1, 0.3 + math.hypot(x - MUIS["x"], y - MUIS["y"]) / 1800.0))
    p = subprocess.Popen(["python3", GLIJ, str(MUIS["x"]), str(MUIS["y"]), str(int(x)), str(int(y)),
                          f"{duur:.3f}", str(boog)])
    while p.poll() is None:
        yield 0.01
    MUIS["x"], MUIS["y"] = int(x), int(y)
    yield 0.12


def klik(knop="1"):
    xdo("click", knop)
    film["kliks"].append(round(time.time(), 3))


def wacht(s):
    t0 = time.time()
    while time.time() - t0 < s:
        yield 0.02


def wiel(knop, keer, tussen=0.07):
    for _ in range(keer):
        xdo("click", knop)
        yield tussen


def zweef(s, r=55):
    """Wachten zoals een mens: de hand rust niet, de muis drijft in kleine bogen rond de plek waar hij was
    (wens Thijs 26 nov 08:48: geen shot langer dan ±2 s zonder beweging)."""
    t0 = time.time()
    x0, y0 = MUIS["x"], MUIS["y"]
    k = 0
    while True:
        rest = s - (time.time() - t0) - 0.12
        if rest < 0.3:
            break
        d = min(0.95, rest)
        hoek = 2.1 * k + 0.6
        yield from muis_naar(x0 + r * math.cos(hoek), y0 + 0.6 * r * math.sin(hoek), duur=d, boog=0.8)
        k += 1
    yield from wacht(max(0.0, s - (time.time() - t0)))


def sleep_middel(dx, dy, duur):
    """Weergave draaien zoals een gebruiker: middelste muisknop vast, muis rustig opzij, los."""
    xdo("mousedown", "2")
    yield 0.1
    yield from muis_naar(MUIS["x"] + dx, MUIS["y"] + dy, duur=duur, boog=0.3)
    xdo("mouseup", "2")
    yield 0.2


# ---------------------------------------------------------------- scène
def srgb(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple((x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4) for x in c) + (1.0,)


def laad_paard():
    s = bpy.context.scene
    for o in list(s.objects):
        bpy.data.objects.remove(o)
    s.unit_settings.system, s.unit_settings.scale_length, s.unit_settings.length_unit = "METRIC", 0.001, "MILLIMETERS"
    naam = os.path.basename(MODEL.rstrip("/"))
    bpy.ops.import_scene.gltf(filepath=os.path.join(MODEL, f"{naam}_1k.gltf"))
    ob = [o for o in s.objects if o.type == "MESH"][0]
    for o in list(s.objects):
        if o is not ob:
            bpy.data.objects.remove(o)
    ob.name = "Horse"
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    zs = [v.co.z for v in ob.data.vertices]
    ob.data.transform(Matrix.Scale(HOOGTE / (max(zs) - min(zs)), 4))
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.05)
    bm.to_mesh(ob.data)
    bm.free()
    ps = [v.co for v in ob.data.vertices]
    mn = Vector([min(p[i] for p in ps) for i in range(3)])
    mx = Vector([max(p[i] for p in ps) for i in range(3)])
    ob.data.transform(Matrix.Translation(Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z))))
    ob.data.materials.clear()
    ob.color = srgb("E9DFCF")
    film["metingen"]["paard_mm"] = [round(v, 1) for v in (mx - mn)]
    # kader van het bed (256 mm, Bambu Lab A1): een draadkubus in de scène van de gebruiker, geen add-on-functie
    bpy.ops.mesh.primitive_cube_add(size=256.0, location=(0, 0, 128.0))
    bed = bpy.context.active_object
    bed.name = "A1 bed 256 mm"
    bed.display_type = "WIRE"
    bed.show_in_front = True
    bed.color = srgb("FFC94A")
    bed.hide_select = True
    for o in s.objects:
        o.select_set(False)
    s.view_layers[0].objects.active = None
    log(f"KORT paard {film['metingen']['paard_mm']} mm, {len(ob.data.polygons)} vlakken")
    return ob, bed


def kijk():
    venster, gebied = gebied_3d()
    sp = gebied.spaces.active
    sp.shading.type, sp.shading.light, sp.shading.color_type = "SOLID", "STUDIO", "OBJECT"
    sp.shading.show_cavity = True
    sp.shading.cavity_type = "WORLD"
    sp.shading.show_shadows = False
    sp.shading.wireframe_color_type = "OBJECT"   # het kader van het bed in goud
    sp.clip_start, sp.clip_end = 0.5, 100000
    ov = sp.overlay
    ov.show_floor, ov.show_axis_x, ov.show_axis_y, ov.show_cursor = True, False, False, False
    ov.show_stats = False
    sp.show_region_header = True
    sp.show_region_tool_header = False
    sp.show_region_toolbar = False
    sp.show_region_ui = True
    pr = bpy.context.preferences
    pr.view.ui_scale = UI
    pr.system.use_region_overlap = False
    pr.view.show_tooltips = False
    pr.inputs.use_zoom_to_mouse = True


def zet_weergave(rot, midden, afstand):
    _, gebied = gebied_3d()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "PERSP"
    rv.view_rotation = rot
    rv.view_location = midden
    rv.view_distance = afstand


def weergave_start():
    rot = Quaternion((0, 0, 1), math.radians(28)) @ Quaternion((1, 0, 0), math.radians(76))
    zet_weergave(rot, Vector((0, 0, 250.0)), float(os.environ.get("CC_AFSTAND", "900")))


def tabblad():
    venster, gebied = gebied_3d()
    ui = next(r for r in gebied.regions if r.type == "UI")
    if ui.active_panel_category == "Click Cuts":
        return True
    x = venster.x + ui.x + ui.width - 8
    y = venster.y + venster.height - (ui.y + ui.height // 2)
    xdo("mousemove", str(x), str(y))
    xdo("keydown", "ctrl")
    xdo("click", "5")
    xdo("keyup", "ctrl")
    return False


def sleep_zijbalk(breed):
    for dx in (2, 6, 12, 18):
        z = rect("UI")
        if z[2] >= breed - 20:
            break
        x, y = z[0] + dx, z[1] + 300
        xdo("mousemove", str(x), str(y))
        yield 0.3
        xdo("mousedown", "1")
        yield 0.2
        doel = z[0] + z[2] - breed
        for i in range(1, 13):
            xdo("mousemove", str(int(x + (doel - x) * i / 12)), str(y))
            yield 0.05
        yield 0.2
        xdo("mouseup", "1")
        yield 0.4
        log(f"KORT zijbalk dx={dx}: {rect('UI')}")


def gat_voor_close_up(stukken):
    """Het snijvlak met een nummer dat het meest naar de kijker wijst: (punt, normaal naar buiten)."""
    _, gebied = gebied_3d()
    rv = gebied.spaces.active.region_3d
    kijk_r = rv.view_rotation @ Vector((0, 0, 1))   # van het midden naar de kijker
    best = None
    for o in stukken:
        mid = Vector(o.get("sj_midden_mm", (0, 0, 0)))
        for g in json.loads(o.get("sj_gaten", "[]")):
            p = Vector(g["p"])
            n = Vector((0, 0, 0))
            n[g["as"]] = 1.0 if p[g["as"]] > mid[g["as"]] else -1.0
            score = n.dot(kijk_r)
            if best is None or score > best[0]:
                best = (score, o, p, n)
    return best


# ---------------------------------------------------------------- verloop
def verloop():
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    yield 1.0
    paard, bed = laad_paard()
    kijk()
    herteken()
    yield 1.0
    for _ in range(14):
        if tabblad():
            break
        yield 0.5
    yield 0.5
    yield from sleep_zijbalk(BREED_ZIJBALK)
    weergave_start()
    xdo("mousemove", str(MUIS["x"]), str(MUIS["y"]))
    yield 1.5
    film["metingen"]["zijbalk"] = rect("UI")
    film["metingen"]["weergave"] = rect("WINDOW")

    # 1. vanaf seconde 0 beweging (Thijs 26 nov): de gebruiker draait de weergave rustig om het paard heen, dat ver
    #    boven het gouden kader van het bed uitsteekt; daarna draait hij terug naar de voorkant
    w = rect("WINDOW")
    yield from muis_naar(w[0] + w[2] // 2 - 110, w[1] + w[3] // 2 + 150, duur=0.4)
    deel("heel")
    yield from sleep_middel(220, 0, 2.6)
    deel("heel2")
    yield from sleep_middel(-220, 0, 2.4)
    yield from zweef(1.2)

    # 2. klik het paard
    p = scherm_punt((0, 0, HOOGTE * 0.55)) or (540, 900)
    yield from muis_naar(p[0] + 30, p[1])
    yield from wacht(0.25)
    klik()
    deel("kies")
    yield 0.4
    if not paard.select_get():
        log("KORT vangnet: paard niet gekozen door de klik")
        paard.select_set(True)
        bpy.context.view_layer.objects.active = paard
    yield from zweef(1.2, r=35)

    # 3. printer kiezen in de lijst (Blender opent de lijst met de huidige keus onder de muis)
    inst = bpy.context.scene.split_joints
    inst.printer = "A1MINI"   # begin op de kleine A1 mini, zodat de gebruiker echt iets kiest
    herteken()
    yield 0.4
    q = yield from zoek("Bambu Lab A1 mini")
    if q:
        yield from muis_naar(q[0], q[1])
        deel("printer")
        yield from wacht(0.3)
        klik()
        yield from wacht(0.8)
        # in de open lijst staat "Bambu Lab A1" (zonder mini) als eigen regel, direct onder A1 mini
        z = rect("UI")
        doel = ocr("Bambu Lab A1", vak=[max(0, z[0] - 300), 0, z[2] + 300, 1920], niet="mini")
        if doel is None:
            doel = (q[0], q[1] + int(21 * UI))
        film["metingen"]["printer_regel"] = [q, doel]
        yield from muis_naar(doel[0], doel[1], duur=0.5, boog=0.2)
        yield from wacht(0.35)
        klik()
        yield 0.5
    else:
        deel("printer")
    if inst.printer != "A1":
        log(f"KORT vangnet printer: {inst.printer} in plaats van A1")
        xdo("key", "Escape")
        inst.printer = "A1"
        herteken()
    film["metingen"]["printer"] = inst.printer
    yield from zweef(0.8, r=30)

    # 4. Split to fit
    q = yield from zoek("Split to fit")
    if q:
        yield from muis_naar(q[0], q[1])
    yield from wacht(0.4)
    deel("knop")
    klik()
    t0 = time.time()
    yield 0.5
    stukken = [o for o in bpy.context.scene.objects if o.get("sj_stuk")]
    if not stukken:
        log("KORT vangnet: Split to fit niet door de klik, script drukt de knop")
        bpy.context.view_layer.objects.active = paard
        paard.select_set(True)
        bpy.ops.split_joints.split_to_fit()
        stukken = [o for o in bpy.context.scene.objects if o.get("sj_stuk")]
    film["metingen"]["split_s"] = round(time.time() - t0, 1)
    bed.hide_set(True)
    herteken()
    deel("klaar")
    pennen = sum(int(o["sj_pennen"]) for o in bpy.context.scene.objects if o.get("sj_pennen"))
    film["metingen"]["stukken"] = len(stukken)
    film["metingen"]["groen"] = sum(1 for o in stukken if o.get("sj_status") == "groen")
    film["metingen"]["pennen"] = pennen
    log(f"KORT split {len(stukken)} stukken, {film['metingen']['groen']} groen, {pennen} pennen, "
        f"{film['metingen']['split_s']} s")
    yield from zweef(2.0, r=45)

    # 5. draaien met de middelste muisknop
    w = rect("WINDOW")
    yield from muis_naar(w[0] + w[2] // 2, w[1] + w[3] // 2)
    deel("draai")
    yield from sleep_middel(-260, 20, 2.2)
    yield from zweef(1.0, r=40)

    # 6. More settings open, scrollen naar de lijst met delen
    q = yield from zoek("More settings")
    if q:
        yield from muis_naar(q[0], q[1])
        yield from wacht(0.3)
        klik()
    yield 0.6
    if not inst.meer:
        log("KORT vangnet: More settings")
        inst.meer = True
        herteken()
    deel("lijst")
    yield from wacht(0.8)
    z = rect("UI")
    yield from muis_naar(z[0] + z[2] // 2, z[1] + z[3] // 2, duur=0.5)
    for _ in range(4):
        yield from wiel("5", 3, 0.09)
        yield from wacht(0.25)
    deel("lijst_onder")
    yield from zweef(2.5, r=40)

    # 7. dichtbij: klik het bovenste stuk (het hoofd), lokale weergave (numpad /), draai naar het snijvlak met
    #    pengaten en nummer, en zoom met het wiel in
    kop = max(stukken, key=lambda o: Vector(o.get("sj_midden_mm", (0, 0, 0))).z)
    gaten = json.loads(kop.get("sj_gaten", "[]"))
    if gaten:
        film["metingen"]["close_up_stuk"] = int(kop["sj_stuk"])
        mid = kop.matrix_world @ Vector(kop.get("sj_midden_mm", (0, 0, 0)))
        q = scherm_punt(mid)
        if q:
            yield from muis_naar(q[0], q[1])
            yield from wacht(0.3)
            klik()
            yield 0.4
        if not kop.select_get():
            log("KORT vangnet: hoofd niet gekozen door de klik")
            for o in bpy.context.selected_objects:
                o.select_set(False)
            kop.select_set(True)
            bpy.context.view_layer.objects.active = kop
        yield from wacht(0.6)
        deel("zoom")
        xdo("key", "KP_Divide")
        yield from wacht(1.2)
        # het vlak met de meeste gaten
        tel = {}
        for g in gaten:
            p = Vector(g["p"])
            kant = 1.0 if p[g["as"]] > Vector(kop.get("sj_midden_mm", (0, 0, 0)))[g["as"]] else -1.0
            tel.setdefault((g["as"], kant), []).append(p)
        (asn, kant), punten = max(tel.items(), key=lambda kv: len(kv[1]))
        vlak = kop.matrix_world @ (sum(punten, Vector()) / len(punten))
        n = Vector((0, 0, 0))
        n[asn] = kant
        film["metingen"]["close_up_vlak"] = [asn, kant, len(punten)]
        _, gebied = gebied_3d()
        rv = gebied.spaces.active.region_3d
        van_rot, van_loc, van_d = rv.view_rotation.copy(), rv.view_location.copy(), rv.view_distance
        schuin = Vector((0.12, -0.15, 0.0)) if asn == 2 else Vector((0, 0, 0.2))   # bijna recht op het vlak
        naar_rot = (n + schuin).normalized().to_track_quat("Z", "Y")
        w = rect("WINDOW")
        yield from muis_naar(w[0] + w[2] // 2, w[1] + w[3] // 2 + 200)
        xdo("mousedown", "2")
        t0 = time.time()
        p0 = (MUIS["x"], MUIS["y"])
        while True:
            t = min(1.0, (time.time() - t0) / 1.8)
            e = zacht(t)
            rv.view_rotation = van_rot.slerp(naar_rot, e)
            rv.view_location = van_loc.lerp(vlak, e)
            rv.view_distance = van_d + (float(os.environ.get("CC_DICHT", "260")) - van_d) * e
            xdo("mousemove", str(int(p0[0] + 160 * e)), str(int(p0[1] - 260 * e)))
            if t >= 1.0:
                break
            yield 0.01
        xdo("mouseup", "2")
        MUIS["x"], MUIS["y"] = int(p0[0] + 160), int(p0[1] - 260)
        yield from wacht(0.5)
        q = scherm_punt(vlak)
        if q:
            yield from muis_naar(q[0] + 40, q[1] + 30, duur=0.6)
        for _ in range(2):
            yield from wiel("4", 1, 0.08)
            yield from wacht(0.25)
        deel("zoom_dicht")
        yield from zweef(3.0, r=50)
    deel("eind")
    yield from wacht(1.0)
    with open(os.path.join(MAP, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"KORT klaar {json.dumps(film['metingen'])}")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None
    except Exception as e:   # noqa: BLE001
        import traceback
        traceback.print_exc()
        log(f"KORT FOUT {e!r}")
        with open(os.path.join(MAP, "film.json"), "w") as f:
            json.dump(film, f, indent=1)
        bpy.ops.wm.quit_blender()
        return None


bpy.app.timers.register(stap, first_interval=3.0)
