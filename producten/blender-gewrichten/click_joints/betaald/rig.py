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
    "SHOULDER": ("upper_arm", "upperarm", "arm", "upper arm"),
    "ELBOW": ("forearm", "lowerarm", "lower_arm", "fore_arm", "lower arm"),
    "HIP": ("thigh", "upleg", "upperleg", "upper_leg", "up_leg", "upper leg"),
    "KNEE": ("shin", "calf", "leg", "lowerleg", "lower_leg", "lower leg"),
    "ANKLE": ("foot",),
    "NECK": ("neck", "spine.004", "spine_004"),
}
VOORVOEGSELS = ("def-", "org-", "mch-", "mixamorig:", "mixamorig1:", "mixamorig2:", "bip01 ", "bip ")


def kant_en_kern(botnaam):
    """("L"/"R"/"", kern) uit een botnaam, bijvoorbeeld "mixamorig:LeftForeArm" -> ("L", "forearm")."""
    n = botnaam.strip().lower()
    for v in VOORVOEGSELS:
        if n.startswith(v):
            n = n[len(v):]
    kant = ""
    m = re.search(r"[._ ]([lr])(\.\d+)?$", n)
    if m:
        kant, n = m.group(1).upper(), n[:m.start()] + (m.group(2) or "")
    else:
        m = re.match(r"^(left|right)[_ .]?", n)
        if m:
            kant, n = ("L" if m.group(1) == "left" else "R"), n[m.end():]
    return kant, n.strip("._ ")


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


def schuif_uit_romp(straal_op, lengte, stap):
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
        if a is not None and b is not None and a <= grens and b <= grens:
            return t
        t += stap
    return 0.0


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
    """De cursor-matrix m van een kogel, met de oorsprong langs de lidas (kolom 2) uit de romp geschoven."""
    from .. import passing
    bvh = bvh_van(doel, context.evaluated_depsgraph_get())
    from ..eigenschappen import eenheid_per_mm
    u = eenheid_per_mm(context.scene)

    def straal_op(t):
        f = m.copy()
        f.col[3][:3] = m.to_translation() + m.col[2].to_3d().normalized() * t
        return passing.grootste_straal(bvh, f, (0.0,), n=24)

    t = schuif_uit_romp(straal_op, lengte, 0.5 * u)
    uit = m.copy()
    uit.col[3][:3] = m.to_translation() + m.col[2].to_3d().normalized() * t
    return uit, t / u


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
        for botnaam, sleutel, naam in lijst:
            pb = arm.pose.bones.get(botnaam)
            soort = figuur.PER_SLEUTEL[sleutel][2]
            stop = eindstop(grens_x(pb)) if soort == "HINGE" else None
            m = cursor_matrix(arm, pb, stop[1] if stop else 1)
            delen = [o for o in context.scene.objects if o.type == "MESH" and o.visible_get()
                     and (o is mesh or o.get("cj_figuur") == fig)]
            doel = deel_met(context, delen, m.to_translation())
            if doel is None:
                overgeslagen.append(f"{naam} (joint outside the mesh)")
                continue
            if soort != "HINGE":
                # Kogel: uit de romp schuiven (de botkop van dij en bovenarm ligt meestal in bekken of borst).
                lengte = ((arm.matrix_world @ pb.tail) - (arm.matrix_world @ pb.head)).length
                m, _mm = kogel_schuif(context, doel, m, lengte)
            for o in context.view_layer.objects:
                o.select_set(False)
            doel.select_set(True)
            context.view_layer.objects.active = doel
            cursor.rotation_mode = "QUATERNION"
            cursor.matrix = m
            ok, melding, _d = figuur.plaats_gewricht(context, sleutel, naam, stop[0] if stop else 0,
                                                     "from rig" if stop else "preset")
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
