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
    keuze = os.environ.get("HB_FIGUUR", "robot")   # "mens": MakeHuman base (CC0), videobeeld #94 stap 3
    arm, ob, _p = FL.laad_figuur(keuze, 220.0)
    if keuze == "mens":
        meting["figuur"] = "MakeHuman base mesh (CC0 1.0, commercie/filmpjes/studio/modellen/makehuman-base-LICENTIE.md), aangekleed door figuur_laden.py"
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
    tweede_set = [o for o in delen if o.name not in voor]
    # strip v3 (#205): tweede set naast de eerste (GB_NAAST=<gat in mm>) of verder naar achter (GB_RIJ2_Y=<mm>)
    if tweede_set and (os.environ.get("GB_NAAST") or os.environ.get("GB_RIJ2_Y")):
        eerste = [o for o in delen if o.name in voor]
        xs1 = [(o.matrix_world @ Vector(c)).x for o in eerste for c in o.bound_box]
        xs2 = [(o.matrix_world @ Vector(c)).x for o in tweede_set for c in o.bound_box]
        ys1 = [(o.matrix_world @ Vector(c)).y for o in eerste for c in o.bound_box]
        ys2 = [(o.matrix_world @ Vector(c)).y for o in tweede_set for c in o.bound_box]
        if os.environ.get("GB_NAAST"):
            d = Vector((max(xs1) + float(os.environ["GB_NAAST"]) - min(xs2),
                        (min(ys1) + max(ys1)) / 2 - (min(ys2) + max(ys2)) / 2, 0))
        else:
            d = Vector(((min(xs1) + max(xs1)) / 2 - (min(xs2) + max(xs2)) / 2,
                        float(os.environ["GB_RIJ2_Y"]) - (min(ys2) + max(ys2)) / 2, 0))
        for o in tweede_set:
            o.matrix_world = Matrix.Translation(d) @ o.matrix_world
        bpy.context.view_layer.update()
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
        # strakke rand (Daan #215 kan-punt, issue strip v3 rand): bij de kogelstaaf blijft de buitenwand wit, alleen
        # het bovenvlak, de nek en de kogel worden goud. Zo loopt de grens over de rand van de staaf, niet rafelig
        # over losse driehoekjes in de wand.
        strak = os.environ.get("GB_STRAKKE_RAND") == "1" and not boven and o.name in voor
        if strak:
            hoeken = [mw @ Vector(c) for c in o.bound_box]
            ax = sum((h.x for h in hoeken)) / 8
            ay = sum((h.y for h in hoeken)) / 8
            straal = max(math.hypot((mw @ v.co).x - ax, (mw @ v.co).y - ay) for v in o.data.vertices)
        for p in o.data.polygons:
            zs = [(mw @ o.data.vertices[i].co).z for i in p.vertices]
            if strak:
                c = mw @ p.center
                nz = (mw.to_3x3() @ p.normal).normalized().z   # bovenvlak wijst omhoog, de wand opzij
                if c.z > 29.5 and (nz > 0.7 or math.hypot(c.x - ax, c.y - ay) < straal * 0.93):
                    p.material_index = 1
            elif (boven and all(z < 30.0 + zone for z in zs)) or (not boven and all(z > 29.5 for z in zs)):
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
    if tweede:
        labels2, sets = {}, {}
        for o in delen:
            if o.get("cj_kaart_getal") and o.name not in voor:
                top = max((o.matrix_world @ Vector(c)).z for c in o.bound_box)
                c = o.matrix_world @ (sum((Vector(h) for h in o.bound_box), Vector()) / 8)
                labels2[o["cj_kaart_getal"]] = {"top": naar_beeld(cam, (c.x, c.y, top)),
                                                "voet": naar_beeld(cam, (c.x, c.y - 10, 0))}
        for naam, groep in (("eerste", [o for o in delen if o.name in voor]),
                            ("tweede", [o for o in delen if o.name not in voor])):
            ps = [o.matrix_world @ Vector(c) for o in groep for c in o.bound_box]
            sets[naam] = {"soort": soort if naam == "eerste" else tweede,
                          "links_onder": naar_beeld(cam, (min(p.x for p in ps), min(p.y for p in ps), 0)),
                          "rechts_onder": naar_beeld(cam, (max(p.x for p in ps), min(p.y for p in ps), 0)),
                          "boven": naar_beeld(cam, ((min(p.x for p in ps) + max(p.x for p in ps)) / 2,
                                                    (min(p.y for p in ps) + max(p.y for p in ps)) / 2,
                                                    max(p.z for p in ps)))}
        meting["labels2"], meting["sets"] = labels2, sets
    render(os.environ.get("GB_NAAM", "strip"))


# ---------------------------------------------------------------- bereik (ronde 3 van beeld 1, na de blinde test)
def gewricht_punt(naam):
    """Midden van de gouden vlakken van een gewricht, na pose (zoals labels() in hoofdbeeld.py)."""
    from collections import Counter
    lijst = GOUD_PLEK.get(naam) or []
    if not lijst:
        return None
    meest = Counter(on for on, _pi in lijst).most_common(1)[0][0]
    lijst = [x for x in lijst if x[0] == meest]
    som, n = Vector(), 0
    for on, pi in lijst[::5] or lijst:
        o = bpy.context.scene.objects[on]
        som += o.matrix_world @ o.data.polygons[pi].center
        n += 1
    return som / max(n, 1)


def bereik():
    """Heel figuur in een pose die elk bereik laat zien (knie tot de stop, elleboog ver gebogen, schouder opzij, nek
    gedraaid), met de punten van vier gewrichten in beeld; daarna een tweede render van dichtbij: het scharnier van de
    linkerknie bij de stop, zijaanzicht langs de as."""
    naam, delen = figuur()
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    goud_gewrichten(delen)
    a, _b = paar("Left knee")
    stop = float(a.get("cj_bereik_graden", 120)) if a is not None else 120.0
    meting["stop_graden"] = stop
    ae, _be = paar("Left elbow")
    meting["elleboog_graden"] = float(ae.get("cj_bereik_graden", 0)) if ae is not None else None
    pose = {"Left hip": [((1, 0, 0), -float(os.environ.get("GB_HEUP", "22")))], "Left knee": stop,
            "Right knee": 6.0, "Right hip": [((0, 1, 0), 6.0)],
            "Left shoulder": [((1, 0, 0), -float(os.environ.get("GB_SCH_L", "20")))],
            "Left elbow": float(os.environ.get("GB_ELL_L", "140")),
            "Right shoulder": [((0, 1, 0), -float(os.environ.get("GB_SCH_R", "28")))],
            "Right elbow": float(os.environ.get("GB_ELL_R", "40")),
            "Neck": [((0, 0, 1), float(os.environ.get("GB_NEK", "20")))]}
    meting["pose"] = R.poseer(delen, pose, uit=float(os.environ.get("GB_UIT", "6")), scharnier=lambda n, g: buig(n, g))
    bpy.context.view_layer.update()
    verberg_rest(delen)
    cam = scene(delen)
    bpy.context.view_layer.update()
    rec = {r["naam"]: r for r in meting["records"]}
    punten = {}
    for n in ("Left knee", "Left elbow", "Right shoulder", "Neck", "Right knee", "Right elbow", "Left shoulder"):
        w = gewricht_punt(n)
        if w is not None:
            punten[n] = {"beeld": naar_beeld(cam, w), "soort": rec.get(n, {}).get("soort"),
                         "graden": rec.get(n, {}).get("graden"), "wereld": list(w)}
    meting["punten"] = punten
    if not os.environ.get("GB_ALLEEN_ZOOM"):
        render("bereik")
    if os.environ.get("GB_GEEN_ZOOM"):
        return
    # dichtbij: scharnier linkerknie, langs de as
    k = Vector(punten["Left knee"]["wereld"])
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y = 1200, 1200
    # alleen het linkerbeen in beeld (dij en scheen van deze knie), zodat je één scharnier ziet
    straal = float(os.environ.get("GB_ZSTRAAL", "30"))
    for o in delen:
        bb = [o.matrix_world @ Vector(c) for c in o.bound_box]
        lo_ = Vector((min(p.x for p in bb), min(p.y for p in bb), min(p.z for p in bb)))
        hi_ = Vector((max(p.x for p in bb), max(p.y for p in bb), max(p.z for p in bb)))
        dichtst = Vector((min(max(k.x, lo_.x), hi_.x), min(max(k.y, lo_.y), hi_.y), min(max(k.z, lo_.z), hi_.z)))
        midden_x = (lo_.x + hi_.x) / 2
        weg = (dichtst - k).length > straal or midden_x < 2.0
        o.hide_render = weg
    cam.data.shift_x = cam.data.shift_y = 0
    cam.data.lens = float(os.environ.get("GB_ZLENS", "100"))
    r = Vector((float(os.environ.get("GB_ZKANT", "1")), float(os.environ.get("GB_ZSCHUIN", "-0.35")), 0.12))
    cam.location = k + r.normalized() * float(os.environ.get("GB_ZAFSTAND", "150"))
    cam.rotation_euler = (k - cam.location).to_track_quat("-Z", "Y").to_euler()
    cam.data.dof.use_dof = True
    cam.data.dof.focus_distance = (k - cam.location).length
    cam.data.dof.aperture_fstop = float(os.environ.get("GB_FSTOP", "5.6"))
    bpy.context.view_layer.update()
    pad = os.path.join(UIT, "render-bereik-knie.png")
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)
    log("klaar", pad)


# ---------------------------------------------------------------- delen (beeld 4, issue #101)
def delen_plat():
    """Alle delen uit Figure from rig naast elkaar op de printplaat (zoals je ze in je slicer zou leggen), na de echte
    knop Export: het aantal bestanden en de namen komen uit wat de add-on schreef. Leggen en camera zijn van ons; de
    add-on legt de delen niet zelf neer."""
    import tempfile
    naam, delen = figuur()
    R.kleur_herstel(delen)
    S.plastic(delen, gewricht="contrast", gewricht_kleur=R.GEWRICHT)
    goud_gewrichten(delen)
    inst = bpy.context.scene.click_joints
    map_ = tempfile.mkdtemp(prefix="cj_export_")
    inst.exportmap = map_
    uitkomst = {}
    for formaat in ("STL", "3MF"):
        inst.formaat = formaat
        r = bpy.ops.click_joints.exporteer()
        uitkomst[formaat] = sorted(f for f in os.listdir(map_) if f.lower().endswith("." + formaat.lower()))
        log("Export", formaat, r, len(uitkomst[formaat]))
    meting["export"] = {"stl": len(uitkomst["STL"]), "3mf": len(uitkomst["3MF"]), "namen": uitkomst["STL"],
                        "zichtbare_delen": len(delen)}
    # leggen: rijen van groot naar klein, elk deel rechtop op de plaat (z laag = 0)
    def maat(o):
        """Kader uit de echte (geëvalueerde) hoekpunten: bound_box telt verborgen hulpvormen soms mee."""
        dg = bpy.context.evaluated_depsgraph_get()
        oe = o.evaluated_get(dg)
        me = oe.to_mesh()
        bb = [oe.matrix_world @ v.co for v in me.vertices] or [o.matrix_world @ Vector(c) for c in o.bound_box]
        oe.to_mesh_clear()
        return (Vector((min(p.x for p in bb), min(p.y for p in bb), min(p.z for p in bb))),
                Vector((max(p.x for p in bb), max(p.y for p in bb), max(p.z for p in bb))))
    gat = float(os.environ.get("GB_GAT", "12"))
    breed_max = float(os.environ.get("GB_RIJ", "260"))
    lijst = sorted(delen, key=lambda o: -((maat(o)[1] - maat(o)[0]).x * (maat(o)[1] - maat(o)[0]).y))
    rijen, rij, x = [], [], 0.0
    for o in lijst:
        lo, hi = maat(o)
        w = hi.x - lo.x
        if rij and x + w > breed_max:
            rijen.append(rij)
            rij, x = [], 0.0
        rij.append(o)
        x += w + gat
    if rij:
        rijen.append(rij)
    if os.environ.get("GB_LEG") == "lichaam" and len(delen) == 10:
        # ronde 2 (#101, mens): zoals een lichaam uit elkaar ligt. Achter: dij, bovenarm, romp, bovenarm, dij;
        # voor: scheen, onderarm, hoofd, onderarm, scheen. Welk deel wat is volgt uit de rusthouding (hoogte, links/rechts).
        mid_ = {o.name: (maat(o)[0] + maat(o)[1]) / 2 for o in delen}
        vol = {o.name: (maat(o)[1] - maat(o)[0]).x * (maat(o)[1] - maat(o)[0]).y * (maat(o)[1] - maat(o)[0]).z for o in delen}
        romp = max(delen, key=lambda o: vol[o.name])
        rest = [o for o in delen if o is not romp]
        hoofd = max(rest, key=lambda o: mid_[o.name].z if abs(mid_[o.name].x) < 15 else -1e9)
        rest = sorted([o for o in rest if o is not hoofd], key=lambda o: -mid_[o.name].z)
        paren = [sorted(rest[i:i + 2], key=lambda o: mid_[o.name].x) for i in range(0, 8, 2)]
        bov, ond, dij, sch = paren
        rijen = [[sch[0], ond[0], hoofd, ond[1], sch[1]], [dij[0], bov[0], romp, bov[1], dij[1]]]   # rij 0 = voor
        meting["leg"] = {"voor": [o.name for o in rijen[0]], "achter": [o.name for o in rijen[1]]}
    y = 0.0
    plek = {}
    for rij in rijen:
        diep = max(maat(o)[1].y - maat(o)[0].y for o in rij)
        tot = sum(maat(o)[1].x - maat(o)[0].x for o in rij) + gat * (len(rij) - 1)
        x = -tot / 2
        for o in rij:
            lo, hi = maat(o)
            d = Vector((x - lo.x, y + (diep - (hi.y - lo.y)) / 2 - lo.y, -lo.z))
            o.matrix_world = Matrix.Translation(d) @ o.matrix_world
            plek[o.name] = d
            x += hi.x - lo.x + gat
        y += diep + gat
    bpy.context.view_layer.update()
    meting["rijen"] = [len(r) for r in rijen]
    verberg_rest(delen)
    cam = scene(delen)
    lo = Vector((min(maat(o)[0].x for o in delen), min(maat(o)[0].y for o in delen), 0))
    hi = Vector((max(maat(o)[1].x for o in delen), max(maat(o)[1].y for o in delen),
                 max(maat(o)[1].z for o in delen)))
    mid = (lo + hi) / 2
    # printplaat onder de delen: afgeronde plaat, iets lichter raster om de 10 mm en een gouden rand (alleen decor)
    rand = float(os.environ.get("GB_PLAATRAND", "26"))
    vloer = bpy.context.scene.objects.get("hb_vloer")
    if vloer is not None:
        vloer.location.z = -7.0
    bpy.ops.mesh.primitive_cube_add(size=1, location=(mid.x, mid.y, -1.5))
    plaat = bpy.context.active_object
    plaat.name = "gb_plaat"
    plaat.scale = (hi.x - lo.x + 2 * rand, hi.y - lo.y + 2 * rand, 3.0)
    bpy.ops.object.transform_apply(scale=True)
    bev = plaat.modifiers.new("rond", "BEVEL")
    bev.width, bev.segments = 10.0, 8
    bev.affect = "EDGES"
    oud_raster = os.environ.get("HB_RASTER")
    os.environ["HB_RASTER"] = os.environ.get("GB_PLAATRASTER", "4A3A5C")
    plaat.data.materials.append(printbed(mat("gb_plaat", "221A2C", rough=0.5, coat=0.2), stap=10.0, dik=0.25))
    if oud_raster is None:
        del os.environ["HB_RASTER"]
    else:
        os.environ["HB_RASTER"] = oud_raster
    bpy.ops.mesh.primitive_cube_add(size=1, location=(mid.x, mid.y, -4.0))
    lijst_ = bpy.context.active_object
    lijst_.name = "gb_plaatrand"
    lijst_.scale = (hi.x - lo.x + 2 * rand + 5, hi.y - lo.y + 2 * rand + 5, 6.0)
    bpy.ops.object.transform_apply(scale=True)
    b2 = lijst_.modifiers.new("rond", "BEVEL")
    b2.width, b2.segments = 11.0, 8
    lijst_.data.materials.append(mat("gb_plaatgoud", os.environ.get("HB_GOUD", "FFB938"), rough=0.3, metal=0.6,
                                     emis=float(os.environ.get("GB_RANDGLOED", "0.6"))))
    meting["plaat_mm"] = [round(hi.x - lo.x + 2 * rand), round(hi.y - lo.y + 2 * rand)]
    doel = Vector((mid.x, mid.y, hi.z * 0.25))
    camera_op(cam, doel, Vector((float(os.environ.get("GB_ZIJ", "-0.25")), -1.0, float(os.environ.get("GB_OP", "0.95")))),
              float(os.environ.get("GB_AFSTAND", "700")), float(os.environ.get("GB_LENS", "60")))
    # punten voor kaartjes: midden-boven van elk deel in beeld, met de bestandsnaam van de STL
    punten = {}
    for o in delen:
        lo_, hi_ = maat(o)
        top = Vector(((lo_.x + hi_.x) / 2, (lo_.y + hi_.y) / 2, hi_.z))
        punten[o.name] = {"beeld": naar_beeld(cam, top), "bestand": bpy.path.clean_name(o.name) + ".stl",
                          "soort": o.get("cj_soort", ""), "gewricht": o.get("cj_naam", "")}
    meting["punten"] = punten
    render("delen")


{"knie": knie, "klik": klik, "strip": strip, "bereik": bereik, "delen": delen_plat}[MODUS]()
