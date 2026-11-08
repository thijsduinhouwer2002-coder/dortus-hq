"""Ronde e (punten van Daan, 8 nov 05:28): automatische kogelmaat (punt 9) en geen selectie na Place joint.
Alle maten in mm."""
import bpy

import figuren
from hulp import delen, gesloten_delen, log, stap, toets_stl, weg


def alles(arm):
    inst = bpy.context.scene.click_joints
    # Zelf een diameter typen zet Auto uit.
    inst.kogel_auto = True
    inst.kogel_mm = 4.0
    stap("diameter typen zet Auto uit", not inst.kogel_auto)

    # Auto aan: de diameter volgt de dikte van de arm op de snede (arm 10 mm dik, golf +-3%).
    inst.kogel_auto = True
    inst.speling_mm, inst.soort, inst.as_bron = 0.2, "KOGEL", "CURSOR"
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    figuren.maak_actief(arm)
    uitslag = bpy.ops.click_joints.plaats()
    lijst = delen()
    d = inst.kogel_mm
    a = next((o for o in lijst if o.get("cj_deel") == "A"), None)
    breedte = a.get("cj_breedte_mm") if a else None
    passing = a.get("cj_passing") if a else None
    log(f"AUTO: uitslag={uitslag} breedte_op_snede={breedte}mm diameter={d}mm ({d / 10.0:.2f} x armdikte 10 mm) "
        f"passing={passing} wand={a.get('cj_wand_mm') if a else None}mm auto_na={inst.kogel_auto}")
    stap("auto: Auto blijft aan na Place joint", inst.kogel_auto)
    stap(f"auto: breedte gemeten 9,4 tot 10,4 mm ({breedte})", breedte is not None and 9.4 <= breedte <= 10.4)
    stap(f"auto: diameter 0,6 x breedte afgerond op 0,5 mm ({d})",
         breedte is not None and abs(d - round(0.6 * breedte * 2) / 2) < 1e-6)
    stap(f"auto: diameter 55 tot 65% van de armdikte ({d})", 5.5 <= d <= 6.5)
    stap(f"auto: kogel in de delen is {d} mm", a is not None and abs(2 * a["cj_kogel_r"] - d) < 1e-6)
    stap(f"auto: passing Good fit of Tight ({passing})", passing in ("groen", "oranje"))
    gesloten_delen("auto", lijst)

    # Geen selectie na Place joint (punt 2): geen oranje rand naast de passingkleur; export werkt toch.
    gekozen = [o.name for o in bpy.context.view_layer.objects if o.select_get()]
    actief = bpy.context.view_layer.objects.active
    log(f"SELECTIE na plaatsen: geselecteerd={gekozen} actief={actief.name if actief else None}")
    stap("na plaatsen: niets geselecteerd", not gekozen)
    stap("na plaatsen: deel A actief (paneel toont de passing)", actief is a)
    if len(lijst) == 2:
        toets_stl(lijst, "STL zonder selectie")
        gekozen = [o.name for o in bpy.context.view_layer.objects if o.select_get()]
        stap(f"na export: nog steeds niets geselecteerd ({gekozen})", not gekozen)
        inst.uit_elkaar = False
        bpy.context.view_layer.update()
        b = next(o for o in lijst if o["cj_deel"] == "B")
        stap("Exploded view uit zonder selectie: deel B op de echte plek", b.delta_location.length < 1e-9)
        inst.uit_elkaar = True
        bpy.context.view_layer.update()
        stap("Exploded view aan zonder selectie: deel B verschoven", b.delta_location.length > 0)
    weg(lijst)
    arm.hide_set(True)
