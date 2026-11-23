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


SNAP_MM = 1e-4  # punten dichter bij elkaar dan dit (in mm) zijn voor de Exact-solver van 4.2 hetzelfde punt


def opschonen(ob, u=1.0):
    """1.2.3, alleen na een Exact-snede (4.2): punten die (bijna) op elkaar liggen samenvoegen en platte vlakjes weghalen.

    Gemeten op de robot van studio-3 in 4.2.23 (run 45273407326, GEZIEN): na de elleboogsnede ligt in deel A bij de
    elleboog een vlakje met twee punten op 0 mm van elkaar. Het deel telt als gesloten, maar elke volgende Exact-snede
    op dat deel maakt er een gat van 3 randen van (lengte 0 en twee keer 6,2 mm), ver van het nieuwe gewricht: nek, knieën,
    schouder en heup vielen daardoor weg (2 gewrichten in plaats van 4). Alleen houden als het deel daarna nog gesloten is
    en het volume (bijna) gelijk is; anders blijft de mesh zoals hij was. Geeft True als er iets veranderde."""
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    v0, n0 = bm.calc_volume(signed=True), len(bm.verts)
    d = SNAP_MM * u
    bmesh.ops.remove_doubles(bm, verts=bm.verts[:], dist=d)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges[:], dist=d)
    veranderd = len(bm.verts) != n0
    goed = (veranderd and all(len(e.link_faces) == 2 for e in bm.edges)
            and abs(bm.calc_volume(signed=True) - v0) <= 1e-6 * max(abs(v0), 1e-9) + 1e-9)
    if goed:
        bm.to_mesh(me)
        me.update()
        ob["cj_opgeschoond"] = ob.get("cj_opgeschoond", 0) + (n0 - len(bm.verts))
    bm.free()
    return goed


def na_exact(delen, u=1.0):
    """Na een Exact-snede: eerst open delen herstellen, dan elk gesloten deel opschonen."""
    from ..gesloten import is_gesloten
    herstel(delen)
    for d in delen:
        if is_gesloten(d.data)[0]:
            opschonen(d, u)
