"""Opengewerkt beeld: deel B staat een stukje langs de as van deel A af, alleen in de weergave.

De verschuiving zit in delta_location van deel B (location blijft van de gebruiker). De mesh zelf
verandert niet. De export zet de verschuiving even op nul (echte_plek), zodat de STL de echte plek heeft."""
from contextlib import contextmanager

from mathutils import Vector

FACTOR = 1.5  # keer de kogeldiameter


def afstand(ob):
    """Verschuiving van deel B in Blender-eenheden (de kogelstraal staat al in eenheden)."""
    return FACTOR * 2.0 * float(ob.get("cj_kogel_r", 0.0))


def zet(ob, aan):
    if ob.get("cj_deel") != "B" or "cj_as" not in ob:
        return
    if aan:
        ob.delta_location = Vector(ob["cj_as"]).normalized() * afstand(ob)
    else:
        ob.delta_location = (0.0, 0.0, 0.0)


def zet_alle(scene):
    aan = scene.click_joints.uit_elkaar
    for ob in scene.objects:
        zet(ob, aan)


def bij_wissel(inst, context):
    """Update van de instelling uit_elkaar."""
    zet_alle(context.scene)


def echte_matrix(ob):
    """matrix_world zonder de weergaveverschuiving (delta_location telt bij de translatie op, zonder ouder).
    Gebruik dit overal waar een deel naar wereldcoördinaten wordt omgerekend, anders bakt de verschuiving in."""
    m = ob.matrix_world.copy()
    if ob.parent is None:
        m.translation -= ob.delta_location
    return m


@contextmanager
def echte_plek(delen):
    """Alle delen even zonder weergaveverschuiving, daarna weer terug."""
    oud = [(d, tuple(d.delta_location)) for d in delen]
    try:
        for d, _ in oud:
            d.delta_location = (0.0, 0.0, 0.0)
        yield
    finally:
        for d, delta in oud:
            d.delta_location = delta
