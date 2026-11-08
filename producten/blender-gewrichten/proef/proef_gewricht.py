"""Bouwproef: één kogelgewricht op een ledemaat van ±260K driehoeken.

Draait in de echte Blender zonder scherm:
  blender -b --factory-startup --python proef_gewricht.py
Meet: gesloten delen (manifold), speling tussen kogel en kom, tijd per solver.
Eenheid: 1 Blender-eenheid = 1 mm (alleen voor deze proef).
"""
import math
import sys
import time

import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

SPELING = 0.2  # mm
KOGEL_R = 2.5
KOGEL_C = Vector((3.0, 0.0, 0.0))
NEK_R = 1.2
SEGMENTEN = 64


def leeg():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def bol(naam, r, c, seg=SEGMENTEN):
    me = bpy.data.meshes.new(naam)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=r)
    bmesh.ops.translate(bm, verts=bm.verts, vec=c)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def cilinder_x(naam, r, x0, x1, seg=SEGMENTEN):
    me = bpy.data.meshes.new(naam)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=seg, radius1=r, radius2=r, depth=x1 - x0)
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=__import__("mathutils").Matrix.Rotation(math.pi / 2, 3, "Y"))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(((x0 + x1) / 2, 0, 0)))
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def blok(naam, xmin, xmax):
    me = bpy.data.meshes.new(naam)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x = xmin if v.co.x < 0 else xmax
        v.co.y *= 100
        v.co.z *= 100
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def ledemaat():
    """Ellipsoïde arm 40 x 10 x 10 mm met lichte 'sculpt'-golven, ±260K driehoeken."""
    me = bpy.data.meshes.new("arm")
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=512, v_segments=256, radius=1.0)
    for v in bm.verts:
        x, y, z = v.co
        golf = 1.0 + 0.03 * math.sin(9 * x) * math.cos(7 * math.atan2(z, y))
        v.co = Vector((x * 20.0, y * 5.0 * golf, z * 5.0 * golf))
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("arm", me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def boolean(doel, gereedschap, actie, solver):
    m = doel.modifiers.new(f"{actie}_{gereedschap.name}", "BOOLEAN")
    m.operation = actie
    m.object = gereedschap
    m.solver = solver
    if solver == "EXACT":
        m.use_self = False
        m.use_hole_tolerant = False
    gereedschap.hide_set(True)


def bak(ob, naam):
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    uit = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(uit)
    return uit


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    rand = sum(1 for e in bm.edges if e.is_boundary)
    niet = sum(1 for e in bm.edges if not e.is_manifold)
    vol = bm.calc_volume(signed=True)
    tris = sum(len(f.verts) - 2 for f in bm.faces)
    bm.free()
    return rand == 0 and niet == 0 and vol > 0, rand, niet, vol, tris


def meet_speling(deel_a, deel_b):
    """Punten op de kogel van deel A, afstand tot het dichtstbijzijnde vlak van deel B."""
    dg = bpy.context.evaluated_depsgraph_get()
    bvh = BVHTree.FromObject(deel_b, dg)
    afst = []
    for v in deel_a.data.vertices:
        p = v.co
        if abs((p - KOGEL_C).length - KOGEL_R) < 1e-3 and p.x > KOGEL_C.x - 1.0:
            hit = bvh.find_nearest(p)
            if hit[0] is not None:
                afst.append(hit[3])
    if not afst:
        return 0, None, None
    gem = sum(afst) / len(afst)
    return len(afst), gem, max(abs(a - SPELING) for a in afst)


def proef(solver):
    leeg()
    arm = ledemaat()
    links = blok("links", -100, 0)
    rechts = blok("rechts", 0, 100)
    kogel = bol("kogel", KOGEL_R, KOGEL_C)
    nek = cilinder_x("nek", NEK_R, -1.0, KOGEL_C.x)
    kom = bol("kom", KOGEL_R + SPELING, KOGEL_C)
    nekgat = cilinder_x("nekgat", NEK_R + SPELING, -1.0, KOGEL_C.x)

    t0 = time.perf_counter()
    a = bak(arm, "arm_a_bron")
    boolean(a, rechts, "DIFFERENCE", solver)
    boolean(a, kogel, "UNION", solver)
    boolean(a, nek, "UNION", solver)
    deel_a = bak(a, "deel_a")
    b = bak(arm, "arm_b_bron")
    boolean(b, links, "DIFFERENCE", solver)
    boolean(b, kom, "DIFFERENCE", solver)
    boolean(b, nekgat, "DIFFERENCE", solver)
    deel_b = bak(b, "deel_b")
    duur = time.perf_counter() - t0

    _, _, _, _, tris_bron = gesloten(arm)
    ok_a, ra, na, va, ta = gesloten(deel_a)
    ok_b, rb, nb, vb, tb = gesloten(deel_b)
    n, gem, maxaf = meet_speling(deel_a, deel_b)
    print(f"PROEF solver={solver} bron_driehoeken={tris_bron} duur={duur:.2f}s")
    print(f"PROEF deel_a gesloten={ok_a} randen_buiten={ra} niet_manifold={na} volume={va:.1f}mm3 driehoeken={ta}")
    print(f"PROEF deel_b gesloten={ok_b} randen_buiten={rb} niet_manifold={nb} volume={vb:.1f}mm3 driehoeken={tb}")
    if gem is None:
        print("PROEF speling: geen kogelpunten gevonden")
    else:
        print(f"PROEF speling ingesteld={SPELING} gemeten_gem={gem:.4f} max_afwijking={maxaf:.4f} punten={n}")
    return ok_a and ok_b and gem is not None and abs(gem - SPELING) < 0.02


def main():
    print("PROEF blender", bpy.app.version_string)
    solvers = [s.identifier for s in bpy.types.BooleanModifier.bl_rna.properties["solver"].enum_items]
    print("PROEF solvers", solvers)
    goed = True
    for s in ("MANIFOLD", "EXACT"):
        if s in solvers:
            try:
                goed = proef(s) and goed
            except Exception as e:  # noqa: BLE001
                print(f"PROEF solver={s} FOUT {e!r}")
                goed = False
    print("PROEF UITSLAG", "GROEN" if goed else "ROOD")
    sys.exit(0 if goed else 1)


main()
