"""Test models in a scene with 1 unit = 1 mm. Free licenses only:
- Suzanne: Blender's own monkey (bmesh.ops.create_monkey), scaled to 330 mm wide.
- Vase: GlassAlpha from GlassVaseFlowers (KhronosGroup glTF-Sample-Assets, CC0 1.0, Eric Chadwick), 600 mm high
  (a floor vase; the glass wall is then about 6.5 mm, at 320 mm it was 3.5 mm: too thin for any pin).
- Skull: ScatteringSkull (KhronosGroup glTF-Sample-Assets, CC0 1.0, Vladimir Petkovic), 300 mm long.
- Tube: a thin tube (2 mm wall) for the "too small for a pin" message.
Every model is made watertight with the add-on's own Make watertight (voxel remesh) before the split."""
import math

import bmesh
import bpy
from mathutils import Matrix, Vector


def mm_scene():
    """Empties the current scene (read_factory_settings would switch the add-on off) and sets 1 unit = 1 mm."""
    s = bpy.context.scene
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    for col in list(bpy.data.collections):
        bpy.data.collections.remove(col)
    for me in list(bpy.data.meshes):
        if me.users == 0:
            bpy.data.meshes.remove(me)
    s.split_joints.bron = ""
    s.split_joints.meldingen = ""
    s.unit_settings.system = "METRIC"
    s.unit_settings.scale_length = 0.001
    s.unit_settings.length_unit = "MILLIMETERS"
    return s


def _object(naam, bm):
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def schaal_naar(ob, as_, mm):
    """Scales the object (applied to the mesh) so its size along as_ is mm, standing on z = 0, centered."""
    me = ob.data
    me.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    xs = [v.co for v in me.vertices]
    lo = Vector([min(p[i] for p in xs) for i in range(3)])
    hi = Vector([max(p[i] for p in xs) for i in range(3)])
    f = mm / (hi[as_] - lo[as_])
    midden = (lo + hi) / 2
    me.transform(Matrix.Translation((0, 0, -lo.z * f)) @ Matrix.Scale(f, 4)
                 @ Matrix.Translation((-midden.x, -midden.y, 0)))
    me.update()
    return ob


def actief(ob):
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        if o is not None:
            o.select_set(False)
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob


def waterdicht(ob, voxel):
    """Make watertight with the add-on; returns the new object."""
    actief(ob)
    bpy.context.scene.split_joints.voxel_mm = voxel
    r = bpy.ops.split_joints.maak_gesloten()
    nieuw = bpy.context.view_layer.objects.active
    print(f"[sj-e2e] waterdicht {ob.name}: {r} -> {nieuw.name} {len(nieuw.data.polygons)} vlakken", flush=True)
    return nieuw


def suzanne():
    bm = bmesh.new()
    bmesh.ops.create_monkey(bm)
    ob = _object("Suzanne", bm)
    sub = ob.modifiers.new("sub", "SUBSURF")
    sub.levels = 1
    schaal_naar(ob, 0, 330.0)
    return waterdicht(ob, 2.5)


def gltf(pad, naam_bevat):
    voor = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=pad)
    nieuw = [o for o in bpy.data.objects if o not in voor and o.type == "MESH"]
    kies = [o for o in nieuw if naam_bevat.lower() in o.name.lower()] or nieuw
    ob = max(kies, key=lambda o: len(o.data.vertices))
    for o in nieuw:
        if o is not ob:
            bpy.data.objects.remove(o)
    mw = ob.matrix_world.copy()
    ob.parent = None
    ob.matrix_world = mw
    return ob


def vaas(pad):
    ob = gltf(pad, "GlassAlpha")
    schaal_naar(ob, 2, 600.0)
    return waterdicht(ob, 2.0)


def schedel(pad):
    ob = gltf(pad, "")
    schaal_naar(ob, 1, 300.0)
    return waterdicht(ob, 2.0)


def buis():
    """Tube 60 mm across, 2 mm wall, 300 mm high: the cut face is too thin for any pin."""
    bm = bmesh.new()
    n = 96
    ringen = []
    for r in (30.0, 28.0):
        for z in (0.0, 300.0):
            ringen.append([bm.verts.new((r * math.cos(2 * math.pi * k / n), r * math.sin(2 * math.pi * k / n), z))
                           for k in range(n)])
    ob_, ot, ib, it = ringen
    for k in range(n):
        j = (k + 1) % n
        bm.faces.new((ob_[k], ob_[j], ot[j], ot[k]))
        bm.faces.new((ib[k], it[k], it[j], ib[j]))
        bm.faces.new((ot[k], ot[j], it[j], it[k]))
        bm.faces.new((ob_[k], ib[k], ib[j], ob_[j]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _object("Tube", bm)
