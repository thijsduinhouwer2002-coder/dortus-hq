"""Pro 1.3 kandidaat 5 (keuring 6dcadc8, A4): een kogelsnede die in rust al vastzit, één keer overdoen met Exact.

Spoor Olaf (23 nov): op de robot van studio-2 gaf de Manifold-snede van de linkerheup op een AMD-runner delen die
in rust al overlappen (beweegproef 0°, "blocked"); op Intel een gave heup. De omweg van 6dcadc8 (een plek 0,3 mm
verder) hielp daar, maar was op MakeHuman net zo vaak kapot. Hier daarom de oorzaak zelf: zit een kogel na een
Manifold-snede vast, dan draait Figure from rig die snede terug en snijdt dezelfde plek opnieuw met Exact
(langzamer, maar rekent niet parallel). Pas als die ook vastzit, gaat de zoektocht naar de volgende plek.
Komt alleen aan de beurt na een weigering, dus een figuur waar het al lukte merkt niets.

PROEF, NIET VOOR MAIN (Olaf 23 nov, lokaal Blender 5.3.0, MakeHuman 220 mm, toets CJ_HERKANS=3, GEZIEN): de
Exact-snede geeft op deze figuur op geen enkele plek gesloten delen: linkerschouder 8 van 8 en linkerheup 11 van 11
"no watertight parts", ook met Self Intersection aan. Exact is hier dus geen herkansing.
"""

# Alleen voor de toets (CJ_HERKANS=2): zo kan een toets zien hoe vaak het herstel liep.
TELLER = {"exact": 0}


def opnieuw_exact(context, doel, voor, m, plaats):
    """Draai de laatste snede terug en doe `plaats()` op dezelfde cursor m met de Exact-solver.

    Geeft (ok, melding, nieuw) van de tweede snede, of None als er niets te herstellen viel (al Exact, of geen
    Manifold in deze Blender). `plaats` is een functie zonder argumenten die figuur.plaats_gewricht aanroept."""
    from .. import gewricht
    from .rig import draai_terug
    if gewricht.solver_naam() != "MANIFOLD":
        return None
    draai_terug(context, doel, voor)
    for o in [o for o in context.view_layer.objects if o is not None]:
        o.select_set(False)
    doel.select_set(True)
    context.view_layer.objects.active = doel
    context.scene.cursor.matrix = m
    oud, oud_zelf = gewricht.FORCEER_SOLVER, gewricht.EXACT_ZELF
    gewricht.FORCEER_SOLVER = "EXACT"
    gewricht.EXACT_ZELF = True
    TELLER["exact"] += 1
    try:
        return plaats()
    finally:
        gewricht.FORCEER_SOLVER, gewricht.EXACT_ZELF = oud, oud_zelf
