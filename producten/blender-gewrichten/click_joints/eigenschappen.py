"""Instellingen van Click Joints, per scene opgeslagen (scene.click_joints)."""
import bpy
from bpy.props import EnumProperty, FloatProperty, PointerProperty, StringProperty


class ClickJointsInstellingen(bpy.types.PropertyGroup):
    speling_mm: FloatProperty(
        name="Speling (mm)", description="Ruimte tussen kogel en kom in millimeter",
        default=0.2, min=0.05, max=1.0, step=1, precision=2)
    kogel_mm: FloatProperty(
        name="Diameter (mm)", description="Diameter van de kogel of pen in millimeter",
        default=5.0, min=1.0, max=50.0, step=10, precision=1)
    soort: EnumProperty(
        name="Soort", items=(("KOGEL", "Kogel", "Kogel en kom, draait alle kanten op"),
                             ("PEN", "Pen", "Pen en gat, draait om één as")),
        default="KOGEL")
    as_bron: EnumProperty(
        name="As", items=(("KIJK", "Kijkrichting", "As langs de kijkrichting van de 3D-weergave"),
                          ("CURSOR", "Cursor", "As langs de Z-as van de 3D-cursor")),
        default="KIJK")
    voxel_mm: FloatProperty(
        name="Voxel (mm)", description="Voxelgrootte voor Maak gesloten in millimeter",
        default=0.5, min=0.05, max=10.0, step=5, precision=2)
    exportmap: StringProperty(
        name="Map", description="Map voor de STL-bestanden. Leeg: map click_joints naast het .blend-bestand",
        default="", subtype="DIR_PATH")  # leeg, want Blender kleurt een pad dat (nog) niet bestaat rood


KLASSEN = (ClickJointsInstellingen,)


def koppel():
    bpy.types.Scene.click_joints = PointerProperty(type=ClickJointsInstellingen)


def ontkoppel():
    del bpy.types.Scene.click_joints


def eenheid_per_mm(scene):
    """Hoeveel Blender-eenheden één millimeter is, volgens de eenheidschaal van de scene."""
    return 1.0 / (scene.unit_settings.scale_length * 1000.0)
