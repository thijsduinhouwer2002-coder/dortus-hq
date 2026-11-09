"""Snelle proef voor filmisch ronde 6 (6e: nerf nog rustiger; 6d: Daan 04:33, bijna egaal hout, rood #E0261C dichterbij, lichtvlek, strakke ring; 6c: punten Daan 03:55, rood van dichtbij op de rode vlakken, pop groter) (Daan 9 nov): gestrekte arm met gewricht op de elleboog, trap met knie-gewricht,
hout beuken, oneindige achtergrond, en het rood op 28 graden vanuit vijf hoeken plus Exploded view.

Laadt film_mooi.py zonder de hoofdlus en daarna film_zes.py in dezelfde namespace (die vervangt pop, hout,
licht en plek van het gewricht). Zo hoeven we niet 40 minuten op de hele film te wachten.

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
zes = os.path.join(HIER, "film_zes.py")
exec(compile(open(zes).read(), zes, "exec"), F)  # noqa: S102  (ronde 6 vervangt pop, hout en licht)
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
    import math
    from mathutils import Quaternion, Vector
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=ZIP, repo="user_default", enable_on_install=True)
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    F["figuren"].mm_scene()
    F["render_instellingen"]()
    bpy.context.scene.cycles.samples = 24
    F["licht_en_wereld"]()
    cam = F["camera"]()
    pop = F["tekenpop"](F["mod"]("gewricht").solver_naam())
    log(f"pop: {len(pop.data.polygons)} vlakken, foute randen {F['gesloten'](pop)}")
    log(f"look {bpy.context.scene.view_settings.view_transform} / {bpy.context.scene.view_settings.look}")
    beschrijf(pop)
    kijk = F["kijk"]
    M, BR = F["POP_MIDDEN"], F["BASIS_RICHTING"]
    # 6c: pop ±112 mm hoog op 80 procent van de beeldhoogte: hoogte in beeld = d x 20,25 / 50, dus d ±345
    kijk(cam, Vector((-4, -8, 56)) + BR * 345, Vector((-4, -8, 56)), lens=50)
    render("1-held")

    inst = bpy.context.scene.click_joints
    uit, a, b = F["plaats_op"](pop, F["ELLEBOOG"], F["ONDERARM"])
    log(f"elleboog: {uit}, kogel {inst.kogel_mm} mm")
    if a is None or b is None:
        log("PROEF FOUT elleboog niet geplaatst")
        return
    pop.hide_render = True
    log(f"6d strakke ring A {F['strakke_ring'](a)} B {F['strakke_ring'](b)}, vakken A {[m.name if m else None for m in a.data.materials]}")
    paneel = F["mod"]("paneel")
    log(f"elleboog: passing {a.get('cj_passing')}, wand {a.get('cj_wand_mm')}, tekst {paneel.buig_tekst(a)}, "
        f"bereik {[round(x, 1) for x in a.get('cj_buig_graden', [])]}, foute randen A {F['gesloten'](a)} B {F['gesloten'](b)}")
    as_ = Vector(a["cj_as"]).normalized()
    c = Vector(a["cj_centrum"])
    rr = float(a["cj_kogel_r"])
    rich = F["mod"]("uit_elkaar").richtingen(as_)
    k = max(range(len(rich)), key=lambda i: rich[i].z)
    inst.pose_richting = str(k)
    grens = paneel.richting_graden(a, k)
    for o in (a, b):
        log(f"nerf_co op {o.name}: {'nerf_co' in o.data.attributes}")
    log(f"richting {k} ({tuple(round(x, 2) for x in rich[k])}), grens {grens}")
    zij = as_.cross(rich[k]).normalized()
    if zij.dot(BR) < 0:
        zij = -zij
    # haak: donker, dichtbij, groene ring gloeit
    F["gloed"](F["mat_naam"]("groen"), F["GROEN"], 6.0)
    kijk(cam, c + (zij + as_ * 0.3).normalized() * 40 * rr, c, lens=60)
    render("2-haak-gloed")
    F["gloed"](F["mat_naam"]("groen"), F["GROEN"], 0.6)
    # close-up schouder en hand in beeld, gewricht op een derde
    kijk(cam, c + zij * 95 * rr + Vector((0, 0, -10)), c + as_ * 8, lens=50)
    render("3-elleboog-0")
    # 28 graden vanuit vijf hoeken om de as, en met Exploded view
    inst.pose_graden = 28.0
    bpy.context.view_layer.update()
    log(f"28 graden: rode vlakken A {len(a.get('cj_rood_vlakken', [])) // 2}")
    for j, hoek in enumerate((0, 60, 120, 270)):  # 180 stond in 6a in de achterwand (zwart beeld)
        r = Quaternion(as_, math.radians(hoek)) @ zij
        kijk(cam, c + (r + as_ * 0.25).normalized() * 60 * rr, c + as_ * 2, lens=60)
        render(f"4-rood28-hoek{hoek}")
    # 6b: rood met deel B (hout en groene ring) half doorzichtig, zoals in film_mooi tijdens het rood
    # 6c (Daan 03:55): rood minstens een tiende van de beeldbreedte, echt rood (B bijna helemaal doorzichtig, dus geen
    # roze door de groene laag), camera recht op de rode vlakken vanaf hun eigen buitenkant.
    F["staat"]["b_door"] = F["hout_doorzichtig"](b)
    F["zet_door"](0.93)
    log(f"6d rood basis #E0261C: {F['rood_basis']()}")
    F["gloed"](F["mat_naam"]("rood"), F["ROOD"], 1.0)   # 6d: Daan 0,8 tot 1,2 op verzadigde basis
    lijst = list(a.get("cj_rood_vlakken", []))
    mw = a.matrix_world
    punten, norm = [], Vector()
    for i in lijst[0::2]:
        pg = a.data.polygons[i]
        punten += [mw @ a.data.vertices[v].co for v in pg.vertices]
        norm += (mw.to_3x3() @ pg.normal) * pg.area
    if punten:
        rc = sum(punten, Vector()) / len(punten)
        maat = max((p - rc).length for p in punten) * 2
        if norm.length < 1e-9:
            norm = zij.copy()
        norm.normalize()
        # beeldbreedte op afstand d met 60 mm lens = 0,6 d; rood op 12 procent: d = maat / 0,072
        d = min(max(maat / 0.2, 4 * rr), 30 * rr)   # 6d: Daan minstens 10 procent (6c3 gaf 8 tot 10)
        log(f"rood midden {tuple(round(x, 2) for x in rc)}, maat {maat:.2f} mm, normaal {tuple(round(x, 2) for x in norm)}, afstand {d:.1f}")
        fstop = cam.data.dof.aperture_fstop
        cam.data.dof.aperture_fstop = 22.0   # zo dichtbij is f/8 te wazig
        for j, kant in enumerate((norm, (norm + zij * 0.6).normalized())):
            kijk(cam, rc + kant * d, rc, lens=60)
            render(f"4b-rood28-doorzichtig-{j}")
        # 6d: Daans terugval, B helemaal weg in de inzet (eerlijk met label "Exploded view" in de film)
        b.hide_render = True
        kijk(cam, rc + norm * d, rc, lens=60)
        render("4b-rood28-zonder-b")
        b.hide_render = False
        cam.data.dof.aperture_fstop = fstop
    else:
        log("geen rode vlakken gevonden voor 4b")
    F["zet_door"](0.0)
    F["gloed"](F["mat_naam"]("rood"), F["ROOD"], 0.0)
    inst.uit_elkaar = True
    bpy.context.view_layer.update()
    kijk(cam, c + (zij + as_ * 0.5).normalized() * 45 * rr, c + as_ * 4, lens=60)
    render("5-rood28-exploded")
    inst.uit_elkaar = False
    inst.pose_graden = 0.0
    bpy.context.view_layer.update()

    # knie (tweede gewricht, op deel A)
    uit2, a2, b2 = F["plaats_op"](a, F["KNIE"], F["SCHEEN"])
    log(f"knie: {uit2}, kogel {inst.kogel_mm} mm, A2 {a2.name if a2 else None}, B2 {b2.name if b2 else None}")
    if a2 is not None:
        a.hide_render = True
        log(f"6d strakke ring A2 {F['strakke_ring'](a2)} B2 {F['strakke_ring'](b2)}")
        log(f"knie: passing {a2.get('cj_passing')}, tekst {paneel.buig_tekst(a2)}, "
            f"bereik {[round(x, 1) for x in a2.get('cj_buig_graden', [])]}")
    log(f"zichtbaar in render: {[o.name for o in bpy.context.scene.objects if o.type == 'MESH' and not o.hide_render]}")
    inst.pose_graden = 15.0
    bpy.context.view_layer.update()
    kijk(cam, Vector((-4, -8, 56)) + BR * 345, Vector((-4, -8, 56)), lens=50)
    render("6-twee-gewrichten-15")
    log("PROEF KLAAR")


try:
    main()
except Exception as e:  # noqa: BLE001
    import traceback
    log("PROEF FOUT " + repr(e))
    log(traceback.format_exc())
    sys.exit(1)
