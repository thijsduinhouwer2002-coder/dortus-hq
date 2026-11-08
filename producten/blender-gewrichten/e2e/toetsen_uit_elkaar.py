"""Toets van de controleur op ronde c: Exploded view mag niet inbakken bij een tweede gewricht of Maak gesloten
op een verschoven deel B. Alle maten in mm."""
import bpy
from mathutils import Vector

import figuren
from hulp import log, plaats, stap, u, weg


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
    alle = plaats("tweede gewricht op verschoven B", b, (8, 0, 0), (1, 0, 0), kogel=3.0)
    nieuw = [d for d in alle if d.get("cj_bron") == b.name]
    stap(f"tweede gewricht: twee nieuwe delen (gevonden {len(nieuw)})", len(nieuw) == 2)
    inst.uit_elkaar = False
    bpy.context.view_layer.update()
    if len(nieuw) == 2:
        snij = Vector(nieuw[0]["cj_snijpunt"]) / u()
        mn, mx = grenzen(nieuw)
        verschil = max(abs(x - y) for x, y in zip(mn + mx, oud[0] + oud[1]))
        log(f"TWEEDE: na uitzetten grenzen nieuwe delen {[round(x, 3) for x in mn]}..{[round(x, 3) for x in mx]} mm, "
            f"deel B {[round(x, 3) for x in oud[0]]}..{[round(x, 3) for x in oud[1]]} mm, verschil {verschil:.5f} mm, "
            f"snijpunt x={snij.x:.4f} mm (cursor 8)")
        stap("tweede gewricht: delen sluiten aan op de echte plek van deel B (binnen 0,01 mm)", verschil < 0.01)
        stap("tweede gewricht: snijvlak op de cursor in echte coördinaten", abs(snij.x - 8.0) < 0.02)
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
