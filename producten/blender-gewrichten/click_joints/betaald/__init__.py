"""Betaalde functies van Click Joints (alleen in de betaalde build, zie e2e/maak_zip.sh).

Het scharnier met eindstop (ontwerp betaald v1.1 in ontwerp.md): vorm in scharnier_vorm.py, operator en
paneelknoppen in scharnier.py. Ook de
weigering als de gratis versie uit een andere repository ook aan staat: zelfde id, dus anders botsen
operators, panelen en scene.click_joints."""
import bpy

from . import scharnier

ACTIEF = True
KLASSEN = scharnier.KLASSEN
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
    # Keuze voor de knoppen in het paneel (niet in de .blend, zoals een knop in een werkbalk).
    bpy.types.WindowManager.cj_flip_bend = bpy.props.BoolProperty(
        name="Flip bend", default=False, description="Bend the other way: the end stop moves to the other side")
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.append(scharnier.teken_knop)


def unregister():
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.remove(scharnier.teken_knop)
    if hasattr(bpy.types.WindowManager, "cj_flip_bend"):
        del bpy.types.WindowManager.cj_flip_bend
    for k in reversed(KLASSEN):
        bpy.utils.unregister_class(k)
