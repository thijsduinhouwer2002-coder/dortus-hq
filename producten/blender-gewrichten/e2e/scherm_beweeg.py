"""Plaatjes 5, 6 en 7 van de schermtest: waaier van het gemeten bereik, pose voorbij de grens (rood)
en het platte lid (eis b). Opgesplitst uit schermen.py (opruimen 8 nov)."""
import importlib

import bpy
from mathutils import Vector

import figuren
from scherm_basis import log, maak_pop, plaats, weergave, zijbalk


def waaier():
    """Plaatje 5 (ronde k, gradenboog sinds ronde o): pop met gewricht, de gradenboog in richting 90 en een
    pose van 15 graden (binnen de grens, wens Daan), loodrecht op het buigvlak."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    maak_pop()
    plaats()
    inst = bpy.context.scene.click_joints
    inst.toon_bereik = True
    inst.pose_richting = "2"
    inst.pose_graden = 15.0
    weergave()
    venster, gebied, _ = zijbalk()
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A" and "cj_buig_graden" in o), None)
    if not gebied or a is None:
        log("WAAIER: geen weergave of geen deel A met bereik")
        return
    as_ = Vector(a["cj_as"]).normalized()
    u = as_.orthogonal().normalized()
    w = as_.cross(u).normalized()
    rich = w  # richting 2 = 90 graden (uit_elkaar.richtingen)
    kijk_r = as_.cross(rich).normalized()  # loodrecht op het buigvlak
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = kijk_r.to_track_quat("-Z", "Y")
    rv3d.view_distance = 14.0 * a["cj_kogel_r"]
    rechts = rv3d.view_rotation @ Vector((1.0, 0, 0))
    rv3d.view_location = Vector(a["cj_centrum"]) + as_ * (2.0 * a["cj_kogel_r"]) + rechts * (1.5 * a["cj_kogel_r"])
    gebied.tag_redraw()
    b = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "B" and "cj_buig_graden" in o), None)
    log(f"WAAIER bereik={list(a['cj_buig_graden'])} tijd={a.get('cj_buig_duur_s')} s pose={inst.pose_graden} "
        f"richting={inst.pose_richting} rood={len(a.get('cj_rood_vlakken', [])) // 2} "
        f"delta_rot_B={tuple(round(x, 4) for x in b.delta_rotation_euler) if b else None}")


def _mod():
    return next(m.module for m in bpy.context.preferences.addons if m.module.endswith("click_joints"))


def boog_verslag(naam, voorbij):
    """Na de schermafbeelding: wat de handler echt tekende (waaier.laatst), met eigen eisen. Regel "BOOG OK"
    is wat de workflow eist (Daan, beoordeling 3: getal gelijk aan het paneel, streepjes, rood voorbij)."""
    waaier = importlib.import_module(f"{_mod()}.waaier")
    paneel = importlib.import_module(f"{_mod()}.paneel")
    inst = bpy.context.scene.click_joints
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A" and "cj_buig_graden" in o), None)
    bogen = waaier.laatst.get("bogen", [])
    log(f"BOOG {naam}: {bogen}")
    if a is None or len(bogen) != 1:
        log(f"BOOG FOUT {naam}: {len(bogen)} bogen getekend")
        return
    n = paneel.richting_graden(a, int(inst.pose_richting))
    b = bogen[0]
    bends = paneel.buig_tekst(a)  # "Bends ±20°": bij de pop is het bereik rondom gelijk, dus hetzelfde getal
    eisen = {
        "tekenbeurt hoort bij deze pose": b["pose"] == round(float(inst.pose_graden), 3)
        and b["richting"] == int(inst.pose_richting),
        "getal gelijk aan paneel": b["getal"] == f"{n}\u00b0" and bends == f"Bends \u00b1{n}\u00b0",
        "getal getekend": b["getal_getekend"],
        "streepjes elke 5 graden": b["streepjes"] == n // 5 + 1,
        "gesloten lijn 48 punten": b["omtrek"] == 48,
        "voorbij klopt": b["voorbij"] == voorbij,
        "rode tekst alleen voorbij": (b["voorbij_tekst"] is not None) == voorbij,
    }
    mis = [k for k, ok in eisen.items() if not ok]
    log(f"BOOG {'OK' if not mis else 'FOUT'} {naam} getal={b['getal']} paneel={n} kijkhoek={b['kijkhoek']} mis={mis}")


def voorbij_grens():
    """Plaatje 6 (ronde l): zelfde beeld als de waaier, maar de pose 8 graden voorbij de gemeten grens,
    zodat de botsende vlakken van deel A rood worden (het eigen gezicht van de beweegproef)."""
    inst = bpy.context.scene.click_joints
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A" and "cj_buig_graden" in o), None)
    if a is None:
        log("ROOD: geen deel A met bereik")
        return
    paneel = importlib.import_module(f"{_mod()}.paneel")
    grens = paneel.richting_graden(a, int(inst.pose_richting))  # het getal op de boog, dan zeker "+8° past limit"
    inst.pose_graden = min(45.0, grens + 8.0)
    log(f"ROOD grens={grens} pose={inst.pose_graden} rood={len(a.get('cj_rood_vlakken', [])) // 2} vlakken")


def plat_lid():
    """Plaatje 7 (ronde l, eis b van Daan): plat, hoekig lid (16 x 12 mm; 12 x 8 is te dun voor een kogel, ronde hoeken) met een
    kogelgewricht in rechte stand, opengewerkt beeld uit, zodat je de naad over vlakke zijden en hoeken ziet."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    bpy.context.view_layer.update()
    figuren.mm_scene()
    lid = figuren.balk("plat_lid", 16.0, 12.0, lengte=40.0)
    lid.color = (0.8, 0.8, 0.8, 1.0)
    figuren.maak_actief(lid)
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    inst = bpy.context.scene.click_joints
    inst.pose_graden = 0.0
    inst.speling_mm, inst.as_bron, inst.kogel_auto = 0.2, "CURSOR", True
    inst.uit_elkaar = False
    inst.toon_bereik = False
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    delen = [o for o in bpy.context.scene.objects if o.get("cj_deel")]
    a = next((d for d in delen if d.get("cj_deel") == "A"), None)
    log(f"PLAT plaats: {uitslag}, {len(delen)} delen, kogel {inst.kogel_mm} mm, passing "
        f"{a.get('cj_passing') if a else None}, wand {a.get('cj_wand_mm') if a else None}, "
        f"bereik {list(a.get('cj_buig_graden', [])) if a else None}")
    weergave()
    venster, gebied, _ = zijbalk()
    if not gebied or a is None:
        return
    rv3d = gebied.spaces.active.region_3d
    richting = Vector((0.35, 0.75, -0.55)).normalized()  # schuin van boven op de brede zijde en de hoek
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = richting.to_track_quat("-Z", "Y")
    rv3d.view_distance = 30.0
    rechts = rv3d.view_rotation @ Vector((1.0, 0, 0))
    rv3d.view_location = Vector(a["cj_centrum"]) + rechts * 3.0
    gebied.tag_redraw()


def winkel(pose):
    """Winkelschermen 8 en 9 (lanceerlijst Daan, 8 nov 17:30): pop met kogel, gradenboog aan, Exploded view uit,
    de 3D-weergave over het hele venster (geen zijbalk, geen gereedschap), kijker loodrecht op het vlak van de
    boog in richting 90 (langs de draaias), het gewricht in het midden. Pose 15 (binnen) of 28 (voorbij)."""
    if pose < 20.0:
        maak_pop()
        plaats()
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = False
    inst.toon_bereik = True
    inst.pose_richting = "2"
    inst.pose_graden = float(pose)
    venster, gebied, _ = zijbalk()
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A" and "cj_buig_graden" in o), None)
    if not gebied or a is None:
        log("WINKEL: geen weergave of geen deel A met bereik")
        return
    if pose < 20.0:
        weergave()
        with bpy.context.temp_override(window=venster, area=gebied):
            bpy.ops.screen.screen_full_area(use_hide_panels=True)
        venster, gebied, _ = zijbalk()
        ruimte = gebied.spaces.active
        ruimte.show_region_ui = False
        ruimte.show_region_toolbar = False
        ruimte.show_region_header = False
        ruimte.overlay.show_text = False  # geen "User Perspective" linksboven op het winkelplaatje
        # Schoon winkelbeeld (kan-punt controleur ronde q): geen 3D-cursor, aslijnen of vloer.
        ruimte.overlay.show_cursor = False
        ruimte.overlay.show_axis_x = False
        ruimte.overlay.show_axis_y = False
        ruimte.overlay.show_floor = False
    as_ = Vector(a["cj_as"]).normalized()
    u = as_.orthogonal().normalized()
    rich = as_.cross(u).normalized()  # richting 2 = 90 graden (uit_elkaar.richtingen)
    kijk_r = as_.cross(rich).normalized()  # draaias van richting 2: loodrecht op het vlak van de boog
    rv3d = gebied.spaces.active.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = kijk_r.to_track_quat("-Z", "Y")
    rv3d.view_distance = 11.0 * a["cj_kogel_r"]
    rv3d.view_location = Vector(a["cj_centrum"])  # het gewricht in het midden (Daan, lanceerlijst punt 2)
    gebied.tag_redraw()
    log(f"WINKEL pose={inst.pose_graden} uit_elkaar={inst.uit_elkaar} gebied={gebied.width}x{gebied.height}")


def winkel_paneel():
    """Winkelscherm 10 (lanceerlijst Daan): zelfde beeld als 8-winkel (pose 15), met de zijbalk open op Click Joints.
    Deel A is actief maar niet geselecteerd, zodat het paneel Good fit, Bends en Bend toont zonder oranje rand."""
    inst = bpy.context.scene.click_joints
    inst.pose_graden = 15.0
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A" and "cj_buig_graden" in o), None)
    if a is not None:
        for o in bpy.context.selected_objects:
            o.select_set(False)
        bpy.context.view_layer.objects.active = a
    venster, gebied, _ = zijbalk()
    if gebied:
        gebied.spaces.active.show_region_ui = True
        gebied.tag_redraw()


def paneel_verslag():
    """Na schermafbeelding 10: staat het paneel echt open op Click Joints, met Good fit en Bends? Regel "PANEEL OK"
    is wat de workflow eist."""
    paneel = importlib.import_module(f"{_mod()}.paneel")
    _, gebied, regio = zijbalk()
    ob = bpy.context.active_object
    eisen = {
        "zijbalk open": bool(gebied and gebied.spaces.active.show_region_ui and regio and regio.width > 50),
        "tabblad Click Joints": bool(regio and regio.active_panel_category == "Click Joints"),
        "deel A actief": bool(ob and ob.get("cj_deel") == "A"),
        "Good fit": bool(ob and ob.get("cj_passing") == "groen"),
        "Bends in paneel": bool(ob and (paneel.buig_tekst(ob) or "").startswith("Bends")),
        "niets geselecteerd": not bpy.context.selected_objects,
        "pose 15": abs(bpy.context.scene.click_joints.pose_graden - 15.0) < 1e-6,
    }
    mis = [k for k, ok in eisen.items() if not ok]
    tekst = paneel.buig_tekst(ob) if ob else None
    log(f"PANEEL {'OK' if not mis else 'FOUT'} winkel tekst={tekst} breed={regio.width if regio else 0} mis={mis}")
