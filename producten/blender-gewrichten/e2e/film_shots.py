"""Shots, camerabanen en hoofdlus van de grote filmische render (ronde 6). Wordt door film_mooi.py in main()
geladen, na film_zes.py, in dezelfde namespace; alle namen van die twee bestaan hier dus al.

Shots (Daan 9 nov 02:35 en 02:50, 30 beelden per seconde):
haak 0,5 s, held 2,5 s, gewricht 2,5 s, buigen 4 s (0, 15, 28 met rood, terug naar 0), uit elkaar 2,5 s,
klik-in 2 s, twee gewrichten 3 s. De eindkaart van 2 s plakt de workflow erachter.
Camera: elk standpunt is (doel, richting, afstand, lens); binnen een shot loopt de camera met glad() van het ene
naar het andere (rustig in en uit), bij close-ups staat het gewricht op een derde van de beeldbreedte."""


def derde(punt, richting, afst, lens, hand):
    """Doel waarbij 'punt' op een derde van de beeldbreedte staat, aan de kant weg van 'hand' (deel B krijgt ruimte).
    Beeldbreedte op afstand d bij een sensor van 36 mm: d x 36 / lens; een derde ligt een zesde naast het midden."""
    rechts = (-richting).cross(Z).normalized()
    kant = 1.0 if hand.dot(rechts) >= 0 else -1.0
    return punt + rechts * kant * (afst * 36.0 / lens) / 6.0


def stand(punt, richting, afst, lens, op_derde=True):
    richting = Vector(richting).normalized()
    doel = derde(punt, richting, afst, lens, staat["as_"]) if op_derde and "as_" in staat else Vector(punt)
    return doel, richting, afst, lens


def meng(s1, s2, p):
    d = s1[0].lerp(s2[0], p)
    r = s1[1].lerp(s2[1], p).normalized()
    afst = s1[2] * (s2[2] / s1[2]) ** p   # zoom gelijkmatig in verhouding, niet in mm
    return d, r, afst, s1[3] + (s2[3] - s1[3]) * p


def zet(cam, s):
    doel, r, afst, lens = s
    kijk(cam, doel + r * afst, doel, lens=lens)


def label(tekst):
    """Label in de hoek van het beeld via de stempel van Blender (Note), zonder de andere stempelvelden."""
    r = bpy.context.scene.render
    try:
        r.use_stamp = bool(tekst)
        if tekst:
            r.stamp_note_text = tekst
    except Exception as e:  # noqa: BLE001
        log(f"label lukte niet: {e}")


def label_instellen():
    r = bpy.context.scene.render
    for k in dir(r):
        if k.startswith("use_stamp_") and k != "use_stamp_note":
            try:
                setattr(r, k, False)
            except Exception:  # noqa: BLE001  (alleen-lezen of geen schakelaar)
                pass
    for k, w in (("use_stamp_note", True), ("use_stamp_labels", False), ("stamp_font_size", 20 if SNEL else 40),
                 ("stamp_foreground", (1.0, 1.0, 1.0, 1.0)), ("stamp_background", (0.0, 0.0, 0.0, 0.45))):
        try:
            setattr(r, k, w)
        except Exception as e:  # noqa: BLE001
            log(f"stempel {k} niet gezet: {e}")
    r.use_stamp = False


# ---------- gewrichten plaatsen (echte add-on) ----------

def plaats_elleboog(pop):
    inst = bpy.context.scene.click_joints
    uit, a, b = plaats_op(pop, ELLEBOOG, ONDERARM)
    if a is None or b is None:
        raise RuntimeError(f"elleboog niet geplaatst: {uit}")
    pop.hide_render = True
    paneel = mod("paneel")
    log(f"elleboog: {uit}, kogel {inst.kogel_mm} mm, passing {a.get('cj_passing')}, wand {a.get('cj_wand_mm')}, "
        f"tekst {paneel.buig_tekst(a)}, bereik {[round(x, 1) for x in a.get('cj_buig_graden', [])]}")
    log(f"strakke ring A {strakke_ring(a)} B {strakke_ring(b)}; foute randen A {gesloten(a)} B {gesloten(b)}")
    as_ = Vector(a["cj_as"]).normalized()
    rich = mod("uit_elkaar").richtingen(as_)
    k = max(range(len(rich)), key=lambda i: rich[i].z)
    inst.pose_richting = str(k)
    zij = as_.cross(rich[k]).normalized()
    if zij.dot(BASIS_RICHTING) < 0:
        zij = -zij
    grens = paneel.richting_graden(a, k)
    staat.update(pop=pop, a=a, b=b, as_=as_, k=k, c=Vector(a["cj_centrum"]), r=float(a["cj_kogel_r"]), zij=zij,
                 grens=grens if grens is not None else 20, los=as_ * mod("uit_elkaar").afstand(b))
    staat["b_door"] = hout_doorzichtig(b)
    log(f"richting {k}, grens {grens}, kogelstraal {staat['r']:.2f}, B doorzichtig {len(staat['b_door'] or [])} materialen")


def plaats_knie():
    a, inst = staat["a"], bpy.context.scene.click_joints
    inst.pose_graden = 0.0
    uit, a2, b2 = plaats_op(a, KNIE, SCHEEN)
    if a2 is None or b2 is None:
        log(f"knie niet geplaatst ({uit}), twee gewrichten wordt alleen de elleboog")
        staat["max_twee"] = min(15.0, staat["grens"] - 3)
        return
    a.hide_render = True
    paneel = mod("paneel")
    grens2 = paneel.richting_graden(a2, staat["k"])
    log(f"knie: {uit}, passing {a2.get('cj_passing')}, tekst {paneel.buig_tekst(a2)}, grens {grens2}, "
        f"strakke ring A2 {strakke_ring(a2)} B2 {strakke_ring(b2)}")
    kleinste = min(staat["grens"], grens2 if grens2 is not None else staat["grens"])
    staat["max_twee"] = min(15.0, kleinste - 3)   # Bend geldt voor alle gewrichten: onder de kleinste grens blijven


def rood_stand():
    """Camera op de normaal van de rode vlakken (cj_rood_vlakken van deel A), afstand maat / 0,2, zoals proef 4b."""
    if "rood_st" in staat:
        return staat["rood_st"]
    a = staat["a"]
    mw, punten, norm = a.matrix_world, [], Vector()
    for i in list(a.get("cj_rood_vlakken", []))[0::2]:
        pg = a.data.polygons[i]
        punten += [mw @ a.data.vertices[v].co for v in pg.vertices]
        norm += (mw.to_3x3() @ pg.normal) * pg.area
    if not punten:
        log("geen rode vlakken op 28 graden, rood-shot blijft van opzij")
        staat["rood_st"] = None
        return None
    rc = sum(punten, Vector()) / len(punten)
    maat = max((p - rc).length for p in punten) * 2
    norm = norm.normalized() if norm.length > 1e-9 else staat["zij"].copy()
    d = min(max(maat / 0.2, 4 * staat["r"]), 30 * staat["r"])
    log(f"rood: {len(punten)} punten, midden {tuple(round(x, 2) for x in rc)}, maat {maat:.2f} mm, afstand {d:.1f}")
    staat["rood_st"] = (rc, norm, d)
    return staat["rood_st"]


# ---------- standpunten ----------

def st_held(a):   # pop van hoofd tot voet ±80 procent van de hoogte (proef 6c), langzaam 12 graden om de pop
    return stand(Vector((-4, -8, 56)), draai(BASIS_RICHTING, Z, -6 + 12 * a), 355 - 15 * a, 50, op_derde=False)


def st_dichtbij(afst_r, lens=50):   # elleboog van opzij, schouder en hand in beeld (proef 3-elleboog-0)
    rr = staat["r"]
    return stand(staat["c"], staat["zij"] * 95 * rr + Vector((0, 0, -10)), afst_r * rr, lens)


def st_uit(hoek, afst_r, schuif):   # om de as gedraaid, zodat je kogel en kom ziet
    zij, as_ = staat["zij"], staat["as_"]
    r = zij * math.cos(math.radians(hoek)) + as_ * math.sin(math.radians(hoek))
    return stand(staat["c"] + as_ * schuif, r, afst_r * staat["r"], 60)


def pose_buigen(t):
    """0 -> 15 (0,9 s), stil tot 1,2, 15 -> 28 (0,8 s), stil op 28 tot 3,2 (rood-shot), 28 -> 0 (0,8 s)."""
    if t < 0.9:
        return 15 * glad(t / 0.9)
    if t < 1.2:
        return 15.0
    if t < 2.0:
        return 15 + 13 * glad((t - 1.2) / 0.8)
    if t < 3.2:
        return 28.0
    return 28 * (1 - glad((t - 3.2) / 0.8))


def zet_pose(g):
    inst = bpy.context.scene.click_joints
    if abs(inst.pose_graden - g) > 1e-3:
        inst.pose_graden = round(g, 2)
        bpy.context.view_layer.update()


# ---------- per beeld ----------

def basis(cam):
    """Alles terug naar de rusttoestand; elk shot zet daarna alleen wat het nodig heeft (scherven lopen door elkaar)."""
    sc = bpy.context.scene
    sc.view_settings.exposure = 0.0
    label(None)
    cam.data.dof.aperture_fstop = staat["fstop"]
    if "b" in staat:
        if "max_twee" not in staat:   # fase elleboog: gewricht zichtbaar, pop weg (gewricht zet dit per beeld om)
            staat["pop"].hide_render = True
            staat["a"].hide_render = False
        staat["b"].hide_render = False
        staat["b"].delta_location = (0, 0, 0)
        zet_door(0.0)
        gloed(mat_naam("groen"), GROEN, 0.6)
        gloed(mat_naam("rood"), ROOD, 0.0)


def zet_beeld(cam, naam, i, n):
    t, a = i / FPS, i / max(n - 1, 1)
    basis(cam)
    if naam == "held":
        zet(cam, st_held(a))
        return
    rr, c, as_ = staat["r"], staat["c"], staat["as_"]
    if naam == "haak":   # dichtbij, donker, de groene ring flitst aan
        zet_pose(0.0)
        bpy.context.scene.view_settings.exposure = -2.2 + 1.0 * glad(a)
        zet(cam, meng(stand(c, staat["zij"] + as_ * 0.3, 46 * rr, 60), stand(c, staat["zij"] + as_ * 0.3, 38 * rr, 60), glad(a)))
        gloed(mat_naam("groen"), GROEN, 7.0 * glad((t - 0.1) / 0.12))
        return
    if naam == "gewricht":   # van de held naar de elleboog; op 0,9 s klikt het gewricht erin en flitst de ring
        zet_pose(0.0)
        zet(cam, meng(st_held(1.0), st_dichtbij(95), glad(t / 2.3)))
        erin = t >= 0.9
        staat["pop"].hide_render = erin
        staat["a"].hide_render = staat["b"].hide_render = not erin
        gloed(mat_naam("groen"), GROEN, 0.6 + 6.5 * math.exp(-((t - 1.1) ** 2) / 0.12) if erin else 0.0)
        return
    if naam == "buigen":
        g = pose_buigen(t)
        zet_pose(g)
        rood_basis()
        voorbij = min(1.0, max(0.0, g - staat["grens"]) / 3.0)
        gloed(mat_naam("rood"), ROOD, 1.0 * voorbij)   # Daan 04:33: verzadigde basis, gloed rond 1
        rs = rood_stand() if 2.0 <= t < 3.2 else None
        if rs is not None:   # inzet: eerst B kort doorzichtig, daarna zonder B met label "Exploded view"
            rc, norm, d = rs
            cam.data.dof.aperture_fstop = 22.0
            zet(cam, stand(rc, norm, d * (1.12 - 0.12 * glad((t - 2.0) / 1.2)), 60, op_derde=False))
            if t < 2.35:
                zet_door(0.93 * glad((t - 2.0) / 0.3))
            else:
                staat["b"].hide_render = True
                label("Exploded view")
        elif t < 3.2:   # van opzij, bij de grens kort inzoomen
            zet(cam, meng(st_dichtbij(95), st_dichtbij(70, 55), glad(t / 2.0)))
        else:
            zet(cam, meng(st_dichtbij(70, 55), st_uit(0, 85, 0), glad((t - 3.2) / 0.8)))
        if i in (0, 36, 66, 90, 110):
            log(f"buigen beeld {i}: pose {g:.1f}, rode vlakken A {len(staat['a'].get('cj_rood_vlakken', [])) // 2}")
        return
    if naam == "uit_elkaar":   # B schuift van de kogel, de camera draait 50 graden mee
        zet_pose(0.0)
        p = glad(t / 1.2)
        staat["b"].delta_location = staat["los"] * 1.25 * p
        q = glad(a)
        zet(cam, meng(st_uit(0, 85, 0), st_uit(50, 70, staat["los"].length * 0.6), q))
        gloed(mat_naam("groen"), GROEN, 0.6 + 1.5 * math.exp(-((t - 1.2) ** 2) / 0.1))
        return
    if naam == "klik_in":   # B schuift terug op de kogel, klikt, veert een fractie terug en ligt stil
        zet_pose(0.0)
        if t < 0.9:
            u = t / 0.9
            uit = 1.25 * (1 - u ** 3)   # versnelt naar de klik toe
            staat["b"].delta_location = staat["los"] * uit
        else:
            s = t - 0.9
            veer = 0.25 * math.exp(-s * 7.0) * abs(math.sin(s * 18.0))   # mm naar buiten, nooit de kogel in
            staat["b"].delta_location = as_ * veer
        zet(cam, meng(st_uit(50, 70, staat["los"].length * 0.6), st_uit(20, 62, 0), glad(a)))
        gloed(mat_naam("groen"), GROEN, 0.6 + 4.0 * math.exp(-((t - 0.9) ** 2) / 0.02))
        return
    if naam == "twee":   # elleboog en knie buigen samen (Bend is voor alle gewrichten gelijk), camera laag eromheen
        zet_pose(staat["max_twee"] * math.sin(math.pi * glad(a)))
        zet(cam, stand(Vector((-4, -8, 56)), draai(BASIS_RICHTING, Z, 10 - 20 * glad(a)), 360 - 25 * glad(a), 50,
                       op_derde=False))


def hoofdlus():
    log(f"Blender {bpy.app.version_string}, scherf {SCHERF}/{AANTAL}, snel {SNEL}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    render_instellingen()
    label_instellen()
    licht_en_wereld()
    cam = camera()
    staat["fstop"] = cam.data.dof.aperture_fstop
    pop = tekenpop(mod("gewricht").solver_naam())
    log(f"pop: {len(pop.data.polygons)} vlakken, foute randen {gesloten(pop)}, look {bpy.context.scene.view_settings.look}")
    totaal = sum(n for _, n in SHOTS)
    mijn = [f for f in range(totaal) if f % AANTAL == SCHERF]
    if os.environ.get("MOOI_ALLEEN"):
        mijn = [int(x) for x in os.environ["MOOI_ALLEEN"].split(",")]
    fase = -1
    for f in sorted(mijn, key=lambda f: (FASE.get(zoek_shot(f)[0], 1), f)):
        naam, i, n = zoek_shot(f)
        nodig = FASE.get(naam, 1)
        if nodig >= 1 and fase < 1:
            plaats_elleboog(pop)
        if nodig >= 2 and fase < 2:
            plaats_knie()
        fase = nodig
        zet_beeld(cam, naam, i, n)
        bpy.context.view_layer.update()
        bpy.context.scene.render.filepath = os.path.join(UIT, "beelden", f"{f + 1:04d}.png")
        bpy.ops.render.render(write_still=True)
        log(f"beeld {f + 1} ({naam} {i}) klaar")
    log(f"MOOI KLAAR ({totaal} beelden in Blender, daarna {EINDKAART} beelden eindkaart in de workflow)")
