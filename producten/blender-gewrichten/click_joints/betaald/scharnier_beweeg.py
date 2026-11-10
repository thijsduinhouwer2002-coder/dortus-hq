"""Beweegproef van het scharnier (ontwerp betaald v1.1, eis 2): deel B draait om H en we zoeken waar het deel A
voor het eerst raakt, naar voren (de eindstop, naar de buigkant) en naar achteren (de achterstop).

Meten in de mesh, niet rekenen: B wordt per hoek gedraaid en met BVHTree.overlap tegen A gelegd. Alleen de
vlakken binnen een bol rond het draaipunt tellen mee (straal `bol`), want verder weg kan bij een recht lid
niets botsen voor de stop, en zo blijft het snel op een arm van 261K. Grof stappen tot de eerste botsing,
daarna halveren tot 0,05 graad.

Draairichting: het frame is X = H, Y = buigkant, Z = lidas (rechtshandig). Naar voren buigen brengt de lidas
naar de buigkant, dat is een draai om lid x buig = -H."""
import math

import bpy
import numpy as np
from mathutils import Matrix, Quaternion, Vector
from mathutils.bvhtree import BVHTree

from .. import uit_elkaar
from ..uit_elkaar import echte_matrix


def pose_q(b):
    """Draaiing van de scharnierpose: om H (lidas x buigkant) over cj_pose_graden."""
    g = float(b.get("cj_pose_graden", 0.0))
    if g == 0.0:
        return Quaternion()
    voor_as = Vector(b["cj_as"]).cross(Vector(b["cj_buigkant"])).normalized()
    return Quaternion(voor_as, math.radians(g))


def zet_scharnier(ob, aan):
    """Weergave van deel B van een scharnier: Exploded view langs de lidas plus pose om het draaipunt.
    Echte matrix M = T(p) R S; in beeld T(e) T(c) Q T(-c) M = T(e + c + Q(p - c)) Q R S (zoals uit_elkaar.zet,
    Blender zet de delta-draaiing links van de eigen draaiing)."""
    e = Vector(ob["cj_as"]).normalized() * uit_elkaar.afstand(ob) if aan else Vector()
    q = pose_q(ob)
    if ob.parent is None and q != Quaternion():
        p, c = Vector(ob.location), Vector(ob["cj_scharnier_punt"])
        ob.delta_location = e + c + q @ (p - c) - p
    else:
        ob.delta_location = e
    uit_elkaar._zet_draai(ob, q)

NAUWKEURIG = 0.05   # graden
MAX_VOOR = 150.0
MAX_ACHTER = 20.0
STAP_VOOR = 2.5     # zoals de kogel: kleine uitsteeksels schieten niet tussen twee stappen door
STAP_ACHTER = 0.5


def _driehoeken(ob, midden, bol):
    """(punten als numpy n x 3 in wereldcoordinaten, driehoeken) van de driehoeken met minstens één hoekpunt
    binnen de bol. Met foreach_get, zodat het ook op een arm van 261K vlot gaat."""
    me = ob.data
    me.calc_loop_triangles()
    co = np.empty(len(me.vertices) * 3, dtype=np.float64)
    me.vertices.foreach_get("co", co)
    co = co.reshape(-1, 3)
    mw = np.array(ob.matrix_world, dtype=np.float64)
    co = co @ mw[:3, :3].T + mw[:3, 3]
    tri = np.empty(len(me.loop_triangles) * 3, dtype=np.int64)
    me.loop_triangles.foreach_get("vertices", tri)
    tri = tri.reshape(-1, 3)
    binnen = np.linalg.norm(co - np.array(midden), axis=1) <= bol
    tri = tri[binnen[tri].any(axis=1)]
    gebruikt, nieuw = np.unique(tri, return_inverse=True)
    return co[gebruikt], nieuw.reshape(-1, 3).tolist()


def _raakt(bvh_a, punten_b, tris_b, draai):
    m = np.array(draai, dtype=np.float64)
    gedraaid = punten_b @ m[:3, :3].T + m[:3, 3]
    return bool(BVHTree.FromPolygons(gedraaid.tolist(), tris_b).overlap(bvh_a))


def _grens(bvh_a, punten_b, tris_b, punt, as_, maximum, stap):
    """Kleinste hoek in graden (0 tot maximum) waarbij B in A komt, of maximum als het nergens raakt.
    None als B bij 0 graden al in A zit (dan klopt de vorm niet)."""
    def draai(graden):
        return (Matrix.Translation(punt) @ Matrix.Rotation(math.radians(graden), 4, as_)
                @ Matrix.Translation(-punt))
    if _raakt(bvh_a, punten_b, tris_b, Matrix.Identity(4)):
        return None
    vrij, hoek = 0.0, stap
    while hoek <= maximum + 1e-9:
        if _raakt(bvh_a, punten_b, tris_b, draai(hoek)):
            break
        vrij, hoek = hoek, hoek + stap
    else:
        return maximum
    raak = hoek
    while raak - vrij > NAUWKEURIG:
        mid = (vrij + raak) / 2
        if _raakt(bvh_a, punten_b, tris_b, draai(mid)):
            raak = mid
        else:
            vrij = mid
    return vrij


def bereik(a, b, punt, h, buig, lid, bol):
    """(eindstop naar voren, achterstop naar achteren) in graden, beide positief gemeten; None als B bij 0
    graden al in A zit."""
    punt = Vector(punt)
    punten_a, tris_a = _driehoeken(a, punt, bol)
    punten_b, tris_b = _driehoeken(b, punt, bol)
    bvh_a = BVHTree.FromPolygons(punten_a.tolist(), tris_a)
    voor_as = Vector(lid).cross(Vector(buig)).normalized()
    voor = _grens(bvh_a, punten_b, tris_b, punt, voor_as, MAX_VOOR, STAP_VOOR)
    if voor is None:
        return None, None
    achter = _grens(bvh_a, punten_b, tris_b, punt, -voor_as, MAX_ACHTER, STAP_ACHTER)
    return voor, achter


def tekst(voor, stand):
    """Wat het paneel en de melding laten zien: het gemeten bereik, nooit meer dan de stand."""
    return f"Bends 0° to {min(int(round(voor)), int(stand))}°"


def geen_stop(voor):
    """Waar als de proef tot het maximum draaide zonder te botsen (dan is er geen stop gevonden)."""
    return voor >= MAX_VOOR - 1e-6


GROEI_MM = 1.0  # rood als vlak (Daan punt 5): ook de vlakken binnen 1 mm van een rakend vlak, anders zie je alleen een lijn


def _terug(ob):
    """Vorige rode vlakken van ob terug naar hun eigen materiaalvak."""
    me = ob.data
    oud = list(ob.get("cj_rood_vlakken", []))
    for i in range(0, len(oud), 2):
        if oud[i] < len(me.polygons):
            me.polygons[oud[i]].material_index = oud[i + 1]
    ob["cj_rood_vlakken"] = []


def _groei(ob, vlakken, afstand):
    """De rakende vlakken plus alle vlakken van ob waarvan het middelpunt binnen `afstand` van een rakend vlak ligt."""
    if not vlakken or afstand <= 0:
        return set(vlakken)
    from mathutils.kdtree import KDTree
    me = ob.data
    n = len(me.polygons)
    c = np.empty(n * 3, dtype=np.float64)
    me.polygons.foreach_get("center", c)
    c = c.reshape(n, 3)
    boom = KDTree(n)
    for i in range(n):
        boom.insert(c[i], i)
    boom.balance()
    uit = set(vlakken)
    for v in vlakken:
        for _co, j, _d in boom.find_range(c[v], afstand):
            uit.add(j)
    return uit


def _kleur(ob, vlakken, kleur_rood):
    me = ob.data
    if not vlakken:
        return
    if len(me.materials) == 0:
        me.materials.append(None)  # eerst een leeg vak 0, anders wordt rood vak 0 en is het hele deel rood
    namen = [m.name if m else None for m in me.materials]
    if kleur_rood.name in namen:
        vak = namen.index(kleur_rood.name)
    else:
        me.materials.append(kleur_rood)
        vak = len(me.materials) - 1
    lijst = []
    for v in sorted(vlakken):
        lijst += [v, me.polygons[v].material_index]
        me.polygons[v].material_index = vak
    ob["cj_rood_vlakken"] = lijst


def pose(a, b, graden, kleur_rood=None):
    """Eis 8 (plaatjes 11 en 12): deel B in de weergave `graden` naar voren om H draaien, zoals de beweegproef.
    Voorbij de gemeten eindstop (cj_bereik_graden) krijgen de vlakken van A en B die elkaar raken het rode materiaal
    (kleur_rood), plus de vlakken binnen GROEI_MM daarvan, zodat het rood als vlak leest (Daan, Pro punt 5); de vorige
    rode vlakken eerst terug. Geeft het aantal rode vlakken van A (zoals eerst); die van B staan in cj_rood_vlakken van B."""
    # Alleen de weergave: de draaiing staat in delta_rotation en delta_location van deel B (zet_scharnier),
    # net als de pose van de kogel. location, rotation en matrix_world-zonder-delta's blijven van de gebruiker,
    # dus de export (echte_plek) en echte_matrix zien deel B recht.
    b["cj_pose_graden"] = float(graden)
    try:
        aan = bool(bpy.context.scene.click_joints.uit_elkaar)
    except AttributeError:
        aan = False
    zet_scharnier(b, aan)
    punt = Vector(b["cj_scharnier_punt"])
    draai = (Matrix.Translation(punt) @ pose_q(b).to_matrix().to_4x4() @ Matrix.Translation(-punt))
    me = a.data
    _terug(a)
    _terug(b)
    if graden <= float(a.get("cj_bereik_graden", MAX_VOOR)) or kleur_rood is None:
        me.update()
        b.data.update()
        return 0
    me.calc_loop_triangles()
    b.data.calc_loop_triangles()
    ma = echte_matrix(a)
    bvh_a = BVHTree.FromPolygons([ma @ v.co for v in me.vertices], [tuple(t.vertices) for t in me.loop_triangles])
    mb = draai @ echte_matrix(b)  # waar B echt zou staan bij deze stand, zonder Exploded view
    bvh_b = BVHTree.FromPolygons([mb @ v.co for v in b.data.vertices],
                                 [tuple(t.vertices) for t in b.data.loop_triangles])
    paren = bvh_a.overlap(bvh_b)
    raak_a = {me.loop_triangles[i].polygon_index for i, _ in paren}
    raak_b = {b.data.loop_triangles[j].polygon_index for _, j in paren}
    try:
        from ..eigenschappen import eenheid_per_mm
        u = eenheid_per_mm(bpy.context.scene)
    except Exception:  # noqa: BLE001  zonder scene: rekenen in mm
        u = 1.0
    # Groeien in de eigen coördinaten van het deel: schaal van het object eruit halen (mesh-eenheden per mm).
    vlakken_a = _groei(a, raak_a, GROEI_MM * u / max(1e-9, ma.to_scale().length / 3 ** 0.5))
    vlakken_b = _groei(b, raak_b, GROEI_MM * u / max(1e-9, echte_matrix(b).to_scale().length / 3 ** 0.5))
    _kleur(a, vlakken_a, kleur_rood)
    _kleur(b, vlakken_b, kleur_rood)
    me.update()
    b.data.update()
    return len(vlakken_a)
