"""Extra cases from the keuring of 23 nov (M1, M2 and the small "kan" points), called from test_kern.py.
- doos: bare closed box 500 x 150 x 120 mm (8 vertices), no voxel: 3 pieces, pins, numbers, export.
- open: Suzanne as Blender makes her (not watertight), no voxel: Split refuses, no pieces.
- twee gekozen: two models selected: Plan cuts says the other one is not part of it.
- meter fout: the same box as an STL in mm lands in a scene in meters (500 m): Plan, Split and Make watertight
  refuse fast with a message; 300 cuts by hand: Split refuses on the cell limit and the panel check stays cheap;
  Convert to mm, then the normal split.
- meter echt: Suzanne of 0.33 m in a scene in meters: all checks of test_kern, measured in mm."""
import importlib
import time

import bpy

import modellen
from hulp import SCHAAL, log, stap, stukken


def _module(naam):
    basis = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_cuts"))
    return importlib.import_module(f"{basis}.{naam}")


def snede_objecten():
    col = bpy.data.collections.get("Click Cuts cut planes")
    return [o for o in col.objects if "sj_as" in o] if col else []


def doos(model):
    modellen.mm_scene()
    ob = modellen.doos(500.0, 150.0, 120.0)
    stap("doos: 8 hoekpunten, geen voxel", len(ob.data.vertices) == 8)
    lijst = model("doos", ob)
    stap("doos: 3 stukken", len(lijst) == 3, str(len(lijst)))


def open_model():
    modellen.mm_scene()
    ob = modellen.suzanne_open(300.0)
    modellen.actief(ob)
    bpy.ops.split_joints.plan()
    try:
        r = bpy.ops.split_joints.split()
    except RuntimeError as e:  # the operator reports an ERROR: in the background that is raised
        r = {"CANCELLED"}
        log(f"open: melding {str(e)[:160]!r}")
    stap("open model: Split weigert", r == {"CANCELLED"} and not stukken(), str(r))
    stap("open model: reden is niet waterdicht", str(bpy.context.scene.get("sj_geweigerd", "")).startswith("open:"),
         str(bpy.context.scene.get("sj_geweigerd")))


def twee_gekozen():
    modellen.mm_scene()
    a = modellen.doos(300.0, 100.0, 100.0, "Box A")
    b = modellen.doos(50.0, 50.0, 50.0, "Box B")
    b.location.x = 400.0
    modellen.actief(a)
    b.select_set(True)
    a.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.split_joints.plan()
    stap("twee gekozen: Plan meldt het andere object", bpy.context.scene.get("sj_andere_gekozen") == 1,
         str(bpy.context.scene.get("sj_andere_gekozen")))


def _probeer(op):
    try:
        return op()
    except RuntimeError as e:
        log(f"melding: {str(e)[:160]!r}")
        return {"CANCELLED"}


def meter_fout(model):
    modellen.meter_scene()
    ob = modellen.doos(500.0, 150.0, 120.0)  # an STL in mm read as meters: 500 m long
    modellen.actief(ob)
    schaal = _module("schaal")
    stap("meter fout: schaalwaarschuwing", schaal.buiten_bereik(ob, bpy.context.scene),
         f"{schaal.maat_mm(ob, bpy.context.scene):.0f} mm")
    t0 = time.time()
    r = _probeer(bpy.ops.split_joints.plan)
    stap("meter fout: Plan weigert snel", r == {"CANCELLED"} and not snede_objecten() and time.time() - t0 < 5.0,
         f"{r} in {time.time() - t0:.2f} s")
    r = _probeer(bpy.ops.split_joints.maak_gesloten)
    stap("meter fout: Make watertight weigert", r == {"CANCELLED"}, str(r))
    for _ in range(300):  # many cuts by hand, all through the middle
        bpy.ops.split_joints.snede_erbij(as_=0)
    modellen.actief(ob)
    snedes = _module("snedes")
    t0 = time.time()
    st = snedes.stand(bpy.context)
    st2 = snedes.stand(bpy.context)
    stap("meter fout: paneeltelling met 300 sneden snel en zonder cellen", st is not None and st[1] is None
         and st2 == st and time.time() - t0 < 1.0, f"{st} in {time.time() - t0:.3f} s")
    r = _probeer(bpy.ops.split_joints.split)
    stap("meter fout: Split weigert (schaal)", r == {"CANCELLED"} and not stukken(), str(r))
    r = bpy.ops.split_joints.zet_om_mm()
    us = bpy.context.scene.unit_settings
    stap("meter fout: Convert to mm", r == {"FINISHED"} and abs(us.scale_length - 0.001) < 1e-9, f"{r} {us.scale_length}")
    r = _probeer(bpy.ops.split_joints.split)
    stap("meter fout: Split weigert 301 cellen", r == {"CANCELLED"} and str(bpy.context.scene.get("sj_geweigerd", ""))
         .startswith("cellen:"), f"{r} {bpy.context.scene.get('sj_geweigerd')}")
    lijst = model("meter-omgezet", ob)  # plan again (removes the 300 cuts) and split normally
    stap("meter fout: na omzetten 3 stukken", len(lijst) == 3, str(len(lijst)))


def meter_echt(model):
    modellen.meter_scene()
    ob = modellen.suzanne(0.33)
    SCHAAL[0] = 1000.0
    try:
        lijst = model("meter-suzanne", ob)
        stap("meter echt: 8 stukken zoals in de mm-scene", len(lijst) == 8, str(len(lijst)))
    finally:
        SCHAAL[0] = 1.0


def alles(model, _uitmap):
    for naam, f in (("doos", lambda: doos(model)), ("open", open_model), ("twee gekozen", twee_gekozen),
                    ("meter fout", lambda: meter_fout(model)), ("meter echt", lambda: meter_echt(model))):
        try:
            f()
        except Exception as e:
            import traceback
            traceback.print_exc()
            stap(f"{naam}: geen fout", False, repr(e)[:200])
