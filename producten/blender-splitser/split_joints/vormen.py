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


def label_frame(as_, teken, richting=None):
    """3x3 frame (right, up, normal) for a label on a face whose outward normal is teken * axis as_.
    Text reads normally when you look at the face from outside. richting: direction of the text line
    (along a thin face); it is flipped if needed so the text is never upside down or mirrored."""
    n = Vector((0.0, 0.0, 0.0))
    n[as_] = float(teken)
    op = Vector((0.0, 0.0, 1.0)) if as_ != 2 else Vector((0.0, 1.0, 0.0))
    rechts = op.cross(n)
    if richting is not None:
        r = Vector(richting)
        r = (r - n * r.dot(n)).normalized()
        if r.length > 0.5:
            if r.dot(rechts) < 0:
                r = -r
            rechts = r
            op = n.cross(rechts)
    return Matrix((rechts, op, n)).transposed()


# Pixel font, 3 x 5 cells per character (rows from the top). Straight edges only: prints clean at 0.4 mm and
# gives the Booleans no tiny curves (the built-in font's "4" left open edges with Exact in 4.2, runs
# 45212458120 and 45214379786). No two cells touch only at a corner, so the mesh stays manifold.
PIXELS = {
    "0": ("111", "101", "101", "101", "111"), "1": ("010", "110", "010", "010", "111"),
    "2": ("111", "001", "111", "100", "111"), "3": ("111", "001", "111", "001", "111"),
    "4": ("101", "101", "111", "001", "001"), "5": ("111", "100", "111", "001", "111"),
    "6": ("111", "100", "111", "101", "111"), "7": ("111", "001", "001", "001", "001"),
    "8": ("111", "101", "111", "101", "111"), "9": ("111", "101", "111", "001", "111"),
    "-": ("000", "000", "111", "000", "000"),
}


def label_cellen(tekst):
    """Filled cells (column, row from the bottom) of the text, 4 columns per character (one empty)."""
    cellen = set()
    for i, teken in enumerate(tekst):
        for r, rij in enumerate(PIXELS.get(teken, PIXELS["-"])):
            for c, vol in enumerate(rij):
                if vol == "1":
                    cellen.add((4 * i + c, 4 - r))
    return cellen


def label_mesh(tekst, h, diepte, punt, as_, teken, u, max_breedte=None, richting=None):
    """Closed mesh of the label text (pixel font), h mm high, from 0.2 mm outside the face to diepte mm
    inside, centered on punt (mm). Returns (mesh, width mm) or (None, 0) for an empty text."""
    cellen = label_cellen(tekst)
    if not cellen:
        return None, 0.0
    px = h / 5.0
    kolommen = 4 * len(tekst) - 1
    if max_breedte and kolommen * px > max_breedte:
        px = max_breedte / kolommen
    bm = bmesh.new()
    punten = {}

    def p(c, r):
        if (c, r) not in punten:
            punten[(c, r)] = bm.verts.new(((c - kolommen / 2.0) * px, (r - 2.5) * px, 0.2))
        return punten[(c, r)]

    vlakken = [bm.faces.new((p(c, r), p(c + 1, r), p(c + 1, r + 1), p(c, r + 1))) for c, r in sorted(cellen)]
    uit = bmesh.ops.extrude_face_region(bm, geom=vlakken, use_keep_orig=True)  # keep the top: closed slab
    nieuw = [g for g in uit["geom"] if isinstance(g, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=nieuw, vec=(0.0, 0.0, -(diepte + 0.2)))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    frame = label_frame(as_, teken, richting).to_4x4()
    bm.transform(Matrix.Scale(u, 4) @ Matrix.Translation(Vector(punt)) @ frame)
    me = bpy.data.meshes.new("sj_label")
    bm.to_mesh(me)
    bm.free()
    return me, kolommen * px
