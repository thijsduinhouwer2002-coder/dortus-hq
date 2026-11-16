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
    uit = []
    for t in stappen:
        if any(abs(t / u - mm) < 1e-6 for _m, mm in uit):
            continue
        k = m.copy()
        k.col[3][:3] = m.to_translation() + m.col[2].to_3d().normalized() * t
        uit.append((k, t / u))
    return uit


BUUR = {"shoulder": "elbow", "hip": "knee"}


def geen_ruimte(melding, naam, bot_mm):
    """Pro 1.1 (run 11): een eerlijke reden als een kogel "too close" krijgt omdat het bot te kort is. De kern zegt dan
    "keep 99 mm apart" (Rigify-metarig: bovenarm 29 mm, de bolnaad van een kogel in de borst is zo groot als de romp),
    en dat helpt een koper niet. Is de nodige afstand langer dan het bot, dan: geen plek op dit bot naast de elleboog
    of knie. Anders None (de oude melding blijft)."""
    import re
    m = re.search(r"too close to another joint, keep (\d+) mm apart", melding or "")
    if not m or int(m.group(1)) <= bot_mm:
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


def kogel_fout(context, armature, naam, nieuw):
    """Pro 1.1 vangnet (run 14, echte Meshy-figuren): een kogel die meer dan zijn eigen lid meeneemt of een los stuk
    achterlaat is kapot, ook als de delen gesloten zijn. Gezien op knight_yellow: de heupkogel nam beide benen mee (de
    tuniek verbindt ze) en liet een blokje van 5 mm in het kruis achter. Geeft een melding, of None als het goed is.
    Meer dan zijn lid: deel B (het lid voorbij het gewricht) bevat de kop van een herkend bot van de andere kant."""
    delen = [d for d in nieuw or [] if d.get("cj_deel") in ("A", "B") and d.type == "MESH"]
    for d in delen:
        if stukken(d) > 1:
            return "the cut left a loose piece here, place it by hand"
    b = next((d for d in delen if d.get("cj_deel") == "B"), None)
    ander = ander_kant(naam)
    if b is None or ander is None:
        return None
    andere_kant = ander.split()[0]  # "Left" of "Right"
    dg = context.evaluated_depsgraph_get()
    for pb in armature.pose.bones:
        h = herken(pb.name)
        if h is None or not h[1].startswith(andere_kant + " "):
            continue
        ok, _a = binnen(b, armature.matrix_world @ pb.head, dg)
        if ok:
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


def deel_met(context, kandidaten, punt):
    """Het deel van de figuur waar het punt in ligt (het diepste, als het in meer ligt), of None."""
    dg = context.evaluated_depsgraph_get()
    beste = None
    for ob in kandidaten:
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
            geblokkeerd, vangnet = False, None
            for i, (m, _mm) in enumerate(kandidaten):
                for o in context.view_layer.objects:
                    o.select_set(False)
                doel.select_set(True)
                context.view_layer.objects.active = doel
                cursor.rotation_mode = "QUATERNION"
                cursor.matrix = m
                voor = {o.name for o in bpy.data.objects}
                ok, melding, nieuw = figuur.plaats_gewricht(context, sleutel, naam, stop[0] if stop else 0, herkomst)
                if ok and soort != "HINGE" and kogel_vast(nieuw):
                    # Vangnet (16 nov run 11): een kogel die volgens de beweegproef niet beweegt is een kapot
                    # gewricht (gezien: Rigify-heup naast de knie). Snede terugdraaien, volgende plek proberen.
                    draai_terug(context, doel, voor)
                    ok, melding, geblokkeerd = False, None, True
                    continue
                fout = kogel_fout(context, arm, naam, nieuw) if ok and soort != "HINGE" else None
                if fout:
                    draai_terug(context, doel, voor)
                    ok, melding, vangnet = False, fout, fout
                    continue
                if ok or i == len(kandidaten) - 1 or "too close" not in (melding or "").lower():
                    break
            if not ok and vangnet:
                melding = vangnet  # de echte reden; latere plekken zeggen vaak alleen "nothing was cut"
            if not ok and soort != "HINGE":
                melding = geen_ruimte(melding, naam, lengte / eenheid_per_mm(context.scene)) or melding
            if not ok and geblokkeerd and not melding:
                melding = "no room for a ball joint that can move here (it would be blocked)"
            if ok:
                gelukt.append(naam)
            else:
                overgeslagen.append(f"{naam} ({melding or 'not placed'})")
        cursor.matrix = oud_cursor
        alle = figuur.figuur_gewrichten(context.scene.objects, fig)
        tekst = figuur.samenvatting(alle) if alle else "No joints placed"
        # Een zichtbaar deel actief maken: de eerste met cj_deel kan een al weer gesneden, verborgen tussendeel zijn
        # (dan staan de knoppen grijs en is de lijst leeg; gezien op plaatje 16).
        mesh_of_deel = next((o for o in context.scene.objects if o.get("cj_figuur") == fig and o.get("cj_deel")
                             and o.visible_get()), None)
        for o in context.scene.objects:
            if o.get("cj_figuur") == fig and o.get("cj_deel"):
                o["cj_rig_overgeslagen"] = "; ".join(overgeslagen)
        if mesh_of_deel is not None:
            context.view_layer.objects.active = mesh_of_deel
        if gelukt:
            # Daan punt 1: na de knop de hele figuur met zijn bereiken in beeld (scharnierbogen en kogelwaaiers).
            context.scene.click_joints.toon_bereik = True
            if hasattr(context.window_manager, "cj_scharnier_boog"):
                context.window_manager.cj_scharnier_boog = True
        if overgeslagen:
            self.report({"WARNING"}, f"{tekst}. Skipped: {'; '.join(overgeslagen)}")
        else:
            self.report({"INFO"}, f"{tekst}.")
        return {"FINISHED"} if gelukt else {"CANCELLED"}


KLASSEN = (CLICK_JOINTS_OT_figuur_uit_rig,)
