"""Split to fit (in_een_klik.py) and the rounded cut position (sj_plek_mm), called from test_kern.py; also alone:
blender -b --factory-startup --python e2e/toetsen_klik.py -- <zip>

Measured on the meshes, not on what the add-on says:
- one click on a bare box 500 x 150 x 120 mm gives the same pieces (count, size, volume within 0.5 mm3, holes
  per piece) and the same pins as Plan cuts plus Split by hand; the result line says "3 parts, all fit the bed";
- a second click with a piece active splits the same model again (no double pieces);
- another printer (A1, 256 mm) gives the count of a plan for that printer;
- a second model, selected, is split instead of the first one (keuring 24 nov, M1), and the first one is
  visible again (K5);
- the line "Cuts changed" shows only after a cut moved, and is gone after Split (K6);
- an open Suzanne (not watertight) gets a watertight copy first, then all pieces are watertight and fit;
- a model in mm in a meter scene is refused at once with a line that says what to do;
- sj_plek_mm reads and writes the cut position in mm (mm scene and meter scene)."""
import os
import sys
import time
import traceback

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modellen  # noqa: E402
from hulp import SCHAAL, dicht, fouten, gaten, log, maat, past, pen_objecten, stap, stukken  # noqa: E402

A1MINI = (176.0, 176.0, 178.0)  # usable bed of the A1 mini after the 2 mm margin


def beschrijf():
    """Pieces as measured: sorted (size rounded to 0.1 mm, volume rounded, holes), and pins in total."""
    uit = []
    for o in sorted(stukken(), key=lambda o: o["sj_stuk"]):
        m = [round(x, 1) for x in maat(o)]
        uit.append((int(o["sj_stuk"]), m, round(float(o.get("sj_volume_mm3", 0.0))), len(gaten(o))))
    pins = sum(int(p["sj_pennen"]) for p in pen_objecten())
    return uit, pins


def doos_scene(printer="A1MINI"):
    s = modellen.mm_scene()
    s.split_joints.printer = printer
    s.split_joints.speling_mm = 0.2
    ob = modellen.doos(500.0, 150.0, 120.0)
    modellen.actief(ob)
    return s, ob


def alles(uitmap=None):
    inst = bpy.context.scene.split_joints
    stap("klik: operator split_joints.split_to_fit bestaat", "split_to_fit" in dir(bpy.ops.split_joints))

    # by hand: Plan cuts + Split
    s, ob = doos_scene()
    r1 = bpy.ops.split_joints.plan()
    snede = next(o for o in s.objects if "sj_as" in o)
    a = int(snede["sj_as"])
    stap("klik: plek in mm gelijk aan de plek", abs(snede.sj_plek_mm - snede.location[a]) < 1e-4,
         f"{snede.sj_plek_mm:.4f} {snede.location[a]:.4f}")
    r2 = bpy.ops.split_joints.split()
    hand, hand_pins = beschrijf()
    log(f"klik: met de hand {r1} {r2} {hand} pennen {hand_pins}")

    # one click
    s, ob = doos_scene()
    t0 = time.time()
    r = bpy.ops.split_joints.split_to_fit()
    duur = time.time() - t0
    klik, klik_pins = beschrijf()
    log(f"klik: een klik {r} in {duur:.1f} s {klik} pennen {klik_pins}")
    stap("klik: een klik lukt", r == {"FINISHED"}, f"{r}")
    stap("klik: zelfde stukken als Plan plus Split", len(hand) == 3 and [(n, m, g) for n, m, _v, g in klik] ==
         [(n, m, g) for n, m, _v, g in hand] and all(abs(x[2] - y[2]) <= 1 for x, y in zip(klik, hand)),
         f"{len(klik)} tegen {len(hand)}")
    stap("klik: zelfde pennen", klik_pins == hand_pins and klik_pins > 0, f"{klik_pins} tegen {hand_pins}")
    stap("klik: elk stuk past en is dicht", all(past(maat(o), A1MINI) and dicht(o)[0] for o in stukken()))
    from importlib import import_module
    basis = next(m.module for m in bpy.context.preferences.addons if m.module.endswith("click_cuts"))
    klikmod = import_module(basis + ".in_een_klik")
    uit = klikmod.uitslag_tekst(s)
    stap("klik: uitslag in een regel", uit is not None and uit[0] == "3 parts, all fit the bed" and inst.uitslag == "",
         f"{uit}")
    stap("klik: uitslag noemt pennen en speling", uit is not None and uit[1] == f"{klik_pins} pins, 0.20 mm clearance",
         f"{uit}")

    # second click with a piece active: same model again, no double pieces
    modellen.actief(stukken()[0])
    r = bpy.ops.split_joints.split_to_fit()
    stap("klik: tweede klik met een stuk actief", r == {"FINISHED"} and len(stukken()) == 3, f"{r} {len(stukken())}")

    # another printer
    s.split_joints.printer = "A1"
    r = bpy.ops.split_joints.split_to_fit()
    n_plan = int(s["sj_plan"]["stukken"])
    stap("klik: andere printer volgt het plan", r == {"FINISHED"} and len(stukken()) == n_plan and n_plan == 2 and
         all(past(maat(o), (252.0, 252.0, 254.0)) for o in stukken()), f"{len(stukken())} plan {n_plan}")

    # a second model in the same scene, selected: that one is split (keuring 24 nov, M1)
    tweede = modellen.doos(400.0, 120.0, 100.0, naam="Second")
    tweede.location.x = 700.0
    modellen.actief(tweede)
    r = bpy.ops.split_joints.split_to_fit()
    n_plan = int(s["sj_plan"]["stukken"])
    xs = [o.matrix_world.translation.x for o in stukken()]
    stap("klik: tweede model gekozen wordt gesneden", r == {"FINISHED"} and s.split_joints.bron == "Second" and
         len(stukken()) == n_plan == 2 and all(past(maat(o), (252.0, 252.0, 254.0)) for o in stukken()),
         f"{r} bron {s.split_joints.bron} {len(stukken())} plan {n_plan}")
    stap("klik: tweede model, eerste doos blijft bestaan", bpy.data.objects.get("Box") is not None and
         max(maat(o)[0] for o in stukken()) <= 252.0, f"{xs}")
    doos = bpy.data.objects.get("Box")
    stap("klik: tweede model, eerste doos weer zichtbaar (K5)", doos is not None and doos.visible_get() and
         not bpy.data.objects["Second"].visible_get(), f"Box {doos.visible_get() if doos else None}")

    # the hint "Cuts changed" only after a moved cut (K6), gone again after Split
    sn = next(m for n, m in sys.modules.items() if n.endswith("click_cuts.snedes"))
    stap("klik: na de klik geen regel 'Cuts changed' (K6)", not sn.verschoven(s), s.get("sj_snedes_bij_split"))
    snede = sn.snede_objecten(s)[0]
    snede.sj_plek_mm = snede.sj_plek_mm + 5.0
    stap("klik: snede verschoven geeft de regel (K6)", sn.verschoven(s), s.get("sj_snedes_bij_split"))
    modellen.actief(bpy.data.objects["Second"])
    r = bpy.ops.split_joints.split()
    stap("klik: na Split weer geen regel (K6)", r == {"FINISHED"} and not sn.verschoven(s), f"{r}")

    # open model: watertight copy first
    s = modellen.mm_scene()
    s.split_joints.printer = "A1MINI"
    s.split_joints.voxel_mm = 1.5
    ob = modellen.suzanne_open(250.0)
    modellen.actief(ob)
    r = bpy.ops.split_joints.split_to_fit()
    st = stukken()
    stap("klik: open model krijgt eerst een dichte kopie", r == {"FINISHED"} and "watertight" in s.get("sj_klik_stappen", "")
         and s.split_joints.bron.endswith("_watertight"), f"{r} {s.get('sj_klik_stappen')} {s.split_joints.bron}")
    stap("klik: open model, stukken dicht en passend", len(st) > 1 and
         all(dicht(o)[0] and past(maat(o), A1MINI) for o in st), f"{len(st)} stukken")

    # meter scene: refused at once, with a line
    s = modellen.meter_scene()
    ob = modellen.doos(500.0, 150.0, 120.0)
    modellen.actief(ob)
    t0 = time.time()
    try:
        r = bpy.ops.split_joints.split_to_fit()
    except RuntimeError as e:  # an ERROR report raises in bpy.ops
        log(f"klik: melding {e}")
        r = {"CANCELLED"}
    stap("klik: meters geweigerd met uitleg", r == {"CANCELLED"} and "Convert to mm" in s.split_joints.uitslag and
         time.time() - t0 < 5 and not stukken(), f"{r} '{s.split_joints.uitslag}'")
    r = bpy.ops.split_joints.zet_om_mm()
    stap("klik: Convert to mm wist de rode regel", r == {"FINISHED"} and s.split_joints.uitslag == "",
         f"{r} '{s.split_joints.uitslag}'")
    try:
        r = bpy.ops.split_joints.split_to_fit()
    except RuntimeError as e:
        log(f"klik: melding {e}")
        r = {"CANCELLED"}
    stap("klik: na Convert to mm snijdt hij wel", r == {"FINISHED"} and len(stukken()) >= 2, f"{r} {len(stukken())}")

    # position in mm in a meter scene
    s = modellen.meter_scene()
    ob = modellen.doos(0.5, 0.15, 0.12)
    modellen.actief(ob)
    bpy.ops.split_joints.plan()
    snede = next(o for o in s.objects if "sj_as" in o)
    a = int(snede["sj_as"])
    stap("klik: plek in mm in een meter-scene", abs(snede.sj_plek_mm - snede.location[a] * 1000.0) < 1e-3,
         f"{snede.sj_plek_mm:.3f} mm, {snede.location[a]:.6f} m")
    snede.sj_plek_mm = 12.3
    stap("klik: plek in mm zetten", abs(snede.location[a] - 0.0123) < 1e-7, f"{snede.location[a]:.7f}")
    SCHAAL[0] = 1.0
    if uitmap:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uitmap, "klik.blend"))


if __name__ == "__main__":
    try:
        args = sys.argv[sys.argv.index("--") + 1:]
        bpy.ops.extensions.package_install_files(filepath=args[0], repo="user_default", enable_on_install=True)
        alles(args[1] if len(args) > 1 else None)
    except Exception:
        traceback.print_exc()
        fouten.append("onverwachte fout")
    log(f"KLAAR {len(fouten)} FOUT {fouten}")
