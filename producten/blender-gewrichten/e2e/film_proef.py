"""Snelle proef voor het filmische filmpje: waarom rendert het hout grijs, en waarom zie je het rood niet?

Laadt film_mooi.py zonder de hoofdlus (zelfde pop, licht, camera en materialen) en rendert een paar kleine
beelden in varianten, met een log van de materialen. Zo hoeven we niet 40 minuten op de hele film te wachten.

    blender -b --python e2e/film_proef.py -- <uitmap> <zip>

Uit: <uitmap>/proef-*.png en <uitmap>/proef.txt."""
import os
import sys

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[sys.argv.index("--") + 1:]
UIT, ZIP = args[0], args[1]
os.makedirs(UIT, exist_ok=True)
sys.argv = sys.argv[:sys.argv.index("--") + 1] + [UIT, ZIP, "0", "1", "snel"]

bron = open(os.path.join(HIER, "film_mooi.py")).read().split("\ntry:\n    main()")[0]
F = {"__file__": os.path.join(HIER, "film_mooi.py"), "__name__": "film_mooi"}
exec(compile(bron, F["__file__"], "exec"), F)  # noqa: S102  (eigen bestand, zonder de hoofdlus)
LOGF = open(os.path.join(UIT, "proef.txt"), "w")


def log(t):
    print(f"[cj-proef] {t}", flush=True)
    LOGF.write(t + "\n")
    LOGF.flush()


def beschrijf(ob):
    log(f"object {ob.name}: {len(ob.data.polygons)} vlakken, vakken {[m.name if m else None for m in ob.data.materials]}")
    gebruikt = {}
    for p in ob.data.polygons:
        gebruikt[p.material_index] = gebruikt.get(p.material_index, 0) + 1
    log(f"  vlakken per vak {dict(sorted(gebruikt.items()))}")
    for m in ob.data.materials:
        if m is None or m.node_tree is None:
            continue
        nt = m.node_tree
        log(f"  materiaal {m.name}: nodes {[n.bl_idname for n in nt.nodes]}")
        for lk in nt.links:
            log(f"    {lk.from_node.bl_idname}.{lk.from_socket.name} -> {lk.to_node.bl_idname}.{lk.to_socket.name}")
        b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
        if b is not None:
            bc = b.inputs["Base Color"]
            log(f"    Base Color gekoppeld {bc.is_linked}, waarde {tuple(round(x, 3) for x in bc.default_value)}")
        uit = [n for n in nt.nodes if n.type == "OUTPUT_MATERIAL"]
        log(f"    uitgangen {[(n.name, n.is_active_output, n.target) for n in uit]}")


def render(naam):
    sc = bpy.context.scene
    sc.render.filepath = os.path.join(UIT, f"proef-{naam}.png")
    bpy.ops.render.render(write_still=True)
    log(f"render {naam} klaar")


def main():
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    F["figuren"].mm_scene()
    F["render_instellingen"]()
    bpy.context.scene.cycles.samples = 16
    F["licht_en_wereld"]()
    cam = F["camera"]()
    pop = F["tekenpop"](F["mod"]("gewricht").solver_naam())
    log(f"engine {bpy.context.scene.render.engine}, view {bpy.context.scene.view_settings.view_transform}, "
        f"look {bpy.context.scene.view_settings.look}")
    beschrijf(pop)
    F["zet_beeld"](cam, "held", 60, 90)
    bpy.context.view_layer.update()
    render("1-hout-nu")

    mat = bpy.data.materials["Film hout"]
    nt = mat.node_tree
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    bc = bsdf.inputs["Base Color"]
    oud = [lk for lk in nt.links if lk.to_socket == bc]
    van = oud[0].from_socket if oud else None
    for lk in oud:
        nt.links.remove(lk)
    bc.default_value = (*F["kleur"](F["HOUT_LICHT"]), 1)
    render("2-effen-bruin")

    uit = next(n for n in nt.nodes if n.type == "OUTPUT_MATERIAL")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*F["kleur"](F["HOUT_LICHT"]), 1)
    oud_surface = uit.inputs["Surface"].links[0].from_socket if uit.inputs["Surface"].is_linked else None
    nt.links.new(em.outputs[0], uit.inputs["Surface"])
    render("3-alleen-gloed-bruin")

    if oud_surface is not None:
        nt.links.new(oud_surface, uit.inputs["Surface"])
    if van is not None:
        nt.links.new(van, bc)
    nt.nodes.remove(em)

    F["plaats_gewricht"](pop)
    a, b = F["deel"]("A"), F["deel"]("B")
    beschrijf(a)
    beschrijf(b)
    F["zet_beeld"](cam, "buigen", 98, 150)
    bpy.context.view_layer.update()
    rood = len(a.get("cj_rood_vlakken", [])) // 2
    door = F["staat"].get("b_door")
    log(f"buigen 28: rode vlakken {rood}, B doorzichtig waarde {door.outputs[0].default_value if door else None}")
    render("4-buigen-28")
    bpy.context.scene.click_joints.pose_graden = 40.0
    bpy.context.view_layer.update()
    log(f"buigen 40: rode vlakken {len(a.get('cj_rood_vlakken', [])) // 2}")
    render("5-buigen-40")
    log("PROEF KLAAR")


try:
    main()
except Exception as e:  # noqa: BLE001
    import traceback
    log("PROEF FOUT " + repr(e))
    log(traceback.format_exc())
    sys.exit(1)
