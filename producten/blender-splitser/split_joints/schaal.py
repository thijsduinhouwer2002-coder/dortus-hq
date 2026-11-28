"""Scale check, taken over from Click Joints (click_joints/schaal.py): a model in mm loaded in a scene in
meters (the Blender default) is 1000 times too big. Below 10 mm or above 3000 mm the unit is probably wrong.

"Convert to mm" changes the unit scale of the scene, not the model: shape, place and other objects stay
as they are, only the meaning of one unit changes (mm, m or cm)."""
import bpy

from .eigenschappen import eenheid_per_mm
from .plan import maat_tekst

MIN_MM = 10.0
MAX_MM = 3000.0  # a big cosplay prop or statue; a model in mm read as meters is 1000 times more
KEUZES = ((0.001, "MILLIMETERS"), (1.0, "METERS"), (0.01, "CENTIMETERS"))


def maat_mm(ob, scene):
    """Largest size of the object in mm (from the unit scale of the scene)."""
    return max(ob.dimensions) / eenheid_per_mm(scene)


def buiten_bereik(ob, scene):
    if ob is None or ob.type != "MESH":
        return False
    maat = maat_mm(ob, scene)
    return maat > 0 and (maat < MIN_MM or maat > MAX_MM)


def beste_keuze(ob):
    """The first unit scale that puts the model between MIN_MM and MAX_MM, or None."""
    eenheden = max(ob.dimensions)
    for schaal, eenheid in KEUZES:
        if MIN_MM <= eenheden * schaal * 1000.0 <= MAX_MM:
            return schaal, eenheid
    return None


class SPLIT_JOINTS_OT_zet_om_mm(bpy.types.Operator):
    bl_idname = "split_joints.zet_om_mm"
    bl_label = "Convert to mm"
    bl_description = "Set the scene unit scale so the model measures between 10 and 3000 mm. The model does not change"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return buiten_bereik(context.active_object, context.scene)

    def execute(self, context):
        ob = context.active_object
        oud = maat_mm(ob, context.scene)
        keuze = beste_keuze(ob)
        if keuze is None:
            self.report({"WARNING"}, f"No unit (mm, cm or m) gives a size between 10 and 3000 mm "
                                     f"(now {maat_tekst(oud)}). Scale the model yourself.")
            return {"CANCELLED"}
        us = context.scene.unit_settings
        us.system = "METRIC"
        us.scale_length, us.length_unit = keuze
        nieuw = maat_mm(ob, context.scene)
        context.scene["sj_schaal_omgezet"] = [oud, nieuw]
        if context.scene.split_joints.uitslag.startswith("Wrong unit"):
            context.scene.split_joints.uitslag = ""  # the red line of Split to fit is solved (keuring C5)
        self.report({"INFO"}, f"Unit scale {keuze[0]:g}: the model now measures {maat_tekst(nieuw)} (was {maat_tekst(oud)})")
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_zet_om_mm,)
