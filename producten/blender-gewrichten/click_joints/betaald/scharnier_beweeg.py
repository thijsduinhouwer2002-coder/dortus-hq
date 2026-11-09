"""Beweegproef van het scharnier (ontwerp betaald v1.1, eis 2): deel B draait om H en we zoeken waar het deel A
voor het eerst raakt, naar voren (de eindstop, naar de buigkant) en naar achteren (de achterstop).

Meten in de mesh, niet rekenen: B wordt per hoek gedraaid en met BVHTree.overlap tegen A gelegd. Alleen de
vlakken binnen een bol rond het draaipunt tellen mee (straal `bol`), want verder weg kan bij een recht lid
niets botsen voor de stop, en zo blijft het snel op een arm van 261K. Grof stappen tot de eerste botsing,
daarna halveren tot 0,05 graad.

Draairichting: het frame is X = H, Y = buigkant, Z = lidas (rechtshandig). Naar voren buigen brengt de lidas
naar de buigkant, dat is een draai om lid x buig = -H."""
import math

import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

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


def pose(a, b, graden, kleur_rood=None):
    """Eis 8 (plaatjes 11 en 12): deel B in de weergave `graden` naar voren om H draaien, zoals de beweegproef.
    Voorbij de gemeten eindstop (cj_bereik_graden) krijgen de vlakken van A die B raken het rode materiaal
    (kleur_rood); de vorige rode vlakken eerst terug. Geeft het aantal rode vlakken."""
    if "cj_pose_basis" not in b:
        b["cj_pose_basis"] = [v for rij in b.matrix_world for v in rij]
    basis = Matrix([b["cj_pose_basis"][i * 4:i * 4 + 4] for i in range(4)])
    punt = Vector(b["cj_scharnier_punt"])
    voor_as = Vector(b["cj_as"]).cross(Vector(b["cj_buigkant"])).normalized()
    draai = (Matrix.Translation(punt) @ Matrix.Rotation(math.radians(graden), 4, voor_as)
             @ Matrix.Translation(-punt))
    b.matrix_world = draai @ basis
    b["cj_pose_graden"] = float(graden)
    me = a.data
    oud = list(a.get("cj_rood_vlakken", []))
    for i in range(0, len(oud), 2):
        if oud[i] < len(me.polygons):
            me.polygons[oud[i]].material_index = oud[i + 1]
    a["cj_rood_vlakken"] = []
    if graden <= float(a.get("cj_bereik_graden", MAX_VOOR)) or kleur_rood is None:
        me.update()
        return 0
    me.calc_loop_triangles()
    mw = a.matrix_world
    bvh_a = BVHTree.FromPolygons([mw @ v.co for v in me.vertices], [tuple(t.vertices) for t in me.loop_triangles])
    mb = b.matrix_world
    bvh_b = BVHTree.FromPolygons([mb @ v.co for v in b.data.vertices],
                                 [tuple(p.vertices) for p in b.data.polygons])
    vlakken = sorted({me.loop_triangles[i].polygon_index for i, _ in bvh_a.overlap(bvh_b)})
    if vlakken:
        namen = [m.name if m else None for m in me.materials]
        if kleur_rood.name in namen:
            vak = namen.index(kleur_rood.name)
        else:
            me.materials.append(kleur_rood)
            vak = len(me.materials) - 1
        lijst = []
        for v in vlakken:
            lijst += [v, me.polygons[v].material_index]
            me.polygons[v].material_index = vak
        a["cj_rood_vlakken"] = lijst
    me.update()
    return len(vlakken)
