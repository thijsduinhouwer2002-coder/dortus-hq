"""Toetsen voor de beweegproef in de add-on (ronde k), vanuit test_achtergrond.py.

- Staaf met bekende maten: elke gemeten grens binnen 2,5 graden van de rekensom (cj_grens_graden uit maat.py),
  en "Bends ±N°" blijft de stand.
- Testarm (±261K driehoeken): het hele bereik meten (8 richtingen) onder 1 s.
- Ronde n (snoei): met en zonder snoeien dezelfde grenzen (arm en blok) en dezelfde rode vlakken (pose 45).
- Pose: echte_matrix klopt met pose, STL en 3MF van deel B gelijk met en zonder pose, voorbij de grens worden
  vlakken van deel A rood, pose 0 haalt het rood weg en zet de oude vakken terug."""
import math
import os
import struct

import bpy
from mathutils import Vector

import figuren
import toetsen_3mf
from hulp import addon, log, plaats, stap, toets_stl, u, weg


def _stl(pad):
    with open(pad, "rb") as f:
        data = f.read()
    return [struct.unpack_from("<12f", data, 84 + 50 * i) for i in range((len(data) - 84) // 50)]


def _3mf_punten(pad):
    _, model = toetsen_3mf.lees(pad)
    return [(float(v.get("x")), float(v.get("y")), float(v.get("z"))) for v in model.iter(toetsen_3mf.NS + "vertex")]


def _verschil(p, q):
    return max((abs(x - y) for a, b in zip(p, q) for x, y in zip(a, b)), default=1e9)


def staaf():
    st = figuren.staaf("staaf_beweeg", 5.0, lengte=40.0)
    lijst = plaats("BUIG staaf", st, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    stap("BUIG staaf: twee delen", len(lijst) == 2)
    if len(lijst) != 2:
        return
    a = next(d for d in lijst if d["cj_deel"] == "A")
    grenzen = list(a.get("cj_buig_graden", []))
    som = a.get("cj_grens_graden", -1.0)
    log(f"BUIG staaf: rekensom {som:.2f} graden, stand {a.get('cj_hoek')}, gemeten {grenzen} in "
        f"{a.get('cj_buig_duur_s')} s, {a.get('cj_buig_toetsen')} toetsen, uitsnede {list(a.get('cj_buig_vlakken', []))}")
    stap("BUIG staaf: 8 richtingen gemeten", len(grenzen) == 8)
    for k, g in enumerate(grenzen):
        # Controleur ronde k: eenzijdig, nooit meer dan de rekensom (plus de afronding van 0,1), hoogstens 1 graad minder.
        stap(f"BUIG staaf richting {k * 45}: {g:.1f} tussen rekensom - 1,0 en rekensom + 0,1 ({som:.2f})",
             som - 1.0 <= g <= som + 0.1)
    hoek = addon("paneel").buig_graden(a)
    stap(f"BUIG staaf: paneel Bends ±{hoek} gelijk aan de stand {a.get('cj_hoek')}", hoek == a.get("cj_hoek"))
    blok(a, next(d for d in lijst if d["cj_deel"] == "B"))
    weg(lijst)
    st.hide_set(True)


def blok(a, b):
    """Controleur ronde k: een blok aan deel A boven de huid van deel B (richting 0) laat B eerder botsen dan de
    rekensom; de kleine uitsnede ziet dat niet, de controle met de grote uitsnede wel.
    Onafhankelijke hoek: de huid van B in het buigvlak is de lijn op afstand R (staafstraal) van het kogelmidden;
    die draait mee en raakt eerst de hoek (xb, h) van het blok: R = Rc cos(90 + t - θc), dus
    t = θc + acos(R / Rc) - 90, met Rc = wortel(xb² + h²) en θc = atan2(h, xb)."""
    import bmesh
    ue, bw = addon("uit_elkaar"), addon("beweeg")
    c, as_ = Vector(a["cj_centrum"]), Vector(a["cj_as"]).normalized()
    d = ue.richtingen(as_)[0]
    w = as_.cross(d).normalized()
    R = 5.0 * u()
    xa, xb, h, dik = 2.0 * u(), 8.0 * u(), 5.6 * u(), 3.0 * u()
    bm = bmesh.new()
    bm.from_mesh(a.data)
    m_inv = ue.echte_matrix(a).inverted()
    punten = [bm.verts.new(m_inv @ (c + as_ * x + d * y + w * z))
              for x in (xa, xb) for y in (h, h + dik) for z in (-dik, dik)]
    for f in ((0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)):
        bm.faces.new([punten[i] for i in f])
    bm.to_mesh(a.data)
    bm.free()
    a.data.update()
    rc, tc = math.hypot(xb, h), math.atan2(h, xb)
    verwacht = math.degrees(tc + math.acos(R / rc)) - 90.0
    grenzen = bw.meet(a, b, u())
    snoei_gelijk("BUIG blok", a, b)
    hoek = addon("paneel").buig_graden(a)
    log(f"BUIG blok: verwacht eerste raakpunt {verwacht:.2f} graden in richting 0, gemeten {grenzen}, "
        f"opnieuw gezocht {a.get('cj_buig_opnieuw')} keer, tijd {a.get('cj_buig_duur_s')} s, Bends ±{hoek}")
    stap(f"BUIG blok: richting 0 gemeten {grenzen[0]:.1f} <= {verwacht:.2f} (+0,15 voor de facetten)",
         grenzen[0] <= verwacht + 0.15)
    stap(f"BUIG blok: richting 0 niet veel te vroeg ({grenzen[0]:.1f} >= {verwacht:.2f} - 1)", grenzen[0] >= verwacht - 1.0)
    stap(f"BUIG blok: paneel Bends ±{hoek} niet meer dan de kleinste gemeten {min(grenzen):.1f}",
         hoek is not None and hoek <= min(grenzen))
    # Ronde l: voorbij de blokgrens (maar ver binnen de grens van de nek) wordt het blok zelf rood, niet alleen de nek.
    n = len(a.data.polygons)
    blokvlakken = set(range(n - 6, n))
    b["cj_pose_richting"] = 0
    b["cj_pose_graden"] = verwacht + 2.0
    aantal = bw.kleur_botsing(bpy.context.scene, b)
    rood = a.get("cj_rood_vlakken", [])
    rode = {rood[i] for i in range(0, len(rood), 2)}
    log(f"BUIG blok rood: pose {verwacht + 2.0:.2f} graden in richting 0, {aantal} rode vlakken, "
        f"waarvan {len(rode & blokvlakken)} op het blok")
    stap("BUIG blok rood: botsing met het figuur zelf (het blok) wordt rood", len(rode & blokvlakken) > 0)
    b["cj_pose_graden"] = 0.0
    bw.kleur_botsing(bpy.context.scene, b)
    stap("BUIG blok rood: pose 0 haalt het rood weg", len(a.get("cj_rood_vlakken", [])) == 0)


def snoei_gelijk(label, a, b, moet_snoeien=False):
    """Ronde n: de grote uitsnede snoeit wat bij de geteste hoek nooit kan botsen. Toets: zonder snoeien precies
    dezelfde grenzen. Daarna opnieuw met snoeien, zodat de delen weer de gewone uitkomst dragen."""
    bw = addon("beweeg")
    met = list(a.get("cj_buig_graden", []))
    vlakken_met = list(a.get("cj_buig_vlakken", []))
    tijden = list(a.get("cj_buig_tijden", []))
    duur_met = a.get("cj_buig_duur_s")
    bw.SNOEI = False
    try:
        zonder = bw.meet(a, b, a.get("cj_eenheid_per_mm", 1.0))
        vlakken_zonder = list(a.get("cj_buig_vlakken", []))
        duur_zonder = a.get("cj_buig_duur_s")
    finally:
        bw.SNOEI = True
        bw.meet(a, b, a.get("cj_eenheid_per_mm", 1.0))
    log(f"{label} snoei: met {met} in {duur_met} s (punten, klein, groot bouwen, groot toetsen: {tijden} s; "
        f"uitsnede {vlakken_met}), zonder {zonder} in {duur_zonder} s (uitsnede {vlakken_zonder})")
    stap(f"{label}: met en zonder snoeien dezelfde grenzen", met == list(zonder) and len(met) == 8)
    if moet_snoeien:
        stap(f"{label}: snoeien maakt de grote uitsnede kleiner ({vlakken_met[2:]} tegen {vlakken_zonder[2:]})",
             len(vlakken_met) == 4 and sum(vlakken_met[2:]) < sum(vlakken_zonder[2:]))


def arm_en_pose(arm):
    lijst = plaats("BUIG arm", arm, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    stap("BUIG arm: twee delen", len(lijst) == 2)
    if len(lijst) != 2:
        return
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    duur = a.get("cj_buig_duur_s", 99.0)
    log(f"BUIG arm: gemeten {list(a.get('cj_buig_graden', []))} graden, rekensom {a.get('cj_grens_graden')}, "
        f"tijd {duur} s, {a.get('cj_buig_toetsen')} toetsen, uitsnede A/B {list(a.get('cj_buig_vlakken', []))} vlakken "
        f"(van {len(a.data.polygons)} en {len(b.data.polygons)})")
    stap(f"BUIG arm: hele bereik onder 1 s, met de controle op de grote uitsnede ({duur} s, opnieuw gezocht "
         f"{a.get('cj_buig_opnieuw')} keer)", duur < 1.0)
    stap("BUIG arm: elke richting buigt", all(g > 0 for g in a.get("cj_buig_graden", [0])))
    snoei_gelijk("BUIG arm", a, b, moet_snoeien=True)

    inst = bpy.context.scene.click_joints
    ue = addon("uit_elkaar")
    exportmap = inst.exportmap
    # Zonder pose: STL en 3MF van deel B als referentie.
    inst.pose_graden = 0.0
    toets_stl(lijst, "BUIG STL pose 0")
    stl_0 = _stl(b["cj_stl"])
    toetsen_3mf.toets(lijst, "BUIG 3MF pose 0")
    mf_0 = _3mf_punten(b["cj_3mf"])
    echt_0 = ue.echte_matrix(b).copy()
    vakken_0 = [p.material_index for p in a.data.polygons]

    # Pose binnen de grens: geen rood, en echte_matrix gelijk.
    inst.pose_richting = "2"
    inst.pose_graden = 20.0
    bpy.context.view_layer.update()
    c = Vector(b["cj_centrum"])
    e = Vector(b["cj_as"]).normalized() * ue.afstand(b) if inst.uit_elkaar else Vector()
    beeld = b.matrix_world @ ue.echte_matrix(b).inverted()  # wat de weergave er bovenop doet
    hoek = math.degrees(beeld.to_quaternion().angle)
    verschuiving = (beeld @ c - (c + e)).length / u()
    afw = max(abs(x - y) for r1, r2 in zip(ue.echte_matrix(b), echt_0) for x, y in zip(r1, r2))
    log(f"BUIG pose 20: weergave draait {hoek:.3f} graden, kogelmidden blijft op zijn plek tot {verschuiving:.6f} mm, "
        f"echte_matrix wijkt {afw:.2e} af, rode vlakken {len(a.get('cj_rood_vlakken', [])) // 2}")
    stap("BUIG pose 20: deel B draait 20 graden in beeld", abs(hoek - 20.0) < 1e-3)
    stap("BUIG pose 20: draaipunt is het kogelmidden", verschuiving < 1e-4)
    stap("BUIG pose 20: echte_matrix gelijk aan zonder pose", afw < 1e-6)
    grens = a["cj_buig_graden"][2]
    if grens > 20.0:
        stap("BUIG pose 20 (binnen de grens): geen rode vlakken", len(a.get("cj_rood_vlakken", [])) == 0)
    toets_stl(lijst, "BUIG STL pose 20")
    stl_20 = _stl(b["cj_stl"])
    toetsen_3mf.toets(lijst, "BUIG 3MF pose 20")
    mf_20 = _3mf_punten(b["cj_3mf"])
    v_stl, v_mf = _verschil(stl_0, stl_20), _verschil(mf_0, mf_20)
    log(f"BUIG export: STL deel B verschil {v_stl:.6f} mm ({len(stl_0)} en {len(stl_20)} driehoeken), "
        f"3MF verschil {v_mf:.6f} mm")
    stap("BUIG: STL van deel B gelijk met en zonder pose", len(stl_0) == len(stl_20) > 0 and v_stl < 1e-4)
    stap("BUIG: 3MF van deel B gelijk met en zonder pose", len(mf_0) == len(mf_20) > 0 and v_mf < 1e-4)
    stap("BUIG: na export staat de pose er nog", abs(math.degrees((b.matrix_world @ ue.echte_matrix(b).inverted())
                                                                   .to_quaternion().angle) - 20.0) < 1e-3)

    # Voorbij de grens: botsende vlakken van deel A rood.
    inst.pose_graden = 45.0
    rood = a.get("cj_rood_vlakken", [])
    rood_mat = addon("kleur").materiaal("rood")
    vakken = [a.data.materials[a.data.polygons[rood[i]].material_index] for i in range(0, len(rood), 2)]
    log(f"BUIG pose 45 (grens {grens:.1f}): {len(rood) // 2} rode vlakken op deel A, materialen "
        f"{sorted({m.name if m else None for m in vakken}, key=str)}")
    stap("BUIG pose 45: vlakken van deel A rood", len(rood) > 0 and all(m == rood_mat for m in vakken))
    bw = addon("beweeg")
    met = {rood[i] for i in range(0, len(rood), 2)}
    bw.SNOEI = False
    try:
        bw.kleur_botsing(bpy.context.scene, b)
        r2 = a.get("cj_rood_vlakken", [])
        zonder = {r2[i] for i in range(0, len(r2), 2)}
    finally:
        bw.SNOEI = True
        bw.kleur_botsing(bpy.context.scene, b)
    log(f"BUIG pose 45 snoei: rode vlakken met {len(met)}, zonder {len(zonder)}")
    stap("BUIG pose 45: met en zonder snoeien dezelfde rode vlakken", met == zonder and len(met) > 0)
    # Terug op 0: rood weg, oude vakken terug.
    bpy.ops.click_joints.reset_pose()
    terug = [p.material_index for p in a.data.polygons]
    stap("BUIG reset pose: pose 0", inst.pose_graden == 0.0 and b.get("cj_pose_graden") == 0.0)
    stap("BUIG reset pose: rood weg en alle vakken van deel A zoals eerst",
         len(a.get("cj_rood_vlakken", [])) == 0 and terug == vakken_0)
    stap("BUIG reset pose: deel B weer recht", (b.matrix_world @ ue.echte_matrix(b).inverted()).to_quaternion().angle < 1e-6)
    inst.exportmap = exportmap
    weg(lijst)


def alles(arm):
    staaf()
    arm_en_pose(arm)
    arm.hide_set(True)
    log(f"BUIG klaar, exportmap {os.path.basename(bpy.context.scene.click_joints.exportmap.rstrip(os.sep))}")
