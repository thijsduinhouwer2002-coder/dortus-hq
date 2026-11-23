"""Exploded view: the pieces stand a little apart in the viewport (delta_location), the mesh stays put.
echte_plek sets the shift to zero for a moment, so the export always has the real position."""
from contextlib import contextmanager

import bpy
from mathutils import Vector

from .eigenschappen import eenheid_per_mm

FACTOR = 0.25  # each piece moves this part of its distance from the middle outward


def stukken(scene):
    return [o for o in scene.objects if o.get("sj_stuk")]


def zet(scene):
    u = eenheid_per_mm(scene)
    aan = scene.split_joints.uit_elkaar
    midden = Vector(scene.get("sj_midden_mm", (0.0, 0.0, 0.0)))
    for o in stukken(scene):
        if aan:
            o.delta_location = (Vector(o.get("sj_midden_mm", midden)) - midden) * FACTOR * u
        else:
            o.delta_location = (0.0, 0.0, 0.0)


@contextmanager
def echte_plek(lijst):
    oud = [tuple(o.delta_location) for o in lijst]
    for o in lijst:
        o.delta_location = (0.0, 0.0, 0.0)
    bpy.context.view_layer.update()
    try:
        yield
    finally:
        for o, d in zip(lijst, oud):
            o.delta_location = d
        bpy.context.view_layer.update()
