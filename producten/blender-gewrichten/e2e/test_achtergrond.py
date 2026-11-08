"""Draait met: blender -b --factory-startup --python e2e/test_achtergrond.py -- <pad naar zip>
Installeert Click Joints als extensie en toetst gewricht, speling, passing, Maak gesloten en STL-export.
Alles wat hij meet staat in het log (regels met [cj-e2e]). Exit 1 bij elke fout."""
import os
import sys
import tempfile
import time
import traceback

import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

zip_pad = sys.argv[sys.argv.index("--") + 1]
fouten = []


def log(tekst):
    print(f"[cj-e2e] {tekst}", flush=True)


def stap(naam, ok):
    log(f"{'OK  ' if ok else 'FOUT'} {naam}")
    if not ok:
        fouten.append(naam)


def meting(ob):
    """(foute randen, volume) van een object: rand met ander aantal vlakken dan 2 telt als fout."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    vol = bm.calc_volume(signed=True)
    bm.free()
    return fout, vol


def delen():
    return [o for o in bpy.context.scene.objects if o.get("cj_deel") and o.visible_get()]


def gesloten_delen(label, lijst):
    stap(f"{label}: precies twee delen (gevonden {len(lijst)})", len(lijst) == 2)
    for d in lijst:
        fout, vol = meting(d)
        log(f"{label}: deel {d.name} foute_randen={fout} volume={vol:.2f}mm3 passing={d.get('cj_passing')} "
            f"wand={d.get('cj_wand_mm')}mm")
        stap(f"{label}: {d.name} gesloten", fout == 0 and vol > 0)


def weg(lijst):
    for o in lijst:
        me = o.data
        bpy.data.objects.remove(o)
        bpy.data.meshes.remove(me)


def plaats(label, ob, punt, as_richting, speling=0.2, kogel=5.0, soort="KOGEL"):
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron = speling, kogel, soort, "CURSOR"
    figuren.zet_cursor(punt, as_richting)
    figuren.maak_actief(ob)
    t0 = time.perf_counter()
    uitslag = bpy.ops.click_joints.plaats()
    duur = time.perf_counter() - t0
    lijst = delen()
    solver = lijst[0].get("cj_solver") if lijst else "-"
    log(f"TIJD {label}: {duur:.2f}s solver={solver} driehoeken_bron={sum(len(p.vertices) - 2 for p in ob.data.polygons)} "
        f"uitslag={uitslag}")
    return lijst


def speling_meten(lijst, ingesteld):
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    c, as_r, r = Vector(a["cj_centrum"]), Vector(a["cj_as"]), a["cj_kogel_r"]
    bm = bmesh.new()
    bm.from_mesh(b.data)
    bvh = BVHTree.FromBMesh(bm)
    bm.free()
    afst = []
    for v in a.data.vertices:
        rel = v.co - c
        if abs(rel.length - r) < 1e-3 and rel.dot(as_r) > -0.4 * r:
            hit = bvh.find_nearest(v.co)
            if hit[0] is not None:
                afst.append(hit[3])
    if not afst:
        stap(f"speling {ingesteld}: kogelpunten gevonden", False)
        return
    gem = sum(afst) / len(afst)
    afw = abs(gem - ingesteld)
    log(f"SPELING ingesteld={ingesteld} gemeten_gem={gem:.4f} afwijking={afw:.4f} "
        f"max={max(afst):.4f} min={min(afst):.4f} punten={len(afst)} addon_meting={a.get('cj_speling_gemeten_mm')}")
    stap(f"speling {ingesteld}: minstens 500 punten", len(afst) >= 500)
    stap(f"speling {ingesteld}: gemiddelde afwijking < 0,02 mm", afw < 0.02)


def toets_stl(lijst):
    bpy.context.scene.click_joints.exportmap = os.path.join(tempfile.gettempdir(), "cj_export") + os.sep
    bpy.ops.click_joints.exporteer()
    for d in lijst:
        pad = d.get("cj_stl", "")
        stap(f"STL {os.path.basename(pad)} bestaat", bool(pad) and os.path.getsize(pad) > 84)
        voor = set(bpy.context.scene.objects)
        bpy.ops.wm.stl_import(filepath=pad, global_scale=1.0, use_scene_unit=False)
        nieuw = [o for o in bpy.context.scene.objects if o not in voor]
        if len(nieuw) != 1:
            stap(f"STL {d.name}: opnieuw geïmporteerd", False)
            continue
        maat_a, maat_b = d.dimensions, nieuw[0].dimensions
        verschil = max(abs(x - y) for x, y in zip(maat_a, maat_b))
        log(f"STL {d.name}: maat {tuple(round(x, 3) for x in maat_a)} mm, terug {tuple(round(x, 3) for x in maat_b)} "
            f"mm, verschil {verschil:.5f} mm, driehoeken {len(nieuw[0].data.polygons)}")
        stap(f"STL {d.name}: zelfde maat binnen 0,01 mm", verschil < 0.01)
        weg(nieuw)


def main():
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    namen = [a.module for a in bpy.context.preferences.addons]
    stap("add-on staat aan", any(n.endswith("click_joints") for n in namen))
    for op in ("plaats", "controleer", "maak_gesloten", "exporteer"):
        stap(f"operator click_joints.{op} bestaat", op in dir(bpy.ops.click_joints))
    stap("paneel geregistreerd", hasattr(bpy.types, "CLICK_JOINTS_PT_paneel"))
    figuren.mm_scene()

    # 1. Groot figuur: speling 0,1 / 0,2 / 0,3 mm, elk precies twee gesloten delen.
    arm = figuren.arm()
    for s in (0.1, 0.2, 0.3):
        lijst = plaats(f"arm speling {s}", arm, (0, 0, 0), (1, 0, 0), speling=s)
        gesloten_delen(f"arm {s}", lijst)
        stap(f"arm {s}: origineel verborgen bewaard", arm.name in bpy.data.objects and not arm.visible_get())
        if len(lijst) == 2:
            speling_meten(lijst, s)
            log(f"PASSING arm {s}: {lijst[0].get('cj_passing')}")
        if s == 0.3 and len(lijst) == 2:
            toets_stl(lijst)
        weg(lijst)

    # 2. Te dunne plek: rood, geen snede, origineel heel.
    lijst = plaats("arm dunne plek", arm, (15, 0, 0), (1, 0, 0))
    rood = [o for o in bpy.context.scene.objects if o.get("cj_passing") == "rood"]
    log(f"DUN: delen={len(lijst)} rode_gewrichten={[o.name for o in rood]} wand={[o.get('cj_wand_mm') for o in rood]}")
    stap("dunne plek: cj_passing == rood", len(rood) == 1)
    stap("dunne plek: niet gesneden", len(lijst) == 0)
    fout, vol = meting(arm)
    stap(f"dunne plek: origineel heel en zichtbaar (foute_randen={fout})", fout == 0 and vol > 0 and arm.visible_get())
    weg(rood)
    arm.hide_set(True)

    # 3. Pop van bollen en cilinders.
    pop = figuren.pop(lijst_solver())
    fout, vol = meting(pop)
    log(f"POP: driehoeken={sum(len(p.vertices) - 2 for p in pop.data.polygons)} foute_randen={fout} volume={vol:.1f}")
    lijst = plaats("pop arm", pop, (11, 0, 3), (1, 0, 0), kogel=3.0)
    gesloten_delen("pop", lijst)
    weg(lijst)
    lijst = plaats("pop pen", pop, (-11, 0, 3), (-1, 0, 0), kogel=2.0, soort="PEN")
    gesloten_delen("pop pen", lijst)
    weg(lijst)
    pop.hide_set(True)

    # 4. Open figuur: eerst een nette melding, na Maak gesloten twee gesloten delen.
    open_ob = figuren.open_arm()
    fout, _ = meting(open_ob)
    log(f"OPEN: foute_randen={fout}")
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    figuren.maak_actief(open_ob)
    melding = None
    try:
        uitslag = bpy.ops.click_joints.plaats()
        log(f"OPEN: uitslag zonder fout {uitslag}")
    except RuntimeError as e:
        melding = str(e).strip()
    log(f"OPEN: melding: {melding}")
    stap("open figuur: nette melding", bool(melding) and "niet gesloten" in melding)
    stap("open figuur: geen delen", len(delen()) == 0)
    bpy.context.scene.click_joints.voxel_mm = 0.4
    bpy.ops.click_joints.maak_gesloten()
    kopie = bpy.context.view_layer.objects.active
    fout, vol = meting(kopie)
    log(f"OPEN: na maak_gesloten {kopie.name} foute_randen={fout} volume={vol:.1f} vlakken={len(kopie.data.polygons)}")
    stap("open figuur: kopie is gesloten", fout == 0 and vol > 0 and kopie is not open_ob)
    lijst = plaats("gesloten kopie", kopie, (0, 0, 0), (1, 0, 0))
    gesloten_delen("na maak_gesloten", lijst)


def lijst_solver():
    from importlib import import_module
    mod = import_module(next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
                        + ".gewricht")
    return mod.solver_naam()


try:
    main()
except Exception:
    traceback.print_exc()
    fouten.append("uitzondering")

log(f"klaar, fouten: {fouten}")
sys.exit(1 if fouten else 0)
