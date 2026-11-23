"""Pro 1.1 stap 2b "Figure from rig" (ontwerp-1.1.md): de rig lezen en per gekozen bot het juiste gewricht.

Botnamen: Rigify (metarig en DEF-/ORG-), Mixamo (mixamorig:), en gewone namen (upper_arm, forearm, thigh, shin,
calf, ...). De kant komt uit .L/_L/.R/_R/Left/Right. Standaard alleen schouders, ellebogen, heupen, knieën en de
nek; enkels via "More bones".

Per bot (pose-matrix in wereld, dus een geposeerde figuur telt zoals hij staat):
- snijpunt op de botkop, lidas langs het bot (kop naar staart), dus deel B is het lid voorbij het gewricht;
- scharnier: as langs de X-as van het bot (in Blender draait een knie of elleboog om de X-as van het bot);
  bereik uit Limit Rotation (X) of de IK-grenzen (X) van het pose-bot: de grootste kant wordt de eindstop
  (afgerond, 30 tot 150), en de kant bepaalt de buigkant: draaien om +X brengt de staart naar +Z van het bot.
  Geen grens in de rig: het preset (135 of 90), label "preset".
- kogel: het bereik meet de kern zelf; de rig zegt hier niets over, dus altijd label "preset".
"""
import math
import re

from mathutils import Matrix, Vector

STANDAARD = ("SHOULDER", "ELBOW", "HIP", "KNEE", "NECK")
NAMEN = {"SHOULDER": "shoulder", "ELBOW": "elbow", "HIP": "hip", "KNEE": "knee", "ANKLE": "ankle", "NECK": "neck"}
# Kern van de botnaam (kleine letters, zonder kant en voorvoegsel) -> preset
KERNEN = {
    "SHOULDER": ("upper_arm", "upperarm", "arm", "upper arm", "shldrbend", "shldr"),
    "ELBOW": ("forearm", "lowerarm", "lower_arm", "fore_arm", "lower arm", "forearmbend"),
    "HIP": ("thigh", "upleg", "upperleg", "upper_leg", "up_leg", "upper leg", "thighbend"),
    "KNEE": ("shin", "calf", "leg", "lowerleg", "lower_leg", "lower leg"),
    "ANKLE": ("foot",),
    "NECK": ("neck", "spine.004", "spine_004", "neck_01", "neck01", "necktwist01", "neck1"),
}
VOORVOEGSELS = ("def-", "org-", "mch-", "mixamorig:", "mixamorig1:", "mixamorig2:", "bip01 ", "bip ",
                "cc_base_", "j_bip_")
# 16 nov run 13: ook Unreal (upperarm_l, calf_l, neck_01), Character Creator (CC_Base_L_Upperarm), VRoid
# (J_Bip_L_UpperArm), 3ds Max Biped (Bip01 L Thigh) en Daz (lShldrBend, lForearmBend, lThighBend, lShin).


def kant_en_kern(botnaam):
    """("L"/"R"/"", kern) uit een botnaam, bijvoorbeeld "mixamorig:LeftForeArm" -> ("L", "forearm")."""
    n = botnaam.strip().lower()
    # 17 nov run 25: Auto-Rig Pro (Lars, verhaal 26): "forearm_stretch.l", "c_leg_fk.r", "thigh_ref.l", "neck.x".
    # Kant .l/.r/.x achteraan, c_ vooraan alleen bij een ARP-achtervoegsel; twist-botten tellen niet (dubbel).
    m = re.match(r"^(c_)?([a-z]+?)(_stretch|_fk|_ref)?\.([lrx])$", n)
    if m and m.group(2) in _alle_kernen() and (m.group(3) or m.group(4) == "x" or not m.group(1)):
        return ("" if m.group(4) == "x" else m.group(4).upper()), m.group(2)
    for v in VOORVOEGSELS:
        if n.startswith(v):
            n = n[len(v):]
    kant = ""
    m = re.match(r"^([lrc])[._ ]", n)  # kant vooraan: "l_upperarm" (CC, VRoid), "l thigh" (Biped); c = midden
    if m:
        return ("" if m.group(1) == "c" else m.group(1).upper()), n[m.end():].strip("._ ")
    if n not in _alle_kernen() and len(n) > 1 and n[0] in "lr" and n[1:] in _alle_kernen():
        return n[0].upper(), n[1:]  # Daz: kant vast aan de naam ("lshin", "rthighbend")
    m = re.search(r"[._ ]([lr])(\.\d+)?$", n)
    if m:
        kant, n = m.group(1).upper(), n[:m.start()] + (m.group(2) or "")
    else:
        m = re.match(r"^(left|right)[_ .]?", n)
        if m:
            kant, n = ("L" if m.group(1) == "left" else "R"), n[m.end():]
    return kant, n.strip("._ ")


def _alle_kernen():
    return {k for kernen in KERNEN.values() for k in kernen}


def herken(botnaam):
    """(preset, "Left knee") of None als het bot geen bekend gewricht is."""
    kant, kern = kant_en_kern(botnaam)
    for sleutel, kernen in KERNEN.items():
        if kern in kernen:
            if sleutel != "NECK" and not kant:
                return None  # een arm of been zonder kant is geen gewricht dat we zeker herkennen
            woord = NAMEN[sleutel]
            naam = woord.capitalize() if not kant else f"{'Left' if kant == 'L' else 'Right'} {woord}"
            return sleutel, naam
    return None


def gewrichten(armature, meer=False):
    """Lijst [(botnaam, preset, naam)] in de volgorde van de botten, standaard alleen STANDAARD; één per naam."""
    uit, gezien = [], set()
    for bot in armature.data.bones:
        h = herken(bot.name)
        if h is None or (not meer and h[0] not in STANDAARD) or h[1] in gezien:
            continue
        # Rigify heeft dezelfde naam als DEF-, ORG- en metarig: de eerste met een vervormend bot gaat voor.
        gezien.add(h[1])
        uit.append((bot.name, h[0], h[1]))
    return uit


def grens_x(pose_bot):
    """(min, max) in graden om de X-as van het bot uit de rig, of None. Limit Rotation gaat voor de IK-grenzen."""
    for c in pose_bot.constraints:
        # Alleen in de eigen ruimte van het bot (LOCAL) is X de buigas; een grens in wereldruimte zegt dat niet.
        if (c.type == "LIMIT_ROTATION" and getattr(c, "use_limit_x", False) and not c.mute
                and getattr(c, "owner_space", "LOCAL") == "LOCAL"):
            return math.degrees(c.min_x), math.degrees(c.max_x)
    if getattr(pose_bot, "use_ik_limit_x", False):
        return math.degrees(pose_bot.ik_min_x), math.degrees(pose_bot.ik_max_x)
    return None


def eindstop(grens, lo=30, hi=150):
    """(graden, kant) uit (min, max): de grootste kant, afgerond en tussen lo en hi; kant +1 of -1. None zonder grens
    of als de grootste kant onder 5 graden ligt (dan zegt de rig niets bruikbaars)."""
    if grens is None:
        return None
    mn, mx = grens
    kant = 1 if mx >= -mn else -1
    g = mx if kant == 1 else -mn
    if g < 5.0:
        return None
    return int(min(hi, max(lo, round(g)))), kant


def ander_kant(naam):
    """"Left knee" -> "Right knee" en andersom; None zonder kant (nek)."""
    for a, b in (("Left ", "Right "), ("Right ", "Left ")):
        if naam.startswith(a):
            return b + naam[len(a):]
    return None


def spiegel_stops(stops):
    """Spiegelen (hoofdchat 16 nov, onderzoek Thijs): {naam: stop of None} -> {naam: (stop, herkomst)}.

    Heeft maar één kant een grens in de rig (veel rigs zetten Limit Rotation alleen links), dan neemt de andere
    kant hetzelfde bereik, met herkomst "mirrored" in plaats van "preset". Een eigen grens gaat altijd voor; heeft
    geen van beide kanten een grens, dan blijft het preset. Buigkant blijft gelijk: een gespiegelde rig (Rigify,
    Mixamo, X-Axis Mirror) buigt aan beide kanten om dezelfde lokale X."""
    uit = {}
    for naam, stop in stops.items():
        if stop is not None:
            uit[naam] = (stop, "from rig")
            continue
        ander = ander_kant(naam)
        if ander is not None and stops.get(ander) is not None:
            uit[naam] = (stops[ander], "mirrored")
        else:
            uit[naam] = (None, "preset")
    return uit


def cursor_matrix(armature, pose_bot, kant=1):
    """Matrix voor de 3D-cursor: oorsprong op de botkop, X = scharnieras, Y = buigkant, Z = lidas (rechtshandig).
    Draaien om +X van het bot brengt de staart naar +Z, dus bij kant +1 is de buigkant +Z en de as -X."""
    m = armature.matrix_world @ pose_bot.matrix
    bx = (m.to_3x3() @ Vector((1, 0, 0))).normalized()
    by = (m.to_3x3() @ Vector((0, 1, 0))).normalized()
    bz = (m.to_3x3() @ Vector((0, 0, 1))).normalized()
    h, buig = (-bx, bz) if kant == 1 else (bx, -bz)
    uit = Matrix.Identity(4)
    for i, v in enumerate((h, buig, by)):
        uit.col[i][:3] = v
    uit.col[3][:3] = m.to_translation()
    return uit


def schuif_uit_romp(straal_op, lengte, stap, naad_vrij=True):
    """Pro 1.1: hoe ver het snijvlak van een kogel langs het bot moet schuiven (vanaf de botkop) om uit de romp te
    komen. Riggers zetten de kop van dij en bovenarm in het bekken en de borst; een kogel daar krijgt een bolnaad zo
    groot als de romp (proef met armen: naad 31 mm in een been van 8 mm) en botst met alles. straal_op(t) geeft de
    grootste afstand van de botas tot de huid op t langs het bot (None buiten de mesh). Grens: 1,3 keer de kleinste
    straal op de eerste helft van het bot plus een stap. Geeft de eerste t waar het vlak en het kogelmidden (t + 0,84 keer de
    lidstraal, het midden ligt 1,4 r verder en r is 0,6 keer de lidstraal) allebei binnen de grens liggen; zoekt tot
    de helft van het bot, anders 0 (niets gevonden: dan zegt de kern zelf wat er misgaat)."""
    # Lidstraal: de kleinste gemeten straal op de eerste helft van het bot. Niet alleen halverwege: daar kan al de
    # sleuf van het scharnier verderop liggen (geen treffer; gezien op de Rigify-metarig, bovenarm van 29 mm).
    metingen = [straal_op(lengte * i / 20) for i in range(11)]
    metingen = [g for g in metingen if g is not None and g > 0]
    if not metingen:
        return 0.0
    lid = min(metingen)
    grens = 1.3 * lid + stap
    t = 0.0
    while t <= lengte / 2:
        a, b = straal_op(t), straal_op(t + 0.84 * lid)
        if a is not None and b is not None and a <= grens and b <= grens and (
                not naad_vrij or _naad_vrij(straal_op, t, lid, a, b, grens, stap)):
            return t
        t += stap
    return 0.0


def _naad_vrij(straal_op, t, lid, a, b, grens, stap):
    """Pro 1.1 (run 9): de bolnaad (straal: lidstraal plus marge, zie maat.zet_naad) mag niet in de romp steken.
    Anders laat `een_lid` de romp heel en houdt deel A een plat stuk romp binnen de naad, waar het lid na een paar
    graden tegenaan komt (toetsfiguur: heup ±14 in plaats van ±30, romp 7,5 mm boven het kogelmidden, naad 9,1).
    Toets twee punten terug vanaf het kogelmidden (richting botkop): halverwege en net voorbij de naad. Buiten de
    mesh (None) is vrij."""
    midden = t + 0.84 * lid
    naad = max(a, b) + 2 * stap  # 2 stappen = 1 mm: naadmarge 0,5 + speling 0,2 + halve speling + wat ruimte
    for terug in (0.5 * naad, naad + stap):
        if midden - terug < 0:
            continue  # voor de botkop: de kern meet daar zelf
        g = straal_op(midden - terug)
        if g is not None and g > grens:
            return False
    return True


def kogel_reden(sleutel, melding):
    """Pro 1.1 (run 16): een leesbare reden als een heup- of schouderkogel op geen enkele plek lukt en de kern alleen
    "too thin" of "nothing was cut" zegt. Gezien op AI-figuren van 150 mm (Meshy): de dijen raken elkaar tot vlak boven
    de knie en de dij is 35 tot 38 mm, korter dan kogel plus knie nodig hebben; een spleet tussen de benen hielp niet
    (proef run 16). Dan weet de koper waar hij moet bijsturen. Andere meldingen blijven zoals ze zijn."""
    if sleutel not in ("HIP", "SHOULDER", "NECK") or (melding or "nothing was cut") not in (
            "too thin here for a ball joint", "nothing was cut"):
        return melding
    if sleutel == "NECK":
        # 23 nov (Olaf, studio-figuren): "Neck (not placed)" zonder reden op 4 van 6 Quaternius-figuren (korte, dikke
        # nek in het hoofd, bot 14 mm op de knight).
        return "no clean spot for a neck ball (the neck is short or sits inside the head), place it by hand"
    if sleutel == "HIP":
        return "no clean spot for a hip ball on this thigh (legs touch or the thigh is short), place it by hand"
    return "no clean spot for a shoulder ball on this upper arm (arm touches the body or is short), place it by hand"


# ---------- Operator "Figure from rig" (bpy alleen hieronder, zodat de naamregels zonder Blender te toetsen zijn) ----------
import bpy  # noqa: E402
from bpy.props import BoolProperty  # noqa: E402
from mathutils.bvhtree import BVHTree  # noqa: E402


def zoek_armature(mesh):
    """De armature van de mesh: uit een Armature-modifier, anders de ouder."""
    for mod in getattr(mesh, "modifiers", []):
        if mod.type == "ARMATURE" and mod.object is not None:
            return mod.object
    p = mesh.parent
    return p if p is not None and p.type == "ARMATURE" else None


def _snijpunten(bvh, punt, richting):
    """Hoe vaak een straal vanuit het punt de huid kruist (oneven: binnen)."""
    n, start = 0, punt.copy()
    for _ in range(200):
        plek, _nrm, _i, _afst = bvh.ray_cast(start, richting)
        if plek is None:
            break
        n += 1
        start = plek + richting * 1e-4
    return n


def binnen(ob, punt, dg):
    """Ligt het punt (wereld) in de mesh? Dichtstbijzijnde punt op de huid en de richting van de normaal."""
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    try:
        mw = ob.matrix_world
        punten = [mw @ v.co for v in me.vertices]
        bvh = BVHTree.FromPolygons(punten, [tuple(p.vertices) for p in me.polygons])
    finally:
        ev.to_mesh_clear()
    plek, normaal, _i, afst = bvh.find_nearest(punt)
    if plek is None:
        return False, None
    return (punt - plek).dot(normaal) < 0, afst


def binnen_streng(ob, punt, dg):
    """Strengere versie voor het vangnet (run 17). Het teken van de normaal op het dichtstbijzijnde punt is willekeurig
    als dat punt op een rand of hoek van een boolean-naad ligt; in de CI (5.2.3) lag zo een punt van het onderbeen
    "binnen" de romp en weigerde de rechterheup op Rigify vals ("both arms"). Hier moet ook een straaltelling in drie
    scheve richtingen (oneven is binnen, meerderheid) het zeggen. Niet voor deel_met: op een Make watertight-kopie
    met overlappende schillen klopt de straaltelling niet (4.2.23, man_backpack: linkerknie viel weg)."""
    ok, _afst = binnen(ob, punt, dg)
    if not ok:
        return False
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    try:
        mw = ob.matrix_world
        bvh = BVHTree.FromPolygons([mw @ v.co for v in me.vertices], [tuple(p.vertices) for p in me.polygons])
    finally:
        ev.to_mesh_clear()
    richtingen = (Vector((0.5774, 0.5774, 0.5774)), Vector((-0.7071, 0.1, -0.7)).normalized(),
                  Vector((0.13, -0.98, 0.17)).normalized())
    return sum(_snijpunten(bvh, punt, r) % 2 for r in richtingen) >= 2


def bvh_van(ob, dg):
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    try:
        mw = ob.matrix_world
        return BVHTree.FromPolygons([mw @ v.co for v in me.vertices], [tuple(p.vertices) for p in me.polygons])
    finally:
        ev.to_mesh_clear()


def kogel_schuif(context, doel, m, lengte):
    """Kandidaten voor de cursor-matrix m van een kogel, met de oorsprong langs de lidas (kolom 2) uit de romp
    geschoven: eerst zo ver dat ook de bolnaad buiten de romp blijft (vol bereik), dan alleen vlak en kogelmidden
    buiten de romp (kleiner bereik, maar meer ruimte tot de knie). Lijst van (matrix, mm), zonder dubbele."""
    from .. import passing
    bvh = bvh_van(doel, context.evaluated_depsgraph_get())
    from ..eigenschappen import eenheid_per_mm
    u = eenheid_per_mm(context.scene)

    def straal_op(t):
        f = m.copy()
        f.col[3][:3] = m.to_translation() + m.col[2].to_3d().normalized() * t
        return passing.grootste_straal(bvh, f, (0.0,), n=24)

    t_vrij = schuif_uit_romp(straal_op, lengte, 0.5 * u, naad_vrij=True)
    t_oud = schuif_uit_romp(straal_op, lengte, 0.5 * u, naad_vrij=False)
    # Run 11: ook de plekken daartussen, per halve mm terug naar de romp. Op de Rigify-metarig is de plek met de
    # bolnaad vrij net te dicht bij de knie en botst de oude plek met de romp; ergens ertussen kan het passen.
    stappen = [t_vrij]
    t = t_vrij - 0.5 * u
    while t > t_oud + 1e-6 and len(stappen) < 8:
        stappen.append(t)
        t -= 0.5 * u
    stappen.append(t_oud)
    # 23 nov (Olaf, robot studio-2: lokaal 9 gewrichten, CI 8): dezelfde heupsnede gaf op een AMD-processor delen
    # die al in rust 1110 driehoeken overlappen ("blocked"), op een Intel-processor een gave heup (GEZIEN, run
    # 45206324187, meetregels DIAGMESH). De snede valt op zo'n plek per processor net anders uit. Als laatste
    # kandidaat daarom dezelfde plek 0,3 mm verder het lid in: komt alleen aan de beurt na een weigering, dus een
    # figuur waar het al lukte merkt niets.
    if t_vrij + 0.3 * u < 0.5 * lengte:
        stappen.append(t_vrij + 0.3 * u)
    uit = []
    for t in stappen:
        if any(abs(t / u - mm) < 1e-6 for _m, mm in uit):
            continue
        k = m.copy()
        o = m.to_translation() + m.col[2].to_3d().normalized() * t
        # Run 21 (17 nov): het kogelmidden in het midden van de doorsnede. Riggers zetten de heup en de schouder
        # vaak aan de rand van het lid (MakeHuman-mens 220 mm: dij 20,7 mm breed, maar het bot 2,8 mm van de
        # huid), en de automatische maat kiest dan een kogel van 2 tot 2,5 mm in een dij van 21 mm: hij past
        # (Good fit), maar breekt bij de eerste keer poseren.
        c = midden_doorsnede(bvh, o, k, u)
        k.col[3][:3] = c if c is not None else o
        uit.append((k, t / u))
    return uit


def midden_doorsnede(bvh, o, m, u):
    """Punt o in het midden van de doorsnede dwars op de lidas (kolom 2 van m): langs kolom 0 en 1 naar het midden
    tussen de twee huidtreffers, twee keer. None als een straal niets raakt of het punt buiten de mesh valt."""
    for _ in range(2):
        for kol in (0, 1):
            w = m.col[kol].to_3d().normalized()
            a, b = bvh.ray_cast(o, w), bvh.ray_cast(o, -w)
            if a[0] is None or b[0] is None:
                return None
            o = o + w * (a[3] - b[3]) / 2
    return o if _binnen_bvh(bvh, o) else None


def scharnier_plekken(context, doel, m, lengte):
    """Pro 1.1 (17 nov run 18): kandidaten voor een scharnier. Rigs zetten het bot van knie en elleboog vaak niet in
    het midden van het lid (MakeHuman-mens op 180 mm: elleboog 2,75 mm tot de voorkant en 6,55 tot de achterkant),
    en het scharnier meet de dikte als de kortste kant (scharnier_vorm.maten). Daarom eerst de botkop in het midden
    van de doorsnede (langs de scharnieras en de buigkant), dan dezelfde plek iets verder het onderste lid in (10 en
    20% van het bot), waar onderarm en scheen meestal dikker zijn. Lijst van (matrix, mm langs het lid)."""
    from ..eigenschappen import eenheid_per_mm
    bvh = bvh_van(doel, context.evaluated_depsgraph_get())
    u = eenheid_per_mm(context.scene)
    as_l = m.col[2].to_3d().normalized()
    uit = [(m, 0.0)]
    for f in (0.0, 0.1, 0.2):
        o = m.to_translation() + as_l * f * lengte
        for _ in range(2):  # twee keer: na de eerste schuif ligt het midden langs de andere as iets anders
            for kol in (0, 1):
                w = m.col[kol].to_3d().normalized()
                a, b = bvh.ray_cast(o, w), bvh.ray_cast(o, -w)
                if a[0] is None or b[0] is None:
                    break
                o = o + w * (a[3] - b[3]) / 2
        if not _binnen_bvh(bvh, o):
            continue
        k = m.copy()
        k.col[3][:3] = o
        if all((k.to_translation() - x.to_translation()).length > 0.2 * u for x, _mm in uit):
            uit.append((k, f * lengte / u))
    return uit


def gedraaid(m, voor=Vector((0, -1, 0))):
    """Pro 1.1 (22 nov, Chris: Quaternius-monsters): dezelfde plek met het scharnier 90 graden om de lidas gedraaid.
    Game-rigs in T-houding zetten de X-as van de onderarm vaak voor-achter, dan buigt de elleboog omhoog en haalt de
    snede een stuk van het hoofd weg (Yeti 150 mm: 16% van de punten kwijt, alles boven z 126 mm, GEZIEN). Gedraaid
    buigt hij horizontaal. Eerst de stand die naar voren buigt (Blender: voorkant is -Y), dan de andere. Rechtshandig:
    (h, buig, lid) naar (buig, -h, lid) of (-buig, h, lid)."""
    h, buig = m.col[0].to_3d(), m.col[1].to_3d()
    uit = []
    for nh, nb in ((buig, -h), (-buig, h)):
        k = m.copy()
        k.col[0][:3] = nh
        k.col[1][:3] = nb
        uit.append(k)
    uit.sort(key=lambda k: -k.col[1].to_3d().dot(voor))
    return uit


def _binnen_bvh(bvh, punt):
    richtingen = (Vector((0.5774, 0.5774, 0.5774)), Vector((-0.7071, 0.1, -0.7)).normalized(),
                  Vector((0.13, -0.98, 0.17)).normalized())
    return sum(_snijpunten(bvh, punt, r) % 2 for r in richtingen) >= 2


BUUR = {"shoulder": "elbow", "hip": "knee"}


def geen_ruimte(melding, naam, bot_mm):
    """Pro 1.1 (run 11): een eerlijke reden als een kogel "too close" krijgt omdat het bot te kort is. De kern zegt dan
    "keep 99 mm apart" (Rigify-metarig: bovenarm 29 mm, de bolnaad van een kogel in de borst is zo groot als de romp),
    en dat helpt een koper niet. Is de nodige afstand langer dan het bot, dan: geen plek op dit bot naast de elleboog
    of knie. Anders None (de oude melding blijft)."""
    import re
    m = re.search(r"too close to another joint, keep (\d+) mm apart", melding or "")
    # Run 16: ook als de afstand meer dan 0,8 keer het bot is. De kogel moet uit de romp (op AI-figuren pas na ±40%
    # van de dij), dus "keep 36 mm apart" op een dij van 38 mm past nooit (man_backpack, Meshy).
    if not m or int(m.group(1)) <= 0.8 * bot_mm:
        return None
    kern = naam.split()[-1].lower()
    buur = BUUR.get(kern, "next joint")
    return (f"no room on this {bot_mm:.0f} mm bone for a ball joint next to the {buur}, "
            f"place it by hand or give the {buur} a smaller range")


def kogel_vast(nieuw):
    """Pro 1.1 vangnet: True als een net geplaatste kogel volgens de beweegproef (vrijwel) niet kan bewegen
    (paneel "±0° (blocked)"). Zonder gemeten delen: False (dan beslist de rest, zoals voorheen)."""
    from .figuur import graden
    for d in nieuw or []:
        if d.get("cj_deel") in ("A", "B") and d.get("cj_soort", "KOGEL") == "KOGEL":
            _s, g = graden(d)
            return g is not None and g < 1.0
    return False


VERLOREN_MAX = 0.06  # grens van verloren_stuk, voor scharnier en (sinds 1.2.3) kogel
KOGEL_MIN_DEEL = 0.4  # kleinste kogel (diameter) als deel van de breedte van het lid bij de snede


def kogel_te_klein(nieuw, u):
    """Pro 1.1 (run 21): True als de automatische maat een kogel koos die veel kleiner is dan het lid (diameter onder
    0,4 keer de breedte bij de snede). Gezien op de MakeHuman-mens: kogel van 2,5 mm in een dij van 20,7 mm, Good
    fit volgens de wand, maar zo'n kogel breekt bij het poseren. Zonder gegevens: False."""
    for d in nieuw or []:
        if d.get("cj_deel") in ("A", "B") and d.get("cj_soort", "KOGEL") == "KOGEL":
            b, r = float(d.get("cj_breedte_mm", -1.0)), float(d.get("cj_kogel_r", 0.0)) / u
            return b > 0 and 2 * r < KOGEL_MIN_DEEL * b
    return False


def stukken(ob):
    """Aantal losse stukken (via gedeelde randen) van een mesh-object."""
    import bmesh
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    gezien, n = set(), 0
    for v in bm.verts:
        if v.index in gezien:
            continue
        n += 1
        rij = [v]
        gezien.add(v.index)
        while rij:
            w = rij.pop()
            for e in w.link_edges:
                o = e.other_vert(w)
                if o.index not in gezien:
                    gezien.add(o.index)
                    rij.append(o)
    bm.free()
    return n


def verloren_stuk(context, bron, nieuw, centrum, straal, n=400):
    """Pro 1.1 vangnet (17 nov run 19, Blender 4.2.23): na een gelukte scharniersnede kan een ver lid helemaal weg
    zijn (toetsfiguur met armen: de rechterscheen zat in geen enkel deel meer, daarna "joint outside the mesh").
    Neem tot n punten van de bron, 0,6 mm naar binnen geschoven; buiten een bol rond het gewricht moet elk punt in een
    van de nieuwe delen liggen. Geeft het deel van de punten dat nergens ligt (0.0 tot 1.0). Gemeten 17 nov: een
    verloren scheen 9 tot 12%; Make watertight-kopieën (knight_yellow) 3 tot 6% door binnenschillen die de UNION
    terecht weghaalt. Daarom de grens 6%."""
    from ..eigenschappen import eenheid_per_mm
    delen = [d for d in nieuw or [] if d.type == "MESH" and d.get("cj_deel") in ("A", "B")]
    if not delen or not bron.data.vertices:
        return 0.0
    dg = context.evaluated_depsgraph_get()
    bvhs = [bvh_van(d, dg) for d in delen]
    eigen = bvh_van(bron, dg)
    u = eenheid_per_mm(context.scene)
    mw, rot = bron.matrix_world, bron.matrix_world.to_3x3()
    vs = bron.data.vertices
    stap = max(1, len(vs) // n)
    geteld = mis = 0
    for v in list(vs)[::stap]:
        p = mw @ v.co - (rot @ v.normal).normalized() * 0.6 * u
        if (p - centrum).length < straal:
            continue
        plek, normaal, _i, _a = eigen.find_nearest(p)
        if plek is None or (p - plek).dot(normaal) >= 0:
            continue  # de toets zegt zelfs in de bron "buiten" (dunne stof, overlappende schillen): niet meetellen
        geteld += 1
        for bvh in bvhs:
            plek, normaal, _i, _a = bvh.find_nearest(p)
            if plek is not None and (p - plek).dot(normaal) < 0:
                break
        else:
            mis += 1
    return mis / geteld if geteld else 0.0


def kogel_fout(context, armature, naam, nieuw):
    """Pro 1.1 vangnet (run 14, echte Meshy-figuren): een kogel die meer dan zijn eigen lid meeneemt of een los stuk
    achterlaat is kapot, ook als de delen gesloten zijn. Gezien op knight_yellow: de heupkogel nam beide benen mee (de
    tuniek verbindt ze) en liet een blokje van 5 mm in het kruis achter. Geeft een melding, of None als het goed is.
    Meer dan zijn lid: deel B (het lid voorbij het gewricht) bevat de kop van een herkend bot van de andere kant."""
    delen = [d for d in nieuw or [] if d.get("cj_deel") in ("A", "B") and d.type == "MESH"]
    for d in delen:
        if stukken(d) > 1:
            return "the cut left a loose piece here, place it by hand"
    ander = ander_kant(naam)
    if not delen or ander is None:
        return None
    andere_kant = ander.split()[0]  # "Left" of "Right"
    dg = context.evaluated_depsgraph_get()
    # Het lid is het deel waar het eigen bot (op driekwart) in ligt, niet vast deel B: welke kant A of B heet hangt
    # aan de stand van de cursor, en in 5.2.3 was B bij de linkerheup de romp (run 15: vals "both arms").
    eigen = next((pb for pb in armature.pose.bones if (herken(pb.name) or (None, ""))[1] == naam), None)
    b = None
    if eigen is not None:
        mw = armature.matrix_world
        p = mw @ (eigen.head + 0.75 * (eigen.tail - eigen.head))
        b = next((d for d in delen if binnen_streng(d, p, dg)), None)
    if b is None:
        return None
    # Alleen botten van hetzelfde soort lid tellen (een heup kan geen arm meenemen; run 17 gaf vals "both arms").
    benen = ("HIP", "KNEE", "ANKLE")
    eigen_soort = (herken(eigen.name) or ("",))[0]
    for pb in armature.pose.bones:
        h = herken(pb.name)
        if h is None or not h[1].startswith(andere_kant + " "):
            continue
        if (h[0] in benen) != (eigen_soort in benen):
            continue
        if binnen_streng(b, armature.matrix_world @ pb.head, dg):
            limb = "legs" if h[0] in ("HIP", "KNEE", "ANKLE") else "arms"
            return f"the cut would take both {limb} (they touch here), place it by hand"
    return None


def draai_terug(context, bron, voor):
    """Haal alles weg wat de laatste snede maakte (objecten die niet in `voor` stonden) en zet de bron terug."""
    for ob in [o for o in bpy.data.objects if o.name not in voor]:
        me = ob.data if ob.type == "MESH" else None
        bpy.data.objects.remove(ob, do_unlink=True)
        if me is not None and me.users == 0:
            bpy.data.meshes.remove(me)
    bron.hide_set(False)
    bron.pop("cj_te_dicht_mm", None)
    bron.pop("cj_weigering", None)
    context.view_layer.update()


def kogels_van_figuur(scene, fig):
    """Alle zichtbare kogeldelen B van de figuur (elke kogel één keer)."""
    return [o for o in scene.objects if o.type == "MESH" and o.visible_get() and o.get("cj_figuur") == fig
            and o.get("cj_deel") == "B" and o.get("cj_soort", "KOGEL") == "KOGEL" and o.get("cj_buig_graden")]


def kogel_heel(context, fig, b, marge=0.5):
    """Pro 1.1 (run 21): meet de beweegproef van kogel b opnieuw tegen het deel waarin zijn midden nu ligt, en geef
    True als hij in geen richting meer dan `marge` graden verloor. Op een tijdelijke kopie, de echte delen houden hun
    getallen. Zonder deel om tegen te meten: True (niets veranderd aan zijn kant)."""
    from .. import beweeg
    from ..eigenschappen import eenheid_per_mm
    oud = list(b["cj_buig_graden"])
    c = Vector(b["cj_centrum"])
    context.view_layer.update()
    tegen = [o for o in context.scene.objects if o.type == "MESH" and o.visible_get() and o is not b
             and o.get("cj_figuur") == fig and _in_kader(o, c)]
    for o in tegen:
        kopie = o.copy()
        kopie.data = o.data.copy()
        context.scene.collection.objects.link(kopie)
        for k in ("cj_centrum", "cj_as", "cj_kogel_r", "cj_speling_mm", "cj_naad_r"):
            if k in b:
                kopie[k] = b[k]
        try:
            nieuw = beweeg.meet(kopie, b, b.get("cj_eenheid_per_mm", eenheid_per_mm(context.scene)))
        finally:
            me = kopie.data
            bpy.data.objects.remove(kopie, do_unlink=True)
            bpy.data.meshes.remove(me)
        b["cj_buig_graden"] = oud  # meet schrijft ook op b
        if any(n < g - marge for n, g in zip(nieuw, oud)):
            return False
    return True


def _in_kader(ob, punt):
    hoeken = [ob.matrix_world @ Vector(h) for h in ob.bound_box]
    return all(min(h[i] for h in hoeken) - 1e-4 <= punt[i] <= max(h[i] for h in hoeken) + 1e-4 for i in range(3))


def deel_met(context, kandidaten, punt):
    """Het deel van de figuur waar het punt in ligt (het diepste, als het in meer ligt), of None."""
    context.view_layer.update()  # kader van een net gesneden deel is anders nog oud
    dg = context.evaluated_depsgraph_get()
    beste = None
    for ob in kandidaten:
        if not _in_kader(ob, punt):
            # Run 18 (MakeHuman-mens, 220 mm): het teken van de normaal is op een naad soms vals; een ver deel (de
            # onderarm) "bevatte" zo de knie en won als diepste. Een punt buiten het kader van een deel ligt er nooit in.
            continue
        ok, afst = binnen(ob, punt, dg)
        if ok and (beste is None or afst > beste[1]):
            beste = (ob, afst)
    return None if beste is None else beste[0]


class CLICK_JOINTS_OT_figuur_uit_rig(bpy.types.Operator):
    bl_idname = "click_joints.figuur_uit_rig"
    bl_label = "Figure from rig"
    bl_description = ("Read the rig of this mesh and place the right joint on each main bone: ball joints for "
                      "shoulders, hips and neck, hinges with an end stop for elbows and knees")
    bl_options = {"REGISTER", "UNDO"}

    meer: BoolProperty(name="More bones", default=False, description="Also the ankles")

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob is not None and ob.type == "MESH"

    def execute(self, context):
        from . import figuur
        from ..eigenschappen import eenheid_per_mm
        mesh = context.active_object
        arm = zoek_armature(mesh)
        if arm is None:
            self.report({"WARNING"}, "No rig found: this mesh has no Armature modifier or armature parent.")
            return {"CANCELLED"}
        lijst = gewrichten(arm, self.meer)
        if not lijst:
            self.report({"WARNING"}, f"No shoulders, elbows, hips, knees or neck found in the bone names of {arm.name}.")
            return {"CANCELLED"}
        context.view_layer.update()  # pose-matrices pas na een evaluatie betrouwbaar
        # Scharnieren eerst (ellebogen, knieën, enkels), dan de kogels: het bereik uit de rig zit in de scharnieren.
        # Liggen een schouder en een elleboog te dicht bij elkaar, dan valt zo de kogel af en niet het bereik
        # (proef met armen 16 nov: andersom vielen beide ellebogen af). Binnen elke groep de volgorde van de rig.
        lijst = sorted(lijst, key=lambda x: figuur.PER_SLEUTEL[x[1]][2] != "HINGE")
        fig = figuur.figuur_naam(mesh)
        mesh["cj_figuur"] = fig
        cursor = context.scene.cursor
        oud_cursor = cursor.matrix.copy()
        gelukt, overgeslagen = [], []
        # Opruimen na afloop: alleen meshes die tijdens deze knop zijn ontstaan en door niets meer gebruikt
        # worden (17 nov run 25: 172 lege tussenmeshes bleven in het bestand). Oude data van de koper blijft.
        al_er = set(bpy.data.meshes[:])
        # Spiegelen: eerst alle grenzen lezen, dan krijgt een kant zonder grens die van de andere kant.
        stops = {naam: (eindstop(grens_x(arm.pose.bones.get(b))) if figuur.PER_SLEUTEL[k][2] == "HINGE" else None)
                 for b, k, naam in lijst}
        per_naam = spiegel_stops(stops)
        for botnaam, sleutel, naam in lijst:
            pb = arm.pose.bones.get(botnaam)
            soort = figuur.PER_SLEUTEL[sleutel][2]
            stop, herkomst = per_naam[naam]
            m = cursor_matrix(arm, pb, stop[1] if stop else 1)
            delen = [o for o in context.scene.objects if o.type == "MESH" and o.visible_get()
                     and (o is mesh or o.get("cj_figuur") == fig)]
            doel = deel_met(context, delen, m.to_translation())
            if doel is None:
                overgeslagen.append(f"{naam} (joint outside the mesh)")
                continue
            kandidaten = [(m, 0.0)]
            lengte = ((arm.matrix_world @ pb.tail) - (arm.matrix_world @ pb.head)).length
            if soort != "HINGE":
                # Kogel: uit de romp schuiven (de botkop van dij en bovenarm ligt meestal in bekken of borst).
                # Eerst met de hele bolnaad buiten de romp (vol bereik); is het daar te dicht bij de knie, dan de
                # oude plek (bereik kleiner, eerlijk in de lijst door de beweegproef).
                kandidaten = kogel_schuif(context, doel, m, lengte)
            else:
                kandidaten = scharnier_plekken(context, doel, m, lengte) or [(m, 0.0)]
                # Vangnet: lukt geen plek met de as uit de rig (de snede verliest een stuk), dan dezelfde plekken met
                # het scharnier gedraaid, alleen naar voren buigend, en met omhulsel H (een_lid_diep.ALTIJD_H), want
                # zonder H sneed de wig de voorkant van de romp weg. Nooit naar achteren: een elleboog die naar de rug
                # buigt is een kapot figuur (keuring Daan 22 nov). Komt alleen aan de beurt na een weigering, dus een
                # rig waar het al lukte merkt er niets van. Alleen de elleboog: een knie of enkel die zijwaarts buigt
                # is fout, die slaan we liever eerlijk over (keuring 86800a6, A5).
                if sleutel == "ELBOW":
                    eigen_n = len(kandidaten)
                    kandidaten = kandidaten + [(gedraaid(k)[0], mm) for k, mm in kandidaten]
            geblokkeerd, vangnet = False, None
            if soort != "HINGE" or sleutel != "ELBOW":
                eigen_n = len(kandidaten)
            from . import afstand, een_lid_diep
            andere, eerste = [], None
            for poging_kk in ((0, 1) if soort != "HINGE" else (0,)):
                if poging_kk == 1:
                    # Run 21: tweede poging zonder de kernregel kogel naast kogel. Die regel rekent met bollen en ziet
                    # niet dat twee heupen op twee benen zitten (MakeHuman-mens: heupen 33 mm uit elkaar, regel 34 mm).
                    # Alleen als de eerste poging op "too close" strandde, en daarna bewijzen: elke andere kogel van
                    # de figuur beweegt nog even ver (beweegproef opnieuw), anders terugdraaien.
                    if ok or "too close" not in (melding or "").lower():
                        break
                    andere = kogels_van_figuur(context.scene, fig)
                    if not andere:
                        break
                    eerste = (melding, vangnet, geblokkeerd)
                    afstand.kk_uit[0] = True
                for i, (m, _mm) in enumerate(kandidaten):
                    # Run 19 (CI 2569d26, 4.2.23): na een mislukte snede kan de lijst van de view layer in 4.2 nog een
                    # leeg plekje (None) hebben voor een weggehaald object; dat liet de knop vastlopen.
                    for o in [o for o in context.view_layer.objects if o is not None]:
                        o.select_set(False)
                    doel.select_set(True)
                    context.view_layer.objects.active = doel
                    cursor.rotation_mode = "QUATERNION"
                    cursor.matrix = m
                    voor = {o.name for o in bpy.data.objects}
                    een_lid_diep.ALTIJD_H[0] = i >= eigen_n
                    try:
                        ok, melding, nieuw = figuur.plaats_gewricht(context, sleutel, naam, stop[0] if stop else 0, herkomst)
                    finally:
                        een_lid_diep.ALTIJD_H[0] = False
                    if ok:
                        # Run 27: ook zonder H (een_lid) kan een snede een kruimel van 0,1 mm achterlaten, ver van het
                        # gewricht (MakeHuman-mens: 4 punten bij de rechterelleboog na de rechterschoudersnede). Zelfde
                        # opruimregel als na een snede met H (alleen dunne, kleine losse stukken), dan pas tellen.
                        from .snippers import ruim_snippers
                        for d in nieuw or []:
                            if d.type == "MESH" and d.get("cj_deel") in ("A", "B") and stukken(d) > 1:
                                d["cj_snippers"] = d.get("cj_snippers", 0) + ruim_snippers(d, eenheid_per_mm(context.scene))
                    if ok and soort != "HINGE" and kogel_vast(nieuw):
                        # Vangnet (16 nov run 11): een kogel die volgens de beweegproef niet beweegt is een kapot
                        # gewricht (gezien: Rigify-heup naast de knie). Snede terugdraaien, volgende plek proberen.
                        draai_terug(context, doel, voor)
                        ok, melding, geblokkeerd = False, None, True
                        continue
                    if ok and soort == "HINGE" and any(stukken(d) > 1 for d in nieuw or []
                                                       if d.get("cj_deel") in ("A", "B") and d.type == "MESH"):
                        # Run 17 (CI 4.2.23, knight_yellow): ook een scharnier kan losse stukken achterlaten; dan
                        # terugdraaien met eerlijke reden in plaats van een deel uit vier stukken.
                        fout = "the cut left a loose piece here, place it by hand"
                    elif ok and verloren_stuk(context, doel, nieuw, m.to_translation(),
                                              max(0.6 * lengte, 15 * eenheid_per_mm(context.scene))) > VERLOREN_MAX:
                        # 1.2.3 (keuring Betrouwbaarheid A, M1): ook bij een kogel, want die krijgt nu soms het voxel-
                        # omhulsel (omhulsel.py); verliest de snede meer dan 6% van het model, dan de volgende plek.
                        fout = "the cut lost part of the model here, place it by hand"
                    elif ok and soort != "HINGE" and kogel_te_klein(nieuw, eenheid_per_mm(context.scene)):
                        fout = "only a tiny ball fits here (the bone sits near the skin), place it by hand"
                    else:
                        fout = kogel_fout(context, arm, naam, nieuw) if ok and soort != "HINGE" else None
                    if fout:
                        draai_terug(context, doel, voor)
                        ok, melding, vangnet = False, fout, fout
                        continue
                    laag = (melding or "").lower()
                    # 23 nov (Olaf, studio-figuur: CI 8 gewrichten, lokaal 9): "no watertight parts" is vaak één
                    # slechte rand uit de booleaanse snede op een bijna platte driehoek, en die valt per machine net
                    # anders uit. Stoppen bij zo'n snede maakte de uitslag toeval; dus net als bij "too close" de
                    # volgende plek proberen. De mesh is dan nog onveranderd (gewricht.py zegt dat zelf).
                    # 1.2.3 (Betrouwbaarheid): in 4.2 (alleen Exact) gaf een scharniersnede soms delen die al in rust
                    # overlappen; de mesh is dan onveranderd, dus ook dan de volgende plek.
                    verder = ("too close" in laag or "no watertight parts" in laag or "overlap before they move" in laag
                              or (soort == "HINGE" and ("too thin" in laag or "tight" in laag)))
                    if ok or i == len(kandidaten) - 1 or not verder:
                        break
            afstand.kk_uit[0] = False
            if ok and eerste is not None:
                if not all(kogel_heel(context, fig, b) for b in andere if b.name in bpy.data.objects):
                    draai_terug(context, doel, voor)
                    ok = False
            if not ok and eerste is not None:
                melding, vangnet, geblokkeerd = eerste  # de reden van de eerste poging telt
            if not ok and vangnet:
                melding = vangnet  # de echte reden; latere plekken zeggen vaak alleen "nothing was cut"
            if not ok and soort != "HINGE":
                melding = geen_ruimte(melding, naam, lengte / eenheid_per_mm(context.scene)) or melding
            if not ok and not geblokkeerd:
                melding = kogel_reden(sleutel, melding)
            if not ok and geblokkeerd and not melding:
                melding = "no room for a ball joint that can move here (it would be blocked)"
            if ok:
                gelukt.append(naam)
            else:
                from .redenen import leesbaar  # 1.2.3: wat de koper kan doen als de snede zelf misging
                overgeslagen.append(f"{naam} ({leesbaar(melding) or 'not placed'})")
        cursor.matrix = oud_cursor
        alle = figuur.figuur_gewrichten(context.scene.objects, fig)
        tekst = figuur.samenvatting(alle) if alle else "No joints placed"
        # Een zichtbaar deel actief maken: de eerste met cj_deel kan een al weer gesneden, verborgen tussendeel zijn
        # (dan staan de knoppen grijs en is de lijst leeg; gezien op plaatje 16).
        mesh_of_deel = next((o for o in context.scene.objects if o.get("cj_figuur") == fig and o.get("cj_deel")
                             and o.visible_get()), None)
        # Ook op het ongesneden model als er niets lukte: anders waren de redenen nergens meer te lezen
        # (CI 4.2.23 run 44045946302, knight_yellow: "No joints placed" en een lege lijst).
        for o in context.scene.objects:
            if o.get("cj_figuur") == fig and (o.get("cj_deel") or o.type == "MESH"):
                o["cj_rig_overgeslagen"] = "; ".join(overgeslagen)
        if mesh_of_deel is not None:
            context.view_layer.objects.active = mesh_of_deel
        if gelukt:
            # Daan punt 1: na de knop de hele figuur met zijn bereiken in beeld (scharnierbogen en kogelwaaiers).
            context.scene.click_joints.toon_bereik = True
            if hasattr(context.window_manager, "cj_scharnier_boog"):
                context.window_manager.cj_scharnier_boog = True
        for m in [m for m in bpy.data.meshes if m not in al_er and m.users == 0]:
            bpy.data.meshes.remove(m)
        if overgeslagen:
            self.report({"WARNING"}, f"{tekst}. Skipped: {'; '.join(overgeslagen)}")
        else:
            self.report({"INFO"}, f"{tekst}.")
        return {"FINISHED"} if gelukt else {"CANCELLED"}


KLASSEN = (CLICK_JOINTS_OT_figuur_uit_rig,)
