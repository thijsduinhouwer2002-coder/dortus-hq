"""Toetsen voor de correcties 5 tot 8 van de controleur (8 nov 2026), zonder scherm.

5: Exact met en zonder Self Intersection, tijd en uitslag in het log.
8: is_gesloten kijkt naar de geëvalueerde mesh (modifiers) en telt een gespiegeld object als gesloten.
6: as op kijkrichting zonder 3D-venster valt terug op de cursor-as, met een melding en een eigenschap.
7: één ronde in de standaardscene (1 eenheid = 1 m), maten in mm."""
import time

import bpy
from mathutils import Vector

import figuren
from hulp import (addon, delen, gesloten_delen, log, meting, plaats, speling_meten, stap, toets_opening,
                  toets_stl, u, weg)


def exact_zelf(arm):
    """5. Dezelfde snede op de grote arm met de Exact-solver, Self Intersection uit en aan.
    Uit (de standaard) moet twee gesloten delen geven. Aan geeft open delen (gemeten 8 nov); dan moet
    de operator netjes weigeren en het figuur heel laten. Beide tijden staan in het log."""
    gw = addon("gewricht")
    oud = gw.EXACT_ZELF
    stap("Exact: Self Intersection staat standaard uit (afwijking, zie ontwerp.md)", oud is False)
    tijden, uitslagen = {}, {}
    try:
        gw.FORCEER_SOLVER = "EXACT"
        for zelf in (False, True):
            gw.EXACT_ZELF = zelf
            label = f"exact zelf {'aan' if zelf else 'uit'}"
            figuren.zet_cursor((0, 0, 0), (1, 0, 0))
            bpy.context.scene.click_joints.as_bron = "CURSOR"
            t0 = time.perf_counter()
            uitslag, melding = probeer_plaats(arm)
            tijden[zelf] = round(time.perf_counter() - t0, 2)
            lijst = delen()
            uitslagen[zelf] = "gesloten" if len(lijst) == 2 else f"geweigerd: {melding}"
            log(f"TIJD {label}: {tijden[zelf]}s uitslag={uitslag} delen={len(lijst)} melding={melding}")
            if not zelf:
                gesloten_delen(label, lijst)
                if len(lijst) == 2:
                    stap(f"{label}: solver EXACT", lijst[0].get("cj_solver") == "EXACT")
                    speling_meten(lijst, 0.2, f"SPELING {label}")
            elif lijst:
                gesloten_delen(label, lijst)
            else:
                fout, vol = meting(arm)
                stap(f"{label}: geweigerd met nette melding, figuur heel en zichtbaar",
                     bool(melding) and fout == 0 and vol > 0 and arm.visible_get())
            weg(lijst)
    finally:
        gw.FORCEER_SOLVER = None
        gw.EXACT_ZELF = oud
    uit, aan = tijden.get(False), tijden.get(True)
    log(f"EXACT_ZELF driehoeken=261120 tijd_uit={uit}s ({uitslagen.get(False)}) "
        f"tijd_aan={aan}s ({uitslagen.get(True)})")
    arm.hide_set(True)


def probeer_plaats(ob):
    """Roept de operator aan en geeft (uitslag, foutmelding)."""
    figuren.maak_actief(ob)
    try:
        return bpy.ops.click_joints.plaats(), None
    except RuntimeError as e:
        return None, str(e).strip()


def modifiers():
    """8a. Niet toegepaste modifier die een gesloten figuur opent, en een die een open figuur sluit."""
    ob = figuren.arm("arm_masker", 128, 64)
    groep = ob.vertex_groups.new(name="helft")
    groep.add([v.index for v in ob.data.vertices if v.co.z > 0], 1.0, "REPLACE")
    m = ob.modifiers.new("masker", "MASK")
    m.vertex_group = "helft"
    fout_data, _ = meting(ob)
    figuren.maak_actief(ob)
    bpy.ops.click_joints.controleer()
    log(f"MODIFIER opent: foute_randen_zonder_modifier={fout_data} cj_gesloten={ob.get('cj_gesloten')}")
    stap("modifier opent: mesh zonder modifier is gesloten", fout_data == 0)
    stap("modifier opent: Controleer zegt niet gesloten", "cj_gesloten" in ob and not ob["cj_gesloten"])
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    uitslag, melding = probeer_plaats(ob)
    log(f"MODIFIER opent: uitslag={uitslag} melding={melding}")
    stap("modifier opent: nette melding niet gesloten", bool(melding) and "niet gesloten" in melding)
    stap("modifier opent: geen delen", len(delen()) == 0)
    weg([ob])

    ob = figuren.open_arm("open_arm_remesh")
    fout_data, _ = meting(ob)
    m = ob.modifiers.new("dicht", "REMESH")
    m.mode = "VOXEL"
    m.voxel_size = 0.4 * u()
    figuren.maak_actief(ob)
    bpy.ops.click_joints.controleer()
    log(f"MODIFIER sluit: foute_randen_zonder_modifier={fout_data} cj_gesloten={ob.get('cj_gesloten')}")
    stap("modifier sluit: mesh zonder modifier is open", fout_data > 0)
    stap("modifier sluit: Controleer zegt gesloten", bool(ob.get("cj_gesloten")))
    lijst = plaats("modifier sluit", ob, (0, 0, 0), (1, 0, 0))
    gesloten_delen("modifier sluit", lijst)
    weg(lijst + [ob])


def gespiegeld():
    """8b. Arm met schaal -1 op X: telt als gesloten, en een gewricht lukt met twee gesloten delen."""
    ob = figuren.arm("arm_spiegel", 128, 64)
    ob.scale = (-1.0, 1.0, 1.0)
    ob.location = (2.0 * u(), 0.0, 0.0)
    bpy.context.view_layer.update()
    det = ob.matrix_world.to_3x3().determinant()
    _, vol_eigen = meting(ob)
    figuren.maak_actief(ob)
    bpy.ops.click_joints.controleer()
    log(f"SPIEGEL: determinant={det:.2f} volume_eigen={vol_eigen:.1f}mm3 cj_gesloten={ob.get('cj_gesloten')}")
    stap("gespiegeld: Controleer zegt gesloten", bool(ob.get("cj_gesloten")))
    lijst = plaats("gespiegeld", ob, (2.0 * u(), 0, 0), (1, 0, 0))
    gesloten_delen("gespiegeld", lijst)
    if len(lijst) == 2:
        stap("gespiegeld: cj_gespiegeld staat op de delen", bool(lijst[0].get("cj_gespiegeld")))
        stap(f"gespiegeld: passing niet rood ({lijst[0].get('cj_passing')})", lijst[0].get("cj_passing") != "rood")
        som = sum(meting(d)[1] for d in lijst)
        verschil = abs(som - vol_eigen) / vol_eigen
        log(f"SPIEGEL: volume delen samen={som:.1f}mm3 figuur={vol_eigen:.1f}mm3 verschil={verschil:.3%}")
        stap("gespiegeld: volume van de delen samen binnen 5% van het figuur", verschil < 0.05)
        speling_meten(lijst, 0.2, "SPELING gespiegeld")
    weg(lijst + [ob])


def kijk_zonder_venster():
    """6. As op kijkrichting zonder 3D-venster (achtergrond): terugval op de Z-as van de cursor, met melding."""
    ob = figuren.arm("arm_kijk", 128, 64)
    lijst = plaats("kijk zonder venster", ob, (0, 0, 0), (1, 0, 0), as_bron="KIJK")
    gesloten_delen("kijk zonder venster", lijst)
    if len(lijst) == 2:
        d = lijst[0]
        hoek = Vector(d["cj_as"]).angle(Vector((1, 0, 0)))
        log(f"KIJK zonder venster: as_bron={d.get('cj_as_bron')} terugval={d.get('cj_as_terugval')} "
            f"as={tuple(round(x, 4) for x in d['cj_as'])} hoek_met_cursor={hoek:.6f}rad")
        stap("kijk zonder venster: terugval op cursor gemeld", d.get("cj_as_bron") == "CURSOR"
             and bool(d.get("cj_as_terugval")))
        stap("kijk zonder venster: as gelijk aan cursor-as", hoek < 1e-4)
    weg(lijst + [ob])
    bpy.context.scene.click_joints.as_bron = "CURSOR"


def meterscene():
    """7. Standaardscene: 1 eenheid = 1 m. Arm van 0,08 m, kogel 5 mm, speling 0,2 mm."""
    figuren.meter_scene()
    stap(f"meterscene: 1 mm = {u()} eenheden", abs(u() - 0.001) < 1e-12)
    ob = figuren.arm("arm_meter", 256, 128, schaal=0.002)
    bpy.context.view_layer.update()
    log(f"METER: arm {tuple(round(x, 4) for x in ob.dimensions)} m")
    lijst = plaats("meterscene", ob, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    gesloten_delen("meterscene", lijst)
    if len(lijst) != 2:
        return
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    speling_meten(lijst, 0.2, "SPELING meter")
    addon_mm = a.get("cj_speling_gemeten_mm") or 0
    stap(f"meterscene: speling van de add-on {addon_mm} mm (0,2 +- 0,02)", abs(addon_mm - 0.2) < 0.02)
    kogel_d = toets_opening(lijst, "meter")
    stap(f"meterscene: kogeldiameter {kogel_d} mm (5 +- 0,01)", kogel_d is not None and abs(kogel_d - 5.0) < 0.01)
    # De kleinste wand is hier de bodem van deel B naast de klikopening: 1,4r - wortel((r+s)^2 - (0,85r)^2)
    # - 0,0137 = 1,821 mm bij r = 2,5 mm en s = 0,2 mm. In meters gerekend zou dat 0,0018 of 1821 worden.
    wand = a.get("cj_wand_mm")
    verwacht = 3.5 - ((2.7 ** 2 - 2.125 ** 2) ** 0.5) - 0.0137
    log(f"METER: passing={a.get('cj_passing')} wand={wand}mm verwacht={verwacht:.3f}mm kogel_r={a['cj_kogel_r']}m")
    stap("meterscene: passing groen, wand gelijk aan de bodem in mm (+- 0,02)",
         a.get("cj_passing") == "groen" and abs(wand - verwacht) < 0.02)
    # Het snijvlak ligt 0,0137 mm naast de cursor, ook in meters: laagste punt van deel B langs de as.
    as_r = Vector(b["cj_as"])
    schuif = min(v.co.dot(as_r) for v in b.data.vertices) / u()
    log(f"METER: snijvlak {schuif:.5f} mm naast de cursor")
    stap("meterscene: snijvlak 0,0137 mm naast de cursor (+- 0,001)", abs(schuif - 0.0137) < 0.001)
    toets_stl(lijst, "STL meter")
    weg(lijst + [ob])


def alles(arm):
    exact_zelf(arm)
    modifiers()
    gespiegeld()
    kijk_zonder_venster()
    meterscene()  # als laatste, want de scene blijft in meters
