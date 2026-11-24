"""Operator split_joints.exporteer: every piece and every pin plate as STL or 3MF, in millimeters.
Same way of writing as Click Joints (exporteer.py and drie_mf.py)."""
import os
import tempfile

import bpy

from . import drie_mf
from .eigenschappen import eenheid_per_mm
from .uit_elkaar import echte_plek

STANDAARD = "//click_cuts/"


def exportmap(scene):
    pad = scene.split_joints.exportmap or STANDAARD
    if pad.startswith("//") and not bpy.data.filepath:
        return os.path.join(tempfile.gettempdir(), "click_cuts")
    return bpy.path.abspath(pad)


def hint(scene):
    if scene.split_joints.exportmap:
        return None
    return "Saves next to the .blend" if bpy.data.filepath else "Saves to a temporary folder"


def bestandsnaam(ob):
    if ob.get("sj_stuk"):
        return f"piece_{int(ob['sj_stuk']):02d}"
    return f"pins_{ob['sj_pen_d']:g}mm_x{int(ob['sj_pennen'])}".replace(".", "_")


def onderdelen(context):
    lijst = [o for o in context.view_layer.objects if o is not None and (o.get("sj_stuk") or o.get("sj_pennen"))]
    return sorted(lijst, key=lambda o: (0, o["sj_stuk"]) if o.get("sj_stuk") else (1, o.name))


class SPLIT_JOINTS_OT_exporteer(bpy.types.Operator):
    bl_idname = "split_joints.exporteer"
    bl_label = "Export"
    bl_description = "Write every piece and the pins as STL or 3MF files in millimeters"

    def execute(self, context):
        formaat = context.scene.split_joints.formaat
        if formaat == "STL" and "stl_export" not in dir(bpy.ops.wm):
            self.report({"ERROR"}, "This Blender has no STL export (needs 4.2 or newer)")
            return {"CANCELLED"}
        lijst = onderdelen(context)
        if not lijst:
            self.report({"WARNING"}, "Split the model first")
            return {"CANCELLED"}
        map_ = exportmap(context.scene)
        os.makedirs(map_, exist_ok=True)
        schaal = 1.0 / eenheid_per_mm(context.scene)
        actief = context.view_layer.objects.active
        gekozen = [o for o in context.view_layer.objects if o is not None and o.select_get()]
        geschreven = []
        with echte_plek([o for o in lijst if o.get("sj_stuk")]):
            for ob in lijst:
                pad = os.path.join(map_, bestandsnaam(ob) + (".3mf" if formaat == "3MF" else ".stl"))
                if formaat == "3MF":
                    ob["sj_3mf_driehoeken"] = drie_mf.schrijf(ob, pad, schaal)
                else:
                    for o in context.view_layer.objects:
                        if o is not None:
                            o.select_set(False)
                    ob.select_set(True)
                    context.view_layer.objects.active = ob
                    bpy.ops.wm.stl_export(filepath=pad, export_selected_objects=True, global_scale=schaal,
                                          use_scene_unit=False, ascii_format=False, apply_modifiers=True)
                ob["sj_bestand"] = pad
                geschreven.append(pad)
        for o in context.view_layer.objects:
            if o is not None:
                o.select_set(o in gekozen)
        context.view_layer.objects.active = actief
        context.scene["sj_laatste_export"] = geschreven
        self.report({"INFO"}, f"{len(geschreven)} {formaat} files in {map_}")
        return {"FINISHED"}


KLASSEN = (SPLIT_JOINTS_OT_exporteer,)
