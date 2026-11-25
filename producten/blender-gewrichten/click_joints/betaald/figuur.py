"""Figuurpresets van Pro 1.1 "Rig to Figure", stap 1 (ontwerp-1.1.md): zes vaste gewrichten zonder rig.

Een preset kiest alleen de soort en het bereik; het snijden zelf doen de bestaande operators (kogel uit de kern,
scharnier uit scharnier.py), dus de vorm, de pasband en de toetsen daarvan blijven gelijk.
- Shoulder, Hip, Neck: kogel (bereik gemeten door de kern, cj_grens_graden, "±N°").
- Elbow, Knee: scharnier met eindstop op 135°. Ankle: scharnier op 90°. Het getal in de lijst is het gemeten
  bereik uit de beweegproef (cj_bereik_graden), niet de stand, zodat we nooit meer graden tonen dan gemeten.

Elk deel krijgt een lijst `cj_gewrichten` (JSON) met alle gewrichten aan zijn kant, zoals cj_scharnieren:
naam, soort, graden en herkomst ("preset" nu, "from rig" in stap 2). Het paneel toont die lijst per figuur.
"""
import json

import bpy
from bpy.props import EnumProperty


# (sleutel, naam in het paneel, soort, stand van het scharnier of None); icoon: iconen/<sleutel>.png
PRESETS = (
    ("SHOULDER", "Shoulder", "BALL", None),
    ("ELBOW", "Elbow", "HINGE", 135),
    ("HIP", "Hip", "BALL", None),
    ("KNEE", "Knee", "HINGE", 135),
    ("ANKLE", "Ankle", "HINGE", 90),
    ("NECK", "Neck", "BALL", None),
)
PER_SLEUTEL = {p[0]: p for p in PRESETS}
KEUZES = [(p[0], p[1], f"{p[1]}: {'ball joint' if p[2] == 'BALL' else f'hinge with an end stop at {p[3]}°'}")
          for p in PRESETS]
SOORT_TEKST = {"BALL": "Ball", "HINGE": "Hinge"}
_iconen = [None]


def icoon(sleutel):
    """icon_value van het kleine lichaamsdeel-icoon, of 0 (dan zonder icoon) als het niet te laden is."""
    pv = _iconen[0]
    if pv is None or sleutel.lower() not in pv:
        return 0
    return pv[sleutel.lower()].icon_id


def lees(ob):
    """Lijst met gewrichten op een deel (leeg als er geen is of de tekst kapot is)."""
    try:
        return list(json.loads(ob.get("cj_gewrichten", "[]")))
    except (TypeError, ValueError):
        return []


def graden(deel):
    """Gemeten bereik van het laatste gewricht op dit deel: (soort, graden) of (soort, None)."""
    if deel.get("cj_soort") == "SCHARNIER":
        g = deel.get("cj_bereik_graden")
        return "HINGE", (None if g is None else round(float(g), 1))
    # Het getal van het paneel ("Bends ±N°"): ook de beweegproef telt, nooit meer graden dan gemeten (16 nov:
    # de lijst zei ±30° bij een heup die volgens de beweegproef 0° kon).
    from ..paneel import buig_graden
    n = buig_graden(deel)
    if n is not None:
        return "BALL", float(n)
    g = deel.get("cj_grens_graden", -1.0)
    return "BALL", (round(float(g), 1) if g is not None and g >= 0 else None)


def bereik_tekst(soort, g):
    if g is None:
        return "range not measured"
    if soort == "BALL" and g < 1.0:
        return "±0° (blocked)"
    return f"0–{g:.0f}°" if soort == "HINGE" else f"±{g:.0f}°"


def regel(rec):
    """Eén regel in het paneel: "Knee · Hinge · 0–135° · preset"."""
    # Daan moet 5 (17 nov): "mirrored" liep af achter "Right elbow · Hinge · 0–140°"; in de regel "mirror".
    herkomst = rec.get("herkomst", "preset")
    return " · ".join((rec["naam"], SOORT_TEKST.get(rec["soort"], rec["soort"]),
                            bereik_tekst(rec["soort"], rec.get("graden")), "mirror" if herkomst == "mirrored" else herkomst))


def figuur_naam(ob):
    """Vaste naam van de figuur: cj_bron wisselt bij elke snede (het gesneden deel), cj_figuur niet."""
    if "cj_figuur" in ob:
        return ob["cj_figuur"]
    return ob.get("cj_bron", ob.name) if ob.get("cj_deel") else ob.name


def figuur_gewrichten(objecten, figuur):
    """Alle gewrichten van één figuur (cj_figuur), elk één keer (op snijpunt), in volgorde van plaatsen."""
    gezien, uit = set(), []
    for ob in objecten:
        if ob.get("cj_figuur") != figuur:
            continue
        for rec in lees(ob):
            sleutel = tuple(round(c, 3) for c in rec.get("punt", ()))
            if sleutel not in gezien:
                gezien.add(sleutel)
                uit.append(rec)
    return sorted(uit, key=lambda r: r.get("nr", 0))


def samenvatting(lijst):
    """Korte regel bovenaan: "3 joints" of "6 joints · 4 from rig · 1 mirrored". Kort (Daan moet 5, 17 nov): de
    lange vorm "7 joints, 4 ranges from your rig (2 mirrored)" liep in de zijbalk af."""
    # Daan 18 nov moet 1 (plaatje 19): teller en lijst gelijk. Eerst telde "from rig" de gespiegelde mee
    # ("9 joints · 4 from rig · 2 mirrored" naast 2 + 2 + 5 in de lijst). Nu elk woord zoals in de lijst, elk lid
    # één keer: "9 joints · 2 rig · 2 mirror · 5 preset". Kort gehouden: 38 tekens past in de zijbalk.
    n = len(lijst)
    rig = sum(1 for r in lijst if r.get("herkomst") == "from rig")
    sp = sum(1 for r in lijst if r.get("herkomst") == "mirrored")
    pre = n - rig - sp
    kop = f"{n} joint" + ("" if n == 1 else "s")
    if not (rig or sp):
        return kop
    return kop + f" · {rig} rig" + (f" · {sp} mirror" if sp else "") + (f" · {pre} preset" if pre else "")


def _snij(context, soort, stand, graden_vrij=0):
    inst = context.scene.click_joints
    if soort == "HINGE":
        flip = bool(getattr(context.window_manager, "cj_flip_bend", False)) if not graden_vrij else False
        return bpy.ops.click_joints.plaats_scharnier(stand=str(stand), flip_bend=flip, graden=int(graden_vrij))
    oud_soort = inst.soort
    inst.soort = "KOGEL"
    try:
        return bpy.ops.click_joints.plaats()
    finally:
        if inst.soort != oud_soort:
            inst.soort = oud_soort


def plaats_gewricht(context, sleutel, naam=None, graden_vrij=0, herkomst="preset"):
    """Snijdt het actieve object op de 3D-cursor met het gewricht van dit preset en schrijft het record.

    graden_vrij > 0: eindstop van het scharnier op dat getal (stap 2, uit de rig). Geeft (ok, melding, delen);
    bij een weigering is de melding die van de onderliggende operator (die stond al in de statusbalk) of None."""
    _s, preset_naam, soort, stand = PER_SLEUTEL[sleutel]
    naam = naam or preset_naam
    bron = context.active_object
    oude = lees(bron)
    fig = figuur_naam(bron)
    voor = {o.name for o in bpy.data.objects}
    bron.pop("cj_te_dicht_mm", None)
    bron.pop("cj_weigering", None)
    try:
        uitslag = _snij(context, soort, stand, graden_vrij)
    except RuntimeError as e:  # een ERROR-melding van de onderliggende operator komt hier als fout binnen
        return False, str(e).replace("Error: ", "").strip(), []
    if "FINISHED" not in uitslag:
        if "cj_te_dicht_mm" in bron:
            return False, f"too close to another joint, keep {bron['cj_te_dicht_mm']} mm apart", []
        if bron.get("cj_weigering"):  # de reden van het scharnier (bijvoorbeeld Tight), in plaats van "not placed"
            return False, str(bron.pop("cj_weigering")).rstrip(". "), []
        return False, None, []
    nieuw = [o for o in bpy.data.objects if o.name not in voor and o.get("cj_deel") in ("A", "B")]
    if not nieuw:
        # De kogel geeft FINISHED met alleen een rood draadteken als het te dun is (niets gesneden).
        dun = any(o.name not in voor and o.name.endswith("_joint_too_thin") for o in bpy.data.objects)
        return False, ("too thin here for a ball joint" if dun else "nothing was cut"), []
    if len(nieuw) != 2:
        return True, f"{naam}: joint placed, but its parts were not found for the joint list.", nieuw
    from . import figuur_ring
    from ..eigenschappen import eenheid_per_mm
    figuur_ring.smal_paar(nieuw, eenheid_per_mm(context.scene))  # Daan 17 nov moet 4: groene ring van een kogel alleen rond het lid, niet over het lijf
    soort_echt, g = graden(nieuw[0])
    nr = 1 + max([r.get("nr", 0) for o in bpy.data.objects if o.get("cj_figuur") == fig for r in lees(o)]
                 + [r.get("nr", 0) for r in oude] + [0])
    rec = {"nr": nr, "naam": naam, "preset": sleutel, "soort": soort_echt, "graden": g,
           "herkomst": herkomst, "punt": [round(c, 4) for c in nieuw[0]["cj_snijpunt"]]}
    for d in nieuw:
        # Elk deel erft de oude gewrichten van het gesneden deel; een gewricht dat aan de andere kant lag,
        # blijft ook op een ander deel van de figuur staan, dus de lijst per figuur raakt niets kwijt.
        d["cj_gewrichten"] = json.dumps(oude + [rec])
        d["cj_naam"] = naam
        d["cj_figuur"] = fig
        d["cj_herkomst"] = herkomst
        if soort_echt == "HINGE" and not d.get("cj_passing"):
            # Daan (16 nov, moet 2): anders zegt "3 Fit and export" "No joint yet" naast acht gewrichten. Een scharnier
            # bestaat alleen bij Good fit (Tight wordt geweigerd), dus groen is waar. Alleen bij figuurdelen.
            d["cj_passing"] = "groen"
    return True, f"{naam}: {SOORT_TEKST[soort_echt].lower()}, {bereik_tekst(soort_echt, g)}.", nieuw


class CLICK_JOINTS_OT_plaats_preset(bpy.types.Operator):
    bl_idname = "click_joints.plaats_preset"
    bl_label = "Place figure joint"
    bl_description = "Place the right joint for this body part at the 3D cursor"
    bl_options = {"REGISTER", "UNDO"}

    deel: EnumProperty(name="Body part", items=KEUZES, default="KNEE")

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        ok, melding, _delen = plaats_gewricht(context, self.deel)
        if not ok:
            if melding:
                self.report({"ERROR"}, melding)
            return {"CANCELLED"}  # anders gaf de onderliggende operator zijn eigen melding al
        self.report({"INFO"}, melding)
        return {"FINISHED"}


def teken_boven(layout, context):
    """Bovenaan het hoofdpaneel, vóór stap 1 (1.2.9, issue 70): heeft je mesh een rig, dan is Figure from rig de eerste
    knop die je ziet. Cleave zet Scan Model bovenaan en Split 3D Print Automatic Detection (GEZIEN, lat kop Paneel);
    bij ons stond onze sterkste knop in een tweede paneel onder ±880 px andere knoppen (GEZIEN, e2e 5.3.0).
    Zonder rig tekent dit niets: dan begin je gewoon bij stap 1."""
    ob = context.active_object
    if ob is None or ob.type != "MESH":
        return
    from . import rig
    arm = rig.zoek_armature(ob)
    if arm is None:
        return
    vak = layout.box()
    vak.label(text=f"Rig found: {arm.name}", icon="ARMATURE_DATA")
    kol = vak.column(align=True)
    kol.scale_y = 1.6
    kol.operator(rig.CLICK_JOINTS_OT_figuur_uit_rig.bl_idname, icon="ARMATURE_DATA").meer = False
    vak.operator(rig.CLICK_JOINTS_OT_figuur_uit_rig.bl_idname, text="More bones (ankles too)").meer = True


class CLICK_JOINTS_PT_figuur(bpy.types.Panel):
    """Eigen paneel "Figure joints" onder Click Joints (zelfde tabblad): in te klappen en te verslepen."""
    bl_label = "Figure joints"
    bl_idname = "CLICK_JOINTS_PT_figuur"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Click Joints"

    def draw_header(self, _context):
        self.layout.label(icon="ARMATURE_DATA")

    def draw(self, context):
        ob = context.active_object
        layout = self.layout
        from . import rig
        arm = rig.zoek_armature(ob) if ob is not None and ob.type == "MESH" else None
        # 1.2.9: Figure from rig staat bovenaan het hoofdpaneel (teken_boven), hier alleen de knoppen per deel.
        layout.label(text="Or put the 3D cursor on a joint, then:" if arm is not None else
                     "Put the 3D cursor on a joint, then:")
        rooster = layout.grid_flow(row_major=True, columns=2, even_columns=True, align=True)
        for sleutel, naam, _soort, _stand in PRESETS:
            ic = icoon(sleutel)
            if ic:
                op = rooster.operator(CLICK_JOINTS_OT_plaats_preset.bl_idname, text=naam, icon_value=ic)
            else:
                op = rooster.operator(CLICK_JOINTS_OT_plaats_preset.bl_idname, text=naam)
            op.deel = sleutel
        lijst = figuur_gewrichten(context.scene.objects, figuur_naam(ob)) if ob is not None else []
        if lijst:
            vak = layout.box()
            vak.label(text=samenvatting(lijst))
            wm = context.window_manager
            if hasattr(wm, "cj_labels"):  # mooier overlay 23 nov: welke gewrichten een boog met label tonen
                rij = vak.row(align=True)
                rij.label(text="Labels")
                rij.prop(wm, "cj_labels", expand=True)
            kol = vak.column(align=True)
            for rec in lijst:
                # Daan (16 nov, kan): `from rig` valt op met een groen bolletje (groen zoals de bogen) in plaats van
                # het lichaamsdeel-icoon. Een losse grijze kolom voor de herkomst paste niet in de zijbalk (het bereik
                # viel weg, eigen beeld 14:35), en de hele regel grijs leest als uitgeschakeld.
                if rec.get("herkomst") in ("from rig", "mirrored"):  # mirrored: bereik van de andere kant van je rig
                    kol.label(text=regel(rec), icon="COLLECTION_COLOR_04")
                else:
                    kol.label(text=regel(rec), icon_value=icoon(rec.get("preset", "")) or 0)


def register():
    from . import rig
    bpy.utils.register_class(CLICK_JOINTS_OT_plaats_preset)
    for k in rig.KLASSEN:
        bpy.utils.register_class(k)
    try:
        import os
        from bpy.utils import previews
        pv = previews.new()
        map_ = os.path.join(os.path.dirname(__file__), "iconen")
        for sleutel, *_ in PRESETS:
            pad = os.path.join(map_, f"{sleutel.lower()}.png")
            if os.path.isfile(pad):
                pv.load(sleutel.lower(), pad, "IMAGE")
        _iconen[0] = pv
    except Exception as e:  # zonder iconen werkt alles, alleen zonder plaatje
        print(f"Click Joints: icons not loaded ({e})")
        _iconen[0] = None
    bpy.utils.register_class(CLICK_JOINTS_PT_figuur)  # na het hoofdpaneel, dus eronder in het tabblad


def unregister():
    bpy.utils.unregister_class(CLICK_JOINTS_PT_figuur)
    if _iconen[0] is not None:
        from bpy.utils import previews
        previews.remove(_iconen[0])
        _iconen[0] = None
    from . import rig
    for k in reversed(rig.KLASSEN):
        bpy.utils.unregister_class(k)
    bpy.utils.unregister_class(CLICK_JOINTS_OT_plaats_preset)

