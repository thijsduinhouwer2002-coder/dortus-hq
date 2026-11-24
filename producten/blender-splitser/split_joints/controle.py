"""Check per piece: fits the bed, watertight, wall around the pin holes. Colors the piece.

green: fits, watertight and every hole has at least the minimum wall.
orange: fits and watertight, but a hole has less wall than asked (still 0.8 mm or more).
red: does not fit the bed, is not watertight, or a hole has less than 0.8 mm wall."""
import json
import math

import bmesh
import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

from . import printers
from .gesloten import foute_randen, volume
from .verbind_3d import as_vec, segment_afstand

# linear values: Blender shows (1.0, 0.26, 0.0) as orange (255, 139, 0) on screen (keuring 24 nov, M1)
KLEUREN = {"groen": (0.0, 0.84, 0.59, 1.0), "oranje": (1.0, 0.26, 0.0, 1.0), "rood": (1.0, 0.03, 0.03, 1.0)}
NAMEN = {"groen": "green", "oranje": "orange", "rood": "red"}
ROOD_WAND_MM = 0.8


def materiaal(status):
    naam = f"Click Cuts {NAMEN[status]}"
    mat = bpy.data.materials.get(naam)
    if mat is None:
        mat = bpy.data.materials.new(naam)
        mat.use_nodes = True
    # always set: a .blend saved with an older version keeps its old colour otherwise (keuring 24 nov, kan)
    mat.diffuse_color = KLEUREN[status]
    bsdf = mat.node_tree.nodes.get("Principled BSDF") if mat.node_tree else None
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = KLEUREN[status]
    return mat


def kleur(ob, status):
    ob.data.materials.clear()
    ob.data.materials.append(materiaal(status))
    for p in ob.data.polygons:
        p.material_index = 0
    ob.color = KLEUREN[status]
    ob["sj_status"] = status


def maat_mm(ob, u):
    co = np.empty(len(ob.data.vertices) * 3)
    ob.data.vertices.foreach_get("co", co)
    p = co.reshape(-1, 3) / u
    if len(p) == 0:
        return (0.0, 0.0, 0.0)
    return tuple(float(v) for v in (p.max(axis=0) - p.min(axis=0)))


def volume_mm3(ob, u):
    return float(volume(ob.data) / (u ** 3))


def vlakken_op(me, n, c, u):
    """Indices of the faces whose points all lie within 0.001 mm of the plane co . n = c (mm), with numpy
    (the loop over the bmesh faces took 2.5 s per piece on 1M polygons, speed test 24 nov)."""
    if not me.polygons:
        return np.zeros(0, dtype=np.int64)
    co = np.empty(len(me.vertices) * 3)
    me.vertices.foreach_get("co", co)
    op = np.abs(co.reshape(-1, 3) / u @ np.array(n[:]) - c) < 1e-3
    vi = np.empty(len(me.loops), dtype=np.int64)
    me.loops.foreach_get("vertex_index", vi)
    start = np.empty(len(me.polygons), dtype=np.int64)
    me.polygons.foreach_get("loop_start", start)
    # reduceat needs rising loop_start values: Blender 4.x and 5.x store the face loops in order
    alle = np.minimum.reduceat(op[vi].astype(np.int8), start)
    return np.flatnonzero(alle)


def bvh_mm(ob, u, zonder_vlak=None):
    """BVH of the mesh in mm. zonder_vlak=(axis, position mm): leave out the faces that lie on that plane
    (the cut face a hole opens onto, which would otherwise be the nearest surface)."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.transform(Matrix.Scale(1.0 / u, 4))
    if zonder_vlak is not None:
        a, c = zonder_vlak
        n = as_vec(a) if isinstance(a, int) else Vector(a)  # a world axis, or the normal of a free cut
        weg = vlakken_op(ob.data, n, c, u)
        if weg.size:
            bm.faces.ensure_lookup_table()
            bmesh.ops.delete(bm, geom=[bm.faces[i] for i in weg.tolist()], context="FACES_ONLY")
    boom = BVHTree.FromBMesh(bm)
    bm.free()
    return boom


def gat_assen(g):
    """(axis, e1, e2) of a hole: along a world axis ("as"), or along the normal "n" of a free cut."""
    if "n" in g:
        n = Vector(g["n"]).normalized()
        e1 = n.orthogonal().normalized()
        return n, e1, n.cross(e1)
    return as_vec(g["as"]), as_vec((g["as"] + 1) % 3), as_vec((g["as"] + 2) % 3)


def status_uit(past, dicht, wand, wand_min):
    """green, orange or red from the measurements (same rule as keur)."""
    if not past or not dicht or (wand is not None and wand < ROOD_WAND_MM):
        return "rood"
    if wand is not None and wand < wand_min - 0.05:
        return "oranje"
    return "groen"


def wand_rond_gaten(ruw, gaten, u):
    """Smallest wall (mm) around the holes of one piece: from the hole wall and the hole bottom to the
    outside of the piece before the holes were cut (without the cut face the hole opens onto), and between
    the holes themselves. None without holes."""
    if not gaten:
        return None
    bomen = {}
    kleinste = math.inf
    for g in gaten:
        n, e1, e2 = gat_assen(g)
        vlak = (g["as"], g["snede"]) if "n" not in g else (tuple(g["n"]), float(n.dot(Vector(g["p"]))))
        sleutel = (tuple(round(x, 4) for x in n), round(vlak[1], 4))
        if sleutel not in bomen:
            bomen[sleutel] = bvh_mm(ruw, u, vlak)
        boom = bomen[sleutel]
        richting = -n * g["teken"]  # into this piece
        p = Vector(g["p"])
        for z in np.linspace(0.0, g["diepte"], 6):
            for k in range(16):
                hoek = 2 * math.pi * k / 16
                q = p + richting * float(z) + (e1 * math.cos(hoek) + e2 * math.sin(hoek)) * g["r_gat"]
                co, _n, _i, afstand = boom.find_nearest(q)
                if co is not None:
                    kleinste = min(kleinste, afstand)
        bodem = p + richting * g["diepte"]
        co, _n, _i, afstand = boom.find_nearest(bodem)
        if co is not None:
            kleinste = min(kleinste, afstand)
    for i, g in enumerate(gaten):
        for h in gaten[i + 1:]:
            a1 = Vector(g["p"]) - gat_assen(g)[0] * g["diepte"]
            b1 = Vector(g["p"]) + gat_assen(g)[0] * g["diepte"]
            a2 = Vector(h["p"]) - gat_assen(h)[0] * h["diepte"]
            b2 = Vector(h["p"]) + gat_assen(h)[0] * h["diepte"]
            kleinste = min(kleinste, segment_afstand(a1, b1, a2, b2) - g["r_gat"] - h["r_gat"])
    return float(kleinste)


def keur(af, ruw, bed, u, wand_min):
    """Fills sj_maat_mm, sj_past, sj_gesloten, sj_foute_randen, sj_wand_mm, sj_status and the color."""
    maat = maat_mm(af, u)
    past = printers.past(maat, bed)
    fout = foute_randen(af.data)
    dicht = fout == 0 and len(af.data.polygons) > 0 and volume(af.data) > 0
    wand = wand_rond_gaten(ruw, json.loads(af.get("sj_gaten", "[]")), u)
    af["sj_maat_mm"] = [round(v, 2) for v in maat]
    af["sj_past"] = past
    af["sj_gesloten"] = dicht
    af["sj_foute_randen"] = fout
    af["sj_wand_mm"] = round(wand, 3) if wand is not None else -1.0
    af["sj_volume_mm3"] = volume_mm3(af, u)
    status = status_uit(past, dicht, wand, wand_min)
    kleur(af, status)
    return status


def tekst(ob):
    """Short line for the panel (the icon in front says green, orange or red): size, and what is wrong."""
    m = ob.get("sj_maat_mm", [0, 0, 0])
    delen = [f"{m[0]:.0f}x{m[1]:.0f}x{m[2]:.0f} mm"]
    if not ob.get("sj_past"):
        delen.append("too big")
    if not ob.get("sj_gesloten"):
        delen.append("not watertight")
    w = ob.get("sj_wand_mm", -1.0)
    if w is not None and w >= 0:
        delen.append(f"wall {w:.1f}")
    return ", ".join(delen)
