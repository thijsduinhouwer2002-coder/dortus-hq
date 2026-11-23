"""De vaste studio voor alle Blender-filmpjes van Click Joints Pro (23 nov 2026, opdracht hoofdchat ±11:45 NL).

Zachte studio: een gebogen achterwand (vloer loopt rond over in de wand, geen naad, geen raster) met een verloop in
muntgroen, een rond wit podium onder het figuur, drie vlakke lampen (sleutel, vul, rand) plus een zacht licht op de
wand achter het figuur. Het figuur krijgt een materiaal als geprint plastic (glans, laklaag, fijne laaglijnen).
Camera's voor staand 9:16 (1080x1920) en liggend 16:9 (1920x1080). En een rustig Blender-scherm voor opnames:
alleen de 3D-weergave met het paneel van Click Joints, groter lettertype, geen menubalk, raster of assen.

Gebruik (in een Blender met beeldscherm, zoals xvfb-run in de workflow):
    import studio as S
    S.bouw()                          # achterwand, podium, lampen, wereld, EEVEE-instellingen
    S.plastic(delen)                  # materialen van het figuur als geprint plastic
    cam = S.camera()
    S.richt(cam, delen, "staand", draai=-30, kantel=8)
    S.render("/tmp/uit/eind.png")     # door de camera, wat de 3D-weergave toont (ook de buiging van de add-on)
    S.rustig_scherm(ui=1.35)          # voor schermopnames
Alle maten in mm (scene in millimeters, zoals de add-on).
"""
import math
import os

import bpy
from mathutils import Vector

# Kleuren (sRGB hex). Munt achter oranje, blauw en geel: rustig, vrolijk en met genoeg contrast.
KLEUR = {
    "vloer": "E4F6EF",      # licht munt, onder het figuur
    "wand": "9EE0CC",       # muntgroen bovenaan de wand
    "podium": "FFFFFF",
    "podium_rand": "FFD23F",
    "gewricht": "FFF6E6",   # roomwit voor de delen die de add-on in het gewricht maakt (kogel, kom, scharnier)
}


def srgb(h, a=1.0):
    c = tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    return tuple((x / 12.92) if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c) + (a,)


def _weg(naam):
    ob = bpy.data.objects.get(naam)
    if ob is not None:
        bpy.data.objects.remove(ob)


def _mat(naam):
    m = bpy.data.materials.get(naam) or bpy.data.materials.new(naam)
    try:
        m.use_nodes = True
    except Exception:  # noqa: BLE001 (Blender 5 heeft altijd nodes)
        pass
    return m


def _bsdf(m):
    nt = m.node_tree
    b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
    if b is None:
        b = nt.nodes.new("ShaderNodeBsdfPrincipled")
        uit = next((n for n in nt.nodes if n.type == "OUTPUT_MATERIAL"), None) or nt.nodes.new("ShaderNodeOutputMaterial")
        nt.links.new(b.outputs[0], uit.inputs[0])
    return b


def _zet(b, naam, waarde):
    if naam in b.inputs:
        b.inputs[naam].default_value = waarde


def achterwand(h, z0=0.0):
    """Gebogen achterwand: vloer tot y=0, kwartcirkel met straal 1,6h omhoog, wand tot 4h. Breed 10h."""
    _weg("studio_wand")
    r, diep, hoog, breed = 1.6 * h, 6.0 * h, 14.0 * h, 40.0 * h
    prof = [(y, 0.0) for y in [(-diep + diep * i / 12) for i in range(13)]]
    for i in range(1, 17):
        a = math.pi / 2 * i / 16
        prof.append((r * math.sin(a), r * (1 - math.cos(a))))
    prof += [(r, r + (hoog - r) * i / 8) for i in range(1, 9)]
    kol = 2
    verts, faces = [], []
    for x in (-breed / 2, breed / 2):
        for (y, z) in prof:
            verts.append((x, y + 1.2 * h, z + z0))
    n = len(prof)
    for i in range(n - 1):
        faces.append((i, i + 1, n + i + 1, n + i))
    me = bpy.data.meshes.new("studio_wand")
    me.from_pydata(verts, [], faces)
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new("studio_wand", me)
    bpy.context.scene.collection.objects.link(ob)
    sub = ob.modifiers.new("glad", "SUBSURF")
    sub.levels = sub.render_levels = 2
    m = _mat("studio_wand")
    nt = m.node_tree
    b = _bsdf(m)
    _zet(b, "Roughness", 0.85)
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    mr = nt.nodes.new("ShaderNodeMapRange")
    mr.inputs["From Min"].default_value = 0.0
    mr.inputs["From Max"].default_value = 1.5 * h
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = srgb(KLEUR["vloer"])
    ramp.color_ramp.elements[1].color = srgb(KLEUR["wand"])
    ramp.color_ramp.elements[0].position = 0.0
    ramp.color_ramp.interpolation = "EASE"
    nt.links.new(tc.outputs["Object"], sep.inputs[0])
    nt.links.new(sep.outputs["Z"], mr.inputs["Value"])
    nt.links.new(mr.outputs["Result"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    m.diffuse_color = srgb(KLEUR["wand"])
    ob.data.materials.append(m)
    ob.hide_select = True
    return ob


def podium(h, z0=0.0):
    """Rond podium, bovenkant op z0 (de voeten van het figuur), met een gele rand."""
    for n in ("studio_podium", "studio_rand"):
        _weg(n)
    r, dik = 0.42 * h, 0.06 * h
    bpy.ops.mesh.primitive_cylinder_add(vertices=128, radius=r, depth=dik, location=(0, 0, z0 - dik / 2))
    ob = bpy.context.active_object
    ob.name = "studio_podium"
    bev = ob.modifiers.new("rond", "BEVEL")
    bev.width, bev.segments = 0.012 * h, 4
    bpy.ops.object.shade_smooth()
    m = _mat("studio_podium")
    b = _bsdf(m)
    b.inputs["Base Color"].default_value = srgb(KLEUR["podium"])
    _zet(b, "Roughness", 0.35)
    _zet(b, "Coat Weight", 0.2)
    m.diffuse_color = srgb(KLEUR["podium"])
    ob.data.materials.append(m)
    bpy.ops.mesh.primitive_torus_add(major_radius=r, minor_radius=0.012 * h, location=(0, 0, z0 - dik * 0.55),
                                     major_segments=128, minor_segments=16)
    ring = bpy.context.active_object
    ring.name = "studio_rand"
    bpy.ops.object.shade_smooth()
    mr = _mat("studio_rand")
    br = _bsdf(mr)
    br.inputs["Base Color"].default_value = srgb(KLEUR["podium_rand"])
    _zet(br, "Roughness", 0.3)
    mr.diffuse_color = srgb(KLEUR["podium_rand"])
    ring.data.materials.append(mr)
    for o in (ob, ring):
        o.hide_select = True
    return ob


KRACHT = {"sleutel": 3.0e6, "vul": 1.0e6, "rand": 2.5e6, "zon": 1.6}   # W, op het oog gezet (zie lampen)


def lampen(h, mid):
    """Drie vlakke lampen (zacht, groot) en een zon zonder schaduw die wand en vloer gelijkmatig licht geeft. Kracht in W op mm-schaal:
    de scene staat in millimeters (1 eenheid = 1 mm), dus de afstanden zijn groot; de getallen zijn op het oog gezet."""
    for n in ("studio_sleutel", "studio_vul", "studio_rand_licht", "studio_wandlicht"):
        _weg(n)
    s = (h / 220.0) ** 2
    lijst = (
        ("studio_sleutel", "AREA", (-1.6 * h, -1.9 * h, 2.0 * h), 1.1 * h, KRACHT["sleutel"] * s, "FFF4E8"),
        ("studio_vul", "AREA", (2.2 * h, -1.6 * h, 0.9 * h), 1.6 * h, KRACHT["vul"] * s, "EAF2FF"),
        ("studio_rand_licht", "AREA", (1.2 * h, 1.4 * h, 2.2 * h), 0.7 * h, KRACHT["rand"] * s, "FFFFFF"),
        ("studio_wandlicht", "SUN", (0.0, -3.0 * h, 3.0 * h), 0.0, KRACHT["zon"], "FFFFFF"),
    )
    obs = []
    for naam, soort, plek, maat, kracht, kleur in lijst:
        ld = bpy.data.lights.new(naam, soort)
        ld.energy = kracht
        ld.color = srgb(kleur)[:3]
        if soort == "AREA":
            ld.shape = "DISK"
            ld.size = maat
        else:   # zon zonder schaduw: gelijkmatig licht op wand en vloer, ook achter de vlakke lampen
            ld.angle = math.radians(30)
        try:
            ld.use_shadow = naam != "studio_wandlicht"
        except Exception:  # noqa: BLE001
            pass
        ob = bpy.data.objects.new(naam, ld)
        bpy.context.scene.collection.objects.link(ob)
        ob.location = Vector(plek) + Vector((mid.x, mid.y, 0))
        doel = mid if naam != "studio_wandlicht" else Vector((mid.x, 1.5 * h, 0.0))
        ob.rotation_euler = (doel - ob.location).to_track_quat("-Z", "Y").to_euler()
        ob.hide_select = True
        obs.append(ob)
    return obs


def wereld():
    sc = bpy.context.scene
    if sc.world is None:
        sc.world = bpy.data.worlds.new("studio")
    w = sc.world
    try:
        w.use_nodes = True
    except Exception:  # noqa: BLE001
        pass
    bg = next((n for n in w.node_tree.nodes if n.type == "BACKGROUND"), None)
    if bg is not None:
        bg.inputs[0].default_value = srgb(KLEUR["wand"])
        bg.inputs[1].default_value = 0.6
    w.color = srgb(KLEUR["wand"])[:3]


def eevee():
    sc = bpy.context.scene
    ids = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
    sc.render.engine = "BLENDER_EEVEE" if "BLENDER_EEVEE" in ids else "BLENDER_EEVEE_NEXT"
    e = sc.eevee
    snel = bool(os.environ.get("CJ_TEST"))
    if snel:
        sc.render.resolution_percentage = 40
    for k, v in (("taa_samples", 8 if snel else 64), ("taa_render_samples", 8 if snel else 64), ("use_shadows", True), ("shadow_ray_count", 1 if snel else 3),
                 ("shadow_step_count", 8), ("use_raytracing", not snel), ("use_gtao", True), ("gtao_distance", 6.0),
                 ("fast_gi_distance", 6.0), ("use_soft_shadows", True)):
        if hasattr(e, k):
            try:
                setattr(e, k, v)
            except Exception:  # noqa: BLE001
                pass
    try:
        sc.view_settings.view_transform = "AgX"
        sc.view_settings.look = "AgX - Medium High Contrast"
    except Exception:  # noqa: BLE001
        pass
    sc.render.film_transparent = False


def bouw(h=220.0, mid=None):
    """Hele studio rond een figuur van h mm hoog met de voeten op z=0."""
    mid = mid or Vector((0, 0, h / 2))
    achterwand(h, z0=-0.06 * h)   # vloer onder het podium, niet in hetzelfde vlak (geen geflikker)
    podium(h)
    lampen(h, mid)
    wereld()
    eevee()


def naadloos(delen):
    """De passingkleuren van de add-on (groen 'Good fit', donker 'Flex slot', grijs restmateriaal) per deel terug naar
    de kleur van het dichtstbijzijnde gewone vlak van dat deel, zoals een print in de kleur van het lichaamsdeel. Alleen
    voor de renders; in het Blender-scherm blijven de echte kleuren van de add-on. Kogel, kom en spleet blijven zichtbaar
    als vorm."""
    from mathutils.kdtree import KDTree
    for o in delen:
        me = o.data
        mats = list(me.materials)
        cj = {i for i, m in enumerate(mats) if m is not None and (m.name.startswith("Click Joints") or m.name.startswith("pla_grijs"))}
        if not cj:
            continue
        gewoon = [p for p in me.polygons if p.material_index not in cj]
        if not gewoon:
            continue
        kd = KDTree(len(gewoon))
        for i, p in enumerate(gewoon):
            kd.insert(p.center, i)
        kd.balance()
        for p in me.polygons:
            if p.material_index in cj:
                _c, i, _d = kd.find(p.center)
                p.material_index = gewoon[i].material_index
        me.update()


def plastic(delen, gewricht="naadloos"):
    """Materialen van het figuur als geprint plastic: glans, een dunne laklaag en fijne laaglijnen (0,4 mm) als reliëf.
    De kleuren blijven die van het figuur. gewricht="naadloos": passingkleuren weg (zie naadloos); "contrast": één
    roomwitte kleur voor kogel, kom en scharnier, zoals een print met de gewrichten in een andere kleur."""
    if gewricht == "naadloos":
        naadloos(delen)
    gezien = set()
    for o in delen:
        for i, m in enumerate(o.data.materials):
            if m is None:
                continue
            if gewricht == "contrast" and (m.name.startswith("Click Joints") or m.name.startswith("pla_grijs")):
                nieuw = bpy.data.materials.get("studio_gewricht") or bpy.data.materials.new("studio_gewricht")
                nieuw.diffuse_color = srgb(KLEUR["gewricht"])
                o.data.materials[i] = nieuw
                m = nieuw
            if m.name in gezien:
                continue
            gezien.add(m.name)
            kleur = tuple(m.diffuse_color)
            if not m.name.startswith(("toy_", "studio_", "Click Joints")) and m.node_tree:
                b0 = next((n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
                if b0 is not None:
                    kleur = tuple(b0.inputs["Base Color"].default_value)
            _plastic_nodes(_mat(m.name), kleur)


def _plastic_nodes(m, kleur):
    nt = m.node_tree
    for n in list(nt.nodes):
        if n.type not in ("OUTPUT_MATERIAL",):
            nt.nodes.remove(n)
    uit = next((n for n in nt.nodes if n.type == "OUTPUT_MATERIAL"), None) or nt.nodes.new("ShaderNodeOutputMaterial")
    b = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(b.outputs[0], uit.inputs["Surface"])
    b.inputs["Base Color"].default_value = kleur
    _zet(b, "Roughness", 0.36)
    _zet(b, "Coat Weight", 0.25)
    _zet(b, "Coat Roughness", 0.12)
    _zet(b, "Specular IOR Level", 0.5)
    _zet(b, "Subsurface Weight", 0.04)
    # laaglijnen: golf langs z in wereldmaat, 0,4 mm per laag, heel licht reliëf
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    mul.inputs[1].default_value = 2 * math.pi / 0.4
    sin = nt.nodes.new("ShaderNodeMath")
    sin.operation = "SINE"
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.06
    if "Distance" in bump.inputs:
        bump.inputs["Distance"].default_value = 0.03
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    nt.links.new(geo.outputs["Position"], sep.inputs[0])
    nt.links.new(sep.outputs["Z"], mul.inputs[0])
    nt.links.new(mul.outputs[0], sin.inputs[0])
    nt.links.new(sin.outputs[0], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], b.inputs["Normal"])
    m.diffuse_color = kleur
    m.roughness = 0.36
    del tc


# ---------- camera ----------

FORMATEN = {"staand": (1080, 1920), "liggend": (1920, 1080)}


def camera(naam="studio_cam", lens=85.0):
    _weg(naam)
    cd = bpy.data.cameras.new(naam)
    cd.lens = lens
    cd.clip_start, cd.clip_end = 1.0, 50000.0
    cam = bpy.data.objects.new(naam, cd)
    bpy.context.scene.collection.objects.link(cam)
    bpy.context.scene.camera = cam
    return cam


def kader(delen):
    pts = [o.matrix_world @ Vector(c) for o in delen if o.visible_get() for c in o.bound_box]
    lo = Vector((min(q.x for q in pts), min(q.y for q in pts), min(q.z for q in pts)))
    hi = Vector((max(q.x for q in pts), max(q.y for q in pts), max(q.z for q in pts)))
    return lo, hi


def richt(cam, delen, formaat="staand", draai=-30.0, kantel=8.0, vul=0.78, midden_y=0.5, onder=None):
    """Camera zo dat het figuur (de zichtbare delen) `vul` van de beeldhoogte (staand) of -breedte vult, van schuin
    voren (draai in graden om z, 0 = recht van voren) en iets van boven (kantel). midden_y: waar het midden van het
    figuur in beeld staat (0 = onder, 1 = boven); laat ruimte voor ondertitels."""
    sc = bpy.context.scene
    b, hgt = FORMATEN[formaat]
    sc.render.resolution_x, sc.render.resolution_y = b, hgt
    sc.render.resolution_percentage = 40 if os.environ.get("CJ_TEST") else 100
    cd = cam.data
    cd.sensor_fit = "VERTICAL" if formaat == "staand" else "HORIZONTAL"
    cd.sensor_height = cd.sensor_width = 36.0
    lo, hi = kader(delen)
    mid = (lo + hi) / 2
    hoog = (hi.z - lo.z)
    breed = max(hi.x - lo.x, hi.y - lo.y)
    fov = 2 * math.atan(18.0 / cd.lens)
    if formaat == "staand":
        maat = max(hoog, breed * hgt / b) / vul
    else:
        maat = max(hoog * b / hgt, breed) / vul * (hgt / b)
    d = maat / (2 * math.tan(fov / 2))
    if formaat == "liggend":
        d = (hoog / vul) / (2 * math.tan(fov / 2) * hgt / b)
    a, e = math.radians(draai), math.radians(kantel)
    richting = Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))
    cam.location = mid + richting * d
    cam.rotation_euler = (-richting).to_track_quat("-Z", "Y").to_euler()
    cd.shift_x = 0.0
    cd.shift_y = -(midden_y - 0.5) * (1.0 if formaat == "staand" else hgt / b)
    return d


# ---------- renders en scherm ----------

def view3d():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                regio = next(r for r in gebied.regions if r.type == "WINDOW")
                return venster, gebied, regio
    return None, None, None


def render(pad, overlays=False):
    """Render door de camera van wat de 3D-weergave toont (Material Preview met de lampen en wereld van de scene,
    EEVEE). Zo staat de buiging van de add-on (delta-draaiing van deel B) er zeker op."""
    sc = bpy.context.scene
    sc.render.filepath = pad
    venster, gebied, regio = view3d()
    ruimte = gebied.spaces.active
    oud = (ruimte.region_3d.view_perspective, ruimte.shading.type, ruimte.overlay.show_overlays)
    ruimte.region_3d.view_perspective = "CAMERA"
    ruimte.shading.type = "MATERIAL"
    ruimte.shading.use_scene_world = True
    ruimte.shading.use_scene_lights = True
    ruimte.overlay.show_overlays = overlays
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.render.opengl(write_still=True, view_context=True)
    ruimte.region_3d.view_perspective, ruimte.shading.type, ruimte.overlay.show_overlays = oud


def rustig_scherm(ui=1.35, letter=12, studio_licht=True):
    """Opname-scherm: alleen de 3D-weergave met het paneel (zijbalk) van Click Joints. Geen menubalk, statusbalk,
    gereedschapsbalk of kopregel; geen raster, assen, 3D-cursor, tekst linksboven of navigatieknoppen. Groter
    lettertype in het paneel (ui-schaal en lettergrootte, alleen deze sessie). Weergave in Material Preview met de
    lampen en wand van de studio, zodat het scherm er net zo uitziet als de renders."""
    pr = bpy.context.preferences
    pr.view.ui_scale = ui
    pr.view.show_tooltips = False
    pr.view.show_splash = False
    try:
        st = pr.ui_styles[0]
        st.widget.points = letter
        st.panel_title.points = letter + 1
        st.widget_label.points = letter
    except Exception:  # noqa: BLE001
        pass
    pr.system.use_region_overlap = False
    venster, gebied, regio = view3d()
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        try:
            bpy.ops.screen.screen_full_area(use_hide_panels=True)
        except Exception:  # noqa: BLE001
            bpy.ops.screen.screen_full_area()
    venster, gebied, regio = view3d()
    ruimte = gebied.spaces.active
    ruimte.show_region_ui = True
    ruimte.show_region_toolbar = False
    ruimte.show_region_tool_header = False
    ruimte.show_region_header = False
    ruimte.show_gizmo_navigate = False
    ruimte.show_gizmo_tool = False
    ov = ruimte.overlay
    for k in ("show_floor", "show_axis_x", "show_axis_y", "show_axis_z", "show_cursor", "show_text", "show_stats",
              "show_object_origins", "show_relationship_lines", "show_extras", "show_bones"):
        if hasattr(ov, k):
            setattr(ov, k, False)
    ov.show_outline_selected = True
    ruimte.shading.type = "MATERIAL" if studio_licht else "SOLID"
    ruimte.shading.use_scene_world = studio_licht
    ruimte.shading.use_scene_lights = studio_licht
    ruimte.clip_start, ruimte.clip_end = 1.0, 50000.0
    ruimte.lens = 70
    gebied.tag_redraw()
    return venster, gebied


def kijk_naar(punt, afstand, draai=-25.0, kantel=82.0):
    """Gebruikersblik in de 3D-weergave (perspectief) op een punt, voor schermopnames."""
    from mathutils import Euler
    _, gebied, _ = view3d()
    rv = gebied.spaces.active.region_3d
    rv.view_perspective = "PERSP"
    rv.view_rotation = Euler((math.radians(kantel), 0.0, math.radians(draai)), "XYZ").to_quaternion()
    rv.view_distance = afstand
    rv.view_location = Vector(punt)
    gebied.tag_redraw()
