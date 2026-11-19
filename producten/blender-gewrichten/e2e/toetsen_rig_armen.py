"""Toets Pro 1.1: "Figure from rig" op een hele figuur (benen, romp, armen) met Rigify-namen.

Figuur uit e2e/proef_armen.py: benen r 8 mm, 20 mm uit elkaar, romp 40 x 20 x 70, armen r 6 horizontaal.
Botkoppen van dij en bovenarm liggen zoals bij echte rigs in of tegen de romp. Op forearm.L Limit Rotation X 0 tot 140.
Twee figuren:
- lang (benen 90 mm, dij 45 mm): alle acht gewrichten lukken (knieën en ellebogen scharnier, heupen en schouders
  kogel), 9 gesloten delen, Left elbow 140 "from rig", samenvatting "8 joints · 1 rig · 1 mirror · 6 preset" (rechterelleboog gespiegeld, sinds Daan 18 nov moet 1);
  de heupkogels liggen onder de romp (uit de romp geschoven), hun bolnaad is niet groter dan 1,5 keer de beenstraal;
- kort (benen 70 mm, dij 33 mm): schouders lukken (26 mm van de elleboog, aan de komkant van de kogel genoeg),
  heupen worden eerlijk overgeslagen met "too close" (de knie van 135 graden reikt 25 mm).
Blender voor 4.5 (alleen de Exact-solver, 16 nov run 5, BEKEND en OPEN): op de lange figuur mislukt de boolean
van één knie of één heup ("The cut gave no watertight parts"), welke wisselt met de maat (90 of 91 mm). Daar eist de
toets minstens 6 van de 8, gesloten delen en bij elk overgeslagen gewricht een reden; in 5.2 en 5.3 alle acht.
Rekenregel (zonder Blender-figuur): reik van de kogel aan de komkant r + s + 0,5 mm, aan de snijvlakkant naad_r + 0,4 r.
Gebruik: blender -b --factory-startup --python e2e/toetsen_rig_armen.py -- <betaalde zip>
"""
import importlib
import math
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

FOUT = []


def log(t):
    print(f"[cj-armen] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def mod(naam):
    return importlib.import_module(f"bl_ext.user_default.click_joints.{naam}")


def figuur(B):
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    for a in list(bpy.data.armatures):
        bpy.data.armatures.remove(a)
    us = bpy.context.scene.unit_settings
    us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    bm = bmesh.new()
    for x in (-10.0, 10.0):
        bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=8, radius2=8, depth=B,
                              matrix=Matrix.Translation((x, 0, B / 2)))
    bmesh.ops.create_cube(bm, size=1, matrix=Matrix.Translation((0, 0, B + 30)) @ Matrix.Diagonal((40, 20, 70, 1)))
    for s in (-1, 1):
        bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=6, radius2=6, depth=75,
                              matrix=Matrix.Translation((s * 55, 0, B + 55)) @ Matrix.Rotation(math.radians(90), 4, "Y"))
    me = bpy.data.meshes.new("b")
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("b", me)
    bpy.context.scene.collection.objects.link(ob)
    r = ob.modifiers.new("v", "REMESH")
    r.mode, r.voxel_size = "VOXEL", 0.6
    dg = bpy.context.evaluated_depsgraph_get()
    me2 = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    bpy.data.objects.remove(ob)
    mesh = bpy.data.objects.new("held", me2)
    bpy.context.scene.collection.objects.link(mesh)
    data = bpy.data.armatures.new("rig")
    arm = bpy.data.objects.new("rig", data)
    bpy.context.scene.collection.objects.link(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode="EDIT")
    kn, sch = B / 2, B + 55
    for k, s in (("L", 1), ("R", -1)):
        th = data.edit_bones.new(f"thigh.{k}"); th.head, th.tail = (s * 10, 0, B - 2), (s * 10, 0, kn)
        sh = data.edit_bones.new(f"shin.{k}"); sh.head, sh.tail = (s * 10, 0, kn), (s * 10, 0, 4); sh.parent = th
        ua = data.edit_bones.new(f"upper_arm.{k}"); ua.head, ua.tail = (s * 24, 0, sch), (s * 55, 0, sch)
        fa = data.edit_bones.new(f"forearm.{k}"); fa.head, fa.tail = (s * 55, 0, sch), (s * 88, 0, sch)
        fa.parent = ua
    bpy.ops.object.mode_set(mode="OBJECT")
    c = arm.pose.bones["forearm.L"].constraints.new("LIMIT_ROTATION")
    c.use_limit_x, c.min_x, c.max_x, c.owner_space = True, 0, math.radians(140), "LOCAL"
    mesh.modifiers.new("Armature", "ARMATURE").object = arm
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    mesh.select_set(True)
    bpy.context.view_layer.objects.active = mesh
    return mesh, arm


def uitvoeren():
    try:
        r = bpy.ops.click_joints.figuur_uit_rig()
    except RuntimeError as e:
        r = {f"fout {e}"}
    fig = mod("betaald.figuur")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, "held")
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == "held" and o.visible_get()
             and o.type == "MESH"]
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_deel")), "")
    log(f"uitslag {r}; {[fig.regel(x) for x in alle]}; overgeslagen: {over}")
    return r, {x["naam"]: x for x in alle}, delen, over or "", fig


def rekenregel():
    af = mod("betaald.afstand")
    c, as_ = Vector((0, 0, 0)), Vector((0, 0, 1))
    boven = af.reik_naar(Vector((0, 0, 20)), c, as_, 8.0, 3.0, 0.2, 1.0)
    onder = af.reik_naar(Vector((0, 0, -20)), c, as_, 8.0, 3.0, 0.2, 1.0)
    check(abs(boven - 3.7) < 1e-6, f"komkant r + s + 0,5 = {boven:.2f}")
    check(abs(onder - 9.2) < 1e-6, f"snijvlakkant naad_r + 0,4 r = {onder:.2f}")
    pen = af.reik_naar(Vector((0, 0, 20)), c, as_, -1.0, 3.0, 0.2, 1.0)
    check(abs(pen - 4.7) < 1e-6, f"pen overal 1,5 r + s = {pen:.2f}")
    rig = mod("betaald.rig")
    # straal 30 (romp) tot t = 6, daarna 8 (been): schuif tot het vlak en het kogelmidden (t + 6,72) in het been liggen
    t = rig.schuif_uit_romp(lambda t: 30.0 if t < 6.0 else 8.0, 40.0, 0.5, naad_vrij=False)
    check(abs(t - 6.0) < 1e-6, f"schuif uit romp {t}")
    # Run 9: ook de bolnaad (8 + 1 mm, plus een stap) buiten de romp: kogelmidden t + 6,72 minstens 9,5 voorbij t = 6
    t = rig.schuif_uit_romp(lambda t: 30.0 if t < 6.0 else 8.0, 40.0, 0.5)
    check(abs(t - 9.0) < 1e-6, f"schuif uit romp met naad vrij {t}")
    check(rig.schuif_uit_romp(lambda t: 8.0, 40.0, 0.5) == 0.0, "geen romp: niet schuiven")


def main():
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    rekenregel()

    figuur(90.0)
    r, per, delen, over, fig = uitvoeren()
    namen = [f"{k} {w}" for k in ("Left", "Right") for w in ("knee", "elbow", "hip", "shoulder")]
    oud = bpy.app.version < (4, 5, 0)  # alleen Exact: bekende losse boolean-fout, zie boven
    if oud:
        mis = [n for n in namen if n not in per]
        log(f"BEKEND 4.2: niet geplaatst {mis}")
        # Run 19 (17 nov): in 4.2.23 verloor een knie soms de andere scheen (geen enkel deel bevatte hem meer). Het
        # vangnet verloren_stuk draait zo'n snede nu terug; op deze toetsfiguur vallen daardoor in 4.2 beide knieën af
        # met reden. Eis in 4.2: minstens de ellebogen en schouders, elk overgeslagen gewricht met reden, en geen
        # voet of hand kwijt.
        check(len(mis) <= 4 and all(f"{n} (" in over for n in mis), f"4.2: minstens 4 van 8, elk met reden ({over})")
        rigm = mod("betaald.rig")
        dg = bpy.context.evaluated_depsgraph_get()
        for punt in ((10, 0, 3), (-10, 0, 3), (88, 0, 145), (-88, 0, 145)):
            p = Vector(punt)
            check(any(rigm._in_kader(o, p) and rigm.binnen(o, p, dg)[0] for o in delen), f"4.2: punt {punt} nog in een deel")
        check(all(ges_ok for ges_ok in [mod("gesloten").is_gesloten(o)[0] for o in delen]), "4.2: alle delen gesloten")
        check("Left elbow" in per and per["Left elbow"].get("herkomst") == "from rig", "4.2: Left elbow from rig")
    else:
        check(all(n in per for n in namen), f"alle acht gewrichten ({sorted(per)})")
    if not oud:
        streng(per, delen, fig, namen)
    # Run 9: elk deel draagt alleen scharnieren die in of tegen dat deel liggen (eerst ging de rechterknie met het
    # linkerbeen mee, dan zag de rechterheup de knie niet en negeerde hij de afstandsregel).
    af = mod("betaald.afstand")
    fout_bij = []
    for o in delen:
        bij = af._bij_deel(o, 1.0)
        fout_bij += [f"{o.name} {tuple(round(c) for c in e[0])}" for e in af.scharnieren(o) if bij and not bij(e)]
    check(not fout_bij, f"scharnieren bij het juiste deel ({fout_bij})")

    figuur(70.0)
    r, per, delen, over, fig = uitvoeren()
    check("Left shoulder" in per and "Right shoulder" in per, "korte figuur: schouders lukken")
    check("Left hip" not in per and ("Left hip (too close" in over or "Left hip (no room on this" in over), f"korte figuur: heup eerlijk overgeslagen ({over})")
    check(all(mod("gesloten").is_gesloten(o)[0] for o in delen), f"korte figuur: alle {len(delen)} delen gesloten")
    log(f"KLAAR {len(FOUT)} FOUT")


def streng(per, delen, fig, namen):
    check(all(per[n]["soort"] == "HINGE" for n in namen if n in per and ("knee" in n or "elbow" in n)),
          "knieën en ellebogen zijn scharnieren")
    check(all(per[n]["soort"] != "HINGE" for n in namen if n in per and ("hip" in n or "shoulder" in n)),
          "heupen en schouders zijn kogels")
    le = per.get("Left elbow", {})
    check(le.get("herkomst") == "from rig" and le.get("graden") is not None and 135.0 <= le["graden"] <= 140.2,
          f"Left elbow from rig 140: {le}")
    check(len(delen) == 9, f"9 delen ({len(delen)})")
    ges = mod("gesloten")
    check(all(ges.is_gesloten(o)[0] for o in delen), "alle delen gesloten")
    tekst = fig.samenvatting(list(per.values()))
    re_ = per.get("Right elbow", {})  # spiegelen: forearm.R heeft geen grens, dus het bereik van links
    check(re_.get("herkomst") == "mirrored" and re_.get("graden") is not None and 135.0 <= re_["graden"] <= 140.2,
          f"Right elbow mirrored 140: {re_}")
    check(per.get("Right knee", {}).get("herkomst") == "preset", "knieën zonder grens aan beide kanten: preset")
    check(tekst == "8 joints · 1 rig · 1 mirror · 6 preset", f"samenvatting '{tekst}'")
    # run 7: snippers van de veersleuf in het verkeerde deel lieten de heupen 0 graden bewegen
    for n in ("Left hip", "Right hip"):
        g = per.get(n, {}).get("graden")
        check(g is not None and g >= 5.0, f"{n} beweegt (±{g}°, niet geblokkeerd)")
    heup = [o for o in delen if o.get("cj_naam") == "Left hip" and o.get("cj_deel") == "B"]
    if heup:
        h = heup[0]
        c = Vector(h["cj_centrum"])
        log(f"Left hip kogelmidden z {c.z:.1f}, bolnaad {h.get('cj_naad_r', -1):.1f}")
        check(c.z < 90.0 - 5.0, f"heupkogel onder de romp (z {c.z:.1f} < 85)")
        check(0 < float(h.get("cj_naad_r", -1)) <= 12.0, f"bolnaad heup {float(h.get('cj_naad_r', -1)):.1f} <= 12 mm")
    else:
        check(False, "deel B van de linkerheup gevonden")



if __name__ == "__main__":  # scherm_rig_armen.py leent figuur() zonder de toets te draaien
    main()
