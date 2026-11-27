"""Help: a ? button in the panel header and right click > Online Manual on every Click Cuts button.

Both open the guide on dortus.com in the browser (Blender's own wm.url_open). Click Cuts itself makes no
network connection. Gap from the lat (organisatie/lat/click-cuts.md, Paneel): Cleave has a ? button."""
import bpy

HULP = "https://dortus.com/click-cuts/"

# operator -> part of the guide (anchors on dortus.com/click-cuts/)
STUKKEN = (
    ("bpy.ops.split_joints.split_to_fit", "#first-split"),
    ("bpy.ops.split_joints.exporteer", "#first-split"),
    ("bpy.ops.split_joints.zet_om_mm", "#faq"),
    ("bpy.ops.split_joints.passing_*", "#fit-test"),
    ("bpy.ops.split_joints.vrije_snede*", "#free-cut"),
    ("bpy.ops.split_joints.maak_gesloten", "#panel"),
    ("bpy.ops.split_joints.plan", "#panel"),
    ("bpy.ops.split_joints.snede_*", "#panel"),
    ("bpy.ops.split_joints.split", "#panel"),
    ("bpy.types.splitjointsinstellingen.verbinder", "#magnets"),
    ("bpy.types.splitjointsinstellingen.magneet", "#magnets"),
    ("bpy.types.splitjointsinstellingen.plat", "#flat"),
    ("bpy.types.splitjointsinstellingen.*", "#panel"),
)


def handboek():
    return HULP, STUKKEN


def knop(layout):
    op = layout.operator("wm.url_open", text="", icon="QUESTION", emboss=False)
    op.url = HULP


def koppel():
    bpy.utils.register_manual_map(handboek)


def ontkoppel():
    bpy.utils.unregister_manual_map(handboek)


KLASSEN = ()
