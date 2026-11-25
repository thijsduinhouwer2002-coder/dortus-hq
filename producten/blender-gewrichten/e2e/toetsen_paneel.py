"""1.2.9 (issue 70): volgorde van het paneel in de betaalde build, zonder scherm.

Het hoofdpaneel tekent in een nep-layout die elke regel en knop in volgorde opschrijft. Dan kijken we:
1. met een rig aan je mesh staat "Figure from rig" bovenaan, vóór stap 1 (zonder rig niet);
2. de proefstrip staat in stap 2 onder Clearance en vóór Place joint;
3. het scharnier staat in stap 2 onder Place joint en vóór stap 3 (niet meer los onder Export);
4. de regel om te beoordelen komt pas na een goed resultaat, met de twee winkels van Pro;
5. bij een geplaatst scharnier zegt stap 3 "Hinge placed" (Daan #83 C2: stap 2 houdt Ball blauw voor het volgende).
Aangeroepen vanuit test_betaald.py met toets(stap, eigen)."""
import sys
from types import SimpleNamespace

import bpy


class Nep:
    """Nep-UILayout: alles wat getekend wordt komt in één gedeelde lijst, in volgorde."""

    def __init__(self, log):
        self.log = log
        self.scale_y = 1.0
        self.alert = False
        self.enabled = True

    def _kind(self, *_a, **_k):
        return Nep(self.log)

    box = column = row = split = grid_flow = _kind

    def label(self, text="", **_k):
        self.log.append(("label", text))

    def prop(self, _data, naam, text=None, **_k):
        self.log.append(("prop", naam))

    def operator(self, idname, text=None, **_k):
        self.log.append(("op", text if text is not None else idname))
        return SimpleNamespace()

    def separator(self, **_k):
        pass


def teken(eigen, ob):
    paneel = sys.modules[eigen + ".paneel"]
    log = []
    ctx = SimpleNamespace(scene=bpy.context.scene, active_object=ob, window_manager=bpy.context.window_manager)
    zelf = SimpleNamespace(layout=Nep(log))
    paneel.CLICK_JOINTS_PT_paneel.draw(zelf, ctx)
    return log


def plek(log, soort, tekst_begin):
    for i, (s, t) in enumerate(log):
        if s == soort and str(t).startswith(tekst_begin):
            return i
    return -1


def toets(stap, eigen):
    meld = sys.modules[eigen + ".meld"]
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.mesh.primitive_cube_add(size=0.02)
    lijf = bpy.context.active_object
    lijf.name = "paneel_lijf"

    zonder = teken(eigen, lijf)
    stap("paneel zonder rig: geen Figure from rig bovenaan", plek(zonder, "label", "Rig found") == -1)

    bpy.ops.object.armature_add()
    arm = bpy.context.active_object
    arm.name = "paneel_rig"
    mod = lijf.modifiers.new("Armature", "ARMATURE")
    mod.object = arm
    log = teken(eigen, lijf)
    print("[cj-betaald] paneel:", " | ".join(str(t) for _s, t in log))
    rig_i, stap1 = plek(log, "label", "Rig found"), plek(log, "label", "1  Place")
    stap("paneel met rig: Figure from rig vóór stap 1", 0 <= rig_i < stap1, f"({rig_i}, {stap1})")
    knop = plek(log, "op", "click_joints.figuur_uit_rig")
    stap("paneel met rig: grote knop Figure from rig bovenaan", 0 <= knop < stap1, f"({knop})")

    speling, proef = plek(log, "prop", "speling_mm"), plek(log, "label", "Not sure? Print a fit test")
    plaats, scharnier = plek(log, "op", "Place joint"), plek(log, "label", "Or a hinge")
    stap3, export = plek(log, "label", "3  Fit and export"), plek(log, "op", "Export")
    stap("paneel: proefstrip in stap 2 tussen Clearance en Place joint", 0 <= speling < proef < plaats,
         f"({speling}, {proef}, {plaats})")
    stap("paneel: scharnier in stap 2 onder Place joint, vóór stap 3", 0 <= plaats < scharnier < stap3,
         f"({plaats}, {scharnier}, {stap3})")
    stap("paneel: niets van Pro meer onder Export", export >= 0 and not any(
        str(t).startswith(("Not sure", "Or a hinge", "Rig found")) for _s, t in log[export:]))

    stap("beoordelen: Pro wijst naar Superhive en Gumroad", [w for w, _l in meld.BEOORDEEL] == ["Superhive", "Gumroad"])
    stap("beoordelen: gratis wijst naar Blender Extensions",
         [w for w, _l in meld.BEOORDEEL_GRATIS] == ["Blender Extensions"])
    stap("beoordelen: niet zonder goed resultaat", not meld.goed_resultaat([lijf]))
    lijf["cj_passing"] = "groen"
    stap("beoordelen: wel na Good fit", meld.goed_resultaat([lijf]))
    log = []
    meld.CLICK_JOINTS_PT_meld.draw(SimpleNamespace(layout=Nep(log)), SimpleNamespace(scene=bpy.context.scene))
    stap("beoordelen: regel en twee knoppen boven Report a problem",
         plek(log, "label", "Happy with it") == 0 and [t for s, t in log if s == "op"][:2] == ["Superhive", "Gumroad"],
         str(log))

    delen = []
    for deel in ("A", "B"):
        bpy.ops.mesh.primitive_cube_add(size=0.02)
        d = bpy.context.active_object
        d.name = f"paneel_scharnier_{deel}"
        for k, v in {"cj_soort": "SCHARNIER", "cj_bron": "paneel_lijf", "cj_deel": deel,
                  "cj_snijpunt": [0.0, 0.0, 0.0], "cj_bereik_graden": 135.0, "cj_stand": 0, "cj_passing": "groen"}.items():  # een Blender-object heeft geen update()
            d[k] = v
        delen.append(d)
    log = teken(eigen, delen[1])
    stap3, klaar = plek(log, "label", "3  Fit and export"), plek(log, "label", "Hinge placed")
    stap("scharnier geplaatst: stap 3 zegt Hinge placed", 0 <= stap3 < klaar, f"({stap3}, {klaar})")

    for o in [lijf, arm] + delen:
        bpy.data.objects.remove(o, do_unlink=True)
