"""Operator click_joints.exporteer: elk zichtbaar gewrichtsdeel als STL, in millimeter."""
import os
import tempfile

import bpy

from .eigenschappen import eenheid_per_mm
from .uit_elkaar import echte_plek


STANDAARD = "//click_joints/"


def exportmap(scene):
    pad = scene.click_joints.exportmap or STANDAARD
    if pad.startswith("//") and not bpy.data.filepath:
        return os.path.join(tempfile.gettempdir(), "click_joints")
    return bpy.path.abspath(pad)


def hint(scene):
    """Korte tekst voor het paneel: waar de STL-bestanden heen gaan als de map leeg is."""
    if scene.click_joints.exportmap:
        return None
    if bpy.data.filepath:
        return "Saves next to the .blend"
    return "Saves to a temporary folder"


def delen(context):
    return [o for o in context.view_layer.objects if o is not None and o.get("cj_deel") and o.visible_get()]


class CLICK_JOINTS_OT_exporteer(bpy.types.Operator):
    bl_idname = "click_joints.exporteer"
    bl_label = "Export STL"
    bl_description = "Write every visible joint part as an STL file in millimeters"

    def execute(self, context):
        if "stl_export" not in dir(bpy.ops.wm):
            self.report({"ERROR"}, "This Blender has no STL export (needs 4.2 or newer)")
            return {"CANCELLED"}
        lijst = delen(context)
        if not lijst:
            self.report({"WARNING"}, "There are no joint parts to export yet")
            return {"CANCELLED"}
        map_ = exportmap(context.scene)
        os.makedirs(map_, exist_ok=True)
        schaal = 1.0 / eenheid_per_mm(context.scene)  # Blender-eenheden naar mm
        actief = context.view_layer.objects.active
        gekozen = [o for o in context.view_layer.objects if o is not None and o.select_get()]
        with echte_plek(lijst):  # opengewerkt beeld even uit: de STL krijgt de echte plek
            geschreven = self.schrijf(context, lijst, map_, schaal)
        context.view_layer.update()
        for o in context.view_layer.objects:  # selectie terug zoals hij was (na Place joint: niets)
            if o is not None:
                o.select_set(o in gekozen)
        context.view_layer.objects.active = actief
        context.scene["cj_laatste_export"] = geschreven
        self.report({"INFO"}, f"{len(geschreven)} STL files in {map_}")
        return {"FINISHED"}

    @staticmethod
    def schrijf(context, lijst, map_, schaal):
        geschreven = []
        for deel in lijst:
            context.view_layer.update()
            for o in context.view_layer.objects:
                if o is not None:
                    o.select_set(False)
            deel.select_set(True)
            context.view_layer.objects.active = deel
            pad = os.path.join(map_, bpy.path.clean_name(deel.name) + ".stl")
            bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=schaal,
                                  use_scene_unit=False, ascii_format=False, apply_modifiers=True)
            deel["cj_stl"] = pad
            geschreven.append(pad)
        return geschreven


KLASSEN = (CLICK_JOINTS_OT_exporteer,)
