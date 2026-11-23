"""Shapes for the cut: box for a cell, hole cylinder, pin with chamfers, engraved label text.

Everything is built in millimeters and then scaled with u (Blender units per mm)."""
import math

import bmesh
import bpy
from mathutils import Matrix, Vector

SEGMENTEN = 32
AFSCHUINING_MM = 0.4  # chamfer on both ends of a pin, so it slides in easily


def _object(naam, bm, collectie):
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    collectie.objects.link(ob)
    return ob


def doos(naam, mn, mx, u, collectie):
    """Axis aligned box from mn to mx (mm)."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector(((mx[i] if v.co[i] > 0 else mn[i]) * u for i in range(3)))
    return _object(naam, bm, collectie)


def as_matrix(as_):
    """Rotation that turns local Z into world axis as_ (0, 1, 2)."""
    if as_ == 0:
        return Matrix.Rotation(math.pi / 2, 4, "Y")
    if as_ == 1:
        return Matrix.Rotation(-math.pi / 2, 4, "X")
    return Matrix.Identity(4)


def gat_bmesh(bm, punt, as_, r_vlak, diepte, u):
    """Adds a closed hole cylinder to bm: its flat sides are r_vlak (mm) from the axis (so the narrowest
    point of the hole is exactly r_vlak), from -diepte to +diepte along world axis as_ around punt (mm)."""
    r_punt = r_vlak / math.cos(math.pi / SEGMENTEN)
    tijdelijk = bmesh.new()
    bmesh.ops.create_cone(tijdelijk, cap_ends=True, segments=SEGMENTEN, radius1=r_punt, radius2=r_punt,
                          depth=2 * diepte)
    m = Matrix.Scale(u, 4) @ Matrix.Translation(Vector(punt)) @ as_matrix(as_)
    tijdelijk.transform(m)
    me = bpy.data.meshes.new("sj_tmp")
    tijdelijk.to_mesh(me)
    tijdelijk.free()
    bm.from_mesh(me)
    bpy.data.meshes.remove(me)


def pen_bmesh(bm, voet, d, lengte, u):
    """Adds a standing pin (diameter d at its corners, length, chamfered ends) with its foot at voet (mm)."""
    r = d / 2.0
    c = min(AFSCHUINING_MM, r * 0.3, lengte * 0.2)
    ringen = [(0.0, r - c), (c, r), (lengte - c, r), (lengte, r - c)]
    nieuw = bmesh.new()
    lussen = []
    for z, rr in ringen:
        lussen.append([nieuw.verts.new((rr * math.cos(2 * math.pi * k / SEGMENTEN),
                                        rr * math.sin(2 * math.pi * k / SEGMENTEN), z)) for k in range(SEGMENTEN)])
    for a, b in zip(lussen, lussen[1:]):
        for k in range(SEGMENTEN):
            k2 = (k + 1) % SEGMENTEN
            nieuw.faces.new((a[k], a[k2], b[k2], b[k]))
    nieuw.faces.new(list(reversed(lussen[0])))
    nieuw.faces.new(lussen[-1])
    nieuw.transform(Matrix.Scale(u, 4) @ Matrix.Translation(Vector(voet)))
    me = bpy.data.meshes.new("sj_tmp")
    nieuw.to_mesh(me)
    nieuw.free()
    bm.from_mesh(me)
    bpy.data.meshes.remove(me)


def label_frame(as_, teken):
    """3x3 frame (right, up, normal) for a label on a face whose outward normal is teken * axis as_.
    Text reads normally when you look at the face from outside."""
    n = Vector((0.0, 0.0, 0.0))
    n[as_] = float(teken)
    op = Vector((0.0, 0.0, 1.0)) if as_ != 2 else Vector((0.0, 1.0, 0.0))
    rechts = op.cross(n)
    return Matrix((rechts, op, n)).transposed()


def label_mesh(tekst, h, diepte, punt, as_, teken, u, max_breedte=None):
    """Closed mesh of the label text, h mm high, from 0.2 mm outside the face to diepte mm inside, centered
    on punt (mm). Returns (mesh, width mm) or (None, 0) if Blender could not make a closed text mesh."""
    cu = bpy.data.curves.new("sj_label", "FONT")
    cu.body = tekst
    if cu.font is None:
        cu.font = bpy.data.fonts.load("<builtin>")
    cu.size = h
    cu.extrude = (diepte + 0.2) / 2.0
    cu.align_x, cu.align_y = "CENTER", "CENTER"
    ob = bpy.data.objects.new("sj_label", cu)
    bpy.context.scene.collection.objects.link(ob)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    bpy.data.objects.remove(ob)
    bpy.data.curves.remove(cu)
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    if not bm.verts:
        bm.free()
        bpy.data.meshes.remove(me)
        return None, 0.0
    xs = [v.co.x for v in bm.verts]
    ys = [v.co.y for v in bm.verts]
    breedte = max(xs) - min(xs)
    schaal = 1.0
    if max_breedte and breedte > max_breedte:
        schaal = max_breedte / breedte
    midden = Vector(((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2, (diepte - 0.2) / 2.0))  # z: -diepte..0.2
    bm.transform(Matrix.Translation(-midden))
    bm.transform(Matrix.Diagonal((schaal, schaal, 1.0, 1.0)))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    frame = label_frame(as_, teken).to_4x4()
    bm.transform(Matrix.Scale(u, 4) @ Matrix.Translation(Vector(punt)) @ frame)
    bm.to_mesh(me)
    bm.free()
    return me, breedte * schaal
