"""Merkbeelden voor de splitser (Dortus, 23 nov 2026, merk-agent).

Snijdt een CC0-model (Poly Haven, lion_head) met vlakke sneden in stukken die elk op een printbed van 256 mm passen,
boort gaten voor losse pennen, schuift de stukken uit elkaar en rendert ze in de studio (gebogen achterwand uit
commercie/filmpjes/studio/studio.py) in twee stijlen.

Let op, eerlijk: dit is gemaakt met Blender-booleans (Manifold), niet met de add-on zelf (die bestaat nog niet). Het
beeld laat zien wat de add-on moet doen. Zodra de add-on werkt: opnieuw renderen met de echte uitkomst.

Gebruik:
  blender -b --factory-startup --python splits_scene.py -- <modelmap> <uitmap> <stijl a|b> <shot> [samples] [schaal]
shot: cover | heel | delen | bed | pen | paneel
"""
import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
MODEL = argv[0] if len(argv) > 0 else "/dev/shm/mod/lion_head"
UIT = argv[1] if len(argv) > 1 else "/dev/shm/w/uit"
STIJL = argv[2] if len(argv) > 2 else "a"
SHOT = argv[3] if len(argv) > 3 else "cover"
SAMPLES = int(argv[4]) if len(argv) > 4 else 32
SCHAAL = int(argv[5]) if len(argv) > 5 else 50
STUDIO = os.environ.get("STUDIO_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..",
                                                    "commercie", "filmpjes", "studio"))
sys.path.insert(0, os.path.abspath(STUDIO))
import studio as S  # noqa: E402

os.makedirs(UIT, exist_ok=True)
BED = 256.0          # mm, printbed (Bambu X1/P1-maat); elk stuk moet hierin passen
PEN_R = 5.0          # straal pen in mm
PEN_L = 28.0         # lengte pen
SPELING = 0.2        # extra straal van het gat
HOOGTE = 436.0       # mm, hoogte van het model (de leeuwenkop van Poly Haven is 0,436 m)

# Kleursets (sRGB hex). a = Pop (heldere studio), b = Nacht (Dortus: pruim, goud, lila).
STIJLEN = {
    "a": {
        "vloer": "7F95FF", "wand": "2443E6",
        "delen": ["FFC83D", "FF5B3A", "FF7AB6", "2ED3A8", "FF9A3C", "F7F4EE", "8C6CFF"],
        "pen": "FFFFFF", "snijvlak_licht": 0.35,
        "lucht": "C9D3FF",
    },
    "b": {
        "vloer": "2E1F3A", "wand": "4A2E57",
        "delen": ["FFD25C", "A58CFF", "FF6B5B", "FF9A3C", "C9B9FF", "FFF4E0", "47D7B4"],
        "pen": "FFD25C", "snijvlak_licht": 0.3,
        "lucht": "1D1426",
    },
}
ST = STIJLEN[STIJL]


def log(*a):
    print("[merk]", *a, flush=True)


# ---------------------------------------------------------------- model
def laad_model():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.unit_settings.system = "METRIC"
    sc.unit_settings.scale_length = 0.001
    naam = os.path.basename(MODEL.rstrip("/"))
    bpy.ops.import_scene.gltf(filepath=os.path.join(MODEL, f"{naam}_1k.gltf"))
    ob = [o for o in sc.objects if o.type == "MESH"][0]
    for o in list(sc.objects):
        if o is not ob:
            bpy.data.objects.remove(o)
    ob.name = "model"
    # schaal naar mm, voeten op z=0, midden op x=y=0
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    zs = [v.co.z for v in ob.data.vertices]
    ob.data.transform(Matrix.Scale(HOOGTE / (max(zs) - min(zs)), 4))
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.05)
    bm.to_mesh(ob.data)
    bm.free()
    xs = [v.co for v in ob.data.vertices]
    mn = Vector((min(c.x for c in xs), min(c.y for c in xs), min(c.z for c in xs)))
    mx = Vector((max(c.x for c in xs), max(c.y for c in xs), max(c.z for c in xs)))
    ob.data.transform(Matrix.Translation(Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z))))
    for p in ob.data.polygons:
        p.use_smooth = True
    log("model", naam, "maat mm", tuple(round(v, 1) for v in (mx - mn)))
    return ob, mx - mn


# ---------------------------------------------------------------- snijden
def snij(ob, punt, normaal, naam_a, naam_b):
    """Knip ob met het vlak (punt, normaal) in twee: a aan de kant van -normaal, b aan +normaal. Boolean Manifold
    met een grote doos; het snijvlak krijgt materiaal 1 (snijvlak)."""
    normaal = Vector(normaal).normalized()
    groot = 4000.0
    res = []
    for kant, naam in ((-1, naam_a), (1, naam_b)):
        bpy.ops.mesh.primitive_cube_add(size=groot)
        doos = bpy.context.active_object
        rot = normaal.to_track_quat("Z", "Y").to_matrix().to_4x4()
        doos.matrix_world = Matrix.Translation(Vector(punt) + normaal * (kant * -groot / 2)) @ rot
        # doos ligt aan de andere kant: verschil laat de gewenste helft over
        kopie = ob.copy()
        kopie.data = ob.data.copy()
        kopie.name = naam
        bpy.context.scene.collection.objects.link(kopie)
        if "snijvlak" not in [m.name if m else "" for m in kopie.data.materials]:
            pass
        doos.data.materials.clear()
        doos.data.materials.append(snijmat())
        m = kopie.modifiers.new("snij", "BOOLEAN")
        m.operation = "DIFFERENCE"
        m.object = doos
        try:
            m.solver = "MANIFOLD"
        except Exception:  # noqa: BLE001
            m.solver = "EXACT"
        bpy.context.view_layer.objects.active = kopie
        bpy.ops.object.modifier_apply(modifier=m.name)
        bpy.data.objects.remove(doos)
        res.append(kopie)
    bpy.data.objects.remove(ob)
    return res


_SNIJ = None


def snijmat():
    global _SNIJ
    if _SNIJ is None:
        _SNIJ = bpy.data.materials.new("snijvlak")
    return _SNIJ


def maat(ob):
    cs = [ob.matrix_world @ v.co for v in ob.data.vertices]
    mn = Vector((min(c.x for c in cs), min(c.y for c in cs), min(c.z for c in cs)))
    mx = Vector((max(c.x for c in cs), max(c.y for c in cs), max(c.z for c in cs)))
    return mn, mx


def binnen(bvh, p):
    loc, nor, _i, _d = bvh.find_nearest(p)
    return loc is not None and (p - loc).dot(nor) < 0


ORIG_BVH = None


def pen_plekken(ob, punt, normaal, n=2, filt=None):
    """Plekken op het snijvlak waar een pen past: genoeg vlees aan beide kanten (half de pen plus wand) en opzij.
    Gemeten op het hele, ongesneden model (ORIG_BVH)."""
    bvh = ORIG_BVH
    normaal = Vector(normaal).normalized()
    u = normaal.orthogonal().normalized()
    v = normaal.cross(u).normalized()
    goed = []
    stap = 5.0
    for i in range(-50, 51):
        for j in range(-50, 51):
            p = Vector(punt) + u * (i * stap) + v * (j * stap)
            if not binnen(bvh, p):
                continue
            ok = True
            for d in (normaal, -normaal):
                hit = bvh.ray_cast(p, d)
                if hit[0] is None or hit[3] < PEN_L / 2 + 4.0:
                    ok = False
                    break
            if not ok:
                continue
            for k in range(12):
                a = 2 * math.pi * k / 12
                d = u * math.cos(a) + v * math.sin(a)
                for dz in (-PEN_L / 2 - 1, -PEN_L / 4, 0.0, PEN_L / 4, PEN_L / 2 + 1):
                    q = p + normaal * dz
                    hit = bvh.ray_cast(q, d)
                    if hit[0] is None or hit[3] < PEN_R + 12.0:
                        ok = False
                        break
                if not ok:
                    break
            if ok and (filt is None or filt(p)):
                goed.append(p)
    if not goed:
        return []
    if n >= 400:
        return goed
    # verst uit elkaar: begin bij het punt het verst van het midden
    mid = sum(goed, Vector()) / len(goed)
    gekozen = [max(goed, key=lambda q: (q - mid).length)]
    while len(gekozen) < n:
        q = max(goed, key=lambda q: min((q - g).length for g in gekozen))
        if min((q - g).length for g in gekozen) < 30:
            break
        gekozen.append(q)
    return gekozen


def maak_pen(p, normaal, naam, straal=PEN_R, lengte=PEN_L, afschuin=True):
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=straal, depth=lengte)
    pen = bpy.context.active_object
    pen.name = naam
    rot = Vector(normaal).to_track_quat("Z", "Y").to_matrix().to_4x4()
    pen.matrix_world = Matrix.Translation(p) @ rot
    if afschuin:
        b = pen.modifiers.new("rand", "BEVEL")
        b.width = 1.0
        b.segments = 3
        b.limit_method = "ANGLE"
    bpy.ops.object.shade_smooth()
    return pen


def boor(ob, pennen):
    for pen in pennen:
        gat = maak_pen(pen.matrix_world.translation, pen.matrix_world.to_3x3() @ Vector((0, 0, 1)), "gat",
                       straal=PEN_R + SPELING, lengte=PEN_L + 1.0, afschuin=False)
        gat.data.materials.append(snijmat())
        m = ob.modifiers.new("gat", "BOOLEAN")
        m.operation = "DIFFERENCE"
        m.object = gat
        try:
            m.solver = "MANIFOLD"
        except Exception:  # noqa: BLE001
            m.solver = "EXACT"
        bpy.context.view_layer.objects.active = ob
        bpy.ops.object.modifier_apply(modifier=m.name)
        bpy.data.objects.remove(gat)


def snijplan(h, w):
    """Snijplan voor de leeuwenkop (436 hoog, 321 breed): het gezicht blijft heel. Voet onderaan, gezicht en kruin in
    het midden, de manen links en rechts in twee stukken. Elk stuk past op een bed van 256 mm."""
    xm = 0.245 * w
    return [
        ("model", (0, 0, 0.25 * h), (0.0, 0.1, 1.0), "d_voet", "d_rest"),
        ("d_rest", (-xm, 0, 0.6 * h), (1.0, 0.22, 0.0), "d_manen_l", "d_rest2"),
        ("d_rest2", (xm, 0, 0.6 * h), (1.0, -0.22, 0.0), "d_kern", "d_manen_r"),
        ("d_kern", (0, 0, 0.745 * h), (0.0, -0.14, 1.0), "d_gezicht", "d_kruin"),
        ("d_manen_l", (-xm, 0, 0.57 * h), (0.15, 0.0, 1.0), "d_manen_lo", "d_manen_lb"),
        ("d_manen_r", (xm, 0, 0.6 * h), (-0.15, 0.0, 1.0), "d_manen_ro", "d_manen_rb"),
    ]


def splits(ob, h, w):
    stukken = {"model": ob}
    vlakken = []
    for bron, punt, n, na, nb in snijplan(h, w):
        n = Vector(n).normalized()
        A, B = snij(stukken.pop(bron), punt, n, na, nb)
        stukken[na], stukken[nb] = A, B
        vlakken.append((Vector(punt), n))
    delen = list(stukken.values())
    for d in delen:
        mn, mx = maat(d)
        log("stuk", d.name, "maat", tuple(round(v) for v in (mx - mn)), "past" if max(mx - mn) <= BED else "TE GROOT")
    return delen, vlakken


def pennen_plaatsen(delen, vlakken):
    """Per snijvlak: geschikte plekken op het hele model, dan per paar buren (allebei raken het vlak daar) twee
    plekken zo ver mogelijk uit elkaar. Pen erin, gaten in allebei."""
    dg = bpy.context.evaluated_depsgraph_get()
    bvhs = {d.name: BVHTree.FromObject(d, dg) for d in delen}
    pennen, paren = [], []
    for punt, n in vlakken:
        kand = pen_plekken(None, punt, n, n=400)
        groepen = {}
        for p in kand:
            raak = [k for k, b in bvhs.items() if b.find_nearest(p)[3] < 0.5]
            if len(raak) == 2:
                groepen.setdefault(tuple(sorted(raak)), []).append(p)
        for (a, b), ps in groepen.items():
            if len(ps) < 3:
                continue
            mid = sum(ps, Vector()) / len(ps)
            g = [max(ps, key=lambda q: (q - mid).length)]
            q = max(ps, key=lambda q: (q - g[0]).length)
            if (q - g[0]).length > 28:
                g.append(q)
            # niet tegen de rand: schuif elk punt 35% naar het midden van de groep
            g = [x.lerp(mid, 0.35) for x in g]
            for i, p in enumerate(g):
                pen = maak_pen(p, n, f"pen_{a}_{b}_{i}")
                pen["a"], pen["b"] = a, b
                pennen.append(pen)
            paren.append((a, b, len(g)))
    namen = {d.name: d for d in delen}
    for d in delen:
        boor(d, [p for p in pennen if d.name in (p["a"], p["b"])])
    return pennen, paren


# ---------------------------------------------------------------- materialen
def plastic_mat(naam, hexkleur, nor_img, snijvlak=False):
    m = bpy.data.materials.new(naam)
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    uit = nt.nodes.new("ShaderNodeOutputMaterial")
    b = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(b.outputs[0], uit.inputs["Surface"])
    kleur = S.srgb(hexkleur)
    if snijvlak:
        kleur = tuple(min(1.0, c * 0.78 + 0.02) for c in kleur[:3]) + (1.0,)
    b.inputs["Base Color"].default_value = kleur
    b.inputs["Roughness"].default_value = 0.42 if not snijvlak else 0.6
    S._zet(b, "Coat Weight", 0.18 if not snijvlak else 0.0)
    S._zet(b, "Coat Roughness", 0.15)
    S._zet(b, "Subsurface Weight", 0.06)
    S._zet(b, "Subsurface Radius", Vector((2.0, 1.2, 0.8)))
    S._zet(b, "Specular IOR Level", 0.5)
    # laaglijnen (0,2 mm laag zoals een echte FDM-print, heel zacht) plus de normal map van het model voor de vacht
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    mul.inputs[1].default_value = 2 * math.pi / 0.6
    sin = nt.nodes.new("ShaderNodeMath")
    sin.operation = "SINE"
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.05 if not snijvlak else 0.0
    bump.inputs["Distance"].default_value = 0.05
    nt.links.new(tc.outputs["Object"], sep.inputs[0])
    nt.links.new(sep.outputs["Z"], mul.inputs[0])
    nt.links.new(mul.outputs[0], sin.inputs[0])
    nt.links.new(sin.outputs[0], bump.inputs["Height"])
    if nor_img is not None and not snijvlak:
        tex = nt.nodes.new("ShaderNodeTexImage")
        tex.image = nor_img
        tex.interpolation = "Cubic"
        nm = nt.nodes.new("ShaderNodeNormalMap")
        nm.inputs["Strength"].default_value = 1.0
        nt.links.new(tc.outputs["UV"], tex.inputs["Vector"])
        nt.links.new(tex.outputs["Color"], nm.inputs["Color"])
        nt.links.new(nm.outputs["Normal"], bump.inputs["Normal"])
    nt.links.new(bump.outputs["Normal"], b.inputs["Normal"])
    m.diffuse_color = kleur
    return m


def pen_mat():
    m = bpy.data.materials.new("pen")
    nt = m.node_tree
    b = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = S.srgb(ST["pen"])
    if STIJL == "b":
        b.inputs["Metallic"].default_value = 0.85
        b.inputs["Roughness"].default_value = 0.22
    else:
        b.inputs["Roughness"].default_value = 0.3
        S._zet(b, "Coat Weight", 0.4)
    return m


def kleur_delen(delen, nor_img):
    volgorde = ["d_gezicht", "d_manen_lo", "d_manen_rb", "d_kruin", "d_manen_ro", "d_manen_lb", "d_voet"]
    delen = sorted(delen, key=lambda d: volgorde.index(d.name) if d.name in volgorde else 99)
    for i, d in enumerate(delen):
        hx = ST["delen"][i % len(ST["delen"])]
        buiten = plastic_mat(f"m_{d.name}", hx, nor_img)
        binnen_m = plastic_mat(f"s_{d.name}", hx, None, snijvlak=True)
        me = d.data
        oud = list(me.materials)
        me.materials.clear()
        me.materials.append(buiten)
        me.materials.append(binnen_m)
        for p in me.polygons:
            mm = oud[p.material_index] if p.material_index < len(oud) else None
            p.material_index = 1 if (mm is not None and mm.name.startswith("snijvlak")) else 0
        me.update()


# ---------------------------------------------------------------- uit elkaar
def uit_elkaar(delen, pennen, h, factor):
    mid = Vector((0, 0, h * 0.5))
    verschuif = {}
    for d in delen:
        mn, mx = maat(d)
        c = (mn + mx) / 2
        r = c - mid
        r.y *= 0.4
        verschuif[d.name] = Vector((r.x * 0.35, r.y * 0.5, r.z * 0.42)) * factor
        d.location += verschuif[d.name]
    for p in pennen:
        a, b = verschuif.get(p["a"], Vector()), verschuif.get(p["b"], Vector())
        p.location += (a + b) / 2
    return verschuif


# ---------------------------------------------------------------- scene
def studio(h, mid):
    S.KLEUR["vloer"] = ST["vloer"]
    S.KLEUR["wand"] = ST["wand"]
    S.achterwand(h * 0.9, z0=-0.0)
    sc = bpy.context.scene
    if sc.world is None:
        sc.world = bpy.data.worlds.new("w")
    w = sc.world
    bg = next((n for n in w.node_tree.nodes if n.type == "BACKGROUND"), None)
    if bg is not None:
        bg.inputs[0].default_value = S.srgb(ST["lucht"])
        bg.inputs[1].default_value = 0.4 if STIJL == "a" else 0.08
    # lampen: groot zacht sleutellicht, vullicht, randlicht
    def lamp(naam, plek, maat_, kracht, kleur):
        ld = bpy.data.lights.new(naam, "AREA")
        ld.shape = "DISK"
        ld.size = maat_
        ld.energy = kracht
        ld.color = S.srgb(kleur)[:3]
        ob = bpy.data.objects.new(naam, ld)
        sc.collection.objects.link(ob)
        ob.location = Vector(plek)
        ob.rotation_euler = (mid - ob.location).to_track_quat("-Z", "Y").to_euler()
        return ob
    k = (h / 436.0) ** 2
    if STIJL == "a":
        lamp("sleutel", (1.5 * h, -1.6 * h, 1.9 * h), 1.2 * h, 1.0e7 * k, "FFF3E4")
        lamp("vul", (-1.9 * h, -1.3 * h, 0.7 * h), 1.8 * h, 1.4e6 * k, "DDE6FF")
        lamp("rand", (-0.9 * h, 1.3 * h, 2.0 * h), 0.8 * h, 6.0e6 * k, "FFFFFF")
    else:
        lamp("sleutel", (1.4 * h, -1.5 * h, 1.8 * h), 1.0 * h, 7.0e6 * k, "FFE2B0")
        lamp("vul", (-1.8 * h, -1.2 * h, 0.6 * h), 1.6 * h, 1.2e6 * k, "B9A6FF")
        lamp("rand", (-1.0 * h, 1.4 * h, 1.9 * h), 0.7 * h, 7.0e6 * k, "FFD25C")
        lamp("rand2", (1.2 * h, 1.2 * h, 1.4 * h), 0.7 * h, 4.0e6 * k, "A58CFF")
        # zachte gloed op de wand achter het model
        ld = bpy.data.lights.new("gloed", "POINT")
        ld.energy = 6.0e6 * k
        ld.shadow_soft_size = 0.3 * h
        ld.color = S.srgb("7A4FB0")[:3]
        ob = bpy.data.objects.new("gloed", ld)
        sc.collection.objects.link(ob)
        ob.location = (0, 1.1 * h, 0.45 * h)


def render_instellingen(bx, by):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = SAMPLES
    sc.cycles.use_denoising = True
    try:
        sc.cycles.denoiser = "OPENIMAGEDENOISE"
    except Exception:  # noqa: BLE001
        pass
    sc.cycles.max_bounces = 6
    sc.render.resolution_x = bx
    sc.render.resolution_y = by
    sc.render.resolution_percentage = SCHAAL
    sc.render.film_transparent = False
    sc.view_settings.view_transform = "AgX"
    try:
        sc.view_settings.look = "AgX - Punchy"
    except Exception:  # noqa: BLE001
        pass
    sc.render.image_settings.file_format = "PNG"


def camera(doel, afstand, hoek_h, hoek_v, lens=70):
    cd = bpy.data.cameras.new("cam")
    cd.lens = lens
    cd.clip_start = 5
    cd.clip_end = 50000
    cam = bpy.data.objects.new("cam", cd)
    bpy.context.scene.collection.objects.link(cam)
    a, e = math.radians(hoek_h), math.radians(hoek_v)
    cam.location = Vector(doel) + Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e))) * afstand
    cam.rotation_euler = (Vector(doel) - cam.location).to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam
    return cam


def kader(objs, c, straal, hh, hv, xbereik, yhalf, lens=60, ymid=0.5):
    """Camera zo zetten dat alle stukken precies in het vak vallen (x van xbereik, y binnen 0,5 +- yhalf)."""
    from bpy_extras.object_utils import world_to_camera_view
    sc = bpy.context.scene
    hoeken = []
    for o in objs:
        mn, mx = maat(o)
        for x in (mn.x, mx.x):
            for y in (mn.y, mx.y):
                for z in (mn.z, mx.z):
                    hoeken.append(Vector((x, y, z)))
    cam = camera(c, straal * 4.0, hh, hv, lens=lens)
    for _ in range(60):
        bpy.context.view_layer.update()
        pts = [world_to_camera_view(sc, cam, p) for p in hoeken]
        x0, x1 = min(p.x for p in pts), max(p.x for p in pts)
        y0, y1 = min(p.y for p in pts), max(p.y for p in pts)
        breed = (x1 - x0) / (xbereik[1] - xbereik[0])
        hoog = (y1 - y0) / (2 * yhalf)
        schaal = max(breed, hoog)
        rechts = cam.matrix_world.to_3x3() @ Vector((1, 0, 0))
        boven = cam.matrix_world.to_3x3() @ Vector((0, 1, 0))
        terug = cam.matrix_world.to_3x3() @ Vector((0, 0, 1))
        d = (cam.location - c).length
        # schuif zodat het midden van de stukken op het midden van het vak valt
        mx_ = (x0 + x1) / 2 - (xbereik[0] + xbereik[1]) / 2
        my_ = (y0 + y1) / 2 - ymid
        breedte_wereld = 2 * d * math.tan(cam.data.angle_x / 2)
        hoogte_wereld = breedte_wereld * sc.render.resolution_y / sc.render.resolution_x
        cam.location += rechts * mx_ * breedte_wereld + boven * my_ * hoogte_wereld
        cam.location += terug * d * (schaal - 1) * 0.7
        if abs(schaal - 1) < 0.01 and abs(mx_) < 0.005 and abs(my_) < 0.005:
            break
    return cam


def emissie_mat(naam, hx, kracht):
    m = bpy.data.materials.new(naam)
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    uit = nt.nodes.new("ShaderNodeOutputMaterial")
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = S.srgb(hx)
    e.inputs["Strength"].default_value = kracht
    nt.links.new(e.outputs[0], uit.inputs["Surface"])
    return m


def bouwvolume(midden_onder, maat_=BED, kleur=None, naam="volume"):
    """Bouwvolume van de printer als doos van gloeiende lijnen plus een heel licht glazen vlak."""
    kleur = kleur or ("FFD23F" if STIJL == "a" else "FFD25C")
    bpy.ops.mesh.primitive_cube_add(size=maat_, location=Vector(midden_onder) + Vector((0, 0, maat_ / 2)))
    doos = bpy.context.active_object
    doos.name = naam
    w = doos.modifiers.new("lijnen", "WIREFRAME")
    w.thickness = 3.2
    w.use_even_offset = False
    doos.data.materials.append(emissie_mat(naam + "_lijn", kleur, 6.0 if STIJL == "b" else 3.0))
    return doos


def plaat(midden, maat_=BED, naam="plaat"):
    """Printplaat: donkere PEI met fijne korrel en een gouden rand."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=Vector(midden) + Vector((0, 0, 3.0)))
    p = bpy.context.active_object
    p.name = naam
    p.scale = (maat_ + 14, maat_ + 14, 6.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    b = p.modifiers.new("rand", "BEVEL")
    b.width = 3.0
    b.segments = 3
    m = bpy.data.materials.new(naam)
    nt = m.node_tree
    bs = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    bs.inputs["Base Color"].default_value = S.srgb("2A2530" if STIJL == "b" else "26262E")
    bs.inputs["Roughness"].default_value = 0.55
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 0.6
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.25
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bs.inputs["Normal"])
    p.data.materials.append(m)
    return p


def leg_op_platen(delen, pennen):
    """Alle stukken rechtop op drie printplaten naast elkaar (zoals je ze print), pennen in een rijtje ervoor."""
    groepen = [["d_gezicht"], ["d_kruin", "d_voet"], ["d_manen_lo", "d_manen_lb", "d_manen_ro", "d_manen_rb"]]
    namen = {d.name: d for d in delen}
    stap = BED + 60
    bpy.context.view_layer.update()
    for gi, g in enumerate(groepen):
        cx = (gi - 1) * stap
        plaat((cx, 0, 0), naam=f"plaat{gi}")
        n = len(g)
        kol = 1 if n == 1 else 2
        for i, nm in enumerate(g):
            d = namen[nm]
            mn, mx = maat(d)
            mid = (mn + mx) / 2
            r, k = divmod(i, kol)
            vak = BED / kol
            doel = Vector((cx - BED / 2 + vak * (k + 0.5), (BED / 2 - vak * (r + 0.5)) if n > 2 else 0.0, 0.0))
            if n == 2:
                doel = Vector((cx - BED / 2 + vak * (k + 0.5), 0.0, 0.0))
            d.location += Vector((doel.x - mid.x, doel.y - mid.y, 6.0 - mn.z))
    for i, p in enumerate(pennen):
        p.matrix_world = Matrix.Translation(Vector((-len(pennen) * 9 + i * 18, -BED / 2 - 70, PEN_R))) @ \
            Matrix.Rotation(math.radians(90), 4, "X")


def main():
    ob, dims = laad_model()
    h = dims.z
    nor_path = os.path.join(MODEL, "textures", os.path.basename(MODEL.rstrip("/")) + "_nor_gl_2k.jpg")
    nor_img = None
    if os.path.exists(nor_path):
        nor_img = bpy.data.images.load(nor_path)
        nor_img.colorspace_settings.name = "Non-Color"
    factor = {"cover": float(os.environ.get("MERK_UITEEN", "0.7")), "delen": 1.25, "heel": 0.0, "bed": 1.0, "pen": 1.5, "samen": 0.035}.get(SHOT, 1.0)
    pennen = []
    delen = [ob]
    global ORIG_BVH
    bm0 = bmesh.new()
    bm0.from_mesh(ob.data)
    ORIG_BVH = BVHTree.FromBMesh(bm0)
    delen, vlakken = splits(ob, h, dims.x)
    pennen, paren = pennen_plaatsen(delen, vlakken)
    log("pennen", len(pennen), paren)
    kleur_delen(delen, nor_img)
    pm = pen_mat()
    for p in pennen:
        p.data.materials.append(pm)
    if SHOT == "heel":
        for p in pennen:
            bpy.data.objects.remove(p)
        pennen = []
        for d in delen:
            d.data.materials[0] = plastic_mat("heel", "F7F4EE" if STIJL == "a" else "FFD25C", nor_img)
            d.data.materials[1] = d.data.materials[0]
        vol = bouwvolume((0, 0, 0))
    elif SHOT == "bed":
        leg_op_platen(delen, pennen)
    elif SHOT == "samen":
        # weer in elkaar: de pennen zitten binnenin, de naden zijn net zichtbaar
        for p in pennen:
            bpy.data.objects.remove(p)
        pennen = []
        uit_elkaar(delen, pennen, h, factor)
    else:
        uit_elkaar(delen, pennen, h, factor)
    studio(h, Vector((0, 0, h * 0.5)))
    objs = delen + pennen
    bpy.context.view_layer.update()
    if SHOT == "heel":
        objs = delen
    mn = Vector((min(maat(o)[0].x for o in objs), min(maat(o)[0].y for o in objs), min(maat(o)[0].z for o in objs)))
    mx = Vector((max(maat(o)[1].x for o in objs), max(maat(o)[1].y for o in objs), max(maat(o)[1].z for o in objs)))
    c = (mn + mx) / 2
    straal = (mx - mn).length / 2
    log("bereik", tuple(round(v) for v in mn), tuple(round(v) for v in mx))
    if SHOT == "cover":
        render_instellingen(2400, 1200)
        kader(objs, c, straal, 30, 8, (0.53, 0.975), 0.465)
    elif SHOT == "bed":
        render_instellingen(1600, 1600)
        objs = objs + [o for o in bpy.data.objects if o.name.startswith("plaat")]
        kader(objs, c, straal, 18, 34, (0.05, 0.95), 0.33, lens=50, ymid=0.42)
    elif SHOT == "pen":
        render_instellingen(1600, 1600)
        nb = [o for o in delen if o.name in ("d_gezicht", "d_manen_ro", "d_manen_rb")]
        nb += [p for p in pennen if p["a"] in ("d_gezicht",) and p["b"] in ("d_manen_ro", "d_manen_rb")]
        kader(nb, c, straal, 62, 6, (0.04, 0.96), 0.41, lens=110, ymid=0.40)
    elif SHOT in ("heel", "samen"):
        render_instellingen(1600, 1600)
        objs = objs + ([vol] if SHOT == "heel" else [])
        kader(objs, c, straal, 28, 9, (0.12, 0.88), 0.355, ymid=0.415)
    else:
        render_instellingen(1600, 1600)
        kader(objs, c, straal, 34, 16, (0.06, 0.94), 0.37, ymid=0.42)
    bpy.context.scene.render.filepath = os.path.join(UIT, f"{STIJL}-{SHOT}.png")
    bpy.ops.render.render(write_still=True)
    log("klaar", bpy.context.scene.render.filepath)


main()
