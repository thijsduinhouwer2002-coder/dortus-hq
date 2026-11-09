"""Filmisch ronde 6 en 6c (6c: punten Daan 9 nov 03:55, nerf per lid in de lengte, beuken #D8A86E/#B98450, hoofdlicht ±4300 K,
wand ver weg, camera iets van boven). Besluit Daan 9 nov 02:35 en bijstelling 02:50): nieuwe houding, echt hout, oneindige achtergrond.

Wordt na film_mooi.py in dezelfde namespace geladen (exec) en vervangt daar de pop, het hout, het licht en de
plek van het gewricht. Zo kan de kleine proef (film_proef.py) het eerst toetsen voordat de grote render erop overgaat.

Wat er anders is dan ronde 5:
1. Linkerarm in rust gestrekt (bovenarm en onderarm in één lijn), zijwaarts, iets naar voren en 15 graden omhoog.
   Het gewricht zit op de elleboog. Waarom niet 30 graden omlaag zoals Daan voorstelde: de add-on snijdt met een
   vlak loodrecht op de as door het hele model; bij een arm die omlaag wijst loopt dat vlak door de voeten (nagerekend:
   de linkervoet komt dan aan de kant van deel B). Daan: "arm verder van het lijf, niet het gewricht ergens anders".
2. Linkerbeen in een trap naar voren, onderbeen horizontaal, zodat ook de knie een gewricht kan krijgen
   (zelfde reden: bij een staand been loopt het snijvlak door het andere been). Rechterbeen draagt.
3. Hout beuken #C99C6E / #A9774A, Wave bands langs de lengte, vervormd met Noise (schaal 3, sterkte 4),
   roughness 0,4, coat 0,3. Hoofdlicht warm (3200 K), randlicht koel (8000 K), AgX Medium High Contrast.
4. Oneindige achtergrond: vloer met een ronde bocht (straal 40 mm) naar een achterwand, zelfde donkere kleur als de
   wereld (#121418) zodat er geen horizon is; een lichtvlek rond de voeten loopt weg in het donker."""
# Deze namen bestaan al uit film_mooi.py: bpy, bmesh, math, Vector, Matrix, _bol, _staaf, kleur, bsdf_van,
# zet_input, figuren, mod, log, staat, deel, gesloten, hout_doorzichtig, paneel-hulp.

ACHTERGROND = "#121418"
HOUT_LICHT, HOUT_DONKER = "#D8A86E", "#B98450"   # 6c: Daan 03:55, licht honingkleurig beuken, weinig contrast
KLEUR_3200K = "#FFE4CE"   # 6c2: hoofdlicht nu ±5000 K (3200 K maakte het hout oranje); naam blijft voor film_mooi
KLEUR_8000K = "#E3E9FF"   # zwarte straler 8000 K, sRGB

SCHOUDER_L = Vector((-15, 0, 92))
ARM = Vector((-0.93, -0.25, 0.27)).normalized()
ELLEBOOG = SCHOUDER_L + ARM * 20.0
HAND = ELLEBOOG + ARM * 28.0
ONDERARM = ARM            # as van het elleboog-gewricht, naar de hand (kant van deel B)
HEUP_L = Vector((-6, 0, 53))
KNIE = Vector((-7, -21, 57))
SCHEEN = Vector((-0.05, -0.99, -0.12)).normalized()
ENKEL = KNIE + SCHEEN * 22.0
POP_MIDDEN = Vector((-8, -6, 62))
BASIS_RICHTING = Vector((0.5, -1.0, -0.22)).normalized()   # 6b: van rechtsvoor, arm dwars in beeld en de trap schuin (6a van links: arm wees naar de lens)


# Assen van de leden voor de nerf (6c): per lid loopt de nerf in de lengte. Romp en hoofd: verticaal.
NERF_LEDEN = [
    ((0, 0, 55), (0, 0, 112), 11.0),
    (SCHOUDER_L, ELLEBOOG, 4.3), (ELLEBOOG, HAND + ARM * 4.0, 4.0),
    ((15, 0, 92), (18, 0, 70), 3.9), ((18, 0, 70), (19.3, -1, 42), 3.3),
    ((6, 0, 53), (6.5, 0, 29), 4.8), ((6.5, 0, 29), (6.5, 0, 1), 3.6),
    (HEUP_L, KNIE, 4.8), (KNIE, ENKEL + Vector((0, -2.0, 2.5)), 3.6),
]


def nerf_coordinaten(me):
    """Zet per punt een vector 'nerf_co' = (langs e1, langs e2, 0,08 x langs de as) van het dichtstbijzijnde lid.
    Waarom (Daan 03:55): met Object-coordinaten liep de nerf als ringen om de arm, want de arm ligt langs X.
    Wave BANDS over de eerste component geeft lijnen evenwijdig aan de as van elk lid; de ruis rekt in de lengte."""
    import numpy as np
    n = len(me.vertices)
    co = np.empty(n * 3, dtype=np.float64)
    me.vertices.foreach_get("co", co)
    co = co.reshape(n, 3)
    beste = np.full(n, np.inf)
    uit = np.zeros((n, 3))
    for p0, p1, r in NERF_LEDEN:
        p0, p1 = np.array(tuple(p0), float), np.array(tuple(p1), float)
        d = p1 - p0
        lengte = np.linalg.norm(d)
        a = d / lengte
        t = np.clip((co - p0) @ a, 0.0, lengte)
        afst = np.linalg.norm(co - (p0 + t[:, None] * a), axis=1) - r
        ref = np.array((0.0, 1.0, 0.0)) if abs(a[1]) < 0.9 else np.array((0.0, 0.0, 1.0))  # e1 dwars op de kijkrichting (-y): geen ringen op de romp
        e1 = np.cross(a, ref)
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(a, e1)
        nieuw = np.stack((co @ e1, co @ e2, (co @ a) * 0.08), axis=1)
        kies = afst < beste
        beste[kies] = afst[kies]
        uit[kies] = nieuw[kies]
    attr = me.attributes.new("nerf_co", "FLOAT_VECTOR", "POINT")
    attr.data.foreach_set("vector", uit.astype(np.float32).ravel())


def tekenpop(solver):
    vormen = [
        _bol(1.0, (0, 0, 108), (6.5, 7.0, 8.5)), _staaf((0, 0, 95), (0, 0, 101), 2.8, 2.6),
        _bol(1.0, (0, 0, 84), (13.0, 8.0, 13.5)), _bol(5.5, (0, 0, 70)), _bol(1.0, (0, 0, 60), (11.0, 7.5, 8.0)),
        # linkerarm gestrekt, gewricht komt op de elleboog
        _bol(4.6, SCHOUDER_L), _staaf(SCHOUDER_L, ELLEBOOG, 4.4, 4.2), _bol(4.6, ELLEBOOG),
        _staaf(ELLEBOOG, HAND, 4.2, 3.8), _bol(1.0, HAND + ARM * 3.0, (4.0, 3.0, 3.6)),
        # rechterarm hangt ontspannen
        _bol(4.6, (15, 0, 92)), _staaf((15, 0, 92), (18, 0, 70), 4.2, 3.6), _bol(4.0, (18, 0, 70)),
        _staaf((18, 0, 70), (19, -1, 49), 3.6, 3.0), _bol(1.0, (19.3, -1, 44), (2.6, 3.2, 5.0)),
        # rechterbeen draagt
        _bol(5.2, (6, 0, 53)), _staaf((6, 0, 53), (6.5, 0, 29), 5.4, 4.3), _bol(4.4, (6.5, 0, 29)),
        _staaf((6.5, 0, 29), (6.5, 0, 6), 4.1, 3.1), _bol(1.0, (6.5, -3, 3), (3.6, 7.0, 3.0)),
        # linkerbeen trapt naar voren, onderbeen horizontaal (knie-gewricht)
        _bol(5.2, HEUP_L), _staaf(HEUP_L, KNIE, 5.4, 4.3), _bol(4.4, KNIE),
        _staaf(KNIE, ENKEL, 4.1, 3.1), _bol(1.0, ENKEL + Vector((0, -2.0, 2.5)), (3.6, 3.0, 7.0)),
    ]
    delen = []
    for i, bm in enumerate(vormen):
        me = bpy.data.meshes.new(f"deel{i}")
        bm.to_mesh(me)
        bm.free()
        ob = bpy.data.objects.new(f"deel{i}", me)
        bpy.context.scene.collection.objects.link(ob)
        delen.append(ob)
    basis = delen[0]
    for d in delen[1:]:
        m = basis.modifiers.new(d.name, "BOOLEAN")
        m.operation, m.object, m.solver = "UNION", d, solver
        d.hide_set(True)
    voxel = float(os.environ.get("MOOI_VOXEL", "0.2"))
    if voxel > 0:
        rm = basis.modifiers.new("zacht", "REMESH")
        rm.mode, rm.voxel_size, rm.use_smooth_shade = "VOXEL", voxel, True
        sm = basis.modifiers.new("glad", "SMOOTH")
        sm.factor, sm.iterations = 0.5, 4
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(basis.evaluated_get(dg))
    for d in delen:
        bpy.data.objects.remove(d)
    me.shade_smooth()
    nerf_coordinaten(me)
    me.materials.clear()  # les ronde 5: new_from_object geeft een leeg vak 0
    me.materials.append(hout_materiaal())
    ob = bpy.data.objects.new("Mannequin", me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def hout_materiaal():
    mat = bpy.data.materials.new("Film hout")
    bsdf = bsdf_van(mat)
    nt = mat.node_tree
    tex = nt.nodes.new("ShaderNodeAttribute")   # 6c: nerf_co per lid (zie nerf_coordinaten), niet Object
    tex.attribute_type, tex.attribute_name = "GEOMETRY", "nerf_co"
    ruis = nt.nodes.new("ShaderNodeTexNoise")
    ruis.inputs["Scale"].default_value = 3.0 / 20.0   # Daans schaal 3 op een pop van ±120 mm (per 20 mm)
    ruis.inputs["Detail"].default_value = 3.0
    vervorm = nt.nodes.new("ShaderNodeVectorMath")     # vector + 4 x ruis: nerf golft, geen strepen met een liniaal
    vervorm.operation = "MULTIPLY_ADD"
    vervorm.inputs[1].default_value = (1.2, 1.2, 1.2)   # 6c: rustig golvend (6a sterkte 4 gaf slangen)
    golf = nt.nodes.new("ShaderNodeTexWave")
    golf.wave_type, golf.bands_direction = "BANDS", "X"   # banden over e1 = nerflijnen in de lengte van elk lid
    golf.inputs["Scale"].default_value = 0.25            # 6b: lijn om de ±1,6 mm (6a: 3,5 mm oogde als zebra)
    golf.inputs["Distortion"].default_value = 1.0
    golf.inputs["Detail"].default_value = 3.0
    meng = nt.nodes.new("ShaderNodeValToRGB")
    meng.color_ramp.elements[0].color = (*kleur(HOUT_DONKER), 1)
    meng.color_ramp.elements[1].color = (*kleur(HOUT_LICHT), 1)
    meng.color_ramp.elements[0].position = 0.15
    meng.color_ramp.elements[1].position = 0.85   # 6b: zachter verloop, minder streep
    nt.links.new(tex.outputs["Vector"], ruis.inputs["Vector"])
    nt.links.new(ruis.outputs["Color"], vervorm.inputs[0])
    nt.links.new(tex.outputs["Vector"], vervorm.inputs[2])
    nt.links.new(vervorm.outputs[0], golf.inputs["Vector"])
    nt.links.new(golf.outputs["Fac"], meng.inputs["Fac"])
    nt.links.new(meng.outputs["Color"], bsdf.inputs["Base Color"])
    zet_input(bsdf, ["Roughness"], 0.4)
    zet_input(bsdf, ["Coat Weight", "Clearcoat"], 0.3)
    zet_input(bsdf, ["Coat Roughness", "Clearcoat Roughness"], 0.15)
    mat.diffuse_color = (*kleur(HOUT_LICHT), 1)
    return mat


def _cyclorama():
    """6c: wand op 500 mm achter de pop (was 60), zodat de bocht nooit als lichte band achter de pop staat.
    Vloer die met een kwartcirkel (straal 40 mm) overgaat in een achterwand, ruim groter dan elk beeld."""
    bm = bmesh.new()
    breed, diep, hoog, straal = 1600.0, 900.0, 900.0, 40.0
    profiel = [(-diep, 0.0)]
    for k in range(0, 17):
        a = math.radians(90 * k / 16)
        profiel.append((straal * math.sin(a), straal * (1 - math.cos(a))))
    profiel.append((straal, hoog))
    rijen = []
    for x in (-breed / 2, breed / 2):
        rijen.append([bm.verts.new((x, py + 500.0, pz)) for py, pz in profiel])
    for i in range(len(profiel) - 1):
        bm.faces.new((rijen[0][i], rijen[1][i], rijen[1][i + 1], rijen[0][i + 1]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new("Achtergrond")
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = True
    return me


def licht_en_wereld():
    sc = bpy.context.scene
    w = sc.world or bpy.data.worlds.new("Film")
    sc.world = w
    try:
        w.use_nodes = True
    except Exception:  # noqa: BLE001
        pass
    bg = next(n for n in w.node_tree.nodes if n.type == "BACKGROUND")
    bg.inputs["Color"].default_value = (*kleur(ACHTERGROND), 1)
    bg.inputs["Strength"].default_value = 0.6

    def zon(naam, richting, kleur_hex, sterkte, hoek):
        ld = bpy.data.lights.new(naam, "SUN")
        ld.energy, ld.angle, ld.color = sterkte, math.radians(hoek), kleur(kleur_hex)
        ob = bpy.data.objects.new(naam, ld)
        sc.collection.objects.link(ob)
        ob.rotation_euler = (-Vector(richting)).normalized().to_track_quat("-Z", "Y").to_euler()

    zon("Hoofdlicht", (-0.7, -0.8, 1.0), KLEUR_3200K, 2.2, 5)   # warm, links voor boven
    zon("Randlicht", (0.6, 1.0, 0.5), KLEUR_8000K, 1.6, 3)      # koel, van achteren
    zon("Vullicht", (1.0, -0.5, 0.25), "#FFF2E6", 0.6, 25)   # 6b: schaduwkant minder zwart
    # Oneindige achtergrond: de wand staat achter de pop (+y), de camera kijkt vanaf -y.
    me = _cyclorama()
    ob = bpy.data.objects.new("Achtergrond", me)
    sc.collection.objects.link(ob)
    mat = bpy.data.materials.new("Film achtergrond")
    b = bsdf_van(mat)
    nt = mat.node_tree
    # lichtvlek rond de voeten: lichter in het midden, wegvloeiend naar de kleur van de wereld
    tex = nt.nodes.new("ShaderNodeTexCoord")
    afst = nt.nodes.new("ShaderNodeVectorMath")
    afst.operation = "LENGTH"
    band = nt.nodes.new("ShaderNodeMapRange")
    band.inputs["From Min"].default_value = 40.0
    band.inputs["From Max"].default_value = 200.0   # 6c: vlek dooft voor de bocht (Daan: geen band)
    kl = nt.nodes.new("ShaderNodeValToRGB")
    kl.color_ramp.elements[0].color = (*kleur("#3A3631"), 1)
    kl.color_ramp.elements[1].color = (*kleur(ACHTERGROND), 1)
    nt.links.new(tex.outputs["Object"], afst.inputs[0])
    nt.links.new(afst.outputs["Value"], band.inputs["Value"])
    nt.links.new(band.outputs["Result"], kl.inputs["Fac"])
    nt.links.new(kl.outputs["Color"], b.inputs["Base Color"])
    # 6c2: buiten de vlek precies de kleur van de wereld, onbelicht (Emission met dezelfde sterkte als de wereld).
    # Zo valt de overgang vloer, bocht en wand weg en staat er geen lichte band achter de pop.
    uit = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*kleur(ACHTERGROND), 1)
    em.inputs["Strength"].default_value = 0.6
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(band.outputs["Result"], mix.inputs[0])
    nt.links.new(b.outputs[0], mix.inputs[1])
    nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], uit.inputs["Surface"])
    zet_input(b, ["Roughness"], 0.6)
    zet_input(b, ["Specular IOR Level", "Specular"], 0.2)
    me.materials.append(mat)


def plaats_op(ob, punt, as_):
    """Echte add-on op het gegeven punt; geeft (uitslag, deel A, deel B) terug."""
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar, inst.toon_bereik, inst.pose_graden = False, False, 0.0
    inst.speling_mm, inst.as_bron, inst.kogel_auto = 0.2, "CURSOR", True
    voor = {o.name for o in bpy.context.scene.objects}
    figuren.zet_cursor(tuple(punt), tuple(as_))
    figuren.maak_actief(ob)
    try:
        uitslag = bpy.ops.click_joints.plaats()
    except RuntimeError as e:  # melding van de add-on (bijvoorbeeld Too close of Too thin)
        uitslag = f"geweigerd: {e}"
    bpy.context.view_layer.update()
    nieuw = [o for o in bpy.context.scene.objects if o.name not in voor]
    a = next((o for o in nieuw if o.get("cj_deel") == "A"), None)
    b = next((o for o in nieuw if o.get("cj_deel") == "B"), None)
    return uitslag, a, b
