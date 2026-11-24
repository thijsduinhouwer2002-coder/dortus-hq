"""Bron-STL voor scherm_gids_stl.py: de CC0-figuur Knight van Quaternius (Ultimate Monsters, CC0 1.0,
https://quaternius.com/packs/ultimatemonsters.html; blend in de repo: commercie/filmpjes/monsters/blends/Knight.blend),
in rustpose, samengevoegd en geschaald naar 250 mm hoog, als STL in mm, zoals een printer hem downloadt.
Schrijft <map>/figure.stl en <map>/gewrichten.json (elleboog en knie in mm, met de richting van het bot).
    blender -b --python e2e/gids_stl_bron.py -- <map>"""
import json
import os
import sys

import bpy
from mathutils import Matrix, Vector

map_ = sys.argv[sys.argv.index("--") + 1]
os.makedirs(map_, exist_ok=True)
hier = os.path.dirname(os.path.abspath(__file__))
blend = os.path.normpath(os.path.join(hier, "..", "..", "..", "commercie", "filmpjes", "monsters", "blends", "Knight.blend"))
bpy.ops.wm.open_mainfile(filepath=blend)
arm = next(o for o in bpy.data.objects if o.type == "ARMATURE")
arm.data.pose_position = "REST"
bpy.context.view_layer.update()
botten = {b.name: (arm.matrix_world @ b.head_local, arm.matrix_world @ b.tail_local) for b in arm.data.bones}
dg = bpy.context.evaluated_depsgraph_get()
me = None
for m in [o for o in bpy.data.objects if o.type == "MESH"]:
    nieuw = bpy.data.meshes.new_from_object(m.evaluated_get(dg))
    nieuw.transform(m.matrix_world)
    if me is None:
        me = nieuw
    else:
        import bmesh
        bm = bmesh.new(); bm.from_mesh(me); bm.from_mesh(nieuw); bm.to_mesh(me); bm.free()
mn = Vector([min(v.co[i] for v in me.vertices) for i in range(3)])
mx = Vector([max(v.co[i] for v in me.vertices) for i in range(3)])
s = 250.0 / (mx.z - mn.z)
zet = Matrix.Scale(s, 4) @ Matrix.Translation(Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z)))
me.transform(zet)
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)
ob = bpy.data.objects.new("figure", me)
bpy.context.scene.collection.objects.link(ob)
print("DIMS mm", [round(d, 1) for d in ob.dimensions])


def bot(naam):
    kop = zet @ botten[naam][0]
    # richting: langs het bovenste bot (bovenarm of dijbeen) naar dit gewricht; in rustpose ligt de ledemaat gestrekt
    vorig = naam.replace("Lower", "Upper")
    richting = (kop - (zet @ botten[vorig][0])).normalized()
    return {"plek": [round(c, 2) for c in kop], "richting": [round(c, 4) for c in richting]}


uit = {n: bot(n) for n in ("LowerArm.L", "LowerArm.R", "LowerLeg.L", "LowerLeg.R")}
print("GEWRICHTEN", uit)
json.dump(uit, open(os.path.join(map_, "gewrichten.json"), "w"), indent=1)
bpy.ops.wm.stl_export(filepath=os.path.join(map_, "figure.stl"), global_scale=1.0, export_selected_objects=False)
