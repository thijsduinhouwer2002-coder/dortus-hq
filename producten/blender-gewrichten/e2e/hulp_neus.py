"""Gedeelde hulp voor de neus-toetsen (toetsen_neus, toetsen_neus_kort): staaf plaatsen, as uit de cursor,
neus meten in de mesh, losse stukken tellen en de melding zoals de operator."""
import bpy
from mathutils import Matrix, Vector

import figuren

TOL_MM = 0.01
KNOKKEL, WANG, ACHTER, ZAAG = 0.35, 0.20, 0.15, 0.65   # eigen rekensom (ontwerp v1.1, staaf rond)


def plaats(straal, cursor, s=0.2, onder=None):
    """Staaf langs X met de cursor in de oorsprong; onder = afstand van de cursor tot het uiteinde aan de kant
    van deel A (-X), anders de gewone 20 mm."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = s
    inst.as_bron = "CURSOR"
    staaf = figuren.staaf("staaf", straal)
    if onder is not None:
        staaf.data.transform(Matrix.Translation((20.0 - onder, 0, 0)))
    figuren.maak_actief(staaf)
    cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    return staaf


def as_uit_cursor(straal, u):
    """(punt op H, H, buigkant, lidas) uit de 3D-cursor: H = X-as, buigkant = Y-as, lidas = Z-as."""
    m = bpy.context.scene.cursor.matrix
    h, buig, lid = (m.col[i].xyz.normalized() for i in range(3))
    return m.to_translation() - buig * (ACHTER * 2 * straal * u), h, buig, lid


def meet_neus(a, b, straal, s, u):
    """Per kant (+H, -H): dict met tong, top, rho_top, wang (afstanden langs H in mm) en het toppunt."""
    p, h, buig, lid = as_uit_cursor(straal, u)
    r = KNOKKEL * straal * u
    rn = r + s * u + WANG * straal * u
    uit = {}
    for teken, kant in ((1, "+H"), (-1, "-H")):
        tong, top, beste = None, None, -1.0
        for v in b.data.vertices:
            d = b.matrix_world @ v.co - p
            x = d.dot(h) * teken
            if x <= 0:
                continue
            rho = (d - h * d.dot(h)).length
            if 0.7 * r < rho < r + 1e-4 * u:
                tong = x if tong is None else max(tong, x)
            elif rho <= 0.7 * r and x > beste:
                beste, top = x, d
        wang = None
        for v in a.data.vertices:
            d = a.matrix_world @ v.co - p
            x = d.dot(h) * teken
            rho = (d - h * d.dot(h)).length
            if x > 0 and d.dot(lid) > s * u and rho < rn - s * u / 2 + 1e-3 * u:
                wang = x if wang is None else min(wang, x)
        if tong is None or top is None or wang is None:
            uit[kant] = None
            continue
        uit[kant] = {"tong": tong / u, "top": beste / u, "wang": wang / u, "punt": p + top,
                     "rho_top": (top - h * top.dot(h)).length / u}
    return uit


def eilanden(ob):
    """Aantal losse stukken in de mesh (hoekpunten verbonden via randen)."""
    ouder = list(range(len(ob.data.vertices)))

    def wortel(i):
        while ouder[i] != i:
            ouder[i] = ouder[ouder[i]]
            i = ouder[i]
        return i
    for e in ob.data.edges:
        a, b = wortel(e.vertices[0]), wortel(e.vertices[1])
        if a != b:
            ouder[a] = b
    return len({wortel(i) for i in range(len(ouder))})

def reden(ops, vorm, neus, staaf, u):
    """Melding zoals de operator: maten, dan neus met de diepte tot de onderkant (zaag_diepte)."""
    from mathutils.bvhtree import BVHTree as _B
    import bmesh
    inst = bpy.context.scene.click_joints
    punt, h, buig, lid = ops.assen(bpy.context, inst)[:4]
    frame = vorm.frame_scharnier(punt, h, buig, lid)
    bm = bmesh.new()
    bm.from_mesh(staaf.data)
    bm.transform(staaf.matrix_world)
    bvh = _B.FromBMesh(bm)
    bm.free()
    maat, reden = vorm.maten(bvh, frame, inst.speling_mm * u, 115, u)
    if maat is not None:
        reden = neus.maten_neus(maat, u, neus.zaag_diepte(bvh, frame, maat))
    return reden
