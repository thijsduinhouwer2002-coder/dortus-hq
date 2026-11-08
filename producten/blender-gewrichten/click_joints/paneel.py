"""Zijbalk (N), tabblad Click Joints: drie genummerde stappen met elk één grote knop."""
import bpy

from . import exporteer, passing, schaal


def grote_knop(layout, idname, tekst, icoon):
    rij = layout.row()
    rij.scale_y = 1.6
    rij.operator(idname, text=tekst, icon=icoon)


class CLICK_JOINTS_PT_paneel(bpy.types.Panel):
    bl_label = "Click Joints"
    bl_idname = "CLICK_JOINTS_PT_paneel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Click Joints"

    def draw(self, context):
        inst = context.scene.click_joints
        ob = context.active_object
        layout = self.layout

        stap = layout.box()
        stap.label(text="1  Plek", icon="PIVOT_CURSOR")
        stap.label(text=f"Figuur: {ob.name if ob else 'kies een figuur'}")
        if schaal.buiten_bereik(ob, context.scene):
            let = stap.box()
            let.alert = True
            let.label(text=f"Figuur is {schaal.maat_mm(ob, context.scene):.4g} mm groot", icon="ERROR")
            let.label(text="Verwacht tussen 5 en 500 mm: klopt de eenheid?")
            grote_knop(let, "click_joints.zet_om_mm", "Zet om naar mm", "DRIVER_DISTANCE")
        stap.label(text="Shift + rechtsklik zet de 3D-cursor")
        stap.prop(inst, "as_bron", expand=True)
        if ob is not None and "cj_gesloten" in ob and not ob["cj_gesloten"]:
            stap.label(text="Figuur is niet gesloten", icon="ERROR")
            stap.prop(inst, "voxel_mm")
            grote_knop(stap, "click_joints.maak_gesloten", "Maak gesloten", "MOD_REMESH")
        else:
            grote_knop(stap, "click_joints.controleer", "Controleer figuur", "VIEWZOOM")

        stap = layout.box()
        stap.label(text="2  Gewricht", icon="MESH_UVSPHERE")
        stap.prop(inst, "soort", expand=True)
        stap.prop(inst, "kogel_mm")
        stap.prop(inst, "speling_mm", slider=True)
        grote_knop(stap, "click_joints.plaats", "Plaats gewricht", "MOD_BOOLEAN")

        stap = layout.box()
        stap.label(text="3  Controleer en exporteer", icon="EXPORT")
        kleur = ob.get("cj_passing") if ob else None
        if kleur:
            tekst = {"groen": "Past", "oranje": "Krap", "rood": "Te dun"}[kleur]
            stap.label(text=f"Passing: {tekst} ({kleur})", icon=passing.ICONEN[kleur])
            if "cj_wand_mm" in ob:
                stap.label(text=f"Wand: {ob['cj_wand_mm']:.2f} mm")
            if "cj_speling_gemeten_mm" in ob:
                stap.label(text=f"Speling gemeten: {ob['cj_speling_gemeten_mm']:.3f} mm")
        else:
            stap.label(text="Nog geen gewricht")
        stap.prop(inst, "exportmap")
        tip = exporteer.hint(context.scene)
        if tip:
            stap.label(text=tip, icon="INFO")
        grote_knop(stap, "click_joints.exporteer", "Exporteer STL", "FILE_3D")


KLASSEN = (CLICK_JOINTS_PT_paneel,)
