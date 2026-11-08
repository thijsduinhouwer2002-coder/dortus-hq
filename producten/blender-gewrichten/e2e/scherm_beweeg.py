"""Plaatjes 5, 6 en 7 van de schermtest: waaier van het gemeten bereik, pose voorbij de grens (rood)
en het platte lid (eis b). Opgesplitst uit schermen.py (opruimen 8 nov)."""
import bpy
from mathutils import Vector

import figuren
from scherm_basis import log, maak_pop, plaats, weergave, zijbalk


def waaier():
    """Plaatje 5 (ronde k): pop met gewricht, de waaier van het gemeten bereik en een pose van 20 graden,
    van opzij op het buigvlak, zodat waaier en buigen groot in beeld zijn."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    maak_pop()
    plaats()
    inst = bpy.context.scene.click_joints
    inst.toon_bereik = True
    inst.pose_richting = "2"
    inst.pose_graden = 20.0
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


def voorbij_grens():
    """Plaatje 6 (ronde l): zelfde beeld als de waaier, maar de pose 8 graden voorbij de gemeten grens,
    zodat de botsende vlakken van deel A rood worden (het eigen gezicht van de beweegproef)."""
    inst = bpy.context.scene.click_joints
    a = next((o for o in bpy.context.scene.objects if o.get("cj_deel") == "A" and "cj_buig_graden" in o), None)
    if a is None:
        log("ROOD: geen deel A met bereik")
        return
    grens = a["cj_buig_graden"][int(inst.pose_richting)]
    inst.pose_graden = min(45.0, round(grens + 8.0))
    log(f"ROOD grens={grens} pose={inst.pose_graden} rood={len(a.get('cj_rood_vlakken', [])) // 2} vlakken")


def plat_lid():
    """Plaatje 7 (ronde l, eis b van Daan): plat, hoekig lid (16 x 12 mm; 12 x 8 is te dun voor een kogel, afgeschuinde hoeken) met een
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
