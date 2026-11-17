"""Proef (17 nov run 24, Ruben): zwaaigebied van deel B uit deel A halen buiten een bol rond het draaipunt, en opnieuw meten.
Op de MakeHuman-elleboog met rig-stop 115: gemeten 82 graden (vlees botst), na deze proef 100. Nog niet in de add-on.
Gebruik: S=10 R=1.0 CJ_EL=115 CJ_HOOGTE=220 blender -b --factory-startup --python e2e/proef_zwaai.py -- <betaalde zip> <base.obj>
"""
import importlib, math, os, sys, bpy, bmesh
from mathutils import Matrix, Vector
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "proef_kuil.py")).read().replace("\nmain()\n", "\n")
G = {"__name__": "k", "__file__": os.path.join(os.path.dirname(os.path.abspath(__file__)), "proef_kuil.py")}
exec(compile(src, "proef_kuil.py", "exec"), G)
G["main"]()
sc = bpy.context.scene
B = next(o for o in sc.objects if o.get("cj_deel") == "B" and o.visible_get())
A = next(o for o in sc.objects if o.get("cj_deel") == "A" and o.visible_get())
beweeg = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_beweeg")
ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
punt = Vector(B["cj_scharnier_punt"]); h = Vector(B["cj_scharnier_as"]); lid = Vector(B["cj_as"]); buig = Vector(B["cj_buigkant"])
stand = int(B["cj_stand"]); rn = B["cj_naad_r"]; R = float(os.environ.get("R", "1.0"))
bol = 1.5 * math.hypot(B["cj_breedte"], B["cj_breedte"]) + rn
print("VOOR", B["cj_bereik_graden"], "stand", stand, "rn", round(rn,2), "knokkel", round(B["cj_knokkel_r"],2))
voor_as = lid.cross(buig).normalized()
bpy.ops.mesh.primitive_uv_sphere_add(radius=rn + R, location=punt, segments=48, ring_count=24)
kern = bpy.context.active_object
S = int(os.environ.get("S", "10")); hoeken = list(range(S, stand, S)) + [stand - 0.5]
for g in hoeken:
    t = B.copy(); t.data = B.data.copy(); sc.collection.objects.link(t)
    t.modifiers.clear()
    t.matrix_world = Matrix.Translation(punt) @ Matrix.Rotation(math.radians(g), 4, voor_as) @ Matrix.Translation(-punt) @ B.matrix_world
    m = t.modifiers.new("k", "BOOLEAN"); m.operation, m.object, m.solver = "DIFFERENCE", kern, "EXACT"
    bpy.context.view_layer.objects.active = t; bpy.ops.object.modifier_apply(modifier="k")
    m = A.modifiers.new("z", "BOOLEAN"); m.operation, m.object, m.solver = "DIFFERENCE", t, "EXACT"
    bpy.context.view_layer.objects.active = A; bpy.ops.object.modifier_apply(modifier="z")
    bpy.data.objects.remove(t)
    b_ = bmesh.new(); b_.from_mesh(A.data); print("STAP", g, round(b_.calc_volume(), 2), len(A.data.polygons)); b_.free()
bpy.data.objects.remove(kern)
voor, achter = beweeg.bereik(A, B, punt, h, buig, lid, bol)
st = G["A"]["mesh_staat"](A)
print("NA", round(voor, 2), "achter", round(achter or 0, 2), "A gesloten", ges.is_gesloten(A)[0], "stukken", st["losse_stukken"])
import numpy as np
from mathutils.bvhtree import BVHTree
for g in (voor + 0.5, voor + 5):
    pa, ta = beweeg._driehoeken(A, punt, bol); pb, tb = beweeg._driehoeken(B, punt, bol)
    M = Matrix.Translation(punt) @ Matrix.Rotation(math.radians(g), 4, voor_as) @ Matrix.Translation(-punt)
    m = np.array(M); pb2 = pb @ m[:3, :3].T + m[:3, 3]
    ba = BVHTree.FromPolygons(pa.tolist(), ta); bb = BVHTree.FromPolygons(pb2.tolist(), tb)
    paren = ba.overlap(bb)
    cs = [Vector(pa[ta[i]].mean(axis=0)) - punt for i, _ in paren]
    fr = [(round(c.dot(h),1), round(c.dot(buig),1), round(c.dot(lid),1)) for c in cs]
    print("RAAK bij", round(g,1), len(paren), "eerste (h, buig, lid):", sorted(set(fr))[:8], "wig", B["cj_wig_graden"], "theta_s", B["cj_theta_s"])
