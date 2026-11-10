"""Afstand tussen gewrichten op één deel (eis 6, twee kan-punten van de controleur na eis 8).

(b) Alle scharnieren van een deel. Elk deel draagt cj_scharnieren: een platte lijst getallen, per scharnier STAP = 5
    (snijpunt x, y, z in wereldcoordinaten, reik, knokkel_r), in Blender-eenheden. Plat, want een lijst getallen
    bewaart Blender zeker als eigenschap (ook in een .blend). Een deel van voor deze lijst heeft alleen cj_snijpunt,
    cj_reik en cj_knokkel_r; dat telt als een lijst van één (terugwaartse werking, de oude sleutels blijven ook staan).
    Na een snede krijgt elk deel de oude punten die op dat deel liggen, plus het nieuwe scharnier (zie
    scharnier_vorm.kant voor een scharnier en markeer_kogel voor een kogel).
(a) Kogel naast scharnier. Nodige afstand tussen het snijpunt van het scharnier en het kogelmidden:
        reik van het scharnier + reik van de kogel.
    Reik van het scharnier (scharnier_vorm.reik): hoe ver stopvlakken, wangen en zaagsnede langs L van de snede
    reiken, plus s. Reik van de kogel: naad_r + 0,4 r, de bolnaad met de nek eronder; hetzelfde getal dat de kern
    voor een nieuw gewricht neemt (maat.te_dicht). Bewust ook aan de komkant naad_r + 0,4 r en niet r + s zoals de
    kern voor een oud gewricht aan de komkant doet: de zaagsnede en de stopvlakken van een scharnier lopen over de
    hele doorsnede van het lid, en zo is de grens in beide volgordes (eerst scharnier of eerst kogel) dezelfde.
    Nooit minder dan r + s (de kom). Bij een pen (geen bolnaad): 1,5 r + s, de pen reikt 0,4 r onder het snijvlak
    en het midden ligt op 1,1 r, het gat r + s eromheen.

De kogel zelf zit in het gratis deel, dat niet verandert. Daarom omhult betaald/__init__.py in register() aan het eind
gewricht.te_dicht (te_dicht_kogel: ook de scharnieren van het deel tellen mee) en gewricht.markeer (markeer_kogel:
de delen van een kogel erven de scharnieren die op hun kant liggen), en zet ze in unregister() alleen terug als ze
nog van ons zijn."""
import math

import bpy
from mathutils import Vector

STAP = 5

_oud_te_dicht = [None]
_oud_markeer = [None]


def scharnieren(ob):
    """[(snijpunt, reik, knokkel_r)] van alle scharnieren op het deel (reik -1 als die niet bekend is)."""
    if "cj_scharnieren" in ob:
        v = [float(x) for x in ob["cj_scharnieren"]]
        return [(Vector(v[i:i + 3]), v[i + 3], v[i + 4]) for i in range(0, len(v) - STAP + 1, STAP)]
    if ob.get("cj_soort") == "SCHARNIER" and "cj_snijpunt" in ob:
        return [(Vector(ob["cj_snijpunt"]), float(ob.get("cj_reik", -1.0)), float(ob.get("cj_knokkel_r", 0.0)))]
    return []


def plat(lijst):
    """De lijst van scharnieren als platte lijst getallen voor cj_scharnieren."""
    return [float(c) for p, reik, k in lijst for c in (p[0], p[1], p[2], reik, k)]


def kogel_reik(naad_r, r, s):
    """Reik van een kogel of pen vanaf het midden (zie boven), in Blender-eenheden."""
    if naad_r > 0:
        return max(naad_r + 0.4 * r, r + s)
    return 1.5 * r + s


def kogel_van(ob, u):
    """(kogelmidden, reik) van de kogel of pen waarvan dit deel komt, of None."""
    if ob.get("cj_soort", "") not in ("KOGEL", "PEN") or "cj_centrum" not in ob:
        return None
    s = float(ob.get("cj_speling_mm", 0.2)) * u
    return Vector(ob["cj_centrum"]), kogel_reik(float(ob.get("cj_naad_r", -1.0)), float(ob.get("cj_kogel_r", 0.0)), s)


def nodig_mm(paren, u):
    """paren: [(afstand, nodige afstand)] in Blender-eenheden. De grootste nodige afstand die niet gehaald wordt, in
    mm naar boven afgerond (zoals de kern), of None als alles ver genoeg is."""
    te = [n / u for d, n in paren if d / u < n / u]
    return math.ceil(max(te) - 1e-9) if te else None


def te_dicht_kogel(bron, centrum, richting, maat, u):
    """Omhulsel van gewricht.te_dicht: eerst de kern (kogel naast kogel), dan elk scharnier op het deel."""
    kern = _oud_te_dicht[0](bron, centrum, richting, maat, u)
    reik_k = kogel_reik(maat.get("naad_r", -1.0), maat["r"], maat["s"])
    paren = [((Vector(centrum) - p).length, reik + reik_k) for p, reik, _k in scharnieren(bron) if reik >= 0]
    eigen = nodig_mm(paren, u)
    uit = [n for n in (kern, eigen) if n is not None]
    return max(uit) if uit else None


def markeer_kogel(ob, kleur, gegevens, maat=None, u=1.0):
    """Omhulsel van gewricht.markeer: na de kern krijgt een deel van de kogel de scharnieren van de bron die aan zijn
    kant van het snijvlak liggen (deel A onder het vlak langs de as, deel B erboven). De snede van de kogel is buiten
    de bolnaad vlak, en elk scharnier ligt verder dan zijn reik plus die van de kogel, dus het teken van de afstand
    tot het vlak is genoeg."""
    _oud_markeer[0](ob, kleur, gegevens, maat, u)
    if maat is None or "cj_snijpunt" not in gegevens or ob.get("cj_deel") not in ("A", "B"):
        return
    bron = bpy.data.objects.get(gegevens.get("cj_bron", ""))
    lijst = scharnieren(bron) if bron is not None else []
    vlak, as_ = Vector(gegevens["cj_snijpunt"]), Vector(gegevens["cj_as"])
    boven = ob.get("cj_deel") == "B"
    eigen = [e for e in lijst if ((e[0] - vlak).dot(as_) >= 0) == boven]
    if eigen:
        ob["cj_scharnieren"] = plat(eigen)


def register(gewricht):
    if _oud_te_dicht[0] is None:
        _oud_te_dicht[0] = gewricht.te_dicht
        gewricht.te_dicht = te_dicht_kogel
    if _oud_markeer[0] is None:
        _oud_markeer[0] = gewricht.markeer
        gewricht.markeer = markeer_kogel


def unregister(gewricht):
    if _oud_te_dicht[0] is not None:
        if gewricht.te_dicht is te_dicht_kogel:  # alleen terugzetten als het nog ons omhulsel is
            gewricht.te_dicht = _oud_te_dicht[0]
        _oud_te_dicht[0] = None
    if _oud_markeer[0] is not None:
        if gewricht.markeer is markeer_kogel:
            gewricht.markeer = _oud_markeer[0]
        _oud_markeer[0] = None
