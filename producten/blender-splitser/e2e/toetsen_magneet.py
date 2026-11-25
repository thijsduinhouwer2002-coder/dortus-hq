"""Magnet holes instead of pins (issue #117, lat: every competitor has magnet holes), called from test_kern.py.

Two models on an A1 mini (176 x 176 x 178 mm after the margin), Joint = Magnets:
- a bare box 300 x 60 x 60 mm (no voxel): 2 pieces, both watertight and green;
- a figure: torso 40 x 40 x 40 mm with an arm 12 x 12 mm, 250 mm long in total, made watertight: the cut goes
  through the arm.
Measured on the meshes, not read from the add-on: every hole is found with rays, radius = magnet/2 + clearance/2
(clearance on the diameter), depth = magnet thickness + 0.1 mm, each hole in exactly two pieces, no pin plates,
the panel count equals the holes, export writes the pieces and no pin files. Then 10x3 on the 12 mm arm: no hole
(the wall would be under 1.2 mm) and the message says why."""
import math
import os

import bmesh
import bpy
from mathutils import Vector

import modellen
from hulp import dicht, gat_maten, gaten, log, maat, past, pen_objecten, stap, stukken

BED = (176.0, 176.0, 178.0)
SPELING = 0.2
MAGNETEN = {"5x2": (5.0, 2.0), "6x2": (6.0, 2.0), "6x3": (6.0, 3.0), "8x3": (8.0, 3.0), "10x3": (10.0, 3.0)}


def figuur():
    bm = bmesh.new()
    for mn, mx in (((-20, -20, 0), (20, 20, 40)), ((15, -6, 24), (230, 6, 36))):
        t = bmesh.new()
        bmesh.ops.create_cube(t, size=1.0)
        for v in t.verts:
            v.co = Vector((mx[i] if v.co[i] > 0 else mn[i]) for i in range(3))
        me = bpy.data.meshes.new("t")
        t.to_mesh(me)
        t.free()
        bm.from_mesh(me)
        bpy.data.meshes.remove(me)
    ob = modellen._object("Figure", bm)
    return modellen.waterdicht(ob, 0.5)


def splits(naam, ob, magneet):
    inst = bpy.context.scene.split_joints
    inst.printer = "A1MINI"
    inst.speling_mm = SPELING
    inst.verbinder = "MAGNET"
    inst.magneet = magneet
    modellen.actief(ob)
    bpy.ops.split_joints.plan()
    r = bpy.ops.split_joints.split()
    log(f"magneet {naam} {magneet}: split {r}, meldingen {inst.meldingen!r}")
    return stukken()


def toets(naam, magneet, uitmap):
    d, t = MAGNETEN[magneet]
    lijst = stukken()
    stap(f"magneet {naam}: 2 stukken", len(lijst) == 2, f"{len(lijst)}")
    for ob in lijst:
        ok, slecht, vol = dicht(ob)
        stap(f"magneet {naam} stuk {ob['sj_stuk']}: waterdicht", ok, f"slechte randen {slecht}")
        stap(f"magneet {naam} stuk {ob['sj_stuk']}: past en groen", past(maat(ob), BED) and ob.get("sj_status") == "groen",
             f"{ob.get('sj_status')}, wand {ob.get('sj_wand_mm')}")
    stap(f"magneet {naam}: geen penplaatjes", not pen_objecten(), str([o.name for o in pen_objecten()]))
    alle = [(ob, g) for ob in lijst for g in gaten(ob)]
    stap(f"magneet {naam}: er zijn magneetgaten", len(alle) >= 2, f"{len(alle)} gaten")
    plekken = {}
    for ob, g in alle:
        stap(f"magneet {naam}: gat is een magneetgat van {magneet}", g.get("soort") == "magneet" and g.get("magneet") == magneet,
             f"{g.get('soort')} {g.get('magneet')}")
        straal, diepte = gat_maten(ob, g)
        if not stap(f"magneet {naam} stuk {ob['sj_stuk']}: gat gevonden", straal is not None):
            continue
        speling_d = 2.0 * (straal - d / 2.0)  # gap on the diameter
        stap(f"magneet {naam} stuk {ob['sj_stuk']}: speling op de diameter {speling_d:.3f} mm",
             SPELING - 0.01 <= speling_d <= SPELING + 0.04, f"gat r {straal:.3f}, magneet {d:g} mm")
        stap(f"magneet {naam} stuk {ob['sj_stuk']}: diepte {diepte:.2f} mm (magneet {t:g} + 0.1)",
             diepte is not None and abs(diepte - (t + 0.1)) <= 0.03)
        plekken.setdefault(tuple(round(c, 3) for c in g["p"]), []).append(ob["sj_stuk"])
    for p, wie in plekken.items():
        stap(f"magneet {naam}: gat {p} in twee verschillende stukken", len(wie) == 2 and wie[0] != wie[1], str(wie))
    import importlib
    eig = importlib.import_module("bl_ext.user_default.click_cuts.eigenschappen")
    klik = importlib.import_module("bl_ext.user_default.click_cuts.in_een_klik")
    tel = eig.magneten(bpy.context.scene)
    stap(f"magneet {naam}: paneeltelling gelijk aan de gaten", tel == {magneet: len(alle)}, str(tel))
    regel = klik.uitslag_tekst(bpy.context.scene)
    stap(f"magneet {naam}: uitslagregel noemt de magneten", regel is not None and f"{len(alle)} magnets {magneet} mm" in regel[1],
         str(regel))
    inst = bpy.context.scene.split_joints
    inst.formaat = "STL"
    inst.exportmap = os.path.join(uitmap, f"magneet_{naam}") + os.sep
    r = bpy.ops.split_joints.exporteer()
    bestanden = sorted(os.listdir(inst.exportmap)) if os.path.isdir(inst.exportmap) else []
    stap(f"magneet {naam}: export alleen de stukken, geen pennen",
         r == {"FINISHED"} and len([b for b in bestanden if b.startswith("piece_")]) == len(lijst)
         and not any(b.startswith("pins_") for b in bestanden), str(bestanden))


def alles(uitmap):
    inst = bpy.context.scene.split_joints
    try:
        modellen.mm_scene()
        doos = modellen.doos(300.0, 60.0, 60.0)
        splits("doos", doos, "6x2")
        toets("doos", "6x2", uitmap)

        modellen.mm_scene()
        arm = figuur()
        lijst = splits("arm", arm, "6x2")
        if lijst:
            toets("arm", "6x2", uitmap)
            snede_x = [g["p"][0] for g in gaten(lijst[0])]
            stap("magneet arm: het gat zit in de arm", any(40.0 < x < 220.0 for x in snede_x), str(snede_x))

        # a 10x3 magnet needs 10.1 mm + 2 x 1.2 mm wall = 12.6 mm: the 12 mm arm is too thin, refused with a message
        modellen.mm_scene()
        arm = figuur()
        lijst = splits("arm-dun", arm, "10x3")
        m = inst.meldingen
        stap("magneet arm 10x3: geen gaten in de te dunne arm", sum(len(gaten(o)) for o in lijst) == 0,
             str([len(gaten(o)) for o in lijst]))
        stap("magneet arm 10x3: melding zegt waarom", "magnet" in m and "Glue this joint" in m, repr(m[:300]))
        stap("magneet arm 10x3: stukken passen en zijn dicht", len(lijst) == 2 and all(past(maat(o), BED) and dicht(o)[0] for o in lijst))
        log(f"magneet: wand {math.inf if not lijst else lijst[0].get('sj_wand_mm')}")
    finally:
        inst.verbinder = "PIN"
