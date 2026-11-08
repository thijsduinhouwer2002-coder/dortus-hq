"""Toets van de controleur op ronde c: Exploded view mag niet inbakken bij een tweede gewricht of Maak gesloten
op een verschoven deel B. Alle maten in mm."""
import bpy
from mathutils import Vector

import figuren
from hulp import delen, log, plaats, stap, u, weg


def grenzen(obs):
    """(min, max) per as in wereldcoördinaten, in mm."""
    punten = [o.matrix_world @ v.co for o in obs for v in o.data.vertices]
    return ([min(p[i] for p in punten) / u() for i in range(3)], [max(p[i] for p in punten) / u() for i in range(3)])


def tweede_gewricht(lijst):
    inst = bpy.context.scene.click_joints
    b = next(d for d in lijst if d["cj_deel"] == "B")
    inst.uit_elkaar = False
    bpy.context.view_layer.update()
    oud = grenzen([b])  # echte plek van deel B
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    log(f"TWEEDE: deel B verschoven {b.delta_location.length / u():.3f} mm voor het tweede gewricht")
    # Ronde j (regel Daan): 8 mm verder reikt de bolnaad van het tweede gewricht tot in kom en trechter van het
    # eerste (run 42471820202: 0 delen). Daar moet de add-on weigeren met de afstand uit de rekensom.
    # Direct aanroepen (niet via hulp.plaats): bij weigeren blijft deel B geselecteerd zoals de gebruiker het had.
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron, inst.kogel_auto = 0.2, 3.0, "KOGEL", "CURSOR", False
    figuren.zet_cursor((8, 0, 0), (1, 0, 0))
    figuren.maak_actief(b)
    try:
        uitslag = bpy.ops.click_joints.plaats()
    except RuntimeError as fout:  # een ERROR-melding wordt in een script een uitzondering
        uitslag = {"FOUT: " + str(fout)}
    nieuw = [d for d in delen() if d.get("cj_bron") == b.name]
    nodig = b.get("cj_te_dicht_mm")
    log(f"TWEEDE: op 8 mm uitslag={uitslag}, {len(nieuw)} nieuwe delen, cj_te_dicht_mm={nodig}, "
        f"deel B zichtbaar={b.visible_get()}")
    stap("tweede gewricht te dicht (8 mm): geweigerd, geen nieuwe delen, afstand gemeld",
         uitslag == {"CANCELLED"} and len(nieuw) == 0 and isinstance(nodig, int) and nodig > 0 and b.visible_get())
    weg(nieuw)
    # Op een plek ver genoeg weg (kogelmiddens minstens de gemelde afstand uit elkaar) moet het wel lukken.
    oud_c = Vector(b["cj_centrum"]) / u()
    x = oud_c.x + (nodig or 8)
    log(f"TWEEDE: oud kogelmidden x={oud_c.x:.3f} mm, tweede gewricht op x={x:.3f} mm")
    alle = plaats("tweede gewricht op verschoven B", b, (x, 0, 0), (1, 0, 0), kogel=3.0)
    nieuw = [d for d in alle if d.get("cj_bron") == b.name]
    stap(f"tweede gewricht: twee nieuwe delen (gevonden {len(nieuw)})", len(nieuw) == 2)
    inst.uit_elkaar = False
    bpy.context.view_layer.update()
    if len(nieuw) == 2:
        snij = Vector(nieuw[0]["cj_snijpunt"]) / u()
        mn, mx = grenzen(nieuw)
        verschil = max(abs(p - q) for p, q in zip(mn + mx, oud[0] + oud[1]))
        log(f"TWEEDE: na uitzetten grenzen nieuwe delen {[round(p, 3) for p in mn]}..{[round(p, 3) for p in mx]} mm, "
            f"deel B {[round(p, 3) for p in oud[0]]}..{[round(p, 3) for p in oud[1]]} mm, verschil {verschil:.5f} mm, "
            f"snijpunt x={snij.x:.4f} mm (cursor {x:.4f})")
        stap("tweede gewricht: delen sluiten aan op de echte plek van deel B (binnen 0,01 mm)", verschil < 0.01)
        stap("tweede gewricht: snijvlak op de cursor in echte coördinaten", abs(snij.x - x) < 0.02)
    # Maak gesloten op het verschoven deel B: de kopie hoort op de echte plek.
    inst.uit_elkaar = True
    figuren.maak_actief(b)
    bpy.context.view_layer.update()
    inst.voxel_mm = 0.5
    bpy.ops.click_joints.maak_gesloten()
    kopie = bpy.context.view_layer.objects.active
    if kopie is not b:
        mn, mx = grenzen([kopie])
        verschil = max(abs(x - y) for x, y in zip(mn + mx, oud[0] + oud[1]))
        log(f"TWEEDE: Maak gesloten op verschoven B, grenzen kopie wijken {verschil:.3f} mm af (voxel 0,5 mm)")
        stap("Maak gesloten op verschoven deel B: kopie op de echte plek (binnen 1 mm)", verschil < 1.0)
    else:
        stap("Maak gesloten op verschoven deel B: kopie gemaakt", False)
    weg(nieuw + ([kopie] if kopie is not b else []))
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
