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

ACHTERGROND = "#0B0C0F"   # 6d: Daan 04:33, rand van de lichtvlek (midden #1E2026)
VLEK = "#1E2026"
HOUT_LICHT, HOUT_DONKER = "#D8A86E", "#C49060"   # 6d: Daan 04:33, bijna egaal, nerf hooguit 10 procent verschil
ROOD = (*kleur("#E0261C"), 1.0)   # 6d: Daan 04:33, verzadigd rood als basis, lage gloed (AgX bleekt fel rood naar roze)
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


def hout_kleur(nt):
    """6d (Daan 04:33): bijna egaal beuken. Fijne, onregelmatige nerflijnen in de lengte van elk lid (nerf_co),
    de lijnen zelf onderbroken door ruis in de breedte, kleurverschil hooguit ±10 procent licht.
    Geeft de kleur-uitgang terug, zodat ook de rand van de groene ring (strakke_ring) hetzelfde hout krijgt."""
    tex = nt.nodes.new("ShaderNodeAttribute")
    tex.attribute_type, tex.attribute_name = "GEOMETRY", "nerf_co"
    ruis = nt.nodes.new("ShaderNodeTexNoise")
    ruis.inputs["Scale"].default_value = 3.0 / 20.0
    ruis.inputs["Detail"].default_value = 3.0
    vervorm = nt.nodes.new("ShaderNodeVectorMath")
    vervorm.operation = "MULTIPLY_ADD"
    vervorm.inputs[1].default_value = (2.4, 2.4, 2.4)
    golf = nt.nodes.new("ShaderNodeTexWave")
    golf.wave_type, golf.bands_direction = "BANDS", "X"
    golf.inputs["Scale"].default_value = 0.55            # 6d: fijner (lijn om de ±0,6 mm)
    golf.inputs["Distortion"].default_value = 4.0
    golf.inputs["Detail"].default_value = 4.0
    golf.inputs["Detail Roughness"].default_value = 0.7
    breed = nt.nodes.new("ShaderNodeTexNoise")           # 6d: lijnen onderbroken en ongelijk, geen ribfluweel
    breed.inputs["Scale"].default_value = 0.35
    breed.inputs["Detail"].default_value = 2.0
    keer = nt.nodes.new("ShaderNodeMath")
    keer.operation = "MULTIPLY"
    meng = nt.nodes.new("ShaderNodeValToRGB")
    meng.color_ramp.elements[0].color = (*kleur(HOUT_LICHT), 1)
    meng.color_ramp.elements[1].color = (*kleur(HOUT_DONKER), 1)
    meng.color_ramp.elements[0].position = 0.15
    meng.color_ramp.elements[1].position = 0.55
    nt.links.new(tex.outputs["Vector"], ruis.inputs["Vector"])
    nt.links.new(ruis.outputs["Color"], vervorm.inputs[0])
    nt.links.new(tex.outputs["Vector"], vervorm.inputs[2])
    nt.links.new(vervorm.outputs[0], golf.inputs["Vector"])
    nt.links.new(tex.outputs["Vector"], breed.inputs["Vector"])
    nt.links.new(golf.outputs["Fac"], keer.inputs[0])
    nt.links.new(breed.outputs["Fac"], keer.inputs[1])
    nt.links.new(keer.outputs[0], meng.inputs["Fac"])
    return meng.outputs["Color"]


def hout_zet(bsdf):
    zet_input(bsdf, ["Roughness"], 0.52)   # 6d: iets ruwer, zachtere glans
    zet_input(bsdf, ["Coat Weight", "Clearcoat"], 0.15)
    zet_input(bsdf, ["Coat Roughness", "Clearcoat Roughness"], 0.25)


def hout_materiaal():
    mat = bpy.data.materials.new("Film hout")
    bsdf = bsdf_van(mat)
    nt = mat.node_tree
    nt.links.new(hout_kleur(nt), bsdf.inputs["Base Color"])
    hout_zet(bsdf)
    mat.diffuse_color = (*kleur(HOUT_LICHT), 1)
    return mat


def doorzichtig_maken(mat):
    """6d: zoals in film_mooi, maar mengt wat er nu aan de uitgang hangt (bij de groene ring: groen plus hout-rand)
    met Transparent, in plaats van de eerste Principled. Anders valt de strakke rand weg zodra B doorzichtig wordt."""
    nt = mat.node_tree
    uit = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    bron = uit.inputs["Surface"].links[0].from_socket
    door, mix, waarde = (nt.nodes.new(t) for t in ("ShaderNodeBsdfTransparent", "ShaderNodeMixShader", "ShaderNodeValue"))
    waarde.outputs[0].default_value = 0.0
    nt.links.new(waarde.outputs[0], mix.inputs[0])
    nt.links.new(bron, mix.inputs[1])
    nt.links.new(door.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], uit.inputs["Surface"])
    return waarde


VOEGEN = []   # (snijpunt, as) en kogelstraal van elk geplaatst gewricht


def strakke_ring(ob):
    """6d (Daan 04:33, punt 4): de groene ring van de add-on kleurt elk vlak met een hoekpunt binnen 3 mm van de
    snede, dus de rand volgt de vlakken van de remesh en is gekarteld als afgescheurd plakband. Alleen voor de film:
    per punt een getal f = 3 mm min de afstand tot het snijvlak (langs de as); bij kogel, nek en kom f = 1.
    Dat getal loopt lineair over elk vlak, dus f > 0 geeft in de shader een strakke rand precies op 3 mm.
    Waar f < 0 binnen een groen vlak valt, krijgt het vlak hetzelfde hout. De add-on zelf blijft ongewijzigd."""
    import numpy as np
    me = ob.data
    vak = ob.get("cj_ring_vak")
    if vak is None or vak >= len(me.materials) or me.materials[vak] is None:
        return False
    n = len(me.vertices)
    co = np.empty(n * 3)
    me.vertices.foreach_get("co", co)
    co = co.reshape(n, 3)
    mw = np.array(ob.matrix_world)
    co = co @ mw[:3, :3].T + mw[:3, 3]
    sleutel = (tuple(round(x, 3) for x in ob["cj_snijpunt"]), tuple(round(x, 4) for x in ob["cj_as"]))
    if sleutel not in [v[0] for v in VOEGEN]:
        VOEGEN.append((sleutel, float(ob.get("cj_kogel_r", 2.0))))
    f = np.full(n, -1e9)
    for (p0, as_), rr in VOEGEN:   # een deel met twee gewrichten (knie op A) houdt ook de eerste ring strak
        p0, as_ = np.array(p0, float), np.array(as_, float)
        as_ /= np.linalg.norm(as_)
        rel = co - p0
        h = rel @ as_
        radiaal = np.linalg.norm(rel - np.outer(h, as_), axis=1)
        fj = 3.0 - np.abs(h)
        fj[(radiaal <= rr + 0.8) & (h >= -3.0) & (h <= 2.5 * rr + 1.0)] = 1.0
        f = np.maximum(f, fj)
    attr = me.attributes.get("cj_film_ring") or me.attributes.new("cj_film_ring", "FLOAT", "POINT")
    attr.data.foreach_set("value", f.astype(np.float32))
    oud = me.materials[vak]
    if oud.get("cj_strak"):   # tweede gewricht: materiaal is al omgebouwd, alleen het getal f was nodig
        return True
    # De kopie krijgt de naam van het origineel (mat_naam("groen")), zodat gloed() en hout_doorzichtig() van
    # film_mooi hem vinden; het origineel heet voortaan "... add-on". De eerste Principled blijft de groene.
    naam = oud.name
    oud.name = naam + " add-on"
    mat = oud.copy()
    mat.name = naam
    mat["cj_strak"] = 1
    if True:
        nt = mat.node_tree
        uit = next(x for x in nt.nodes if x.type == "OUTPUT_MATERIAL")
        groen = next(x for x in nt.nodes if x.type == "BSDF_PRINCIPLED")
        hout = nt.nodes.new("ShaderNodeBsdfPrincipled")
        nt.links.new(hout_kleur(nt), hout.inputs["Base Color"])
        hout_zet(hout)
        at = nt.nodes.new("ShaderNodeAttribute")
        at.attribute_type, at.attribute_name = "GEOMETRY", "cj_film_ring"
        stap = nt.nodes.new("ShaderNodeMath")
        stap.operation = "GREATER_THAN"
        stap.inputs[1].default_value = 0.0
        mix = nt.nodes.new("ShaderNodeMixShader")
        nt.links.new(at.outputs["Fac"], stap.inputs[0])
        nt.links.new(stap.outputs[0], mix.inputs[0])
        nt.links.new(hout.outputs[0], mix.inputs[1])
        nt.links.new(groen.outputs[0], mix.inputs[2])
        nt.links.new(mix.outputs[0], uit.inputs["Surface"])
    for o in bpy.data.objects:   # ook andere delen die het oude groen nog dragen (A en B delen het)
        if o.type == "MESH":
            for i, m in enumerate(o.data.materials):
                if m is oud:
                    o.data.materials[i] = mat
    return True


def rood_basis():
    """6d: basiskleur van Too thin verzadigd rood (#E0261C), zodat een lage gloed rood blijft en niet roze wordt."""
    m = bpy.data.materials.get(mat_naam("rood"))
    if m is None or m.node_tree is None:
        return False
    b = next((x for x in m.node_tree.nodes if x.type == "BSDF_PRINCIPLED"), None)
    if b is not None:
        b.inputs["Base Color"].default_value = ROOD
    m.diffuse_color = ROOD
    return True


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
    # 6d (Daan 04:33, punt 3): zachte lichtvlek achter en onder de pop, radiaal #1E2026 naar #0B0C0F, zonder rand,
    # in elk shot gelijk. Hoe: de achtergrond is onbelicht (Emission) met een vlek in beeldcoördinaten (Window),
    # dus de vlek staat altijd achter het onderwerp, van ver en van dichtbij. Alleen dicht bij de voeten (tot 60 mm)
    # gaat hij over in een belichte vloer in de vlekkleur, voor een zachte schaduw onder de voeten.
    tex = nt.nodes.new("ShaderNodeTexCoord")
    mid = nt.nodes.new("ShaderNodeVectorMath")
    mid.operation = "SUBTRACT"
    mid.inputs[1].default_value = (0.5, 0.42, 0.0)
    schaal = nt.nodes.new("ShaderNodeVectorMath")
    schaal.operation = "MULTIPLY"
    schaal.inputs[1].default_value = (1.0, 0.5625, 0.0)   # 16:9, vlek rond
    lengte = nt.nodes.new("ShaderNodeVectorMath")
    lengte.operation = "LENGTH"
    vlek = nt.nodes.new("ShaderNodeMapRange")
    vlek.interpolation_type = "SMOOTHSTEP"
    vlek.inputs["From Min"].default_value = 0.0
    vlek.inputs["From Max"].default_value = 0.62
    kl = nt.nodes.new("ShaderNodeValToRGB")
    kl.color_ramp.elements[0].color = (*kleur(VLEK), 1)
    kl.color_ramp.elements[1].color = (*kleur(ACHTERGROND), 1)
    nt.links.new(tex.outputs["Window"], mid.inputs[0])
    nt.links.new(mid.outputs[0], schaal.inputs[0])
    nt.links.new(schaal.outputs[0], lengte.inputs[0])
    nt.links.new(lengte.outputs["Value"], vlek.inputs["Value"])
    nt.links.new(vlek.outputs["Result"], kl.inputs["Fac"])
    b.inputs["Base Color"].default_value = (*kleur(VLEK), 1)
    voet = nt.nodes.new("ShaderNodeVectorMath")
    voet.operation = "LENGTH"
    band = nt.nodes.new("ShaderNodeMapRange")
    band.interpolation_type = "SMOOTHSTEP"
    band.inputs["From Min"].default_value = 25.0
    band.inputs["From Max"].default_value = 60.0
    nt.links.new(tex.outputs["Object"], voet.inputs[0])
    nt.links.new(voet.outputs["Value"], band.inputs["Value"])
    uit = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    em = nt.nodes.new("ShaderNodeEmission")
    nt.links.new(kl.outputs["Color"], em.inputs["Color"])
    em.inputs["Strength"].default_value = 1.0
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


_render_instellingen_mooi = render_instellingen


def render_instellingen():
    """6c3: zelfde als ronde 5, maar look AgX Base Contrast: Medium High Contrast maakte het beuken oranje."""
    _render_instellingen_mooi()
    try:
        bpy.context.scene.view_settings.look = "AgX - Base Contrast"
    except TypeError:  # oudere naam
        bpy.context.scene.view_settings.look = "None"
