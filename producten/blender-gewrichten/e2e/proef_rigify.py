"""Proef (geen toets, 16 nov run 5): Figure from rig op de echte Rigify-metarig (Human), 100 keer geschaald (±18 cm),
met een eenvoudige mesh van buizen om de hoofdbotten (dij r 7, scheen 6, bovenarm 6,5, onderarm 6 mm).
Uitkomst 16 nov in 5.3.0: zeven gewrichten (ellebogen, knieën, heupen, nek), 8 gesloten delen; schouders
overgeslagen: de sleuf van de elleboog (135 graden reikt ±20 mm) laat op een bovenarm van 29 mm geen plek voor de kom.
Eerder met dij r 9 en onderarm r 5: ellebogen Tight (te dun) en de benen raakten elkaar. Werkpunten in ontwerp-1.1.md.
    blender -b --factory-startup --python e2e/proef_rigify.py -- <betaalde zip>
Met CJ_ALLEEN=hip,knee (stukjes van de gewone namen) alleen die gewrichten, om uit te zoeken welke elkaar storen.
"""
import sys, math, importlib, addon_utils, bpy, bmesh
from mathutils import Matrix, Vector
zip_pad = sys.argv[sys.argv.index("--") + 1]
bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
print("PROBE rigify", addon_utils.enable("rigify", default_set=True) is not None)
for ob in list(bpy.data.objects): bpy.data.objects.remove(ob)
us = bpy.context.scene.unit_settings; us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
inst = bpy.context.scene.click_joints
inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
bpy.ops.object.armature_human_metarig_add()
arm = bpy.context.active_object
arm.scale = (100, 100, 100)
bpy.ops.object.transform_apply(scale=True)
# dikte per bot (mm), alleen hoofdbotten
DIK = {"thigh": 7, "shin": 6, "upper_arm": 6.5, "forearm": 6, "spine": 16, "spine.001": 16, "spine.002": 17, "spine.003": 17,
       "spine.004": 5, "spine.005": 5, "spine.006": 10, "foot": 5, "hand": 4, "pelvis": 0, "shoulder": 7, "breast": 0}
bm = bmesh.new()
for b in arm.data.bones:
    k = b.name.split(".L")[0].split(".R")[0]
    r = DIK.get(k) or DIK.get(b.name)
    if not r: continue
    h, t = arm.matrix_world @ b.head_local, arm.matrix_world @ b.tail_local
    d = t - h; L = d.length
    rot = d.to_track_quat("Z", "Y").to_matrix().to_4x4()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=r, radius2=r, depth=L + r, matrix=Matrix.Translation((h + t) / 2) @ rot)
    bmesh.ops.create_uvsphere(bm, u_segments=16, v_segments=8, radius=r, matrix=Matrix.Translation(t))
me = bpy.data.meshes.new("b"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("b", me); bpy.context.scene.collection.objects.link(ob)
m = ob.modifiers.new("v", "REMESH"); m.mode, m.voxel_size = "VOXEL", 0.8
dg = bpy.context.evaluated_depsgraph_get(); me2 = bpy.data.meshes.new_from_object(ob.evaluated_get(dg)); bpy.data.objects.remove(ob)
mesh = bpy.data.objects.new("held", me2); bpy.context.scene.collection.objects.link(mesh)
mesh.modifiers.new("Armature", "ARMATURE").object = arm
print("PROBE hoogte", round(max((v.co.z for v in me2.vertices)), 1), "botten", [b.name for b in arm.data.bones if any(x in b.name for x in ("thigh", "shin", "upper_arm", "forearm", "spine.004"))])
bpy.context.view_layer.update()
for o in bpy.context.scene.objects: o.select_set(False)
mesh.select_set(True); bpy.context.view_layer.objects.active = mesh
import os
_alleen = os.environ.get("CJ_ALLEEN", "")
if _alleen:
    _rigm = importlib.import_module("bl_ext.user_default.click_joints.betaald.rig")
    _g = _rigm.gewrichten
    _rigm.gewrichten = lambda a, meer=False: [x for x in _g(a, meer) if any(w in x[2].lower() for w in _alleen.split(","))]
try:
    r = bpy.ops.click_joints.figuur_uit_rig()
except RuntimeError as e:
    r = f"fout {e}"
fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
alle = fig.figuur_gewrichten(bpy.context.scene.objects, "held")
print("PROBE", r, [fig.regel(x) for x in alle])
print("PROBE overgeslagen", next((o.get("cj_rig_overgeslagen") for o in bpy.context.scene.objects if o.get("cj_deel")), None))
ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == "held" and o.visible_get() and o.type == "MESH"]
print("PROBE delen", len(delen), "open", [o.name for o in delen if not ges.is_gesloten(o)])
