"""Twee kan-punten van de controleur bij eis 6 (te dichtbij), aangeroepen vanuit test_betaald.py.

Staven van 5 mm straal langs X in een mm-scene, speling 0,2, cursor als as-bron (scharnier: H = wereld-Y, L = X;
kogel: as = X, 3,0 mm, Auto uit), Exploded view uit (alles in echte coordinaten).

(a) Kogel naast scharnier, in beide volgordes. Eigen rekensom van de grens (los van de add-on):
    grens = reik scharnier + reik kogel, reik scharnier = max(t_vlak sin a, Rn, lip) + s (uit de opgeslagen maten),
    reik kogel = max(naad_r + 0,4 r, r + s), gemeten van snijpunt scharnier tot kogelmidden. De maten van kogel en
    scharnier komen van een eerst geplaatst gewricht op een losse staaf van dezelfde dikte. N = grens naar boven.
    Net onder de grens (grens - 0,2 mm): geweigerd met "Too close to another joint (keep N mm apart).", geen nieuwe
    objecten, de delen van het andere gewricht heel. Net boven (grens + 0,2 mm): geplaatst, twee gesloten delen.
(b) Drie scharnieren op één staaf: 1 op x = 0, 2 op deel B op x = 4 reik + 2 (ver van 1). Het middendeel draagt
    dan beide snijpunten (cj_scharnieren), het buitenste alleen dat van 2. Een derde op het middendeel bij 1, dus
    ver van het laatste snijpunt (2): op x = 0,5 "There is already a hinge here"; op 2 reik - 0,2 geweigerd met
    keep N (N = 2 reik naar boven, de oude code keek alleen naar 2 en liet hem toe); op 2 reik + 0,2 geplaatst,
    gesloten, en de twee nieuwe delen erven elk de juiste punten. Ook de oude enkele sleutels werken nog.
Alle maten in het log in mm, regels met [cj-betaald]."""
import math
import sys

import bpy
from mathutils import Vector

import figuren
from toetsen_teksten import vang

TOO_CLOSE = "Too close to another joint (keep {} mm apart)."
HIER = "There is already a hinge here."


def _reik_h(ob, u):
    """Eigen rekensom van de reik van een scharnier in mm uit de opgeslagen maten (zie de docstring)."""
    a = math.radians(float(ob["cj_wig_graden"]))
    s = float(ob["cj_speling_mm"]) * u
    return (max(float(ob["cj_t_vlak"]) * math.sin(a), float(ob["cj_naad_r"]), float(ob["cj_lip"])) + s) / u


def _reik_k(ob, u):
    r, naad, s = float(ob["cj_kogel_r"]), float(ob["cj_naad_r"]), float(ob["cj_speling_mm"]) * u
    return max(naad + 0.4 * r, r + s) / u


def _scharnier(x, bron, cursor):
    figuren.maak_actief(bron)
    cursor((x, 0, 0), Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)))
    try:
        return bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as fout:
        return {"FOUT: " + str(fout)}


def _kogel(x, bron):
    inst = bpy.context.scene.click_joints
    inst.soort, inst.kogel_mm, inst.kogel_auto = "KOGEL", 3.0, False
    figuren.zet_cursor((x, 0, 0), (1, 0, 0))
    figuren.maak_actief(bron)
    try:
        return bpy.ops.click_joints.plaats()
    except RuntimeError as fout:
        return {"FOUT: " + str(fout)}


def _poging(doe, bron):
    """(uitslag, nieuwe objecten, gevangen tekst)."""
    voor = {o.name for o in bpy.data.objects}
    if "cj_te_dicht_mm" in bron:
        del bron["cj_te_dicht_mm"]
    tekst = []
    with vang(tekst):
        uitslag = doe()
    return uitslag, [o for o in bpy.data.objects if o.name not in voor], tekst[0] if tekst else ""


def _heel(gesloten, obs):
    return all(o is not None and o.name in bpy.data.objects and gesloten.is_gesloten(o)[0] for o in obs)


def _xs(ob, afstand, u):
    return sorted(round(p.x / u, 3) for p, _r, _k in afstand.scharnieren(ob))


def toets(stap, eigen, cursor):
    eig = sys.modules[eigen + ".eigenschappen"]
    gesloten = sys.modules[eigen + ".gesloten"]
    afstand = sys.modules[eigen + ".betaald.afstand"]
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    inst = bpy.context.scene.click_joints
    inst.speling_mm, inst.as_bron, inst.uit_elkaar = 0.2, "CURSOR", False
    u = eig.eenheid_per_mm(bpy.context.scene)

    # Maten: scharnier op staaf s1 (x = 0), kogel op staaf s2 (cursor x = 0).
    s1 = figuren.staaf("s1", 5.0, lengte=120.0)
    uit_h = _scharnier(0.0, s1, cursor)
    s2 = figuren.staaf("s2", 5.0, lengte=120.0)
    uit_k = _kogel(0.0, s2)
    s1a, s1b = bpy.data.objects.get("s1_A"), bpy.data.objects.get("s1_B")
    s2a, s2b = bpy.data.objects.get("s2_A"), bpy.data.objects.get("s2_B")
    stap("afstand: scharnier en kogel op losse staven geplaatst", uit_h == {"FINISHED"} and uit_k == {"FINISHED"}
         and all((s1a, s1b, s2a, s2b)), f"{uit_h} {uit_k}")
    if not all((s1a, s1b, s2a, s2b)):
        return
    reik_h, reik_k = _reik_h(s1b, u), _reik_k(s2b, u)
    mz = Vector(s2b["cj_centrum"]).x / u  # kogelmidden voor de cursor langs de as
    grens = reik_h + reik_k
    n = math.ceil(grens - 1e-9)
    print(f"[cj-betaald] METING afstand: reik scharnier {reik_h:.3f} mm (cj_reik {float(s1b['cj_reik']) / u:.3f}), "
          f"reik kogel {reik_k:.3f} mm (r {float(s2b['cj_kogel_r']) / u:.3f}, naad_r {float(s2b['cj_naad_r']) / u:.3f}), "
          f"kogelmidden {mz:.3f} mm voor de cursor, grens {grens:.3f}, N {n}")
    # Binnen 0,01 mm: cj_wig_graden staat afgerond op 0,001 graad (run 42653795314: 10,349 tegen 10,348).
    stap("afstand: cj_reik gelijk aan de eigen rekensom (binnen 0,01 mm)", abs(float(s1b["cj_reik"]) / u - reik_h) < 0.01,
         f"{float(s1b['cj_reik']) / u:.4f} tegen {reik_h:.4f}")
    stap("afstand: deel van een scharnier draagt cj_scharnieren met zijn snijpunt", _xs(s1b, afstand, u) == [0.0]
         and _xs(s1a, afstand, u) == [0.0], f"{_xs(s1a, afstand, u)} {_xs(s1b, afstand, u)}")

    # (a1) Eerst scharnier, dan kogel op deel B (x > 0).
    for d, mag in ((grens - 0.2, False), (grens + 0.2, True)):
        uitslag, nieuw, tekst = _poging(lambda: _kogel(d - mz, s1b), s1b)
        delen = [o for o in nieuw if o.get("cj_deel")]
        print(f"[cj-betaald] METING afstand (a1) kogel op {d:.3f} mm van het scharnier: uitslag={uitslag}, "
              f"cj_te_dicht_mm={s1b.get('cj_te_dicht_mm')}, nieuw {sorted(o.name for o in nieuw)}")
        if not mag:
            stap(f"afstand (a1): kogel {d:.3f} mm van het scharnier (grens - 0,2) geweigerd met keep {n} mm",
                 uitslag == {"CANCELLED"} and s1b.get("cj_te_dicht_mm") == n and not nieuw,
                 f"kreeg {s1b.get('cj_te_dicht_mm')}, nieuw {len(nieuw)}")
            stap("afstand (a1): melding precies 'Too close ...'", f"Warning: {TOO_CLOSE.format(n)}" in tekst)
            stap("afstand (a1): beide delen van het scharnier heel", _heel(gesloten, (s1a, s1b)))
        else:
            stap(f"afstand (a1): kogel {d:.3f} mm van het scharnier (grens + 0,2) geplaatst, twee gesloten delen",
                 uitslag == {"FINISHED"} and len(delen) == 2 and _heel(gesloten, delen), str(uitslag))
            onder = next((o for o in delen if o["cj_deel"] == "A"), None)
            boven = next((o for o in delen if o["cj_deel"] == "B"), None)
            stap("afstand (a1): deel A van de kogel (kant van het scharnier) erft het scharnier, deel B niet",
                 onder is not None and boven is not None and _xs(onder, afstand, u) == [0.0]
                 and not afstand.scharnieren(boven),
                 f"A {onder and _xs(onder, afstand, u)} B {boven and _xs(boven, afstand, u)}")
            stap("afstand (a1): deel A van het scharnier heel", _heel(gesloten, (s1a,)))

    # (a2) Eerst kogel, dan scharnier op deel B van de kogel (komkant, x > kogelmidden).
    c = Vector(s2b["cj_centrum"]).x / u
    for d, mag in ((grens - 0.2, False), (grens + 0.2, True)):
        uitslag, nieuw, tekst = _poging(lambda: _scharnier(c + d, s2b, cursor), s2b)
        delen = [o for o in nieuw if o.get("cj_deel")]
        print(f"[cj-betaald] METING afstand (a2) scharnier op {d:.3f} mm van het kogelmidden: uitslag={uitslag}, "
              f"cj_te_dicht_mm={s2b.get('cj_te_dicht_mm')}, nieuw {sorted(o.name for o in nieuw)}")
        if not mag:
            stap(f"afstand (a2): scharnier {d:.3f} mm van de kogel (grens - 0,2) geweigerd met keep {n} mm",
                 uitslag == {"CANCELLED"} and s2b.get("cj_te_dicht_mm") == n and not nieuw,
                 f"kreeg {s2b.get('cj_te_dicht_mm')}, nieuw {len(nieuw)}")
            stap("afstand (a2): melding precies 'Too close ...'", f"Warning: {TOO_CLOSE.format(n)}" in tekst)
            stap("afstand (a2): beide delen van de kogel heel", _heel(gesloten, (s2a, s2b)))
        else:
            stap(f"afstand (a2): scharnier {d:.3f} mm van de kogel (grens + 0,2) geplaatst, twee gesloten delen",
                 uitslag == {"FINISHED"} and len(delen) == 2 and _heel(gesloten, delen), str(uitslag))
            stap("afstand (a2): deel A van de kogel heel", _heel(gesloten, (s2a,)))

    # (b) Drie scharnieren op een staaf.
    s3 = figuren.staaf("s3", 5.0, lengte=160.0)
    _scharnier(0.0, s3, cursor)
    s3b = bpy.data.objects.get("s3_B")
    if s3b is None:
        stap("afstand (b): eerste scharnier op s3", False)
        return
    reik = _reik_h(s3b, u)
    x2 = round(4 * reik + 2.0, 3)
    uitslag = _scharnier(x2, s3b, cursor)
    s3a, mid, buiten = (bpy.data.objects.get(k) for k in ("s3_A", "s3_B_A", "s3_B_B"))
    stap(f"afstand (b): tweede scharnier op {x2} mm geplaatst", uitslag == {"FINISHED"} and mid and buiten,
         str(uitslag))
    if mid is None or buiten is None:
        return
    print(f"[cj-betaald] METING afstand (b): reik {reik:.3f} mm, cj_scharnieren s3_A {_xs(s3a, afstand, u)}, "
          f"s3_B_A {_xs(mid, afstand, u)}, s3_B_B {_xs(buiten, afstand, u)}, cj_snijpunt middendeel "
          f"{Vector(mid['cj_snijpunt']).x / u:.3f}")
    stap("afstand (b): middendeel draagt beide snijpunten", _xs(mid, afstand, u) == [0.0, x2], str(_xs(mid, afstand, u)))
    stap("afstand (b): buitenste deel alleen het tweede", _xs(buiten, afstand, u) == [x2], str(_xs(buiten, afstand, u)))
    stap("afstand (b): oude enkele sleutel cj_snijpunt blijft (laatste scharnier)",
         abs(Vector(mid["cj_snijpunt"]).x / u - x2) < 1e-3, f"{Vector(mid['cj_snijpunt']).x / u:.6f}")  # cursor in float32
    oud = afstand.scharnieren({"cj_soort": "SCHARNIER", "cj_snijpunt": [1.0, 2.0, 3.0], "cj_reik": 4.0,
                               "cj_knokkel_r": 0.5})
    stap("afstand (b): deel met alleen de oude sleutels telt als een scharnier",
         len(oud) == 1 and tuple(oud[0][0]) == (1.0, 2.0, 3.0) and oud[0][1:] == (4.0, 0.5), str(oud))
    andere = (s3a, buiten)
    tellen = [len(o.data.vertices) for o in andere]
    # Op het eerste snijpunt (ver van het laatste): already here.
    uitslag, nieuw, tekst = _poging(lambda: _scharnier(0.5, mid, cursor), mid)
    stap("afstand (b): derde scharnier op 0,5 mm (bij het eerste, niet het laatste): 'already a hinge here'",
         uitslag == {"CANCELLED"} and not nieuw and HIER in tekst, f"{uitslag} nieuw {len(nieuw)}")
    n2 = math.ceil(2 * reik - 1e-9)
    for x3, mag in ((round(2 * reik - 0.2, 3), False), (round(2 * reik + 0.2, 3), True)):
        uitslag, nieuw, tekst = _poging(lambda: _scharnier(x3, mid, cursor), mid)
        delen = [o for o in nieuw if o.get("cj_deel")]
        print(f"[cj-betaald] METING afstand (b) derde scharnier op x={x3} mm (tot het tweede {x2 - x3:.3f} mm): "
              f"uitslag={uitslag}, cj_te_dicht_mm={mid.get('cj_te_dicht_mm')}, nieuw {sorted(o.name for o in nieuw)}")
        if not mag:
            stap(f"afstand (b): derde scharnier op {x3} mm (2 reik - 0,2 van het eerste) geweigerd met keep {n2} mm",
                 uitslag == {"CANCELLED"} and mid.get("cj_te_dicht_mm") == n2 and not nieuw,
                 f"kreeg {mid.get('cj_te_dicht_mm')}, nieuw {len(nieuw)}")
            stap("afstand (b): melding precies 'Too close ...'", f"Warning: {TOO_CLOSE.format(n2)}" in tekst)
        else:
            stap(f"afstand (b): derde scharnier op {x3} mm (2 reik + 0,2) geplaatst, twee gesloten delen",
                 uitslag == {"FINISHED"} and len(delen) == 2 and _heel(gesloten, delen), str(uitslag))
            a3 = next((o for o in delen if o["cj_deel"] == "A"), None)
            b3 = next((o for o in delen if o["cj_deel"] == "B"), None)
            if a3 is not None and b3 is not None:
                stap("afstand (b): nieuwe delen erven de juiste punten (A: eerste en derde, B: derde en tweede)",
                     _xs(a3, afstand, u) == [0.0, x3] and _xs(b3, afstand, u) == [x3, x2],
                     f"A {_xs(a3, afstand, u)} B {_xs(b3, afstand, u)}")
    stap("afstand (b): de andere delen (s3_A en het buitenste) heel en onveranderd",
         _heel(gesloten, andere) and [len(o.data.vertices) for o in andere] == tellen)
