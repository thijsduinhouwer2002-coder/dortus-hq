"""Toetsen van het scharnier (ontwerp betaald v1.1, eis 1), aangeroepen vanuit test_betaald.py.

Staaf van 10 mm (figuren.staaf, straal 5) in een mm-scene, cursor als as-bron: lidas langs de staaf (X),
scharnieras H langs wereld-Y (X-as van de cursor). Eisen: twee gesloten delen, speling om H (knokkel in de
holle cilinder) en langs H (tong tussen de wangen) gemeten in de mesh gelijk aan de ingestelde binnen 0,01 mm,
tijd gelogd. Regels met [cj-betaald]."""
import math
import sys

import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

import figuren

TOL_MM = 0.01


def _bvh(ob):
    me = ob.data
    punten = [ob.matrix_world @ v.co for v in me.vertices]
    return BVHTree.FromPolygons(punten, [tuple(p.vertices) for p in me.polygons])


def _cursor(punt, x, y, z):
    m = Matrix.Identity(4)
    for i, v in enumerate((x, y, z)):
        m.col[i][:3] = v
    m.col[3][:3] = punt
    c = bpy.context.scene.cursor
    c.rotation_mode = "QUATERNION"
    c.matrix = m


def meet(a, b, u):
    """(afstanden om H, afstanden langs H) in mm: van punten van deel B naar het dichtstbijzijnde punt van A."""
    p = Vector(b["cj_scharnier_punt"])
    h = Vector(b["cj_scharnier_as"]).normalized()
    lid = Vector(b["cj_as"]).normalized()
    buig = Vector(b["cj_buigkant"]).normalized()
    r, tw, rn, s = b["cj_knokkel_r"], b["cj_tong_half"], b["cj_naad_r"], b["cj_speling_mm"] * u
    bvh_a = _bvh(a)
    om, langs = [], []
    for v in b.data.vertices:
        q = b.matrix_world @ v.co
        d = q - p
        x = d.dot(h)
        radiaal = d - h * x
        rho = radiaal.length
        if abs(abs(x) - tw) > 1e-4 * u:
            continue
        # Langs H: punten op de zijkant van de tong, binnen de wangen.
        if rho < rn - 2 * s:
            hit = bvh_a.find_nearest(q)
            if hit[0] is not None:
                langs.append(hit[3] / u)
        # Om H: randpunten van de knokkel (straal R) waar deel A hem omvat: achter en onder H (voor H ligt
        # de wig open, daar zit geen A tegen de knokkel). Langs de rechte rand naar het midden van de tong
        # geschoven, zodat de wangen niet meetellen.
        if abs(rho - r) < 1e-4 * u and d.dot(lid) < -2 * s and d.dot(buig) < 0:
            hit = bvh_a.find_nearest(p + radiaal)
            if hit[0] is not None:
                om.append(hit[3] / u)
    return om, langs


def toets(stap, eigen):
    """Draait de toetsen; stap(naam, ok, extra) logt en telt fouten."""
    eig = sys.modules[eigen + ".eigenschappen"]
    gesloten = sys.modules[eigen + ".gesloten"]
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    scene = bpy.context.scene
    u = eig.eenheid_per_mm(scene)
    inst = scene.click_joints
    inst.speling_mm = 0.2
    inst.as_bron = "CURSOR"
    staaf = figuren.staaf("staaf", 5.0)
    figuren.maak_actief(staaf)
    _cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    stap("scharnier geplaatst", uitslag == {"FINISHED"}, str(uitslag))
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    if a is None or b is None:
        stap("twee delen staaf_A en staaf_B", False)
        return
    ga, gb = gesloten.is_gesloten(a), gesloten.is_gesloten(b)
    stap("twee gesloten delen", ga[0] and gb[0], f"A {ga[1]} B {gb[1]} foute randen")
    h = Vector(b["cj_scharnier_as"])
    stap("H langs de X-as van de cursor", abs(abs(h.dot(Vector((0, 1, 0)))) - 1) < 1e-6, str(tuple(round(c, 4) for c in h)))
    om, langs = meet(a, b, u)
    for naam, lijst in (("om H", om), ("langs H", langs)):
        if not lijst:
            stap(f"speling {naam} gemeten", False, "geen meetpunten")
            continue
        gem = sum(lijst) / len(lijst)
        ok = abs(gem - 0.2) <= TOL_MM and abs(min(lijst) - 0.2) <= TOL_MM and abs(max(lijst) - 0.2) <= TOL_MM
        stap(f"speling {naam} 0.2 mm binnen {TOL_MM} mm", ok,
             f"gemiddeld {gem:.4f} min {min(lijst):.4f} max {max(lijst):.4f} over {len(lijst)} punten")
    stap("tijd scharnier", True, f"{b.get('cj_duur_s', -1)} s solver {b.get('cj_solver')} "
                                 f"wig {b.get('cj_wig_graden')} graden R {b.get('cj_knokkel_r', 0):.3f} mm")
    # Wighoek (controleur ronde t1): stop = 2 * wig + s/r moet de stand zijn, binnen 0,1 graad.
    vorm_m = sys.modules[eigen + ".betaald.scharnier_vorm"]
    th = float(b.get("cj_theta_s", -1.0))
    stop = vorm_m.stop_graden(math.radians(float(b.get("cj_wig_graden", 0.0))), th)
    stap("stop 115 = 2 wig + s/r binnen 0.1 graad", th > 0 and abs(stop - 115) <= 0.1,
         f"wig {b.get('cj_wig_graden')} theta_s {math.degrees(th):.3f} stop {stop:.3f}")
    # Kijkrichting langs de lidas geeft de melding (zonder venster valt kijk terug op de cursor, dus hier
    # alleen de rekensom zelf).
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    lid = Vector((1, 0, 0))
    stap("kijken langs de lidas weigert", vorm.scharnier_assen(lid, kijk=Vector((0.95, 0.2, 0)).normalized()) is None)
    schuin = vorm.scharnier_assen(lid, kijk=Vector((1, 1, 0)).normalized(), omhoog=Vector((0, 0, 1)))
    stap("schuin (45 graden) geeft H loodrecht op L", schuin is not None and abs(schuin[0].dot(lid)) < 1e-6
         and math.isclose(abs(schuin[0].y), 1.0, abs_tol=1e-6), str(schuin and tuple(schuin[0])))
