"""Proef (geen toets): Figure from rig op een figuur met armen (Rigify-namen, elleboog links met grens 140).
16 nov run 5: kogel aan de komkant alleen r + s + 0,5 mm en kogels uit de romp geschoven; korte benen: schouders
lukken, heupen niet (dij 33 mm, knie reikt 25 mm); met "lang" (dij 45 mm) lukken alle acht.
16 nov run 4: met kogels eerst vielen beide ellebogen af naast de schouderkogel; met scharnieren eerst lukken
knieën en ellebogen (links 0-140 from rig) en vallen schouders en heupen af (afstandsregel kogel-scharnier).
    blender -b --factory-startup --python e2e/proef_armen.py -- <betaalde zip> [lang]
"""
import sys, math, importlib, bpy, bmesh
from mathutils import Matrix
zip_pad = sys.argv[sys.argv.index("--") + 1]
# Tweede argument "lang": benen 90 mm (dij 50 mm, zoals een figuur van ±18 cm), anders de korte benen van run 4.
B = 90.0 if "lang" in sys.argv[sys.argv.index("--") + 1:] else 70.0
bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
for ob in list(bpy.data.objects): bpy.data.objects.remove(ob)
us = bpy.context.scene.unit_settings; us.system, us.scale_length, us.length_unit = "METRIC", 0.001, "MILLIMETERS"
inst = bpy.context.scene.click_joints
inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
bm = bmesh.new()
for x in (-10.0, 10.0):  # benen r 8
    bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=8, radius2=8, depth=B, matrix=Matrix.Translation((x, 0, B / 2)))
bmesh.ops.create_cube(bm, size=1, matrix=Matrix.Translation((0, 0, B + 30)) @ Matrix.Diagonal((40, 20, 70, 1)))  # romp z B-5..B+65
for s in (-1, 1):  # armen r 6, horizontaal van x=20 tot 90 op z 125
    bmesh.ops.create_cone(bm, cap_ends=True, segments=32, radius1=6, radius2=6, depth=75,
                          matrix=Matrix.Translation((s * 55, 0, B + 55)) @ Matrix.Rotation(math.radians(90), 4, "Y"))
me = bpy.data.meshes.new("b"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("b", me); bpy.context.scene.collection.objects.link(ob)
r = ob.modifiers.new("v", "REMESH"); r.mode, r.voxel_size = "VOXEL", 0.6
dg = bpy.context.evaluated_depsgraph_get(); me2 = bpy.data.meshes.new_from_object(ob.evaluated_get(dg)); bpy.data.objects.remove(ob)
mesh = bpy.data.objects.new("held", me2); bpy.context.scene.collection.objects.link(mesh)
data = bpy.data.armatures.new("rig"); arm = bpy.data.objects.new("rig", data); bpy.context.scene.collection.objects.link(arm)
bpy.context.view_layer.objects.active = arm; bpy.ops.object.mode_set(mode="EDIT")
for k, s in (("L", 1), ("R", -1)):
    kn, sch = B / 2, B + 55  # knie halverwege het been, schouderhoogte
    th = data.edit_bones.new(f"thigh.{k}"); th.head, th.tail = (s*10, 0, B - 2), (s*10, 0, kn)
    sh = data.edit_bones.new(f"shin.{k}"); sh.head, sh.tail = (s*10, 0, kn), (s*10, 0, 4); sh.parent = th
    ua = data.edit_bones.new(f"upper_arm.{k}"); ua.head, ua.tail = (s*24, 0, sch), (s*55, 0, sch)
    fa = data.edit_bones.new(f"forearm.{k}"); fa.head, fa.tail = (s*55, 0, sch), (s*88, 0, sch); fa.parent = ua
bpy.ops.object.mode_set(mode="OBJECT")
c = arm.pose.bones["forearm.L"].constraints.new("LIMIT_ROTATION"); c.use_limit_x, c.min_x, c.max_x, c.owner_space = True, 0, math.radians(140), "LOCAL"
mesh.modifiers.new("Armature", "ARMATURE").object = arm
for o in bpy.context.view_layer.objects: o.select_set(False)
mesh.select_set(True); bpy.context.view_layer.objects.active = mesh
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
