"""1.2.2: geeft de Manifold-snede een open deel, dan één keer opnieuw snijden met Exact.

Spoor Olaf (23 nov): zelfde figuur gaf in CI 8 gewrichten en lokaal 9, met "no watertight parts" op de
linkerschouder. Manifold rekent parallel; een bijna-platte driehoek op de snede kan dan één open rand geven.
Staat in Pro, niet in het gratis deel (dat blijft gelijk aan de gekeurde stand, toets_zips.py). Pro omhult
daarom `gewricht.snij`, net als snippers.py; deze omhulling komt buitenom, zodat de tweede snede ook de
snippers opruimt.
Omdat de operator `cj_solver` pas na de snede via `gewricht.markeer` op de delen zet (met de eerste solver),
omhult deze module ook `markeer`: een deel met `cj_solver_terugval` krijgt daarna `cj_solver` = "EXACT".
Registreren na afstand.py, zodat deze omhulling van markeer buitenom zit (afmelden gaat in omgekeerde volgorde).
"""

import bmesh
import bpy

from .. import een_lid

# Alleen voor de test: zoveel keer doen alsof de snede open delen gaf. 1: de eerste snede (dan de terugval);
# 2: ook de tweede snede (dan haalt de toets echt één vlak uit deel A, zodat de operator zelf netjes weigert).
FORCEER_OPEN = 0

_oud = [None]
_oud_markeer = [None]
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


def _maak_open(ob):
    """Alleen voor de test: haalt één vlak weg, zodat het deel echt een open rand heeft."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.faces.ensure_lookup_table()
    if bm.faces:
        bmesh.ops.delete(bm, geom=[bm.faces[0]], context="FACES_ONLY")
    bm.to_mesh(ob.data)
    bm.free()


def _snij(hulp, werk, frame, maat, soort, solver):
    voor = {o.name for o in hulp.objects}
    deel_a, deel_b = _oud[0](hulp, werk, frame, maat, soort, solver)
    _herstel(deel_a, deel_b, solver == "EXACT")  # 1.2.3: randen met 4 vlakken splitsen (en na Exact opschonen)
    if solver != "MANIFOLD" or not _open(deel_a, deel_b):
        return deel_a, deel_b
    _ruim_extra(hulp, voor)
    if een_lid.STAND.get("h") is not None:
        een_lid.STAND["solver"] = "EXACT"
        een_lid.STAND["bronnen"] = {}
    deel_a, deel_b = _oud[0](hulp, werk, frame, maat, soort, "EXACT")
    global FORCEER_OPEN
    if FORCEER_OPEN > 0:  # test: ook de tweede snede open, de operator moet zelf weigeren
        FORCEER_OPEN -= 1
        _maak_open(deel_a)
    _herstel(deel_a, deel_b, True)
    for d in (deel_a, deel_b):
        d["cj_solver_terugval"] = True
    return deel_a, deel_b


def _herstel(deel_a, deel_b, exact=False):
    from . import herstel
    if exact:  # 1.2.3: na een Exact-snede ook bijna samenvallende punten samenvoegen (herstel.opschonen)
        from ..eigenschappen import eenheid_per_mm
        herstel.na_exact((deel_a, deel_b), eenheid_per_mm(bpy.context.scene))
    elif not all(_gw[0].is_gesloten(d.data)[0] for d in (deel_a, deel_b)):
        herstel.herstel((deel_a, deel_b))


def _markeer(ob, kleur, gegevens, maat=None, u=1.0):
    _oud_markeer[0](ob, kleur, gegevens, maat, u)
    if ob.get("cj_solver_terugval"):
        ob["cj_solver"] = "EXACT"


def register(gewricht):
    if _oud[0] is None:
        _gw[0] = gewricht
        _oud[0] = gewricht.snij
        gewricht.snij = _snij
    if _oud_markeer[0] is None:
        _oud_markeer[0] = gewricht.markeer
        gewricht.markeer = _markeer


def unregister(gewricht):
    if _oud[0] is not None:
        if gewricht.snij is _snij:
            gewricht.snij = _oud[0]
        _oud[0] = None
        _gw[0] = None
    if _oud_markeer[0] is not None:
        if gewricht.markeer is _markeer:
            gewricht.markeer = _oud_markeer[0]
        _oud_markeer[0] = None
