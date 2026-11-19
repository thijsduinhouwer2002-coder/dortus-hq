"""Toets Pro: Fit test strip (ontwerp `platformen/blender-2/testkaart-ontwerp.md`).

Knop click_joints.testkaart (soort KOGEL of SCHARNIER) maakt in een nieuwe collectie "Fit test" vijf staafjes,
elk met één gewricht bij 0.10 / 0.15 / 0.20 / 0.25 / 0.30 mm speling en het getal in reliëf op het bovenste deel.
Eisen:
1. precies 10 delen met cj_deel, allemaal in een collectie die met "Fit test" begint;
2. per speling precies twee delen met die cj_speling_mm, en het getal (cj_kaart_getal) klopt met de speling;
3. alle tien delen gesloten;
4. scene.click_joints.speling_mm, de cursor en een eigen object van de koper blijven zoals ze waren;
5. Export daarna geeft 10 bestanden;
6. een tweede klik maakt een nieuwe set die de eerste niet raakt (20 delen, geen overlap);
7. in een scene in meters zijn de staafjes even groot in mm als in een mm-scene.
Gebruik: blender -b --factory-startup --python e2e/toetsen_testkaart.py -- <betaalde zip>
"""
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

FOUT = []
SPELINGEN = (0.10, 0.15, 0.20, 0.25, 0.30)


def log(t):
    print(f"[cj-kaart] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return fout == 0


def leeg():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)


def delen():
    return [o for o in bpy.context.scene.objects if o.get("cj_deel")]


def in_kaart(ob):
    return any(c.name.startswith("Fit test") for c in ob.users_collection)


def doos(obs):
    if not obs:
        return Vector((0, 0, 0)), Vector((0, 0, 0))
    pts = [o.matrix_world @ Vector(h) for o in obs for h in o.bound_box]
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    return lo, hi


def raken(a, b):
    (alo, ahi), (blo, bhi) = a, b
    return all(alo[i] < bhi[i] and blo[i] < ahi[i] for i in range(3))


def klik(soort):
    try:
        return bpy.ops.click_joints.testkaart(soort=soort)
    except (RuntimeError, AttributeError, TypeError) as e:
        return f"fout {e}"


def proef(soort):
    leeg()
    figuren.mm_scene()
    scene = bpy.context.scene
    inst = scene.click_joints
    inst.speling_mm, inst.uit_elkaar = 0.17, False
    eigen = figuren.staaf("mijn_model", 5.0)
    eigen_verts = len(eigen.data.vertices)
    m = Matrix.Translation((3.0, -2.0, 1.0))
    scene.cursor.matrix = m
    r = klik(soort)
    check(r == {"FINISHED"}, f"{soort}: knop geeft FINISHED ({r})")
    lijst = delen()
    check(len(lijst) == 10, f"{soort}: 10 delen ({len(lijst)})")
    check(all(in_kaart(o) for o in lijst), f"{soort}: alle delen in collectie Fit test")
    for s in SPELINGEN:
        paar = [o for o in lijst if abs(float(o.get("cj_speling_mm", -1)) - s) < 1e-6]
        check(len(paar) == 2, f"{soort}: speling {s:.2f} op twee delen ({len(paar)})")
        getal = [o.get("cj_kaart_getal") for o in paar if o.get("cj_kaart_getal")]
        check(getal == [f"{s:.2f}"], f"{soort}: getal {s:.2f} op één deel ({getal})")
    open_ = [o.name for o in lijst if not gesloten(o)]
    check(not open_, f"{soort}: alle delen gesloten (open: {open_})")
    check(abs(inst.speling_mm - 0.17) < 1e-6, f"{soort}: speling scene blijft 0.17 ({inst.speling_mm:.3f})")
    check((scene.cursor.matrix.translation - m.translation).length < 1e-6, f"{soort}: cursor blijft staan")
    check(eigen.name in scene.objects and len(eigen.data.vertices) == eigen_verts and not eigen.get("cj_deel")
          and not in_kaart(eigen), f"{soort}: eigen model niet aangeraakt")
    # 5: export
    inst.formaat = "STL"
    inst.exportmap = os.path.join(bpy.app.tempdir or "/tmp", f"cj_kaart_{soort}") + os.sep
    r = bpy.ops.click_joints.exporteer()
    bestanden = list(scene.get("cj_laatste_export", []))
    check(r == {"FINISHED"} and len(bestanden) == 10 and all(os.path.getsize(f) > 0 for f in bestanden),
          f"{soort}: export geeft 10 bestanden ({len(bestanden)})")
    # 6: tweede klik
    eerste = doos(lijst)
    r = klik(soort)
    nieuw = [o for o in delen() if o not in lijst]
    check(r == {"FINISHED"} and len(nieuw) == 10, f"{soort}: tweede klik 10 nieuwe delen ({len(nieuw)})")
    if nieuw:
        check(not raken(eerste, doos(nieuw)), f"{soort}: tweede set raakt de eerste niet")
    lo, hi = eerste
    return (hi - lo) / figuren_u()


def figuren_u():
    import importlib
    eig = importlib.import_module("bl_ext.user_default.click_joints.eigenschappen")
    return eig.eenheid_per_mm(bpy.context.scene)


def meters(soort, maat_mm):
    leeg()
    figuren.meter_scene()
    bpy.context.scene.cursor.location = (3.0, -2.0, 1.0)  # 3 m van de oorsprong: daar ging het getal eerst mis
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.uit_elkaar = 0.2, False
    r = klik(soort)
    lijst = delen()
    if r != {"FINISHED"} or len(lijst) != 10:
        check(False, f"{soort} meters: 10 delen ({r}, {len(lijst)})")
        return
    lo, hi = doos(lijst)
    maat = (hi - lo) / figuren_u()
    check(all(abs(maat[i] - maat_mm[i]) < 0.05 for i in range(3)),
          f"{soort} meters: zelfde maat in mm ({tuple(round(x, 2) for x in maat)} tegen "
          f"{tuple(round(x, 2) for x in maat_mm)})")
    check(all(gesloten(o) for o in lijst), f"{soort} meters: alle delen gesloten")
    getallen = sorted(o.get("cj_kaart_getal") for o in lijst if o.get("cj_kaart_getal"))
    check(getallen == [f"{s:.2f}" for s in SPELINGEN], f"{soort} meters: vijf getallen ({getallen})")


def main():
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    log(f"Blender {bpy.app.version_string}")
    for soort in ("KOGEL", "SCHARNIER"):
        maat = proef(soort)
        log(f"{soort}: maat set {tuple(round(x, 2) for x in maat)} mm")
        meters(soort, maat)
    log(f"KLAAR {len(FOUT)} FOUT")


main()
