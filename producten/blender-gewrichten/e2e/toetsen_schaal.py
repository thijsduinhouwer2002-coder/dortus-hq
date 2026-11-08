"""Toetsen voor de schaalwaarschuwing en de lege exportmap (vanuit test_achtergrond.py)."""
import bpy

import figuren
from hulp import addon, log, stap, weg


def blok(naam, maat):
    """Kubus met ribbe `maat` eenheden."""
    import bmesh
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=maat)
    return figuren._object(naam, bm)


def ronde(label, scene_fn, maat_eenheden, verwacht_schaal, verwacht_mm):
    schaal = addon("schaal")
    scene_fn()
    sc = bpy.context.scene
    ob = blok(f"blok_{label}", maat_eenheden)
    figuren.maak_actief(ob)
    bpy.context.view_layer.update()
    voor = schaal.maat_mm(ob, sc)
    waarschuw = schaal.buiten_bereik(ob, sc)
    uitslag = bpy.ops.click_joints.zet_om_mm() if waarschuw else None
    na = schaal.maat_mm(ob, sc)
    log(f"SCHAAL {label}: voor={voor:.4g}mm waarschuwing={waarschuw} uitslag={uitslag} "
        f"eenheidschaal={sc.unit_settings.scale_length} lengte={sc.unit_settings.length_unit} na={na:.4g}mm "
        f"ribbe_eenheden={max(ob.dimensions):.4g}")
    stap(f"schaal {label}: waarschuwing bij {voor:.4g} mm", waarschuw)
    stap(f"schaal {label}: eenheidschaal {verwacht_schaal}", abs(sc.unit_settings.scale_length - verwacht_schaal) < 1e-9)
    stap(f"schaal {label}: figuur nu {verwacht_mm} mm", abs(na - verwacht_mm) < 1e-6 * verwacht_mm)
    stap(f"schaal {label}: figuur zelf niet veranderd", abs(max(ob.dimensions) - maat_eenheden) < 1e-6 * maat_eenheden)  # float32
    stap(f"schaal {label}: geen waarschuwing meer", not schaal.buiten_bereik(ob, sc))
    weg([ob])


def alles():
    schaal = addon("schaal")
    # STL van 80 mm in de standaardscene (meters): 80 eenheden = 80 m. Omzetten: 1 eenheid = 1 mm.
    ronde("STL in meterscene", figuren.meter_scene, 80.0, 0.001, 80.0)
    # In meters gemaakt figuur (0,08 eenheden) in een mm-scene: 0,08 mm. Omzetten: 1 eenheid = 1 m.
    ronde("meters in mm-scene", figuren.mm_scene, 0.08, 1.0, 80.0)
    # Gewone maat: geen waarschuwing, knop niet beschikbaar.
    figuren.mm_scene()
    ob = blok("blok_gewoon", 80.0)
    figuren.maak_actief(ob)
    bpy.context.view_layer.update()
    stap("schaal 80 mm: geen waarschuwing", not schaal.buiten_bereik(ob, bpy.context.scene))
    stap("schaal 80 mm: knop niet beschikbaar", not bpy.ops.click_joints.zet_om_mm.poll())
    weg([ob])
    figuren.mm_scene()

    # Lege exportmap: standaard leeg (Blender kleurt een niet bestaand pad rood) met een hint in het paneel.
    inst = bpy.context.scene.click_joints
    exp = addon("exporteer")
    log(f"MAP: standaard={inst.exportmap!r} hint={exp.hint(bpy.context.scene)!r} "
        f"doel={exp.exportmap(bpy.context.scene)!r}")
    stap("exportmap standaard leeg", inst.exportmap == "")
    stap("exportmap leeg: hint in paneel", bool(exp.hint(bpy.context.scene)))
    stap("exportmap leeg: export gaat naar click_joints", exp.exportmap(bpy.context.scene).rstrip("/\\").endswith("click_joints"))
