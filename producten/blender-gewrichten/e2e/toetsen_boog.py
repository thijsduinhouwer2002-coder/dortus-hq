"""Toetsen voor de gradenboog (Daan, beoordeling 3, moet 1), zonder scherm, vanuit test_achtergrond.py.

De vorm staat in click_joints/gradenboog.py; het tekenen (pixels, streepjes, getal) toetst de schermtest.
Hier, met eigen rekenwerk naast de add-on:
- het getal op de boog is in elke richting het getal van het paneel: de gemeten grens in die richting,
  nooit meer dan stand en rekensom, naar beneden afgerond; bij een gelijk bereik gelijk aan "Bends ±N°";
- de boog eindigt op dat getal, ligt op straal 4 keer de kogelstraal, streepjes elke 5 graden;
- de gesloten lijn door de grenzen: 48 punten, op de richtingen precies de grens, ertussen lineair;
- pose: binnen de grens wit, voorbij de grens "+N° past limit" en een rood vlak van grens tot pose;
- bij rood geen boog. Alle hoeken in graden."""
import math

from mathutils import Vector

import figuren
from hulp import addon, log, plaats, stap, weg


def _hoek(v, c, as_):
    return math.degrees((v - c).angle(as_))


def eigen_getal(a, k):
    g = min(float(a["cj_hoek"]), float(a["cj_grens_graden"]), float(a["cj_buig_graden"][k]))
    return int(math.floor(g + 1e-6))


def vorm_toetsen(a, label):
    boog_m, paneel = addon("gradenboog"), addon("paneel")
    c, as_ = Vector(a["cj_centrum"]), Vector(a["cj_as"]).normalized()
    R = 4.0 * a["cj_kogel_r"]
    for k in range(8):
        v = boog_m.vorm(a, k, 0.0)
        n = eigen_getal(a, k)
        stap(f"BOOG {label} richting {k * 45}: getal {v['getal'] if v else None} gelijk aan eigen som {n} "
             f"en paneel {paneel.richting_graden(a, k)}", v is not None and v["getal"] == n == paneel.richting_graden(a, k))
        if v is None:
            continue
        stap(f"BOOG {label} richting {k * 45}: tekst {v['tekst']}", v["tekst"] == f"{n}°")
        eind = _hoek(v["grens_eind"], c, as_)
        stap(f"BOOG {label} richting {k * 45}: boog eindigt op {eind:.3f} graden (getal {n})", abs(eind - n) < 0.01)
        afstand = max(abs((p - c).length - R) for p in v["boog"])
        stap(f"BOOG {label} richting {k * 45}: boog op straal 4r (afwijking {afstand:.2e})", afstand < 1e-4 * R)
        hoeken = [g for g, _, _ in v["streepjes"]]
        stap(f"BOOG {label} richting {k * 45}: streepjes {hoeken}", hoeken == list(range(0, n + 1, 5)))
        vlak = max(abs((p - c).dot(v["normaal"].normalized())) for p in v["boog"] + [v["label"]])
        stap(f"BOOG {label} richting {k * 45}: boog en getal in het buigvlak ({vlak:.2e})", vlak < 1e-4 * R)
        stap(f"BOOG {label} richting {k * 45}: geen pose, geen pose-lijn", v["pose_eind"] is None and not v["voorbij"])
    # gesloten lijn: op elke richting (elk 6e punt) precies de grens met stand en rekensom als plafond
    v = boog_m.vorm(a, 0, 0.0)
    plafond = min(float(a["cj_hoek"]), float(a["cj_grens_graden"]))
    gr = [min(float(g), plafond) for g in a["cj_buig_graden"]]
    stap(f"BOOG {label}: gesloten lijn heeft 48 punten", len(v["omtrek"]) == 48)
    slecht = []
    for i, p in enumerate(v["omtrek"]):
        f, k = (i % 6) / 6.0, i // 6
        verwacht = gr[k] * (1 - f) + gr[(k + 1) % 8] * f
        if abs(_hoek(p, c, as_) - verwacht) > 0.01 or abs((p - c).length - R) > 1e-4 * R:
            slecht.append((i, round(_hoek(p, c, as_), 3), round(verwacht, 3)))
    stap(f"BOOG {label}: gesloten lijn door de grenzen, lineair ertussen (afwijkend: {slecht[:3]})", not slecht)


def pose_toetsen(a):
    boog_m = addon("gradenboog")
    c, as_ = Vector(a["cj_centrum"]), Vector(a["cj_as"]).normalized()
    n = eigen_getal(a, 0)
    grens = min(float(a["cj_hoek"]), float(a["cj_grens_graden"]), float(a["cj_buig_graden"][0]))
    binnen = boog_m.vorm(a, 0, float(n))
    stap(f"BOOG pose {n} (grens {grens:.2f}): wit, niet voorbij", binnen["pose_eind"] is not None and not binnen["voorbij"]
         and binnen["voorbij_tekst"] is None)
    half = boog_m.vorm(a, 0, n + 0.5)  # controleur ronde o: voorbij de boog van het getal is al rood
    stap(f"BOOG pose {n + 0.5}: voorbij de boog van {n} graden, tekst {half['voorbij_tekst']!r}",
         half["voorbij"] and half["voorbij_tekst"] == "+1\u00b0 past limit")
    pose = float(n + 5)
    voor = boog_m.vorm(a, 0, pose)
    stap(f"BOOG pose {pose:.0f}: voorbij, tekst {voor['voorbij_tekst']!r}",
         voor["voorbij"] and voor["voorbij_tekst"] == "+5° past limit")
    rv = voor["rood_vlak"]
    stap(f"BOOG pose {pose:.0f}: rood vlak van {_hoek(rv[0], c, as_):.2f} tot {_hoek(rv[-1], c, as_):.2f} graden",
         len(rv) >= 2 and abs(_hoek(rv[0], c, as_) - n) < 0.01 and abs(_hoek(rv[-1], c, as_) - pose) < 0.01)
    lijn = _hoek(voor["pose_eind"], c, as_)
    stap(f"BOOG pose {pose:.0f}: pose-lijn op {lijn:.2f} graden, langer dan de boog",
         abs(lijn - pose) < 0.01 and (voor["pose_eind"] - c).length > (voor["grens_eind"] - c).length)


def ongelijk(a):
    """Bereik dat per richting verschilt (zoals bij een schouder): elk getal volgt zijn eigen richting."""
    oud = list(a["cj_buig_graden"])
    plafond = min(float(a["cj_hoek"]), float(a["cj_grens_graden"]))  # onder het plafond, anders worden ze gelijk
    try:
        a["cj_buig_graden"] = [plafond - 9.6, oud[1], plafond - 3.2, oud[3], oud[4], plafond - 14.9, oud[6], oud[7]]
        vorm_toetsen(a, "ongelijk")
        getallen = [addon("gradenboog").vorm(a, k, 0.0)["getal"] for k in range(8)]
        log(f"BOOG ongelijk: bereik {[round(x, 2) for x in a['cj_buig_graden']]}, getallen {getallen}, "
            f"paneel Bends ±{addon('paneel').buig_graden(a)}")
        stap(f"BOOG ongelijk: getallen verschillen ({sorted(set(getallen))})", len(set(getallen)) >= 3)
        stap("BOOG ongelijk: paneel Bends is de kleinste boog", addon("paneel").buig_graden(a) == min(getallen))
    finally:
        a["cj_buig_graden"] = oud


def rood(a):
    oud = a.get("cj_passing")
    try:
        a["cj_passing"] = "rood"
        stap("BOOG rood: geen boog", addon("gradenboog").vorm(a, 0, 0.0) is None)
    finally:
        a["cj_passing"] = oud


def alles():
    st = figuren.staaf("staaf_boog", 5.0, lengte=40.0)
    lijst = plaats("BOOG staaf", st, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    stap("BOOG staaf: twee delen", len(lijst) == 2)
    if len(lijst) == 2:
        a = next(d for d in lijst if d["cj_deel"] == "A")
        log(f"BOOG staaf: stand {a.get('cj_hoek')}, rekensom {a.get('cj_grens_graden'):.2f}, "
            f"gemeten {[round(x, 2) for x in a['cj_buig_graden']]}")
        vorm_toetsen(a, "staaf")
        stap(f"BOOG staaf: gelijk bereik, elk getal is Bends ±{addon('paneel').buig_graden(a)}",
             all(addon("gradenboog").vorm(a, k, 0.0)["getal"] == addon("paneel").buig_graden(a) for k in range(8)))
        pose_toetsen(a)
        ongelijk(a)
        rood(a)
    weg(lijst)
    st.hide_set(True)
