"""Measurements for the e2e test, independent of the add-on: everything measured on the meshes and files."""
import json
import math
import os
import struct
import zipfile

import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

fouten = []


def log(t):
    print(f"[sj-e2e] {t}", flush=True)


def stap(naam, ok, extra=""):
    log(f"{'OK  ' if ok else 'FOUT'} {naam} {extra}")
    if not ok:
        fouten.append(naam)
    return ok


def as_vec(a):
    v = Vector((0.0, 0.0, 0.0))
    v[a] = 1.0
    return v


def maat(ob):
    """Size in mm of the mesh in world coordinates without the exploded view (scene in mm)."""
    ps = [v.co for v in ob.data.vertices]
    return [max(p[i] for p in ps) - min(p[i] for p in ps) for i in range(3)]


def past(m, bed):
    return all(a <= b + 1e-6 for a, b in zip(sorted(m), sorted(bed)))


def dicht(ob):
    """(watertight, bad edges, volume) measured with bmesh."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    slecht = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = bm.calc_volume(signed=True)
    bm.free()
    return slecht == 0 and vol > 0, slecht, vol


def boom(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    b = BVHTree.FromBMesh(bm)
    bm.free()
    return b


def gat_maten(ob, g):
    """(smallest radius, depth) of one hole, measured with rays in the finished piece."""
    b = boom(ob)
    n = as_vec(g["as"])
    richting = -n * g["teken"]
    p = Vector(g["p"])
    e1, e2 = as_vec((g["as"] + 1) % 3), as_vec((g["as"] + 2) % 3)
    straal = math.inf
    for z in (0.25, 0.5, 0.75):
        midden = p + richting * (g["diepte"] * z)
        for k in range(64):
            hoek = 2 * math.pi * (k + 0.5) / 64
            d = e1 * math.cos(hoek) + e2 * math.sin(hoek)
            hit = b.ray_cast(midden, d, 50.0)
            if hit[0] is None:
                return None, None
            straal = min(straal, hit[3])
    hit = b.ray_cast(p + richting * 0.01, richting, 200.0)
    diepte = hit[3] + 0.01 if hit[0] is not None else None
    return straal, diepte


def pennen(ob):
    """Per loose pin: (largest radius from its axis, length)."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.verts.ensure_lookup_table()
    gezien, uit = set(), []
    for v0 in bm.verts:
        if v0.index in gezien:
            continue
        groep, rij = [], [v0]
        gezien.add(v0.index)
        while rij:
            v = rij.pop()
            groep.append(v.co.copy())
            for e in v.link_edges:
                w = e.other_vert(v)
                if w.index not in gezien:
                    gezien.add(w.index)
                    rij.append(w)
        cx = (max(p.x for p in groep) + min(p.x for p in groep)) / 2
        cy = (max(p.y for p in groep) + min(p.y for p in groep)) / 2
        r = max(math.hypot(p.x - cx, p.y - cy) for p in groep)
        lengte = max(p.z for p in groep) - min(p.z for p in groep)
        uit.append((r, lengte))
    bm.free()
    return uit


def label_punten(ob, lb, diepte):
    """Number of vertices of the piece at the bottom of the engraved number (depth +-0.02 mm) near its spot."""
    n = as_vec(lb["as"])
    p = Vector(lb["p"])
    binnen = -n * lb["teken"]
    straal = lb["h"] * max(1, len(lb["tekst"]))
    teller = 0
    for v in ob.data.vertices:
        d = v.co - p
        z = d.dot(binnen)
        vlak = (d - binnen * z).length
        if abs(z - diepte) < 0.02 and vlak < straal:
            teller += 1
    return teller


def lees_stl(pad):
    with open(pad, "rb") as f:
        data = f.read()
    n = struct.unpack("<I", data[80:84])[0]
    ps = []
    for i in range(n):
        vals = struct.unpack("<12f", data[84 + 50 * i:84 + 50 * i + 48])
        ps += [vals[3:6], vals[6:9], vals[9:12]]
    m = [max(p[i] for p in ps) - min(p[i] for p in ps) for i in range(3)] if ps else [0, 0, 0]
    return n, m, len(data) == 84 + 50 * n


def lees_3mf(pad):
    with zipfile.ZipFile(pad) as z:
        namen = set(z.namelist())
        model = z.read("3D/3dmodel.model").decode()
    return {"delen": {"[Content_Types].xml", "_rels/.rels", "3D/3dmodel.model"} <= namen,
            "mm": 'unit="millimeter"' in model, "driehoeken": model.count("<triangle ")}


def gaten(ob):
    return json.loads(ob.get("sj_gaten", "[]"))


def labels(ob):
    return json.loads(ob.get("sj_labels", "[]"))


def stukken():
    return sorted((o for o in bpy.context.scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])


def pen_objecten():
    return [o for o in bpy.context.scene.objects if o.get("sj_pennen")]


def bestaat(pad):
    return os.path.exists(pad) and os.path.getsize(pad) > 84
