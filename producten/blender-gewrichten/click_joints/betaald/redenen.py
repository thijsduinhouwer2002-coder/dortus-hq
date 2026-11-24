"""Pro 1.2.3 (Betrouwbaarheid, 23 nov): een leesbare reden met wat de koper kan doen, als Figure from rig een
gewricht overslaat omdat de snede zelf misging.

De kern meldt dan technische zinnen ("The cut gave no watertight parts (bad edges: part A 0, part B 3); the mesh is
unchanged.", "The parts overlap before they move; ..."). In de lijst van Figure from rig zegt dat een koper niets.
Hier wordt dat: wat er gebeurde, en wat hij kan doen (met de hand een paar mm verder plaatsen). In Blender voor 4.5
(alleen de Exact-solver) ook: een nieuwere Blender. We noemen 5.2, want 5.2 en 5.3 zijn gemeten en 4.5 niet (keuring
Betrouwbaarheid A, 24 nov). "It would be blocked" krijgt die tip niet: een geblokkeerde kogel komt vaak door de vorm
(ook in 5.3 gezien). "The cut failed" is een fout van Blender zelf en geen open snede, dus een eigen zin.
De oude kern van de zin blijft erin, want toetsen zoeken erop. Andere meldingen (te dun, te dicht, geen ruimte)
blijven zoals ze zijn: die zeggen al wat er moet gebeuren.
"""

import bpy

NIEUWER = ", or use a newer Blender such as 5.2, which cuts more reliably"


def _oud():
    return bpy.app.version < (4, 5, 0)


def leesbaar(melding):
    """De melding voor de lijst van Figure from rig; None blijft None."""
    if not melding:
        return melding
    laag = melding.lower()
    extra = NIEUWER if _oud() else ""
    if "no watertight parts" in laag:
        return f"the cut gave no watertight parts here; place it by hand a few mm along the bone{extra}"
    if "the cut failed" in laag:
        return f"Blender could not make this cut (the cut failed); place it by hand a few mm along the bone{extra}"
    if "overlap before they move" in laag:
        return f"the cut parts overlap before they move here; place it by hand a few mm along the bone{extra}"
    if "it would be blocked" in laag:
        return "no room for a ball joint that can move here (it would be blocked); place it by hand"
    return melding
