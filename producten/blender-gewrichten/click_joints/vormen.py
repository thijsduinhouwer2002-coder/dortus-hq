"""Hulpvormen (bol, cilinder, doos) als gesloten meshes, in een frame waarvan Z de gewrichtsas is."""
import math

import bmesh
import bpy
from mathutils import Matrix

SEGMENTEN = 64
# Polen van de bol dwars op de as en de cilinder een halve stap gedraaid,
# zodat er geen punten van kogel, nek en kom precies op elkaar vallen.
_DWARS = Matrix.Rotation(math.pi / 2, 4, "X")
_HALF = Matrix.Rotation(math.pi / SEGMENTEN, 4, "Z")


def _object(naam, bm, collectie):
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    collectie.objects.link(ob)
    return ob


def bol(naam, r, z, frame, collectie):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=SEGMENTEN, v_segments=SEGMENTEN // 2, radius=r)
    bm.transform(frame @ Matrix.Translation((0, 0, z)) @ _DWARS)
    return _object(naam, bm, collectie)


def cilinder(naam, r, z0, z1, frame, collectie):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=SEGMENTEN, radius1=r, radius2=r, depth=z1 - z0)
    bm.transform(frame @ Matrix.Translation((0, 0, (z0 + z1) / 2)) @ _HALF)
    return _object(naam, bm, collectie)


def doos(naam, half, z0, z1, frame, collectie):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x = half if v.co.x > 0 else -half
        v.co.y = half if v.co.y > 0 else -half
        v.co.z = z1 if v.co.z > 0 else z0
    bm.transform(frame)
    return _object(naam, bm, collectie)


def frame_voor(punt, as_richting):
    """Matrix met oorsprong op het punt en Z langs de as."""
    rot = as_richting.normalized().to_track_quat("Z", "Y").to_matrix().to_4x4()
    return Matrix.Translation(punt) @ rot


def kegel(naam, r0, r1, z0, z1, frame, collectie):
    """Afgeknotte kegel langs Z: straal r0 op hoogte z0, straal r1 op hoogte z1."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=SEGMENTEN, radius1=r0, radius2=r1, depth=z1 - z0)
    bm.transform(frame @ Matrix.Translation((0, 0, (z0 + z1) / 2)) @ _HALF)
    return _object(naam, bm, collectie)
