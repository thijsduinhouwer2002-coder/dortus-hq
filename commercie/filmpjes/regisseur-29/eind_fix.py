"""Maakt eind.blend klaar voor de Cycles-eindfilm (v7b, keuring Daan #217). Twee fouten uit v7:
1. De add-on bewaart de tussenstappen van het snijden als verborgen objecten. Verborgen in de weergave is niet
   verborgen in de render, dus in de eindfilm stonden armen in rust over de geposeerde robot heen ("twee poses").
   Elk mesh dat niet zichtbaar is, gaat hier ook uit de render.
2. De camera ging in een rechte lijn van begin naar eind en kwam halverwege 13% dichterbij (sokkel van het beeld).
   Hier gaat hij over een boog om het midden van de robot, met gelijke afstand; kijkrichting draait mee.
    blender -b eind.blend --python eind_fix.py   (slaat eind.blend zelf op)"""
import bpy
from mathutils import Vector

sc = bpy.context.scene
n = 0
for o in bpy.data.objects:
    if o.type == "MESH" and not o.visible_get() and not o.hide_render:
        o.hide_render = True
        n += 1
delen = [o for o in sc.objects if o.type == "MESH" and o.get("cj_figuur") and not o.hide_render]
lo = Vector((min((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box),
             min((o.matrix_world @ Vector(c)).y for o in delen for c in o.bound_box),
             min((o.matrix_world @ Vector(c)).z for o in delen for c in o.bound_box)))
hi = Vector((max((o.matrix_world @ Vector(c)).x for o in delen for c in o.bound_box),
             max((o.matrix_world @ Vector(c)).y for o in delen for c in o.bound_box),
             max((o.matrix_world @ Vector(c)).z for o in delen for c in o.bound_box)))
mid = (lo + hi) / 2
cam = sc.camera
f0, f1 = sc.frame_start, sc.frame_end
sc.frame_set(f0)
l0, q0 = cam.matrix_world.to_translation(), cam.matrix_world.to_quaternion()
sc.frame_set(f1)
l1, q1 = cam.matrix_world.to_translation(), cam.matrix_world.to_quaternion()
cam.animation_data_clear()
cam.rotation_mode = "QUATERNION"
v0, v1 = l0 - mid, l1 - mid
r0, r1 = v0.length, v1.length
d0, d1 = v0.normalized(), v1.normalized()


def zacht(t):
    return t * t * (3 - 2 * t)


def slerp_v(a, b, t):
    from mathutils import Quaternion
    q = a.rotation_difference(b)
    return Quaternion(q.axis, q.angle * t) @ a


for f in range(f0, f1 + 1, 3):
    t = zacht((f - f0) / max(1, f1 - f0))
    cam.location = mid + slerp_v(d0, d1, t) * (r0 + (r1 - r0) * t)
    cam.rotation_quaternion = q0.slerp(q1, t)
    cam.keyframe_insert("location", frame=f)
    cam.keyframe_insert("rotation_quaternion", frame=f)
print(f"EIND_FIX {n} verborgen meshes uit de render, {len(delen)} delen, camera boog r {r0:.0f} tot {r1:.0f}")
bpy.ops.wm.save_mainfile()
