"""Filmpje Click Joints, filmische opname, grote render ronde 6 (acht shots van Daan, film.md 02:35 en 02:50,
antwoorden 04:33 en 05:35 in ontwerp.md).

Rendert in de echte Blender (achtergrond, Cycles) met de echte add-on: de gewrichten (elleboog en knie), de groene
passingring, de buiging (Bend) en het rood bij te ver zijn echte toestand van Click Joints. Filmwerk: licht, camera,
hout, gloed, de strakke rand van de ring (strakke_ring) en deel B doorzichtig of weg in de inzet "Exploded view".
De look van proef 6 (pop met gestrekte arm en trap, beuken, lichtvlek) staat in film_zes.py; die wordt in main()
over deze definities heen geladen, zoals film_proef.py doet.

    blender -b --python e2e/film_mooi.py -- <uitmap> <zip> <scherf> <aantal_scherven> [snel]

Elke scherf rendert de beelden f met f % aantal == scherf. Uit: <uitmap>/beelden/0001.png ... en
<uitmap>/log-<scherf>.txt. De eindkaart (2 s) rendert Blender niet: de workflow plakt Daans eind.png erachter.
Alleen gratis functies in beeld."""
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
# Shots van Daan (beelden bij 30 per seconde). Daarna nog de eindkaart van 2 s (60 beelden) in de workflow.
SHOTS = [("haak", 15), ("held", 75), ("gewricht", 75), ("buigen", 120), ("uit_elkaar", 75), ("klik_in", 60),
         ("twee", 90)]
EINDKAART = 60
FASE = {"held": 0, "twee": 2}   # volgorde binnen een scherf: eerst de pop zonder gewricht, dan elleboog, dan knie
ACHTERGROND = "#1B1E25"         # film_zes.py zet de kleuren van proef 6
HOUT_LICHT, HOUT_DONKER = "#DDB07A", "#C9985F"
GROEN = (0.0, 0.672, 0.305, 1.0)
ROOD = (1.0, 0.074, 0.074, 1.0)
Z = Vector((0, 0, 1))


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
    return a * a * a * (a * (6 * a - 15) + 10)  # rustig in, rustig uit


def mod(naam):
    m = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    return importlib.import_module(f"{m}.{naam}")


def mat_naam(soort):
    k = mod("kleur")
    return k.PREFIX + k.NAMEN[soort]


def zoek_shot(f):
    begin = 0
    for naam, n in SHOTS:
        if f < begin + n:
            return naam, f - begin, n
        begin += n
    return None, 0, 0


# ---------- bouwstenen voor de pop (film_zes.py bouwt de pop zelf met deze twee) ----------

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


def gesloten(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    fout = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    bm.free()
    return fout


# ---------- materialen, camera, render (pop, hout en licht komen uit film_zes.py) ----------

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


def hout_doorzichtig(ob):
    """Eigen kopie van het hout en van de groene ring voor deel B, met een doorzichtig-schuif. Alleen nog als korte
    overgang naar de inzet zonder B (Daan 05:35). Geeft de Value-nodes terug (0 = dicht, 1 = weg)."""
    bron = bpy.data.materials.get("Film hout")
    if bron is None or not ob.data.materials:
        return None
    waarden = []
    for i, m in enumerate(list(ob.data.materials)):
        if m is not None and m.name in (bron.name, mat_naam("groen")):
            kopie = m.copy()
            kopie.name = m.name + " B"
            ob.data.materials[i] = kopie
            waarden.append(doorzichtig_maken(kopie))
    return waarden or None


def doorzichtig_maken(mat):  # film_zes.py vervangt dit (mengt de hele uitgang, ook de strakke ring)
    nt = mat.node_tree
    uit = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    door, mix, waarde = (nt.nodes.new(t) for t in ("ShaderNodeBsdfTransparent", "ShaderNodeMixShader", "ShaderNodeValue"))
    waarde.outputs[0].default_value = 0.0
    nt.links.new(waarde.outputs[0], mix.inputs[0])
    nt.links.new(bsdf.outputs[0], mix.inputs[1])
    nt.links.new(door.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], uit.inputs["Surface"])
    return waarde


def zet_door(x):
    for w in staat.get("b_door") or []:
        w.outputs[0].default_value = x


def gloed(naam, kleur_rgba, sterkte):
    for n in (naam, naam + " B"):  # de kopie van B gloeit mee
        mat = bpy.data.materials.get(n)
        if mat is None:
            continue
        bsdf = next(x for x in mat.node_tree.nodes if x.type == "BSDF_PRINCIPLED")
        zet_input(bsdf, ["Emission Color", "Emission"], kleur_rgba)
        zet_input(bsdf, ["Emission Strength"], sterkte)


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


staat = {}


def deel(letter):
    return next((o for o in bpy.context.scene.objects if o.get("cj_deel") == letter), None)


def draai(v, as_, graden):
    return Quaternion(as_, math.radians(graden)) @ v


# De rest (shots, camerabanen, label en de hoofdlus) staat in film_shots.py, zodat elk bestand kort blijft.
# Volgorde in main(): eerst film_zes.py (look van proef 6), dan film_shots.py, beide in deze namespace.

def laad(naam):
    pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), naam)
    exec(compile(open(pad).read(), pad, "exec"), globals())  # noqa: S102  (eigen bestand van deze map)


def main():
    laad("film_zes.py")
    laad("film_shots.py")
    hoofdlus()


try:
    main()
except Exception as e:  # noqa: BLE001
    import traceback
    log("MOOI FOUT " + repr(e))
    log(traceback.format_exc())
    sys.exit(1)
