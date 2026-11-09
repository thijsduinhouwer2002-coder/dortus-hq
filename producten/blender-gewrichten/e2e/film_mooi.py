"""Filmpje Click Joints, filmische opname (bericht Thijs 8 nov 23:15: geen braaf schermopname-filmpje).

Rendert in de echte Blender (achtergrond, Cycles) met de echte add-on: het gewricht, de groene passingring,
de buiging (pose) en het rood bij te ver zijn allemaal echte toestand van Click Joints. Alleen licht, camera,
houtmateriaal en de gloed van groen en rood zijn filmwerk.

    blender -b --python e2e/film_mooi.py -- <uitmap> <zip> <scherf> <aantal_scherven> [snel]

Elke scherf rendert de beelden f met f % aantal == scherf, zodat de workflow ze naast elkaar kan draaien.
Uit: <uitmap>/beelden/0001.png ... en <uitmap>/log-<scherf>.txt. Alleen gratis functies in beeld."""
import importlib
import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Quaternion, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
UIT, ZIP, SCHERF, AANTAL = args[0], args[1], int(args[2]), int(args[3])
SNEL = len(args) > 4 and args[4] == "snel"
os.makedirs(os.path.join(UIT, "beelden"), exist_ok=True)
LOG = open(os.path.join(UIT, f"log-{SCHERF:02d}.txt"), "a")

FPS = 30
# Shots (beelden, 30 per seconde): 1 held, 2 gewricht, 3 buigen en rood, 4 uit elkaar. Samen 14,5 s.
SHOTS = [("held", 90), ("gewricht", 90), ("buigen", 150), ("uit_elkaar", 105)]
HOUT_LICHT, HOUT_DONKER = "#C98A4B", "#6E4220"  # ronde 4: dieper, want AgX bleekt fel licht hout
ACHTERGROND = "#1B1E25"


def log(t):
    print(f"[cj-mooi] {t}", flush=True)
    LOG.write(t + "\n")
    LOG.flush()


def srgb_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def kleur(hexa):
    return [srgb_lin(int(hexa[i:i + 2], 16) / 255) for i in (1, 3, 5)]


def glad(a):
    a = min(max(a, 0.0), 1.0)
    return a * a * a * (a * (6 * a - 15) + 10)  # zachter dan smoothstep: rustig in, rustig uit


def mod(naam):
    m = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return importlib.import_module(f"{m}.{naam}")


def zoek_shot(f):
    begin = 0
    for naam, n in SHOTS:
        if f < begin + n:
            return naam, f - begin, n
        begin += n
    return None, 0, 0


# ---------- de tekenpop: zelfde maten als film.py, fijner en met zachte overgangen (voxel-remesh) ----------

def _bol(r, c, schaal=(1, 1, 1), seg=64):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=seg, v_segments=seg // 2, radius=1.0)
    bm.transform(Matrix.Translation(c) @ Matrix.Diagonal((r * schaal[0], r * schaal[1], r * schaal[2], 1.0)))
    return bm


def _staaf(p0, p1, r0, r1):
    p0, p1 = Vector(p0), Vector(p1)
    d = p1 - p0
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=64, radius1=r0, radius2=r1, depth=d.length)
    rot = d.normalized().to_track_quat("Z", "Y").to_matrix().to_4x4()
    bm.transform(Matrix.Translation((p0 + p1) / 2) @ rot)
    return bm


SCHOUDER_R = Vector((-15, 0, 92))
ELLEBOOG = Vector((-31, -2, 80))
ONDERARM = Vector((-0.85, -0.45, 0.2)).normalized()
SNEDE = 11.0
POP_MIDDEN = Vector((-6, 0, 60))
BASIS_RICHTING = Vector((-0.4, 1.0, -0.12)).normalized()


def tekenpop(solver):
    hand = ELLEBOOG + ONDERARM * 30.0
    vormen = [
        _bol(1.0, (0, 0, 108), (6.5, 7.0, 8.5)), _staaf((0, 0, 95), (0, 0, 101), 2.8, 2.6),
        _bol(1.0, (0, 0, 84), (13.0, 8.0, 13.5)), _bol(5.5, (0, 0, 70)), _bol(1.0, (0, 0, 60), (11.0, 7.5, 8.0)),
        _bol(4.6, SCHOUDER_R), _bol(4.6, (15, 0, 92)),
        _staaf(SCHOUDER_R, ELLEBOOG, 4.4, 4.2), _bol(4.6, ELLEBOOG),
        _staaf(ELLEBOOG, hand, 4.2, 3.8), _bol(1.0, hand + ONDERARM * 3.0, (3.0, 3.6, 4.0)),
        _staaf((15, 0, 92), (18, 0, 70), 4.2, 3.6), _bol(4.0, (18, 0, 70)),
        _staaf((18, 0, 70), (19, -1, 49), 3.6, 3.0), _bol(1.0, (19.3, -1, 44), (2.6, 3.2, 5.0)),
        _bol(5.2, (6, 0, 53)), _staaf((6, 0, 53), (6.5, 0, 29), 5.4, 4.3), _bol(4.4, (6.5, 0, 29)),
        _staaf((6.5, 0, 29), (6.5, 0, 6), 4.1, 3.1), _bol(1.0, (6.5, -3, 3), (3.6, 7.0, 3.0)),
        _bol(5.2, (-6, 0, 53)), _staaf((-6, 0, 53), (-9, -3, 30), 5.4, 4.3), _bol(4.4, (-9, -3, 30)),
        _staaf((-9, -3, 30), (-9.5, 1, 6.5), 4.1, 3.1), _bol(1.0, (-9.8, -2, 3), (3.6, 7.0, 3.0)),
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
    if voxel > 0:  # zachte overgangen tussen de delen, zoals een gedraaide houten pop
        rm = basis.modifiers.new("zacht", "REMESH")
        rm.mode, rm.voxel_size, rm.use_smooth_shade = "VOXEL", voxel, True
        sm = basis.modifiers.new("glad", "SMOOTH")
        sm.factor, sm.iterations = 0.5, 4
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(basis.evaluated_get(dg))
    for d in delen:
        bpy.data.objects.remove(d)
    me.shade_smooth()
    me.materials.append(hout_materiaal())
    ob = bpy.data.objects.new("Mannequin", me)
    bpy.context.scene.collection.objects.link(ob)
    return ob


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return fout


# ---------- materialen, licht, camera ----------

def bsdf_van(mat):
    try:
        mat.use_nodes = True
    except Exception:  # noqa: BLE001  (in Blender 5 altijd nodes)
        pass
    return next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def zet_input(bsdf, namen, waarde):
    for n in namen:
        if n in bsdf.inputs:
            bsdf.inputs[n].default_value = waarde
            return


def hout_materiaal():
    mat = bpy.data.materials.new("Film hout")
    bsdf = bsdf_van(mat)
    nt = mat.node_tree
    tex = nt.nodes.new("ShaderNodeTexCoord")
    golf = nt.nodes.new("ShaderNodeTexWave")
    golf.wave_type, golf.rings_direction = "RINGS", "Z"  # bij RINGS telt rings_direction
    golf.inputs["Scale"].default_value = 0.07   # ring om de 2π/(20·0,07) ≈ 4,5 mm, op de pop van 117 mm goed te zien
    golf.inputs["Distortion"].default_value = 2.5
    golf.inputs["Detail"].default_value = 4.0
    ruis = nt.nodes.new("ShaderNodeTexNoise")
    ruis.inputs["Scale"].default_value = 0.6
    meng = nt.nodes.new("ShaderNodeValToRGB")
    meng.color_ramp.elements[0].color = (*kleur(HOUT_DONKER), 1)
    meng.color_ramp.elements[1].color = (*kleur(HOUT_LICHT), 1)
    meng.color_ramp.elements[0].position = 0.35
    meng.color_ramp.elements[1].position = 0.75
    nt.links.new(tex.outputs["Object"], golf.inputs["Vector"])
    nt.links.new(tex.outputs["Object"], ruis.inputs["Vector"])
    som = nt.nodes.new("ShaderNodeMath")
    som.operation = "MULTIPLY_ADD"
    som.inputs[1].default_value = 0.8
    ruis_klein = nt.nodes.new("ShaderNodeMath")  # ruis maal 0,3 (0 tot 0,3), zodat de som rond het midden van de kleurband blijft
    ruis_klein.operation = "MULTIPLY_ADD"
    ruis_klein.inputs[1].default_value = 0.3
    ruis_klein.inputs[2].default_value = 0.0
    nt.links.new(ruis.outputs["Fac"], ruis_klein.inputs[0])
    nt.links.new(golf.outputs["Fac"], som.inputs[0])
    nt.links.new(ruis_klein.outputs[0], som.inputs[2])
    nt.links.new(som.outputs[0], meng.inputs["Fac"])
    nt.links.new(meng.outputs["Color"], bsdf.inputs["Base Color"])
    zet_input(bsdf, ["Roughness"], 0.42)
    zet_input(bsdf, ["Coat Weight", "Clearcoat"], 0.12)
    zet_input(bsdf, ["Coat Roughness", "Clearcoat Roughness"], 0.12)
    mat.diffuse_color = (*kleur(HOUT_LICHT), 1)
    return mat


def hout_doorzichtig(ob):
    """Eigen kopie van het hout voor deel B met een doorzichtig-schuif (Mix met Transparent BSDF).
    Waarom: de rode vlakken van een botsing zitten aan deel A precies waar B erin drukt, dus B dekt ze altijd af
    (ronde 3b: bij 28 graden geen rood te zien). Tijdens het rood wordt B half doorzichtig, zodat je ziet waar
    het botst. Geeft de Value-node terug (0 = dicht, 1 = helemaal doorzichtig)."""
    bron = bpy.data.materials.get("Film hout")
    if bron is None or not ob.data.materials:
        return None
    mat = bron.copy()
    mat.name = "Film hout B"
    nt = mat.node_tree
    uit = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    door = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    waarde = nt.nodes.new("ShaderNodeValue")
    waarde.outputs[0].default_value = 0.0
    nt.links.new(waarde.outputs[0], mix.inputs[0])
    nt.links.new(bsdf.outputs[0], mix.inputs[1])
    nt.links.new(door.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], uit.inputs["Surface"])
    for i, m in enumerate(ob.data.materials):
        if m is bron:
            ob.data.materials[i] = mat
    return waarde


def gloed(naam, kleur_rgba, sterkte):
    mat = bpy.data.materials.get(naam)
    if mat is None:
        return
    bsdf = bsdf_van(mat)
    zet_input(bsdf, ["Emission Color", "Emission"], kleur_rgba)
    zet_input(bsdf, ["Emission Strength"], sterkte)


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
    bg.inputs["Strength"].default_value = 1.0

    def zon(naam, richting, kleur_hex, sterkte, hoek):
        ld = bpy.data.lights.new(naam, "SUN")
        ld.energy, ld.angle, ld.color = sterkte, math.radians(hoek), kleur(kleur_hex)
        ob = bpy.data.objects.new(naam, ld)
        sc.collection.objects.link(ob)
        ob.rotation_euler = (-Vector(richting)).normalized().to_track_quat("-Z", "Y").to_euler()

    zon("Hoofdlicht", (-0.6, -0.9, 0.9), "#FFDDB0", 1.7, 6)   # warm, links voor boven
    zon("Randlicht", (0.7, 1.0, 0.45), "#E6F0FF", 0.9, 3)     # koel, van achteren: lichte rand om de pop
    zon("Vullicht", (0.9, -0.6, 0.2), "#FFF0E0", 0.3, 20)
    # Vloer: donker, licht glanzend, zodat de pop een zachte spiegeling en schaduw heeft
    bm = bmesh.new()
    bmesh.ops.create_circle(bm, cap_ends=True, segments=96, radius=6000)  # rand van de vloer op de horizon, niet als lijn achter de pop
    me = bpy.data.meshes.new("Vloer")
    bm.to_mesh(me)
    bm.free()
    vloer = bpy.data.objects.new("Vloer", me)
    sc.collection.objects.link(vloer)
    mat = bpy.data.materials.new("Film vloer")
    b = bsdf_van(mat)
    zet_input(b, ["Base Color"], (*kleur("#2A2D33"), 1))
    zet_input(b, ["Roughness"], 0.55)
    zet_input(b, ["Specular IOR Level", "Specular"], 0.25)
    me.materials.append(mat)


def camera():
    sc = bpy.context.scene
    cd = bpy.data.cameras.new("Film")
    cd.lens, cd.clip_start, cd.clip_end = 70, 1.0, 10000
    cd.dof.use_dof, cd.dof.aperture_fstop = True, float(os.environ.get("MOOI_FSTOP", "8"))
    cam = bpy.data.objects.new("Film", cd)
    sc.collection.objects.link(cam)
    sc.camera = cam
    return cam


def kijk(cam, oog, doel, lens=70):
    oog = Vector(oog)
    if oog.z < 12.0:
        oog.z = 12.0
    cam.location = oog
    cam.rotation_euler = (Vector(doel) - Vector(oog)).normalized().to_track_quat("-Z", "Y").to_euler()
    cam.data.lens = lens
    cam.data.dof.focus_distance = (Vector(doel) - Vector(oog)).length


def render_instellingen():
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    cy = sc.cycles
    cy.device = "CPU"
    cy.samples = 12 if SNEL else int(os.environ.get("MOOI_SAMPLES", "64"))
    cy.use_adaptive_sampling, cy.adaptive_threshold = True, 0.02
    cy.use_denoising = True
    try:
        cy.denoiser = "OPENIMAGEDENOISE"
    except TypeError:
        pass
    cy.max_bounces, cy.diffuse_bounces, cy.glossy_bounces, cy.transmission_bounces = 6, 3, 3, 2
    sc.render.resolution_x, sc.render.resolution_y = (960, 540) if SNEL else (1920, 1080)
    sc.render.resolution_percentage = 100
    sc.render.image_settings.file_format = "PNG"
    sc.render.film_transparent = False
    try:
        sc.view_settings.view_transform = "AgX"
        sc.view_settings.look = "AgX - Medium High Contrast"
    except TypeError:
        log("AgX-look niet gevonden, standaard blijft")
    gloed_compositor()


def gloed_compositor():
    """Zachte gloed (Glare, Bloom) rond groen en rood. Blender 5 heeft een eigen compositor-boom per scene."""
    sc = bpy.context.scene
    try:
        if hasattr(sc, "compositing_node_group"):
            ng = bpy.data.node_groups.new("Film gloed", "CompositorNodeTree")
            sc.compositing_node_group = ng
            ri = ng.nodes.new("CompositorNodeRLayers")
            gl = ng.nodes.new("CompositorNodeGlare")
            uit = ng.nodes.new("NodeGroupOutput")
            ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
            try:
                gl.inputs["Type"].default_value = "Bloom"
            except Exception:  # noqa: BLE001
                gl.glare_type = "BLOOM"
            for naam, w in (("Threshold", 1.2), ("Strength", 0.6), ("Size", 0.6)):
                if naam in gl.inputs:
                    gl.inputs[naam].default_value = w
            ng.links.new(ri.outputs["Image"], gl.inputs["Image"])
            ng.links.new(gl.outputs["Image"], uit.inputs[0])
        else:
            sc.use_nodes = True
            nt = sc.node_tree
            ri = next(n for n in nt.nodes if n.type == "R_LAYERS")
            co = next(n for n in nt.nodes if n.type == "COMPOSITE")
            gl = nt.nodes.new("CompositorNodeGlare")
            gl.glare_type, gl.threshold, gl.size = "FOG_GLOW", 1.2, 7
            nt.links.new(ri.outputs["Image"], gl.inputs["Image"])
            nt.links.new(gl.outputs["Image"], co.inputs["Image"])
        log("gloed: compositor aan")
    except Exception as e:  # noqa: BLE001
        if hasattr(sc, "compositing_node_group"):
            sc.compositing_node_group = None  # halve boom zou een zwart beeld geven
        log(f"gloed: compositor lukte niet ({e}), render zonder gloed")


# ---------- het gewricht (echte add-on) ----------

staat = {}


def deel(letter):
    return next((o for o in bpy.context.scene.objects if o.get("cj_deel") == letter), None)


def plaats_gewricht(pop):
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = False
    inst.toon_bereik = False
    inst.pose_graden = 0.0
    inst.speling_mm, inst.as_bron, inst.kogel_auto = 0.2, "CURSOR", True
    figuren.zet_cursor(tuple(ELLEBOOG + ONDERARM * SNEDE), tuple(ONDERARM))
    figuren.maak_actief(pop)
    uitslag = bpy.ops.click_joints.plaats()
    bpy.context.view_layer.update()
    a, b = deel("A"), deel("B")
    pop.hide_render = True  # zo ziet de gebruiker het ook: de add-on verbergt het origineel (hide_set)
    paneel = mod("paneel")
    log(f"plaats: {uitslag}, kogel {inst.kogel_mm} mm, passing {a.get('cj_passing')}, wand {a.get('cj_wand_mm')}, "
        f"tekst {paneel.buig_tekst(a)}, bereik {[round(x, 1) for x in a.get('cj_buig_graden', [])]}")
    log(f"deel A foute randen {gesloten(a)}, deel B foute randen {gesloten(b)}")
    as_ = Vector(a["cj_as"]).normalized()
    rich = mod("uit_elkaar").richtingen(as_)
    k = max(range(len(rich)), key=lambda i: rich[i].z)
    inst.pose_richting = str(k)
    kijk_r = as_.cross(rich[k]).normalized()
    if kijk_r.dot(BASIS_RICHTING) < 0:
        kijk_r = -kijk_r
    staat.update(as_=as_, rich=rich[k], c=Vector(a["cj_centrum"]), r=float(a["cj_kogel_r"]), kijk_r=kijk_r,
                 grens=paneel.richting_graden(a, k), los=as_ * mod("uit_elkaar").afstand(b))
    staat["b_door"] = hout_doorzichtig(b)
    log(f"richting {k}, grens {staat['grens']}, B doorzichtig {'ja' if staat['b_door'] else 'NEE'}")


def draai(v, as_, graden):
    return Quaternion(as_, math.radians(graden)) @ v


# ---------- per beeld ----------

GROEN = (0.0, 0.672, 0.305, 1.0)
ROOD = (1.0, 0.074, 0.074, 1.0)


def pose_curve(t):
    """Daans buiging: 0 -> 15 (1,5 s), stil 0,5 s, 15 -> 28 (1,2 s), stil 0,8 s, terug naar 15 (1,0 s)."""
    if t < 1.5:
        return 15 * glad(t / 1.5)
    if t < 2.0:
        return 15.0
    if t < 3.2:
        return 15 + 13 * glad((t - 2.0) / 1.2)
    if t < 4.0:
        return 28.0
    return 28 - 13 * glad((t - 4.0) / 1.0)


def zet_beeld(cam, naam, i, n):
    t, a = i / FPS, i / max(n - 1, 1)
    inst = bpy.context.scene.click_joints
    z = Vector((0, 0, 1))
    if naam == "held":  # langzaam om de pop heen, laag standpunt, de pop groot en heldhaftig
        r = draai(Vector((BASIS_RICHTING.x, BASIS_RICHTING.y, 0)).normalized(), z, -28 + 30 * glad(a))
        oog = POP_MIDDEN + r * 430 + Vector((0, 0, -22 + 12 * a))  # z 38 tot 50: laag standpunt, boven de vloer
        kijk(cam, oog, POP_MIDDEN + Vector((0, 0, 2)), lens=50)
        return
    c, rr, kr = staat["c"], staat["r"], staat["kijk_r"]
    if naam == "gewricht":  # rijdt naar de elleboog; de groene ring gloeit op en zakt naar een rustige gloed
        p = glad(t / 2.4)
        r0 = draai(BASIS_RICHTING, z, 2)
        rich = r0.slerp(kr, p) if hasattr(r0, "slerp") else r0.lerp(kr, p).normalized()
        doel = POP_MIDDEN.lerp(c + staat["as_"] * 3, p) + Vector((0, 0, 6)) * (1 - p)
        afst = 430 + (75 * rr - 430) * p
        kijk(cam, doel + rich * afst, doel, lens=50 + 10 * p)
        piek = math.exp(-((t - 1.1) ** 2) / 0.18)
        gloed(mat_naam("groen"), GROEN, 0.6 + 7.0 * piek if t > 0.4 else 0.0)
        return
    if naam == "buigen":  # van opzij; de onderarm buigt, voorbij de grens kleurt het rood en gloeit het
        g = pose_curve(t)
        inst.pose_graden = round(g, 2)
        rich = draai(kr, staat["as_"].cross(kr).normalized(), -6 + 10 * a)
        doel = c + staat["as_"] * 7
        kijk(cam, doel + rich * (85 * rr), doel, lens=60)
        gloed(mat_naam("groen"), GROEN, 0.6)
        voorbij = max(0.0, g - staat["grens"])
        sterk = min(1.0, voorbij / 3.0)
        gloed(mat_naam("rood"), ROOD, (6.0 + 3.0 * math.sin(t * 11)) * sterk)
        if staat.get("b_door") is not None:
            staat["b_door"].outputs[0].default_value = 0.6 * sterk
        if i in (0, 98, 140):
            a_ob = deel("A")
            rood = sum(1 for p in a_ob.data.polygons if a_ob.data.materials[p.material_index]
                       and a_ob.data.materials[p.material_index].name == mat_naam("rood"))
            log(f"buigen beeld {i}: pose {g:.1f} rode vlakken A {rood}")
        return
    if naam == "uit_elkaar":  # deel B schuift van de kogel, de camera draait mee zodat je kogel en kom ziet
        if inst.pose_graden != 0.0:
            inst.pose_graden = 0.0
        b = deel("B")
        p = glad(t / 1.3)
        b.delta_location = staat["los"] * 1.25 * p
        as_ = staat["as_"]
        rich = (kr * math.cos(math.radians(50 * glad(t / 3.0))) + as_ * math.sin(math.radians(50 * glad(t / 3.0))))
        doel = c + as_ * (staat["los"].length * 0.6 * p)
        kijk(cam, doel + rich.normalized() * (70 * rr), doel, lens=60)
        gloed(mat_naam("groen"), GROEN, 0.6 + 1.5 * math.exp(-((t - 1.3) ** 2) / 0.1))
        gloed(mat_naam("rood"), ROOD, 0.0)
        if staat.get("b_door") is not None:
            staat["b_door"].outputs[0].default_value = 0.0


def mat_naam(soort):
    k = mod("kleur")
    return k.PREFIX + k.NAMEN[soort]


def main():
    log(f"Blender {bpy.app.version_string}, scherf {SCHERF}/{AANTAL}, snel {SNEL}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    figuren.mm_scene()
    render_instellingen()
    licht_en_wereld()
    cam = camera()
    solver = mod("gewricht").solver_naam()
    pop = tekenpop(solver)
    log(f"pop: {len(pop.data.polygons)} vlakken, foute randen {gesloten(pop)}, solver {solver}")
    totaal = sum(n for _, n in SHOTS)
    mijn = [f for f in range(totaal) if f % AANTAL == SCHERF]
    if os.environ.get("MOOI_ALLEEN"):
        mijn = [int(x) for x in os.environ["MOOI_ALLEEN"].split(",")]
    geplaatst = False
    for f in sorted(mijn, key=lambda f: (zoek_shot(f)[0] != "held", f)):
        naam, i, n = zoek_shot(f)
        if naam != "held" and not geplaatst:
            plaats_gewricht(pop)
            geplaatst = True
        zet_beeld(cam, naam, i, n)
        bpy.context.view_layer.update()
        bpy.context.scene.render.filepath = os.path.join(UIT, "beelden", f"{f + 1:04d}.png")
        bpy.ops.render.render(write_still=True)
        log(f"beeld {f + 1} ({naam} {i}) klaar")
    log("MOOI KLAAR")


try:
    main()
except Exception as e:  # noqa: BLE001
    import traceback
    log("MOOI FOUT " + repr(e))
    log(traceback.format_exc())
    sys.exit(1)
