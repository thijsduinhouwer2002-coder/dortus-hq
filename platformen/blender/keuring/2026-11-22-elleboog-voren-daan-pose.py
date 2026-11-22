import bpy, sys, importlib, math
from mathutils import Vector
args = sys.argv[sys.argv.index("--") + 1:]
uitpng = args[0]
sc = bpy.context.scene
zb = importlib.import_module("bl_ext.user_default.click_joints.betaald.scharnier_beweeg")
delen = [o for o in sc.objects if o.type == "MESH" and o.get("cj_figuur") and o.visible_get()]
for o in sc.objects:
    if o.type == "MESH" and o not in delen:
        o.hide_render = True
    if o.type == "ARMATURE":
        o.hide_render = True
n = 0
for o in delen:
    if o.name.endswith("_B") and o.get("cj_soort") == "SCHARNIER" and "cj_scharnier_punt" in o.keys() and "cj_buigkant" in o.keys():
        try:
            o["cj_pose_graden"] = 90.0
            zb.zet_scharnier(o, False)
            n += 1
        except Exception as e:
            print("POSE fout", o.name, e)
print("GEPOSEERD", n, [o.name for o in delen])
for o in delen:
    print("DEEL", o.name, o.visible_get(), {k: (list(o[k]) if hasattr(o[k], "__len__") and not isinstance(o[k], str) else o[k]) for k in o.keys() if k in ("cj_buigkant", "cj_bereik_graden", "cj_pose_graden")})
pts = [o.matrix_world @ Vector(c) for o in delen if o.visible_get() for c in o.bound_box]
lo = Vector([min(p[i] for p in pts) for i in range(3)]); hi = Vector([max(p[i] for p in pts) for i in range(3)])
mid = (lo + hi) / 2; maat = max(hi - lo) * 1.1
sc.render.engine = "BLENDER_WORKBENCH"
sc.display.shading.color_type = "RANDOM"
sc.render.resolution_x = sc.render.resolution_y = 800
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam)
cam.data.type = "ORTHO"; cam.data.ortho_scale = maat; cam.data.clip_end = 100000
sc.camera = cam
for naam, pos, rot in (("boven", mid + Vector((0, 0, maat * 2)), (0, 0, 0)), ("voor", mid + Vector((0, -maat * 2, 0)), (math.pi / 2, 0, 0))):
    cam.location = pos; cam.rotation_euler = rot
    sc.render.filepath = f"{uitpng}-{naam}.png"
    bpy.ops.render.render(write_still=True)
