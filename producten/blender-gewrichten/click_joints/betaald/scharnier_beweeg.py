"""Beweegproef van het scharnier (ontwerp betaald v1.1, eis 2): deel B draait om H en we zoeken waar het deel A
voor het eerst raakt, naar voren (de eindstop, naar de buigkant) en naar achteren (de achterstop).

Meten in de mesh, niet rekenen: B wordt per hoek gedraaid en met BVHTree.overlap tegen A gelegd. Alleen de
vlakken binnen een bol rond het draaipunt tellen mee (straal `bol`), want verder weg kan bij een recht lid
niets botsen voor de stop, en zo blijft het snel op een arm van 261K. Grof stappen tot de eerste botsing,
daarna halveren tot 0,05 graad.

Draairichting: het frame is X = H, Y = buigkant, Z = lidas (rechtshandig). Naar voren buigen brengt de lidas
naar de buigkant, dat is een draai om lid x buig = -H."""
import math

from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

NAUWKEURIG = 0.05   # graden
MAX_VOOR = 150.0
MAX_ACHTER = 20.0


def _driehoeken(ob, midden, bol):
    """(punten in wereldcoordinaten, driehoeken) van de vlakken met minstens één hoekpunt binnen de bol."""
    mw = ob.matrix_world
    punten = [mw @ v.co for v in ob.data.vertices]
    ob.data.calc_loop_triangles()
    tris = []
    for t in ob.data.loop_triangles:
        if any((punten[i] - midden).length <= bol for i in t.vertices):
            tris.append(tuple(t.vertices))
    gebruikt = sorted({i for t in tris for i in t})
    nieuw = {oud: k for k, oud in enumerate(gebruikt)}
    return [punten[i] for i in gebruikt], [tuple(nieuw[i] for i in t) for t in tris]


def _raakt(bvh_a, punten_b, tris_b, draai):
    gedraaid = [draai @ p for p in punten_b]
    return bool(BVHTree.FromPolygons(gedraaid, tris_b).overlap(bvh_a))


def _grens(bvh_a, punten_b, tris_b, punt, as_, maximum, stap):
    """Kleinste hoek in graden (0 tot maximum) waarbij B in A komt, of maximum als het nergens raakt."""
    def draai(graden):
        return (Matrix.Translation(punt) @ Matrix.Rotation(math.radians(graden), 4, as_)
                @ Matrix.Translation(-punt))
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
    """(eindstop naar voren, achterstop naar achteren) in graden, beide positief gemeten."""
    punt = Vector(punt)
    punten_a, tris_a = _driehoeken(a, punt, bol)
    punten_b, tris_b = _driehoeken(b, punt, bol)
    bvh_a = BVHTree.FromPolygons(punten_a, tris_a)
    voor_as = Vector(lid).cross(Vector(buig)).normalized()
    voor = _grens(bvh_a, punten_b, tris_b, punt, voor_as, MAX_VOOR, 5.0)
    achter = _grens(bvh_a, punten_b, tris_b, punt, -voor_as, MAX_ACHTER, 0.5)
    return voor, achter


def tekst(voor, stand):
    """Wat het paneel en de melding laten zien: het gemeten bereik, nooit meer dan de stand."""
    return f"Bends 0° to {min(int(round(voor)), int(stand))}°"
