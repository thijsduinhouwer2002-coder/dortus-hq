"""Toets klikneus van het scharnier (ontwerp betaald v1.1, eis 3), aangeroepen vanuit toetsen_scharnier.py.

Staaf van 10 mm (straal 5), stand 115, speling 0,2 mm, cursor als as-bron (zoals eis 1). Gemeten in de mesh
van deel B: punten op de neus zijn punten met |x| > tw (x langs H vanaf het draaipunt) binnen de knokkelstraal.
Hoogte = grootste |x| - tw, aan beide kanten; midden = afstand van de top tot H. Eisen: hoogte 0,25 mm en
midden op H, elk binnen 0,01 mm; rek van de add-on hoogstens 3% en gelijk aan een eigen rekensom
1,5 * t * h / L^2. Kuiltje in A: dichtste punt van A bij de top van de neus is de speling s (0,2 mm).
Dunne staaf van 5 mm (straal 2,5): CANCELLED met de te-dun- of Tight-melding en geen nieuwe objecten."""
import math
import sys

import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

import figuren

TOL_MM = 0.01


def _plaats(straal, cursor):
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = 0.2
    inst.as_bron = "CURSOR"
    staaf = figuren.staaf("staaf", straal)
    figuren.maak_actief(staaf)
    cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    return staaf


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    neus = sys.modules[eigen + ".betaald.scharnier_neus"]
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    _plaats(5.0, cursor)
    u = eig.eenheid_per_mm(bpy.context.scene)
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    stap("neus: scharnier op staaf 10 mm geplaatst", uitslag == {"FINISHED"} and a and b, str(uitslag))
    if not (a and b):
        return
    p = Vector(b["cj_scharnier_punt"])
    h_as = Vector(b["cj_scharnier_as"]).normalized()
    tw, r = float(b["cj_tong_half"]), float(b["cj_knokkel_r"])
    for teken, kant in ((1, "+H"), (-1, "-H")):
        top, beste = None, -1.0
        for v in b.data.vertices:
            d = b.matrix_world @ v.co - p
            x = d.dot(h_as) * teken
            rho = (d - h_as * d.dot(h_as)).length
            if x > tw + 1e-5 * u and rho < r and x > beste:
                beste, top = x, d
        if top is None:
            stap(f"neus {kant}: punten op de neus gevonden", False, "geen punt voorbij de tong")
            continue
        hoogte = (beste - tw) / u
        midden = (top - h_as * top.dot(h_as)).length / u
        print(f"[cj-betaald] METING neus {kant}: hoogte {hoogte:.4f} mm, top tot H {midden:.4f} mm, "
              f"tw {tw / u:.4f} mm, voet {float(b.get('cj_neus_voet', -1)) / u:.4f} mm")
        stap(f"neus {kant}: hoogte 0.25 mm binnen {TOL_MM} mm", abs(hoogte - 0.25) <= TOL_MM, f"{hoogte:.4f} mm")
        stap(f"neus {kant}: midden op H binnen {TOL_MM} mm", midden <= TOL_MM, f"{midden:.4f} mm")
        # Kuiltje: van de top van de neus tot A is de speling (concentrische bollen).
        pa = [a.matrix_world @ v.co for v in a.data.vertices]
        bvh_a = BVHTree.FromPolygons(pa, [tuple(f.vertices) for f in a.data.polygons])
        hit = bvh_a.find_nearest(p + top)
        afstand = hit[3] / u if hit[0] is not None else -1
        print(f"[cj-betaald] METING kuiltje {kant}: top neus tot deel A {afstand:.4f} mm")
        stap(f"kuiltje {kant}: speling boven de neus 0.2 mm binnen {TOL_MM} mm", abs(afstand - 0.2) <= TOL_MM,
             f"{afstand:.4f} mm")
    # Rek: eigen rekensom uit de maten van het deel, tegen wat de add-on opsloeg.
    s = float(b["cj_speling_mm"]) * u
    wx = 5.0 * u
    t = wx - tw - s
    lip = (float(b["cj_naad_r"]) - s / 2) + 0.6 * 2 * 5.0 * u
    h = float(b.get("cj_neus_h", -1))
    eigen_rek = 1.5 * t * h / (lip * lip)
    rek = float(b.get("cj_rek", -1))
    print(f"[cj-betaald] METING rek: add-on {rek * 100:.3f}% eigen {eigen_rek * 100:.3f}% "
          f"t {t / u:.3f} mm L {lip / u:.3f} mm h {h / u:.3f} mm")
    stap("neus: rek hoogstens 3% en gelijk aan de eigen rekensom", 0 < rek <= 0.03
         and abs(rek - eigen_rek) < 1e-4, f"{rek * 100:.3f}% (eigen {eigen_rek * 100:.3f}%)")
    duur = float(b.get("cj_duur_s", 99))
    print(f"[cj-betaald] METING tijd met neuzen {duur} s solver {b.get('cj_solver')}")
    # Dunne staaf 5 mm: nooit een scharnier dat toch geplaatst wordt.
    staaf = _plaats(2.5, cursor)
    voor = sorted(o.name for o in bpy.data.objects)
    tekst = ""
    try:
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:
        uitslag, tekst = {"CANCELLED"}, str(fout)
    na = sorted(o.name for o in bpy.data.objects)
    ops = sys.modules[eigen + ".betaald.scharnier"]
    # De melding zelf: maten en neus opnieuw rekenen zoals de operator (zonder venster komt report niet terug).
    reden = _reden(ops, vorm, neus, staaf, u)
    print(f"[cj-betaald] METING dunne staaf 5 mm: {uitslag}, melding \"{reden}\", objecten {na}")
    stap("dunne staaf 5 mm: CANCELLED, geen nieuwe objecten", uitslag == {"CANCELLED"} and voor == na
         and not staaf.hide_get(), f"{uitslag} {na}")
    stap("dunne staaf 5 mm: melding te dun of Tight", reden in (vorm.TE_DUN, neus.TIGHT) and
         (not tekst or reden in tekst), reden)
    stap("Tight-rekensom: hoge neus op een korte lip geeft Tight", neus.maten_neus(
        {"s": 0.2, "wx": 5.0, "tw": 1.0, "rn": 0.3, "wy": 0.2, "r": 1.0}, 1.0) == neus.TIGHT)


def _reden(ops, vorm, neus, staaf, u):
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
        reden = neus.maten_neus(maat, u)
    return reden
