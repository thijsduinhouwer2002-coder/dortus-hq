"""Instellingen van Click Joints, per scene opgeslagen (scene.click_joints)."""
import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty, PointerProperty, StringProperty

from . import beweeg as _beweeg
from . import uit_elkaar as _uit

_zelf = [False]  # True terwijl Place joint de diameter zelf invult: dan blijft Auto aan


def _handmatig(inst, context):
    """Update van kogel_mm: de gebruiker koos zelf een maat, dus Auto gaat uit."""
    if not _zelf[0]:
        inst.kogel_auto = False


def zet_auto_diameter(inst, mm):
    """Vult de automatische diameter in zonder Auto uit te zetten."""
    _zelf[0] = True
    try:
        inst.kogel_mm = mm
    finally:
        _zelf[0] = False


class ClickJointsInstellingen(bpy.types.PropertyGroup):
    speling_mm: FloatProperty(
        name="Clearance (mm)", description="Gap between ball and socket in millimeters",
        default=0.2, min=0.05, max=1.0, step=1, precision=2)
    kogel_mm: FloatProperty(
        name="Diameter (mm)", description="Diameter of the ball or pin in millimeters",
        default=5.0, min=1.0, max=50.0, step=10, precision=1, update=_handmatig)
    kogel_auto: BoolProperty(
        name="Auto", description="Pick the diameter for you at Place joint: the largest ball with a good fit "
        "(wall 1.5 mm or more), at most 60% of the thickness of the mesh at the cut. Typing a diameter turns this off", default=True)
    soort: EnumProperty(
        name="Type", items=(("KOGEL", "Ball", "Ball and socket, turns in every direction"),
                             ("PEN", "Pin", "Pin and hole, turns around one axis")),
        default="KOGEL")
    as_bron: EnumProperty(
        name="Axis", items=(("KIJK", "View direction", "Axis along the view direction of the 3D viewport"),
                          ("CURSOR", "3D cursor", "Axis along the Z axis of the 3D cursor")),
        default="KIJK")
    voxel_mm: FloatProperty(
        name="Voxel (mm)", description="Voxel size for Make watertight in millimeters",
        default=0.5, min=0.05, max=10.0, step=5, precision=2)
    formaat: EnumProperty(
        name="Format", items=(("STL", "STL", "One binary STL file per part, in millimeters"),
                              ("3MF", "3MF", "One 3MF file per part, in millimeters (Bambu Studio, PrusaSlicer, Cura)")),
        default="STL")
    exportmap: StringProperty(
        name="Folder", description="Folder for the exported files. Empty: click_joints folder next to the .blend file",
        default="", subtype="DIR_PATH")  # leeg, want Blender kleurt een pad dat (nog) niet bestaat rood
    uit_elkaar: BoolProperty(
        name="Exploded view", description="Show part B a little apart along the joint axis, so you see the "
        "ball. Only in the viewport: the export uses the real position",
        default=True, update=_uit.bij_wissel)
    # Beweegproef (ronde k): waaier met het gemeten bereik en een pose die deel B alleen in beeld draait.
    toon_bereik: BoolProperty(
        name="Show bend range", description="Show how far the joint bends, as a protractor in the chosen direction in the viewport",
        default=True)
    pose_graden: FloatProperty(
        name="Bend", description="Tilt part B around the ball, only in the viewport. Past the measured range, "
        "the parts that collide turn red. The export always uses the straight position",
        default=0.0, min=0.0, max=45.0, step=100, precision=0,
        update=_beweeg.bij_pose)
    pose_richting: EnumProperty(
        name="Direction", items=[(str(k), f"{k * 45}\u00b0", f"Tilt toward {k * 45} degrees around the axis")
                                 for k in range(8)],
        default="0", update=_beweeg.bij_pose)


KLASSEN = (ClickJointsInstellingen,)


def koppel():
    bpy.types.Scene.click_joints = PointerProperty(type=ClickJointsInstellingen)


def ontkoppel():
    del bpy.types.Scene.click_joints


def eenheid_per_mm(scene):
    """Hoeveel Blender-eenheden één millimeter is, volgens de eenheidschaal van de scene."""
    return 1.0 / (scene.unit_settings.scale_length * 1000.0)
