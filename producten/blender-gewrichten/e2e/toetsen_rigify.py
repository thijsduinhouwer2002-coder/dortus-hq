"""Toets Pro 1.1 (16 nov run 11): "Figure from rig" op de echte Rigify-metarig (Human), figuur uit e2e/proef_rigify.py.

Eerst gevonden als proef: met de knieën erbij stonden beide heupen op "±0° (blocked)". Oorzaak: de snede van de knie
loopt tot de grens van een_lid (1,2 keer de reik plus s, hier ±23,7 mm de dij in), de afstandsregel kogel naast
scharnier rekende met de reik (19,6). De kom van de heup kwam in de snede van de knie. Nu (afstand.snede_reik) en met
plekken per halve mm tussen "bolnaad vrij van de romp" en de oude plek vindt de heup een plek die beweegt.
Eisen:
- geen enkel gewricht in de lijst staat op blocked (vangnet: een kogel die niet beweegt wordt teruggedraaid);
- beide heupen staan erin met meer dan 10 graden (5.x; in Blender voor 4.5 mag een heup ontbreken door de bekende
  booleanfout van de Exact-solver, mits met reden);
- knieën en ellebogen staan erin als scharnier;
- alle zichtbare delen zijn gesloten; bij elk overgeslagen gewricht staat een reden.
Gebruik: blender -b --factory-startup --python e2e/toetsen_rigify.py -- <betaalde zip>
"""
import importlib
import os
import re

import bpy

FOUT = []


def log(t):
    print(f"[cj-rigify] {t}", flush=True)


def eis(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


hier = os.path.dirname(os.path.abspath(__file__))
os.environ.pop("CJ_ALLEEN", None)
os.environ.pop("CJ_HOOK", None)
os.environ.pop("CJ_NA", None)
exec(compile(open(os.path.join(hier, "proef_rigify.py")).read(), "proef_rigify.py", "exec"))

fig = importlib.import_module("bl_ext.user_default.click_joints.betaald.figuur")
alle = fig.figuur_gewrichten(bpy.context.scene.objects, "held")
regels = [fig.regel(x) for x in alle]
oud = bpy.app.version < (4, 5, 0)
log(f"Blender {bpy.app.version_string}, regels {regels}")
eis(not any("blocked" in r for r in regels), "geen gewricht op blocked")
for kant in ("Left", "Right"):
    for lid in ("knee", "elbow"):
        r = next((x for x in regels if x.startswith(f"{kant} {lid}")), None)
        eis(r is not None and "Hinge" in r or (oud and r is None), f"{kant} {lid} als scharnier ({r})")
    r = next((x for x in regels if x.startswith(f"{kant} hip")), None)
    g = re.search(r"±(\d+)°", r or "")
    eis((r is not None and g is not None and int(g.group(1)) > 10) or (oud and r is None),
        f"{kant} hip beweegt meer dan 10 graden ({r})")
over = next((o.get("cj_rig_overgeslagen") for o in bpy.context.scene.objects if o.get("cj_deel")), "") or ""
for stuk in [s for s in over.split("; ") if s]:
    eis("(" in stuk and not stuk.endswith("()"), f"overgeslagen met reden: {stuk}")
ges = importlib.import_module("bl_ext.user_default.click_joints.gesloten")
delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == "held" and o.visible_get() and o.type == "MESH"]
eis(len(delen) >= len(alle) + 1 and all(ges.is_gesloten(o)[0] for o in delen),
    f"{len(delen)} delen, alle gesloten ({len(alle)} gewrichten)")
log(f"KLAAR {len(FOUT)} FOUT")
