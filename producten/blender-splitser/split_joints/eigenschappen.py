"""Settings of Click Cuts, stored per scene (scene.split_joints)."""
import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty, PointerProperty, StringProperty

from . import passing, printers, verbinders


def _speling(inst, context):
    from . import passingproef
    passingproef.speling_gezet(inst.id_data)


def _onthouden(inst, context):
    from . import passingproef
    passingproef.pas_toe(context)


def _uit_elkaar(inst, context):
    from . import uit_elkaar
    uit_elkaar.zet(context.scene)


def _kleur(inst, context):
    from . import kleuren
    kleuren.zet(inst.id_data)


class SplitJointsInstellingen(bpy.types.PropertyGroup):
    printer: EnumProperty(name="Printer", description="Your printer. Split to fit cuts the model to fit its build volume",
                          items=printers.items(), default="A1", update=_onthouden)
    materiaal: EnumProperty(
        name="Material", description="Your filament. The clearance that fits is remembered per printer and material",
        items=passing.MATERIALEN, default="PLA", update=_onthouden)
    eigen_x: FloatProperty(name="X (mm)", description="Build width of your printer in millimeters",
                           default=200.0, min=20.0, max=2000.0, precision=0)
    eigen_y: FloatProperty(name="Y (mm)", description="Build depth of your printer in millimeters",
                           default=200.0, min=20.0, max=2000.0, precision=0)
    eigen_z: FloatProperty(name="Z (mm)", description="Build height of your printer in millimeters",
                           default=200.0, min=20.0, max=2000.0, precision=0)
    marge_mm: FloatProperty(
        name="Margin (mm)", description="Keep this much room free on every side of the bed",
        default=2.0, min=0.0, max=30.0, precision=1)
    verbinder: EnumProperty(
        name="Joint", description="What holds the pieces together",
        items=(("PIN", "Pins", "Printed round pins in holes on both sides of every cut"),
               ("MAGNET", "Magnets", "A hole for a disc magnet on both sides of every cut. Magnets are not included")),
        default="PIN")
    magneet: EnumProperty(
        name="Magnet (mm)", description="Diameter x thickness of your disc magnets. The hole gets the clearance "
        "on the diameter and 0.1 mm extra depth for glue",
        items=[(k, f"{k} mm", f"Disc magnet {d:g} mm across, {t:g} mm thick") for k, d, t in verbinders.MAGNETEN],
        default="6x2")
    pen_mm: FloatProperty(
        name="Pin diameter (mm)", description="Diameter of the pins. Holes get the clearance on top",
        default=5.0, min=2.0, max=20.0, step=50, precision=1)
    pen_auto: BoolProperty(
        name="Smaller pins on small faces", description="Use a smaller pin (down to 3 mm) where the default "
        "does not fit", default=True)
    pen_lengte_mm: FloatProperty(
        name="Pin length (mm)", description="Total length of a pin. Each hole is half this deep plus 0.3 mm",
        default=12.0, min=4.0, max=60.0, step=50, precision=1)
    speling_mm: FloatProperty(
        name="Clearance (mm)", description="Gap between pin and hole on every side, in millimeters",
        default=0.2, min=0.0, max=1.0, step=1, precision=2, update=_speling)
    wand_mm: FloatProperty(
        name="Min. wall (mm)", description="Keep at least this much material around every hole",
        default=1.2, min=0.4, max=10.0, step=10, precision=1)
    labels: BoolProperty(
        name="Engrave numbers", description="Engrave the piece number and its neighbor on every cut face, "
        "for example 3-5 on piece 3 where it meets piece 5", default=True)
    label_diepte_mm: FloatProperty(
        name="Depth (mm)", description="How deep the numbers go into the cut face",
        default=0.6, min=0.2, max=3.0, step=10, precision=1)
    voxel_mm: FloatProperty(
        name="Voxel (mm)", description="Voxel size for Make watertight in millimeters",
        default=1.0, min=0.05, max=10.0, step=10, precision=2)
    formaat: EnumProperty(
        name="Format", items=(("STL", "STL", "One binary STL file per piece, in millimeters"),
                              ("3MF", "3MF", "One 3MF file per piece, in millimeters")),
        default="STL")
    exportmap: StringProperty(
        name="Folder", description="Folder for the exported files. Empty: click_cuts folder next to the .blend",
        default="", subtype="DIR_PATH")
    plat: BoolProperty(
        name="Lay parts flat", description="Turn every piece so a cut face lies on the bed, only if it still fits "
        "the printer. Otherwise the piece keeps its own way up. Pins and fit test stay as they are", default=True)
    uit_elkaar: BoolProperty(
        name="Exploded view", description="Show the pieces a little apart, only in the viewport. "
        "The export uses the real position", default=True, update=_uit_elkaar)
    kleur: EnumProperty(
        name="Colors", items=(("PIECE", "Per piece", "Every piece its own color, neighbors never the same. Pins in gold. "
                               "Replaces materials on the pieces"),
                              ("CHECK", "Check", "Green fits, orange thin wall, red needs attention")),
        default="PIECE", update=_kleur)
    bron: StringProperty(name="Model", description="The model the cuts belong to", default="")
    uitslag: StringProperty(default="")  # error line of Split to fit; empty: the panel shows the pieces
    meer: BoolProperty(name="More settings", description="Printer margin, cuts, pins, fit test, check and export",
                       default=False)
    meldingen: StringProperty(default="")  # one message per line, from the last split


KLASSEN = (SplitJointsInstellingen,)


def _plek_scene(ob):
    scenes = ob.users_scene
    return scenes[0] if scenes else bpy.context.scene


def _plek_get(ob):
    """Position of a cut plane along its axis in mm (panel shows it rounded to 0.1 mm)."""
    if "sj_as" not in ob:
        return 0.0
    return ob.location[int(ob["sj_as"])] / eenheid_per_mm(_plek_scene(ob))


def _plek_set(ob, waarde):
    if "sj_as" in ob:
        ob.location[int(ob["sj_as"])] = waarde * eenheid_per_mm(_plek_scene(ob))


def koppel():
    bpy.types.Scene.split_joints = PointerProperty(type=SplitJointsInstellingen)
    bpy.types.Object.sj_plek_mm = FloatProperty(
        name="Position", description="Where the cut lies along its axis, in mm (drag or type, G also works)",
        get=_plek_get, set=_plek_set, precision=1, step=10)


def ontkoppel():
    del bpy.types.Object.sj_plek_mm
    del bpy.types.Scene.split_joints


def verbind_opties(inst):
    """Options for verbind_3d.plan_alles from the settings: pins or magnets."""
    if inst.verbinder == "MAGNET":
        return verbinders.magneet_opties(inst.magneet, inst.speling_mm, inst.wand_mm)
    return {"pen_d": inst.pen_mm, "speling": inst.speling_mm, "wand": inst.wand_mm, "auto": inst.pen_auto,
            "min_d": 3.0, "pen_lengte": inst.pen_lengte_mm}


def magneten(scene):
    """{size key: count} of the magnet holes in the pieces of the scene (one magnet per hole)."""
    import json
    tel = {}
    for o in scene.objects:
        if o.get("sj_stuk"):
            for g in json.loads(o.get("sj_gaten", "[]")):
                if g.get("soort") == "magneet":
                    tel[g["magneet"]] = tel.get(g["magneet"], 0) + 1
    return tel


def eenheid_per_mm(scene):
    """Blender units per millimeter, from the unit scale of the scene."""
    return 1.0 / (scene.unit_settings.scale_length * 1000.0)


def bed(scene):
    """Usable build volume (x, y, z) in mm: preset or custom, minus the margin."""
    inst = scene.split_joints
    m = printers.maat(inst.printer, (inst.eigen_x, inst.eigen_y, inst.eigen_z))
    return printers.bruikbaar(m, inst.marge_mm)
