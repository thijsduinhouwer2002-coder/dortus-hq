"""Toets (Pro, issue 42): Check parts geeft per deel een uitslag en een klik selecteert precies de foute plek.

Een kogel op een dunne staaf (straal 4 mm, kogel 5 mm) geeft delen A en B met een krappe wand rond de kom. Eisen:
1. de uitslag heeft precies de twee delen, zonder open randen of losse stukken;
2. een dunne wand rond de kom wordt gevonden: met Min wall net boven de gemeten wand (cj_wand_mm + 0,4 mm) heeft
   deel B vlakken met een dunne wand; met 0,1 mm heeft geen deel er een;
3. een klik op de dunne wand opent deel B in Edit Mode met precies dat aantal vlakken gekozen;
4. een gat in deel A (één vlak weg): open randen gevonden, en de klik kiest precies die randen;
5. een los blokje in deel B: één los stuk, en de klik kiest precies zijn 8 punten;
6. het paneel tekent in stap 3 de knop Check parts en een regel per deel (nep-layout uit toetsen_paneel).
Aangeroepen vanuit test_betaald.py met toets(stap, eigen)."""
import json

import bmesh
import bpy

import figuren
import toetsen_los
import toetsen_paneel


def _gekozen(ob, soort):
    """Aantal gekozen punten, randen of vlakken van ob (leest na terug naar Object Mode)."""
    if bpy.context.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    reeks = {"v": ob.data.vertices, "e": ob.data.edges, "f": ob.data.polygons}[soort]
    return sum(1 for x in reeks if x.select)


def _uitslag(naam):
    lijst = json.loads(bpy.context.scene.get("cj_check", "[]"))
    return next((d for d in lijst if d["naam"] == naam), None), lijst


def toets(stap, eigen):
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    scene = bpy.context.scene
    inst = scene.click_joints
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron = 0.2, 5.0, "KOGEL", "CURSOR"
    inst.kogel_auto, inst.uit_elkaar = False, False
    staaf = figuren.staaf("cstaaf", 4.0)
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    figuren.maak_actief(staaf)
    uitslag = bpy.ops.click_joints.plaats()
    a, b = bpy.data.objects.get("cstaaf_A"), bpy.data.objects.get("cstaaf_B")
    stap("check: kogel op de dunne staaf geplaatst", uitslag == {"FINISHED"} and a is not None and b is not None,
         f"{uitslag} passing {b.get('cj_passing') if b else '-'} wand {b.get('cj_wand_mm') if b else '-'}")
    if a is None or b is None:
        return
    wand = float(b.get("cj_wand_mm", 1.0))
    print(f"[cj-check] passing {b.get('cj_passing')} wand {wand:.3f} mm")

    # 1 en 2: uitslag per deel, dunne wand wel en niet gevonden.
    scene.cj_check_wand_mm = wand + 0.4
    stap("check: Check parts loopt", bpy.ops.click_joints.check_delen() == {"FINISHED"})
    db, lijst = _uitslag("cstaaf_B")
    da, _l = _uitslag("cstaaf_A")
    print("[cj-check] uitslag ruim:", lijst)
    stap("check: precies de twee delen in de uitslag", sorted(d["naam"] for d in lijst) == ["cstaaf_A", "cstaaf_B"],
         str([d["naam"] for d in lijst]))
    stap("check: geen open randen en geen losse stukken na het plaatsen",
         all(d["open"] == 0 and d["los"] == 0 for d in lijst), str(lijst))
    stap("check: dunne wand rond de kom gevonden (Min wall = wand + 0,4 mm)", db is not None and db["dun"] > 0, str(db))
    scene.cj_check_wand_mm = 0.1
    bpy.ops.click_joints.check_delen()
    print("[cj-check] uitslag 0,1 mm:", json.loads(scene["cj_check"]))
    stap("check: met Min wall 0,1 mm geen dunne wand", all(d["dun"] == 0 for d in json.loads(scene["cj_check"])))

    # 3: klik op de dunne wand.
    scene.cj_check_wand_mm = wand + 0.4
    bpy.ops.click_joints.check_delen()
    db, _l = _uitslag("cstaaf_B")
    uit = bpy.ops.click_joints.check_toon(naam="cstaaf_B", soort="dun")
    modus = bpy.context.mode
    actief = bpy.context.view_layer.objects.active
    n = _gekozen(b, "f")
    stap("check: klik op dunne wand opent deel B in Edit Mode met precies die vlakken",
         uit == {"FINISHED"} and modus == "EDIT_MESH" and actief == b and db is not None and n == db["dun"],
         f"{uit} {modus} {actief.name if actief else '-'} gekozen {n} uitslag {db['dun'] if db else '-'}")

    # 4: een gat in deel A.
    bm = bmesh.new()
    bm.from_mesh(a.data)
    bm.faces.ensure_lookup_table()
    bmesh.ops.delete(bm, geom=[bm.faces[0]], context="FACES_ONLY")
    bm.to_mesh(a.data)
    bm.free()
    a.data.update()
    bpy.ops.click_joints.check_delen()
    da, _l = _uitslag("cstaaf_A")
    uit = bpy.ops.click_joints.check_toon(naam="cstaaf_A", soort="open")
    n = _gekozen(a, "e")
    stap("check: gat in deel A geeft open randen en de klik kiest precies die randen",
         da is not None and da["open"] >= 3 and uit == {"FINISHED"} and n == da["open"],
         f"uitslag {da} gekozen {n}")

    # 5: een los blokje in deel B.
    toetsen_los._blok(b, (-14.0, 0.0, 12.0), (3.0, 3.0, 3.0))
    bpy.ops.click_joints.check_delen()
    db, _l = _uitslag("cstaaf_B")
    uit = bpy.ops.click_joints.check_toon(naam="cstaaf_B", soort="los")
    n = _gekozen(b, "v")
    stap("check: los blokje in deel B is één los stuk en de klik kiest zijn 8 punten",
         db is not None and db["los"] == 1 and uit == {"FINISHED"} and n == 8, f"uitslag {db} gekozen {n}")

    # 6: het paneel.
    log = toetsen_paneel.teken(eigen, a)
    stap3, export = toetsen_paneel.plek(log, "label", "3  Fit and export"), toetsen_paneel.plek(log, "op", "Export")
    knop = toetsen_paneel.plek(log, "op", "click_joints.check_delen")
    regel_a = toetsen_paneel.plek(log, "label", "cstaaf_A")
    gat = toetsen_paneel.plek(log, "op", f"{da['open']} open edges")
    stap("check: paneel toont Check parts in stap 3 vóór Export, met een regel en knop per fout",
         0 <= stap3 < knop < regel_a < gat < export, f"({stap3}, {knop}, {regel_a}, {gat}, {export})")
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    if "cj_check" in scene:
        del scene["cj_check"]
