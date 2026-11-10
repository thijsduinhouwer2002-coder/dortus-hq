"""Eis 6 van het scharnier (ontwerp betaald v1.1): Exploded view, export op de echte plek en te dichtbij.
Aangeroepen vanuit toetsen_scharnier.py; zelfde opzet als de kogel in hulp.toets_uit_elkaar en toetsen_uit_elkaar.py.

Staaf van 5 mm straal en 80 mm lang langs X, stand 115, speling 0,2, cursor als as-bron (H = wereld-Y, L = X).
(a) Exploded view aan: deel B staat in de weergave 1,5 keer de wangdiameter (3 Rn) langs L verschoven, loodrecht
    op L niets; de tong is dan helemaal uit de vork (laagste punt van B langs L boven het hoogste punt van A).
    Uit: geen verschuiving. Location en mesh veranderen niet.
(b) Export STL en 3MF met Exploded view aan: het bestand gelijk aan de export met Exploded view uit, en de grenzen
    van deel B in het bestand gelijk aan de echte plek (binnen 0,001 mm).
(c) Tweede scharnier op deel B te dichtbij: geweigerd met "Too close to another joint (keep N mm apart).", geen
    nieuwe delen, op 2 reik - 0,5 mm. N zelf gerekend: reik = max(t_vlak sin a, Rn, lip) + s, N = 2 keer het grootste
    bereik naar boven afgerond (vlak bij het oude meet het nieuwe korter, dus telt het oude). Precies op N lukt het:
    twee nieuwe gesloten delen en een gemeten bereik van 113 tot 115 graden.
Alle maten in het log in mm."""
import math
import os
import struct
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

import bpy
from mathutils import Vector

import figuren
from toetsen_teksten import vang

NS = "{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}"


def _grenzen(punten):
    return ([min(p[i] for p in punten) for i in range(3)], [max(p[i] for p in punten) for i in range(3)])


def _echt(ob, u):
    """Hoekpunten van het deel in mm via matrix_world, dus zoals in beeld: met Exploded view aan verschoven, uit
    op de echte plek."""
    return [tuple(c / u for c in ob.matrix_world @ v.co) for v in ob.data.vertices]


def _stl(pad):
    with open(pad, "rb") as f:
        data = f.read()
    return [struct.unpack_from("<12f", data, 84 + 50 * i)[3:] for i in range((len(data) - 84) // 50)]


def _drie_mf(pad):
    with zipfile.ZipFile(pad) as z:
        boom = ET.fromstring(z.read("3D/3dmodel.model"))
    return [(float(v.get("x")), float(v.get("y")), float(v.get("z"))) for v in boom.iter(NS + "vertex")]


def _exporteer(inst, formaat, b):
    inst.exportmap = os.path.join(tempfile.gettempdir(), "cj_export_scharnier") + os.sep
    inst.formaat = formaat
    uitslag = bpy.ops.click_joints.exporteer()
    inst.formaat = "STL"
    pad = b.get("cj_3mf" if formaat == "3MF" else "cj_stl", "")
    if uitslag != {"FINISHED"} or not pad:
        return None
    if formaat == "3MF":
        return _drie_mf(pad)
    return [p[i:i + 3] for p in _stl(pad) for i in (0, 3, 6)]


def _reik(ob, u):
    """Eigen rekensom van het bereik langs L in mm uit de opgeslagen maten (zie de docstring)."""
    a = math.radians(float(ob["cj_wig_graden"]))
    s = float(ob["cj_speling_mm"]) * u
    return (max(float(ob["cj_t_vlak"]) * math.sin(a), float(ob["cj_naad_r"]), float(ob["cj_lip"])) + s) / u


def _plaats(punt, bron, cursor):
    figuren.maak_actief(bron)
    cursor(punt, Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    try:
        return bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:  # een ERROR-melding wordt in een script een uitzondering
        return {"FOUT: " + str(fout)}


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar = 0.2, "CURSOR", True
    u = eig.eenheid_per_mm(bpy.context.scene)
    staaf = figuren.staaf("lang", 5.0, lengte=80.0)
    uitslag = _plaats((0, 0, 0), staaf, cursor)
    a, b = bpy.data.objects.get("lang_A"), bpy.data.objects.get("lang_B")
    stap("eis 6: scharnier geplaatst op de lange staaf", uitslag == {"FINISHED"} and a and b, str(uitslag))
    if a is None or b is None:
        return
    lid = Vector(b["cj_as"]).normalized()
    loc = Vector(b.location)
    # (a) Exploded view aan en uit.
    for aan in (True, False):
        inst.uit_elkaar = aan
        bpy.context.view_layer.update()
        d = (b.matrix_world.translation - b.location) / u
        langs, dwars = d.dot(lid), (d - lid * d.dot(lid)).length
        verwacht = 1.5 * 2 * float(b["cj_naad_r"]) / u if aan else 0.0
        laag_b = min(Vector(p).dot(lid) for p in _echt(b, u))
        hoog_a = max(Vector(p).dot(lid) for p in _echt(a, u))
        print(f"[cj-betaald] METING eis 6 Exploded view aan={aan}: deel B {langs:.4f} mm langs L (verwacht "
              f"{verwacht:.4f}, Rn {float(b['cj_naad_r']) / u:.4f}), dwars {dwars:.5f} mm, laagste punt B langs L "
              f"{laag_b:.3f} mm, hoogste punt A {hoog_a:.3f} mm, location {tuple(round(x, 4) for x in b.location)}")
        stap(f"eis 6: Exploded view aan={aan}: deel B {verwacht:.3f} mm langs L verschoven, dwars niets",
             abs(langs - verwacht) < 1e-3 and dwars < 1e-4, f"{langs:.4f} mm, dwars {dwars:.5f}")
        if aan:
            stap("eis 6: Exploded view: tong helemaal uit de vork (B boven A langs L)", laag_b > hoog_a,
                 f"spleet {laag_b - hoog_a:.3f} mm")
    stap("eis 6: location van deel B verandert niet", (Vector(b.location) - loc).length < 1e-9)
    echt_b = _grenzen(_echt(b, u))  # Exploded view staat nu uit
    # (b) Export STL en 3MF: met Exploded view aan gelijk aan uit, en op de echte plek.
    for formaat in ("STL", "3MF"):
        uit = {}
        for aan in (True, False):
            inst.uit_elkaar = aan
            bpy.context.view_layer.update()
            uit[aan] = _exporteer(inst, formaat, b)
        if not uit[True] or not uit[False]:
            stap(f"eis 6: export {formaat} van deel B gelukt", False)
            continue
        gelijk = len(uit[True]) == len(uit[False]) and max(
            abs(x - y) for p, q in zip(uit[True], uit[False]) for x, y in zip(p, q)) < 1e-4
        gb = _grenzen(uit[True])
        verschil = max(abs(x - y) for x, y in zip(gb[0] + gb[1], echt_b[0] + echt_b[1]))
        print(f"[cj-betaald] METING eis 6 export {formaat} deel B met Exploded view aan: {len(uit[True])} punten, "
              f"grenzen {[round(x, 3) for x in gb[0]]}..{[round(x, 3) for x in gb[1]]} mm, echte plek "
              f"{[round(x, 3) for x in echt_b[0]]}..{[round(x, 3) for x in echt_b[1]]} mm, verschil {verschil:.6f} mm, "
              f"gelijk aan export met Exploded view uit {gelijk}")
        stap(f"eis 6: {formaat} deel B gelijk met en zonder Exploded view", gelijk)
        stap(f"eis 6: {formaat} deel B op de echte plek (binnen 0,001 mm)", verschil < 1e-3, f"{verschil:.6f} mm")
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    stap("eis 6: na export staat deel B weer verschoven",
         abs((b.matrix_world.translation - b.location).length / u - 3 * float(b["cj_naad_r"]) / u) < 1e-3)
    # (c) Tweede scharnier op deel B: net te dicht (2 reik - 0,5 mm), daarna precies op N.
    gesloten = sys.modules[eigen + ".gesloten"]
    reik = _reik(b, u)
    nodig = math.ceil(2 * reik - 1e-9)
    x = 2 * reik - 0.5
    voor = {o.name for o in bpy.data.objects}
    tekst = []
    with vang(tekst):
        uitslag = _plaats((x, 0, 0), b, cursor)
    nieuw = {o.name for o in bpy.data.objects} - voor
    gemeld = b.get("cj_te_dicht_mm")
    verwacht = f"Too close to another joint (keep {nodig} mm apart)."
    print(f"[cj-betaald] METING eis 6 te dicht: reik {reik:.3f} mm (t_vlak {float(b['cj_t_vlak']) / u:.3f}, "
          f"wig {b['cj_wig_graden']}, Rn {float(b['cj_naad_r']) / u:.3f}, lip {float(b['cj_lip']) / u:.3f}), "
          f"2 reik {2 * reik:.3f}, N eigen rekensom {nodig}, tweede op x={x:.3f} mm: uitslag={uitslag}, "
          f"cj_te_dicht_mm={gemeld}, nieuwe objecten {sorted(nieuw)}, melding gevangen {verwacht in tekst[0]}")
    stap(f"eis 6: tweede scharnier op {x:.3f} mm (2 reik - 0,5) geweigerd met keep {nodig} mm, geen nieuwe delen",
         uitslag == {"CANCELLED"} and gemeld == nodig and not nieuw, f"kreeg {gemeld}, nieuw {sorted(nieuw)}")
    stap(f"eis 6: melding precies '{verwacht}'", f"Warning: {verwacht}" in tekst[0])
    x = float(nodig)
    uitslag = _plaats((x, 0, 0), b, cursor)
    nieuw = [o for o in bpy.data.objects if o.name not in voor and o.get("cj_deel")]
    dicht = [gesloten.is_gesloten(o) for o in nieuw]
    bereik = [float(o.get("cj_bereik_graden", -1)) for o in nieuw]
    print(f"[cj-betaald] METING eis 6 tweede scharnier op x={x:.1f} mm (precies N): uitslag={uitslag}, nieuwe delen "
          f"{sorted(o.name for o in nieuw)}, foute randen {[d[1] for d in dicht]}, cj_bereik_graden {bereik}")
    stap(f"eis 6: tweede scharnier op N = {x:.1f} mm geplaatst (twee nieuwe delen)",
         uitslag == {"FINISHED"} and len(nieuw) == 2, str(uitslag))
    stap("eis 6: tweede scharnier op N: beide delen gesloten", len(dicht) == 2 and all(d[0] for d in dicht),
         str([d[1] for d in dicht]))
    stap("eis 6: tweede scharnier op N: gemeten bereik binnen 2 graden onder de stand 115",
         len(bereik) == 2 and all(113.0 <= g <= 115.05 for g in bereik), str(bereik))
