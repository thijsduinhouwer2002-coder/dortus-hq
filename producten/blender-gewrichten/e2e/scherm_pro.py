"""Winkelplaatjes voor Click Joints Pro (Daan, antwoord op plaatjes 11 en 12, 10 nov 04:45): het betaalde scharnier
op een echt ding, een houten been (dij en scheen, rond en taps, met een knie), in plaats van twee cilinders.
    blender --python e2e/scherm_pro.py -- <map> <betaalde zip>
Plaatjes (alle 1920x1080, hele X-scherm):
  13-pro-knie-schoon-x.png  pose 60, zonder gradenboog (bron voor de poster in ontwerp/click-joints/pro/)
  13-pro-knie-x.png         pose 60 met de gradenboog van de add-on
  14-pro-knie-rood-x.png    3 graden voorbij de gemeten stop, rood van de add-on op A, B doorzichtig
En pro-knie.json met de echte getallen (bereik, speling, stand) en de plek in beeld van H en de lidas, voor de poster.

Wat het script zelf doet en de add-on niet (alleen weergave, de export verandert niet):
- Groene band: de vlakken van A en B die binnen speling + 2 mm van het andere deel liggen (een band langs de naad en de
  spleet rond de knokkel) krijgen het passingmateriaal "Good fit" van de gratis versie, zodat het één familie is met plaatje 8.
  De add-on kleurt het scharnier zelf (nog) niet; de band toont waar de 0,2 mm speling zit.
- Op 14 is B doorzichtig (materiaal met alpha), zodat het rode vlak van A achter B als vlak te zien is.
- Eigen effen donkere achtergrond (viewport-kleur), geen selectie, geen middelpunt.
Regels "PRO OK pose", "PRO OK schoon" en "PRO OK rood" zijn wat de workflow eist."""
import importlib
import json
import math
import os
import subprocess
import sys

import bmesh
import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
import scherm_basis  # noqa: E402
from scherm_basis import log, schiet, toestand, weergave, zijbalk, zip_pad  # noqa: E402

POSE = 60.0
VOORBIJ = 3.0
SPELING = 0.2
BAND_MM = 2.0         # groen: vlakken binnen speling + dit van het andere deel (band langs de naad, als RING_MM 3 gratis)
ACHTERGROND = (0.017, 0.019, 0.026)  # #23262D van de gratis poster (lineair)
HOUT = (0.80, 0.58, 0.36, 1.0)
HOOGTE, BREEDTE = 0.62, 0.80
ROOD_MIN = 400        # rood als vlak: minstens zoveel heldere rode pixels (12 had er rond 30 tot 200)
staat = {}


def _mod(naam):
    m = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return importlib.import_module(f"{m}.{naam}")


def straal(x):
    """Profiel van het been langs de lidas (x in mm, knie op 0): dij naar -x, scheen naar +x, ronde uiteinden."""
    if x < 0:
        r = 5.6 + 1.6 * (min(-x, 40.0) / 40.0) ** 0.9
    else:
        r = 5.6 - 1.4 * min(x, 40.0) / 40.0 + 0.6 * math.exp(-((x - 15.0) / 7.0) ** 2)
    r += 0.35 * math.exp(-(x / 4.0) ** 2)  # knie iets dikker
    eind = abs(x) - 39.0
    if eind > 0:
        r *= math.sqrt(max(0.0, 1.0 - (eind / 3.0) ** 2))
    return r


def been(naam="been"):
    """Gesloten draaivorm om X: ringen om de 0,2 mm binnen 14 mm van de knie (fijne rode vlakken), verder om 0,5."""
    xs = [-42.0 + 0.25 * i for i in range(12)] + [-39.0 + 0.5 * i for i in range(50)]
    xs = [x for x in xs if x < -14.0] + [round(-14.0 + 0.2 * i, 4) for i in range(141)]
    xs += [14.0 + 0.5 * i for i in range(1, 51)] + [39.0 + 0.25 * i for i in range(1, 12)]
    xs = sorted(set(round(x, 4) for x in xs if -42.0 < x < 42.0))
    n = 160
    bm = bmesh.new()
    pool0 = bm.verts.new((-42.0, 0, 0))
    pool1 = bm.verts.new((42.0, 0, 0))
    ringen = []
    for x in xs:
        r = max(straal(x), 0.05)
        ringen.append([bm.verts.new((x, r * math.cos(2 * math.pi * k / n), r * math.sin(2 * math.pi * k / n)))
                       for k in range(n)])
    for k in range(n):
        bm.faces.new((pool0, ringen[0][(k + 1) % n], ringen[0][k]))
        bm.faces.new((pool1, ringen[-1][k], ringen[-1][(k + 1) % n]))
    for a, b in zip(ringen, ringen[1:]):
        for k in range(n):
            bm.faces.new((a[k], a[(k + 1) % n], b[(k + 1) % n], b[k]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    mat = bpy.data.materials.new("Hout")
    mat.diffuse_color = HOUT
    mat.roughness = 0.5
    me.materials.append(mat)
    return ob


def _bvh_wereld(ob, mw):
    me = ob.data
    me.calc_loop_triangles()
    return BVHTree.FromPolygons([mw @ v.co for v in me.vertices], [tuple(t.vertices) for t in me.loop_triangles])


def groene_band(a, b):
    """Vlakken van A en B binnen SPELING + BAND_MM van het andere deel (rechte stand) krijgen "Good fit"."""
    echte = _mod("uit_elkaar").echte_matrix
    groen = _mod("kleur").materiaal("groen")
    tel = {}
    for ob, ander in ((a, b), (b, a)):
        bvh = _bvh_wereld(ander, echte(ander))
        mw = echte(ob)
        me = ob.data
        if groen.name not in [m.name if m else None for m in me.materials]:
            me.materials.append(groen)
        vak = [m.name if m else None for m in me.materials].index(groen.name)
        n = 0
        for p in me.polygons:
            hit = bvh.find_nearest(mw @ p.center, SPELING + BAND_MM)
            if hit[0] is not None:
                p.material_index = vak
                n += 1
        me.update()
        tel[ob.name] = n
    return tel


def schoon_beeld():
    venster, gebied, _ = zijbalk()
    with bpy.context.temp_override(window=venster, area=gebied):
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.show_region_ui = ruimte.show_region_toolbar = ruimte.show_region_header = False
    ruimte.show_gizmo_navigate = False  # geen assenkruis en knoppen rechtsboven (in 4.2 wel in beeld)
    ov = ruimte.overlay
    ov.show_text = ov.show_cursor = ov.show_axis_x = ov.show_axis_y = ov.show_floor = False
    ov.show_outline_selected = False
    ov.show_object_origins = False
    ov.show_extras = False
    sh = ruimte.shading
    sh.background_type = "VIEWPORT"
    sh.background_color = ACHTERGROND
    sh.show_object_outline = False
    return gebied


def plaats():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    lid = been()
    figuren.maak_actief(lid)
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):  # H, buigkant, lidas
        m.col[i][:3] = v
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.toon_bereik = SPELING, "CURSOR", False, False
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("been_A"), bpy.data.objects.get("been_B")
    staat["a"], staat["b"] = a, b
    log(f"PRO plaats: {uitslag}, A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} knokkel_r={a.get('cj_knokkel_r') if a else None} "
        f"melding={a.get('cj_melding') if a else None}")
    weergave()
    gebied = schoon_beeld()
    if a is None or b is None:
        return
    staat["groen"] = groene_band(a, b)
    log(f"PRO groene band: {staat['groen']}")
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    h = Vector(a["cj_scharnier_as"]).normalized()
    lidas = Vector(a["cj_as"]).normalized()
    buig = Vector(a["cj_buigkant"]).normalized()
    kijk = (h * math.cos(math.radians(20)) + lidas * math.sin(math.radians(20))).normalized()
    kijk = (kijk * math.cos(math.radians(15)) + buig * math.sin(math.radians(15))).normalized()
    rv3d.view_rotation = kijk.to_track_quat("-Z", "Y")
    rv3d.view_distance = 120.0
    rv3d.view_location = Vector(a["cj_scharnier_punt"])
    gebied.tag_redraw()


def deselecteer():
    """Geen selectie in beeld (Daan punt 1): A blijft actief voor de pose-schuif, maar niets is geselecteerd."""
    a = staat.get("a")
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    if a is not None:
        bpy.context.view_layer.objects.active = a


def zet(graden):
    a = staat.get("a")
    if a is None:
        return 0
    bpy.context.view_layer.objects.active = a
    bpy.context.window_manager.cj_scharnier_pose = float(graden)
    deselecteer()
    n = len(a.get("cj_rood_vlakken", [])) // 2
    log(f"PRO pose={graden} rood_vlakken={n}")
    return n


def _punten(a, b):
    bpy.context.view_layer.update()
    lijst = []
    for ob in (a, b):
        co = np.empty(len(ob.data.vertices) * 3, dtype=np.float64)
        ob.data.vertices.foreach_get("co", co)
        mw = np.array(ob.matrix_world)
        lijst.append(np.c_[co.reshape(-1, 3), np.ones(len(co) // 3)] @ mw.T)
    return np.vstack(lijst)


def kader():
    a, b = staat.get("a"), staat.get("b")
    _, gebied, _ = zijbalk()
    if a is None or b is None or gebied is None:
        return
    rv3d = gebied.spaces.active.region_3d
    pw = rv3d.window_matrix.copy()
    pt = _punten(a, b)
    rot = rv3d.view_rotation.to_matrix()
    for _ in range(10):
        r4 = rv3d.view_rotation.to_matrix().to_4x4()
        vm = (Matrix.Translation(rv3d.view_location) @ r4 @ Matrix.Translation((0, 0, rv3d.view_distance))).inverted()
        h = pt @ np.array(pw @ vm).T
        ndc = h[:, :2] / h[:, 3:4]
        lo, hi = ndc.min(axis=0), ndc.max(axis=0)
        c, maat = (lo + hi) / 2.0, hi - lo
        d = rv3d.view_distance
        rv3d.view_location = rv3d.view_location + rot.col[0] * float(c[0] * d / pw[0][0]) \
            + rot.col[1] * float(c[1] * d / pw[1][1])
        rv3d.view_distance = d * float(max(maat[1] / (2 * HOOGTE), maat[0] / (2 * BREEDTE)))
    gebied.tag_redraw()
    log(f"PRO kader afstand={rv3d.view_distance:.1f}")


def in_beeld(punt):
    """Pixelplek (x van links, y van boven) van een wereldpunt op het hele scherm van 1920x1080."""
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d
    p = naar2d(regio, gebied.spaces.active.region_3d, Vector(punt))
    if p is None:
        return None
    return [round(regio.x + p.x, 1), round(venster.height - (regio.y + p.y), 1)]


def schrijf_json():
    """Echte getallen en plekken in beeld voor de poster (geen eigen getallen in de HTML)."""
    a, b = staat["a"], staat["b"]
    c = Vector(a["cj_scharnier_punt"])
    lidas = Vector(a["cj_as"]).normalized()
    voor_as = lidas.cross(Vector(a["cj_buigkant"])).normalized()
    echte = _mod("uit_elkaar").echte_matrix
    midden_b = sum((echte(b) @ Vector(hk) for hk in b.bound_box), Vector()) / 8.0
    d = lidas if (midden_b - c).dot(lidas) >= 0 else -lidas
    zij = voor_as.cross(d)
    boog_mod = _mod("betaald.scharnier_boog")
    grens = boog_mod.grens(a)
    R = 15.0  # mm, buiten het been (dij hoogstens 7,2 mm dik)
    boog = [in_beeld(c + R * (d * math.cos(math.radians(g)) + zij * math.sin(math.radians(g))))
            for g in range(0, grens + 1)]
    pose_r = Matrix.Rotation(math.radians(POSE), 3, voor_as)
    data = {
        "blender": bpy.app.version_string,
        "bereik_graden": round(float(a["cj_bereik_graden"]), 2), "grens": grens, "stand": int(a["cj_stand"]),
        "tekst": boog_mod.tekst(a), "speling_mm": SPELING, "pose": POSE, "knokkel_r": float(a["cj_knokkel_r"]),
        "centrum": in_beeld(c), "boog_r_mm": R, "boog": boog,
        "pose_eind": in_beeld(c + R * 1.12 * (d * math.cos(math.radians(POSE)) + zij * math.sin(math.radians(POSE)))),
        "pose_richting_check": list(pose_r @ d),
        "groene_vlakken": staat.get("groen"),
    }
    pad = os.path.join(scherm_basis.uitmap, "pro-knie.json")
    with open(pad, "w") as f:
        json.dump(data, f, indent=1)
    log(f"PRO json {pad} bereik={data['bereik_graden']} centrum={data['centrum']}")


def _pixels(naam):
    pad = os.path.join(scherm_basis.uitmap, naam)
    if not os.path.exists(pad):
        return None, None
    img = bpy.data.images.load(pad)
    w, h = img.size
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    bpy.data.images.remove(img)
    return px.reshape(-1, 4), (w, h)


def verslag(naam, soort, graden, rood_vlakken, boog_aan):
    px, maat = _pixels(naam)
    a, b = staat.get("a"), staat.get("b")
    if px is None:
        log(f"PRO FOUT {soort} {naam} ontbreekt")
        return
    rood = int(np.count_nonzero((px[:, 0] > 0.6) & (px[:, 1] < 0.3) & (px[:, 2] < 0.3)))
    groen = int(np.count_nonzero((px[:, 1] > 0.45) & (px[:, 0] < 0.35) & (px[:, 2] < 0.6)))
    # Oranje selectierand van Blender (rond 1,0 / 0,6 / 0,2): mag er niet zijn.
    oranje = int(np.count_nonzero((px[:, 0] > 0.85) & (px[:, 1] > 0.45) & (px[:, 1] < 0.7) & (px[:, 2] < 0.3)))
    rand = px.reshape(maat[1], maat[0], 4)[:20, :, :3]
    voorbij = soort == "rood"
    eisen = {
        "maat 1920x1080": maat == (1920, 1080),
        "pose klopt": bool(b) and abs(b.get("cj_pose_graden", -1) - graden) < 1e-6,
        "niets geselecteerd": not any(o.select_get() for o in bpy.context.view_layer.objects),
        "geen oranje rand": oranje < 40,
        "eigen achtergrond": float(rand.mean()) < 0.2 and float(rand[..., 2].mean() - rand[..., 0].mean()) > 0.02,
        "groene band in beeld": groen >= 300,
        "rode vlakken alleen voorbij": (rood_vlakken > 0) == voorbij,
        "boog zoals gevraagd": bool(bpy.context.window_manager.cj_scharnier_boog) == boog_aan,
    }
    if voorbij:
        eisen["rood als vlak"] = rood >= ROOD_MIN
    else:
        eisen["geen rood"] = rood < 50
    mis = [k for k, ok in eisen.items() if not ok]
    log(f"PRO {'OK' if not mis else 'FOUT'} {soort} {naam} rode_pixels={rood} groene_pixels={groen} "
        f"oranje={oranje} rand={float(rand.mean()):.3f} rood_vlakken={rood_vlakken} "
        f"bereik={a.get('cj_bereik_graden') if a else None} mis={mis}")


def doorzichtig_b():
    """Op 14: B half doorzichtig, zodat het rode vlak van A eronder als vlak leest (alleen weergave)."""
    b = staat.get("b")
    if b is None:
        return
    for i, m in enumerate(b.data.materials):
        if m is not None and m.name.startswith("Hout"):
            glas = m.copy()
            glas.name = "Hout doorzichtig"
            glas.diffuse_color = (HOUT[0], HOUT[1], HOUT[2], 0.18)
            if hasattr(glas, "surface_render_method"):
                glas.surface_render_method = "BLENDED"
            elif hasattr(glas, "blend_method"):
                glas.blend_method = "BLEND"
            b.data.materials[i] = glas


def kijk_van_boven():
    """Op 14 meer van de buigkant (boven) op de stop, zodat het rode stopvlak van A door B heen als vlak leest."""
    a = staat.get("a")
    _, gebied, _ = zijbalk()
    if a is None or gebied is None:
        return
    rv3d = gebied.spaces.active.region_3d
    h = Vector(a["cj_scharnier_as"]).normalized()
    lidas = Vector(a["cj_as"]).normalized()
    buig = Vector(a["cj_buigkant"]).normalized()
    kijk = (h * math.cos(math.radians(20)) + lidas * math.sin(math.radians(20))).normalized()
    kijk = (kijk * math.cos(math.radians(50)) + buig * math.sin(math.radians(50))).normalized()
    rv3d.view_rotation = kijk.to_track_quat("-Z", "Y")
    gebied.tag_redraw()


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    wm = bpy.context.window_manager
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        plaats()
        wm.cj_scharnier_boog = False
        staat["rood13"] = zet(POSE)
        return 2.0
    if n == 3:
        kader()
        return 1.5
    if n == 4:
        schiet("13-pro-knie-schoon.png")
        verslag("13-pro-knie-schoon-x.png", "schoon", POSE, staat["rood13"], False)
        if staat.get("a"):
            schrijf_json()
        wm.cj_scharnier_boog = True
        return 2.0
    if n == 5:
        schiet("13-pro-knie.png")
        verslag("13-pro-knie-x.png", "pose", POSE, staat["rood13"], True)
        a = staat.get("a")
        staat["voorbij"] = round(float(a["cj_bereik_graden"]) + VOORBIJ, 1) if a else 0.0
        doorzichtig_b()
        staat["rood14"] = zet(staat["voorbij"])
        kijk_van_boven()
        return 2.5
    if n == 6:
        kader()
        return 1.5
    if n == 7:
        schiet("14-pro-knie-rood.png")
        verslag("14-pro-knie-rood-x.png", "rood", staat["voorbij"], staat["rood14"], True)
        return 0.5
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
