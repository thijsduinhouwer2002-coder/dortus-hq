"""Instellingen van Click Joints, per scene opgeslagen (scene.click_joints)."""
import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty, PointerProperty, StringProperty

from . import uit_elkaar as _uit


class ClickJointsInstellingen(bpy.types.PropertyGroup):
    speling_mm: FloatProperty(
        name="Clearance (mm)", description="Gap between ball and socket in millimeters",
        default=0.2, min=0.05, max=1.0, step=1, precision=2)
    kogel_mm: FloatProperty(
        name="Diameter (mm)", description="Diameter of the ball or pin in millimeters",
        default=5.0, min=1.0, max=50.0, step=10, precision=1)
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
    exportmap: StringProperty(
        name="Folder", description="Folder for the STL files. Empty: click_joints folder next to the .blend file",
        default="", subtype="DIR_PATH")  # leeg, want Blender kleurt een pad dat (nog) niet bestaat rood
    uit_elkaar: BoolProperty(
        name="Exploded view", description="Show part B a little apart along the joint axis, so you see the "
        "ball. Only in the viewport: the STL export uses the real position",
        default=True, update=_uit.bij_wissel)


KLASSEN = (ClickJointsInstellingen,)


def koppel():
    bpy.types.Scene.click_joints = PointerProperty(type=ClickJointsInstellingen)


def ontkoppel():
    del bpy.types.Scene.click_joints


def eenheid_per_mm(scene):
    """Hoeveel Blender-eenheden één millimeter is, volgens de eenheidschaal van de scene."""
    return 1.0 / (scene.unit_settings.scale_length * 1000.0)
