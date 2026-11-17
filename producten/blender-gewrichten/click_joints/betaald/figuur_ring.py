"""Smalle passingring bij een kogel op een hele figuur (Daan 17 nov moet 4: de groene banden bij de heupen lagen
als twee platte blokken op het lijf).

Oorzaak: kleur.in_ring (gratis deel, verandert niet) kleurt elk vlak binnen RING_MM van het snijvlak, over het hele
vlak. Bij een los lid is dat precies de naad; bij een figuur loopt dat vlak ook door het bekken of de schouders, dus
kleurde deel A daar een brede plak mee. Hier, alleen voor figuurdelen in Pro: de straal van het lid bij de snede
meten op deel B (zijn punten binnen RING_MM van het snijvlak, dat is het lid zelf), en op beide delen ringvlakken
verder dan die straal plus een rand van het snijpunt terugzetten op het materiaal van het dichtstbijzijnde vlak
buiten de ring. Kogel, nek en kom blijven groen (die liggen dicht bij de as). Alleen weergave: vorm en STL gelijk."""
import numpy as np
from mathutils import Vector
from mathutils.kdtree import KDTree

from .. import kleur as kleuren

RAND_MM = 1.5   # zo ver buiten de straal van het lid mag de ring nog doorlopen (schuine huid bij de naad)


def _co(ob):
    me = ob.data
    n = len(me.vertices)
    co = np.empty(n * 3, dtype=np.float64)
    me.vertices.foreach_get("co", co)
    co = co.reshape(n, 3)
    mw = np.array(ob.matrix_world, dtype=np.float64)
    return co @ mw[:3, :3].T + mw[:3, 3]


def _radiaal(punten, snijpunt, as_):
    rel = punten - np.asarray(snijpunt, dtype=np.float64)
    a = np.asarray(as_, dtype=np.float64)
    a = a / np.linalg.norm(a)
    h = rel @ a
    return h, np.linalg.norm(rel - np.outer(h, a), axis=1)


def straal_lid(b, u=1.0):
    """Straal van het lid bij de snede, gemeten op deel B. None als er niets te meten is."""
    if "cj_snijpunt" not in b or "cj_as" not in b or len(b.data.vertices) == 0:
        return None
    h, r = _radiaal(_co(b), b["cj_snijpunt"], b["cj_as"])
    dicht = np.abs(h) <= kleuren.RING_MM * u
    if not dicht.any():
        return None
    return float(r[dicht].max())


def smal(ob, straal, u=1.0):
    """Zet ringvlakken buiten straal + RAND_MM terug. Geeft het aantal teruggezette vlakken."""
    vak = ob.get("cj_ring_vak")
    me = ob.data
    n = len(me.polygons)
    if vak is None or straal is None or n == 0 or "cj_snijpunt" not in ob:
        return 0
    idx = np.empty(n, dtype=np.int32)
    me.polygons.foreach_get("material_index", idx)
    c = np.empty(n * 3, dtype=np.float64)
    me.polygons.foreach_get("center", c)
    c = c.reshape(n, 3)
    mw = np.array(ob.matrix_world, dtype=np.float64)
    cw = c @ mw[:3, :3].T + mw[:3, 3]
    _h, r = _radiaal(cw, ob["cj_snijpunt"], ob["cj_as"])
    ring = idx == int(vak)
    terug = ring & (r > straal + RAND_MM * u)
    buiten = np.nonzero(~ring)[0]
    if not terug.any() or len(buiten) == 0:
        return 0
    boom = KDTree(len(buiten))
    for i, j in enumerate(buiten):
        boom.insert(Vector(c[j]), i)
    boom.balance()
    for j in np.nonzero(terug)[0]:
        _p, i, _d = boom.find(Vector(c[j]))
        idx[j] = idx[buiten[i]]
    me.polygons.foreach_set("material_index", idx)
    me.update()
    ob["cj_ring_deel"] = round(float((idx == int(vak)).mean()), 4)
    return int(terug.sum())


def smal_paar(delen, u=1.0):
    """Beide delen van een kogel op een figuur. Geeft {naam deel: teruggezet} of {} bij een scharnier."""
    if len(delen) != 2 or any(d.get("cj_soort", "KOGEL") != "KOGEL" for d in delen):
        return {}
    b = next((d for d in delen if d.get("cj_deel") == "B"), None)
    if b is None:
        return {}
    straal = straal_lid(b, u)
    uit = {d.name: smal(d, straal, u) for d in delen}
    for d in delen:
        d["cj_lid_straal_mm"] = round(straal, 2) if straal is not None else -1.0
    return uit
