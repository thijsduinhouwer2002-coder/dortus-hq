"""Schaalwaarschuwing: is het figuur kleiner dan 5 mm of groter dan 500 mm, dan klopt de eenheid
waarschijnlijk niet (bijvoorbeeld een STL in mm geladen in een scene in meters).

"Zet om naar mm" verandert de eenheidschaal van de scene, niet het figuur. Waarom: de vorm, de
plek en de andere objecten blijven precies zoals ze waren, alleen de betekenis van één eenheid
verandert (mm, cm of m). De export in mm volgt daarna vanzelf via eenheid_per_mm. Het figuur
schalen zou ook de cursor, modifiers en andere objecten uit verhouding brengen."""
import bpy

from .eigenschappen import eenheid_per_mm

MIN_MM = 5.0
MAX_MM = 500.0
# (eenheidschaal, lengte-eenheid) in volgorde van voorkeur: 1 eenheid = 1 mm, dan 1 m, dan 1 cm.
KEUZES = ((0.001, "MILLIMETERS"), (1.0, "METERS"), (0.01, "CENTIMETERS"))


def maat_mm(ob, scene):
    """Grootste afmeting van het object in millimeter (volgens de eenheidschaal van de scene)."""
    return max(ob.dimensions) / eenheid_per_mm(scene)


def buiten_bereik(ob, scene):
    if ob is None or ob.type != "MESH":
        return False
    maat = maat_mm(ob, scene)
    return maat > 0 and (maat < MIN_MM or maat > MAX_MM)


def beste_keuze(ob):
    """De eerste eenheidschaal waarbij het figuur tussen 5 en 500 mm valt, of None."""
    eenheden = max(ob.dimensions)
    for schaal, eenheid in KEUZES:
        if MIN_MM <= eenheden * schaal * 1000.0 <= MAX_MM:
            return schaal, eenheid
    return None


class CLICK_JOINTS_OT_zet_om_mm(bpy.types.Operator):
    bl_idname = "click_joints.zet_om_mm"
    bl_label = "Convert to mm"
    bl_description = ("Set the scene unit scale so the mesh measures between 5 and 500 mm. "
                      "The mesh itself does not change")
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return buiten_bereik(context.active_object, context.scene)

    def execute(self, context):
        ob = context.active_object
        oud = maat_mm(ob, context.scene)
        keuze = beste_keuze(ob)
        if keuze is None:
            self.report({"WARNING"}, f"No unit (mm, cm or m) gives a size between 5 and 500 mm "
                                     f"(now {oud:.4g} mm). Scale the mesh yourself.")
            return {"CANCELLED"}
        us = context.scene.unit_settings
        us.system = "METRIC"
        us.scale_length, us.length_unit = keuze
        nieuw = maat_mm(ob, context.scene)
        context.scene["cj_schaal_omgezet"] = [oud, nieuw]
        self.report({"INFO"}, f"Unit scale {keuze[0]:g}: the mesh now measures {nieuw:.1f} mm "
                              f"(was {oud:.4g} mm)")
        return {"FINISHED"}


KLASSEN = (CLICK_JOINTS_OT_zet_om_mm,)
