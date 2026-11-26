"""Hoofdbeeld Click Cuts (Beeldmaker, 25 nov 2026, issue #13): voor en na in één beeld.

blender -b --factory-startup --python hoofdbeeld.py -- <click_cuts.zip> <modelmap> <uit.png> <json> [samples] [schaal%]

Links (in beeld): het hele model in één neutrale kleur, met het gouden bouwvolume van de printer (256 mm, Bambu A1)
aan zijn voet: het steekt er ver bovenuit. Rechts: hetzelfde model, gesneden door de echte knop Split to fit van
Click Cuts (de zip van main), met de kleuren per stuk die de add-on geeft en gouden pennen op de plek van de gaten.
Het aantal stukken, de maat van elk stuk en het aantal pennen komen uit de add-on en gaan naar <json>.

Model: Horse Statue 01 van Poly Haven (https://polyhaven.com/a/horse_statue_01), licentie CC0
(https://polyhaven.com/license). Geen AI-beeld. Het beeld is een render, geen foto van een print.
Omgeving: HB_HOOGTE (mm, standaard 520), HB_UIT (uit elkaar, standaard 0.55), HB_PRINTER (standaard A1).
"""
import json
import math
import os
import sys

import bmesh
import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector

a = sys.argv[sys.argv.index("--") + 1:]
ZIP, MODEL, UIT, META = a[0], a[1], a[2], a[3]
SAMPLES = int(a[4]) if len(a) > 4 else 64
SCHAAL = int(a[5]) if len(a) > 5 else 100
HOOGTE = float(os.environ.get("HB_HOOGTE", "520"))
UITF = float(os.environ.get("HB_UIT", "0.55"))
PRINTER = os.environ.get("HB_PRINTER", "A1")
BED = 256.0
BX, BY = 2400, 1350


def log(*t):
    print("[hb]", *t, flush=True)


def srgb(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple((x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4) for x in c) + (1.0,)


def zet(b, naam, w):
    if naam in b.inputs:
        b.inputs[naam].default_value = w


# ------------------------------------------------------------------ model en snijden
def laad():
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    s = bpy.context.scene
    for o in list(s.objects):
        bpy.data.objects.remove(o)
    s.unit_settings.system = "METRIC"
    s.unit_settings.scale_length = 0.001
    s.unit_settings.length_unit = "MILLIMETERS"
    naam = os.path.basename(MODEL.rstrip("/"))
    bpy.ops.import_scene.gltf(filepath=os.path.join(MODEL, f"{naam}_1k.gltf"))
    ob = [o for o in s.objects if o.type == "MESH"][0]
    for o in list(s.objects):
        if o is not ob:
            bpy.data.objects.remove(o)
    ob.name = "Horse"
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix.Identity(4)
    zs = [v.co.z for v in ob.data.vertices]
    ob.data.transform(Matrix.Scale(HOOGTE / (max(zs) - min(zs)), 4))
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.05)
    bm.to_mesh(ob.data)
    bm.free()
    ps = [v.co for v in ob.data.vertices]
    mn = Vector([min(p[i] for p in ps) for i in range(3)])
    mx = Vector([max(p[i] for p in ps) for i in range(3)])
    ob.data.transform(Matrix.Translation(Vector((-(mn.x + mx.x) / 2, -(mn.y + mx.y) / 2, -mn.z))))
    for p in ob.data.polygons:
        p.use_smooth = True
    log("model mm", [round(v, 1) for v in (mx - mn)])
    return ob, mx - mn


def splits(ob):
    s = bpy.context.scene
    voor = ob.copy()
    voor.data = ob.data.copy()
    voor.name = "voor"
    s.collection.objects.link(voor)
    voor.hide_set(True)
    for o in s.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    inst = s.split_joints
    inst.printer = PRINTER
    if os.environ.get("HB_VERBINDER"):  # MAGNET: magneetgaten in plaats van pennen (galerijbeeld Magnets, #137)
        inst.verbinder = os.environ["HB_VERBINDER"]
        inst.magneet = os.environ.get("HB_MAGNEET", "8x3")
    r = bpy.ops.split_joints.split_to_fit()
    voor.hide_set(False)
    stukken = sorted((o for o in s.objects if o.get("sj_stuk")), key=lambda o: o["sj_stuk"])
    bak = [o for o in s.objects if o.get("sj_pennen")]
    log("split", r, len(stukken), "stukken", [o.get("sj_status") for o in stukken])
    return voor, stukken, bak


# ------------------------------------------------------------------ materialen
def plastic(naam, kleur, rough=0.4, coat=0.2):
    m = bpy.data.materials.new(naam)
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = kleur
    b.inputs["Roughness"].default_value = rough
    zet(b, "Coat Weight", coat)
    zet(b, "Coat Roughness", 0.2)
    zet(b, "Subsurface Weight", 0.05)
    zet(b, "Specular IOR Level", 0.5)
    return m


def goud():
    m = bpy.data.materials.new("goud")
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = srgb("FFD25C")
    b.inputs["Metallic"].default_value = 0.9
    b.inputs["Roughness"].default_value = 0.25
    return m


def gloed(naam, hx, kracht):
    m = bpy.data.materials.new(naam)
    nt = m.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    o = nt.nodes.new("ShaderNodeOutputMaterial")
    e = nt.nodes.new("ShaderNodeEmission")
    e.inputs["Color"].default_value = srgb(hx)
    e.inputs["Strength"].default_value = kracht
    nt.links.new(e.outputs[0], o.inputs["Surface"])
    return m


def kleur_stukken(stukken):
    for o in stukken:
        k = tuple(o.color)
        m = plastic(f"m_{o.name}", k)
        o.data.materials.clear()
        o.data.materials.append(m)
        for p in o.data.polygons:
            p.material_index = 0
            p.use_smooth = True


# ------------------------------------------------------------------ uit elkaar en pennen
def uit_elkaar(stukken, verschuif):
    s = bpy.context.scene
    midden = Vector(s.get("sj_midden_mm", (0.0, 0.0, 0.0)))
    d = {}
    for o in stukken:
        r = Vector(o.get("sj_midden_mm", midden)) - midden
        r.y *= 0.6
        r.z *= float(os.environ.get("HB_UIT_Z", "0.55"))
        d[o["sj_stuk"]] = r * UITF
    # alles omhoog tot het laagste stuk op de vloer staat
    laag = min(min((o.matrix_world @ v.co).z for v in o.data.vertices) + d[o["sj_stuk"]].z for o in stukken)
    for o in stukken:
        d[o["sj_stuk"]].z -= laag
        o.delta_location = (0, 0, 0)
        o.location = verschuif + d[o["sj_stuk"]]
    return d


def zilver():
    """Vernikkelde schijfmagneet."""
    m = bpy.data.materials.new("zilver")
    b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = srgb("D9DDE3")
    b.inputs["Metallic"].default_value = 1.0
    b.inputs["Roughness"].default_value = 0.16
    return m


def magneten(stukken, d, verschuif, mat):
    """Een schijfmagneet in elk magneetgat (beide kanten van elke snede), net boven het snijvlak uit."""
    n = 0
    sjabloon = None
    for o in stukken:
        for g in json.loads(o.get("sj_gaten", "[]")):
            if g.get("soort") != "magneet":
                continue
            t = g["diepte"] - 0.3
            if sjabloon is None:
                bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=g["pen_d"] / 2, depth=t)
                sjabloon = bpy.context.active_object
                bv = sjabloon.modifiers.new("afschuin", "BEVEL")
                bv.width, bv.segments = 0.3, 2
                sjabloon.data.materials.append(mat)
                for p in sjabloon.data.polygons:
                    p.use_smooth = abs(p.normal.z) < 0.99
                mg = sjabloon
            else:
                mg = sjabloon.copy()
                bpy.context.scene.collection.objects.link(mg)
            rot = {0: Matrix.Rotation(math.pi / 2, 4, "Y"), 1: Matrix.Rotation(math.pi / 2, 4, "X"),
                   2: Matrix.Identity(4)}[g["as"]]
            uit = Vector((0, 0, 0))
            uit[g["as"]] = g.get("teken", 1)
            plek = Vector(g["p"]) + verschuif + d[o["sj_stuk"]] + uit * (float(os.environ.get("HB_MAG_UIT", "0.6")) - t / 2)
            mg.matrix_world = Matrix.Translation(plek) @ rot
            mg["hb_pen"] = 1
            n += 1
    return n


def pennen(stukken, d, verschuif, mat):
    """Een gouden pen op elk gatenpaar, halverwege tussen de twee stukken in de uiteengetrokken stand."""
    if any(g.get("soort") == "magneet" for o in stukken for g in json.loads(o.get("sj_gaten", "[]"))):
        return magneten(stukken, d, verschuif, zilver())
    gezien = set()
    n = 0
    sjabloon = None
    for o in stukken:
        for g in json.loads(o.get("sj_gaten", "[]")):
            buur = g.get("buur")
            sleutel = (min(o["sj_stuk"], buur), max(o["sj_stuk"], buur), tuple(round(c, 1) for c in g["p"]))
            if sleutel in gezien:
                continue
            gezien.add(sleutel)
            if sjabloon is None:
                bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=g["pen_d"] / 2, depth=12.0)
                sjabloon = bpy.context.active_object
                bv = sjabloon.modifiers.new("afschuin", "BEVEL")
                bv.width, bv.segments = 0.6, 2
                sjabloon.data.materials.append(mat)
                for p in sjabloon.data.polygons:
                    p.use_smooth = True
                pen = sjabloon
            else:
                pen = sjabloon.copy()
                bpy.context.scene.collection.objects.link(pen)
            rot = {0: Matrix.Rotation(math.pi / 2, 4, "Y"), 1: Matrix.Rotation(math.pi / 2, 4, "X"),
                   2: Matrix.Identity(4)}[g["as"]]
            plek = Vector(g["p"]) + verschuif + (d[o["sj_stuk"]] + d.get(buur, d[o["sj_stuk"]])) / 2
            pen.matrix_world = Matrix.Translation(plek) @ rot
            pen["hb_pen"] = 1
            n += 1
    return n


# ------------------------------------------------------------------ studio
def studio(h):
    s = bpy.context.scene
    # vloer en gebogen achterwand, pruim van Dortus
    r, diep, hoog, breed = 1.4 * h, 6 * h, 8 * h, 30 * h
    prof = [(-diep + diep * i / 10, 0.0) for i in range(11)]
    for i in range(1, 17):
        t = math.pi / 2 * i / 16
        prof.append((r * math.sin(t), r * (1 - math.cos(t))))
    prof += [(r, r + (hoog - r) * i / 6) for i in range(1, 7)]
    verts, faces = [], []
    for x in (-breed / 2, breed / 2):
        for (y, z) in prof:
            verts.append((x, y + 0.9 * h, z))
    n = len(prof)
    for i in range(n - 1):
        faces.append((i, i + 1, n + i + 1, n + i))
    me = bpy.data.meshes.new("wand")
    me.from_pydata(verts, [], faces)
    for p in me.polygons:
        p.use_smooth = True
    w = bpy.data.objects.new("wand", me)
    s.collection.objects.link(w)
    sub = w.modifiers.new("glad", "SUBSURF")
    sub.levels = sub.render_levels = 2
    w.data.materials.append(plastic("wand", srgb("2A1B36"), rough=0.9, coat=0.0))
    if s.world is None:
        s.world = bpy.data.worlds.new("w")
    bg = next((n for n in s.world.node_tree.nodes if n.type == "BACKGROUND"), None)
    if bg:
        bg.inputs[0].default_value = srgb("1D1426")
        bg.inputs[1].default_value = 0.08

    def lamp(naam, plek, maat, kracht, kleur, doel):
        ld = bpy.data.lights.new(naam, "AREA")
        ld.shape, ld.size, ld.energy = "DISK", maat, kracht
        ld.color = srgb(kleur)[:3]
        ob = bpy.data.objects.new(naam, ld)
        s.collection.objects.link(ob)
        ob.location = Vector(plek)
        ob.rotation_euler = (doel - ob.location).to_track_quat("-Z", "Y").to_euler()
    k = (h / 436.0) ** 2
    doel = Vector((0, 0, h * 0.45))
    lamp("sleutel", (0.9 * h, -1.8 * h, 1.9 * h), 1.2 * h, 9.0e6 * k, "FFE6C2", doel)
    lamp("vul", (-2.2 * h, -1.4 * h, 0.8 * h), 1.8 * h, 2.2e6 * k, "C2B4FF", doel)
    lamp("rand", (-1.2 * h, 1.3 * h, 1.8 * h), 0.8 * h, 6.0e6 * k, "FFD25C", doel)
    lamp("rand2", (1.6 * h, 1.1 * h, 1.4 * h), 0.8 * h, 5.0e6 * k, "A58CFF", doel)
    ld = bpy.data.lights.new("gloed", "POINT")
    ld.energy, ld.shadow_soft_size = 7.0e6 * k, 0.4 * h
    ld.color = srgb("7A4FB0")[:3]
    g = bpy.data.objects.new("gloed", ld)
    s.collection.objects.link(g)
    g.location = (0.3 * h, 1.3 * h, 0.5 * h)


def bouwvolume(midden):
    bpy.ops.mesh.primitive_cube_add(size=BED, location=Vector(midden) + Vector((0, 0, BED / 2)))
    doos = bpy.context.active_object
    doos.name = "bouwvolume"
    wf = doos.modifiers.new("lijnen", "WIREFRAME")
    wf.thickness = 3.0
    doos.data.materials.append(gloed("lijn", "FFD25C", 7.0))
    # printplaat onder het volume
    bpy.ops.mesh.primitive_cube_add(size=1, location=Vector(midden) + Vector((0, 0, -3.0)))
    p = bpy.context.active_object
    p.name = "plaat"
    p.scale = (BED + 16, BED + 16, 6.0)
    bv = p.modifiers.new("rand", "BEVEL")
    bv.width, bv.segments = 3.0, 3
    p.data.materials.append(plastic("plaat", srgb("1A1420"), rough=0.55, coat=0.0))
    return [doos, p]


# ------------------------------------------------------------------ camera
def punten(objs):
    pts = []
    for o in objs:
        pts += [o.matrix_world @ Vector(c) for c in o.bound_box]
    return pts


def camera(objs, richting, xb, yb, lens=60):
    s = bpy.context.scene
    cd = bpy.data.cameras.new("cam")
    cd.lens = lens
    cd.clip_end = 1e6
    cam = bpy.data.objects.new("cam", cd)
    s.collection.objects.link(cam)
    s.camera = cam
    pts = punten(objs)
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    doel = (lo + hi) / 2
    afst = (hi - lo).length * 1.5
    for _ in range(120):
        cam.location = doel + richting.normalized() * afst
        cam.rotation_euler = (doel - cam.location).to_track_quat("-Z", "Y").to_euler()
        bpy.context.view_layer.update()
        uv = [world_to_camera_view(s, cam, p) for p in pts]
        x0, x1 = min(q.x for q in uv), max(q.x for q in uv)
        y0, y1 = min(q.y for q in uv), max(q.y for q in uv)
        # schuif het beeld naar het doelvak, dan zoom tot het past
        cd.shift_x += ((x0 + x1) / 2 - (xb[0] + xb[1]) / 2) * 0.5
        cd.shift_y += ((y0 + y1) / 2 - (yb[0] + yb[1]) / 2) * 0.5 * BY / BX
        schaal = max((x1 - x0) / (xb[1] - xb[0]), (y1 - y0) / (yb[1] - yb[0]))
        afst *= 1 + (schaal - 1) * 0.5
    log("camera", round(afst), "shift", round(cd.shift_x, 3), round(cd.shift_y, 3),
        "vak", round(x0, 3), round(x1, 3), round(y0, 3), round(y1, 3))
    return cam


def main():
    ob, dims = laad()
    h = dims.z
    voor, stukken, bak = splits(ob)
    for b in bak:
        bpy.data.objects.remove(b)
    kleur_stukken(stukken)
    afstand = float(os.environ.get("HB_AFSTAND", str(BED * 1.55)))
    links, rechts = Vector((-afstand, 0, 0)), Vector((afstand * 0.55, 0, 0))
    voor.location = links
    voor.data.materials.clear()
    voor.data.materials.append(plastic("voor", srgb("C9C2CF"), rough=0.5, coat=0.05))
    d = uit_elkaar(stukken, rechts)
    n_pen = pennen(stukken, d, rechts, goud())
    vol = bouwvolume(links)
    studio(h)
    s = bpy.context.scene
    s.render.engine = "CYCLES"
    s.cycles.device = "CPU"
    s.cycles.samples = SAMPLES
    s.cycles.use_denoising = True
    s.cycles.max_bounces = 6
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = BX, BY, SCHAAL
    s.view_settings.view_transform = "AgX"
    try:
        s.view_settings.look = "AgX - Punchy"
    except Exception:  # noqa: BLE001
        pass
    bpy.context.view_layer.update()
    objs = [voor] + stukken + vol
    zichtbaar = set(objs) | {o for o in s.objects if o.get("hb_pen") or o.name == "wand"}
    for o in s.objects:
        if o.type == "MESH":
            o.hide_render = o not in zichtbaar
    xb = (float(os.environ.get("HB_X0", "0.42")), 0.975)
    camera(objs, Vector((float(os.environ.get("HB_DRAAI", "0.25")), -1.0, float(os.environ.get("HB_KANTEL", "0.18")))),
           xb, (float(os.environ.get("HB_Y0", "0.21")), 0.94), lens=70)
    # posities in het beeld voor de tekstlaag
    cam = s.camera
    def vak(lijst):
        uv = [world_to_camera_view(s, cam, p) for p in punten(lijst)]
        return [min(q.x for q in uv), max(q.x for q in uv), 1 - max(q.y for q in uv), 1 - min(q.y for q in uv)]
    maten = [sorted(round(v, 1) for v in o.dimensions) for o in stukken]
    meta = {"model": "Horse Statue 01, Poly Haven, CC0", "hoogte_mm": round(h, 1),
            "breedte_mm": round(dims.x, 1), "diepte_mm": round(dims.y, 1),
            "printer": PRINTER, "bed_mm": BED, "stukken": len(stukken), "pennen": n_pen,
            "status": [o.get("sj_status") for o in stukken], "grootste_stuk_mm": max(maten, key=lambda m: m[2]),
            "alle_passen": all(m[2] <= BED for m in maten),
            "vak_voor": vak([voor]), "vak_bed": vak(vol[:1]), "vak_na": vak(stukken)}
    with open(META, "w") as f:
        json.dump(meta, f, indent=1)
    log("meta", json.dumps(meta))
    s.render.filepath = UIT
    bpy.ops.render.render(write_still=True)
    log("klaar", UIT)


main()
