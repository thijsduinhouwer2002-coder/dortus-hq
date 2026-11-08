"""Passingkleur als materiaal, zodat hij te zien is in de standaard Solid-weergave (kleur volgens Material).

Elk deel krijgt in al zijn materiaalvakken een materiaal per passing (gedeeld: "Click Joints groen" enz.).
De vakken staan op Object, dus de materialen van de mesh zelf blijven bewaard: zet een vak terug op
Data en het eigen materiaal van het figuur is er weer."""
import bpy

from . import passing

PREFIX = "Click Joints "


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


def kleur_deel(ob, kleur):
    """Zet het passingmateriaal op elk materiaalvak van het object (gekoppeld aan het object)."""
    mat = materiaal(kleur)
    if ob.data is not None and len(ob.material_slots) == 0:
        ob.data.materials.append(None)
    for vak in ob.material_slots:
        vak.link = "OBJECT"
        vak.material = mat
    ob.color = passing.KLEUREN[kleur]  # ook bij Viewport Shading op Object
