"""Magnet holes instead of pins (issue #117, lat: every competitor has magnet holes), called from test_kern.py.

Two models on an A1 mini (176 x 176 x 178 mm after the margin), Joint = Magnets:
- a bare box 300 x 60 x 60 mm (no voxel): 2 pieces, both watertight and green;
- a figure: torso 40 x 40 x 40 mm with an arm 12 x 12 mm, 250 mm long in total, made watertight: the cut goes
  through the arm.
Measured on the meshes, not read from the add-on: every hole is found with rays, radius = magnet/2 + clearance/2
(clearance on the diameter), depth = magnet thickness + 0.3 mm, each hole in exactly two pieces, no pin plates,
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
        stap(f"magneet {naam} stuk {ob['sj_stuk']}: diepte {diepte:.2f} mm (magneet {t:g} + 0.3)",
             diepte is not None and abs(diepte - (t + 0.3)) <= 0.03)
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


def vlak_tussen_gaten(ob):
    """Daan #150 M1: the cut face between and around two magnet holes on the same face must be flat, no groove.
    Rays from 1 mm outside the face straight in, on a fine grid over the stadium around each pair of holes
    (along the line between the centres and across it, holes and number labels left out). Returns per pair:
    (pieces, holes, rays that hit, rays deeper than 0.02 mm but under 1 mm, deepest of those, misses or deeper
    than 1 mm (off the face edge), largest tilt of the surface normal in degrees where it is flat)."""
    from hulp import boom, as_vec, SCHAAL, labels
    b = boom(ob)
    k = SCHAAL[0]
    gl = gaten(ob)
    lbs = labels(ob)
    uit = []
    for i in range(len(gl)):
        for j in range(i + 1, len(gl)):
            g, h = gl[i], gl[j]
            if g["as"] != h["as"] or g.get("teken") != h.get("teken"):
                continue
            n = as_vec(g["as"])
            richting = -n * g["teken"]  # into the piece
            pg, ph = Vector(g["p"]), Vector(h["p"])
            if abs((pg - ph).dot(n)) > 0.01 or (pg - ph).length > 150.0:
                continue
            lang = ph - pg
            lengte = lang.length
            e = lang / lengte
            dwars = n.cross(e)
            r = g["r_gat"]
            raak = ondiep = mis = rand = 0
            diepst, kantel = 0.0, 0.0
            plek = None
            stappen_l = max(2, int((lengte + 2 * (r + 0.8)) / 0.25))
            stappen_d = int(2 * (r + 0.8) / 0.05)
            for a in range(stappen_l + 1):
                s = -(r + 0.8) + a * (lengte + 2 * (r + 0.8)) / stappen_l
                for c in range(stappen_d + 1):
                    t = -(r + 0.8) + c * 0.05
                    q = pg + e * s + dwars * t
                    if (q - pg).length < r + 0.1 or (q - ph).length < r + 0.1:
                        continue
                    if any(lb.get("as") == g["as"] and (q - Vector(lb["p"])).length < lb.get("h", 5.0) * (len(lb.get("tekst", "")) * 0.7 + 1.5)
                           for lb in lbs):
                        continue
                    hit = b.ray_cast((q - richting * 1.0) / k, richting, 50.0 / k)
                    if hit[0] is None or hit[3] * k - 1.0 > 1.0:
                        mis += 1
                        continue
                    diep = hit[3] * k - 1.0
                    raak += 1
                    if diep > 0.02:
                        # a groove (like the line Daan saw, along the holes) has flat face on both sides of it within
                        # 1 mm; the edge of the face only on the inside: there the skin of the model starts and slopes
                        # away (counted as rand). Along the line is left out: a wavy outline of the face has flat on
                        # both ends of a dip in the skin (run 45776302877, face 7-8, normal 41.7 degrees there).
                        def vlak_op(v):
                            for stapje in range(1, 11):
                                w = q + v * (0.1 * stapje)
                                hh = b.ray_cast((w - richting * 1.0) / k, richting, 50.0 / k)
                                if hh[0] is not None and hh[3] * k - 1.0 <= 0.02:
                                    return True
                            return False
                        if vlak_op(dwars) and vlak_op(-dwars):
                            ondiep += 1
                            if diep > diepst:
                                diepst, plek = diep, (round(s, 2), round(t, 2))
                        else:
                            rand += 1
                    else:
                        kantel = max(kantel, math.degrees(hit[1].angle(-richting)))
            uit.append(((ob["sj_stuk"], i, j), raak, ondiep, diepst, plek, mis, kantel, lengte, r, rand))
    return uit


def proef_groef():
    """Shows that vlak_tussen_gaten sees a groove: a box with two holes noted on its top face, once flat and once
    with a 0.2 mm deep, 0.3 mm wide groove 4.0 to 4.3 mm beside the line between them (where Daan saw the line)."""
    import json
    uit = []
    for met_groef in (False, True):
        modellen.mm_scene()
        ob = modellen.doos(140.0, 40.0, 20.0, "Proef")
        if met_groef:
            mes = modellen.doos(80.0, 0.3, 1.2, "Mes")
            mes.location = (0.0, 4.15, 19.8)
            mod = ob.modifiers.new("groef", "BOOLEAN")
            mod.operation, mod.object, mod.solver = "DIFFERENCE", mes, "EXACT"
            dg = bpy.context.evaluated_depsgraph_get()
            me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
            ob.modifiers.clear()
            ob.data = me
            bpy.data.objects.remove(mes)
        ob["sj_stuk"] = 1
        ob["sj_gaten"] = json.dumps([{"p": [x, 0.0, 20.0], "as": 2, "teken": 1, "r_gat": 4.1} for x in (-50.0, 50.0)])
        m = vlak_tussen_gaten(ob)
        uit.append(m[0] if m else None)
    return uit


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

        # gallery moment (issue #144, Daan #120 K3): Suzanne split with 8x3 magnet holes, rendered by scherm_kern.py
        modellen.mm_scene()
        suz = modellen.suzanne()
        lijst = splits("suzanne", suz, "8x3")
        n_gaten = sum(len(gaten(o)) for o in lijst)
        stap("magneet suzanne: stukken met magneetgaten en geen penplaatjes",
             len(lijst) > 1 and n_gaten >= 2 and not pen_objecten(), f"{len(lijst)} stukken, {n_gaten} gaten")
        # Daan #150 M1: is the thin stadium line between two holes on face 5-7 a groove? Measured with rays.
        paren = 0
        for ob in lijst:
            for wie, raak, ondiep, diepst, plek, mis, kantel, lengte, r, rand in vlak_tussen_gaten(ob):
                paren += 1
                log(f"vlakmeting stuk {ob.get('sj_naam', ob.name)} gaten {wie[1]}-{wie[2]} ({lengte:.1f} mm uit elkaar, r {r:.2f}): "
                    f"{raak} raak, {ondiep} in een groef dieper dan 0.02 mm (diepst {diepst:.3f} mm op {plek}), {rand} aan de rand van het vlak, {mis} buiten het vlak, "
                    f"normaal hooguit {kantel:.2f} graden scheef")
                stap(f"magneet suzanne stuk {wie[0]} gaten {wie[1]}-{wie[2]}: vlak tussen de gaten, geen groef",
                     raak > 0 and ondiep == 0, f"{ondiep} punten dieper dan 0.02 mm, diepst {diepst:.3f} mm")
        stap("magneet suzanne: er zijn paren gaten op één vlak gemeten", paren > 0, f"{paren} paren")
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uitmap, "magneet.blend"))
        # the measurement itself: flat box gives 0, a 0.2 mm groove is found (otherwise the 0 above means nothing)
        vlak, groef = proef_groef()
        log(f"vlakmeting proef: zonder groef {vlak}, met groef {groef}")
        stap("vlakmeting proef: vlakke doos geeft geen groef", vlak is not None and vlak[1] > 0 and vlak[2] == 0, str(vlak))
        stap("vlakmeting proef: groef van 0.2 mm wordt gevonden", groef is not None and groef[2] > 0 and 0.15 <= groef[3] <= 0.25,
             str(groef))
    finally:
        inst.verbinder = "PIN"
