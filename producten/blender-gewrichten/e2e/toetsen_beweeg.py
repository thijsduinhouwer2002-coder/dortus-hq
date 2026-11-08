"""Toetsen voor de beweegproef in de add-on (ronde k), vanuit test_achtergrond.py.

- Staaf met bekende maten: elke gemeten grens binnen 2,5 graden van de rekensom (cj_grens_graden uit maat.py),
  en "Bends ±N°" blijft de stand.
- Testarm (±261K driehoeken): het hele bereik meten (8 richtingen) onder 1 s.
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
        stap(f"BUIG staaf richting {k * 45}: {g:.1f} binnen 2,5 graden van de rekensom {som:.2f}", abs(g - som) <= 2.5)
    hoek = addon("paneel").buig_graden(a)
    stap(f"BUIG staaf: paneel Bends ±{hoek} gelijk aan de stand {a.get('cj_hoek')}", hoek == a.get("cj_hoek"))
    weg(lijst)
    st.hide_set(True)


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
    stap(f"BUIG arm: hele bereik onder 1 s ({duur} s)", duur < 1.0)
    stap("BUIG arm: elke richting buigt", all(g > 0 for g in a.get("cj_buig_graden", [0])))

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
