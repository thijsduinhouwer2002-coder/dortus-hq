"""Gradenboog van de beweegproef (Daan, beoordeling 3, moet 1): de vorm in 3D, los van het tekenen.

Eén boog in de gekozen richting, van de as tot de gemeten grens, met streepjes elke 5 graden en het getal
aan het eind. Dat getal is altijd hetzelfde als in het paneel: `paneel.richting_graden` (gemeten grens in
de gekozen richting, nooit meer dan stand en rekensom, naar beneden afgerond). De andere zeven richtingen
worden één dunne gesloten lijn door de grenspunten. Alles in wereldcoördinaten; waaier.py projecteert
het naar pixels. Zonder scherm te toetsen (e2e/toetsen_boog.py)."""
import math

from . import paneel, uit_elkaar

STRAAL = 4.0       # keer de kogelstraal (2 keer de diameter, mag blijven van Daan)
STREEP = 5         # graden tussen twee streepjes
OMTREK_PUNTEN = 48  # punten van de gesloten lijn door de grenzen
POSE_LANG = 1.15   # pose-lijn iets langer dan de boog


def _punt(c, as_, rich, R, graden):
    t = math.radians(graden)
    return c + R * (as_ * math.cos(t) + rich * math.sin(t))


def grenzen(a):
    """Grens per richting zoals het paneel hem telt (stand en rekensom als plafond), niet afgerond.
    Alleen aanroepen als paneel.richting_graden een getal gaf (dan zijn stand en rekensom groter dan 0)."""
    plafond = min(float(a["cj_hoek"]), float(a["cj_grens_graden"]))
    return [min(float(g), plafond) for g in a["cj_buig_graden"]]


def omtrek_graden(gr, phi):
    """Grens bij hoek phi (graden rond de as), lineair in graden tussen de twee richtingen ernaast."""
    n = len(gr)
    stap = 360.0 / n
    k = int(math.floor(phi / stap)) % n
    f = (phi - k * stap) / stap
    return gr[k] * (1.0 - f) + gr[(k + 1) % n] * f


def vorm(a, k, pose):
    """Alles van de gradenboog voor deel A in richting k bij een pose (graden), in wereldcoördinaten.
    Geeft None als er geen getal is (geen stand, of rood)."""
    from mathutils import Vector
    n = paneel.richting_graden(a, k)
    if n is None:
        return None
    c = Vector(a["cj_centrum"])
    as_ = Vector(a["cj_as"]).normalized()
    rich = uit_elkaar.richtingen(as_)
    r_k = rich[k % len(rich)]
    R = STRAAL * a["cj_kogel_r"]
    gr = grenzen(a)
    boog = [_punt(c, as_, r_k, R, n * i / max(1, n)) for i in range(max(1, n) + 1)] if n > 0 else [_punt(c, as_, r_k, R, 0)]
    # streepjes: (graden, punt op de boog, punt iets naar buiten voor de richting in pixels)
    streep = [(g, _punt(c, as_, r_k, R, g), _punt(c, as_, r_k, R * 1.1, g)) for g in range(0, n + 1, STREEP)]
    u, w = rich[0], rich[len(rich) // 4]
    omtrek = []
    for i in range(OMTREK_PUNTEN):
        phi = 360.0 * i / OMTREK_PUNTEN
        d = u * math.cos(math.radians(phi)) + w * math.sin(math.radians(phi))
        omtrek.append(_punt(c, as_, d, R, omtrek_graden(gr, phi)))
    voorbij = pose > gr[k % len(gr)] + 1e-6
    pose_eind = _punt(c, as_, r_k, R * POSE_LANG, pose) if pose > 0 else None
    rood_vlak = []
    if voorbij:
        stappen = max(1, int(math.ceil(pose - n)))
        rood_vlak = [_punt(c, as_, r_k, R, n + (pose - n) * i / stappen) for i in range(stappen + 1)]
    return {
        "getal": n, "tekst": f"{n}°", "centrum": c, "as": as_, "richting": r_k, "normaal": as_.cross(r_k),
        "boog": boog, "as_eind": _punt(c, as_, r_k, R, 0), "grens_eind": boog[-1],
        "label": _punt(c, as_, r_k, R * 1.22, n), "streepjes": streep, "omtrek": omtrek,
        "pose": pose, "pose_eind": pose_eind, "voorbij": voorbij, "rood_vlak": rood_vlak,
        "voorbij_tekst": f"+{max(1, int(round(pose - n)))}° past limit" if voorbij else None,
    }
