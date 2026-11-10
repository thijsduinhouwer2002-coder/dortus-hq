"""Groene passingband van het scharnier (Daan, punt 4 van de Pro-winkelplaatjes, 10 nov): zoals de ring van de kogel
(kleur.kleur_deel van het gratis deel, dat niet verandert) krijgen de vlakken langs de naad en rond de knokkel het
gedeelde materiaal "Click Joints Good fit".

Eerlijk: een scharnier wordt alleen geplaatst als de passing goed is (scharnier_neus.maten_neus weigert Tight), dus
groen is altijd waar. Welke vlakken: die van A die binnen speling + BAND_MM van B liggen, en andersom, in de rechte
stand (echte_matrix, dus zonder pose en Exploded view). Alleen vlakken binnen de bol rond het draaipunt worden
bekeken, zodat het ook op een arm van 261K vlot gaat.

Alleen weergave: vorm, vlakken en hoekpunten veranderen niet, alleen material_index; STL en 3MF blijven gelijk."""
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

from .. import kleur as kleuren
from ..uit_elkaar import echte_matrix

BAND_MM = 2.0   # zoals RING_MM 3 van de kogel, iets smaller omdat de naad van het scharnier langer is


def _wereld(ob):
    me = ob.data
    n = len(me.vertices)
    co = np.empty(n * 3, dtype=np.float64)
    me.vertices.foreach_get("co", co)
    mw = np.array(echte_matrix(ob), dtype=np.float64)
    return co.reshape(n, 3) @ mw[:3, :3].T + mw[:3, 3]


def _centra(ob):
    me = ob.data
    n = len(me.polygons)
    c = np.empty(n * 3, dtype=np.float64)
    me.polygons.foreach_get("center", c)
    mw = np.array(echte_matrix(ob), dtype=np.float64)
    return c.reshape(n, 3) @ mw[:3, :3].T + mw[:3, 3]


def _bvh(ob, midden, bol):
    me = ob.data
    me.calc_loop_triangles()
    co = _wereld(ob)
    tri = np.empty(len(me.loop_triangles) * 3, dtype=np.int64)
    me.loop_triangles.foreach_get("vertices", tri)
    tri = tri.reshape(-1, 3)
    binnen = np.linalg.norm(co - np.asarray(midden), axis=1) <= bol
    tri = tri[binnen[tri].any(axis=1)]
    return BVHTree.FromPolygons(co.tolist(), tri.tolist())


def band(a, b, speling, u, bol):
    """Zet de band op A en B. speling en bol in scene-eenheden, u = eenheden per mm. Geeft {naam: aantal vlakken}."""
    mat = kleuren.materiaal("groen")
    midden = Vector(a["cj_scharnier_punt"])
    grens = speling + BAND_MM * u
    tel = {}
    for ob, ander in ((a, b), (b, a)):
        bvh = _bvh(ander, midden, bol + grens)
        me = ob.data
        if len(me.materials) == 0:
            me.materials.append(None)  # vak 0 blijft het eigen (lege) materiaal van het figuur
        namen = [m.name if m else None for m in me.materials]
        if mat.name in namen:
            vak = namen.index(mat.name)
        else:
            me.materials.append(mat)
            vak = len(me.materials) - 1
        n = len(me.polygons)
        idx = np.empty(n, dtype=np.int32)
        me.polygons.foreach_get("material_index", idx)
        centra = _centra(ob)
        kandidaat = np.flatnonzero(np.linalg.norm(centra - np.asarray(midden), axis=1) <= bol + grens)
        raak = [i for i in kandidaat if bvh.find_nearest(Vector(centra[i]), grens)[0] is not None]
        idx[raak] = vak
        me.polygons.foreach_set("material_index", idx)
        me.update()
        ob["cj_band_vlakken"] = len(raak)
        tel[ob.name] = len(raak)
    return tel
