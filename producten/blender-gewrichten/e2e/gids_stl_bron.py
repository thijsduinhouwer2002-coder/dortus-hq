"""Bron-STL voor scherm_gids_stl.py: een CC0-figuur van Quaternius (glb uit quaternius-showcase), samengevoegd en
geschaald naar 250 mm hoog, als STL in mm, zoals een printer hem downloadt. Paden staan vast op /home/claude/g5 (proef 24 nov).
    blender -b --python e2e/gids_stl_bron.py"""
import bpy, json
from mathutils import Vector
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath="/home/claude/g5/knight.glb")
arm = next((o for o in bpy.data.objects if o.type=="ARMATURE"), None)
bones = {}
if arm:
    for b in arm.data.bones:
        bones[b.name] = list(arm.matrix_world @ b.head_local)
meshes = [o for o in bpy.data.objects if o.type=="MESH" and o.name!="Icosphere"]
print("MESHES", [(m.name, len(m.data.polygons)) for m in meshes])
dg = bpy.context.evaluated_depsgraph_get()
nieuw = []
for m in meshes:
    me = bpy.data.meshes.new_from_object(m.evaluated_get(dg))
    me.transform(m.matrix_world)
    o = bpy.data.objects.new(m.name+"_x", me); bpy.context.scene.collection.objects.link(o); nieuw.append(o)
for o in list(bpy.data.objects):
    if o not in nieuw: bpy.data.objects.remove(o)
bpy.context.view_layer.objects.active = nieuw[0]
for o in nieuw: o.select_set(True)
bpy.ops.object.join()
ob = bpy.context.active_object
mn = Vector([min(v.co[i] for v in ob.data.vertices) for i in range(3)])
mx = Vector([max(v.co[i] for v in ob.data.vertices) for i in range(3)])
h = mx.z - mn.z
s = 250.0 / h
ob.data.transform(__import__("mathutils").Matrix.Scale(s,4))
print("HOOGTE oud", h, "schaal", s, "dims", [ (mx[i]-mn[i])*s for i in range(3)])
json.dump({k:[c*s for c in v] for k,v in bones.items()}, open("/home/claude/g5/bones.json","w"), indent=0)
bpy.ops.wm.stl_export(filepath="/home/claude/g5/figure.stl", global_scale=1.0, export_selected_objects=False)
