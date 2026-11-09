"""Plaatjes 11 en 12 (eis 8 van het scharnier, ontwerp betaald v1.1): betaalde build, staaf van 10 mm met een
scharnier, pose 60 (11-scharnier) en voorbij de eindstop met rode vlakken (12-scharnier-rood), hele venster
zoals de winkelschermen 8 en 9. Draait in een eigen stap met de betaalde zip, zodat de gratis schermtest
(schermen.py, plaatjes 1 tot 10) precies gelijk blijft:
    blender --python e2e/scherm_scharnier.py -- <map> <betaalde zip>
Regels "SCHARNIER OK pose" en "SCHARNIER OK rood" zijn wat de workflow eist; de rode pixels tellen we op het
X-scherm (r > 0,7, g en b < 0,3). Zoals 8 en 9: gradenboog van het scharnier (betaald/scharnier_boog.py) met de
regel "Bends 0° to N°" in beeld, het scharnier in het midden. De boog bewijzen we met pixels: eerst een opname
zonder boog, dan met, en de pixels die duidelijk lichter werden zijn de boog.

Plaatje 12 staat 3 graden voorbij de stop (bij 8 graden lag B dwars over A). De staaf is om de mm in de lengte
doorgesneden: de zijvlakken van een gewone cilinder lopen over de hele lengte, dan wordt bij elke aanraking de
hele bovenkant van A rood in plaats van alleen de stop."""
import importlib
import math
import os
import subprocess
import sys

import bmesh

import bpy
import numpy as np
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402
import scherm_basis  # noqa: E402
from scherm_basis import log, schiet, toestand, weergave, zijbalk, zip_pad  # noqa: E402

POSE = 60.0
VOORBIJ = 3.0  # graden voorbij de gemeten stop op plaatje 12
# Rood op 12 alleen rond de stop: hoogstens 3000 pixels. Met de hele bovenkant van A rood (run 42626458193,
# B 8 graden voorbij) waren het er 4006 en 4039; de stop is een strook van een paar mm bij H, dus ruim minder.
# Ondergrens 30 en niet 300: het rode materiaal is in Solid belicht meestal donkerder dan r 0,7 (run 42633644592:
# heel A rood gaf maar 193 pixels), dus 300 zou ook bij een goede stop falen. Dat er rood is bewijzen de rode
# vlakken; de pixels laten zien dat het in beeld komt.
ROOD_MIN, ROOD_MAX = 30, 3000
ROOD_STRAAL = 3.0  # rode vlakken: middelpunt binnen 15 mm van H (A is 20 mm lang; de stopvlakken reiken tot 12,4)
STAAF_R = 5.0
BOOG_MIN = 1500  # pixels die met de boog aan duidelijk lichter zijn (boog, streepjes, getal, kop)
staat = {}


def _mod(naam):
    m = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return importlib.import_module(f"{m}.{naam}")


def _pixels(pad):
    img = bpy.data.images.load(pad)
    w, h = img.size
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    bpy.data.images.remove(img)
    return px.reshape(-1, 4), (w, h)


def zonder_boog(naam):
    """Opname van het X-scherm met de boog uit (alleen voor de vergelijking, niet in de map met plaatjes)."""
    pad = os.path.join("/tmp", naam)
    subprocess.run(["import", "-window", "root", pad], capture_output=True, text=True)
    return pad


def boog_pixels(zonder, met):
    """Pixels die met de boog aan minstens 0,25 lichter zijn en bijna grijs/wit (boogkleur wit)."""
    if not (os.path.exists(zonder) and os.path.exists(met)):
        return -1
    a, _ = _pixels(zonder)
    b, _ = _pixels(met)
    licht = b[:, :3].mean(axis=1) - a[:, :3].mean(axis=1)
    wit = (b[:, :3].max(axis=1) - b[:, :3].min(axis=1)) < 0.12
    return int(np.count_nonzero((licht > 0.25) & wit))


def staaf_in_plakken(naam, straal, lengte=40.0):
    """Als figuren.staaf, maar om de mm in de lengte doorgesneden (zie boven)."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=128, radius1=straal, radius2=straal, depth=lengte)
    bm.transform(Matrix.Rotation(math.pi / 2, 4, "Y"))
    for i in range(1, int(lengte)):
        x = -lengte / 2 + i
        geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
        bmesh.ops.bisect_plane(bm, geom=geom, plane_co=(x, 0, 0), plane_no=(1, 0, 0))
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def rode_pixels(naam):
    pad = os.path.join(scherm_basis.uitmap, naam)
    if not os.path.exists(pad):
        return -1, None
    px, (w, h) = _pixels(pad)
    rood = int(np.count_nonzero((px[:, 0] > 0.7) & (px[:, 1] < 0.3) & (px[:, 2] < 0.3)))
    return rood, (w, h)


def plaats_scharnier():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    staaf = staaf_in_plakken("staaf", STAAF_R)
    staaf.color = (0.8, 0.8, 0.8, 1.0)
    figuren.maak_actief(staaf)
    m = Matrix.Identity(4)
    for i, v in enumerate((Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))):  # H, buigkant, lidas
        m.col[i][:3] = v
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.toon_bereik = 0.2, "CURSOR", False, False
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    staat["a"], staat["b"] = a, b
    log(f"SCHARNIER plaats: {uitslag}, A={a is not None} B={b is not None} "
        f"bereik={a.get('cj_bereik_graden') if a else None} melding={a.get('cj_melding') if a else None}")
    weergave()
    venster, gebied, _ = zijbalk()
    with bpy.context.temp_override(window=venster, area=gebied):
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.show_region_ui = ruimte.show_region_toolbar = ruimte.show_region_header = False
    ov = ruimte.overlay
    ov.show_text = ov.show_cursor = ov.show_axis_x = ov.show_axis_y = ov.show_floor = False
    if a is None:
        return
    rv3d = ruimte.region_3d
    rv3d.view_perspective = "PERSP"
    # Bijna langs H (het vlak van de boog), 25 graden gekanteld naar de lidas en 12 naar de buigkant, zodat ook
    # het stopvlak (dat H bevat) als vlak te zien is. Kijkhoek op de boog dan ruim boven 15 graden: getal en streepjes.
    h = Vector(a["cj_scharnier_as"]).normalized()
    lid = Vector(a["cj_as"]).normalized()
    buig = Vector(a["cj_buigkant"]).normalized()
    kijk = (h * math.cos(math.radians(25)) + lid * math.sin(math.radians(25))).normalized()
    kijk = (kijk * math.cos(math.radians(12)) + buig * math.sin(math.radians(12))).normalized()
    rv3d.view_rotation = kijk.to_track_quat("-Z", "Y")
    rv3d.view_distance = 60.0
    rv3d.view_location = Vector(a["cj_scharnier_punt"])  # het scharnier in het midden
    gebied.tag_redraw()


def zet(graden):
    a, b = staat.get("a"), staat.get("b")
    if a is None or b is None:
        log("SCHARNIER: geen delen")
        return 0
    wm = bpy.context.window_manager
    figuren.maak_actief(a)
    wm.cj_scharnier_pose = float(graden)  # de pose-schuif van het paneel (update draait B en kleurt rood)
    n = len(a.get("cj_rood_vlakken", [])) // 2
    log(f"SCHARNIER pose={graden} rood_vlakken={n}")
    return n


def rood_bij_stop(a):
    """Alle rode vlakken van A met hun middelpunt dicht bij het draaipunt (de stop, niet de rest van A)."""
    lijst = list(a.get("cj_rood_vlakken", []))
    punt = Vector(a["cj_scharnier_punt"])
    mw = a.matrix_world
    afstand = [(mw @ a.data.polygons[lijst[i]].center - punt).length for i in range(0, len(lijst), 2)]
    return (max(afstand) if afstand else 0.0)


def verslag(naam, graden, rood_vlakken, voorbij, zonder):
    rood, maat = rode_pixels(naam)
    a = staat.get("a")
    boog_mod = _mod("betaald.scharnier_boog")
    bogen = boog_mod.laatst.get("bogen", [])
    tb = bogen[0] if len(bogen) == 1 else {}
    wit = boog_pixels(zonder, os.path.join(scherm_basis.uitmap, naam))
    verst = rood_bij_stop(a) if a else -1.0
    tekst = boog_mod.tekst(a) if a else None
    if boog_mod.laatst.get("fout"):
        log(f"SCHARNIER boogfout: {boog_mod.laatst['fout']!r}")
    log(f"SCHARNIER handler={boog_mod._handler[0] is not None} boog_aan={bpy.context.window_manager.cj_scharnier_boog} "
        f"laatst={boog_mod.laatst}")
    eisen = {
        "plaatje bestaat": rood >= 0,
        "maat 1920x1080": maat == (1920, 1080),
        "pose klopt": bool(a) and abs(staat["b"].get("cj_pose_graden", -1) - graden) < 1e-6,
        "voorbij de stop klopt": bool(a) and (graden > a["cj_bereik_graden"]) == voorbij,
        "rode vlakken alleen voorbij": (rood_vlakken > 0) == voorbij,
        "rode pixels": ROOD_MIN <= rood <= ROOD_MAX if voorbij else rood < 50,
        "rood alleen bij de stop": verst <= ROOD_STRAAL * STAAF_R,
        "een boog getekend": len(bogen) == 1,
        "boog hoort bij deze pose": tb.get("pose") == round(float(graden), 3),
        "getal gelijk aan paneel": bool(tekst) and tb.get("getal") == f"{boog_mod.grens(a)}\u00b0"
        and tekst == f"Bends 0\u00b0 to {boog_mod.grens(a)}\u00b0",
        "getal getekend": bool(tb.get("getal_getekend")),
        "kop Bends in beeld": tb.get("kop") == tekst,
        "streepjes elke 5 graden": bool(a) and tb.get("streepjes") == boog_mod.grens(a) // 5 + 1,
        "voorbij klopt": tb.get("voorbij") == voorbij,
        "rode tekst alleen voorbij": (tb.get("voorbij_tekst") is not None) == voorbij,
        "boog in pixels": wit >= BOOG_MIN,
    }
    mis = [k for k, ok in eisen.items() if not ok]
    log(f"SCHARNIER {'OK' if not mis else 'FOUT'} {'rood' if voorbij else 'pose'} {naam} maat={maat} "
        f"rode_pixels={rood} rode_vlakken={rood_vlakken} verst_rood={verst:.2f} boog_pixels={wit} tekst={tekst} "
        f"boog={tb} pose={graden} "
        f"bereik={a.get('cj_bereik_graden') if a else None} mis={mis}")


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, betaalde zip {zip_pad}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        return 1.0
    if n == 2:
        plaats_scharnier()
        bpy.context.window_manager.cj_scharnier_boog = False
        staat["rood11"] = zet(POSE)
        return 2.0
    if n == 3:
        staat["zonder11"] = zonder_boog("cj_zonder_11.png")
        bpy.context.window_manager.cj_scharnier_boog = True
        return 2.0
    if n == 4:
        schiet("11-scharnier.png")
        verslag("11-scharnier-x.png", POSE, staat["rood11"], voorbij=False, zonder=staat["zonder11"])
        a = staat.get("a")
        staat["voorbij"] = round(float(a["cj_bereik_graden"]) + VOORBIJ, 1) if a else 0.0
        bpy.context.window_manager.cj_scharnier_boog = False
        staat["rood12"] = zet(staat["voorbij"])
        return 2.0
    if n == 5:
        staat["zonder12"] = zonder_boog("cj_zonder_12.png")
        bpy.context.window_manager.cj_scharnier_boog = True
        return 2.0
    if n == 6:
        schiet("12-scharnier-rood.png")
        verslag("12-scharnier-rood-x.png", staat["voorbij"], staat["rood12"], voorbij=True, zonder=staat["zonder12"])
        return 0.5
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
