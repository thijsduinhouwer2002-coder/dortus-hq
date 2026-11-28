import bpy,sys
from mathutils import Vector
S=sys.argv[-1]  # map met zips/click_joints_pro-<versie>.zip en uit2-5.3.0-1.2.8/my_figure.stl (uit kopersreis_pro_iris.py)
z=sys.argv[-2]
bpy.ops.extensions.package_install_files(filepath=S+"/zips/click_joints_pro-%s.zip"%z, repo="user_default", enable_on_install=True)
for p in [(-22.4,0,-100),(-22.0,0.3,-100),(-22.4,0,-97.3)]:
    bpy.ops.wm.read_homefile(use_factory_startup=True)
    bpy.ops.wm.stl_import(filepath=S+"/uit2-5.3.0-1.2.8/my_figure.stl")
    bpy.ops.click_joints.zet_om_mm()
    c=bpy.context.scene.cursor; c.location=p; c.rotation_mode="QUATERNION"; c.rotation_quaternion=Vector((0,0,1)).to_track_quat("Z","Y")
    try: r=bpy.ops.click_joints.plaats_preset(deel="KNEE"); print("KNIE",z,p,r,[o.name for o in bpy.data.objects if o.get("cj_deel")])
    except Exception as e: print("KNIE",z,p,str(e).strip())
