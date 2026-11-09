"""Betaalde functies van Click Joints (alleen in de betaalde build, zie e2e/maak_zip.sh).

Het scharnier met eindstop (ontwerp betaald v1.1 in ontwerp.md): vorm in scharnier_vorm.py, operator en
paneelknoppen in scharnier.py. Ook de
weigering als de gratis versie uit een andere repository ook aan staat: zelfde id, dus anders botsen
operators, panelen en scene.click_joints."""
import bpy

from .. import uit_elkaar
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


_oude_afstand = [None]


def _afstand(ob):
    """Eis 6: Exploded view schuift deel B van een scharnier 1,5 keer de wangdiameter (3 Rn = 3 cj_naad_r) langs
    de lidas; de tong reikt tot R onder H en de wangen van A tot Rn - s/2 erboven, dus de tong komt helemaal uit
    de vork. Anders (kogel) de functie van het gratis deel, dat zelf niet verandert."""
    if ob.get("cj_soort") == "SCHARNIER":
        return uit_elkaar.FACTOR * 2.0 * float(ob.get("cj_naad_r", 0.0))
    return _oude_afstand[0](ob)


def register():
    # uit_elkaar.zet (en via zet_alle ook bij_wissel) zoekt afstand op in de module, dus neemt dit omhulsel mee.
    if _oude_afstand[0] is None:
        _oude_afstand[0] = uit_elkaar.afstand
        uit_elkaar.afstand = _afstand
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
    if _oude_afstand[0] is not None:
        uit_elkaar.afstand = _oude_afstand[0]
        _oude_afstand[0] = None
