"""Betaalde functies van Click Joints (alleen in de betaalde build, zie e2e/maak_zip.sh).

Nog leeg: het scharnier met eindstop komt hier (ontwerp betaald v1.1 in ontwerp.md). Wel al de
weigering als de gratis versie uit een andere repository ook aan staat: zelfde id, dus anders botsen
operators, panelen en scene.click_joints."""
import bpy

ACTIEF = True
KLASSEN = ()
MELDING = "Disable the free Click Joints first. Your settings stay in the .blend file."


def andere_versies(namen, eigen):
    """Modules van andere Click Joints-installaties (zelfde id, andere repository) die aan staan."""
    return [n for n in namen if n != eigen and (n == "click_joints" or n.endswith(".click_joints"))]


def weiger_dubbel(eigen):
    namen = [a.module for a in bpy.context.preferences.addons]
    if andere_versies(namen, eigen):
        raise RuntimeError(MELDING)


def register():
    for k in KLASSEN:
        bpy.utils.register_class(k)


def unregister():
    for k in reversed(KLASSEN):
        bpy.utils.unregister_class(k)
