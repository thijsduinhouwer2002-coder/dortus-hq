"""Hoofdbeeld Click Joints Pro met de robot-actiefiguur (25 nov 2026, Beeldmaker, issue #1).

Waarom: blinde test 24 nov, beide rechters: "een gedetailleerd, gestileerd personage in plaats van de tekenpop".
Figuur: de robot uit commercie/filmpjes/studio/figuur_robot.py (eigen werk van Dortus, geen download, geen AI).
De gewrichten maakt de echte knop Figure from rig van Click Joints Pro (zip van main, 1.2.8). Niets is nagetekend:
kogels, kommen en scharnieren zijn de vormen die de add-on maakte, alleen in een goudkleur gezet.

    blender -b --factory-startup --python hoofdbeeld.py -- <pro-zip> <uitmap> [samples] [schaal%]
Uit: hoofdbeeld-render.png (2400x1350, zonder tekst) en hoofdbeeld.json (gewrichten van de add-on en waar ze in
beeld staan, voor de labels). De tekst komt erop met tekst.py (Pillow).
"""
import importlib
import json
import math
import os
import sys
import time

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.abspath(os.path.join(HIER, "..", "..", "..", "commercie", "filmpjes", "studio"))
sys.path.insert(0, STUDIO)
import figuur_laden as FL  # noqa: E402
import figuur_robot as R  # noqa: E402
import studio as S  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
ZIP, UIT = args[0], args[1]
SAMPLES = int(args[2]) if len(args) > 2 else 128
SCHAAL = int(args[3]) if len(args) > 3 else 100
UIT_MM = float(os.environ.get("HB_UIT", "36"))
os.makedirs(UIT, exist_ok=True)
meting = {"figuur": "robot (figuur_robot.py, eigen werk)", "uit_mm": UIT_MM}


def log(*a):
    print("[hoofdbeeld]", *a, flush=True)


def srgb(h):
    return S.srgb(h)


def mat(naam, kleur, rough=0.4, metal=0.0, emis=0.0, coat=0.0):
    m = bpy.data.materials.get(naam) or bpy.data.materials.new(naam)
    m.use_nodes = True
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    b = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(b.outputs[0], o.inputs["Surface"])
    b.inputs["Base Color"].default_value = srgb(kleur)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if coat:
        b.inputs["Coat Weight"].default_value = coat
    if emis:
        b.inputs["Emission Color"].default_value = srgb(kleur)
        b.inputs["Emission Strength"].default_value = emis
    return m


def delen_van(naam):
    return [o for o in bpy.context.scene.objects if o.type == "MESH" and o.get("cj_figuur") == naam and o.visible_get()]


def paar(naam):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_soort", "") == "SCHARNIER":
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def buig(naam, graden):
    a, b = paar(naam)
    if b is None:
        return None
    stop = float(a.get("cj_bereik_graden", 0) or 0) if a is not None else 0
    g = min(graden, stop) if stop else graden
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(g, 1)
    bpy.context.view_layer.update()
    return round(float(b.get("cj_pose_graden", g)), 1), stop


def figuur():
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    keuze = os.environ.get("HB_FIGUUR", "robot")   # "mens": MakeHuman base (CC0), aangekleed (#101 ronde 2)
    arm, ob, _p = FL.laad_figuur(keuze, 220.0)
    if keuze == "mens":
        meting["figuur"] = "MakeHuman base mesh (CC0 1.0, commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md), aangekleed door figuur_laden.py"
    elif keuze not in ("robot", "tekenpop"):   # #285: eigen .blend of .glb met rig
        meting["figuur"] = os.environ.get("HB_FIGUUR_BRON", keuze)
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    naam = ob.name
    FL.actief(ob)
    t0 = time.time()
    r = bpy.ops.click_joints.figuur_uit_rig()
    meting["knop_s"] = round(time.time() - t0, 1)
    log("Figure from rig", r, meting["knop_s"], "s")
    arm.hide_set(True)
    arm.hide_render = True
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    meting["gewrichten"] = [fig.regel(x) for x in lijst]
    meting["records"] = [{"naam": x.get("naam"), "soort": x.get("soort"), "graden": x.get("graden"),
                          "punt": list(x.get("punt", ()))} for x in lijst]
    log("gewrichten", len(lijst), meting["gewrichten"])
    try:
        bpy.context.window_manager.cj_scharnier_boog = False
        inst.toon_bereik = False
    except Exception:  # noqa: BLE001
        pass
    return naam, delen_van(naam)


GOUD_PLEK = {}   # gewricht -> [(object, vlak)] van de gouden vlakken, voor de labels
BOOG_RUST = {}   # scharnier -> gradenboog van de add-on in rusthouding (#38 ronde 4)
AS_PLEK = {}     # scharnier -> (drager, punt lokaal, as lokaal), voor labels op de as en de knie-camera


def goud_gewrichten(delen):
    """Kogel, nek, kom en scharnier in goud, zoals op onze tekenpop-cover. kleur_herstel maakt de vlakken van de
    add-on antraciet; hier worden de antraciete vlakken (en vlakken zonder kleur) dicht bij een gewricht goud.
    Alleen de kleur verandert, niet de vorm. Moet in rusthouding (vóór poseer)."""
    goud = mat("hb_goud", os.environ.get("HB_GOUD", "FFB938"), rough=0.28, metal=float(os.environ.get("HB_METAAL", "0.55")), coat=0.3)
    zones = {}
    for o in bpy.context.scene.objects:
        n = o.get("cj_naam")
        if not n or n in zones or not o.get("cj_figuur"):
            continue
        if o.get("cj_soort") == "KOGEL" and "cj_centrum" in o:
            zones[n] = (Vector(o["cj_centrum"]), Vector(o["cj_snijpunt"]), float(o["cj_kogel_r"]) * 1.25)
        elif o.get("cj_soort") == "SCHARNIER" and "cj_scharnier_punt" in o:
            c = Vector(o["cj_scharnier_punt"])
            r = max(float(o.get("cj_breedte", 8)) * 0.85, float(o.get("cj_knokkel_r", 2)) * 4.5)
            zones[n] = (c, c, r)
    # #38 M3 (Daan #156): het label van een scharnier wijst naar de as zelf, niet naar het midden van het goud
    # (dat lag bij de elleboog op de hand). Punt en as vastgemaakt aan het deel waar het scharnier aan vastzit
    # (bovenarm, bovenbeen = deel B van schouder of heup, R.KETEN), in rusthouding. Deel A kan niet: dat object is na
    # latere sneden de romp; deel B (onderarm) schuift bij "uit elkaar" weg van de as.
    for o in bpy.context.scene.objects:
        n = o.get("cj_naam")
        if o.get("cj_figuur") and o.get("cj_soort") == "SCHARNIER" and o.get("cj_deel") in ("A", "B") and "cj_scharnier_punt" in o and n not in AS_PLEK:
            drager = R._deel_b(R.KETEN.get(n)) if R.KETEN.get(n) else None
            if drager is None:
                continue
            inv = drager.matrix_world.inverted()
            as_ = Vector(o.get("cj_scharnier_as", (1, 0, 0)))
            AS_PLEK[n] = (drager.name, inv @ Vector(o["cj_scharnier_punt"]), (inv.to_3x3() @ as_).normalized())

    def afstand(p, a, b):
        ab = b - a
        t = 0.0 if ab.length < 1e-6 else max(0.0, min(1.0, (p - a).dot(ab) / ab.length_squared))
        return (p - (a + ab * t)).length
    teller = 0
    for o in delen:
        mats = list(o.data.materials)
        donker = {i for i, m in enumerate(mats) if m is None or m.name in ("toy_donker", "studio_gewricht")
                  or m.name.startswith("Click Joints")}
        if "hb_goud" not in [getattr(m, "name", "") for m in mats]:
            o.data.materials.append(goud)
        gi = [getattr(m, "name", "") for m in o.data.materials].index("hb_goud")
        mw = o.matrix_world
        for p in o.data.polygons:
            if p.material_index not in donker:
                continue
            w = mw @ p.center
            for zn, (a, b, r) in zones.items():
                if afstand(w, a, b) < r:
                    p.material_index = gi
                    teller += 1
                    GOUD_PLEK.setdefault(zn, []).append((o.name, p.index))
                    break
        o.data.update()
    meting["goud_vlakken"] = teller
    log("goud vlakken", teller, "zones", len(zones))


def nek_kleur(delen):
    """HB_NEK_TINT (#327, Daan #322 K1 en K2): de vlakken rond de nekkogel die na goud_gewrichten nog donker zijn
    (kom onder het hoofd, snederand van de hals) krijgen de kleur van hun eigen deel, maal deze factor (bijvoorbeeld
    0.78: iets donkerder). Alleen de kleur verandert, niet de vorm. Straal in mm met HB_NEK_STRAAL (standaard 24)."""
    f = float(os.environ["HB_NEK_TINT"])
    straal = float(os.environ.get("HB_NEK_STRAAL", "24"))
    c = None
    for o in bpy.context.scene.objects:
        if o.get("cj_naam") == "Neck" and o.get("cj_figuur") and "cj_centrum" in o:
            c = Vector(o["cj_centrum"])
            break
    if c is None:
        log("nek_kleur: geen nekkogel")
        return
    teller = 0
    for o in delen:
        mats = list(o.data.materials)
        donker = {i for i, m in enumerate(mats) if m is None or m.name in ("toy_donker", "studio_gewricht")
                  or m.name.startswith("Click Joints")}
        eigen = [i for i, m in enumerate(mats) if m is not None and m.name.startswith("hb_deel_")]
        if not donker or not eigen:
            continue
        mw = o.matrix_world
        raak = [p for p in o.data.polygons if p.material_index in donker and (mw @ p.center - c).length < straal]
        if not raak:
            continue
        from collections import Counter
        tel = Counter(p.material_index for p in o.data.polygons if p.material_index in eigen)
        basis = mats[tel.most_common(1)[0][0]] if tel else mats[eigen[0]]
        nm = basis.name + "_nek"
        g = bpy.data.materials.get(nm)
        if g is None:
            g = basis.copy()
            g.name = nm
            bs = next((n for n in g.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
            if bs is not None:
                k = bs.inputs["Base Color"].default_value
                bs.inputs["Base Color"].default_value = (k[0] * f, k[1] * f, k[2] * f, 1)
        if nm not in [getattr(m, "name", "") for m in o.data.materials]:
            o.data.materials.append(g)
        gi = [getattr(m, "name", "") for m in o.data.materials].index(nm)
        for p in raak:
            p.material_index = gi
            teller += 1
        o.data.update()
    meting["nek_kleur"] = {"factor": f, "straal_mm": straal, "vlakken": teller}
    log("nek_kleur", teller)


def printbed(m, stap=10.0, dik=0.35):
    """Vloer als een donkere printplaat: fijne rasterlijnen om de 10 mm (alleen kleur, geen vorm)."""
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(geo.outputs["Position"], sep.inputs[0])
    lijnen = []
    for as_ in ("X", "Y"):
        mod = nt.nodes.new("ShaderNodeMath")
        mod.operation = "PINGPONG"
        mod.inputs[1].default_value = stap / 2
        nt.links.new(sep.outputs[as_], mod.inputs[0])
        lt = nt.nodes.new("ShaderNodeMath")
        lt.operation = "LESS_THAN"
        lt.inputs[1].default_value = dik
        nt.links.new(mod.outputs[0], lt.inputs[0])
        lijnen.append(lt)
    mx = nt.nodes.new("ShaderNodeMath")
    mx.operation = "MAXIMUM"
    nt.links.new(lijnen[0].outputs[0], mx.inputs[0])
    nt.links.new(lijnen[1].outputs[0], mx.inputs[1])
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.inputs[6].default_value = srgb("1A1220")
    mix.inputs[7].default_value = srgb(os.environ.get("HB_RASTER", "3A2C46"))
    nt.links.new(mx.outputs[0], mix.inputs[0])
    nt.links.new(mix.outputs[2], b.inputs["Base Color"])
    return m


def scene(delen):
    sc = bpy.context.scene
    lo = Vector((min((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box),
                 min((o.matrix_world @ Vector(c)).y for o in delen for c in o.bound_box),
                 min((o.matrix_world @ Vector(c)).z for o in delen for c in o.bound_box)))
    hi = Vector((max((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box),
                 max((o.matrix_world @ Vector(c)).y for o in delen for c in o.bound_box),
                 max((o.matrix_world @ Vector(c)).z for o in delen for c in o.bound_box)))
    mid = (lo + hi) / 2
    h = hi.z - lo.z
    meting["kader"] = [list(lo), list(hi)]
    # vloer: donker glanzend, pruim
    bpy.ops.mesh.primitive_plane_add(size=6000, location=(0, 0, lo.z))
    vloer = bpy.context.active_object
    vloer.name = "hb_vloer"
    vloer.data.materials.append(printbed(mat("hb_vloer", "1A1220", rough=0.32, coat=0.4)))
    # achterwand: gebogen doek ver achter, donker, met een zachte gloed achter het figuur
    bpy.ops.mesh.primitive_plane_add(size=6000, location=(0, 1400, 1000), rotation=(math.radians(90), 0, 0))
    wand = bpy.context.active_object
    wand.name = "hb_wand"
    wand.data.materials.append(mat("hb_wand", "120B17", rough=0.9))
    # gloed: een grote zachte schijf achter het figuur (licht, niet in beeld als vorm door de grootte)
    w = bpy.context.scene.world or bpy.data.worlds.new("hb_wereld")
    sc.world = w
    w.use_nodes = True
    bg = next(n for n in w.node_tree.nodes if n.type == "BACKGROUND")
    bg.inputs[0].default_value = srgb("140C1A")
    bg.inputs[1].default_value = 1.0

    def lamp(naam, plek, maat, kracht, kleur, vorm="DISK"):
        ld = bpy.data.lights.new(naam, "AREA")
        ld.shape = vorm
        ld.size = maat
        ld.energy = kracht
        ld.color = tuple(srgb(kleur)[:3])
        lo_ = bpy.data.objects.new(naam, ld)
        sc.collection.objects.link(lo_)
        lo_.location = plek
        d = (mid - Vector(plek))
        lo_.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
        lo_.visible_glossy = False   # geen witte vlek van de lamp in de glanzende vloer
        return lo_
    f = h / 230.0
    k = float(os.environ.get("HB_LICHT", "1.0"))
    lamp("hb_key", mid + Vector((-420, -520, 380)) * f, 380 * f, 2.6e6 * f * f * k, "FFF3E2")
    lamp("hb_vul", mid + Vector((520, -380, 60)) * f, 500 * f, 0.7e6 * f * f * k, "C9D8FF")
    lamp("hb_rand_goud", mid + Vector((-360, 420, 160)) * f, 160 * f, 2.2e6 * f * f * k, "FFB547")
    lamp("hb_rand_blauw", mid + Vector((380, 380, 220)) * f, 160 * f, 2.0e6 * f * f * k, "5FA8FF")
    lamp("hb_top", mid + Vector((0, -60, 520)) * f, 300 * f, 0.9e6 * f * f * k, "FFFFFF")
    # zachte gloed op de wand achter het figuur
    ld = bpy.data.lights.new("hb_gloed", "POINT")
    ld.energy = 3.5e7 * f * f * k
    ld.color = tuple(srgb("7A3FA0")[:3])
    ld.shadow_soft_size = 200
    gl = bpy.data.objects.new("hb_gloed", ld)
    sc.collection.objects.link(gl)
    gl.visible_glossy = False
    # camera: iets van onder (heldhaftig), figuur rechts in beeld via lens-shift
    cd = bpy.data.cameras.new("hb_cam")
    cd.lens = 70
    cd.sensor_width = 36
    cd.clip_start, cd.clip_end = 10, 20000
    cam = bpy.data.objects.new("hb_cam", cd)
    sc.collection.objects.link(cam)
    sc.camera = cam
    draai = math.radians(float(os.environ.get("HB_DRAAI", "-24")))
    kantel = math.radians(float(os.environ.get("HB_KANTEL", "4")))
    # afstand zo dat het figuur ±86% van de beeldhoogte vult (16:9, verticale fov)
    rw, rh = int(os.environ.get("HB_W", "2400")), int(os.environ.get("HB_H", "1350"))   # vierkant: HB_W=HB_H (#94)
    sc.render.resolution_x, sc.render.resolution_y = rw, rh
    fov_v = 2 * math.atan((cd.sensor_width * min(1.0, rh / rw)) / 2 / cd.lens)
    vul = float(os.environ.get("HB_VUL", "0.80"))
    afstand = (h / vul) / 2 / math.tan(fov_v / 2) + (hi.y - lo.y) / 2
    doel = mid.copy()
    richting = Vector((math.sin(draai) * math.cos(kantel), -math.cos(draai) * math.cos(kantel), math.sin(kantel)))
    cam.location = doel + richting * afstand
    cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
    cd.shift_x = float(os.environ.get("HB_SHIFT", "-0.21"))
    cd.shift_y = float(os.environ.get("HB_SHIFT_Y", "0"))
    cd.dof.use_dof = False
    # gloed op de wand precies achter het figuur, gezien vanaf de camera
    bpy.context.view_layer.update()
    straal = (mid - cam.location).normalized()
    t = (1250 - cam.location.y) / straal.y
    raak = cam.location + straal * t
    gl.location = (raak.x, 1250, mid.z + 0.35 * h)
    # render
    sc.render.engine = "CYCLES"
    sc.cycles.samples = SAMPLES
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces = 8
    sc.render.resolution_percentage = SCHAAL
    sc.render.film_transparent = False
    sc.view_settings.view_transform = "AgX"
    try:
        sc.view_settings.look = "AgX - Medium High Contrast"
    except Exception:  # noqa: BLE001
        pass
    sc.render.image_settings.file_format = "PNG"
    sc.render.image_settings.color_mode = "RGB"
    return cam


def labels(cam):
    """Waar de gewrichten in beeld staan (0..1, y van boven): het midden van de gouden vlakken van elk gewricht,
    na pose en uit elkaar. Bereik uit de add-on (cj_bereik_graden op de scharnierdelen)."""
    sc = bpy.context.scene
    uit = {}
    for naam, lijst in GOUD_PLEK.items():
        from collections import Counter
        tel = Counter(on for on, _pi in lijst).most_common()
        meest = tel[0][0]   # het deel met het meeste goud (kogel)
        if naam in os.environ.get("HB_KOGEL_MINST", "").split(",") and len(tel) > 1:
            meest = tel[-1][0]   # #285: de kogel zelf heeft hier minder goud dan de kom
        lijst = [x for x in lijst if x[0] == meest]
        som, n = Vector(), 0
        for on, pi in lijst[::7] or lijst:
            o = sc.objects[on]
            som += o.matrix_world @ o.data.polygons[pi].center
            n += 1
        p = som / max(n, 1)
        if naam in AS_PLEK and naam in os.environ.get("HB_LABEL_AS", "Left elbow,Right elbow").split(","):
            an, lp, _la = AS_PLEK[naam]
            p = sc.objects[an].matrix_world @ lp
        v = world_to_camera_view(sc, cam, p)
        uit[naam] = {"x": round(v.x, 4), "y": round(1 - v.y, 4), "soort": None, "graden": None}
    for o in sc.objects:
        n = o.get("cj_naam")
        if n in uit and o.get("cj_figuur"):
            uit[n]["soort"] = o.get("cj_soort")
            if o.get("cj_bereik_graden"):
                uit[n]["graden"] = float(o.get("cj_bereik_graden"))
    meting["labels"] = uit


def knie_camera(cam, delen, naam):
    """#38 M2 (Daan #156): inzet die in één blik 'scharnier' zegt. Alleen de twee delen van dit scharnier in beeld,
    camera precies langs de as (pen en oog als rondje), vierkant. HB_KNIE_AFSTAND: mm van de as, HB_KNIE_KANT=-1
    kijkt van de andere kant, HB_KNIE_SCHUIF=x,y verschuift het midden in mm (beeldvlak)."""
    sc = bpy.context.scene
    a, b = paar(naam)
    an, lp, la = AS_PLEK[naam]
    mw = sc.objects[an].matrix_world
    p = mw @ lp
    straal = float(os.environ.get("HB_KNIE_STRAAL", "25"))
    zicht = []
    for o in delen:   # alleen de delen die het scharnier raken (bovenbeen en onderbeen)
        dichtbij = any(((o.matrix_world @ v.co) - p).length < straal for i, v in enumerate(o.data.vertices) if i % 5 == 0)
        if dichtbij:
            zicht.append(o.name)
        else:
            o.hide_render = True
    meting["knie_delen"] = zicht
    if os.environ.get("HB_KNIE_GEEST"):   # alleen voor het beeld: het bovenbeen half doorzichtig, zodat pen en oog
        drager = sc.objects[an]           # achter het ronde eind van het bovenbeen te zien zijn (vermeld in LEESMIJ)
        a_ = float(os.environ["HB_KNIE_GEEST"])
        for i, m in enumerate(list(drager.data.materials)):
            if m is None or m.name == "hb_goud":
                continue
            g = m.copy()
            g.name = m.name + "_geest"
            b = next((n for n in g.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
            if b is not None:
                b.inputs["Alpha"].default_value = a_
            drager.data.materials[i] = g
        meting["knie_geest"] = {"deel": drager.name, "alpha": a_}
    as_ = (mw.to_3x3() @ la).normalized() * float(os.environ.get("HB_KNIE_KANT", "1"))
    afst = float(os.environ.get("HB_KNIE_AFSTAND", "140"))
    if os.environ.get("HB_KNIE_SCHUIN"):
        # Daan #290 M1: camera schuin op de as (graden om de beeld-y en beeld-x), zodat je het scharnier en het vlak
        # van de stop ziet in plaats van alleen het ronde eind van het bovenbeen
        ga, gb = (math.radians(float(v)) for v in os.environ["HB_KNIE_SCHUIN"].split(","))
        r0 = (-as_).to_track_quat("-Z", "Y").to_matrix()
        as_ = Matrix.Rotation(gb, 3, r0 @ Vector((1, 0, 0))) @ (Matrix.Rotation(ga, 3, r0 @ Vector((0, 1, 0))) @ as_)
        meting["knie_schuin"] = os.environ["HB_KNIE_SCHUIN"]
    cam.location = p + as_ * afst
    cam.rotation_euler = (-as_).to_track_quat("-Z", "Y").to_euler()
    cd = cam.data
    cd.lens = float(os.environ.get("HB_KNIE_LENS", "70"))
    cd.shift_x = cd.shift_y = 0.0
    sx, sy = (float(v) for v in os.environ.get("HB_KNIE_SCHUIF", "0,0").split(","))
    bpy.context.view_layer.update()
    rot = cam.matrix_world.to_3x3()
    cam.location = cam.location + rot @ Vector((sx, sy, 0))
    m = int(os.environ.get("HB_KNIE_MAAT", "1000"))
    sc.render.resolution_x = sc.render.resolution_y = m
    # licht van de camerakant zodat het goud en de pen gaan glanzen
    ld = bpy.data.lights.new("hb_knie_licht", "AREA")
    ld.size = afst * 0.8
    ld.energy = float(os.environ.get("HB_KNIE_LICHT", "1.0")) * 2.0e5 * (afst / 140) ** 2
    lo_ = bpy.data.objects.new("hb_knie_licht", ld)
    sc.collection.objects.link(lo_)
    lo_.location = p + as_ * afst + rot @ Vector((-afst * 0.6, afst * 0.5, 0))
    lo_.rotation_euler = (p - lo_.location).to_track_quat("-Z", "Y").to_euler()
    lo_.visible_glossy = False
    meting["knie_cam"] = {"scharnier": naam, "punt": list(p), "as": list(as_), "afstand": afst,
                          "pose_graden": float(b.get("cj_pose_graden", 0) or 0) if b else None,
                          "bereik": float(a.get("cj_bereik_graden", 0) or 0) if a else None}
    log("knie-camera", meting["knie_cam"])
    if os.environ.get("HB_KNIE_BOOG") and BOOG_RUST.get(naam):
        # #38 ronde 4 (Daan #170 M2 keuze a): de gradenboog van de add-on zelf (Show bend range, scharnier_boog.vorm),
        # in pixels van deze camera, zodat inzet.py hem tekent zoals de koper hem in Blender ziet.
        v = BOOG_RUST.get(naam)

        def px(w):
            q = world_to_camera_view(sc, cam, Vector(w))
            return [round(q.x * m, 1), round((1 - q.y) * m, 1)]
        meting["knie_boog"] = {"getal": v["getal"], "centrum": px(v["centrum"]), "boog": [px(w) for w in v["boog"]],
                               "as_eind": px(v["as_eind"]), "grens_eind": px(v["grens_eind"]), "label": px(v["label"]),
                               "label_0": px(v["label_0"]),
                               "streepjes": [[g, px(p1), px(p2)] for g, p1, p2 in v["streepjes"]], "maat": m}
        log("knie-boog", v["getal"], meting["knie_boog"]["centrum"], meting["knie_boog"]["grens_eind"])
    if os.environ.get("HB_KNIE_DONKER"):   # Daan #290 M1: de andere delen (scheen) donkerder, het goud en het
        f = float(os.environ["HB_KNIE_DONKER"])   # bovenbeen blijven over als één vorm
        for nm in zicht:
            o = sc.objects[nm]
            if nm == an:
                continue
            for i, mt in enumerate(list(o.data.materials)):
                if mt is None or mt.name == "hb_goud" or not mt.use_nodes:
                    continue
                g = mt.copy()
                g.name = mt.name + "_donker"
                bs = next((n for n in g.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
                if bs is not None:
                    c = bs.inputs["Base Color"].default_value
                    bs.inputs["Base Color"].default_value = (c[0] * f, c[1] * f, c[2] * f, 1)
                o.data.materials[i] = g
        meting["knie_donker"] = f
    if os.environ.get("HB_KNIE_TINT"):   # bovenbeen een tint lichter dan onderbeen (Daan #170 M2 b), twee delen in één blik
        f = float(os.environ["HB_KNIE_TINT"])
        drager = sc.objects[an]
        for i, mt in enumerate(list(drager.data.materials)):
            if mt is None or mt.name == "hb_goud" or not mt.use_nodes:
                continue
            g = mt.copy()
            g.name = mt.name + "_licht"
            bs = next((n for n in g.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
            if bs is not None:
                c = bs.inputs["Base Color"].default_value
                bs.inputs["Base Color"].default_value = (c[0] + (1 - c[0]) * f, c[1] + (1 - c[1]) * f, c[2] + (1 - c[2]) * f, 1)
            drager.data.materials[i] = g


def deel_kleur(delen):
    """HB_DEELKLEUR (#285, held): elk deel één eigen kleur filament, zoals op het hoofdbeeld van Cleave. Alleen het
    materiaal held_* van het figuur wordt vervangen; de vlakken van de gewrichten houden hun eigen materiaal."""
    kl = json.loads(os.environ["HB_DEELKLEUR"])   # {"romp": hex, "onderarm": hex, "dij": hex, "scheen": hex}
    zs = []
    for o in delen:
        bb = [o.matrix_world @ Vector(c) for c in o.bound_box]
        zs.append((o, sum(v.z for v in bb) / 8, max(v.z for v in bb) - min(v.z for v in bb)))
    hoog = max(z for _o, z, _h in zs) if zs else 1
    romp = max(zs, key=lambda t: t[2])[0] if zs else None
    for o, zc, _h in zs:
        if o is romp:
            soort = "romp"
        elif "kop_los" in kl and zc > 0.80 * 220:
            soort = "kop_los"   # #320: het hoofd is los (nekkogel van Figure from rig) en krijgt een eigen kleur
        elif zc > 0.42 * 220:
            soort = "onderarm"
        elif zc > 0.25 * 220:
            soort = "dij"
        else:
            soort = "scheen"
        m = mat("hb_deel_" + soort, kl.get(soort, "DDDDDD"), rough=0.5)
        for i, mm in enumerate(list(o.data.materials)):
            if mm is not None and mm.name.startswith("held_"):
                o.data.materials[i] = m
        if o is romp and ("kop" in kl or "bovenarm" in kl):
            # op de romp: kop boven de hals en de bovenarmen (buiten de schouder) een eigen kleur, in rusthouding
            mats = list(o.data.materials)
            ri = mats.index(m)
            extra = {}
            for soort2 in ("kop", "bovenarm"):
                if soort2 in kl:
                    o.data.materials.append(mat("hb_deel_" + soort2, kl[soort2], rough=0.5))
                    extra[soort2] = len(o.data.materials) - 1
            mw = o.matrix_world
            for f in o.data.polygons:
                if f.material_index != ri:
                    continue
                c = mw @ f.center
                if "kop" in extra and c.z > 0.845 * 220:
                    f.material_index = extra["kop"]
                elif "bovenarm" in extra and abs(c.x) > 0.118 * 220 and 0.40 * 220 < c.z < 0.86 * 220:
                    f.material_index = extra["bovenarm"]
    meting["deelkleur"] = kl


def main():
    naam, delen = figuur()
    if os.environ.get("HB_DEELKLEUR"):
        deel_kleur(delen)
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    goud_gewrichten(delen)
    if os.environ.get("HB_NEK_TINT"):
        nek_kleur(delen)
    # HB_POSE: eigen pose als json (#38, organisch figuur), zelfde vorm als R.HELD; anders de heldenpose van de robot
    pose = json.loads(os.environ["HB_POSE"]) if os.environ.get("HB_POSE") else R.HELD
    if os.environ.get("HB_KNIE_BOOG") and os.environ.get("HB_KNIE_CAM"):
        # boog in rusthouding (been recht, zoals de add-on hem rekent); het bovenbeen beweegt daarna niet (heup niet
        # geposeerd, HB_UIT=0), dus de punten blijven kloppen
        sb = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_boog")
        ka, kb = paar(os.environ["HB_KNIE_CAM"])
        BOOG_RUST[os.environ["HB_KNIE_CAM"]] = sb.vorm(ka, kb, 0.0)
    meting["pose"] = R.poseer(delen, pose, uit=UIT_MM, scharnier=lambda n, g: buig(n, g))
    bpy.context.view_layer.update()
    for o in bpy.context.scene.objects:   # alleen de delen van de add-on in beeld (het origineel en hulpvormen weg)
        if o.type in ("MESH", "CURVE", "FONT", "EMPTY") and o not in delen:
            o.hide_render = True
            o.hide_set(True)
    cam = scene(delen)
    bpy.context.view_layer.update()
    labels(cam)
    if os.environ.get("HB_KNIE_CAM"):
        knie_camera(cam, delen, os.environ["HB_KNIE_CAM"])
    if os.environ.get("HB_RAND"):   # #38: alleen een uitsnede (x0,x1,y0,y1 als 0..1, y van onder) voor een inzet
        x0, x1, y0, y1 = (float(v) for v in os.environ["HB_RAND"].split(","))
        r = bpy.context.scene.render
        r.use_border, r.use_crop_to_border = True, True
        r.border_min_x, r.border_max_x, r.border_min_y, r.border_max_y = x0, x1, y0, y1
    pad = os.path.join(UIT, os.environ.get("HB_NAAM", "hoofdbeeld") + "-render.png")
    bpy.context.scene.render.filepath = pad
    t0 = time.time()
    bpy.ops.render.render(write_still=True)
    meting["render_s"] = round(time.time() - t0, 1)
    json.dump(meting, open(os.path.join(UIT, os.environ.get("HB_NAAM", "hoofdbeeld") + ".json"), "w"), indent=1, ensure_ascii=False, default=str)
    if os.environ.get("HB_BEWAAR"):
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(UIT, "hoofdbeeld.blend"))
    log("klaar", pad, meting["render_s"], "s")


main()
