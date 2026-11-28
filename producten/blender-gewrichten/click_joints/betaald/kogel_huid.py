"""Pro 1.2.10, issue 410: kogel na Shift + rechtsklik (cursor op de huid): naar het midden van het lid, as langs het lid.

Omhult gewricht.as_en_punt van de kern (zelfde manier als afstand.py en snippers.py): de gratis versie blijft
onveranderd. Alleen bij as-bron View direction met een 3D-weergave, en alleen als de cursor op de huid ligt
(cursor_lid.op_huid, binnen 0,5 mm). De uitleg komt in LAATSTE[0] en op de delen als cj_bijgesteld (via
gewricht.markeer), net als bij het scharnier."""
import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from ..eigenschappen import eenheid_per_mm
from ..gesloten import gespiegeld
from ..uit_elkaar import echte_matrix
from . import cursor_lid

_oud = [None]
_oud_markeer = [None]
LAATSTE = [""]


def _bvh(context):
    """(BVH van het actieve object in wereldcoordinaten zoals de operator hem bouwt, midden van zijn kader), of None."""
    ob = context.active_object
    if ob is None or ob.type != "MESH":
        return None
    dg = context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    try:
        me.transform(echte_matrix(ob))
        bm = bmesh.new()
        bm.from_mesh(me)
        if gespiegeld(ob):
            bmesh.ops.reverse_faces(bm, faces=bm.faces[:])
        if not bm.faces:
            bm.free()
            return None
        bvh = BVHTree.FromBMesh(bm)
        lo = [min(v.co[i] for v in bm.verts) for i in range(3)]
        hi = [max(v.co[i] for v in bm.verts) for i in range(3)]
        bm.free()
    finally:
        bpy.data.meshes.remove(me)
    return bvh, Vector([(a + b) / 2.0 for a, b in zip(lo, hi)])


def as_en_punt_huid(context, inst):
    LAATSTE[0] = ""
    punt, richting, bron = _oud[0](context, inst)
    if bron != "KIJK":
        return punt, richting, bron
    uit = _bvh(context)
    if uit is None:
        return punt, richting, bron
    nieuw, as_, wat = cursor_lid.kogel_bijstellen(uit[0], punt, richting, eenheid_per_mm(context.scene), uit[1])
    LAATSTE[0] = wat
    return nieuw, as_, bron


def _markeer(ob, kleur, gegevens, maat=None, u=1.0):
    if LAATSTE[0] and gegevens.get("cj_soort") == "KOGEL":
        gegevens["cj_bijgesteld"] = LAATSTE[0]
    return _oud_markeer[0](ob, kleur, gegevens, maat, u)


def register(gewricht):
    if _oud[0] is None:
        _oud[0] = gewricht.as_en_punt
        gewricht.as_en_punt = as_en_punt_huid
    if _oud_markeer[0] is None:
        _oud_markeer[0] = gewricht.markeer
        gewricht.markeer = _markeer


def unregister(gewricht):
    if _oud[0] is not None:
        if gewricht.as_en_punt is as_en_punt_huid:  # alleen terugzetten als het nog ons omhulsel is
            gewricht.as_en_punt = _oud[0]
        _oud[0] = None
    if _oud_markeer[0] is not None:
        if gewricht.markeer is _markeer:
            gewricht.markeer = _oud_markeer[0]
        _oud_markeer[0] = None
    LAATSTE[0] = ""
