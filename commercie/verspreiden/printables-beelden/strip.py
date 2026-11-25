import bpy, math, sys
from mathutils import Vector

stl, out, view = sys.argv[1], sys.argv[2], sys.argv[3]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.wm.stl_import(filepath=stl)
obj = bpy.context.selected_objects[0]
# origin to bounds centre, bottom on z=0
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
obj.location = (0, 0, 0)
bpy.context.view_layer.update()
zmin = min((obj.matrix_world @ Vector(c)).z for c in obj.bound_box)
obj.location.z -= zmin
if view == 'onder':
    obj.rotation_euler = (math.pi, 0, 0)
    bpy.context.view_layer.update()
    zmin = min((obj.matrix_world @ Vector(c)).z for c in obj.bound_box)
    obj.location.z -= zmin
bpy.ops.object.shade_auto_smooth(angle=math.radians(35))

# material: matte PLA orange
m = bpy.data.materials.new('pla'); m.use_nodes = True
b = m.node_tree.nodes['Principled BSDF']
b.inputs['Base Color'].default_value = (0.80, 0.25, 0.04, 1)
b.inputs['Roughness'].default_value = 0.45
obj.data.materials.append(m)

# ground: soft light grey that fades
bpy.ops.mesh.primitive_plane_add(size=2000, location=(0, 0, 0))
g = bpy.context.object
gm = bpy.data.materials.new('grond'); gm.use_nodes = True
gb = gm.node_tree.nodes['Principled BSDF']
gb.inputs['Base Color'].default_value = (0.75, 0.76, 0.78, 1)
gb.inputs['Roughness'].default_value = 0.8
g.data.materials.append(gm)

w = bpy.context.scene.world or bpy.data.worlds.new('w')
bpy.context.scene.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.42, 0.44, 0.47, 1)
w.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.6

def area(loc, power, size):
    bpy.ops.object.light_add(type='AREA', location=loc)
    l = bpy.context.object; l.data.energy = power; l.data.size = size
    d = Vector((0, 0, 15)) - l.location
    l.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
area((-150, -120, 220), 220000, 160)   # key
area((200, -60, 90), 50000, 120)      # fill
area((40, 220, 160), 90000, 120)      # rim

if view == 'schuin':
    cam_loc, target, lens = (190, -310, 210), (0, 0, 16), 70
else:
    cam_loc, target, lens = (0, -60, 330), (0, 0, 0), 62
bpy.ops.object.camera_add(location=cam_loc)
cam = bpy.context.object
cam.rotation_euler = (Vector(target) - cam.location).to_track_quat('-Z', 'Y').to_euler()
cam.data.lens = lens
cam.data.dof.use_dof = view == 'schuin'
cam.data.dof.focus_distance = (Vector(target) - cam.location).length
cam.data.dof.aperture_fstop = 8
bpy.context.scene.camera = cam

s = bpy.context.scene
s.render.engine = 'CYCLES'; s.cycles.device = 'CPU'
s.cycles.samples = 48; s.cycles.use_denoising = True
s.render.resolution_x, s.render.resolution_y = 1600, 1200
s.view_settings.view_transform = 'AgX'
s.view_settings.look = 'AgX - Medium High Contrast'
s.render.filepath = out
bpy.ops.render.render(write_still=True)
