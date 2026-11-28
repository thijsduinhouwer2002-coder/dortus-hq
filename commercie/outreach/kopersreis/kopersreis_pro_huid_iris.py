import bpy,sys,traceback
from mathutils import Vector
S=sys.argv[-1]  # map met zips/click_joints_pro-<versie>.zip en uit2-5.3.0-1.2.8/my_figure.stl (uit kopersreis_pro_iris.py); z=sys.argv[-2]; F=7.0
bpy.ops.extensions.package_install_files(filepath=S+"/zips/click_joints_pro-%s.zip"%z, repo="user_default", enable_on_install=True)
GEVALLEN=[("SHOULDER",(-8*F,-2.6*F,3*F)),("HIP",(-3.2*F,-3.0*F,-6.5*F)),("KNEE",(-3.2*F,-3.0*F,-14.3*F)),("ELBOW",(-11.3*F,-2.6*F,3*F)),
          ("SHOULDER_mid",(-8*F,0,3*F))]
def run():
    try:
        for deel,p in GEVALLEN:
            for o in list(bpy.data.objects): bpy.data.objects.remove(o)
            us=bpy.context.scene.unit_settings; us.scale_length=1.0; us.length_unit="METERS"
            bpy.ops.wm.stl_import(filepath=S+"/uit2-5.3.0-1.2.8/my_figure.stl")
            bpy.ops.click_joints.zet_om_mm()
            ob=bpy.context.view_layer.objects.active
            win=bpy.context.window_manager.windows[0]
            area=[a for a in win.screen.areas if a.type=="VIEW_3D"][0]
            reg=[r for r in area.regions if r.type=="WINDOW"][0]
            r3=area.spaces[0].region_3d
            # vooraanzicht: kijker op -Y kijkt naar +Y
            from mathutils import Euler
            r3.view_rotation=Euler((1.5707963,0,0)).to_quaternion(); r3.view_perspective="ORTHO"
            c=bpy.context.scene.cursor; c.location=p; c.rotation_mode="QUATERNION"
            # Shift + rechtsklik met standaard keymap: oriëntatie VIEW, cursor-Z naar de kijker
            c.rotation_quaternion=r3.view_rotation
            with bpy.context.temp_override(window=win,area=area,region=reg):
                try:
                    r=bpy.ops.click_joints.plaats_preset(deel=deel.split("_")[0]); print("SCHERM",z,deel,r,len([o for o in bpy.data.objects if o.get("cj_deel")]),flush=True)
                except Exception as e: print("SCHERM",z,deel,str(e).strip(),flush=True)
    except Exception:
        traceback.print_exc()
    bpy.ops.wm.quit_blender()
bpy.app.timers.register(run, first_interval=1.0)
