"""Operator click_joints.exporteer: elk zichtbaar gewrichtsdeel als STL, in millimeter."""
import os
import tempfile

import bpy

from .eigenschappen import eenheid_per_mm


def exportmap(scene):
    pad = scene.click_joints.exportmap or "//click_joints/"
    if pad.startswith("//") and not bpy.data.filepath:
        return os.path.join(tempfile.gettempdir(), "click_joints")
    return bpy.path.abspath(pad)


def delen(context):
    return [o for o in context.view_layer.objects if o.get("cj_deel") and o.visible_get()]


class CLICK_JOINTS_OT_exporteer(bpy.types.Operator):
    bl_idname = "click_joints.exporteer"
    bl_label = "Exporteer STL"
    bl_description = "Schrijf elk zichtbaar gewrichtsdeel als STL-bestand in millimeter"

    def execute(self, context):
        if "stl_export" not in dir(bpy.ops.wm):
            self.report({"ERROR"}, "Deze Blender heeft geen STL-export (nodig: 4.2 of nieuwer)")
            return {"CANCELLED"}
        lijst = delen(context)
        if not lijst:
            self.report({"WARNING"}, "Er zijn nog geen gewrichtsdelen om te exporteren")
            return {"CANCELLED"}
        map_ = exportmap(context.scene)
        os.makedirs(map_, exist_ok=True)
        schaal = 1.0 / eenheid_per_mm(context.scene)  # Blender-eenheden naar mm
        actief = context.view_layer.objects.active
        geschreven = []
        for deel in lijst:
            for o in context.view_layer.objects:
                o.select_set(False)
            deel.select_set(True)
            context.view_layer.objects.active = deel
            pad = os.path.join(map_, bpy.path.clean_name(deel.name) + ".stl")
            bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=schaal,
                                  use_scene_unit=False, ascii_format=False, apply_modifiers=True)
            deel["cj_stl"] = pad
            geschreven.append(pad)
        context.view_layer.objects.active = actief
        context.scene["cj_laatste_export"] = geschreven
        self.report({"INFO"}, f"{len(geschreven)} STL-bestanden in {map_}")
        return {"FINISHED"}


KLASSEN = (CLICK_JOINTS_OT_exporteer,)
