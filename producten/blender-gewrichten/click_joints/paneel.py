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
        stap.label(text="1  Place", icon="PIVOT_CURSOR")
        stap.label(text=f"Mesh: {ob.name if ob else 'select a mesh'}")
        if schaal.buiten_bereik(ob, context.scene):
            let = stap.box()
            let.alert = True
            let.label(text=f"Mesh is {schaal.maat_mm(ob, context.scene):.4g} mm in size", icon="ERROR")
            let.label(text="Expected 5 to 500 mm: is the unit right?")
            grote_knop(let, "click_joints.zet_om_mm", "Convert to mm", "DRIVER_DISTANCE")
        stap.label(text="Shift + right click sets the 3D cursor")
        stap.row(align=True).prop(inst, "as_bron", expand=True)
        if ob is not None and "cj_gesloten" in ob and not ob["cj_gesloten"]:
            stap.label(text="Mesh is not watertight", icon="ERROR")
            stap.prop(inst, "voxel_mm")
            grote_knop(stap, "click_joints.maak_gesloten", "Make watertight", "MOD_REMESH")
        else:
            grote_knop(stap, "click_joints.controleer", "Check mesh", "VIEWZOOM")

        stap = layout.box()
        stap.label(text="2  Joint", icon="MESH_UVSPHERE")
        stap.row(align=True).prop(inst, "soort", expand=True)
        rij = stap.row(align=True)
        rij.prop(inst, "kogel_mm")
        rij.prop(inst, "kogel_auto", toggle=True)
        stap.prop(inst, "speling_mm", slider=True)
        grote_knop(stap, "click_joints.plaats", "Place joint", "MOD_BOOLEAN")
        stap.prop(inst, "uit_elkaar", icon="MOD_EXPLODE")

        stap = layout.box()
        stap.label(text="3  Fit and export", icon="EXPORT")
        kleur = ob.get("cj_passing") if ob else None
        if kleur:
            hoofd, _, reden = passing.fit_tekst(kleur, ob.get("cj_wand_mm", -1.0)).partition(" (")
            stap.label(text=hoofd, icon=passing.ICONEN[kleur])
            if reden:  # op een eigen regel, anders kapt Blender de tekst af
                stap.label(text=reden.rstrip(")").capitalize(), icon="BLANK1")
            if ob.get("cj_wand_mm", -1.0) >= 0 and not reden:  # bij Tight staat de wand al in de reden
                stap.label(text=f"Wall: {ob['cj_wand_mm']:.2f} mm")
            if "cj_speling_gemeten_mm" in ob:
                stap.label(text=f"Clearance measured: {ob['cj_speling_gemeten_mm']:.3f} mm")
        else:
            stap.label(text="No joint yet")
        stap.prop(inst, "exportmap")
        tip = exporteer.hint(context.scene)
        if tip:
            for i, regel in enumerate(tip.split(" next to ")):
                stap.label(text=regel if i == 0 else "next to " + regel, icon="INFO" if i == 0 else "BLANK1")
        grote_knop(stap, "click_joints.exporteer", "Export STL", "FILE_3D")


KLASSEN = (CLICK_JOINTS_PT_paneel,)
