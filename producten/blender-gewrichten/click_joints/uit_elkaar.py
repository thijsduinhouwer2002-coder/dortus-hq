"""Opengewerkt beeld en pose: deel B staat een stukje langs de as van deel A af en kan om het kogelmidden
gedraaid staan, alleen in de weergave.

De verschuiving zit in delta_location, de draaiing (pose, ronde k) in delta_rotation van deel B (location en
rotation blijven van de gebruiker). De mesh zelf verandert niet. De export zet beide even op nul (echte_plek),
zodat de STL de echte plek heeft."""
import math
from contextlib import contextmanager

from mathutils import Matrix, Quaternion, Vector

FACTOR = 1.5  # keer de kogeldiameter
RICHTINGEN = 8


def afstand(ob):
    """Verschuiving van deel B in Blender-eenheden (de stralen staan al in eenheden). Kogel: 1,5 keer de
    kogeldiameter. Scharnier (eis 6): 1,5 keer de diameter van de wang (Rn), langs de lidas L (cj_as); de tong
    van B reikt tot R onder H en de wangen van A tot Rn - s/2 erboven, dus 3 Rn haalt de tong helemaal uit de vork."""
    if ob.get("cj_soort") == "SCHARNIER":
        return FACTOR * 2.0 * float(ob.get("cj_naad_r", 0.0))
    return FACTOR * 2.0 * float(ob.get("cj_kogel_r", 0.0))


def richtingen(as_):
    """De 8 richtingen loodrecht op de as (dezelfde als in de bouwproef proef_beweeg.py)."""
    u = as_.orthogonal().normalized()
    w = as_.cross(u).normalized()
    return [u * math.cos(2 * math.pi * k / RICHTINGEN) + w * math.sin(2 * math.pi * k / RICHTINGEN)
            for k in range(RICHTINGEN)]


def pose_q(ob):
    """Draaiing van de pose: de as van deel B kantelt over cj_pose_graden naar richting cj_pose_richting."""
    g = float(ob.get("cj_pose_graden", 0.0))
    if g == 0.0 or "cj_as" not in ob:
        return Quaternion()
    as_ = Vector(ob["cj_as"]).normalized()
    rich = richtingen(as_)[int(ob.get("cj_pose_richting", 0)) % RICHTINGEN]
    return Quaternion(as_.cross(rich), math.radians(g))


def _zet_draai(ob, q):
    if ob.rotation_mode == "QUATERNION" or ob.rotation_mode == "AXIS_ANGLE":
        ob.delta_rotation_quaternion = q
    else:
        ob.delta_rotation_euler = q.to_euler(ob.rotation_mode)


def zet(ob, aan):
    """Weergave van deel B: verschuiving (Exploded view) plus pose om het kogelmidden.
    Echte matrix M = T(p) R S; in beeld T(e) T(c) Q T(-c) M = T(e + c + Q(p - c)) Q R S,
    en Blender rekent de delta-draaiing links van de eigen draaiing (Q R)."""
    if ob.get("cj_deel") != "B" or "cj_as" not in ob:
        return
    e = Vector(ob["cj_as"]).normalized() * afstand(ob) if aan else Vector()
    q = pose_q(ob)
    if "cj_centrum" in ob and ob.parent is None and q != Quaternion():
        p, c = Vector(ob.location), Vector(ob["cj_centrum"])
        ob.delta_location = e + c + q @ (p - c) - p
    else:
        ob.delta_location = e
    _zet_draai(ob, q)


def zet_alle(scene):
    aan = scene.click_joints.uit_elkaar
    for ob in scene.objects:
        zet(ob, aan)


def bij_wissel(inst, context):
    """Update van de instelling uit_elkaar."""
    zet_alle(context.scene)


def echte_matrix(ob):
    """matrix_world zonder weergaveverschuiving en pose (de delta's). Zonder ouder opgebouwd uit location,
    rotation en scale zelf. Gebruik dit overal waar een deel naar wereldcoördinaten wordt omgerekend."""
    if ob.parent is not None:
        return ob.matrix_world.copy()
    if ob.get("cj_deel") != "B":  # alleen deel B krijgt delta's van de add-on; de rest zoals voor ronde k
        m = ob.matrix_world.copy()
        m.translation -= ob.delta_location
        return m
    if ob.rotation_mode == "QUATERNION":
        rot = ob.rotation_quaternion.to_matrix()
    elif ob.rotation_mode == "AXIS_ANGLE":
        hoek, *as_ = ob.rotation_axis_angle
        rot = Matrix.Rotation(hoek, 3, Vector(as_))
    else:
        rot = ob.rotation_euler.to_matrix()
    schaal = Vector([a * b for a, b in zip(ob.scale, ob.delta_scale)])
    return Matrix.LocRotScale(Vector(ob.location), rot, schaal)


@contextmanager
def echte_plek(delen):
    """Alle delen even zonder weergaveverschuiving en pose, daarna weer terug."""
    oud = [(d, tuple(d.delta_location), tuple(d.delta_rotation_euler), tuple(d.delta_rotation_quaternion))
           for d in delen]
    try:
        for d, *_ in oud:
            d.delta_location = (0.0, 0.0, 0.0)
            d.delta_rotation_euler = (0.0, 0.0, 0.0)
            d.delta_rotation_quaternion = (1.0, 0.0, 0.0, 0.0)
        yield
    finally:
        for d, loc, eul, quat in oud:
            d.delta_location = loc
            d.delta_rotation_euler = eul
            d.delta_rotation_quaternion = quat
