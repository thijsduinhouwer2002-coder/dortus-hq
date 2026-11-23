"""1.2.2: geeft de Manifold-snede een open deel, dan één keer opnieuw snijden met Exact.

Spoor Olaf (23 nov): zelfde figuur gaf in CI 8 gewrichten en lokaal 9, met "no watertight parts" op de
linkerschouder. Manifold rekent parallel; een bijna-platte driehoek op de snede kan dan één open rand geven.
Staat in Pro, niet in het gratis deel (dat blijft gelijk aan de gekeurde stand, toets_zips.py). Pro omhult
daarom `gewricht.snij`, net als snippers.py; deze omhulling komt buitenom, zodat de tweede snede ook de
snippers opruimt.
"""

import bpy

from .. import een_lid

# Alleen voor de test: zoveel keer doen alsof de eerste snede open delen gaf.
FORCEER_OPEN = 0

_oud = [None]
_gw = [None]


def _open(deel_a, deel_b):
    global FORCEER_OPEN
    if FORCEER_OPEN > 0:
        FORCEER_OPEN -= 1
        return True
    return not all(_gw[0].is_gesloten(d.data)[0] for d in (deel_a, deel_b))


def _ruim_extra(hulp, houd):
    for ob in [o for o in hulp.objects if o.name not in houd]:
        me = ob.data
        bpy.data.objects.remove(ob)
        if me is not None and me.users == 0:
            bpy.data.meshes.remove(me)


def _snij(hulp, werk, frame, maat, soort, solver):
    voor = {o.name for o in hulp.objects}
    deel_a, deel_b = _oud[0](hulp, werk, frame, maat, soort, solver)
    if solver != "MANIFOLD" or not _open(deel_a, deel_b):
        return deel_a, deel_b
    _ruim_extra(hulp, voor)
    if een_lid.STAND.get("h") is not None:
        een_lid.STAND["solver"] = "EXACT"
        een_lid.STAND["bronnen"] = {}
    deel_a, deel_b = _oud[0](hulp, werk, frame, maat, soort, "EXACT")
    for d in (deel_a, deel_b):
        d["cj_solver_terugval"] = True
    return deel_a, deel_b


def register(gewricht):
    if _oud[0] is None:
        _gw[0] = gewricht
        _oud[0] = gewricht.snij
        gewricht.snij = _snij


def unregister(gewricht):
    if _oud[0] is not None:
        if gewricht.snij is _snij:
            gewricht.snij = _oud[0]
        _oud[0] = None
        _gw[0] = None
