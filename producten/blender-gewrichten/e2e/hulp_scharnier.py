"""Gedeelde hulp voor de scharnier-toetsen (toetsen_scharnier, toetsen_kijk, toetsen_flip, toetsen_neus)."""
from mathutils import Matrix
from mathutils.bvhtree import BVHTree

import bpy


def bvh(ob):
    me = ob.data
    punten = [ob.matrix_world @ v.co for v in me.vertices]
    return BVHTree.FromPolygons(punten, [tuple(p.vertices) for p in me.polygons])


def cursor(punt, x, y, z):
    m = Matrix.Identity(4)
    for i, v in enumerate((x, y, z)):
        m.col[i][:3] = v
    m.col[3][:3] = punt
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m
