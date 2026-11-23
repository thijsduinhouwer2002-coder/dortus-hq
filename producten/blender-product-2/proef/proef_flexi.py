"""Bouwproef Flexi Joints (run 2, 23 nov 2026): print-in-place scharnier tussen twee segmenten.

Draai: blender -b --factory-startup --python proef_flexi.py -- <uitmap>

Vorm per scharnier (punt J op de lijn, as Z = loodrecht op het printbed, ketting langs +X):
- Knokkel K (deel A): cilinder straal Rk in de middenband [z1, z2], met een kegel van 45 graden erop.
- Vork (deel B): de schijf Rk boven en onder de middenband (armen), min K met speling s eromheen (Ks).
- Wig: buiten de schijf horen de delen bij twee wiggen (A achter, B voor) met een spleet van alfa graden
  aan elke kant. Zodra B alfa graden draait, raken de vlakke wangen: dat is de eindstop.
A = lichaam ∩ ((WA - Cks buiten de middenband) ∪ K)   (WA in de middenband is de hals naar K)
B = lichaam ∩ ((WB ∪ Ck) - Ks)
Alle maten in mm. Toetsen: delen gesloten, delen raken elkaar niet, B draait vrij tot alfa en stopt daarna.
"""
import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

UIT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "/tmp/flexi"
os.makedirs(UIT, exist_ok=True)

S = 0.4        # speling
RK = 3.0       # straal knokkel
RT = 1.0       # straal plat bovenop de kegel
ALFA = 30.0    # buigbereik per kant in graden
Z1, Z2 = 2.0, 5.0
SEG = 64
GROOT = 200.0
SOLVER = "MANIFOLD" if bpy.app.version >= (4, 5, 0) else "EXACT"

uitslag = []


def meld(regel):
    print("FLEXI", regel)
    uitslag.append(regel)


def object_uit(naam, bm):
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def draai_profiel(naam, punten, m):
    """Omwentelingslichaam om Z uit een profiel [(r, z), ...] van as naar as."""
    bm = bmesh.new()
    ringen = []
    for i in range(SEG):
        hoek = 2 * math.pi * (i + 0.5) / SEG
        c, s_ = math.cos(hoek), math.sin(hoek)
        ringen.append([bm.verts.new((r * c, r * s_, z)) for r, z in punten[1:-1]])
    onder = bm.verts.new((0, 0, punten[0][1]))
    boven = bm.verts.new((0, 0, punten[-1][1]))
    n = len(punten) - 2
    for i in range(SEG):
        a, b = ringen[i], ringen[(i + 1) % SEG]
        bm.faces.new((onder, b[0], a[0]))
        for k in range(n - 1):
            bm.faces.new((a[k], b[k], b[k + 1], a[k + 1]))
        bm.faces.new((a[-1], b[-1], boven))
    bm.normal_update()
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.transform(m)
    return object_uit(naam, bm)


def prisma(naam, punten2d, z0, z1, m):
    bm = bmesh.new()
    o = [bm.verts.new((x, y, z0)) for x, y in punten2d]
    b = [bm.verts.new((x, y, z1)) for x, y in punten2d]
    n = len(punten2d)
    bm.faces.new(list(reversed(o)))
    bm.faces.new(b)
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((o[i], o[j], b[j], b[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.transform(m)
    return object_uit(naam, bm)


def wig(naam, kant, z0, z1, m):
    """Wig A (kant -1, achter) of B (kant +1, voor), punt iets van J af zodat de spleet bij J ook S is."""
    # Punt precies op J: dan raken de wangen precies bij ALFA. De spleet bij J is smaller dan S,
    # maar daar ligt de schijf Cks (straal RK + S) al overheen; op die straal is de spleet ALFA * (RK + S).
    d = 0.0
    h = math.radians(90 + ALFA / 2) if kant < 0 else math.radians(90 - ALFA / 2)
    px = -d if kant < 0 else d
    p1 = (px + GROOT * math.cos(h), GROOT * math.sin(h))
    p2 = (px + GROOT * math.cos(-h), GROOT * math.sin(-h))
    ver = (kant * GROOT, GROOT), (kant * GROOT, -GROOT)
    pts = [(px, 0), p1, ver[0], ver[1], p2] if kant > 0 else [(px, 0), p2, ver[1], ver[0], p1]
    # pts moet tegen de klok in; prisma rekent de normalen zelf na.
    return prisma(naam, pts, z0, z1, m)


def boolean(doel, gereedschap, actie):
    mod = doel.modifiers.new(actie, "BOOLEAN")
    mod.operation = actie
    mod.object = gereedschap
    mod.solver = SOLVER
    if SOLVER == "EXACT":
        mod.use_self = False
        mod.use_hole_tolerant = False
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(doel.evaluated_get(dg))
    doel.modifiers.clear()
    oud = doel.data
    doel.data = me
    bpy.data.meshes.remove(oud)
    return doel


def kopie(ob, naam):
    nieuw = ob.copy()
    nieuw.data = ob.data.copy()
    nieuw.name = naam
    bpy.context.scene.collection.objects.link(nieuw)
    return nieuw


def weg(*obs):
    for ob in obs:
        me = ob.data
        bpy.data.objects.remove(ob)
        bpy.data.meshes.remove(me)


def snij(lichaam, m, naam):
    """Snijdt lichaam (wereldcoördinaten) bij frame m in deel A (achter) en B (voor)."""
    kegel_h = RK - RT
    k = draai_profiel("k", [(0, Z1), (RK, Z1), (RK, Z2), (RT, Z2 + kegel_h), (0, Z2 + kegel_h)], m)
    w2 = S * math.sqrt(2)
    ks = draai_profiel("ks", [(0, Z1 - S), (RK + S, Z1 - S), (RK + S, Z2 + w2 - S),
                              (RT + w2 - S, Z2 + kegel_h + S), (0, Z2 + kegel_h + S)], m)
    # Cks zonder de middenband: daar blijft WA staan als hals naar de knokkel. Twee losse cilinders
    # in plaats van "WA ∪ hals": die twee hadden dezelfde wangen en gaven T-naden (gemeten 23 nov).
    cks = draai_profiel("cks", [(0, -GROOT), (RK + S, -GROOT), (RK + S, Z1), (0, Z1)], m)
    cks2 = draai_profiel("cks2", [(0, Z2), (RK + S, Z2), (RK + S, GROOT), (0, GROOT)], m)
    ck = draai_profiel("ck", [(0, -GROOT), (RK, -GROOT), (RK, GROOT), (0, GROOT)], m)
    wa = wig("wa", -1, -GROOT, GROOT, m)
    wb = wig("wb", 1, -GROOT, GROOT, m)

    # Gereedschap A: (WA - Cks buiten de middenband) ∪ K
    boolean(wa, cks, "DIFFERENCE")
    boolean(wa, cks2, "DIFFERENCE")
    boolean(wa, k, "UNION")
    a = kopie(lichaam, naam + "_A")
    boolean(a, wa, "INTERSECT")
    # Deel B: (lichaam ∩ (WB ∪ Ck)) - Ks. Ks direct van het deel af, niet eerst van het gereedschap:
    # dat gaf bij de ronde buis in 4.2 open randen (gemeten 23 nov), bij de staaf niet.
    boolean(wb, ck, "UNION")
    b = kopie(lichaam, naam + "_B")
    boolean(b, wb, "INTERSECT")
    boolean(b, ks, "DIFFERENCE")
    weg(k, ks, cks, cks2, ck, wa, wb)
    for deel in (a, b):
        heel(deel)
    return a, b


def heel(ob):
    """Punten op minder dan 0,1 micron samen: de Exact-solver laat soms dubbele punten achter."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-5)
    bm.to_mesh(ob.data)
    bm.free()


def foute_randen(me, toon=False):
    tel = {}
    for p in me.polygons:
        for e in p.edge_keys:
            tel[e] = tel.get(e, 0) + 1
    fout = [(e, v) for e, v in tel.items() if v != 2]
    if toon:
        for e, v in fout[:8]:
            print("FLEXI-RAND", v, tuple(round(c, 3) for c in me.vertices[e[0]].co),
                  tuple(round(c, 3) for c in me.vertices[e[1]].co))
    return len(fout)


def volume(me):
    bm = bmesh.new()
    bm.from_mesh(me)
    v = bm.calc_volume(signed=True)
    bm.free()
    return v


def eilanden(me):
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.verts.ensure_lookup_table()
    gezien, n = set(), 0
    for v in bm.verts:
        if v.index in gezien:
            continue
        n += 1
        stapel = [v]
        while stapel:
            w = stapel.pop()
            if w.index in gezien:
                continue
            gezien.add(w.index)
            stapel.extend(e.other_vert(w) for e in w.link_edges)
    bm.free()
    return n


def bvh(ob, m=Matrix()):
    me = ob.data
    pts = [m @ v.co for v in me.vertices]
    return BVHTree.FromPolygons(pts, [tuple(p.vertices) for p in me.polygons]), pts


def raakt(a, b, m_b):
    ta, _ = bvh(a)
    tb, _ = bvh(b, m_b)
    return len(ta.overlap(tb))


def kleinste_afstand(a, b):
    ta, _ = bvh(a)
    beste = 1e9
    for v in b.data.vertices:
        hit = ta.find_nearest(v.co)
        if hit[0] is not None:
            beste = min(beste, hit[3])
    return beste


def draai_om(m, graden):
    j = m.translation
    as_ = m.col[2].xyz
    return Matrix.Translation(j) @ Matrix.Rotation(math.radians(graden), 4, as_) @ Matrix.Translation(-j)


def toets_paar(a, b, m, naam):
    goed = True
    for ob in (a, b):
        fr, vol, eil = foute_randen(ob.data, True), volume(ob.data), eilanden(ob.data)
        ok = fr == 0 and vol > 0 and eil == 1
        goed &= ok
        meld(f"{naam} {ob.name}: foute randen {fr}, volume {vol:.1f} mm3, eilanden {eil} {'OK' if ok else 'FOUT'}")
    rust = raakt(a, b, Matrix())
    afstand = kleinste_afstand(a, b)
    ok = rust == 0 and afstand >= 0.9 * S
    goed &= ok
    meld(f"{naam} rust: raakvlakken {rust}, kleinste afstand {afstand:.3f} mm {'OK' if ok else 'FOUT'}")
    for kant in (1, -1):
        vrij = raakt(a, b, draai_om(m, kant * (ALFA - 3)))
        stop = raakt(a, b, draai_om(m, kant * (ALFA + 3)))
        ok = vrij == 0 and stop > 0
        goed &= ok
        meld(f"{naam} draai {kant * (ALFA - 3):+.0f} graden: raakt {vrij}; {kant * (ALFA + 3):+.0f}: raakt {stop} "
             f"{'OK' if ok else 'FOUT'}")
    return goed


def lichaam_staaf():
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= 64
        v.co.y *= 12
        v.co.z = 10 if v.co.z > 0 else 0
    return object_uit("staaf", bm)


def lichaam_slang():
    """Ronde buis (straal 6) langs X, plat onderaan op het bed, hoogte 10: zoals een flexi-slang."""
    # boog van rechtsonder (z = 0) over de top naar linksonder, tegen de klok in
    begin = math.asin(-4 / 6)
    eind = math.pi - begin
    profiel = []
    for i in range(41):
        h = begin + (eind - begin) * i / 40
        profiel.append((6 * math.cos(h), 4 + 6 * math.sin(h)))
    profiel[0] = (profiel[0][0], 0.0)
    profiel[-1] = (profiel[-1][0], 0.0)
    # profiel in (y, z), extruderen langs X van -35 tot 35
    ob = prisma("slang", profiel, -35, 35, Matrix())
    m = Matrix(((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1)))  # (y, z, x) -> (x, y, z)
    ob.data.transform(m)
    ob.data.flip_normals() if volume(ob.data) < 0 else None
    return ob


def main():
    goed = True
    # Proef 1: een staaf, een scharnier in het midden.
    staaf = lichaam_staaf()
    m = Matrix.Translation((0, 0, 0))
    a, b = snij(staaf, m, "staaf")
    goed &= toets_paar(a, b, m, "staaf")

    # Proef 2: ketting van 5 segmenten uit een ronde buis (4 scharnieren om de 14 mm).
    slang = lichaam_slang()
    meld(f"slang zelf: foute randen {foute_randen(slang.data)}, volume {volume(slang.data):.1f}")
    rest = slang
    delen = []
    for i, x in enumerate((-21, -7, 7, 21)):
        mi = Matrix.Translation((x, 0, 0))
        a_i, b_i = snij(rest, mi, f"seg{i}")
        goed &= toets_paar(a_i, b_i, mi, f"ketting{i}")
        if rest is not slang:
            weg(rest)
        delen.append(a_i)
        rest = b_i
    delen.append(rest)
    slang.hide_set(True)
    staaf.hide_set(True)

    # Export: alle segmenten in één STL (één print).
    for ob in bpy.context.scene.objects:
        ob.select_set(ob in delen)
    pad = os.path.join(UIT, "flexi_ketting.stl")
    if hasattr(bpy.ops.wm, "stl_export"):
        bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True)
    else:
        bpy.ops.export_mesh.stl(filepath=pad, use_selection=True)
    meld(f"export {pad} {os.path.getsize(pad)} bytes")

    # Beeld: ketting in rust, daarachter met elk scharnier 25 graden gebogen, voor de staaf.
    gebogen = [kopie(d, d.name + "_buig") for d in delen]
    m_tot = Matrix()
    gebogen[0].matrix_world = Matrix.Translation((0, 22, 0))
    for i, x in enumerate((-21, -7, 7, 21)):
        m_tot = m_tot @ draai_om(Matrix.Translation((x, 0, 0)), 25)
        gebogen[i + 1].matrix_world = Matrix.Translation((0, 22, 0)) @ m_tot
    for ob in (a, b):
        ob.location = (0, -24, 0)
    # Doorsnede van de staaf bij y = 0 (alleen voor het beeld): knokkel, kegel en vork te zien.
    snede = []
    for ob in (a, b):
        c = kopie(ob, ob.name + "_snede")
        bm = bmesh.new()
        bm.from_mesh(c.data)
        bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0),
                               plane_no=(0, -1, 0), clear_outer=True)
        bm.to_mesh(c.data)
        bm.free()
        c.location = (0, -48, 0)
        snede.append(c)
    beeld(delen + gebogen + [a, b] + snede)

    meld("PROEF OK" if goed else "PROEF FOUT")
    with open(os.path.join(UIT, "uitslag.txt"), "w") as f:
        f.write("\n".join(uitslag) + "\n")


def beeld(obs):
    sc = bpy.context.scene
    mat = bpy.data.materials.new("plastic")
    mat.diffuse_color = (0.95, 0.55, 0.15, 1)
    for i, ob in enumerate(obs):
        ob.data.materials.clear()
        ob.data.materials.append(mat)
        ob.hide_set(False)
        ob.hide_render = False
    for ob in sc.objects:
        if ob not in obs:
            ob.hide_render = True
    cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam"))
    sc.collection.objects.link(cam)
    cam.location = (40, -150, 95)
    doel = bpy.data.objects.new("doel", None)
    sc.collection.objects.link(doel)
    doel.location = (8, -8, 0)
    volg = cam.constraints.new("TRACK_TO")
    volg.target = doel
    cam.data.lens = 50
    sc.camera = cam
    zon = bpy.data.objects.new("zon", bpy.data.lights.new("zon", "SUN"))
    zon.rotation_euler = (math.radians(40), math.radians(20), 0)
    zon.data.energy = 4
    sc.collection.objects.link(zon)
    sc.render.engine = "CYCLES"
    sc.cycles.samples = 24
    sc.cycles.device = "CPU"
    sc.render.resolution_x, sc.render.resolution_y = 1280, 900
    if sc.world is None:
        sc.world = bpy.data.worlds.new("w")
    sc.world.color = (0.8, 0.82, 0.86)
    sc.render.filepath = os.path.join(UIT, "flexi_proef.png")
    bpy.ops.render.render(write_still=True)
    meld(f"beeld {sc.render.filepath}")


main()
