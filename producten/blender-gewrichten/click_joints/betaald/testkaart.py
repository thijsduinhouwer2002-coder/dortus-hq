"""Fit test strip (Pro): vijf staafjes met elk één gewricht bij 0.10 tot 0.30 mm speling, getal in reliëf.

Ontwerp: platformen/blender-2/testkaart-ontwerp.md. De koper print ze alle vijf en neemt de speling van het
gewricht dat draait zonder te wiebelen. Alles komt in een eigen collectie "Fit test"; de instellingen van de
scene, de cursor en de selectie staan na afloop (ook na een fout) weer zoals ze waren."""
import bmesh
import bpy
from mathutils import Matrix, Vector

from ..eigenschappen import eenheid_per_mm
from ..gesloten import is_gesloten

SPELINGEN = (0.10, 0.15, 0.20, 0.25, 0.30)
LENGTE_MM = 60.0
STRAAL_MM = {"KOGEL": 10.0, "SCHARNIER": 7.0}
TUSSEN_MM = 10.0  # ruimte tussen twee staafjes
LETTER_MM = 3.6
RELIEF_MM = 0.6
IN_MM = 0.2  # het getal steekt zoveel in de staaf, zodat de union één stuk wordt
MAX_VER_MM = 1000.0  # verder dan 1 m achter de scene zetten we hem niet; dan gewoon bij de oorsprong
UITLEG = "Print all five. Use the clearance of the one that turns without wobble."
# Kleine schuif van de cursor tegen vlakken die precies samenvallen. Lukt de snede niet, dan nog een keer met de
# volgende: in 4.2.23 weigerde in een scene in meters soms één scharnier (19 nov, run 44576138702).
SCHUIVEN_MM = ((0.031, 0.137, 0.071), (0.083, -0.052, 0.113), (-0.047, 0.091, -0.129), (0.119, 0.023, -0.061))


def _staaf(naam, r, lengte, plek, collectie):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=96, radius1=r, radius2=r, depth=lengte,
                          matrix=Matrix.Translation((0, 0, lengte / 2)))
    me = bpy.data.meshes.new(naam)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(naam, me)
    ob.location = plek
    collectie.objects.link(ob)
    return ob


def _getal(tekst, u, midden, boven, collectie):
    """Mesh-object met het getal, liggend op z = boven, 0,6 mm hoog en 0,2 mm in de staaf."""
    cu = bpy.data.curves.new("cj_kaart_tekst", "FONT")
    cu.body = tekst
    cu.size = LETTER_MM * u
    cu.align_x, cu.align_y = "CENTER", "CENTER"
    cu.extrude = (RELIEF_MM + IN_MM) * u / 2
    cu.fill_mode = "BOTH"
    tijdelijk = bpy.data.objects.new("cj_kaart_tekst", cu)
    collectie.objects.link(tijdelijk)
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(tijdelijk.evaluated_get(dg))
    bpy.data.objects.remove(tijdelijk)
    bpy.data.curves.remove(cu)
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4 * u)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("cj_kaart_getal", me)
    hoogte = (RELIEF_MM + IN_MM) * u
    ob.location = Vector((midden.x, midden.y, boven - IN_MM * u + hoogte / 2))
    collectie.objects.link(ob)
    return ob


def _zet_getal(deel, tekst, u, collectie):
    """Union van het getal op de bovenkant van het deel, gerekend in een kopie in mm rond de oorsprong.
    Niet gesloten daarna = getal weg en False; het deel blijft heel."""
    pts = [Vector(h) for h in deel.bound_box]  # eigen coördinaten van het deel
    boven = max(p.z for p in pts)
    midden = sum(pts, Vector()) / len(pts)
    terug = Matrix.Translation(midden) @ Matrix.Scale(u, 4)  # werkkopie in mm rond de oorsprong
    werk_me = deel.data.copy()
    werk_me.transform(terug.inverted())
    werk = bpy.data.objects.new("cj_kaart_werk", werk_me)
    collectie.objects.link(werk)
    getal = _getal(tekst, 1.0, Vector((0.0, 0.0, 0.0)), (boven - midden.z) / u, collectie)
    m = werk.modifiers.new("cj_getal", "BOOLEAN")
    m.operation, m.object, m.solver = "UNION", getal, "EXACT"
    dg = bpy.context.evaluated_depsgraph_get()
    nieuw = bpy.data.meshes.new_from_object(werk.evaluated_get(dg))
    bpy.data.objects.remove(werk)
    bpy.data.objects.remove(getal)
    bpy.data.meshes.remove(werk_me)
    ok, _ = is_gesloten(nieuw)
    if ok and len(nieuw.vertices) > len(deel.data.vertices):
        nieuw.transform(terug)
        vorige = deel.data
        deel.data = nieuw
        nieuw.name = vorige.name
        bpy.data.meshes.remove(vorige)
        deel["cj_kaart_getal"] = tekst
        return True
    bpy.data.meshes.remove(nieuw)
    return False


def _snijd(context, inst, soort, staaf, plek, u, schuif, collectie):
    """Eén gewricht midden op de staaf. Geeft de twee delen, of [] als het niet lukte (staaf dan onaangeraakt)."""
    scene = context.scene
    scene.cursor.matrix = Matrix.Translation(plek + Vector((schuif[0] * u, schuif[1] * u,
                                                             LENGTE_MM * u / 2 + schuif[2] * u)))
    context.view_layer.update()
    for o in context.view_layer.objects:
        o.select_set(False)
    staaf.select_set(True)
    context.view_layer.objects.active = staaf
    try:
        if soort == "KOGEL":
            uit = bpy.ops.click_joints.plaats()
        else:
            uit = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError:
        uit = {"CANCELLED"}
    delen = [o for o in collectie.objects if o.get("cj_deel") and o.get("cj_bron") == staaf.name]
    if uit == {"FINISHED"} and len(delen) == 2:
        return delen
    for o in delen:
        bpy.data.objects.remove(o)
    return []


def _bezette_y(context):
    """Hoogste y van wat er al in de scene staat (meshes van de koper en eerdere Fit test-sets), of None."""
    ys = [(o.matrix_world @ Vector(h)).y for o in context.scene.objects if o.type == "MESH" and o.visible_get()
          for h in o.bound_box]
    return max(ys) if ys else None


class CLICK_JOINTS_OT_testkaart(bpy.types.Operator):
    bl_idname = "click_joints.testkaart"
    bl_label = "Fit test strip"
    bl_description = "Print this first: five joints from 0.10 to 0.30 mm clearance, each with its number on top"
    bl_options = {"REGISTER", "UNDO"}

    soort: bpy.props.EnumProperty(
        name="Joint", items=(("KOGEL", "Ball", "Five ball joints"), ("SCHARNIER", "Hinge", "Five hinges")),
        default="KOGEL")

    def execute(self, context):
        scene = context.scene
        inst = scene.click_joints
        u = eenheid_per_mm(scene)
        r = STRAAL_MM[self.soort] * u
        stap = 2 * r + TUSSEN_MM * u
        # Bij de oorsprong, achter alles wat er al staat. Niet bij de cursor: ver van de oorsprong in een scene in
        # meters ging het getal op het scharnier mis (19 nov, cursor op 3 m: 3 tot 19 open randen).
        begin = Vector((0.0, 0.0, 0.0))
        bezet = _bezette_y(context)
        if bezet is not None and bezet + r + TUSSEN_MM * u <= MAX_VER_MM * u:
            begin.y = max(0.0, bezet + r + TUSSEN_MM * u)
        collectie = bpy.data.collections.new("Fit test")
        scene.collection.children.link(collectie)
        # kogel_mm vóór kogel_auto: een nieuwe kogel_mm zet Auto uit (eigenschappen._handmatig).
        oud = {k: getattr(inst, k) for k in ("speling_mm", "soort", "kogel_mm", "kogel_auto", "as_bron", "uit_elkaar",
                                              "pose_graden") if hasattr(inst, k)}
        oud_cursor = scene.cursor.matrix.copy()
        oud_actief = context.view_layer.objects.active
        oud_kies = [o for o in context.view_layer.objects if o.select_get()]
        gelukt, zonder_getal, mis = 0, [], []
        try:
            inst.as_bron, inst.uit_elkaar = "CURSOR", False
            if hasattr(inst, "pose_graden"):
                inst.pose_graden = 0.0
            if self.soort == "KOGEL":
                inst.soort, inst.kogel_auto = "KOGEL", True
            for i, s in enumerate(SPELINGEN):
                tekst = f"{s:.2f}"
                plek = begin + Vector((i * stap, 0, 0))
                staaf = _staaf(f"Fit {tekst}", r, LENGTE_MM * u, plek, collectie)
                inst.speling_mm = s
                delen = []
                for schuif in SCHUIVEN_MM:
                    delen = _snijd(context, inst, self.soort, staaf, plek, u, schuif, collectie)
                    if delen:
                        break
                if not delen:
                    mis.append(tekst)
                    bpy.data.objects.remove(staaf)
                    continue
                bpy.data.objects.remove(staaf)  # de bron is van ons, niet van de koper: weg na de snede
                for o in delen:
                    o.name = f"Fit {tekst} {o['cj_deel']}"
                boven = max(delen, key=lambda o: max((o.matrix_world @ Vector(h)).z for h in o.bound_box))
                if not _zet_getal(boven, tekst, u, collectie):
                    zonder_getal.append(tekst)
                gelukt += 1
        finally:
            for k, v in oud.items():
                setattr(inst, k, v)
            scene.cursor.matrix = oud_cursor
            context.view_layer.update()
            for o in context.view_layer.objects:
                o.select_set(o in oud_kies)
            context.view_layer.objects.active = oud_actief
        if not gelukt:
            bpy.data.collections.remove(collectie)
            self.report({"ERROR"}, "The fit test strip could not be made")
            return {"CANCELLED"}
        extra = ""
        if mis:
            extra += f" Missing: {', '.join(mis)} mm."
        if zonder_getal:
            extra += f" No number on: {', '.join(zonder_getal)} mm."
        self.report({"WARNING"} if extra else {"INFO"}, UITLEG + extra)
        return {"FINISHED"}


def teken_knop(layout, context):
    """In stap 2 direct onder Clearance (1.2.9): de proefstrip zegt welke speling past, dus hij hoort bij die schuif."""
    vak = layout.column(align=True)
    vak.label(text="Not sure? Print a fit test first:")  # uitleg staat in de knoptip; past in een smalle zijbalk
    rij = vak.row(align=True)
    rij.operator(CLICK_JOINTS_OT_testkaart.bl_idname, text="Fit test: ball").soort = "KOGEL"
    rij.operator(CLICK_JOINTS_OT_testkaart.bl_idname, text="Fit test: hinge").soort = "SCHARNIER"


KLASSEN = (CLICK_JOINTS_OT_testkaart,)
