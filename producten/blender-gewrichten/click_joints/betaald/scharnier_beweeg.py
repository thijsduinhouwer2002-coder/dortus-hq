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
