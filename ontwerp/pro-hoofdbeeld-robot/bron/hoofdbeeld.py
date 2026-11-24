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
from mathutils import Vector

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
    arm, ob, _p = FL.laad_figuur("robot", 220.0)
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
    sc.render.resolution_x, sc.render.resolution_y = 2400, 1350
    fov_v = 2 * math.atan((cd.sensor_width * 1350 / 2400) / 2 / cd.lens)
    vul = float(os.environ.get("HB_VUL", "0.80"))
    afstand = (h / vul) / 2 / math.tan(fov_v / 2) + (hi.y - lo.y) / 2
    doel = mid.copy()
    richting = Vector((math.sin(draai) * math.cos(kantel), -math.cos(draai) * math.cos(kantel), math.sin(kantel)))
    cam.location = doel + richting * afstand
    cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
    cd.shift_x = float(os.environ.get("HB_SHIFT", "-0.21"))
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
        meest = Counter(on for on, _pi in lijst).most_common(1)[0][0]   # het deel met het meeste goud (kogel)
        lijst = [x for x in lijst if x[0] == meest]
        som, n = Vector(), 0
        for on, pi in lijst[::7] or lijst:
            o = sc.objects[on]
            som += o.matrix_world @ o.data.polygons[pi].center
            n += 1
        v = world_to_camera_view(sc, cam, som / max(n, 1))
        uit[naam] = {"x": round(v.x, 4), "y": round(1 - v.y, 4), "soort": None, "graden": None}
    for o in sc.objects:
        n = o.get("cj_naam")
        if n in uit and o.get("cj_figuur"):
            uit[n]["soort"] = o.get("cj_soort")
            if o.get("cj_bereik_graden"):
                uit[n]["graden"] = float(o.get("cj_bereik_graden"))
    meting["labels"] = uit


def main():
    naam, delen = figuur()
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    goud_gewrichten(delen)
    meting["pose"] = R.poseer(delen, R.HELD, uit=UIT_MM, scharnier=lambda n, g: buig(n, g))
    bpy.context.view_layer.update()
    for o in bpy.context.scene.objects:   # alleen de delen van de add-on in beeld (het origineel en hulpvormen weg)
        if o.type in ("MESH", "CURVE", "FONT", "EMPTY") and o not in delen:
            o.hide_render = True
            o.hide_set(True)
    cam = scene(delen)
    bpy.context.view_layer.update()
    labels(cam)
    pad = os.path.join(UIT, "hoofdbeeld-render.png")
    bpy.context.scene.render.filepath = pad
    t0 = time.time()
    bpy.ops.render.render(write_still=True)
    meting["render_s"] = round(time.time() - t0, 1)
    json.dump(meting, open(os.path.join(UIT, "hoofdbeeld.json"), "w"), indent=1, ensure_ascii=False, default=str)
    if os.environ.get("HB_BEWAAR"):
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(UIT, "hoofdbeeld.blend"))
    log("klaar", pad, meting["render_s"], "s")


main()
