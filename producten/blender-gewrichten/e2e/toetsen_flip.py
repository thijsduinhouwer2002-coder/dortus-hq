"""Toets Flip bend van het scharnier (ontwerp punt 4, ronde t2 d), aangeroepen vanuit toetsen_scharnier.py."""
import sys

import bpy
from mathutils import Vector

import figuren
from hulp_scharnier import bvh as _bvh
from hulp_scharnier import cursor as _cursor


def _plaats_staaf(flip, **extra):
    """Lege mm-scene, staaf straal 5 actief, cursor als bij de andere toetsen; (uitslag, A, B)."""
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm = 0.2
    inst.as_bron = extra.pop("as_bron", "CURSOR")
    staaf = figuren.staaf("staaf", 5.0)
    figuren.maak_actief(staaf)
    _cursor((0, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    uitslag = bpy.ops.click_joints.plaats_scharnier(stand="115", flip_bend=flip, **extra)
    return uitslag, bpy.data.objects.get("staaf_A"), bpy.data.objects.get("staaf_B")


def toets_flip(stap, eigen):
    """Ontwerp punt 4, ronde t2 (d): Flip bend uit en aan op stand 115. Beide keren twee gesloten delen en een
    eindstop van 113 tot 115 graden gemeten in de mesh, maar aan tegengestelde kanten. Kant onafhankelijk van
    de add-on gemeten: B draait om een vaste wereldas W = L x buigkant(uit). Zonder flip komt B bij +W pas op
    de eindstop en bij -W al op de achterstop; met flip precies andersom. Daarnaast: de stopvlakken (de
    wigpunt van A) liggen aan de kant van de buigkant."""
    gesloten = sys.modules[eigen + ".gesloten"]
    beweeg = sys.modules[eigen + ".betaald.scharnier_beweeg"]
    vorm = sys.modules[eigen + ".betaald.scharnier_vorm"]
    uit = {}
    w = None
    for flip in (False, True):
        naam = f"flip {'aan' if flip else 'uit'}"
        uitslag, a, b = _plaats_staaf(flip)
        if uitslag != {"FINISHED"} or a is None or b is None:
            stap(f"{naam}: scharnier geplaatst", False, str(uitslag))
            return
        ga, gb = gesloten.is_gesloten(a), gesloten.is_gesloten(b)
        stap(f"{naam}: twee gesloten delen (0 open randen)", ga[0] and gb[0], f"A {ga[1]} B {gb[1]} foute randen")
        p = Vector(b["cj_scharnier_punt"])
        buig, lid = Vector(b["cj_buigkant"]).normalized(), Vector(b["cj_as"]).normalized()
        if w is None:
            w = lid.cross(buig).normalized()
        pb, tb = beweeg._driehoeken(b, p, 1e9)
        bvh_a = _bvh(a)
        plus = beweeg._grens(bvh_a, pb, tb, p, w, beweeg.MAX_VOOR, beweeg.STAP_VOOR)
        min_ = beweeg._grens(bvh_a, pb, tb, p, -w, beweeg.MAX_VOOR, beweeg.STAP_VOOR)
        voor = float(b.get("cj_bereik_graden", -1))
        eind, terug = (min_, plus) if flip else (plus, min_)
        stap(f"{naam}: eindstop add-on tussen 113 en 115 graden", 113 <= voor <= 115.05, f"gemeten {voor:.2f}")
        stap(f"{naam}: eigen beweegproef om vaste as W, eindstop aan de {'-W' if flip else '+W'} kant 113 tot 115",
             eind is not None and 113 <= eind <= 115.05 and abs(eind - voor) <= 0.1,
             f"+W {plus} -W {min_} graden")
        stap(f"{naam}: andere kant ({'+W' if flip else '-W'}) stuit op de achterstop onder 5 graden",
             terug is not None and terug < 5.0, f"{terug}")
        # Stopvlakken: het platte achterstopvlak van A (z = -s/2, buiten de wangen) ligt achter H, dus aan de
        # kant tegenover de buigkant; de wig (eindstop) opent naar de buigkant.
        u = sys.modules[eigen + ".eigenschappen"].eenheid_per_mm(bpy.context.scene)
        s = float(b["cj_speling_mm"]) * u
        h = Vector(b["cj_scharnier_as"]).normalized()
        achter = []
        for v in a.data.vertices:
            d = a.matrix_world @ v.co - p
            if abs(d.dot(lid) + s / 2) < 1e-4 * u and (d - h * d.dot(h)).length > float(b["cj_naad_r"]) + s:
                achter.append(d.dot(buig))
        stap(f"{naam}: achterstopvlak van A tegenover de buigkant, wig opent naar de buigkant",
             bool(achter) and max(achter) < 0,
             f"{len(achter)} punten, grootste afstand naar de buigkant {max(achter) if achter else 0:.3f} mm")
        k = round(voor)
        kop = "Hinge placed, bend flipped" if flip else "Hinge placed"
        stap(f"{naam}: melding toont het gemeten bereik", b.get("cj_melding") == f"{kop}. Bends 0° to {k}°.",
             str(b.get("cj_melding")))
        stap(f"{naam}: cj_flip_bend opgeslagen", bool(b.get("cj_flip_bend")) == flip)
        uit[flip] = (buig, plus, min_)
    stap("flip: buigkant tegengesteld", uit[False][0].dot(uit[True][0]) < -0.999,
         f"dot {uit[False][0].dot(uit[True][0]):.6f}")
    # Controleur (d), punt 1: op dezelfde plek van een bestaand scharnier weigert de operator (geen extra delen).
    a_oud = bpy.data.objects.get("staaf_A")
    figuren.maak_actief(a_oud)
    voor_namen = {o.name for o in bpy.data.objects}
    try:
        tweede = bpy.ops.click_joints.plaats_scharnier(stand="115", flip_bend=False)
    except RuntimeError as fout:
        tweede = f"fout: {fout}"
    nieuw = {o.name for o in bpy.data.objects} - voor_namen
    stap("opnieuw snijden op hetzelfde scharnier geweigerd, geen nieuwe objecten",
         tweede == {"CANCELLED"} and not nieuw, f"{tweede}, nieuw {sorted(nieuw)}")
    # Lidas omhoog op het scherm: omhoog zegt niets, buigkant vast L x H, flip keert hem om.
    lid = Vector((1, 0, 0))
    kijk = Vector((0, 0, -1))
    z = [vorm.scharnier_assen(lid, kijk=kijk, omhoog=lid.copy(), omdraaien=f) for f in (False, True)]
    stap("lidas omhoog op het scherm: buigkant vast en flip keert hem om", None not in z
         and abs(z[0][1].dot(lid)) < 1e-6 and z[0][1].dot(z[1][1]) < -0.999
         and abs(z[0][0].dot(Vector((0, 0, 1)))) > 0.999, str(z[0] and tuple(z[0][1])))
    for flip in (False, True):
        naam = f"kijk met lidas omhoog op het scherm, flip {'aan' if flip else 'uit'}"
        try:
            uitslag, a, b = _plaats_staaf(flip, as_bron="KIJK", kijk_richting=tuple(kijk), kijk_omhoog=tuple(lid))
        except RuntimeError as fout:
            solver = sys.modules[eigen + ".gewricht"].solver_naam()
            if solver != "MANIFOLD":
                print(f"[cj-betaald] BEKEND {naam} op {solver}: {fout}")
                continue
            uitslag, a, b = {"CANCELLED"}, None, None
        if uitslag != {"FINISHED"} or a is None or b is None:
            stap(f"{naam}: scharnier geplaatst", False, str(uitslag))
            continue
        buig = Vector(b["cj_buigkant"]).normalized()
        verwacht = z[1 if flip else 0][1]
        ga, gb = gesloten.is_gesloten(a), gesloten.is_gesloten(b)
        voor = float(b.get("cj_bereik_graden", -1))
        stap(f"{naam}: buigkant zoals gekozen, gesloten, eindstop 113 tot 115",
             buig.dot(verwacht) > 0.999 and ga[0] and gb[0] and 113 <= voor <= 115.05,
             f"buig {tuple(round(c, 3) for c in buig)} A {ga[1]} B {gb[1]} eindstop {voor:.2f}")
