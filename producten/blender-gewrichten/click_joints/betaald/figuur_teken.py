"""Pro 1.1: hoe een figuur in beeld staat (Daan, 16 nov ±13:50, plaatje 17).

- Een kogel van een figuur krijgt geen witte waaier van het gratis deel meer, maar een kleine groene wig in de
  passingkleur, symmetrisch om de lidas (van -N tot +N), met één getal `±N°`. N is het getal van het paneel
  ("Bends ±N°", de kleinste gemeten richting), dus nergens meer graden dan er zijn. De wig staat in het vlak dat
  het meest naar de kijker draait, zodat een heup van opzij geen witte streep langs het been meer is.
- Het getal van een kogel staat aan de buitenkant van het lid (weg van het midden van de figuur) en nooit binnen
  40 px (maal ui_scale) van een ander getal (Daan, moet 1). Het getal van een scharnier blijft waar het stond.
- Getallen van een figuur hebben een donkere rand van 1 px (Daan, kan), zodat ze los van het model staan.

Het gratis deel verandert niet: Pro omhult `waaier.teken_een` (zoals `uit_elkaar.afstand` in betaald/__init__.py)
en laat alles wat geen figuur is, of een figuurkogel met een pose, naar de oude tekenaar gaan."""
import math

import bpy
from mathutils import Vector

FIGUUR_X = 0.7      # zelfde verkleining als de scharnierboog bij een figuur
AFSTAND_PX = 40.0   # Daan: geen twee getallen binnen 40 px op 1920 van elkaar (gat tussen de tekstvakken)
PX = 16             # zelfde maat als het scharniergetal bij een figuur
_oud = [None]
laatst = {}         # bewijs voor de schermtest: wat de laatste tekenbeurt van de figuur tekende


def _mod(naam):
    import importlib
    return importlib.import_module(f"{__package__.rsplit('.', 1)[0]}.{naam}")


def kleur(ob):
    rgba = _mod("passing").KLEUREN.get(ob.get("cj_passing", "groen"), _mod("passing").KLEUREN["groen"])
    return tuple(rgba[:3])


def tekst_rand(punt, tekst, kleur_, px):
    """Tekst met een donkere rand van 1 px: acht keer donker 1 px verschoven, dan de tekst zelf."""
    import blf
    if punt is None:
        return False
    blf.size(0, px)
    breed, hoog = blf.dimensions(0, tekst)
    x0, y0 = punt.x - breed / 2.0, punt.y - hoog / 2.0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:
                blf.color(0, 0.05, 0.05, 0.05, 1.0)
                blf.position(0, x0 + dx, y0 + dy, 0)
                blf.draw(0, tekst)
    blf.color(0, kleur_[0], kleur_[1], kleur_[2], 1.0)
    blf.position(0, x0, y0, 0)
    blf.draw(0, tekst)
    return True


def vak(punt, tekst, px):
    import blf
    blf.size(0, px)
    breed, hoog = blf.dimensions(0, tekst)
    return (punt.x - breed / 2.0, punt.y - hoog / 2.0, punt.x + breed / 2.0, punt.y + hoog / 2.0)


def gat(v1, v2):
    """Kleinste afstand in pixels tussen twee tekstvakken (0 als ze overlappen)."""
    dx = max(0.0, max(v1[0], v2[0]) - min(v1[2], v2[2]))
    dy = max(0.0, max(v1[1], v2[1]) - min(v1[3], v2[3]))
    return math.hypot(dx, dy)


def _kijk(rv3d, c):
    inv = rv3d.view_matrix.inverted()
    if rv3d.is_perspective:
        k = c - inv.translation
    else:
        k = inv.to_3x3() @ Vector((0.0, 0.0, -1.0))
    return k.normalized() if k.length else Vector((0.0, 0.0, -1.0))


def kogel_vorm(a, b, rv3d):
    """Wig van de figuurkogel in wereldcoördinaten, of None (geen getal of rood)."""
    n = _mod("paneel").buig_graden(b)
    if n is None or a.get("cj_passing") == "rood":
        return None
    c = Vector(a["cj_centrum"])
    as_ = Vector(a["cj_as"]).normalized()
    # Kant van deel B: de wig wijst langs het lid naar B (zoals de waaier van het gratis deel).
    from ..uit_elkaar import echte_matrix, richtingen
    mb = echte_matrix(b)
    midden_b = sum((mb @ Vector(h) for h in b.bound_box), Vector()) / 8.0
    if (midden_b - c).dot(as_) < 0:
        as_ = -as_
    kijk = _kijk(rv3d, c)
    r_k = max(richtingen(as_), key=lambda r: abs(kijk.dot(as_.cross(r))))  # vlak zo veel mogelijk naar de kijker
    R = FIGUUR_X * _mod("gradenboog").STRAAL * float(a["cj_kogel_r"])

    def punt(g, r=R):
        t = math.radians(g)
        return c + r * (as_ * math.cos(t) + r_k * math.sin(t))
    return {"getal": n, "tekst": f"±{n}°", "centrum": c, "R": R, "as": as_, "normaal": as_.cross(r_k),
            "boog": [punt(g) for g in range(-n, n + 1)], "links": punt(-n), "rechts": punt(n), "as_eind": punt(0)}


def figuur_midden(scene, fig):
    """Midden van alle zichtbare delen van de figuur (bounding boxes, wereld): daar is 'binnen'."""
    pts = [o.matrix_world @ Vector(h) for o in scene.objects
           if o.get("cj_figuur") == fig and o.type == "MESH" and o.visible_get() for h in o.bound_box]
    return sum(pts, Vector()) / len(pts) if pts else None


def scharnier_getallen(context, regio, rv3d):
    """Vakken van de scharniergetallen van een figuur, op de plek waar scharnier_boog ze tekent."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d
    from . import scharnier_boog as sb
    from .. import waaier
    schaal = context.preferences.system.ui_scale
    if not getattr(context.window_manager, "cj_scharnier_boog", False):
        return []
    uit = []
    for b in context.scene.objects:
        if not (b.get("cj_soort") == "SCHARNIER" and b.get("cj_deel") == "B" and b.get("cj_figuur") and b.visible_get()):
            continue
        a, _ = sb.paar(context.scene, b)
        if a is None or "cj_bereik_graden" not in a or sb.beweeg.geen_stop(float(a["cj_bereik_graden"])):
            continue
        v = sb._klein(sb.vorm(a, b, float(b.get("cj_pose_graden", 0.0))), sb.FIGUUR_X)
        if waaier.kijkhoek(rv3d, v) < waaier.SCHUIN_MIN:
            continue
        p = naar2d(regio, rv3d, v["label"])
        if p is not None:
            uit.append(vak(p, f"{v['getal']}°", int(sb.FIGUUR_PX * schaal)))
    return uit


def kogel_plekken(context, regio, rv3d):
    """Plek van elk kogelgetal van een figuur in dit beeld: {naam deel B: (punt, vak)}.
    Begin aan de buitenkant van het lid (van het figuurmidden naar het kogelmidden, in beeld), net buiten de wig;
    zoek dan rondom en verder weg tot het vak minstens AFSTAND_PX van elk ander getal ligt en binnen het beeld valt."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d
    from .. import beweeg
    schaal = context.preferences.system.ui_scale
    px = int(PX * schaal)
    bezet = scharnier_getallen(context, regio, rv3d)
    plekken = {}
    kogels = []
    gezien = set()
    for b in context.scene.objects:
        if not (b.get("cj_deel") == "B" and b.get("cj_figuur") and "cj_buig_graden" in b and b.visible_get()):
            continue
        a = beweeg.paar(context.scene, b)
        if a is None:
            continue
        sleutel = tuple(round(x, 3) for x in a["cj_centrum"])
        if sleutel in gezien:  # één getal per kogel
            continue
        v = kogel_vorm(a, b, rv3d)
        if v is None:
            continue
        gezien.add(sleutel)
        kogels.append((b, v))
    for b, v in sorted(kogels, key=lambda t: t[0].name):
        c2 = naar2d(regio, rv3d, v["centrum"])
        if c2 is None:
            continue
        m = figuur_midden(context.scene, b.get("cj_figuur"))
        m2 = naar2d(regio, rv3d, m) if m is not None else None
        uit = (c2 - m2) if m2 is not None else Vector((0.0, 1.0))
        if uit.length < 1e-3:
            uit = Vector((0.0, 1.0))
        uit.normalize()
        r_px = max((naar2d(regio, rv3d, x) - c2).length for x in (v["links"], v["rechts"], v["as_eind"])
                   if naar2d(regio, rv3d, x) is not None) if c2 else 0.0
        gekozen = None
        for t in [r_px + 22.0 * schaal + 12.0 * schaal * i for i in range(30)]:
            for g in sorted(range(-165, 181, 15), key=abs):
                h = math.radians(g)
                d = Vector((uit.x * math.cos(h) - uit.y * math.sin(h), uit.x * math.sin(h) + uit.y * math.cos(h)))
                p = c2 + d * t
                vk = vak(p, v["tekst"], px)
                if vk[0] < 0 or vk[1] < 0 or vk[2] > regio.width or vk[3] > regio.height - 100.0 * schaal:
                    continue
                if all(gat(vk, o) >= AFSTAND_PX * schaal for o in bezet):
                    gekozen = (p, vk)
                    break
            if gekozen:
                break
        if gekozen is None:
            p = c2 + uit * (r_px + 22.0 * schaal)
            gekozen = (p, vak(p, v["tekst"], px))
        bezet.append(gekozen[1])
        plekken[b.name] = (gekozen[0], gekozen[1], v)
    return plekken


def teken_kogel(regio, rv3d, a, b, schaal):
    """Figuurkogel: kleine groene wig en één getal ±N° op een vrije plek buiten het lid."""
    import gpu
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d
    from .. import waaier
    context = bpy.context
    sleutel = (tuple(rv3d.view_matrix.col[3]), tuple(rv3d.view_matrix.col[2]), regio.width, regio.height,
               len(context.scene.objects))
    if laatst.get("sleutel") != sleutel or b.name not in laatst.get("plekken", {}):
        laatst["sleutel"] = sleutel
        laatst["plekken"] = kogel_plekken(context, regio, rv3d)
        laatst["getekend"] = {}
    plek = laatst["plekken"].get(b.name)
    if plek is None:  # dubbel deel van dezelfde kogel of geen getal: niets tekenen
        return None
    p_tekst, vk, v = plek
    KL = kleur(a)
    vlak = gpu.shader.from_builtin("UNIFORM_COLOR")
    dik = gpu.shader.from_builtin("POLYLINE_UNIFORM_COLOR")
    c2 = naar2d(regio, rv3d, v["centrum"])
    boog = [naar2d(regio, rv3d, x) for x in v["boog"]]
    waaier._waaiervlak(vlak, c2, boog, (*KL, 0.22))
    waaier._lijn(dik, regio, [c2, naar2d(regio, rv3d, v["as_eind"])], (*KL, 0.55), 2.0 * schaal)
    for x in ("links", "rechts"):
        waaier._lijn(dik, regio, [c2, naar2d(regio, rv3d, v[x])], (*KL, 0.9), 3.0 * schaal)
    waaier._lijn(dik, regio, boog, (*KL, 0.9), 3.0 * schaal)
    getal = tekst_rand(p_tekst, v["tekst"], KL, int(PX * schaal))
    uit = {"pose": round(float(b.get("cj_pose_graden", 0.0)), 3), "richting": int(b.get("cj_pose_richting", 0)),
           "getal": v["tekst"], "getal_getekend": getal, "streepjes": 0, "kijkhoek": 90.0, "omtrek": 0,
           "voorbij": False, "voorbij_tekst": None, "label_px": tuple(p_tekst), "figuur": True, "kleur": KL,
           "naam": b.get("cj_naam", ""), "vak": tuple(round(x, 1) for x in vk), "centrum_px": tuple(c2) if c2 else None}
    laatst["getekend"][b.name] = uit
    return uit


def _teken_een(regio, rv3d, a, b, schaal):
    if b.get("cj_figuur") and float(b.get("cj_pose_graden", 0.0)) <= 0.0:
        try:
            return teken_kogel(regio, rv3d, a, b, schaal)
        except Exception as fout:  # noqa: BLE001  tekenen mag Blender nooit laten vallen
            import traceback
            laatst["fout"] = traceback.format_exc()[-600:]
            print(f"Click Joints: figure ball not drawn ({fout})", flush=True)
            return None
    return _oud[0](regio, rv3d, a, b, schaal)


def register():
    from .. import waaier
    if _oud[0] is None:
        _oud[0] = waaier.teken_een
        waaier.teken_een = _teken_een


def unregister():
    from .. import waaier
    if _oud[0] is not None:
        if waaier.teken_een is _teken_een:
            waaier.teken_een = _oud[0]
        _oud[0] = None
    laatst.clear()
