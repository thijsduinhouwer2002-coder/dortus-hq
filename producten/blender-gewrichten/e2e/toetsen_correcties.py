"""Toetsen voor de correcties 5 tot 8 van de controleur (8 nov 2026), zonder scherm.

5: Exact met en zonder Self Intersection, tijd en uitslag in het log.
8: is_gesloten kijkt naar de geëvalueerde mesh (modifiers) en telt een gespiegeld object als gesloten.
6: as op kijkrichting zonder 3D-venster valt terug op de cursor-as, met een melding en een eigenschap.
7: één ronde in de standaardscene (1 eenheid = 1 m), maten in mm."""
import time

import bpy
from mathutils import Vector

import figuren
import toetsen_3mf
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
    stap("modifier opent: nette melding niet gesloten", bool(melding) and "not watertight" in melding)
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
        # Ronde j (Daan akkoord): vorm v0.3 neemt bewust ruimte weg (kom min kogel, trechter min nek, de spleet
        # van s langs de bolnaad). Die ruimte meten we los uit de vorm (steekproef in het originele figuur)
        # en tellen hem mee; de grens van 5% blijft voor de rest.
        a = next(d for d in lijst if d["cj_deel"] == "A")
        weg_mm3 = bewust_weg(ob, a)
        verschil = abs(som + weg_mm3 - vol_eigen) / vol_eigen
        log(f"SPIEGEL: volume delen samen={som:.1f}mm3 bewust weg={weg_mm3:.1f}mm3 figuur={vol_eigen:.1f}mm3 "
            f"verschil={verschil:.3%} (zonder de weggenomen ruimte {abs(som - vol_eigen) / vol_eigen:.3%})")
        stap("gespiegeld: volume van de delen samen plus de bewust weggenomen ruimte binnen 5% van het figuur",
             weg_mm3 > 0 and verschil < 0.05)
        speling_meten(lijst, 0.2, "SPELING gespiegeld")
    weg(lijst + [ob])


def bewust_weg(ob, a, n=200000):
    """Volume in mm3 van de ruimte die vorm v0.3 bewust weghaalt binnen het figuur, als steekproef:
    binnen het figuur, niet in het gebied van deel A (onder het vlak door het kogelmidden en buiten de bol
    naad_r + s/2), niet in kogel of nek, en ofwel buiten het gebied van deel B (de spleet langs de bolnaad)
    ofwel in kom (r + s) of trechter. Alle vormen zijn rond om de as, dus alleen afstand tot de as telt."""
    import math
    import random
    import bmesh
    from mathutils.bvhtree import BVHTree
    r, s = a["cj_kogel_r"], a["cj_speling_mm"] * u()
    naad, open_r, lip, nek = a["cj_naad_r"], a["cj_open_r"], a["cj_lip_d"], a["cj_nek_r"]
    schuif = 0.0137 * u()
    as_r = Vector(a["cj_as"]).normalized()
    c = Vector(a["cj_centrum"])
    cursor = Vector(a["cj_snijpunt"]) - as_r * schuif
    mz = (c - cursor).dot(as_r)
    vlak = mz + schuif
    tan = math.tan(math.radians(a["cj_grens_graden"] + 3.0))
    z_lip = mz - lip
    z_top, z_bodem = z_lip + 0.25 * r, mz - naad - s - 0.5 * r
    onder = min(-0.4 * r, mz - naad - 0.4 * r)
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.transform(ob.matrix_world)
    if ob.matrix_world.determinant() < 0:
        bmesh.ops.reverse_faces(bm, faces=bm.faces[:])
    bvh = BVHTree.FromBMesh(bm)
    bm.free()
    h = naad + s
    rng = random.Random(7)
    # twee loodrechte richtingen op de as
    e1 = as_r.orthogonal().normalized()
    e2 = as_r.cross(e1).normalized()
    raak = 0
    for _ in range(n):
        x, y, z = (rng.uniform(-h, h) for _ in range(3))
        zc = mz + z  # hoogte in het frame (0 = cursor)
        d2 = x * x + y * y + z * z
        rho = math.sqrt(x * x + y * y)
        if d2 < r * r or (rho < nek and onder <= zc <= mz):
            continue  # kogel of nek (deel A)
        if zc < vlak and d2 > (naad + s / 2) ** 2:
            continue  # gebied van deel A
        in_b = zc >= vlak or d2 < (naad - s / 2) ** 2
        kom = d2 < (r + s) ** 2
        trechter = z_bodem <= zc <= z_top and rho <= open_r + (z_lip - zc) * tan
        if in_b and not kom and not trechter:
            continue  # gewoon deel B
        p = c + as_r * z + e1 * x + e2 * y
        loc, nor, _, _ = bvh.find_nearest(p)
        if loc is not None and (p - loc).dot(nor) < 0:
            raak += 1
    weg = raak / n * (2 * h) ** 3 / u() ** 3
    log(f"SPIEGEL: steekproef bewust weg {raak}/{n} punten, kubus {2 * h / u():.2f} mm, {weg:.1f} mm3")
    return weg


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
    # Vorm v0.3 (ronde j): de bodem van deel B bestaat niet meer. De kleinste wand is nu de kleinste van
    # (1) de schil van deel B tussen kom en bolnaad: naad_r - s/2 - (r + s), en (2) de trechterwand: van de
    # klikrand langs de trechter tot de bolnaad, loodrecht op de trechter tot de huid van het originele figuur.
    # Hier zelf nagerekend op het origineel; in meters gerekend zou het 1000 keer te klein of te groot zijn.
    wand = a.get("cj_wand_mm")
    verwacht = verwachte_wand(ob, a)
    log(f"METER: passing={a.get('cj_passing')} wand={wand}mm verwacht={verwacht:.3f}mm kogel_r={a['cj_kogel_r']}m")
    stap("meterscene: passing groen, wand gelijk aan de kleinste van schil en trechterwand in mm (+- 0,02)",
         a.get("cj_passing") == "groen" and abs(wand - verwacht) < 0.02)
    # Vorm v0.3: de naad tussen A en B is een bol om het kogelmidden (deel B tot naad_r - s/2), en buiten die bol
    # loopt de vlakke snede door het kogelmidden, 0,0137 mm verder langs de as. Bij deze arm is de bol breder dan
    # de arm (naad_r = grootste straal + marge), dus er is buiten de bol geen vlak stuk: daar eisen we dat geen
    # punt van B buiten de bol onder dat vlak ligt. De bol zelf toetsen we met de oude precisie (0,001 mm): het
    # verste punt van B onder het vlak ligt op naad_r - s/2 van het kogelmidden.
    as_r, c = Vector(b["cj_as"]), Vector(b["cj_centrum"])
    naad, s_e = b.get("cj_naad_r", -1.0), b["cj_speling_mm"] * u()
    vlak = c.dot(as_r) + 0.0137 * u()
    rb = naad - s_e / 2
    onder = [(v.co - c).length for v in b.data.vertices if v.co.dot(as_r) < vlak - 0.001 * u()]
    verst = max(onder) / u() if onder else -1.0
    buiten_onder = [v for v in b.data.vertices if (v.co - c).length > rb + 0.001 * u() and v.co.dot(as_r) < vlak - 0.001 * u()]
    log(f"METER: bolnaad deel B verst {verst:.5f} mm van het kogelmidden, verwacht {rb / u():.5f} mm; "
        f"punten buiten de bol onder het vlak door het kogelmidden: {len(buiten_onder)}")
    stap("meterscene: naad van deel B is de bol naad_r - s/2 om het kogelmidden (+- 0,001 mm)",
         naad > 0 and abs(verst - rb / u()) < 0.001)
    stap("meterscene: buiten de bol ligt deel B boven het vlak door het kogelmidden + 0,0137 mm",
         naad > 0 and not buiten_onder)
    hoek, grens = a.get("cj_hoek"), a.get("cj_grens_graden", -1.0)
    log(f"METER: hoekstand {hoek} graden, berekende grens {grens} graden, nek_r {a['cj_nek_r'] / u():.3f} mm")
    stap("meterscene: hoekstand 30, 25 of 20 en berekende grens minstens die stand",
         hoek in (30, 25, 20) and grens >= hoek - 1e-6)
    toets_stl(lijst, "STL meter")
    toetsen_3mf.toets(lijst, "3MF meter")  # ronde h: ook in meters komt de 3MF in mm
    weg(lijst + [ob])


def verwachte_wand(ob, a):
    """Kleinste van schil (kom tot bolnaad) en trechterwand in mm, gemeten op het originele figuur `ob`."""
    import math
    from mathutils import Matrix
    from mathutils.bvhtree import BVHTree
    import bmesh
    r, s = a["cj_kogel_r"], a["cj_speling_mm"] * u()
    naad, open_r, lip = a["cj_naad_r"], a["cj_open_r"], a["cj_lip_d"]
    as_r = Vector(a["cj_as"]).normalized()
    punt = Vector(a["cj_snijpunt"]) - as_r * (0.0137 * u())  # de cursor
    mz = (Vector(a["cj_centrum"]) - punt).dot(as_r)
    schil = (naad - s / 2 - (r + s)) / u()
    frame = Matrix.Translation(punt) @ as_r.to_track_quat("Z", "Y").to_matrix().to_4x4()
    rot = frame.to_3x3()
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bm.transform(ob.matrix_world)
    bvh = BVHTree.FromBMesh(bm)
    bm.free()
    # Onafhankelijk van de add-on (controleur ronde j): dichte bemonstering, stap 0,01r en 120 richtingen,
    # tot en met het eindpunt op de bolnaad, dat hier met bisectie wordt gezocht in plaats van met de formule.
    hoek = math.radians(a["cj_grens_graden"] + 3.0)
    grens, kleinste = naad - s / 2, math.inf
    def buiten(t):
        return math.hypot(open_r + t * math.tan(hoek), lip + t) > grens
    lo, hi = 0.0, 10.0 * r
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if buiten(mid) else (mid, hi)
    eind = lo
    stappen = max(1, math.ceil(eind / (0.01 * r)))
    for k in range(stappen + 1):
        t = eind * k / stappen
        z, x = mz - lip - t, open_r + t * math.tan(hoek)
        for i in range(120):
            ca, sa = math.cos(2 * math.pi * i / 120), math.sin(2 * math.pi * i / 120)
            p = Vector((ca * x, sa * x, z))
            n = Vector((ca * math.cos(hoek), sa * math.cos(hoek), math.sin(hoek)))
            hit = bvh.ray_cast(frame @ p, (rot @ n).normalized())
            if hit[0] is not None:
                kleinste = min(kleinste, hit[3])
    log(f"METER: schil {schil:.3f} mm, trechterwand {kleinste / u():.3f} mm")
    return min(schil, kleinste / u())


def alles(arm):
    exact_zelf(arm)
    modifiers()
    gespiegeld()
    kijk_zonder_venster()
    meterscene()  # als laatste, want de scene blijft in meters
