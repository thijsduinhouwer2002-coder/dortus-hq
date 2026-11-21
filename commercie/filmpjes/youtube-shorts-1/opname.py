"""Opname voor YouTube Shorts reeks 1 (21 nov 2026, opdracht hoofdchat ±12:45 NL): staande opname (X-scherm 1080x1920)
in de echte Blender 5.3.0, zonder zijbalk, op de MakeHuman-figuur (base.obj, CC0) met de rig uit e2e/proef_mens.py
(linkerknie 120 en linkerelleboog 140 in Limit Rotation).
    CJ_SOORT=pro|gratis CJ_MENS_OBJ=<base.obj> blender --gpu-backend opengl start.blend --python opname.py -- <map> <zip>
Twee soorten:
  pro     betaalde add-on 1.1.0, figuur lichtblauw. Delen: heel (figuur met rig), knop (Figure from rig),
          elleboog (linkerelleboog 0 tot de stop, voorbij de stop rood, terug), schouder (kogel in de schouder: bereik,
          voorbij de grens rood, dan rond in 8 richtingen), pose (knieen, ellebogen en kogels samen gebogen, rond).
  gratis  gratis add-on (zelfde code als op extensions.blender.org, zonder betaald/), figuur zandkleur, geen rig.
          Delen: heel, cursor (3D-cursor in de nek), plaats (Place joint: kogel met pasband, Exploded view),
          bereik (kogel buigen tot de grens, voorbij de grens rood, dan rond in 8 richtingen).
Het script kleurt niets aan de add-on: bogen, getallen, rood en pasband komen van de add-on. Het zet de camera, de
kleur van de figuur (invoer), de 3D-cursor en de schuiven zoals een gebruiker. Regels "KORT OK <deel>" eist de workflow.
Uit: <map>/beelden/b00001.png ... en <map>/film.json (eerste beeld per deel, metingen)."""
import importlib
import json
import math
import os
import sys

import bpy
from mathutils import Euler, Vector
from mathutils.bvhtree import BVHTree

SOORT = os.environ.get("CJ_SOORT", "pro")
E2E = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                                   "producten", "blender-gewrichten", "e2e"))
sys.path.insert(0, E2E)
_film = open(os.path.join(E2E, "film_pro.py"), encoding="utf-8").read()
_film = _film[:_film.index("def verloop():")].replace(
    "sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))", "")
exec(compile(_film, "film_pro_hulp", "exec"), globals())   # noqa: S102 (eigen code uit de repo)
_mens = open(os.path.join(E2E, "scherm_mens.py"), encoding="utf-8").read()
_mens = _mens.replace("bpy.app.timers.register(stap, first_interval=3.0)", "")
_mens = _mens.replace("HIER = os.path.dirname(os.path.abspath(__file__))", f"HIER = {E2E!r}")
SM = {"__name__": "scherm_mens_hulp", "__file__": os.path.join(E2E, "scherm_mens.py")}
exec(compile(_mens, "scherm_mens_hulp", "exec"), SM)   # noqa: S102
M, A = SM["M"], SM["A"]
film["metingen"] = {"soort": SOORT}
film["soort"] = SOORT
KLEUR = {"pro": (0x9F, 0xBF, 0xE0), "gratis": (0xE2, 0xC6, 0xA2)}[SOORT]   # sRGB: lichtblauw of zand
VOORBIJ = 12.0   # graden voorbij de stop bij een scharnier
VOORBIJ_KOGEL = 8.0


def lin(c):
    return tuple(((x / 255.0 + 0.055) / 1.055) ** 2.4 for x in c) + (1.0,)


SCHAAL = 1.5      # zichtbare hoogte van het staande kijkvenster in mm = SCHAAL x view_distance (gemeten op de proef)
OMHOOG = 109      # px: het punt waar de camera op richt komt zoveel boven het midden van het scherm (ruimte voor tekst)


def zet_rot(q, afstand, punt):
    _, gebied, _ = zijbalk()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "ORTHO"
    rv.view_rotation = q
    omhoog = q @ Vector((0.0, 1.0, 0.0))
    rv.view_location = tuple(Vector(punt) - omhoog * (OMHOOG * SCHAAL * afstand / 1920.0))
    rv.view_distance = afstand
    gebied.tag_redraw()


def cam(draai, kantel, afstand, punt):
    zet_rot(Euler((math.radians(kantel), 0.0, math.radians(draai)), "XYZ").to_quaternion(), afstand, punt)


def cam_kijk(kijk, afstand, punt):
    """Camera die langs `kijk` kijkt, met wereld-z zo veel mogelijk omhoog in beeld."""
    zet_rot(Vector(kijk).normalized().to_track_quat("-Z", "Y"), afstand, punt)


def beste_richting(b, wens):
    """Richting k (0 tot 7) van de kogel waarin deel B het meest naar `wens` kantelt."""
    ue = importlib.import_module(naam_module() + ".uit_elkaar")
    as_ = Vector(b["cj_as"]).normalized()
    r = ue.richtingen(as_)
    return max(range(len(r)), key=lambda i: r[i].dot(Vector(wens).normalized()))


def mengen(a, b, t):
    return [x + (y - x) * t for x, y in zip(a, b)]


def stuk(stappen, doe):
    for i in range(stappen):
        doe(zacht(i / max(1, stappen - 1)))
        yield 0.04
        neem()


def kijk_staand():
    _, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.shading.type = "SOLID"
    ruimte.shading.color_type = "MATERIAL"
    ruimte.clip_start, ruimte.clip_end = 0.1, 10000
    zijbalk_aan(False)
    ov = ruimte.overlay
    ov.show_cursor = False
    ov.show_stats = False
    try:
        ruimte.show_region_header = False
        ruimte.show_region_tool_header = False
        ruimte.show_region_toolbar = False
    except Exception as fout:  # noqa: BLE001
        log(f"KORT kop: {fout}")


def figuur(met_rig):
    A["leeg"]()
    ob, punten = M["laad_mens"](os.environ["CJ_MENS_OBJ"])
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    SM["etalagepop"](ob)
    ob.data.materials[0].diffuse_color = lin(KLEUR)
    arm = None
    if met_rig:
        arm = M["maak_rig"](punten)
        arm.data.display_type = "STICK"
        arm.show_in_front = True
        ob.modifiers.new("Armature", "ARMATURE").object = arm
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    return ob, arm, punten


def geen_selectie():
    for o in bpy.context.view_layer.objects:
        o.select_set(False)


def paar(naam, soort="SCHARNIER"):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_figuur") and o.get("cj_naam") == naam and o.get("cj_soort", "") == soort:
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def kogel_paar(naam):
    a = b = None
    for o in bpy.context.scene.objects:
        if o.get("cj_naam") == naam and "cj_buig_graden" in o:
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def buig_scharnier(b, graden):
    bpy.context.view_layer.objects.active = b
    bpy.context.window_manager.cj_scharnier_pose = round(graden, 1)


def grens(a, k):
    return importlib.import_module(naam_module() + ".paneel").richting_graden(a, k)


def naam_module():
    return next(x.module for x in bpy.context.preferences.addons if x.module.endswith("click_joints"))


def nek_cursor(ob, p):
    """3D-cursor in het midden van de nek, Z langs de nek (van nek naar hoofd), zoals een gebruiker hem zet."""
    as_ = (p["head"] - p["neck"]).normalized()
    o = p["neck"] + (p["head"] - p["neck"]) * float(os.environ.get("CJ_NEK_T", "0.15"))
    dg = bpy.context.evaluated_depsgraph_get()
    bvh = BVHTree.FromObject(ob, dg)
    q = as_.to_track_quat("Z", "Y")
    m = q.to_matrix()
    for _ in range(2):
        for kol in (0, 1):
            w = m.col[kol].normalized()
            h1, h2 = bvh.ray_cast(o, w), bvh.ray_cast(o, -w)
            if h1[0] is None or h2[0] is None:
                continue
            o = o + w * (h1[3] - h2[3]) / 2
    c = bpy.context.scene.cursor
    c.location = o
    c.rotation_mode = "QUATERNION"
    c.rotation_quaternion = q
    return o


def start():
    log(f"Blender {bpy.app.version_string}, soort {SOORT}, zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)


def verloop_pro():
    wm = bpy.context.window_manager
    start()
    yield 1.0
    ob, arm, p = figuur(True)
    naam = ob.name
    SM["rustig"]()
    leeg_beeld()
    kijk_staand()
    heel = (0.0, 0.0, 112.0)
    D_HEEL = 290.0
    cam(-30, 84.0, D_HEEL, heel)
    yield 1.5

    deel("heel")
    yield from stuk(75, lambda t: cam(-30 + 22 * t, 84.0, D_HEEL, heel))
    log("KORT OK heel")

    deel("knop")
    neem(10)
    uitslag = bpy.ops.click_joints.figuur_uit_rig()
    arm.hide_set(True)
    fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
    lijst = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    film["metingen"]["gewrichten"] = len(lijst)
    film["metingen"]["regels"] = [fig.regel(r) for r in lijst]
    log(f"KORT knop {uitslag} {len(lijst)} gewrichten {film['metingen']['regels']}")
    geen_selectie()
    yield 0.5
    yield from stuk(60, lambda t: cam(-8 + 16 * t, 84.0, D_HEEL, heel))
    log(f"KORT {'OK' if len(lijst) >= 4 else 'FOUT'} knop")

    # elleboog: linkerelleboog (+x), van schuin voor-links, dichtbij
    a, b = paar("Left elbow")
    if a is None or b is None:
        log("KORT FOUT elleboog: geen linkerelleboog")
        bpy.ops.wm.quit_blender()
        return
    stop = float(a["cj_bereik_graden"])
    film["metingen"]["elleboog_stop"] = stop
    geen_selectie()
    buig_scharnier(b, 0.0)
    e = p["l-elbow"]
    lidas = (p["l-elbow"] - p["l-shoulder"]).normalized()
    h = lidas.cross(Vector((0.0, -1.0, 0.0))).normalized()   # scharnieras: dwars op bovenarm en buigkant (voor)
    if h.z > 0:
        h = -h    # camera boven en buiten de arm, kijkt naar binnen en omlaag
    kijk_e = (h + Vector((0.0, 0.3, 0.0))).normalized()
    film["metingen"]["elleboog_kijk"] = [round(x, 3) for x in kijk_e]
    mid_e = e + Vector((0.0, -6.0, 6.0))
    cam_kijk(kijk_e, 60.0, mid_e)
    yield 1.0
    deel("elleboog")
    neem(12)
    s = math.floor(stop * 10) / 10
    yield from stuk(105, lambda t: buig_scharnier(b, s * t))
    neem(50)
    film["metingen"]["elleboog_pose_stop"] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    deel("elleboog_rood")
    yield from stuk(36, lambda t: buig_scharnier(b, stop + VOORBIJ * t))
    neem(75)
    film["metingen"]["elleboog_pose_rood"] = round(float(b.get("cj_pose_graden", 0.0)), 1)
    film["metingen"]["elleboog_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
    yield from stuk(36, lambda t: buig_scharnier(b, stop + VOORBIJ - (stop + VOORBIJ - 90.0) * t))
    neem(15)
    log(f"KORT {'OK' if film['metingen']['elleboog_rood_vlakken'] > 0 else 'FOUT'} elleboog {film['metingen']}")
    buig_scharnier(b, 0.0)
    yield 0.3

    # schouder: kogel in de linkerschouder, dichtbij, eerst met Exploded view (kogel en kom te zien), dan dicht
    # (geen pose: een gekantelde kogel draait alleen het deel tot de elleboog, dat geeft een knik bij de elleboog)
    ka, kb = kogel_paar("Left shoulder")
    if ka is None:
        log("KORT FOUT schouder: geen kogel")
        bpy.ops.wm.quit_blender()
        return
    inst = bpy.context.scene.click_joints
    inst.toon_bereik = True
    inst.pose_graden = 0.0
    film["metingen"]["schouder_grens"] = grens(ka, 0) or 20
    film["metingen"]["schouder_buig_graden"] = [round(float(x), 1) for x in ka["cj_buig_graden"]]
    film["metingen"]["schouder_passing"] = ka.get("cj_passing")
    film["metingen"]["schouder_wand_mm"] = round(float(ka.get("cj_wand_mm", -1)), 2)
    geen_selectie()
    bpy.context.view_layer.objects.active = None
    sch = p["l-shoulder"] + (p["l-elbow"] - p["l-shoulder"]) * 0.3
    mid_s = (sch.x, sch.y, sch.z)
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    cam(10, 86.0, 62.0, mid_s)
    yield 1.0
    deel("schouder")
    yield from stuk(180, lambda t: cam(10 + 30 * t, 86.0, 62.0, mid_s))
    inst.uit_elkaar = False
    bpy.context.view_layer.update()
    yield 0.3
    deel("schouder_dicht")
    yield from stuk(150, lambda t: cam(40 + 15 * t, 86.0 - 4 * t, 62.0, mid_s))
    log(f"KORT OK schouder grens={film['metingen']['schouder_grens']} passing={film['metingen']['schouder_passing']}")
    yield 0.3

    # pose: knieen, ellebogen en kogels samen, rond
    standen = {"Right knee": 75.0, "Left knee": 20.0, "Left elbow": 110.0, "Right elbow": 60.0}
    paren = {n: paar(n) for n in standen}
    inst.toon_bereik = True
    cam(-30, 84.0, D_HEEL, heel)
    yield 0.8
    deel("pose")
    neem(8)

    def zet_pose(t):
        for n, (pa, pb) in paren.items():
            if pb is not None:
                buig_scharnier(pb, standen[n] * t)
        geen_selectie()
        cam(-30 + 20 * t, 84.0, D_HEEL, heel)
    yield from stuk(75, zet_pose)
    deel("pose_rond")
    yield from stuk(270, lambda t: cam(-10 + 150 * t, 84.0, D_HEEL, heel))
    rood = sum(len(pa.get("cj_rood_vlakken", [])) // 2 for pa, _pb in paren.values() if pa is not None)
    film["metingen"]["pose_rood_vlakken"] = rood
    film["metingen"]["pose"] = standen
    log(f"KORT OK pose rood={rood}")


def verloop_gratis():
    start()
    yield 1.0
    ob, _arm, p = figuur(False)
    SM["rustig"]()
    leeg_beeld()
    kijk_staand()
    hoofd = (0.0, 0.0, 165.0)
    cam(-30, 86.0, 170.0, hoofd)
    yield 1.5
    deel("heel")
    yield from stuk(45, lambda t: cam(-30 + 15 * t, 86.0, 170.0, hoofd))
    log("KORT OK heel")

    nek = nek_cursor(ob, p)
    blik = nek + Vector((0.0, 0.0, 6.0))   # camera iets boven de nek: hoofd en schouders in beeld
    film["metingen"]["nek_cursor"] = [round(x, 2) for x in nek]
    _, gebied, _ = zijbalk()
    gebied.spaces.active.overlay.show_cursor = True
    deel("cursor")
    yield from stuk(30, lambda t: cam(-15 + 5 * t, 86.0, 170.0 - 95 * t, mengen(hoofd, blik, t)))
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = True
    inst.toon_bereik = False
    A["actief"](ob)
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    gebied.spaces.active.overlay.show_cursor = False
    geen_selectie()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    a = next((d for d in delen if d.get("cj_deel") == "A"), None)
    film["metingen"]["plaats"] = str(uitslag)
    film["metingen"]["delen"] = len(delen)
    film["metingen"]["passing"] = a.get("cj_passing") if a else None
    film["metingen"]["kogel_mm"] = round(inst.kogel_mm, 2)
    film["metingen"]["wand_mm"] = round(float(a.get("cj_wand_mm", -1)), 2) if a else None
    log(f"KORT plaats {uitslag} delen={len(delen)} passing={film['metingen']['passing']} kogel={inst.kogel_mm}")
    if a is None or "cj_buig_graden" not in a:
        log("KORT FOUT plaats: geen kogel")
        bpy.ops.wm.quit_blender()
        return
    deel("plaats")
    yield from stuk(90, lambda t: cam(-10 + 40 * t, 86.0, 75.0, blik))
    log("KORT OK plaats")

    inst.uit_elkaar = False
    inst.toon_bereik = True
    b = next((d for d in delen if d.get("cj_deel") == "B"), None)
    k = beste_richting(b, (1.0, 0.0, 0.0))   # hoofd kantelt opzij: in het vlak van het beeld (camera van voren)
    inst.pose_richting = str(k)
    g = grens(a, k) or 20
    film["metingen"]["nek_grens"] = g
    film["metingen"]["nek_buig_graden"] = [round(float(x), 1) for x in a["cj_buig_graden"]]
    cam(0, 88.0, 75.0, blik)
    yield 0.5
    deel("bereik")
    neem(8)
    yield from stuk(54, lambda t: setattr(inst, "pose_graden", round(g * t)))
    neem(30)
    deel("bereik_rood")
    yield from stuk(24, lambda t: setattr(inst, "pose_graden", round(g + VOORBIJ_KOGEL * t)))
    neem(45)
    film["metingen"]["nek_pose_rood"] = inst.pose_graden
    film["metingen"]["nek_rood_vlakken"] = len(a.get("cj_rood_vlakken", [])) // 2
    yield from stuk(24, lambda t: setattr(inst, "pose_graden", round((g + VOORBIJ_KOGEL) - (g + VOORBIJ_KOGEL - 12) * t)))
    deel("bereik_rond")
    for i in range(16):
        inst.pose_richting = str((k + i // 2) % 8)
        for _ in range(6):
            cam(-i * 1.2, 88.0, 75.0, blik)
            yield 0.04
            neem()
    log(f"KORT OK bereik grens={g} rood={film['metingen']['nek_rood_vlakken']}")


def verloop():
    try:
        yield from (verloop_pro() if SOORT == "pro" else verloop_gratis())
    except Exception as fout:  # noqa: BLE001
        import traceback
        log(f"KORT FOUT {fout}\n{traceback.format_exc()}")
    deel("eind")
    with open(os.path.join(scherm_basis.uitmap, "film.json"), "w") as f:
        json.dump(film, f, indent=1)
    log(f"KORT klaar {film['n']} beelden")
    bpy.ops.wm.quit_blender()


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None


bpy.app.timers.register(stap, first_interval=3.0)
