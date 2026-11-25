"""Gradenboog en pose-schuif van het scharnier (eis 8, ontwerp betaald v1.1, "Wat je ziet").

Zoals de gradenboog van de kogel (waaier.py en gradenboog.py van het gratis deel, die niet veranderen), maar
met één boog om de scharnieras H: van rechtdoor (0) tot de grens, de grens is het getal van het paneel
("Bends 0° to N°", gemeten, nooit meer dan de stand). Voorbij de grens een rood vlak, een rode pose-lijn en
"+N° past limit". Bovenaan het beeld staat dezelfde regel "Bends 0° to N°" als in het paneel.

De pose-schuif in het paneel draait deel B alleen in de weergave (scharnier_beweeg.pose) en kleurt voorbij de
stop de vlakken van A die B raken rood, net als de pose van de kogel. In achtergrondmodus geen handler."""
import math

import bpy
from mathutils import Vector

from . import scharnier_beweeg as beweeg
from .labels import figuur_x, label_tekst  # noqa: F401  (mooier overlay; ook gebruikt door figuur_teken)

WIT = (1.0, 1.0, 1.0)
ROOD = (1.0, 0x4D / 255.0, 0x4D / 255.0)  # zelfde rood als de kogelboog
STRAAL = 3.5        # keer de knokkelstraal: de kleinste straal
DIKTE_X = 2.1       # boogstraal minstens zoveel keer de halve dikte van het lid bij de knie (Daan, Pro punt 6: de boog
                    # buiten het deel, niet door de knokkel; de poster van ronde 1 had 15 mm op een been van 7,2 mm)
_dikte = {}         # (naam A, naam B, aantal hoekpunten) -> halve dikte; in de tekenbeurt mag niets op het object
STREEP = 5          # graden tussen twee streepjes
POSE_LANG = 1.15
ROOD_PX = 24        # "+N° past limit": groot genoeg voor een winkelplaatje (16 was te klein)
FIGUUR_PX = 22  # Daan 17 nov moet 4 (was 16)
_handler = [None]
laatst = {}  # wat de laatste tekenbeurt tekende, voor het bewijs in de schermtest


def grens(a):
    """Getal op de boog: zelfde als het paneel (beweeg.tekst), nooit meer dan de stand."""
    return min(int(round(float(a["cj_bereik_graden"]))), int(a["cj_stand"]))


def tekst(a):
    return beweeg.tekst(float(a["cj_bereik_graden"]), int(a["cj_stand"]))


def paar(scene, ob):
    """(A, B) van het scharnier waar ob bij hoort, of (None, None)."""
    if ob is None or ob.get("cj_soort") != "SCHARNIER":
        return None, None
    a = b = None
    for o in scene.objects:
        if o.get("cj_soort") == "SCHARNIER" and o.get("cj_bron") == ob.get("cj_bron") \
                and list(o.get("cj_snijpunt", [])) == list(ob.get("cj_snijpunt", [])):
            if o.get("cj_deel") == "A":
                a = o
            elif o.get("cj_deel") == "B":
                b = o
    return a, b


def dikte(a, b):
    """Halve dikte van het lid bij de knie in het buigvlak: de verste afstand langs de buigkant (beide kanten) tot het
    draaipunt van de hoekpunten van A en B binnen 5 knokkelstralen van het draaipunt langs de lidas, rechte stand.
    (2 knokkelstralen was te krap: daar is het lid rond de knokkel weggesneden, run 42794577017 gaf 4,2 mm op een been
    van ±6 mm.)"""
    sleutel = (a.name, b.name, len(a.data.vertices), len(b.data.vertices))
    if sleutel in _dikte:
        return _dikte[sleutel]
    import numpy as np
    from ..uit_elkaar import echte_matrix
    c = np.array(a["cj_scharnier_punt"], dtype=np.float64)
    lid = np.array(Vector(a["cj_as"]).normalized())
    buig = np.array(Vector(a["cj_buigkant"]).normalized())
    k = float(a["cj_knokkel_r"])
    best = k
    for ob in (a, b):
        n = len(ob.data.vertices)
        co = np.empty(n * 3, dtype=np.float64)
        ob.data.vertices.foreach_get("co", co)
        mw = np.array(echte_matrix(ob), dtype=np.float64)
        rel = co.reshape(n, 3) @ mw[:3, :3].T + mw[:3, 3] - c
        dicht = np.abs(rel @ lid) <= 5.0 * k
        if dicht.any():
            best = max(best, float(np.abs(rel[dicht] @ buig).max()))
    if b.get("cj_figuur"):
        best = _dikte_straal(a, b, c, lid, buig, k, best)
    _dikte[sleutel] = best
    return best


def _dikte_straal(a, b, c, lid, buig, k, plak):
    """Bij een figuur (run 20): de plak van 5 knokkelstralen loopt dwars door de romp als deel A het hele lijf is (een
    elleboog op een echte mens gaf een boog zo groot als de arm). Daarom hier de eigen huid van het lid: stralen vanaf
    de lidas langs plus en min de buigkant, op 1 tot 5 knokkelstralen langs de lidas, eerste raakpunt in A of B; de
    grootste daarvan. Lukt geen enkele straal, dan blijft de plak-maat."""
    import numpy as np
    from mathutils.bvhtree import BVHTree
    from ..uit_elkaar import echte_matrix
    bomen = []
    for ob in (a, b):
        mw = echte_matrix(ob)
        vs = [mw @ v.co for v in ob.data.vertices]
        bomen.append(BVHTree.FromPolygons(vs, [tuple(p.vertices) for p in ob.data.polygons]))
    C, L, U = Vector(c.tolist()), Vector(lid.tolist()), Vector(buig.tolist())
    best = None
    for f in (-5.0, -4.0, -3.0, -2.0, 2.0, 3.0, 4.0, 5.0):
        o = C + L * (f * k)
        for r in (U, -U):
            raak = [bm.ray_cast(o, r) for bm in bomen]
            d = [x[3] for x in raak if x[0] is not None]
            if d:
                best = max(best or 0.0, min(d))
    if best is None:
        return plak
    return float(np.clip(best, k, plak))


def straal(a, b):
    """Straal van de boog: buiten het lid (DIKTE_X keer de halve dikte), nooit kleiner dan STRAAL knokkelstralen."""
    return max(STRAAL * float(a["cj_knokkel_r"]), DIKTE_X * dikte(a, b))


def vorm(a, b, pose):
    """De boog in wereldcoördinaten. Beginrichting: de lidas naar de kant van B in rechte stand."""
    c = Vector(a["cj_scharnier_punt"])
    lid = Vector(a["cj_as"]).normalized()
    voor_as = lid.cross(Vector(a["cj_buigkant"])).normalized()
    # Middelpunt van B in rechte stand: de bounding box via de matrix zonder pose en Exploded view.
    from ..uit_elkaar import echte_matrix
    mb = echte_matrix(b)
    hoeken = [mb @ Vector(h) for h in b.bound_box]
    midden_b = sum(hoeken, Vector()) / 8.0
    d = lid if (midden_b - c).dot(lid) >= 0 else -lid
    zij = voor_as.cross(d)  # draaien om voor_as brengt d hierheen
    R = straal(a, b)

    def punt(g, r=R):
        t = math.radians(g)
        return c + r * (d * math.cos(t) + zij * math.sin(t))
    n = grens(a)
    voorbij = pose > n + 1e-6
    rood = []
    if voorbij:
        stappen = max(1, int(math.ceil(pose - n)))
        rood = [punt(n + (pose - n) * i / stappen) for i in range(stappen + 1)]
    return {
        "getal": n, "centrum": c, "normaal": voor_as, "boog": [punt(g) for g in range(n + 1)],
        "as_eind": punt(0), "grens_eind": punt(n), "label": punt(n, R * 1.25), "label_0": punt(0, R * 1.25),
        "streepjes": [(g, punt(g), punt(g, R * 1.1)) for g in range(0, n + 1, STREEP)],
        "pose_eind": punt(pose, R * POSE_LANG) if pose > 0 else None, "voorbij": voorbij, "rood_vlak": rood,
        "voorbij_tekst": f"+{max(1, int(round(pose - n)))}° past limit" if voorbij else None,
    }


def _omhulsel(punten):
    """Convexe omhullende in beeld (monotone keten), tegen de klok in."""
    p = sorted({(round(x.x, 2), round(x.y, 2)) for x in punten if x is not None})
    if len(p) < 3:
        return p

    def kruis(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    onder, boven = [], []
    for rij, uit in ((p, onder), (reversed(p), boven)):
        for x in rij:
            while len(uit) >= 2 and kruis(uit[-2], uit[-1], x) <= 0:
                uit.pop()
            uit.append(x)
    return onder[:-1] + boven[:-1]


def _binnen(hul, x, y):
    n = len(hul)
    return n >= 3 and all((hul[(i + 1) % n][0] - hul[i][0]) * (y - hul[i][1])
                          - (hul[(i + 1) % n][1] - hul[i][1]) * (x - hul[i][0]) >= 0 for i in range(n))


def _rood_plek(regio, rv3d, q, uit, delen, tekst_, px, schaal):
    """Plek van "+N° past limit". Zoals op de kogelboog (winkelplaatje 9) moet rood met donkere rand op de achtergrond
    staan: over een grijs deel is het slecht leesbaar. Kandidaten in ringen rond het eind van de pose-lijn, eerst
    dichtbij en in de richting van de lijn, dan verder en rondom; de eerste waarvan het tekstvak buiten de omhullende
    van A en B (hoekpunten van de bound box, in beeld) en binnen het beeld ligt wint. Alleen langs de pose-lijn zoeken
    (tot run 42668200920) vond bij een schuin scharnier niets vrij: de lijn wijst dan in deel B.
    Geeft (plek, vrij, (breed, hoog)); niets vrij: de oude plek (70 px verder langs de lijn)."""
    import blf
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d
    blf.size(0, px)
    breed, hoog = blf.dimensions(0, tekst_)
    hullen = [_omhulsel([naar2d(regio, rv3d, d.matrix_world @ Vector(h)) for h in d.bound_box]) for d in delen]
    rand = 8.0 * schaal
    hoeken = sorted(range(-180, 180, 15), key=abs)
    for t in [70.0 + 30.0 * i for i in range(40)]:
        for g in hoeken:
            r = math.radians(g)
            richting = Vector((uit.x * math.cos(r) - uit.y * math.sin(r), uit.x * math.sin(r) + uit.y * math.cos(r)))
            m = q["pose_eind"] + richting * (t * schaal)
            x0, x1, y0, y1 = m.x - breed / 2 - rand, m.x + breed / 2 + rand, m.y - hoog / 2 - rand, m.y + hoog / 2 + rand
            if x0 < 0 or y0 < 0 or x1 > regio.width or y1 > regio.height - 100.0 * schaal:
                continue
            proef = [(x, y) for x in (x0, m.x, x1) for y in (y0, m.y, y1)]
            if q["label"] is not None and (m - q["label"]).length < breed / 2 + 40.0 * schaal:
                continue
            if any(_binnen(h, x, y) for h in hullen for x, y in proef):
                continue
            if any(x0 <= hx <= x1 and y0 <= hy <= y1 for h in hullen for hx, hy in h):
                continue
            return m, True, (breed, hoog)
    return q["pose_eind"] + uit * (70.0 * schaal), False, (breed, hoog)


def _tot_vak(van, m, breed, hoog, rand):
    """Punt op de rand van het tekstvak (midden m) op de lijn van van naar m: daar stopt het verwijslijntje."""
    d = m - van
    if d.length == 0:
        return m
    sx = (breed / 2 + rand) / abs(d.x) if d.x else float("inf")
    sy = (hoog / 2 + rand) / abs(d.y) if d.y else float("inf")
    return m - d * min(1.0, sx, sy)


def figuur_kleur(a):
    """Kleur van de boog bij een figuur: de passingkleur van het gewricht. Een scharnier bestaat alleen bij
    Good fit (Tight geeft geen scharnier, eis 3), dus groen, zoals de ring rond de snede in de weergave."""
    from ..passing import KLEUREN
    rgba = KLEUREN.get(a.get("cj_passing", "groen"), KLEUREN["groen"])
    return tuple(rgba[:3])


def _klein(v, f):
    """De boog f keer zo groot om het middelpunt (bij een figuur: zes waaiers naast elkaar mogen niet overlappen)."""
    c = v["centrum"]

    def k(x):
        return c + (x - c) * f if x is not None else None
    w = dict(v)
    for sleutel in ("as_eind", "grens_eind", "label", "label_0", "pose_eind"):
        w[sleutel] = k(v[sleutel])
    w["boog"] = [k(x) for x in v["boog"]]
    w["rood_vlak"] = [k(x) for x in v["rood_vlak"]]
    w["streepjes"] = [(g, k(s0), k(s1)) for g, s0, s1 in v["streepjes"]]
    return w


def _teken_een(regio, rv3d, a, b, schaal, actief=True):
    import gpu
    from bpy_extras.view3d_utils import location_3d_to_region_2d as naar2d

    from .. import waaier  # alleen de tekenhulpjes lezen, het gratis deel verandert niet
    from . import labels
    pose = float(b.get("cj_pose_graden", 0.0))
    v = vorm(a, b, pose)
    fig = bool(b.get("cj_figuur"))
    KL = figuur_kleur(a) if fig else WIT
    if fig:
        v = _klein(v, figuur_x(bpy.context))

    def p(x):
        return naar2d(regio, rv3d, x) if x is not None else None
    q = {k: p(v[k]) for k in ("centrum", "as_eind", "grens_eind", "label", "pose_eind")}
    boog = [p(x) for x in v["boog"]]
    vlak = gpu.shader.from_builtin("UNIFORM_COLOR")
    dik = gpu.shader.from_builtin("POLYLINE_UNIFORM_COLOR")
    # Keuring 23 nov C4: in de stand Selected staat er maar één boog, dus die mag feller (was even bleek als bij All).
    sel = fig and labels.stand(bpy.context) == "SELECTED"
    waaier._waaiervlak(vlak, q["centrum"], boog, (*KL, 0.38 if sel else (0.22 if fig else 0.15)))
    waaier._lijn(dik, regio, [q["centrum"], q["as_eind"]], (*KL, 0.55), 2.0 * schaal)
    if fig:  # mooier overlay: donkere onderlijn, zodat de groene boog ook op een licht model los staat
        labels.onderlijn(regio, [q["centrum"], q["grens_eind"]], 7.0 * schaal)
        labels.onderlijn(regio, boog, 7.0 * schaal)
    waaier._lijn(dik, regio, [q["centrum"], q["grens_eind"]], (*KL, 1.0 if sel else 0.9), (4.0 if sel else 3.0) * schaal)
    waaier._lijn(dik, regio, boog, (*KL, 1.0 if sel else 0.9), (4.0 if sel else 3.0) * schaal)
    hoek = waaier.kijkhoek(rv3d, v)
    naam = fig and labels.met_naam(bpy.context, b)
    streep, getal, nul = [], False, False
    if hoek >= waaier.SCHUIN_MIN:
        if not fig:  # bij een figuur geen streepjes en geen 0°: klein houden, alleen het getal
            streep = waaier.streep_lijnen([(g, p(s0), p(s1)) for g, s0, s1 in v["streepjes"]], schaal)
            for _, s0, s1 in streep:
                waaier._lijn(dik, regio, [s0, s1], (*WIT, 0.9), 2.0 * schaal)
            # Ook 0° aan het begin (Daan, Pro punt 6): dan lees je de boog als "van 0° tot 115°".
            nul = waaier._tekst(0, p(v["label_0"]), "0°", WIT, int(20 * schaal))
        if fig:  # mooier overlay: label als donkere pil met een groen bolletje (was witte tekst met donkere rand);
            getal = q["label"] is not None  # getekend na de pose-lijn, zodat die er niet dwars doorheen loopt
        else:
            getal = waaier._tekst(0, q["label"], f"{v['getal']}°", KL, int(20 * schaal))
    rood_tekst, vrij = False, None
    if q["pose_eind"] is not None:
        if v["voorbij"]:
            waaier._waaiervlak(vlak, q["centrum"], [p(x) for x in v["rood_vlak"]], (*ROOD, 0.30))
        waaier._lijn(dik, regio, [q["centrum"], q["pose_eind"]], (*(ROOD if v["voorbij"] else WIT), 1.0),
                     4.0 * schaal)
        if v["voorbij"] and hoek >= waaier.SCHUIN_MIN:
            # Verder naar buiten dan het getal van de grens, anders liggen "115°" en "+3° past limit" over elkaar.
            uit = q["pose_eind"] - q["centrum"] if q["centrum"] is not None else Vector((0.0, 1.0))
            uit = uit.normalized() if uit.length > 0 else Vector((0.0, 1.0))
            groot = int(ROOD_PX * schaal)
            plek, vrij, (breed, hoog) = _rood_plek(regio, rv3d, q, uit, (a, b), v["voorbij_tekst"], groot, schaal)
            if vrij:  # dun rood lijntje van het eind van de pose-lijn naar de tekst op de vrije plek
                waaier._lijn(dik, regio, [q["pose_eind"], _tot_vak(q["pose_eind"], plek, breed, hoog, 6.0 * schaal)],
                             (*ROOD, 0.9), 2.0 * schaal)
            if fig:  # mooier overlay: bij een figuur een rode pil; een los scharnier houdt zijn gekeurde beeld (12, 14)
                rood_tekst = labels.pil(plek, v["voorbij_tekst"], groot, schaal, achter=labels.ROOD_ACHTER) is not None
            else:
                rood_tekst = waaier._tekst(0, plek, v["voorbij_tekst"], ROOD, groot)
    if fig and getal:
        getal = labels.pil(q["label"], label_tekst(b, v["getal"], naam), int(FIGUUR_PX * schaal), schaal,
                           accent=ROOD if v["voorbij"] else KL) is not None  # C4: bolletje rood voorbij de stop
    # De regel van het paneel ook in beeld (winkelschermen 11 en 12), bovenaan in het midden.
    # Bij een figuur alleen voor het actieve gewricht, anders staan zes regels over elkaar.
    kop = tekst(a)
    if fig and b.get("cj_naam"):  # bij een figuur met de naam erbij: "Left knee: bends 0° to 120°"
        kop = f"{b['cj_naam']}: {kop[:1].lower()}{kop[1:]}"
    if naam:  # stand Selected: de naam staat al in het label, geen kopregel dwars over het beeld
        actief = False
    kop_getekend = actief and waaier._tekst(0, Vector((regio.width / 2.0, regio.height - 60.0 * schaal)), kop,
                                            WIT, int(28 * schaal))
    return {"pose": round(pose, 3), "getal": f"{v['getal']}°", "getal_getekend": getal, "nul_getekend": nul,
            "straal": round((v["boog"][0] - v["centrum"]).length, 3),
            "streepjes": len(streep), "kijkhoek": round(hoek, 1), "voorbij": v["voorbij"],
            "voorbij_tekst": v["voorbij_tekst"] if rood_tekst else None,
            "kop": kop if kop_getekend else None, "rood_vrij": vrij, "figuur": fig, "kleur": KL,
            "naam": b.get("cj_naam", ""), "label_tekst": label_tekst(b, v["getal"], naam) if fig else None,
            "centrum_px": tuple(q["centrum"]) if q["centrum"] is not None else None,
            "label_px": tuple(q["label"]) if getal and q["label"] is not None else None}


def teken():
    import gpu
    context = bpy.context
    wm = context.window_manager
    if not getattr(wm, "cj_scharnier_boog", False):
        laatst.clear()
        laatst["bogen"] = []
        return
    regio, rv3d = context.region, context.region_data
    if regio is None or rv3d is None:
        return
    schaal = context.preferences.system.ui_scale
    gpu.state.blend_set("ALPHA")
    gpu.state.depth_test_set("NONE")
    getekend = []
    bs = [o for o in context.scene.objects
          if o.get("cj_soort") == "SCHARNIER" and o.get("cj_deel") == "B" and o.visible_get()]
    act = context.view_layer.objects.active
    from . import labels
    for b in bs:
        a, _ = paar(context.scene, b)
        if a is None or "cj_bereik_graden" not in a or beweeg.geen_stop(float(a["cj_bereik_graden"])):
            continue
        if not labels.toon(context, a, b):  # mooier overlay: bij een figuur alleen het gekozen gewricht
            continue
        # Kopregel: altijd bij een los scharnier (1.0), bij een figuur alleen voor het actieve deel.
        actief = not b.get("cj_figuur") or act is b  # bij een figuur: alleen als je het lid voorbij het gewricht kiest
        getekend.append(_teken_een(regio, rv3d, a, b, schaal, actief))
    gpu.state.blend_set("NONE")
    laatst.clear()
    laatst["bogen"] = getekend


def _veilig():
    try:
        teken()
    except Exception as fout:  # noqa: BLE001  tekenen mag Blender nooit laten vallen
        import traceback
        laatst["fout"] = traceback.format_exc()[-600:]
        print(f"Click Joints: hinge range not drawn ({fout})", flush=True)


def herteken(_wm=None, context=None):
    """Alle 3D-weergaven opnieuw tekenen (een eigenschap van de WindowManager doet dat zelf niet)."""
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                gebied.tag_redraw()


def _actief_paar():
    ctx = bpy.context
    ob = getattr(ctx, "active_object", None) or ctx.view_layer.objects.active
    return paar(ctx.scene, ob)


def _pose_lees(_wm):
    """De pose-schuif hoort bij het actieve scharnier: de stand staat op deel B (cj_pose_graden), dus elk scharnier
    houdt zijn eigen stand, ook na heropenen van het bestand (kan-punt controleur eis 8)."""
    try:
        _a, b = _actief_paar()
    except AttributeError:  # bpy.context zonder scene of view_layer (tijdens laden of registreren)
        return 0.0
    return float(b.get("cj_pose_graden", 0.0)) if b is not None else 0.0


def _pose_zet(_wm, waarde):
    from .. import kleur
    a, b = _actief_paar()
    if a is None or b is None:
        return
    beweeg.pose(a, b, float(waarde), kleur.materiaal("rood"))
    herteken()


def teken_paneel(layout, context):
    """In stap 3 van het paneel bij een actief scharnierdeel (1.2.9: naast de passing, niet los onder Export):
    "Bends 0° to N°", de boog aan of uit en de pose-schuif."""
    ob = context.active_object
    a, b = paar(context.scene, ob)
    if a is None or b is None or "cj_bereik_graden" not in a:
        return
    wm = context.window_manager
    vak = layout.column(align=True)
    # Daan #83 C2: stap 2 houdt Ball blauw (keuze voor het volgende gewricht), dus hier zeggen wat er al staat
    vak.label(text="Hinge placed", icon="CON_PIVOT")
    if beweeg.geen_stop(float(a["cj_bereik_graden"])):
        vak.label(text="No end stop found", icon="ERROR")
        return
    vak.label(text=tekst(a), icon="BLANK1")
    blok = vak.column(align=True)
    blok.prop(wm, "cj_scharnier_boog", icon="LIGHT_SPOT")
    blok.prop(wm, "cj_scharnier_pose", slider=True)


def _kern_paneel():
    """Module paneel.py van de kern waar dit Pro-deel in zit (zelfde pakket, één map hoger)."""
    from .. import paneel
    return paneel


def register():
    bpy.types.WindowManager.cj_scharnier_boog = bpy.props.BoolProperty(
        name="Show bend range", default=True, description="Draw the measured bend range of the hinge", update=herteken)
    bpy.types.WindowManager.cj_scharnier_pose = bpy.props.FloatProperty(
        name="Bend", default=0.0, min=0.0, max=150.0,
        description="Bend part B in the view only, to check the range. Past the end stop, touching faces turn red",
        get=_pose_lees, set=_pose_zet)
    kern = _kern_paneel()
    if kern is not None and teken_paneel not in kern.STAP3:
        kern.STAP3.append(teken_paneel)
    if not bpy.app.background and _handler[0] is None:
        _handler[0] = bpy.types.SpaceView3D.draw_handler_add(_veilig, (), "WINDOW", "POST_PIXEL")


def unregister():
    if _handler[0] is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_handler[0], "WINDOW")
        _handler[0] = None
    kern = _kern_paneel()
    if kern is not None and teken_paneel in kern.STAP3:
        kern.STAP3.remove(teken_paneel)
    for naam in ("cj_scharnier_pose", "cj_scharnier_boog"):
        if hasattr(bpy.types.WindowManager, naam):
            delattr(bpy.types.WindowManager, naam)
