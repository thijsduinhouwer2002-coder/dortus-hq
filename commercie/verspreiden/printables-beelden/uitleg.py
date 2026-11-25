import bpy, math, sys
from mathutils import Vector, Matrix

D = '/home/claude/render/delen/'
out = sys.argv[1]
flip = sys.argv[2] if len(sys.argv) > 2 else ''
bpy.ops.wm.read_factory_settings(use_empty=True)

m = bpy.data.materials.new('pla')
b = m.node_tree.nodes['Principled BSDF']
b.inputs['Base Color'].default_value = (0.85, 0.27, 0.03, 1)
b.inputs['Roughness'].default_value = 0.42

def load(name):
    bpy.ops.wm.stl_import(filepath=D + name + '.stl')
    o = bpy.context.selected_objects[0]
    o.data.materials.append(m)
    bpy.ops.object.shade_auto_smooth(angle=math.radians(35))
    return o

def ground(o):
    bpy.context.view_layer.update()
    z = min((o.matrix_world @ Vector(c)).z for c in o.bound_box)
    o.location.z -= z

def centre_xy(o, x, y):
    bpy.context.view_layer.update()
    cs = [o.matrix_world @ Vector(c) for c in o.bound_box]
    cx = (min(c.x for c in cs) + max(c.x for c in cs)) / 2
    cy = (min(c.y for c in cs) + max(c.y for c in cs)) / 2
    o.location.x += x - cx; o.location.y += y - cy

# assembled pair 20: ball centre and cup centre measured with trimesh
bal_c = Vector((70.031, 10.137, 38.471))
kom_c = Vector((70.031, 42.251, 21.525))
bal = load('bal20')
kom = load('kom20')
R = Matrix.Rotation(math.pi, 4, 'X')
# put flipped cup centre on the ball centre
R = Matrix.Rotation(math.radians(-62), 4, 'X') @ R
kom.matrix_world = Matrix.Translation(bal_c + Vector((0, -10, 20))) @ R @ Matrix.Translation(-kom_c)
shift = Vector((0, 40, 0)) - Vector((bal_c.x, bal_c.y, 0))
bal.location += shift; kom.location += shift

# loose cups lying on their side, numbered end toward camera
xs = {'kom10': -63, 'kom15': -21, 'kom25': 21, 'kom30': 63}
for n, x in xs.items():
    o = load(n)
    o.rotation_euler = (-math.pi / 2, 0, 0)
    if n in flip:
        o.rotation_euler = (-math.pi / 2, math.pi, 0)
    ground(o); centre_xy(o, x, -15)

bpy.ops.mesh.primitive_plane_add(size=3000)
g = bpy.context.object
gm = bpy.data.materials.new('grond')
gb = gm.node_tree.nodes['Principled BSDF']
gb.inputs['Base Color'].default_value = (0.86, 0.84, 0.80, 1)
gb.inputs['Roughness'].default_value = 0.75
g.data.materials.append(gm)

w = bpy.data.worlds.new('w'); bpy.context.scene.world = w
w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.80, 0.79, 0.77, 1)
w.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.5

def area(loc, power, size, aim=(0, 10, 20)):
    bpy.ops.object.light_add(type='AREA', location=loc)
    l = bpy.context.object; l.data.energy = power; l.data.size = size
    l.rotation_euler = (Vector(aim) - l.location).to_track_quat('-Z', 'Y').to_euler()
area((-170, -150, 230), 260000, 170)
area((220, -90, 110), 60000, 130)
area((60, 260, 180), 110000, 130)

bpy.ops.object.camera_add(location=(0, -300, 150))
cam = bpy.context.object
tgt = Vector((0, 15, 30))
cam.rotation_euler = (tgt - cam.location).to_track_quat('-Z', 'Y').to_euler()
cam.data.lens = 62
cam.data.dof.use_dof = True
cam.data.dof.focus_distance = (Vector((0, 20, 30)) - cam.location).length
cam.data.dof.aperture_fstop = 5.6
bpy.context.scene.camera = cam

s = bpy.context.scene
s.render.engine = 'CYCLES'; s.cycles.device = 'CPU'
s.cycles.samples = int(sys.argv[3]) if len(sys.argv) > 3 else 48
s.cycles.use_denoising = True
s.render.resolution_x, s.render.resolution_y = (1600, 1200) if s.cycles.samples > 20 else (800, 600)
s.view_settings.view_transform = 'AgX'
s.view_settings.look = 'AgX - Medium High Contrast'
s.render.filepath = out
bpy.ops.render.render(write_still=True)
