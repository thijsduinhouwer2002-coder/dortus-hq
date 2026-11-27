"""Fit test (passingproef), called from test_kern.py. Everything measured on the meshes and the files:
block watertight and on the bed, four holes with the engraved clearance and the right radius (rays), the pins
fit every hole, the chosen clearance is saved per printer and material in the add-on preferences and comes
back when you switch, export of block and pins, a scene in meters, and Split leaves the fit test alone."""
import json
import os

import bpy

import modellen
from hulp import SCHAAL, bestaat, dicht, gat_maten, label_punten, lees_3mf, lees_stl, log, maat, past, pennen, stap

BED = (176.0, 176.0, 178.0)
PAKKET = "bl_ext.user_default.click_cuts"


def proef():
    col = bpy.data.collections.get("Click Cuts fit test")
    objs = list(col.objects) if col else []
    blok = next((o for o in objs if o.get("sj_passing") == "blok"), None)
    pen = next((o for o in objs if o.get("sj_passing") == "pennen"), None)
    return blok, pen


def voorkeur():
    addon = bpy.context.preferences.addons.get(PAKKET)
    return json.loads(addon.preferences.spelingen_json) if addon and addon.preferences else None


def toets_blok(naam, speling, pen_d=5.0, pen_lengte=12.0):
    blok, pen = proef()
    if not stap(f"{naam}: blok en pennen gemaakt", blok is not None and pen is not None):
        return None, None
    ok, slecht, vol = dicht(blok)
    stap(f"{naam}: blok waterdicht", ok, f"slechte randen {slecht}, volume {vol:.0f} mm3")
    m = maat(blok)
    stap(f"{naam}: blok past op een A1 mini", past(m, BED), f"{[round(v, 1) for v in m]}")
    verwacht = [round(max(0.0, speling - 0.05) + k * 0.05, 3) for k in range(4)]
    stap(f"{naam}: vier spelingen rond de ingestelde", [round(s, 3) for s in blok["sj_spelingen"]] == verwacht,
         f"{list(blok['sj_spelingen'])} verwacht {verwacht}")
    gaten = json.loads(blok["sj_gaten"])
    stap(f"{naam}: vier gaten", len(gaten) == 4)
    straal_pen = max(r for r, _l in pennen(pen))
    for g in gaten:
        r, d = gat_maten(blok, g)
        doel = pen_d / 2.0 + g["speling"]
        if not stap(f"{naam} gat {g['speling']:.2f}: gevonden", r is not None):
            continue
        stap(f"{naam} gat {g['speling']:.2f}: straal klopt", doel - 0.005 <= r <= doel + 0.02,
             f"gemeten {r:.3f}, doel {doel:.3f}")
        stap(f"{naam} gat {g['speling']:.2f}: speling gemeten", abs((r - straal_pen) - g["speling"]) < 0.02,
             f"{r - straal_pen:.3f}")
        stap(f"{naam} gat {g['speling']:.2f}: diep genoeg voor een halve pen", d is not None and d >= pen_lengte / 2.0,
             f"diepte {d}")
        lb = {"tekst": f"{g['speling']:.2f}", "p": [g["p"][0], g["p"][1] - (pen_d / 2.0 + verwacht[-1] + 1.5 + 2.0),
                                                    g["p"][2]], "as": 2, "teken": 1, "h": 4.0}
        n = label_punten(blok, lb, 0.6)
        stap(f"{naam} gat {g['speling']:.2f}: speling gegraveerd", n >= 8, f"{n} punten op 0,6 mm diepte")
    lijst = pennen(pen)
    stap(f"{naam}: vier pennen van de eigen maat", len(lijst) == 4 and all(abs(r - pen_d / 2.0) < 0.01 and
                                                                              abs(lengte - pen_lengte) < 0.01
                                                                              for r, lengte in lijst),
         f"{[(round(r, 3), round(lengte, 2)) for r, lengte in lijst]}")
    return blok, pen


def alles(uitmap):
    for op in ("passing_maak", "passing_kies", "passing_export"):
        stap(f"operator split_joints.{op} bestaat", op in dir(bpy.ops.split_joints))
    stap("voorkeuren van de add-on bestaan", voorkeur() is not None)

    # 1. Next to a model in a mm scene, default pin
    modellen.mm_scene()
    ob = modellen.suzanne()
    inst = bpy.context.scene.split_joints
    inst.printer, inst.materiaal, inst.speling_mm = "A1MINI", "PLA", 0.2
    r = bpy.ops.split_joints.passing_maak()
    stap("passing: knop werkt", r == {"FINISHED"}, f"{r}")
    blok, pen = toets_blok("passing", 0.2)
    if blok is not None:
        model_y = max((ob.matrix_world @ v.co).y for v in ob.data.vertices)
        blok_y = min(v.co.y for v in blok.data.vertices)
        stap("passing: blok staat naast het model", blok_y > model_y, f"blok {blok_y:.1f}, model {model_y:.1f}")
        stap("passing: blok ligt op de vloer", abs(min(v.co.z for v in blok.data.vertices)) < 0.01)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uitmap, "passing.blend"))

    # 2. Export of the fit test, STL and 3MF, read back
    inst.exportmap = os.path.join(uitmap, "passing")
    for formaat in ("STL", "3MF"):
        inst.formaat = formaat
        r = bpy.ops.split_joints.passing_export()
        ext = formaat.lower()
        b = os.path.join(uitmap, "passing", f"fit_test_block.{ext}")
        p = os.path.join(uitmap, "passing", f"fit_test_pins.{ext}")
        stap(f"passing export {formaat}: twee bestanden", r == {"FINISHED"} and bestaat(b) and bestaat(p), f"{r}")
        if blok is not None and bestaat(b):
            m = lees_stl(b)[1] if formaat == "STL" else lees_3mf(b)["maat"]
            stap(f"passing export {formaat}: maat blok gelijk", all(abs(m[i] - maat(blok)[i]) < 0.01 for i in range(3)),
                 f"{[round(v, 2) for v in m]}")
    inst.formaat = "STL"

    # 3. Pick one: saved per printer and material, comes back when you switch
    r = bpy.ops.split_joints.passing_kies(waarde=0.25)
    stap("kies 0,25: speling ingesteld", abs(inst.speling_mm - 0.25) < 1e-6, f"{r} {inst.speling_mm}")
    vk = voorkeur() or {}
    stap("kies 0,25: bewaard in de voorkeuren", abs(vk.get("A1MINI|PLA", -1) - 0.25) < 1e-6, f"{vk}")
    inst.printer = "MK4"
    stap("andere printer zonder proef: speling blijft", abs(inst.speling_mm - 0.25) < 1e-6, f"{inst.speling_mm}")
    inst.speling_mm = 0.1
    inst.printer = "A1MINI"
    stap("terug naar A1 mini: 0,25 komt terug", abs(inst.speling_mm - 0.25) < 1e-6, f"{inst.speling_mm}")
    inst.materiaal = "PETG"
    bpy.ops.split_joints.passing_kies(waarde=0.3)
    inst.materiaal = "PLA"
    stap("PETG 0,30 en PLA 0,25 los bewaard", abs(inst.speling_mm - 0.25) < 1e-6 and
         abs((voorkeur() or {}).get("A1MINI|PETG", -1) - 0.3) < 1e-6, f"{inst.speling_mm} {voorkeur()}")
    modellen.mm_scene()  # emptied scene: the saved value comes back on choosing the printer
    inst = bpy.context.scene.split_joints
    inst.printer = "MK4"
    inst.speling_mm = 0.2
    inst.printer = "A1MINI"
    stap("lege scene: bewaarde speling komt terug", abs(inst.speling_mm - 0.25) < 1e-6, f"{inst.speling_mm}")
    # new file (keurder M2): the load handler gives every scene without a typed clearance the saved one
    laden = next((h for h in bpy.app.handlers.load_post if getattr(h, "__name__", "") == "sj_laden"), None)
    stap("handler bij openen bestaat", laden is not None)
    if laden is not None:
        sc = bpy.context.scene
        inst.speling_mm = 0.2
        del sc["sj_speling_eigen"]  # like a fresh file on A1 mini + PLA
        laden(None)
        stap("nieuw bestand: bewaarde 0,25 zonder printer te wisselen", abs(inst.speling_mm - 0.25) < 1e-6, f"{inst.speling_mm}")
        inst.speling_mm = 0.18  # typed by the user
        laden(None)
        stap("zelf getypte speling blijft bij openen", abs(inst.speling_mm - 0.18) < 1e-6, f"{inst.speling_mm}")
    # highest clearance (keurder M3): every button can be saved as shown
    inst.speling_mm = 1.0
    bpy.ops.split_joints.passing_maak()
    blok_, _p = proef()
    hoog = list(blok_["sj_spelingen"]) if blok_ else []
    stap("speling 1,0: knoppen niet boven 1,0", bool(hoog) and max(hoog) <= 1.0 + 1e-9, f"{hoog}")
    bpy.ops.split_joints.passing_kies(waarde=hoog[-1] if hoog else 1.0)
    stap("speling 1,0: bewaard wat de knop zegt", abs((voorkeur() or {}).get("A1MINI|PLA", -1) - (hoog[-1] if hoog else -9)) < 1e-6,
         f"{voorkeur()}")
    bpy.ops.split_joints.passing_kies(waarde=0.25)

    # 3b. Start clearance per material (#227): nothing saved for MK4, nothing typed
    modellen.mm_scene()
    sc = bpy.context.scene
    inst = sc.split_joints
    inst.printer, inst.materiaal = "MK4", "PLA"
    if "sj_speling_eigen" in sc:
        del sc["sj_speling_eigen"]
    inst.materiaal = "RESIN"
    stap("hars zonder proef: speling 0,10", abs(inst.speling_mm - 0.1) < 1e-6, f"{inst.speling_mm}")
    r = bpy.ops.split_joints.passing_maak()
    stap("hars: knop werkt", r == {"FINISHED"}, f"{r}")
    toets_blok("passing hars", 0.1)
    inst.materiaal = "TPU"
    stap("TPU zonder proef: speling 0,30", abs(inst.speling_mm - 0.3) < 1e-6, f"{inst.speling_mm}")
    inst.materiaal = "PLA"
    stap("PLA zonder proef: speling 0,20", abs(inst.speling_mm - 0.2) < 1e-6, f"{inst.speling_mm}")
    inst.printer = "A1MINI"
    stap("A1 mini PLA: bewaarde 0,25 gaat voor", abs(inst.speling_mm - 0.25) < 1e-6, f"{inst.speling_mm}")
    inst.materiaal = "RESIN"
    stap("A1 mini hars zonder proef: speling 0,10", abs(inst.speling_mm - 0.1) < 1e-6, f"{inst.speling_mm}")
    inst.materiaal = "PETG"
    stap("A1 mini PETG: bewaarde 0,30 gaat voor startwaarde 0,25", abs(inst.speling_mm - 0.3) < 1e-6, f"{inst.speling_mm}")
    inst.printer = "MK4"
    stap("andere printer zonder proef: speling blijft (geen startwaarde)", abs(inst.speling_mm - 0.3) < 1e-6,
         f"{inst.speling_mm}")
    inst.speling_mm = 0.18  # typed by the user
    inst.materiaal = "RESIN"
    stap("zelf getypte 0,18 blijft bij ander materiaal", abs(inst.speling_mm - 0.18) < 1e-6, f"{inst.speling_mm}")
    inst.materiaal = "PLA"
    stap("zelf getypte 0,18 blijft ook terug op PLA", abs(inst.speling_mm - 0.18) < 1e-6, f"{inst.speling_mm}")
    del sc["sj_speling_eigen"]
    inst.printer = "A1MINI"
    stap("na de toetsen: A1 mini PLA weer 0,25", abs(inst.speling_mm - 0.25) < 1e-6, f"{inst.speling_mm}")

    # 4. Split after a fit test: the fit test stays, the piece export does not take it
    ob = modellen.suzanne()
    inst.speling_mm = 0.2
    modellen.actief(ob)
    bpy.ops.split_joints.passing_maak()
    stap("na de proef: het model blijft actief (keuring M1)", bpy.context.view_layer.objects.active == ob,
         f"{bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else None}")
    bpy.ops.split_joints.plan()
    stap("na de proef: Plan cuts werkt op het model", bpy.context.scene.split_joints.bron == ob.name and
         dict(bpy.context.scene.get("sj_plan", {})).get("stukken", 0) > 1, bpy.context.scene.split_joints.bron)
    blok_, _p = proef()
    if blok_ is not None:
        modellen.actief(blok_)
        r = bpy.ops.split_joints.plan.poll()
        stap("proefblok actief: Plan cuts kiest het blok niet", bpy.context.scene.split_joints.bron == ob.name, f"poll {r}")
        modellen.actief(ob)
    bpy.ops.split_joints.split()
    blok, pen = proef()
    stap("na Split: proef staat er nog", blok is not None and pen is not None)
    inst.exportmap = os.path.join(uitmap, "passing_stukken")
    bpy.ops.split_joints.exporteer()
    namen = os.listdir(os.path.join(uitmap, "passing_stukken"))
    stap("export van de stukken neemt de proef niet mee", not any(n.startswith("fit_test") for n in namen), f"{sorted(namen)[:4]}")

    # 5. Other pin (3 mm, 8 mm long), clearance 0 (lowest value stays 0)
    modellen.mm_scene()
    inst = bpy.context.scene.split_joints
    inst.pen_mm, inst.pen_lengte_mm, inst.speling_mm = 3.0, 8.0, 0.0
    bpy.ops.split_joints.passing_maak()
    toets_blok("passing 3 mm", 0.0, pen_d=3.0, pen_lengte=8.0)

    # 6. Scene in meters (mm model in a meter scene): same block, measured in mm
    modellen.meter_scene()
    SCHAAL[0] = 1000.0
    try:
        inst = bpy.context.scene.split_joints
        inst.pen_mm, inst.pen_lengte_mm, inst.speling_mm = 5.0, 12.0, 0.2
        bpy.ops.split_joints.passing_maak()
        toets_blok("passing meters", 0.2)
    finally:
        SCHAAL[0] = 1.0
    log("passing: klaar")
