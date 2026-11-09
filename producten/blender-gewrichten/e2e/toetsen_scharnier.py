"""Toetsen van het scharnier (ontwerp betaald v1.1, eis 1 en 2), aangeroepen vanuit test_betaald.py.

Staaf van 10 mm (figuren.staaf, straal 5) in een mm-scene, cursor als as-bron: lidas langs de staaf (X),
scharnieras H langs wereld-Y (X-as van de cursor). Eisen: twee gesloten delen, speling om H (knokkel in de
holle cilinder) en langs H (tong tussen de wangen) gemeten in de mesh gelijk aan de ingestelde binnen 0,01 mm,
tijd gelogd; beweegproef per stand (eis 2). Invoer (eis 4) staat in toetsen_kijk.py, Flip bend in
toetsen_flip.py, de klikneus en de zaagsnede (eis 3, vorm punt 5) in toetsen_neus.py. Regels met [cj-betaald]."""
import math
import sys

import bpy
from mathutils import Matrix, Vector

import figuren
import toetsen_flip
import toetsen_kijk
import toetsen_neus
from hulp_scharnier import bvh as _bvh
from hulp_scharnier import cursor as _cursor

TOL_MM = 0.01


def meet(a, b, u):
    """(afstanden om H, afstanden langs H) in mm: van punten van deel B naar het dichtstbijzijnde punt van A."""
    p = Vector(b["cj_scharnier_punt"])
    h = Vector(b["cj_scharnier_as"]).normalized()
    lid = Vector(b["cj_as"]).normalized()
    buig = Vector(b["cj_buigkant"]).normalized()
    r, tw, rn, s = b["cj_knokkel_r"], b["cj_tong_half"], b["cj_naad_r"], b["cj_speling_mm"] * u
    bvh_a = _bvh(a)
    om, langs, voet = [], [], []
    for v in b.data.vertices:
        q = b.matrix_world @ v.co
        d = q - p
        x = d.dot(h)
        radiaal = d - h * x
        rho = radiaal.length
        if abs(abs(x) - tw) > 1e-4 * u:
            continue
        # Langs H: punten op de zijkant van de tong, binnen de wangen.
        # De voetring van de klikneus (dichter dan 0,7 R bij H) hoort bij de neus: daar ligt het kuiltje schuin
        # boven, dus meer ruimte dan s (getoetst als voet, nooit minder dan s); de neus zelf in toetsen_neus.
        if rho < rn - 2 * s:
            hit = bvh_a.find_nearest(q)
            if hit[0] is not None:
                (voet if rho < 0.7 * r else langs).append(hit[3] / u)
        # Om H: randpunten van de knokkel (straal R) waar deel A hem omvat: achter en onder H (voor H ligt
        # de wig open, daar zit geen A tegen de knokkel). Langs de rechte rand naar het midden van de tong
        # geschoven, zodat de wangen niet meetellen.
        if abs(rho - r) < 1e-4 * u and d.dot(lid) < -2 * s and d.dot(buig) < 0:
            hit = bvh_a.find_nearest(p + radiaal)
            if hit[0] is not None:
                om.append(hit[3] / u)
    return om, langs, voet


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
    om, langs, voet = meet(a, b, u)
    stap("voetring klikneus: speling nergens kleiner dan 0.2 mm min 0.01", bool(voet) and min(voet) >= 0.2 - TOL_MM,
         f"min {min(voet) if voet else -1:.4f} max {max(voet) if voet else -1:.4f} over {len(voet)} punten")
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
    doel = 115 - vorm_m.MARGE
    stap(f"stop {doel} = 2 wig + s/r binnen 0.1 graad", th > 0 and abs(stop - doel) <= 0.1,
         f"wig {b.get('cj_wig_graden')} theta_s {math.degrees(th):.3f} stop {stop:.3f}")
    # Kijkrichting langs de lidas geeft de melding (zonder venster valt kijk terug op de cursor, dus hier
    # alleen de rekensom zelf).
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    lid = Vector((1, 0, 0))
    stap("kijken langs de lidas weigert", vorm.scharnier_assen(lid, kijk=Vector((0.95, 0.2, 0)).normalized()) is None)
    schuin = vorm.scharnier_assen(lid, kijk=Vector((1, 1, 0)).normalized(), omhoog=Vector((0, 0, 1)))
    stap("schuin (45 graden) geeft H loodrecht op L", schuin is not None and abs(schuin[0].dot(lid)) < 1e-6
         and math.isclose(abs(schuin[0].y), 1.0, abs_tol=1e-6), str(schuin and tuple(schuin[0])))
    toetsen_kijk.toets_kijk(stap, eigen)
    toets_beweeg(stap, eigen)
    toetsen_flip.toets_flip(stap, eigen)
    toetsen_neus.toets(stap, eigen, _cursor)  # eis 3: klikneus en vorm punt 5: zaagsnede


def toets_beweeg(stap, eigen):
    """Eis 2: beweegproef om H, gemeten door de add-on in de mesh, tegen een eigen rekensom per stand.
    Staaf straal 5 mm: halve dikte 5, H ligt e = 0,15 x 10 = 1,5 mm naar achteren, dus r_lip = 5 - 1,5 = 3,5 mm
    en de achterstop hoogstens atan(0,2 / 3,5) = 3,27 graden (plus 0,5). Eindstop tussen N - 2 en N + 0,5."""
    eig = sys.modules[eigen + ".eigenschappen"]
    beweeg = sys.modules[eigen + ".betaald.scharnier_beweeg"]
    s, straal = 0.2, 5.0
    r_lip = straal - 0.15 * 2 * straal
    achter_max = math.degrees(math.atan(s / r_lip)) + 0.5
    for n in (90, 115, 135):
        for ob in list(bpy.data.objects):
            bpy.data.objects.remove(ob)
        figuren.mm_scene()
        scene = bpy.context.scene
        inst = scene.click_joints
        inst.speling_mm = s
        inst.as_bron = "CURSOR"
        staaf = figuren.staaf("staaf", straal)
        figuren.maak_actief(staaf)
        _cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
        uitslag = bpy.ops.click_joints.plaats_scharnier(stand=str(n))
        b = bpy.data.objects.get("staaf_B")
        if uitslag != {"FINISHED"} or b is None:
            stap(f"stand {n}: scharnier geplaatst", False, str(uitslag))
            continue
        voor = float(b.get("cj_bereik_graden", -1))
        achter = float(b.get("cj_achter_graden", -1))
        stap(f"stand {n}: eindstop gemeten tussen {n - 2} en {n} graden", n - 2 <= voor <= n + 0.05,
             f"gemeten {voor:.2f}")
        achter_min = max(0.0, achter_max - 1.0)   # atan(s/r_lip) - 0,5: vangt overlap bij 0 graden
        stap(f"stand {n}: achterstop gemeten tussen -{achter_max:.2f} en +0.5 graden", 0 <= achter <= achter_max,
             f"gemeten -{achter:.2f} r_lip add-on {b.get('cj_r_lip', -1):.3f} eigen {r_lip:.3f} mm")
        stap(f"stand {n}: r_lip gelijk aan de eigen rekensom", abs(float(b.get("cj_r_lip", -1)) - r_lip) < 0.01)
        stap(f"stand {n}: achterstop minstens {achter_min:.2f} graden (geen botsing bij 0)", achter >= achter_min)
        k = round(voor)
        stap(f"stand {n}: tekst letterlijk met het gemeten getal ({n - 2} tot {n})",
             n - 2 <= k <= n and beweeg.tekst(voor, n) == f"Bends 0° to {k}°", beweeg.tekst(voor, n))
        stap(f"stand {n}: melding van de operator letterlijk",
             b.get("cj_melding") == f"Hinge placed. Bends 0° to {k}°.", str(b.get("cj_melding")))
        duur, solver = float(b.get("cj_duur_s", 99)), b.get("cj_solver")
        grens = 5.0 if solver == "MANIFOLD" else 10.0
        stap(f"stand {n}: tijd met beweegproef onder {grens} s ({solver})", duur < grens, f"{duur} s")
        _waar_raakt(stap, beweeg, n, voor)
    _toets_arm(stap, eigen, s)
    stap("tekst nooit meer dan de stand", beweeg.tekst(118.0, 115) == "Bends 0° to 115°")


def _toets_arm(stap, eigen, s):
    """Testarm van 261K (eis 1 en 2): scharnier plaatsen met beweegproef binnen de tijdseis."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = s
    inst.as_bron = "CURSOR"
    arm = figuren.arm("arm")
    figuren.maak_actief(arm)
    _cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115")
    b = bpy.data.objects.get("arm_B")
    if uitslag != {"FINISHED"} or b is None:
        stap("arm 261K: scharnier geplaatst", False, str(uitslag))
        return
    duur, solver = float(b.get("cj_duur_s", 99)), b.get("cj_solver")
    grens = 5.0 if solver == "MANIFOLD" else 10.0
    voor = float(b.get("cj_bereik_graden", -1))
    stap(f"arm 261K: tijd met beweegproef onder {grens} s ({solver})", duur < grens,
         f"{duur} s eindstop {voor:.2f} achterstop -{float(b.get('cj_achter_graden', -1)):.2f}")
    stap("arm 261K: eindstop tussen 113 en 115 graden", 113 <= voor <= 115.05, f"{voor:.2f}")


def _waar_raakt(stap, beweeg, n, voor):
    """Diagnose (run 28): waar raken A en B net voorbij de gemeten stop? Middelpunten van de overlappende
    driehoeken van B in het frame (x langs H, y buigkant, z lidas, oorsprong op het draaipunt), in mm."""
    from mathutils.bvhtree import BVHTree as _B
    a, b = bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")
    p = Vector(b["cj_scharnier_punt"])
    h, buig, lid = (Vector(b[k]).normalized() for k in ("cj_scharnier_as", "cj_buigkant", "cj_as"))
    pa, ta = beweeg._driehoeken(a, p, 1e9)
    pb, tb = beweeg._driehoeken(b, p, 1e9)
    hoek = voor + 0.06
    m = (Matrix.Translation(p) @ Matrix.Rotation(math.radians(hoek), 4, lid.cross(buig).normalized())
         @ Matrix.Translation(-p))
    import numpy as np
    mm = np.array(m)
    gb = pb @ mm[:3, :3].T + mm[:3, 3]
    paren = _B.FromPolygons(gb.tolist(), tb).overlap(_B.FromPolygons(pa.tolist(), ta))

    def f(q):
        c = Vector(q) - p
        return (round(c.dot(h), 2), round(c.dot(buig), 2), round(c.dot(lid), 2))
    print(f"[cj-betaald] DIAGNOSE stand {n}: {len(paren)} paren bij {hoek:.2f} graden, t_vlak "
          f"{b.get('cj_t_vlak', -1):.3f} wig {b.get('cj_wig_graden')}")
    for j, i in paren[:6]:  # overlap geeft (index in B, index in A)
        print(f"[cj-betaald] DIAGNOSE stand {n}: B {[f(gb[k]) for k in tb[j]]} A {[f(pa[k]) for k in ta[i]]}")
