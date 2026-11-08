"""Passingkleur als materiaal, zodat hij te zien is in de standaard Solid-weergave (kleur volgens Material).

Het figuur houdt zijn eigen materiaal (of geen). Alleen een ring rond de snede krijgt de passingkleur:
de vlakken binnen RING_MM van het snijvlak, plus kogel of pen, nek en kom. Daarvoor komt er één
materiaalvak bij met het gedeelde passingmateriaal ("Click Joints groen" enz.), en die vlakken krijgen
dat vak als material_index. Het rode teken (draadbol) krijgt het materiaal op elk vak, zoals eerst."""
import bpy
import numpy as np

from . import passing

PREFIX = "Click Joints "
RING_MM = 3.0      # zo ver van het snijvlak (langs de as) kleuren de vlakken mee
RAND_MM = 0.4      # bij de kom en kogel: tot zo ver buiten kom of pen (de wand is altijd dikker, minstens 0,8 mm)


def materiaal(kleur):
    """Geeft het gedeelde materiaal voor deze passing, en maakt het als het nog niet bestaat."""
    naam = PREFIX + kleur
    mat = bpy.data.materials.get(naam)
    if mat is None:
        mat = bpy.data.materials.new(naam)
    rgba = passing.KLEUREN[kleur]
    mat.diffuse_color = rgba           # Solid-weergave (Material) en Workbench
    mat.roughness = 0.6
    mat.metallic = 0.0
    boom = getattr(mat, "node_tree", None)  # ook in Material Preview en de render dezelfde kleur
    bsdf = boom.nodes.get("Principled BSDF") if boom is not None else None
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = rgba
    return mat


def kleur_teken(ob, kleur):
    """Rode draadbol: het passingmateriaal op elk materiaalvak (gekoppeld aan het object)."""
    mat = materiaal(kleur)
    if ob.data is not None and len(ob.material_slots) == 0:
        ob.data.materials.append(None)
    for vak in ob.material_slots:
        vak.link = "OBJECT"
        vak.material = mat
    ob.color = passing.KLEUREN[kleur]


def in_ring(centra, snijpunt, as_, r, s, u):
    """Bool per vlakcentrum (n x 3, wereld = mesh, want de delen staan in wereldcoördinaten):
    binnen RING_MM van het snijvlak, of bij kogel, pen, nek of kom (dicht bij de as, tot boven de kom)."""
    rel = centra - np.asarray(snijpunt, dtype=np.float64)
    as_ = np.asarray(as_, dtype=np.float64)
    as_ = as_ / np.linalg.norm(as_)
    h = rel @ as_
    radiaal = np.linalg.norm(rel - np.outer(h, as_), axis=1)
    band = np.abs(h) <= RING_MM * u
    gewricht = (radiaal <= r + s + RAND_MM * u) & (h >= -RING_MM * u) & (h <= 2.5 * r + s + RAND_MM * u)
    return band | gewricht


def vlakcentra(me):
    n = len(me.polygons)
    c = np.empty(n * 3, dtype=np.float64)
    me.polygons.foreach_get("center", c)
    return c.reshape(n, 3)


def kleur_deel(ob, kleur, snijpunt, as_, r, s, u):
    """Voegt een vak met het passingmateriaal toe en zet de vlakken in de ring op dat vak.
    Vorm en vlakken veranderen niet, dus het deel blijft gesloten en de STL blijft gelijk."""
    mat = materiaal(kleur)
    me = ob.data
    if len(me.materials) == 0:
        me.materials.append(None)  # vak 0: het eigen (lege) materiaal van het figuur
    namen = [m.name if m else None for m in me.materials]
    if mat.name in namen:
        index = namen.index(mat.name)
    else:
        me.materials.append(mat)
        index = len(me.materials) - 1
    n = len(me.polygons)
    idx = np.empty(n, dtype=np.int32)
    me.polygons.foreach_get("material_index", idx)
    ring = in_ring(vlakcentra(me), snijpunt, as_, r, s, u)
    idx[ring] = index
    me.polygons.foreach_set("material_index", idx)
    me.update()
    ob["cj_ring_vak"] = index
    ob["cj_ring_deel"] = round(float(ring.mean()), 4) if n else 0.0
