# Render van het kogelpaar voor Printables in Blender zelf (Bram, 27 nov, #257, M1 van Daan #267).
# Vervangt de oude matplotlib-render (die gaf streepjes en gaten door de tekenvolgorde).
# Draaien: pip install bpy==5.3.0, dan vanuit de repo-root:
#   python3 producten/blender-gewrichten/vindbaar/render_kogelpaar.py
import math, bpy, mathutils

TP = "commercie/blender-click-joints/testprint/"
UIT = "producten/blender-gewrichten/vindbaar/printables-kogelpaar.png"

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene

mat = bpy.data.materials.new("PLA")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.85, 0.32, 0.06, 1)
bsdf.inputs["Roughness"].default_value = 0.42

def laad(naam, remesh):
    bpy.ops.wm.stl_import(filepath=TP + naam)
    ob = bpy.context.selected_objects[0]
    ob.data.materials.append(mat)
    # mm naar Blender-eenheden: alles in mm laten, camera past zich aan
    bpy.context.view_layer.objects.active = ob
    # Alleen voor het beeld: fijne voxel-remesh (0,12 mm) zodat de lange smalle driehoeken van de
    # boolean-snede geen gekartelde schaduw geven. Vorm blijft binnen ±0,1 mm van de STL.
    # Alleen bij deel B: bij deel A is de rand van de kom dunner dan een voxel en zou hij rafelen;
    # deel A is met zijn eigen driehoeken al schoon.
    if remesh:
        rm = ob.modifiers.new('remesh', 'REMESH'); rm.mode = 'VOXEL'; rm.voxel_size = 0.12; rm.adaptivity = 0.0
        bpy.ops.object.modifier_apply(modifier='remesh')
    bpy.ops.object.shade_smooth_by_angle(angle=math.radians(50 if remesh else 35))
    return ob

a = laad("kogel-deel-A.stl", False)
b = laad("kogel-deel-B.stl", True)
b.rotation_euler = (math.pi, 0, 0)
bpy.context.view_layer.update()
for ob, x in ((a, -17.0), (b, 17.0)):
    bb = [ob.matrix_world @ mathutils.Vector(c) for c in ob.bound_box]
    mx = sum(v.x for v in bb) / 8; my = sum(v.y for v in bb) / 8; mz = min(v.z for v in bb)
    ob.location.x += x - mx; ob.location.y -= my; ob.location.z -= mz

# vloer
bpy.ops.mesh.primitive_plane_add(size=600)
vloer = bpy.context.object
vm = bpy.data.materials.new("vloer"); vm.use_nodes = True
vm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.05, 0.05, 0.055, 1)
vm.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.6
vloer.data.materials.append(vm)

# licht
w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs["Color"].default_value = (0.03, 0.03, 0.035, 1)
w.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0
def lamp(naam, loc, energie, grootte):
    l = bpy.data.lights.new(naam, "AREA"); l.energy = energie; l.size = grootte
    o = bpy.data.objects.new(naam, l); sc.collection.objects.link(o); o.location = loc
    d = mathutils.Vector((0, 0, 18)) - o.location
    o.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
lamp("hoofd", (-70, -90, 120), 90000, 80)
lamp("vul", (110, -40, 50), 25000, 60)
lamp("rand", (0, 120, 80), 40000, 50)

cam = bpy.data.cameras.new("cam"); cam.lens = 85
co = bpy.data.objects.new("cam", cam); sc.collection.objects.link(co); sc.camera = co
co.location = (0, -205, 150)
d = mathutils.Vector((0, 0, 20)) - co.location
co.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()

sc.render.engine = "CYCLES"
sc.cycles.samples = 64
sc.cycles.use_denoising = True
sc.cycles.device = "CPU"
sc.render.resolution_x, sc.render.resolution_y = 2400, 1350
sc.view_settings.view_transform = "AgX"
sc.render.filepath = UIT
bpy.ops.render.render(write_still=True)
print(UIT)
