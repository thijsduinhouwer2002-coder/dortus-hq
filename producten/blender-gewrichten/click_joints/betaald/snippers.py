"""1.1: losse snippers na een snede met één lid weghalen (heupen bewogen 0 graden, 16 nov run 7).

Staat in Pro, niet in het gratis deel: het gratis deel is gekeurd op 014172e en blijft gelijk aan de live zip
(toets_zips.py). Pro omhult daarom `gewricht.snij` (zoals afstand.py `gewricht.te_dicht` omhult); het scharnier
van Pro roept `ruim_snippers` zelf aan.
"""

import bmesh
import bpy

from .. import een_lid
from ..eigenschappen import eenheid_per_mm


def actief():
    """True tijdens een snede die maar één lid snijdt (een_lid.bereid gaf een H)."""
    return een_lid.STAND.get("h") is not None


DUN_MM = 0.15     # volume / oppervlak onder deze waarde: een plaatje dunner dan ±0,3 mm, niet te printen
KLEIN = 0.05      # en hooguit dit deel van de hoekpunten van het hele deel


def ruim_snippers(ob, u):
    """1.1 (heupen bewogen 0 graden, 16 nov run 7): haal losse snippers weg die de snede met H achterlaat.

    H is het lid een fractie groter (elk punt langs zijn normaal naar buiten). In een smalle sleuf (de veersleuf
    van een scharnier, 0,2 mm) schuiven de twee wanden daarbij door elkaar, en dan laat de boolean dunne plaatjes
    van 0,1 mm van die wanden achter in het verkeerde deel. Die raken het andere deel, zodat de beweegproef 0 graden
    meet, en printen kan ze niet. Weg gaat alleen een los stuk dat (1) niet het grootste stuk is, (2) hooguit
    KLEIN van de hoekpunten heeft en (3) volume / oppervlak < DUN_MM (in mm) heeft. Een echt los onderdeel van
    het figuur (een oog, een knoop) is veel dikker en blijft. Geeft het aantal weggehaalde stukken."""
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.verts.ensure_lookup_table()
    gezien = set()
    stukken = []
    for v in bm.verts:
        if v.index in gezien:
            continue
        stapel, ids = [v], []
        gezien.add(v.index)
        while stapel:
            x = stapel.pop()
            ids.append(x)
            for e in x.link_edges:
                w = e.other_vert(x)
                if w.index not in gezien:
                    gezien.add(w.index)
                    stapel.append(w)
        stukken.append(ids)
    if len(stukken) < 2:
        bm.free()
        return 0
    stukken.sort(key=len, reverse=True)
    totaal = len(bm.verts)
    weg = []
    for ids in stukken[1:]:
        if len(ids) > KLEIN * totaal:
            continue
        vlakken = {f for v in ids for f in v.link_faces}
        opp = sum(f.calc_area() for f in vlakken)
        vol = 0.0
        # Run 27: kegels vanaf een punt van het stuk zelf, niet vanaf de oorsprong. Met de oorsprong op 45 mm afstand
        # gaf de afronding (float32) bij een kruimel van 0,08 mm een volume groter dan het echte, en bleef hij staan.
        o = ids[0].co.copy()
        for f in vlakken:  # gesloten stuk: som van de kegels vanaf o (elk vlak als waaier)
            p = [x.co - o for x in f.verts]
            for i in range(1, len(p) - 1):
                vol += p[0].dot(p[i].cross(p[i + 1])) / 6.0
        vol = abs(vol)
        if opp <= 0 or vol / opp < DUN_MM * u:
            weg += ids
    n = 0
    if weg:
        wegset = set(weg)
        n = sum(1 for ids in stukken[1:] if ids[0] in wegset)
        bmesh.ops.delete(bm, geom=list(set(weg)), context="VERTS")
        bm.to_mesh(me)
        me.update()
    bm.free()
    return n


_oud = [None]


def _snij(*args, **kw):
    deel_a, deel_b = _oud[0](*args, **kw)
    if actief():
        u = eenheid_per_mm(bpy.context.scene)
        for d in (deel_a, deel_b):
            d["cj_snippers"] = ruim_snippers(d, u)
    return deel_a, deel_b


def register(gewricht):
    if _oud[0] is None:
        _oud[0] = gewricht.snij
        gewricht.snij = _snij


def unregister(gewricht):
    if _oud[0] is not None:
        if gewricht.snij is _snij:
            gewricht.snij = _oud[0]
        _oud[0] = None
