"""Renders voor het nieuwe strip-beeld: doorsnede van paar 20 en de rij nummers. Transparante achtergrond."""
import bpy, bmesh, math, sys
from mathutils import Vector, Matrix

D = '/home/claude/render/delen/'
modus, out, samples = sys.argv[1], sys.argv[2], int(sys.argv[3])
bpy.ops.wm.read_factory_settings(use_empty=True)

def mat(naam, kleur, rough, metal=0.0):
    m = bpy.data.materials.new(naam)
    b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = kleur
    b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal
    return m

WIT = mat('wit', (0.80, 0.76, 0.70, 1), 0.55)
GOUD = mat('goud', (1.0, 0.55, 0.12, 1), 0.28, 0.6)
INKT = mat('inkt', (0.85, 0.42, 0.06, 1), 0.35, 0.4)
SNEDE = mat('snede', (0.62, 0.60, 0.66, 1), 0.7)
KOMSNEDE = mat('komsnede', (0.92, 0.90, 0.86, 1), 0.7)

def load(name):
    bpy.ops.wm.stl_import(filepath=D + name + '.stl')
    o = bpy.context.selected_objects[0]
    o.data.materials.append(WIT)
    return o

BAL_C = Vector((70.031, 10.137, 38.471))
KOM_C = Vector((70.031, 42.251, 21.525))

def cam(loc, tgt, lens, ortho=None):
    bpy.ops.object.camera_add(location=loc)
    c = bpy.context.object
    c.rotation_euler = (Vector(tgt) - c.location).to_track_quat('-Z', 'Y').to_euler()
    c.data.lens = lens
    if ortho:
        c.data.type = 'ORTHO'; c.data.ortho_scale = ortho
    bpy.context.scene.camera = c

def area(loc, power, size, aim):
    bpy.ops.object.light_add(type='AREA', location=loc)
    l = bpy.context.object; l.data.energy = power; l.data.size = size
    l.rotation_euler = (Vector(aim) - l.location).to_track_quat('-Z', 'Y').to_euler()

if modus in ('doorsnede', 'zoom'):
    bal = load('bal20'); kom = load('kom20')
    kom.matrix_world = Matrix.Translation(BAL_C) @ Matrix.Rotation(math.pi, 4, 'X') @ Matrix.Translation(-KOM_C)
    bpy.context.view_layer.update()
    # snijblok: alles met y < ball centre weg
    bpy.ops.mesh.primitive_cube_add(size=200, location=(BAL_C.x, BAL_C.y - 100, BAL_C.z))
    blok = bpy.context.object
    for o in (bal, kom):
        o.data.materials.append(SNEDE)
        m = o.modifiers.new('snij', 'BOOLEAN'); m.operation = 'DIFFERENCE'; m.object = blok; m.solver = 'EXACT'
        m.material_mode = 'TRANSFER'
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.modifier_apply(modifier='snij')
    # goud bolletje: bol net binnen de kogel, snijvlak 0,005 mm voor het snijvlak van de kogel
    bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=64, radius=5.995, location=BAL_C)
    bol = bpy.context.object; bol.data.materials.append(GOUD)
    bpy.ops.object.shade_smooth()
    blok.location.y -= 0.005
    m = bol.modifiers.new('snij', 'BOOLEAN'); m.operation = 'DIFFERENCE'; m.object = blok; m.solver = 'EXACT'
    bpy.context.view_layer.objects.active = bol
    bpy.ops.object.modifier_apply(modifier='snij')
    blok.hide_render = True; blok.hide_viewport = True
    # kleuren: snijvlak (normaal -Y, op y = BAL_C.y) grijs, bol goud
    for o in (bal, kom):
        if len(o.data.materials) < 3:
            o.data.materials.append(GOUD)
            o.data.materials.append(KOMSNEDE)
        idx_k = list(o.data.materials).index(KOMSNEDE)
        idx_w = 0; idx_s = list(o.data.materials).index(SNEDE); idx_g = list(o.data.materials).index(GOUD)
        mw = o.matrix_world
        for p in o.data.polygons:
            c = mw @ p.center
            n = (mw.to_3x3() @ p.normal).normalized()
            if abs(c.y - BAL_C.y) < 0.02 and n.y < -0.9:
                if o is bal and (c - BAL_C).length < 6.0:
                    p.material_index = idx_g
                elif o is kom:
                    p.material_index = idx_k
                else:
                    p.material_index = idx_s
            elif o is bal and (c - BAL_C).length < 6.05:
                p.material_index = idx_g
            else:
                p.material_index = idx_w
        for p in o.data.polygons:
            p.use_smooth = False
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.shade_auto_smooth(angle=math.radians(30))
    if modus == 'doorsnede':
        cam((BAL_C.x + 75, BAL_C.y - 150, BAL_C.z + 45), (BAL_C.x, BAL_C.y, BAL_C.z - 3), 85)
    else:  # recht op het spleetje boven de bol
        g = BAL_C + Vector((0, 0, 6.1))
        cam((g.x + 3, g.y - 22, g.z + 2), (g.x, g.y, g.z - 1.0), 100)
    area((BAL_C.x - 120, BAL_C.y - 160, BAL_C.z + 160), 300000, 120, BAL_C)
    area((BAL_C.x + 160, BAL_C.y - 80, BAL_C.z + 30), 50000, 100, BAL_C)
    area((BAL_C.x + 20, BAL_C.y + 150, BAL_C.z + 120), 80000, 100, BAL_C)
else:  # nummers: vijf kommetjes, genummerd eind boven, rechte rij
    for i, n in enumerate(['kom10', 'kom15', 'kom20', 'kom25', 'kom30']):
        o = load(n)
        bpy.context.view_layer.update()
        cs = [o.matrix_world @ Vector(c) for c in o.bound_box]
        cx = sum(c.x for c in cs) / 8; cy = sum(c.y for c in cs) / 8
        o.matrix_world = Matrix.Translation((i * 26, 0, 0)) @ Matrix.Rotation(math.pi, 4, 'Z') @ Matrix.Rotation(math.pi, 4, 'Y') @ Matrix.Translation((-cx, -cy, -o.dimensions.z))
        bpy.context.view_layer.update()
        if len(o.data.materials) < 2:
            o.data.materials.append(INKT)
        mw = o.matrix_world; top = max((mw @ v.co).z for v in o.data.vertices)
        for p in o.data.polygons:
            c = mw @ p.center
            if top - 3 < c.z < top - 0.01 and math.hypot(c.x - i * 26, c.y) < 9.3:
                p.material_index = 1
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.shade_auto_smooth(angle=math.radians(30))
    cam((52, -300, 260), (52, 0, 14), 88)
    area((-60, -120, 200), 150000, 140, (52, 0, 0))
    area((180, -40, 80), 40000, 100, (52, 0, 0))

w = bpy.data.worlds.new('w'); bpy.context.scene.world = w
w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.05, 0.04, 0.08, 1)
w.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.0
s = bpy.context.scene
s.render.film_transparent = True
s.render.engine = 'CYCLES'; s.cycles.device = 'CPU'
s.cycles.samples = samples; s.cycles.use_denoising = True
s.render.resolution_x, s.render.resolution_y = {'doorsnede': (1400, 1400), 'zoom': (900, 900), 'nummers': (1600, 560)}[modus]
if samples < 16:
    s.render.resolution_percentage = 50
s.view_settings.view_transform = 'AgX'
s.view_settings.look = 'AgX - Medium High Contrast'
s.render.filepath = out
bpy.ops.render.render(write_still=True)
