"""Dortus Proef: lege add-on die alleen bewijst dat laden en testen in de echte Blender werkt."""
import bpy


class DORTUS_OT_hallo(bpy.types.Operator):
    bl_idname = "dortus.hallo"
    bl_label = "Hallo Dortus"
    bl_description = "Zet een vlag op de scene, zodat de test kan zien dat de knop werkt"

    def execute(self, context):
        context.scene["dortus_hallo"] = True
        self.report({"INFO"}, "Hallo van Dortus")
        return {"FINISHED"}


class DORTUS_PT_paneel(bpy.types.Panel):
    bl_label = "Dortus Proef"
    bl_idname = "DORTUS_PT_paneel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Dortus"

    def draw(self, context):
        self.layout.label(text="De test in de echte Blender werkt.")
        self.layout.operator(DORTUS_OT_hallo.bl_idname, icon="CHECKMARK")


KLASSEN = (DORTUS_OT_hallo, DORTUS_PT_paneel)


def register():
    for k in KLASSEN:
        bpy.utils.register_class(k)


def unregister():
    for k in reversed(KLASSEN):
        bpy.utils.unregister_class(k)
