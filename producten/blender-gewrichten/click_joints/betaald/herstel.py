"""Pro 1.2.3 (Betrouwbaarheid, 23 nov): een snede met de Exact-solver die een paar randen met 4 vlakken geeft.

Gemeten in Blender 4.2.23 (alleen Exact; runs 45255097554 en 45256924126 op tak claude/betrouwbaar-rig, GEZIEN): na
een snede heeft een deel soms één rand met 4 vlakken, vaak ver van het gewricht (27 tot 93 mm), op een plek waar
twee stukken huid precies tegen elkaar komen. De melding is dan "no watertight parts" en het gewricht valt weg.
Zo'n rand is twee keer twee vlakken die elkaar in een lijn raken; Blender's "split edges" maakt er twee randen van,
elk met 2 vlakken. De vorm verandert niet (geen punt verschuift), alleen de verbinding. Daarna moet het hele deel
gesloten zijn (elke rand 2 vlakken, positief volume), anders blijft alles zoals het was.
Alleen bij weinig zulke randen (`MAX_RANDEN`) en geen enkele andere foute rand: meer is een echt kapotte snede.
"""
import bmesh

MAX_RANDEN = 4


def splits_vier(ob):
    """True als het deel nu gesloten is door randen met 4 vlakken te splitsen; de mesh blijft anders gelijk."""
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    vier = [e for e in bm.edges if len(e.link_faces) == 4]
    anders = sum(1 for e in bm.edges if len(e.link_faces) not in (2, 4))
    if not vier or anders or len(vier) > MAX_RANDEN:
        bm.free()
        return False
    bmesh.ops.split_edges(bm, edges=vier)
    goed = all(len(e.link_faces) == 2 for e in bm.edges) and bm.calc_volume(signed=True) > 0
    if goed:
        bm.to_mesh(me)
        me.update()
        ob["cj_herstel_randen"] = ob.get("cj_herstel_randen", 0) + len(vier)
    bm.free()
    return goed


def herstel(delen):
    """Probeert elk open deel te herstellen; geeft het aantal herstelde delen."""
    from ..gesloten import is_gesloten
    n = 0
    for d in delen:
        if not is_gesloten(d.data)[0] and splits_vier(d):
            n += 1
    return n
