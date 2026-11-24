"""Sidebar (N), tab Click Cuts: printer, one big Split to fit button with a one-line result, Export, and
the four numbered steps folded under More settings."""
import bpy

from . import controle, exporteer, in_een_klik, passingproef, printers, schaal, snedes
from .eigenschappen import bed


def grote_knop(layout, idname, tekst, icoon):
    rij = layout.row()
    rij.scale_y = 1.6
    return rij.operator(idname, text=tekst, icon=icoon)


MAX_RIJEN = 20  # cut rows shown in the panel; more is drawn as one line
ICOON = {"groen": "CHECKMARK", "oranje": "ERROR", "rood": "CANCEL"}


class SPLIT_JOINTS_PT_paneel(bpy.types.Panel):
    bl_label = "Click Cuts"
    bl_idname = "SPLIT_JOINTS_PT_paneel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Click Cuts"

    def draw(self, context):
        scene = context.scene
        inst = scene.split_joints
        layout = self.layout

        # one click: printer, Split to fit, result, export (keuring K3, opdracht hoofdchat 23 nov 23:35)
        layout.label(text="Your printer")
        layout.prop(inst, "printer", text="")
        rij = layout.row()
        rij.scale_y = 2.0
        rij.operator("split_joints.split_to_fit", text="Split to fit", icon="MOD_EXPLODE")
        uit = in_een_klik.uitslag_tekst(scene)
        if inst.uitslag:
            vak = layout.box().column(align=True)
            vak.alert = True
            vak.label(text=inst.uitslag, icon="ERROR")
        elif uit:
            hoofd, detail, goed = uit
            vak = layout.box().column(align=True)
            vak.label(text=hoofd, icon="CHECKMARK" if goed else "ERROR")
            vak.label(text=detail)
            if snedes.snede_objecten(scene):
                vak.label(text="Move a cut in More settings, then Split")
        if uit:
            grote_knop(layout, "split_joints.exporteer", f"Export parts ({inst.formaat})", "EXPORT")
        layout.prop(inst, "meer", icon="TRIA_DOWN" if inst.meer else "TRIA_RIGHT", emboss=False)
        if not inst.meer:
            return

        stap = layout.box()
        stap.label(text="1  Printer", icon="MOD_BUILD")
        stap.prop(inst, "printer", text="")
        if inst.printer == printers.EIGEN:
            rij = stap.row(align=True)
            rij.prop(inst, "eigen_x", text="X")
            rij.prop(inst, "eigen_y", text="Y")
            rij.prop(inst, "eigen_z", text="Z")
        b = bed(scene)
        stap.prop(inst, "marge_mm")
        stap.label(text=f"Usable: {b[0]:.0f} x {b[1]:.0f} x {b[2]:.0f} mm")

        stap = layout.box()
        stap.label(text="2  Cuts", icon="MOD_BOOLEAN")
        ob = context.active_object
        if ob is not None and ob.type == "MESH" and not ob.get("sj_stuk") and "sj_as" not in ob \
                and not ob.get("sj_pennen") and not ob.get("sj_passing") and not ob.get("sj_vrij"):
            if schaal.buiten_bereik(ob, scene):
                let = stap.column(align=True)
                let.alert = True
                let.label(text=f"Model is {schaal.maat_mm(ob, scene):.4g} mm in size", icon="ERROR")
                let.label(text="Wrong unit? (mm model in a meter scene)")
                let.operator("split_joints.zet_om_mm", icon="SETTINGS")
            stap.operator("split_joints.maak_gesloten", icon="MOD_REMESH")
            stap.prop(inst, "voxel_mm")
        grote_knop(stap, "split_joints.plan", "Plan cuts", "GRID")
        lijst = snedes.snede_objecten(scene)
        if lijst:
            kol = stap.column(align=True)
            for s in lijst[:MAX_RIJEN]:
                rij = kol.row(align=True)
                rij.prop(s, "sj_plek_mm", text=f"Cut {snedes.ASNAAM[int(s['sj_as'])]} (mm)")
                rij.operator("split_joints.snede_weg", text="", icon="X").naam = s.name
            if len(lijst) > MAX_RIJEN:
                kol.label(text=f"and {len(lijst) - MAX_RIJEN} more cuts")
            st = snedes.stand(context)
            if st:
                n, goed, groot = st
                if goed is None:
                    stap.label(text=f"{n} cells: too many, remove cuts", icon="ERROR")
                else:
                    stap.label(text=f"{n} cells, {goed} fit the bed", icon="CHECKMARK" if goed == n else "ERROR")
        rij = stap.row(align=True)
        rij.label(text="Add cut:")
        for i, letter in enumerate("XYZ"):
            rij.operator("split_joints.snede_erbij", text=letter).as_ = i

        stap = layout.box()
        stap.label(text="3  Pins and numbers", icon="SNAP_FACE_CENTER")
        stap.prop(inst, "pen_mm")
        stap.prop(inst, "pen_auto")
        stap.prop(inst, "pen_lengte_mm")
        stap.prop(inst, "speling_mm")
        passingproef.teken(stap, context)
        stap.prop(inst, "wand_mm")
        stap.prop(inst, "labels")
        sub = stap.row()
        sub.enabled = inst.labels
        sub.prop(inst, "label_diepte_mm", text="Number depth (mm)")
        grote_knop(stap, "split_joints.split", "Split", "MOD_EXPLODE")

        stap = layout.box()
        stap.label(text="4  Check and export", icon="EXPORT")
        stukken = sorted((o for o in scene.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])
        if stukken:
            stap.prop(inst, "uit_elkaar")
            rij = stap.row(align=True)
            rij.prop(inst, "kleur", expand=True)
            kol = stap.column(align=True)
            for o in stukken:
                kol.label(text=f"{int(o['sj_stuk'])}: {controle.tekst(o)}", icon=ICOON.get(o.get("sj_status"), "DOT"))
            pennen = [o for o in scene.objects if o.get("sj_pennen")]
            for p in pennen:
                kol.label(text=f"{int(p['sj_pennen'])} pins of {p['sj_pen_d']:g} mm, {p['sj_pen_lengte']:g} mm long",
                          icon="DOT")
        if stukken:
            vrij = stap.box()
            vrij.label(text="Free cut (one piece, any angle)", icon="MOD_LINEART")
            rij = vrij.row(align=True)
            rij.operator("split_joints.vrije_snede_erbij", text="Add free cut", icon="ADD")
            rij.operator("split_joints.vrije_snede", text="Cut piece", icon="MOD_BOOLEAN")
        if inst.meldingen:
            vak = stap.column(align=True)
            for regel in inst.meldingen.split("\n")[:8]:
                vak.label(text=regel, icon="INFO")
        rij = stap.row(align=True)
        rij.prop(inst, "formaat", expand=True)
        stap.prop(inst, "exportmap")
        h = exporteer.hint(scene)
        if h:
            stap.label(text=h)
        grote_knop(stap, "split_joints.exporteer", f"Export {inst.formaat}", "EXPORT")


KLASSEN = (SPLIT_JOINTS_PT_paneel,)
