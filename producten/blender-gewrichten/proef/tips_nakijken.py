"""Bram, 16 nov: de tips van de reeks "Printable joints in Blender" nadoen in de echte Blender met Click Joints 0.1.1.
blender -b --factory-startup --python tips_nakijken.py -- <e2e-map> <zip> <uitmap>"""
import math
import os
import struct
import sys

import bpy

e2e, zip_pad, uit = sys.argv[sys.argv.index("--") + 1:][:3]
sys.path.insert(0, e2e)
import figuren  # noqa: E402
from hulp import addon, delen, log, plaats, speling_meten, weg  # noqa: E402

os.makedirs(uit, exist_ok=True)
bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
log(f"Blender {bpy.app.version_string}")
figuren.mm_scene()
maat = addon("maat")
inst = bpy.context.scene.click_joints


def info(lijst):
    a = next((d for d in lijst if d["cj_deel"] == "A"), None)
    return (a.get("cj_passing"), a.get("cj_wand_mm"), a.get("cj_speling_gemeten_mm")) if a else (None, None, None)


# Tip 1: speling. Per speling: gemeten speling, komstraal, klikopening en de klem bij het inklikken.
staaf = figuren.staaf("staaf10", 5.0)
for s in (0.05, 0.2, 0.4):
    inst.speling_mm, inst.kogel_mm, inst.soort = s, 5.0, "KOGEL"
    m = maat.maten(inst, 1.0)
    log(f"TIP1 speling {s}: kogel_r={m['r']:.3f} kom_r={m['r'] + m['s']:.3f} opening_r={m['open_r']:.3f} "
        f"klem_bij_inklikken(r-opening)={m['r'] - m['open_r']:.3f} mm, per kant tussen kogel en kom={m['s']:.3f}")
    lijst = plaats(f"tip1 s{s}", staaf, (0, 0, 0), (1, 0, 0), speling=s)
    if len(lijst) == 2:
        speling_meten(lijst, s, "TIP1 SPELING")
    log(f"TIP1 s{s} passing/wand/gemeten = {info(lijst)}")
    weg(lijst)

# Tip 2: wand. Staven van verschillende dikte, kogel 5 mm: wand en melding.
for straal in (3.6, 3.9, 4.2, 4.6):
    st = figuren.staaf(f"staaf_r{straal}", straal)
    lijst = plaats(f"tip2 r{straal}", st, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    p, w, _ = info(lijst)
    tekst = addon("passing").fit_tekst(p, w) if p else "geen delen"
    log(f"TIP2 staaf dik {2 * straal} mm, kogel 5: passing={p} wand={w} tekst='{tekst}'")
    weg(lijst)

# Tip 4: Auto op een staaf van 10 mm; daarna 0,5 mm groter.
inst.kogel_auto = True
figuren.zet_cursor((0, 0, 0), (1, 0, 0))
figuren.maak_actief(staaf)
bpy.ops.click_joints.plaats()
lijst = delen()
d = inst.kogel_mm
log(f"TIP4 auto staaf 10 mm: diameter={d} {info(lijst)}")
weg(lijst)
lijst = plaats("tip4 groter", staaf, (0, 0, 0), (1, 0, 0), kogel=d + 0.5)
log(f"TIP4 diameter {d + 0.5}: {info(lijst)}")
weg(lijst)

# Tip 6: pen draait om één as, kogel alle kanten (beschrijving in de add-on).
props = bpy.types.ClickJointsInstellingen.bl_rna.properties["soort"].enum_items if hasattr(
    bpy.types, "ClickJointsInstellingen") else inst.bl_rna.properties["soort"].enum_items
for it in props:
    log(f"TIP6 soort {it.identifier}: {it.name} = {it.description}")

# Tip 8: open mesh.
arm_open = figuren.open_arm()
figuren.zet_cursor((0, 0, 0), (1, 0, 0))
figuren.maak_actief(arm_open)
try:
    r = bpy.ops.click_joints.plaats()
except RuntimeError as fout:
    r = f"RuntimeError: {str(fout).strip()}"
log(f"TIP8 open mesh: uitslag={r} delen={len(delen())}")

# Tip 7: figuur van 0,2 m in de standaard meterscene, export met Blender zelf (standaard) en met Click Joints.
figuren.meter_scene()
bpy.ops.mesh.primitive_cube_add(size=0.2)
kubus = bpy.context.active_object


def stl_maat(pad):
    with open(pad, "rb") as f:
        data = f.read()
    n = struct.unpack("<I", data[80:84])[0]
    zs = []
    for i in range(n):
        v = struct.unpack("<12f", data[84 + 50 * i: 84 + 50 * i + 48])
        zs += [v[5], v[8], v[11]]
    return max(zs) - min(zs)


p = os.path.join(uit, "kubus_blender.stl")
bpy.ops.object.select_all(action="DESELECT")
kubus.select_set(True)
bpy.ops.wm.stl_export(filepath=p, export_selected_objects=True)
log(f"TIP7 kubus 0,2 m, Blender STL-export met standaardinstellingen: hoogte in bestand = {stl_maat(p):.4f} "
    f"(slicer leest dat als mm)")
log(f"TIP7 schaalwaarschuwing add-on: grootste maat in mm = {addon('schaal').grootste_mm(kubus) if hasattr(addon('schaal'), 'grootste_mm') else 'functie?'}")
log("KLAAR")
