"""Pose van het scharnier is alleen weergave (moet-punt eis 8, run 42 Bram).
Aangeroepen vanuit toetsen_scharnier.py na eis 6, zelfde staaf als toetsen_scharnier_uit (5 mm, 80 mm, stand 115).

(a) Pose 60: location, rotation en echte_matrix van deel B veranderen niet; in beeld staat B wel 60 graden om H
    gedraaid (de lidas van B in matrix_world maakt 60 graden met de oude lidas) en het draaipunt ligt stil.
(b) Export STL en 3MF van deel B met pose 60 gelijk aan de export zonder pose (binnen 0,0001 mm).
(c) Exploded view aan en uit met pose 60: de draaiing blijft die om H (niet de kogelpose), het draaipunt schuift
    precies 3 Rn langs L mee; export ook dan gelijk.
(d) Pose terug naar 0: matrix_world gelijk aan echte_matrix (geen restje draaiing).
(e) Ook als de gebruiker B zelf draaide (euler en QUATERNION): matrix_world . echte_matrix^-1 is precies
    T(c) Q T(-c) met Q 60 graden om lidas x buigkant (dus ook de draairichting), export gelijk aan zonder pose.
Alle maten in het log in mm."""
import math
import sys

import bpy
from mathutils import Matrix, Quaternion, Vector

import figuren
from toetsen_scharnier_uit import _exporteer, _plaats


def _max_verschil(p, q):
    if not p or not q or len(p) != len(q):
        return float("inf")
    return max(abs(x - y) for a, b in zip(p, q) for x, y in zip(a, b))


def _matrix_verschil(m1, m2):
    return max(abs(m1[i][j] - m2[i][j]) for i in range(4) for j in range(4))


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    uit_elkaar = sys.modules[eigen + ".uit_elkaar"]
    beweeg = sys.modules[eigen + ".betaald.scharnier_beweeg"]
    kleur = sys.modules[eigen + ".kleur"]
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar = 0.2, "CURSOR", False
    u = eig.eenheid_per_mm(bpy.context.scene)
    staaf = figuren.staaf("pose", 5.0, lengte=80.0)
    uitslag = _plaats((0, 0, 0), staaf, cursor)
    a, b = bpy.data.objects.get("pose_A"), bpy.data.objects.get("pose_B")
    stap("pose: scharnier geplaatst", uitslag == {"FINISHED"} and a and b, str(uitslag))
    if a is None or b is None:
        return
    bpy.context.view_layer.update()
    loc, rot = Vector(b.location), tuple(b.rotation_euler)
    echt0 = uit_elkaar.echte_matrix(b).copy()
    lid = Vector(b["cj_as"]).normalized()
    punt = Vector(b["cj_scharnier_punt"])
    ref = {f: _exporteer(inst, f, b) for f in ("STL", "3MF")}
    stap("pose: export zonder pose gelukt", all(ref.values()))
    # (a) Pose 60.
    beweeg.pose(a, b, 60.0, kleur.materiaal("rood"))
    bpy.context.view_layer.update()
    mw = b.matrix_world
    lid_beeld = (mw.to_3x3() @ (echt0.to_3x3().inverted() @ lid)).normalized()
    hoek = math.degrees(lid_beeld.angle(lid))
    punt_beeld = mw @ (echt0.inverted() @ punt)
    stil = (punt_beeld - punt).length / u
    blijft = (Vector(b.location) - loc).length < 1e-9 and tuple(b.rotation_euler) == rot \
        and _matrix_verschil(uit_elkaar.echte_matrix(b), echt0) < 1e-9
    print(f"[cj-betaald] METING pose 60: lidas in beeld {hoek:.4f} graden gedraaid, draaipunt {stil:.6f} mm verplaatst, "
          f"delta_rotation {tuple(round(x, 5) for x in b.delta_rotation_euler)}, "
          f"delta_location {tuple(round(x / u, 4) for x in b.delta_location)} mm, location en echte_matrix gelijk {blijft}")
    stap("pose 60: location, rotation en echte_matrix van B ongewijzigd", blijft)
    stap("pose 60: in beeld 60 graden om H gedraaid, draaipunt stil", abs(hoek - 60.0) < 0.01 and stil < 1e-4,
         f"{hoek:.4f} graden, {stil:.6f} mm")
    # (b) Export met pose gelijk aan zonder.
    for f in ("STL", "3MF"):
        d = _max_verschil(_exporteer(inst, f, b), ref[f])
        print(f"[cj-betaald] METING pose 60 export {f}: grootste verschil met export zonder pose {d:.7f} mm")
        stap(f"pose 60: export {f} van deel B gelijk aan zonder pose", d < 1e-4, f"{d:.7f} mm")
    bpy.context.view_layer.update()
    stap("pose 60: na export staat B weer gedraaid",
         abs(math.degrees((b.matrix_world.to_3x3() @ (echt0.to_3x3().inverted() @ lid)).normalized().angle(lid))
             - 60.0) < 0.01)
    # (c) Exploded view aan en uit met pose.
    for aan in (True, False):
        inst.uit_elkaar = aan
        bpy.context.view_layer.update()
        mw = b.matrix_world
        h = math.degrees((mw.to_3x3() @ (echt0.to_3x3().inverted() @ lid)).normalized().angle(lid))
        schuif = (mw @ (echt0.inverted() @ punt)) - punt
        verwacht = lid * (3 * float(b["cj_naad_r"])) if aan else Vector()
        fout = (schuif - verwacht).length / u
        print(f"[cj-betaald] METING pose 60 Exploded view aan={aan}: draaiing {h:.4f} graden, draaipunt "
              f"{schuif.length / u:.4f} mm verschoven (verwacht {verwacht.length / u:.4f}), afwijking {fout:.6f} mm")
        stap(f"pose 60 met Exploded view aan={aan}: draaiing om H blijft 60, draaipunt op de goede plek",
             abs(h - 60.0) < 0.01 and fout < 1e-4, f"{h:.4f} graden, {fout:.6f} mm")
        if aan:
            for f in ("STL", "3MF"):
                d = _max_verschil(_exporteer(inst, f, b), ref[f])
                stap(f"pose 60 met Exploded view: export {f} gelijk aan zonder pose", d < 1e-4, f"{d:.7f} mm")
    # (d) Pose terug naar 0.
    beweeg.pose(a, b, 0.0, kleur.materiaal("rood"))
    bpy.context.view_layer.update()
    rest = _matrix_verschil(b.matrix_world, uit_elkaar.echte_matrix(b))
    stap("pose 0: matrix_world gelijk aan echte_matrix", rest < 1e-6, f"{rest:.2e}")
    # (e) B zelf gedraaid, euler en quaternion; draairichting ook vast.
    voor_as = Vector(b["cj_as"]).cross(Vector(b["cj_buigkant"])).normalized()
    doel = Matrix.Translation(punt) @ Matrix.Rotation(math.radians(60.0), 4, voor_as) @ Matrix.Translation(-punt)
    for modus, zet in (("XYZ", lambda: setattr(b, "rotation_euler", (0.3, -0.2, 0.5))),
                       ("QUATERNION", lambda: setattr(b, "rotation_quaternion",
                                                      Quaternion(Vector((1, 2, 3)).normalized(), 0.7)))):
        b.rotation_mode = modus
        zet()
        beweeg.pose(a, b, 0.0, kleur.materiaal("rood"))
        bpy.context.view_layer.update()
        ref_e = _exporteer(inst, "STL", b)
        beweeg.pose(a, b, 60.0, kleur.materiaal("rood"))
        bpy.context.view_layer.update()
        fout = _matrix_verschil(b.matrix_world @ uit_elkaar.echte_matrix(b).inverted(), doel)
        d = _max_verschil(_exporteer(inst, "STL", b), ref_e)
        print(f"[cj-betaald] METING pose 60 met B zelf gedraaid ({modus}): afwijking van T(c) Q T(-c) {fout:.2e}, "
              f"export STL verschil {d:.7f} mm")
        stap(f"pose 60 met B zelf gedraaid ({modus}): draaiing om H door het draaipunt, goede richting",
             fout < 1e-5, f"{fout:.2e}")
        stap(f"pose 60 met B zelf gedraaid ({modus}): export STL gelijk aan zonder pose", d < 1e-4, f"{d:.7f} mm")
    beweeg.pose(a, b, 0.0, kleur.materiaal("rood"))
    # (f) Pose-schuif in het paneel hoort bij het actieve scharnier en leest de stand van deel B terug.
    wm = bpy.context.window_manager
    figuren.maak_actief(b)
    wm.cj_scharnier_pose = 30.0
    bpy.context.view_layer.update()
    terug = wm.cj_scharnier_pose
    stap("pose-schuif: zet de stand op deel B en leest hem terug",
         abs(float(b.get("cj_pose_graden", -1)) - 30.0) < 1e-6 and abs(terug - 30.0) < 1e-4, f"{terug}")
    b["cj_pose_graden"] = 45.0  # zoals na heropenen: de stand staat in de .blend, de schuif volgt
    stap("pose-schuif volgt de stand die op deel B staat", abs(wm.cj_scharnier_pose - 45.0) < 1e-4,
         f"{wm.cj_scharnier_pose}")
    figuren.maak_actief(staaf)
    stap("pose-schuif zonder actief scharnier: 0", wm.cj_scharnier_pose == 0.0, f"{wm.cj_scharnier_pose}")
    figuren.maak_actief(b)
    wm.cj_scharnier_pose = 0.0
