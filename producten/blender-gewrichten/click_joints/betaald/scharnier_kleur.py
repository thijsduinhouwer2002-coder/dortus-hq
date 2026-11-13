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


def _normalen(ob):
    me = ob.data
    n = len(me.polygons)
    nn = np.empty(n * 3, dtype=np.float64)
    me.polygons.foreach_get("normal", nn)
    m3 = np.array(echte_matrix(ob), dtype=np.float64)[:3, :3]
    w = nn.reshape(n, 3) @ np.linalg.inv(m3)   # rij-vector maal M^-1 = M^-T maal n: goed ook bij scheve schaal
    lengte = np.linalg.norm(w, axis=1)
    lengte[lengte == 0] = 1.0
    return w / lengte[:, None]


def strak(ob, s, u):
    """1.0.1 (Daan moet 1, 10 nov): hele vlakken in plaats van losse driehoeken binnen een afstand. Een vlak hoort
    bij de band als het op een van de cilinders om H ligt die het scharnier zelf sneed: op B de knokkel (straal R,
    over de tong) en de naad (Rn + s/2, naast de tong), op A de holle cilinder (R + s, in de gleuf) en de wangen
    (Rn - s/2). Die vlakken zijn door de snede begrensd, dus de rand van het groen is de rand van de vorm: geen
    trapjes, en geen losse strepen op het been (dat ligt op een andere straal of staat niet loodrecht op H).
    Geeft de vlaknummers."""
    p = np.array(ob["cj_scharnier_punt"], dtype=np.float64)
    hx = np.array(Vector(ob["cj_scharnier_as"]).normalized())
    hy = np.array(Vector(ob["cj_buigkant"]).normalized())
    hz = np.array(Vector(ob["cj_as"]).normalized())
    r, rn, tw = float(ob["cj_knokkel_r"]), float(ob["cj_naad_r"]), float(ob["cj_tong_half"])
    c = _centra(ob) - p
    x, y, z = c @ hx, c @ hy, c @ hz
    rho = np.hypot(y, z)
    rad = (np.outer(y, hy) + np.outer(z, hz)) / np.maximum(rho, 1e-12)[:, None]
    loodrecht = np.abs(np.einsum("ij,ij->i", _normalen(ob), rad)) > 0.95   # normaal langs de straal: cilinderwand
    tol = 0.25 * s + 0.01 * rn + 0.05 * u   # 64 zijden: middelpunt van een zijvlak ligt 0,12% binnen de straal
    if ob.get("cj_deel") == "B":
        ringen = ((r, np.abs(x) <= tw + tol), (rn + s / 2, np.abs(x) >= tw - tol))
    else:
        ringen = ((r + s, np.abs(x) <= tw + s + tol), (rn - s / 2, np.abs(x) >= tw + s - tol))
    op = np.zeros(len(c), dtype=bool)
    for straal, binnen in ringen:
        op |= binnen & (np.abs(rho - straal) <= tol)
    # alleen de wanden bij het scharnier zelf (de naad en wang lopen niet verder dan de huid van het lid)
    breed = float(ob.get("cj_breedte", tw + 2.0 * rn))   # halve breedte van het lid langs H (sinds 1.0.1 bewaard)
    op &= loodrecht & (np.abs(x) <= breed + tol)
    return np.flatnonzero(op)


def band(a, b, speling, u, bol):
    """Zet de band op A en B. speling en bol in scene-eenheden, u = eenheden per mm. Geeft {naam: aantal vlakken}.
    Sinds 1.0.1 met hele cilindervlakken (strak); valt dat leeg uit (oude scharnieren zonder alle maten), dan de
    oude manier met een afstand."""
    mat = kleuren.materiaal("groen")
    midden = Vector(a["cj_scharnier_punt"])
    grens = speling + BAND_MM * u
    tel = {}
    for ob, ander in ((a, b), (b, a)):
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
        raak = []
        if all(k in ob for k in ("cj_scharnier_as", "cj_naad_r", "cj_tong_half", "cj_deel")):
            raak = strak(ob, speling, u).tolist()
            ob["cj_band_soort"] = "strak"
        if not raak:
            bvh = _bvh(ander, midden, bol + grens)
            centra = _centra(ob)
            kandidaat = np.flatnonzero(np.linalg.norm(centra - np.asarray(midden), axis=1) <= bol + grens)
            raak = [i for i in kandidaat if bvh.find_nearest(Vector(centra[i]), grens)[0] is not None]
            ob["cj_band_soort"] = "afstand"
        idx[raak] = vak
        me.polygons.foreach_set("material_index", idx)
        me.update()
        ob["cj_band_vlakken"] = len(raak)
        tel[ob.name] = len(raak)
    return tel
