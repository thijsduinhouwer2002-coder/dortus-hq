"""Beeld bij een proef: vooraanzicht en zijaanzicht van een _rig.blend, delen in kleur, botkoppen als rode bolletjes.

Gebruik: blender -b <naam>_rig.blend --python e2e/kijk_figuur.py -- <uitmap>
"""
import bpy, sys, os, math
from mathutils import Vector
uit = sys.argv[sys.argv.index("--") + 1]
naam = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
sc = bpy.context.scene
kleuren = [(0.9,0.5,0.2,1),(0.3,0.6,0.9,1),(0.5,0.8,0.3,1),(0.9,0.8,0.2,1),(0.8,0.3,0.6,1),(0.4,0.9,0.9,1),(0.7,0.7,0.7,1)]
meshes = [o for o in sc.objects if o.type == "MESH" and o.visible_get()]
for i, o in enumerate(meshes):
    o.color = kleuren[i % len(kleuren)]
rig = next((o for o in sc.objects if o.type == "ARMATURE"), None)
if rig:
    for b in rig.data.bones:
        p = rig.matrix_world @ b.head_local
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2.0, location=p)
        s = bpy.context.active_object; s.color = (1, 0, 0, 1); s.show_in_front = True
    rig.hide_render = True
sc.render.engine = "BLENDER_WORKBENCH"
sc.display.shading.color_type = "OBJECT"
sc.display.shading.show_xray = True
sc.display.shading.xray_alpha = 0.6
sc.render.resolution_x, sc.render.resolution_y = 700, 900
alle = [o for o in sc.objects if o.type == "MESH"]
lo = Vector([min((o.matrix_world @ Vector(c))[i] for o in meshes for c in o.bound_box) for i in range(3)])
hi = Vector([max((o.matrix_world @ Vector(c))[i] for o in meshes for c in o.bound_box) for i in range(3)])
mid = (lo + hi) / 2; groot = max(hi - lo) * 1.15
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.type = "ORTHO"; cam.data.ortho_scale = groot; cam.data.clip_end = 10000
for kant, loc, rot in (("voor", (0, -1, 0), (90, 0, 0)), ("zij", (1, 0, 0), (90, 0, 90))):
    cam.location = mid + Vector(loc) * groot * 3
    cam.rotation_euler = [math.radians(r) for r in rot]
    sc.render.filepath = os.path.join(uit, f"{naam}-{kant}.png")
    bpy.ops.render.render(write_still=True)
print("[kijk] " + naam + " dim", tuple(round(x,1) for x in (hi-lo)), "delen", len(meshes))
