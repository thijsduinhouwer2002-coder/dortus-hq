import sys, bpy, bmesh, importlib
from mathutils import Matrix, Vector
OUT='/home/claude/testprint/'
bpy.ops.extensions.package_install_files(filepath='/tmp/click_joints_betaald.zip', repo='user_default', enable_on_install=True)
sys.modules.setdefault('click_joints', importlib.import_module('bl_ext.user_default.click_joints'))
print('PRO', 'plaats_scharnier' in dir(bpy.ops.click_joints))
def leeg():
    for ob in list(bpy.data.objects): bpy.data.objects.remove(ob)
    us=bpy.context.scene.unit_settings; us.system,us.scale_length,us.length_unit='METRIC',0.001,'MILLIMETERS'
def staaf(r, naam):
    bm=bmesh.new(); bmesh.ops.create_cone(bm,cap_ends=True,segments=48,radius1=r,radius2=r,depth=60,matrix=Matrix.Translation((0,0,30)))
    me=bpy.data.meshes.new(naam); bm.to_mesh(me); bm.free(); ob=bpy.data.objects.new(naam,me); bpy.context.scene.collection.objects.link(ob); return ob
def actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects: o.select_set(False)
    ob.select_set(True); bpy.context.view_layer.objects.active=ob
def zet_cursor(z):
    m=Matrix.Identity(4); m.col[3][:3]=Vector((0.031,0.137,z+0.071)); c=bpy.context.scene.cursor; c.rotation_mode='QUATERNION'; c.matrix=m
    inst=bpy.context.scene.click_joints; inst.as_bron, inst.uit_elkaar='CURSOR', False
    return inst
def exporteer(naam):
    delen=[o for o in bpy.context.scene.objects if o.get('cj_deel')]
    for d in delen:
        for o in bpy.context.view_layer.objects: o.select_set(False)
        d.select_set(True); bpy.context.view_layer.objects.active=d
        f=f"{OUT}{naam}-deel-{d.get('cj_deel')}.stl"
        bpy.ops.wm.stl_export(filepath=f, export_selected_objects=True, global_scale=1.0, apply_modifiers=True)
        print('STL', f, len(d.data.vertices))
    return len(delen)
# 1 scharnier 115
leeg(); ob=staaf(7.0,'knie'); zet_cursor(30.0); actief(ob)
print('scharnier', bpy.ops.click_joints.plaats_scharnier(stand='115')); print('delen', exporteer('scharnier-115'))
# 2 kogel
leeg(); ob=staaf(10.0,'arm'); inst=zet_cursor(30.0); inst.soort, inst.kogel_auto='KOGEL', True; actief(ob)
print('kogel', bpy.ops.click_joints.plaats()); print('delen', exporteer('kogel'))
