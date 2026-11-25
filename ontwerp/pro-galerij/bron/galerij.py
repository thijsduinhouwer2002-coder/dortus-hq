"""Galerijbeelden Click Joints Pro (Beeldmaker, 25 nov 2026, issue #49).

Zelfde studio, robot en goud als het hoofdbeeld (ontwerp/pro-hoofdbeeld-robot/bron/hoofdbeeld.py; die functies worden
hier geladen, niet nagetekend). Alles wat je ziet maakte de echte add-on (zip van main, Pro 1.2.8): de knop
Figure from rig voor de robot, de knop Fit test strip voor de staafjes. Alleen kleur en camera zijn van ons.

    GB_MODUS=knie|klik|strip blender -b --factory-startup --python galerij.py -- <pro-zip> <uitmap> [samples] [schaal%]

knie:  zijaanzicht van het linkerbeen, knie gebogen tot de eindstop die de add-on meldt; json met de punten voor de
       boog in graden (scharniermidden, richting dij, scheen bij 0 en bij de stop) in beeldcoördinaten.
klik:  links het figuur zoals je het aanlevert (één stuk, met de botten van de rig erin), rechts de delen uit de knop.
strip: de vijf staafjes van Fit test: ball, bovenste helft iets opgetild zodat je kogel en kom ziet.
"""
import json
import math
import os
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
HB = os.path.abspath(os.path.join(HIER, "..", "..", "pro-hoofdbeeld-robot", "bron", "hoofdbeeld.py"))
MODUS = os.environ.get("GB_MODUS", "knie")
bron = open(HB, encoding="utf-8").read()
bron = bron[:bron.rindex("\nmain()")]
__file__ = HB  # noqa: A001  (hoofdbeeld.py zoekt de studio naast zichzelf)
exec(compile(bron, HB, "exec"))  # noqa: S102  zet o.a. figuur, goud_gewrichten, scene, buig, meting, ZIP, UIT
meting["modus"] = MODUS


def naar_beeld(cam, p):
    v = world_to_camera_view(bpy.context.scene, cam, Vector(p))
    return [round(v.x, 4), round(1 - v.y, 4)]


def verberg_rest(houden):
    for o in bpy.context.scene.objects:
        if o.type in ("MESH", "CURVE", "FONT", "EMPTY") and o not in houden:
            o.hide_render = True
            o.hide_set(True)


def camera_op(cam, doel, richting, afstand, lens):
    cam.data.lens = lens
    cam.data.shift_x = float(os.environ.get("GB_SHIFT", "0"))
    cam.data.shift_y = float(os.environ.get("GB_SHIFT_Y", "0"))
    cam.location = doel + richting.normalized() * afstand
    cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
    bpy.context.view_layer.update()


def scharnierdeel(naam, deel):
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_deel") == deel and o.type == "MESH":
            return o
    return None


def render(naam):
    pad = os.path.join(UIT, f"render-{naam}.png")
    bpy.context.scene.render.filepath = pad
    bpy.ops.render.render(write_still=True)
    json.dump(meting, open(os.path.join(UIT, f"{naam}.json"), "w"), indent=1, ensure_ascii=False, default=str)
    log("klaar", pad)


# ---------------------------------------------------------------- knie
def knie():
    naam, delen = figuur()
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    goud_gewrichten(delen)
    a, b = paar("Left knee")
    stop = float(a.get("cj_bereik_graden", 120)) if a is not None else 120.0
    meting["stop_graden"] = stop
    # Rustpunten (vóór pose): scharniermidden, heup en enkel op de as van het been.
    rec = {r["naam"]: r for r in meting["records"]}
    k0 = Vector(rec["Left knee"]["punt"])
    pose = {"Left hip": [((1, 0, 0), -float(os.environ.get("GB_HEUP", "22")))], "Left knee": stop,
            "Right knee": 8.0, "Left elbow": 70.0, "Right elbow": 70.0,
            "Left shoulder": [((1, 0, 0), 18.0)], "Right shoulder": [((1, 0, 0), -18.0)]}
    vb = b.matrix_world.copy()
    va = a.matrix_world.copy() if a is not None else None
    meting["pose"] = R.poseer(delen, pose, uit=float(os.environ.get("GB_UIT", "0")), scharnier=lambda n, g: buig(n, g))
    bpy.context.view_layer.update()
    verberg_rest(delen)
    # wereldmatrices: deel A (dij) en deel B (scheen) na pose; zo rekenen we rustpunten door naar beeld
    ma = a.matrix_world @ va.inverted()
    mb = b.matrix_world @ vb.inverted()
    heup = Vector(rec["Left hip"]["punt"]) if "Left hip" in rec else k0 + Vector((0, 0, 40))
    knie_w = ma @ k0
    dij_w = ma @ (k0 + (heup - k0).normalized() * 40)
    scheen0_w = ma @ (k0 + Vector((0, 0, -40)))       # scheen recht (0 graden), mee met de dij
    scheen_w = mb @ (k0 + Vector((0, 0, -40)))        # scheen bij de stop
    cam = scene(delen)
    # zijaanzicht langs de scharnieras (wereld-x na de heupdraai is nog x)
    doel = knie_w + Vector((0, 0, float(os.environ.get("GB_HOOG", "-6"))))
    camera_op(cam, doel, Vector((float(os.environ.get("GB_KANT", "1")), float(os.environ.get("GB_SCHUIN", "-0.18")), 0.08)),
              float(os.environ.get("GB_AFSTAND", "420")), float(os.environ.get("GB_LENS", "85")))
    meting["boog"] = {"knie": naar_beeld(cam, knie_w), "dij": naar_beeld(cam, dij_w),
                      "scheen0": naar_beeld(cam, scheen0_w), "scheen": naar_beeld(cam, scheen_w)}
    render("knie")


# ---------------------------------------------------------------- klik
def botten(arm, dx):
    """Botten van de rig als Blenders octaëders (mesh, zodat Cycles ze rendert). dx: schuif naar links."""
    me_lijst = []
    for bot in arm.data.bones:
        if not bot.use_deform and bot.parent is not None and "root" in bot.name.lower():
            continue
        h = arm.matrix_world @ bot.head_local
        t = arm.matrix_world @ bot.tail_local
        L = (t - h).length
        if L < 1e-3:
            continue
        as_ = (t - h).normalized()
        hulp = Vector((0, 0, 1)) if abs(as_.z) < 0.9 else Vector((1, 0, 0))
        u = as_.cross(hulp).normalized()
        v = as_.cross(u).normalized()
        w = L * 0.1
        m = h + as_ * L * 0.18
        pts = [h, m + u * w, m + v * w, m - u * w, m - v * w, t]
        vl = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (5, 2, 1), (5, 3, 2), (5, 4, 3), (5, 1, 4)]
        me = bpy.data.meshes.new("gb_bot")
        me.from_pydata([p + Vector((dx, 0, 0)) for p in pts], [], vl)
        me.update()
        me_lijst.append(me)
    obs = []
    mbot = mat("gb_bot", os.environ.get("GB_BOTKLEUR", "4FB3FF"), rough=0.35, emis=1.2)
    for me in me_lijst:
        o = bpy.data.objects.new("gb_bot", me)
        bpy.context.scene.collection.objects.link(o)
        o.data.materials.append(mbot)
        obs.append(o)
    return obs


def glas_spook(o):
    m = bpy.data.materials.new("gb_spook")
    m.use_nodes = True
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = srgb("DCE6F5")
    b.inputs["Roughness"].default_value = 0.35
    b.inputs["Alpha"].default_value = float(os.environ.get("GB_ALFA", "0.22"))
    o.data.materials.clear()
    o.data.materials.append(m)


def klik():
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    arm, ob, _p = FL.laad_figuur("robot", 220.0)
    # kopie van het figuur zoals de koper het aanlevert, vóór de knop
    spook = ob.copy()
    spook.data = ob.data.copy()
    spook.modifiers.clear()
    bpy.context.scene.collection.objects.link(spook)
    for c in list(spook.users_collection):
        if c != bpy.context.scene.collection:
            c.objects.unlink(spook)
    bpy.context.view_layer.update()
    spook.matrix_world = ob.matrix_world.copy()
    # nu de knop, op het origineel (zelfde instellingen als figuur())
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    naam = ob.name
    FL.actief(ob)
    r = bpy.ops.click_joints.figuur_uit_rig()
    log("Figure from rig", r)
    import importlib
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    meting["gewrichten"] = [fig.regel(x) for x in lijst]
    meting["delen"] = 0
    delen = delen_van(naam)
    meting["delen"] = len(delen)
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    goud_gewrichten(delen)
    meting["pose"] = R.poseer(delen, {}, uit=float(os.environ.get("GB_UIT", "16")), scharnier=lambda n, g: buig(n, g))
    bpy.context.view_layer.update()
    breed = max((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box) - \
        min((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box)
    dx = -float(os.environ.get("GB_AFSTAND_X", "1.55")) * breed
    # spook op dezelfde vloer als de delen, naar links
    laag_s = min((spook.matrix_world @ v.co).z for v in spook.data.vertices)
    spook.matrix_world = Matrix.Translation((dx, 0, -laag_s)) @ spook.matrix_world
    bpy.context.view_layer.update()
    glas_spook(spook)
    arm.hide_set(False)
    arm.matrix_world = Matrix.Translation((0, 0, -laag_s)) @ arm.matrix_world
    bpy.context.view_layer.update()
    bot_obs = botten(arm, dx)
    arm.hide_set(True)
    arm.hide_render = True
    verberg_rest(delen + [spook] + bot_obs)
    cam = scene(delen + [spook])
    rec_r = [(o.matrix_world @ Vector(c)) for o in delen for c in o.bound_box]
    rec_s = [(spook.matrix_world @ Vector(c)) for c in spook.bound_box]
    meting["kaders"] = {"rig": [naar_beeld(cam, min(rec_s, key=lambda p: p.x)), naar_beeld(cam, max(rec_s, key=lambda p: p.x))],
                        "delen": [naar_beeld(cam, min(rec_r, key=lambda p: p.x)), naar_beeld(cam, max(rec_r, key=lambda p: p.x))]}
    meting["botten"] = len(bot_obs)
    render("klik")


# ---------------------------------------------------------------- strip
def strip():
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    for o in list(bpy.context.scene.objects):
        bpy.data.objects.remove(o)
    sc = bpy.context.scene
    sc.unit_settings.system, sc.unit_settings.scale_length, sc.unit_settings.length_unit = "METRIC", 0.001, "MILLIMETERS"
    soort = os.environ.get("GB_SOORT", "KOGEL")
    r = bpy.ops.click_joints.testkaart(soort=soort)
    log("Fit test strip", r)
    voor = {o.name for o in sc.objects if o.type == "MESH" and o.get("cj_deel")}
    tweede = os.environ.get("GB_SOORT2")
    if tweede:   # tweede set (Fit test: hinge); de add-on zet hem zelf achter de eerste
        log("Fit test strip 2", bpy.ops.click_joints.testkaart(soort=tweede))
    delen = [o for o in sc.objects if o.type == "MESH" and o.get("cj_deel")]
    meting["delen"] = sorted(o.name for o in delen)
    meting["getallen"] = sorted({o.get("cj_kaart_getal") for o in delen if o.get("cj_kaart_getal")})
    wit = mat("gb_wit", "F4EFE6", rough=0.42, coat=0.25)
    goud = mat("hb_goud", os.environ.get("HB_GOUD", "FFB938"), rough=0.28, metal=0.55, coat=0.3)
    til = float(os.environ.get("GB_TIL", "14"))
    labels = {}
    for o in delen:
        o.data.materials.clear()
        o.data.materials.append(wit)
        o.data.materials.append(goud)
        # vlakken dicht bij het snijvlak (midden van de staaf, 30 mm) goud: kogel, nek en kom
        mw = o.matrix_world
        zone = float(os.environ.get("GB_GOUDZONE", "11"))
        boven = bool(o.get("cj_kaart_getal"))   # bovenste helft: de kom; onderste helft: kogel en nek
        for p in o.data.polygons:
            zs = [(mw @ o.data.vertices[i].co).z for i in p.vertices]
            if (boven and all(z < 30.0 + zone for z in zs)) or (not boven and all(z > 29.5 for z in zs)):
                p.material_index = 1
        o.data.update()
    kantel = math.radians(float(os.environ.get("GB_KANTEL_TOP", "0")))
    for o in delen:
        if o.get("cj_kaart_getal"):
            pts = [o.matrix_world @ Vector(h) for h in o.bound_box]
            p0 = sum(pts, Vector()) / 8
            p0.z = min(p.z for p in pts)
            o.matrix_world = (Matrix.Translation(p0 + Vector((0, 0, til))) @ Matrix.Rotation(kantel, 4, "X")
                              @ Matrix.Translation(-p0) @ o.matrix_world)
    bpy.context.view_layer.update()
    cam = scene(delen)
    lo = Vector((min((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box),
                 min((o.matrix_world @ Vector(c)).y for o in delen for c in o.bound_box), 0))
    hi = Vector((max((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box),
                 max((o.matrix_world @ Vector(c)).y for o in delen for c in o.bound_box),
                 max((o.matrix_world @ Vector(c)).z for o in delen for c in o.bound_box)))
    mid = (lo + hi) / 2
    doel = Vector((mid.x, mid.y, hi.z * 0.5))
    camera_op(cam, doel, Vector((float(os.environ.get("GB_ZIJ", "-0.35")), -1.0, float(os.environ.get("GB_OP", "0.55")))),
              float(os.environ.get("GB_AFSTAND", "330")), float(os.environ.get("GB_LENS", "60")))
    for o in delen:
        if o.get("cj_kaart_getal") and o.name in voor:
            top = max((o.matrix_world @ Vector(c)).z for c in o.bound_box)
            c = o.matrix_world @ (sum((Vector(h) for h in o.bound_box), Vector()) / 8)
            labels[o["cj_kaart_getal"]] = {"top": naar_beeld(cam, (c.x, c.y, top)),
                                           "voet": naar_beeld(cam, (c.x, c.y - 10, 0))}
    meting["labels"] = labels
    render("strip")


{"knie": knie, "klik": klik, "strip": strip}[MODUS]()
