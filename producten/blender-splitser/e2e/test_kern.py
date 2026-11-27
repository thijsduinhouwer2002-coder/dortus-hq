"""Runs with: blender -b --factory-startup --python e2e/test_kern.py -- <zip> <vase.gltf> <skull.gltf> <out dir>
Installs Click Cuts as an extension and splits three free models for a Bambu Lab A1 mini (180 mm).
Checks per model: every piece fits the bed, every piece is watertight, every pin fits its holes with the
set clearance and is not longer than both holes, every piece has its engraved numbers, export to STL and
3MF works (both read back and measured). Plus: a moved cut, a thin tube that gives a clear "too small" message,
and toetsen_extra.py (bare box without voxel, open model, two selected objects, scenes in meters). Exit 1 on any error."""
import os
import sys
import traceback

import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modellen  # noqa: E402
import toetsen_extra  # noqa: E402
import toetsen_klik  # noqa: E402
import toetsen_kleur  # noqa: E402
import toetsen_magneet  # noqa: E402
import toetsen_passing  # noqa: E402
import toetsen_vrij  # noqa: E402
from hulp import (SCHAAL, bestaat, dicht, fouten, gat_maten, gaten, label_punten, labels, lees_3mf,  # noqa: E402
                  lees_stl, log, maat, past, pen_objecten, pennen, raakvlak, stap, stukken)

args = sys.argv[sys.argv.index("--") + 1:]
zip_pad, vaas_pad, schedel_pad, uitmap = args[0], args[1], args[2], args[3]
BED = (176.0, 176.0, 178.0)  # A1 mini 180 x 180 x 180 minus the 2 mm margin
SPELING = 0.2


def splits(naam, ob, printer="A1MINI"):
    inst = bpy.context.scene.split_joints
    inst.printer = printer
    inst.speling_mm = SPELING
    modellen.actief(ob)
    r = bpy.ops.split_joints.plan()
    plan = dict(bpy.context.scene.get("sj_plan", {}))
    log(f"{naam}: plan {r} {plan.get('stukken')} stukken, n={list(plan.get('n', []))}")
    return plan


def toets_stukken(naam, verwacht_pennen=True):
    lijst = stukken()
    stap(f"{naam}: meer dan 1 stuk", len(lijst) > 1, f"{len(lijst)} stukken")
    meldingen = bpy.context.scene.split_joints.meldingen
    if meldingen:
        log(f"{naam}: meldingen: {meldingen!r}")
    for ob in lijst:
        m = maat(ob)
        stap(f"{naam} stuk {ob['sj_stuk']}: past op het bed", past(m, BED), f"{[round(v, 1) for v in m]}")
        ok, slecht, vol = dicht(ob)
        stap(f"{naam} stuk {ob['sj_stuk']}: waterdicht", ok, f"slechte randen {slecht}, volume {vol:.0f} mm3, per stap {list(ob.get('sj_fout_stappen', []))}")
        stap(f"{naam} stuk {ob['sj_stuk']}: status groen", ob.get("sj_status") == "groen",
             f"{ob.get('sj_status')}, wand {ob.get('sj_wand_mm')}")
    # pins: every hole measured in the finished piece, against the pins that come with it
    alle_gaten = [(ob, g) for ob in lijst for g in gaten(ob)]
    paren = len(alle_gaten) // 2
    pen_lijst = [p for po in pen_objecten() for p in pennen(po)]
    stap(f"{naam}: aantal pennen gelijk aan de gatenparen", len(pen_lijst) == paren, f"{len(pen_lijst)} pennen, {paren} paren")
    if verwacht_pennen:
        stap(f"{naam}: er zijn pennen", paren > 0)
    per_snede = {}
    for ob, g in alle_gaten:
        straal, diepte = gat_maten(ob, g)
        if straal is None:
            stap(f"{naam} stuk {ob['sj_stuk']}: gat bij {[round(c, 1) for c in g['p']]} gevonden", False)
            continue
        r_pen = g["pen_d"] / 2.0
        speling = straal - r_pen
        stap(f"{naam} stuk {ob['sj_stuk']}: speling gat {speling:.3f} mm", SPELING - 0.005 <= speling <= SPELING + 0.02,
             f"gat r {straal:.3f}, pen r {r_pen:.3f}, diepte {diepte:.2f}")
        sleutel = (round(g["p"][0], 3), round(g["p"][1], 3), round(g["p"][2], 3))
        per_snede.setdefault(sleutel, []).append((diepte, g["pen_d"]))
    for sleutel, lijst_d in per_snede.items():
        stap(f"{naam}: gat {sleutel} in twee stukken", len(lijst_d) == 2, str(len(lijst_d)))
        if len(lijst_d) == 2:
            som = lijst_d[0][0] + lijst_d[1][0]
            d = lijst_d[0][1]
            langst = max((ln for (r, ln) in pen_lijst if abs(r - d / 2) < 0.01), default=None)
            stap(f"{naam}: pen {d:g} mm past helemaal in de twee gaten", langst is not None and langst <= som,
                 f"pen {langst}, gaten samen {som:.2f}")
    for (r, ln) in pen_lijst:
        if not any(abs(r - g["pen_d"] / 2) < 0.01 for _o, g in alle_gaten):
            stap(f"{naam}: pen r {r:.3f} hoort bij een gat", False)
    # numbers: one on every cut face the piece shares with a neighbor (keuring M3), each really engraved
    for ob in lijst:
        lbs = labels(ob)
        buren = verwachte_buren(ob, lijst)
        kreeg = {int(lb["tekst"].split("-")[1]) for lb in lbs}
        stap(f"{naam} stuk {ob['sj_stuk']}: een nummer op elk snijvlak met een buur", kreeg == buren and len(buren) > 0,
             f"buren {sorted(buren)}, nummers {[lb['tekst'] for lb in lbs]}")
        for lb in lbs:
            stap(f"{naam} stuk {ob['sj_stuk']}: nummer {lb['tekst']} begint met het eigen nummer",
                 lb["tekst"].split("-")[0] == str(ob["sj_stuk"]))
            n = label_punten(ob, lb, ob["sj_label_diepte_mm"])
            stap(f"{naam} stuk {ob['sj_stuk']}: nummer {lb['tekst']} verdiept in het vlak", n >= 8, f"{n} punten op de bodem")
    return lijst


def verwachte_buren(ob, lijst):
    """Numbers of the pieces next to ob (cell one step away along one axis) that really touch it: both
    have faces in the shared plane. Measured on the meshes, not from the add-on's labels."""
    uit = set()
    cel = list(ob["sj_cel"])
    for o in lijst:
        c2 = list(o["sj_cel"])
        verschil = [c2[i] - cel[i] for i in range(3)]
        if sorted(abs(d) for d in verschil) != [0, 0, 1]:
            continue
        a = next(i for i in range(3) if verschil[i])
        laag = ob if verschil[a] > 0 else o
        c = max(v.co[a] for v in laag.data.vertices) * SCHAAL[0]
        if raakvlak(ob, a, c) and raakvlak(o, a, c):
            uit.add(int(o["sj_stuk"]))
    return uit


def stl_driehoeken(pad):
    """(n, 3, 3) triangles in mm from a binary STL."""
    import numpy as np
    with open(pad, "rb") as f:
        data = f.read()
    n = int.from_bytes(data[80:84], "little")
    rec = np.frombuffer(data, dtype=np.dtype([("n", "<f4", 3), ("v", "<f4", (3, 3)), ("a", "<u2")]), count=n, offset=84)
    return rec["v"].astype(np.float64)


def stl_volume(v):
    import numpy as np
    return float(np.einsum("ij,ij->i", v[:, 0], np.cross(v[:, 1], v[:, 2])).sum() / 6)


def snij_mesh(ob):
    """Pin holes and numbers of a piece as (point mm, axis): they lie in its cut faces."""
    import json
    uit = []
    for g in json.loads(ob.get("sj_gaten") or "[]") + json.loads(ob.get("sj_labels") or "[]"):
        a = g["n"] if "n" in g else [1.0 if i == g.get("as") else 0.0 for i in range(3)]
        uit.append((Vector(g["p"]), Vector(a).normalized()))
    return uit


def grootste_vlak_mesh(ob, alleen_snij=False):
    """Largest flat plane of a piece, measured on its own mesh in mm (normal and offset rounded), in mm2.
    alleen_snij: only planes that hold a pin hole or number (a cut face)."""
    snij = snij_mesh(ob) if alleen_snij else None
    som = {}
    # the mesh's own coordinates: holes and numbers are stored like that, without the exploded-view shift
    # (delta_location, which matrix_basis includes)
    for p in ob.data.polygons:
        nw = p.normal.normalized()
        c = p.center * SCHAAL[0]
        k = (round(nw.x, 3), round(nw.y, 3), round(nw.z, 3), round(nw.dot(c), 1))
        if snij is not None and not any(abs(nw.dot(a)) > 0.999 and abs(nw.dot(q) - nw.dot(c)) < 0.15 for q, a in snij):
            continue
        som[k] = som.get(k, 0.0) + p.area * SCHAAL[0] ** 2
    return max(som.values()) if som else 0.0


def toets_plat(naam, lijst):
    """Lay parts flat (1.0.0): measured on the STL files, not on what the add-on says."""
    import numpy as np
    import importlib
    bed_mm = importlib.import_module("bl_ext.user_default.click_cuts.eigenschappen").bed
    inst = bpy.context.scene.split_joints
    inst.formaat = "STL"
    voor = {o.name: [tuple(r) for r in o.matrix_world] for o in lijst}
    inst.plat = False
    inst.exportmap = os.path.join(uitmap, naam, "plat_uit") + os.sep
    bpy.ops.split_joints.exporteer()
    pen_uit = {os.path.basename(p): open(p, "rb").read() for p in bpy.context.scene["sj_laatste_export"] if "pins_" in p}
    vol_uit = {o.name: abs(stl_volume(stl_driehoeken(o["sj_bestand"]))) for o in lijst}  # same piece, not turned
    maat_uit = {o.name: np.ptp(stl_driehoeken(o["sj_bestand"]).reshape(-1, 3), axis=0) for o in lijst}
    inst.plat = True
    inst.exportmap = os.path.join(uitmap, naam, "plat_aan") + os.sep
    r = bpy.ops.split_joints.exporteer()
    stap(f"{naam}: plat export", r == {"FINISHED"})
    bed = bed_mm(bpy.context.scene)
    op_snijvlak = 0
    for ob in lijst:
        v = stl_driehoeken(ob["sj_bestand"])
        z = v[:, :, 2]
        e1, e2 = v[:, 1] - v[:, 0], v[:, 2] - v[:, 0]
        kruis = np.cross(e1, e2)
        opp = np.linalg.norm(kruis, axis=1) / 2
        vol = stl_volume(v)
        nz = kruis[:, 2] / np.maximum(np.linalg.norm(kruis, axis=1), 1e-12)
        onder = float(opp[(nz < -0.999) & (z.max(axis=1) < 0.01)].sum())
        mx = np.ptp(v[:, :, 0]); my = np.ptp(v[:, :, 1]); mz = np.ptp(z)
        past_bed = mz <= bed[2] + 0.01 and ((mx <= bed[0] + 0.01 and my <= bed[1] + 0.01) or (mx <= bed[1] + 0.01 and my <= bed[0] + 0.01))
        rang = int(ob.get("sj_plat_rang", -9))
        snijvlak = bool(ob.get("sj_plat_snijvlak"))
        groot = grootste_vlak_mesh(ob, alleen_snij=snijvlak)
        stap(f"{naam}: plat stuk {int(ob['sj_stuk'])} laagste punt op z = 0, past op het bed",
             abs(float(z.min())) < 0.01 and past_bed, f"z {z.min():.3f}, {mx:.1f} x {my:.1f} x {mz:.1f}, rang {rang}")
        stap(f"{naam}: plat stuk {int(ob['sj_stuk'])} zelfde volume als het stuk",
             abs(abs(vol) - vol_uit[ob.name]) < max(1.0, 1e-4 * abs(vol)), f"{abs(vol):.0f} / {vol_uit[ob.name]:.0f} mm3")
        if rang >= 0:  # M1 Daan: only a cut face may go down
            stap(f"{naam}: plat stuk {int(ob['sj_stuk'])} ligt op een snijvlak", snijvlak and onder > 0,
                 f"rang {rang}, onder {onder:.0f} mm2")
            op_snijvlak += snijvlak
        if rang == 0:
            stap(f"{naam}: plat stuk {int(ob['sj_stuk'])} grootste snijvlak ligt onder",
                 onder >= 0.99 * groot > 0, f"onder {onder:.0f} mm2, grootste {groot:.0f} mm2")
        elif rang == -1:
            mu = maat_uit[ob.name]
            stap(f"{naam}: plat stuk {int(ob['sj_stuk'])} geen snijvlak past: eigen stand, niet gedraaid",
                 np.allclose([mx, my, mz], mu, atol=0.01), f"{mx:.1f} x {my:.1f} x {mz:.1f} / {mu[0]:.1f} x {mu[1]:.1f} x {mu[2]:.1f}")
        elif rang < -1:
            stap(f"{naam}: plat stuk {int(ob['sj_stuk'])} kreeg geen stand", False, f"rang {rang}")
    stap(f"{naam}: plat minstens de helft van de stukken ligt op een snijvlak", 2 * op_snijvlak >= len(lijst),
         f"{op_snijvlak} van {len(lijst)}")
    pen_aan = {os.path.basename(p): open(p, "rb").read() for p in bpy.context.scene["sj_laatste_export"] if "pins_" in p}
    stap(f"{naam}: plat pennenplaat ongewijzigd", pen_aan == pen_uit and len(pen_aan) > 0, f"{len(pen_aan)} platen")
    na = {o.name: [tuple(r) for r in o.matrix_world] for o in lijst}
    stap(f"{naam}: plat stukken staan na export nog op hun plek in de scene", na == voor)
    inst.plat = False  # the other export checks compare sizes with the pieces as they stand


def toets_export(naam, lijst):
    inst = bpy.context.scene.split_joints
    toets_plat(naam, lijst)
    for formaat in ("STL", "3MF"):
        inst.formaat = formaat
        inst.exportmap = os.path.join(uitmap, naam, formaat.lower()) + os.sep
        r = bpy.ops.split_joints.exporteer()
        bestanden = list(bpy.context.scene.get("sj_laatste_export", []))
        stap(f"{naam}: export {formaat}", r == {"FINISHED"} and len(bestanden) == len(lijst) + len(pen_objecten()),
             f"{len(bestanden)} bestanden")
        for ob in lijst + pen_objecten():
            pad = ob.get("sj_bestand", "")
            if not bestaat(pad):
                stap(f"{naam}: bestand {pad}", False)
                continue
            m = maat(ob)
            if formaat == "STL":
                n, mm, heel = lees_stl(pad)
                stap(f"{naam}: STL {os.path.basename(pad)} maat gelijk", heel and all(abs(a - b) < 0.01 for a, b in zip(m, mm)),
                     f"{n} driehoeken, {[round(v, 2) for v in mm]}")
            else:
                d = lees_3mf(pad)
                stap(f"{naam}: 3MF {os.path.basename(pad)} in mm, maat gelijk",
                     d["delen"] and d["mm"] and d["driehoeken"] > 0 and all(abs(a - b) < 0.01 for a, b in zip(m, d["maat"])),
                     f"{d['driehoeken']} driehoeken, {[round(v, 2) for v in d['maat']]}")


def model(naam, ob):
    plan = splits(naam, ob)
    r = bpy.ops.split_joints.split()
    log(f"{naam}: split {r} in {bpy.context.scene.get('sj_duur_s')} s, solver "
        f"{stukken()[0].get('sj_solver') if stukken() else '-'}")
    lijst = toets_stukken(naam)
    stap(f"{naam}: aantal stukken gelijk aan het plan", len(lijst) == plan.get("stukken"), f"{len(lijst)} / {plan.get('stukken')}")
    toets_export(naam, lijst)
    toetsen_kleur.toets(naam)
    return lijst


def main():
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    for op in ("plan", "split", "exporteer", "maak_gesloten", "snede_erbij", "snede_weg", "vrije_snede_erbij",
               "vrije_snede", "vrije_snede_tekenen", "vrije_snede_om", "split_to_fit"):
        stap(f"operator split_joints.{op} bestaat", op in dir(bpy.ops.split_joints))
    for naam, maak in (("suzanne", modellen.suzanne), ("vaas", lambda: modellen.vaas(vaas_pad)),
                       ("schedel", lambda: modellen.schedel(schedel_pad))):
        try:
            modellen.mm_scene()
            ob = maak()
            model(naam, ob)
            if naam == "suzanne":
                verschuif(ob)
            bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uitmap, f"{naam}.blend"))
        except Exception:
            traceback.print_exc()
            stap(f"{naam}: geen fout", False)
    for naam, f in (("buis", te_klein), ("extra", lambda: toetsen_extra.alles(model, uitmap)),
                    ("passing", lambda: toetsen_passing.alles(uitmap)), ("vrij", lambda: toetsen_vrij.alles(uitmap)),
                    ("tekenen", lambda: toetsen_vrij.tekenen(uitmap)),
                    ("klik", lambda: toetsen_klik.alles(uitmap)), ("magneet", lambda: toetsen_magneet.alles(uitmap))):
        try:
            f()
        except Exception:
            traceback.print_exc()
            stap(f"{naam}: geen fout", False)


def verschuif(ob):
    """A cut moved by hand (5 mm along its axis): the pieces follow the plane and still fit."""
    col = bpy.data.collections.get("Click Cuts cut planes")
    cuts = sorted((o for o in col.objects if "sj_as" in o), key=lambda o: o.name) if col else []
    if not stap("verschuif: er is een snede", bool(cuts)):
        return
    c = cuts[0]
    a = int(c["sj_as"])
    oud = c.location[a]
    c.location[a] = oud + 5.0
    r = bpy.ops.split_joints.split()
    lijst = stukken()
    randen = [max(v.co[a] for v in o.data.vertices) for o in lijst] + [min(v.co[a] for v in o.data.vertices) for o in lijst]
    stap("verschuif: een stuk eindigt op de nieuwe plek", any(abs(x - (oud + 5.0)) < 0.05 for x in randen),
         f"{r}, snede {oud:.2f} -> {oud + 5.0:.2f}")
    stap("verschuif: geen stuk eindigt op de oude plek", not any(abs(x - oud) < 0.05 for x in randen))
    for o in lijst:
        stap(f"verschuif stuk {o['sj_stuk']}: past en waterdicht", past(maat(o), BED) and dicht(o)[0])


def te_klein():
    modellen.mm_scene()
    ob = modellen.buis()
    splits("buis", ob)
    bpy.ops.split_joints.split()
    m = bpy.context.scene.split_joints.meldingen
    stap("buis: melding te klein voor een pen", "too small for a pin" in m, repr(m[:200]))
    stap("buis: geen pennen", not pen_objecten())
    for ob in stukken():
        stap(f"buis stuk {ob['sj_stuk']}: past en waterdicht", past(maat(ob), BED) and dicht(ob)[0])


try:
    main()
except Exception:
    traceback.print_exc()
    fouten.append("onverwachte fout")
log(f"KLAAR {len(fouten)} FOUT {fouten}")
sys.exit(1 if fouten else 0)
