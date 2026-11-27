"""Help (issue #268): the ? in the panel header and right click > Online Manual lead to dortus.com/click-cuts/."""
import bpy

from hulp import stap

VERWACHT = {
    "bpy.ops.split_joints.split_to_fit": "#first-split",
    "bpy.ops.split_joints.passing_maak": "#fit-test",
    "bpy.ops.split_joints.vrije_snede_tekenen": "#free-cut",
    "bpy.ops.split_joints.plan": "#panel",
    "bpy.types.SplitJointsInstellingen.verbinder": "#magnets",
    "bpy.types.SplitJointsInstellingen.plat": "#flat",
    "bpy.types.SplitJointsInstellingen.speling_mm": "#panel",
}


def alles(uitmap):
    from bl_operators.wm import WM_OT_doc_view_manual as Handboek
    for rna_id, anker in VERWACHT.items():
        url = Handboek._lookup_rna_url(rna_id, verbose=False)
        stap(f"handboek {rna_id}", url == "https://dortus.com/click-cuts/" + anker, f"{url}")
    paneel = bpy.types.SPLIT_JOINTS_PT_paneel
    stap("paneel heeft een ?-knop in de kop", hasattr(paneel, "draw_header_preset"))
