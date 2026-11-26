"""Free cut (vrije_snede.py), called from test_kern.py; also runs alone:
blender -b --factory-startup --python e2e/toetsen_vrij.py -- <zip>

Model: a torso (40 x 40 x 40 mm) with an arm sticking out (60 x 16 x 16 mm), made watertight with the add-on.
Split gives one piece on an A1 mini. Then a free cut turned 90 degrees (arrow along +X) and 15 degrees around Z
through the arm. Measured on the meshes: two pieces, both watertight and green, the new piece holds only the arm
end (its size), volumes add up, every new hole is as deep as planned along the plane normal on both sides,
the two halves get different colors, pins match the hole pairs. Refused (piece count stays): a rectangle
smaller than the arm, a plane that misses the piece, a plane through an existing pin hole (message checked);\na parallel plane 3 mm past the bottom of that hole does cut."""
import math
import os
import sys
import traceback

import bmesh
import bpy
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import modellen  # noqa: E402
from hulp import dicht, fouten, log, pen_objecten, stap, stukken  # noqa: E402


def torso_met_arm():
    bm = bmesh.new()
    for mn, mx in (((-20, -20, 0), (20, 20, 40)), ((15, -8, 22), (80, 8, 38))):
        t = bmesh.new()
        bmesh.ops.create_cube(t, size=1.0)
        for v in t.verts:
            v.co = Vector((mx[i] if v.co[i] > 0 else mn[i]) for i in range(3))
        me = bpy.data.meshes.new("t")
        t.to_mesh(me)
        t.free()
        bm.from_mesh(me)
        bpy.data.meshes.remove(me)
    ob = modellen._object("Figure", bm)
    return modellen.waterdicht(ob, 0.5)


def boom(ob):
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    b = BVHTree.FromBMesh(bm)
    bm.free()
    return b


def vrije_snede(stuk, x, hoek_z=15.0, schaal=1.0):
    modellen.actief(stuk)
    r = bpy.ops.split_joints.vrije_snede_erbij()
    snede = bpy.context.view_layer.objects.active
    snede.location = (x, 0.0, 30.0)
    snede.rotation_mode = "XYZ"  # first 90 degrees around Y (arrow to +X), then turned around world Z
    snede.rotation_euler = (0.0, math.radians(90.0), math.radians(hoek_z))
    snede.scale = (schaal, schaal, 1.0)
    bpy.context.view_layer.update()
    return r, snede


LAATSTE = [""]  # message of the last refused Cut piece


def knip():
    """Runs Cut piece; an ERROR report raises in bpy.ops, that counts as CANCELLED with the message."""
    LAATSTE[0] = ""
    try:
        return bpy.ops.split_joints.vrije_snede()
    except RuntimeError as e:
        LAATSTE[0] = str(e).strip()
        log(f"vrij: melding {LAATSTE[0][:160]}")
        return {"CANCELLED"}


def alles(uitmap=None):
    modellen.mm_scene()
    inst = bpy.context.scene.split_joints
    inst.printer = "A1MINI"
    inst.speling_mm = 0.2
    ob = torso_met_arm()
    modellen.actief(ob)
    bpy.ops.split_joints.plan()
    bpy.ops.split_joints.split()
    lijst = stukken()
    if not stap("vrij: split geeft 1 stuk", len(lijst) == 1, f"{len(lijst)} stukken"):
        return
    stuk = lijst[0]
    v_voor = dicht(stuk)[2]

    # refused: rectangle smaller than the arm (16 mm), the box would cut the arm lengthwise
    r, snede = vrije_snede(stuk, 50.0, schaal=0.05)
    modellen.actief(snede)
    r = knip()
    stap("vrij: te kleine rechthoek geweigerd", r == {"CANCELLED"} and len(stukken()) == 1, f"{r}")
    # refused: the plane misses the piece
    snede.scale = (1.0, 1.0, 1.0)
    snede.location = (200.0, 0.0, 30.0)
    bpy.context.view_layer.update()
    r = knip()
    stap("vrij: snede naast het stuk geweigerd", r == {"CANCELLED"} and len(stukken()) == 1, f"{r}")

    # the real cut
    snede.location = (50.0, 0.0, 30.0)
    bpy.context.view_layer.update()
    n = Vector(snede.matrix_world.to_3x3() @ Vector((0, 0, 1))).normalized()
    r = knip()
    lijst = stukken()
    stap("vrij: snijden lukt", r == {"FINISHED"}, f"{r}")
    if not stap("vrij: 2 stukken", len(lijst) == 2, f"{len(lijst)}"):
        return
    a, b = lijst
    stap("vrij: snedevlak weg", not any(o.get("sj_vrij") for o in bpy.context.scene.objects))
    for o in lijst:
        ok, slecht, vol = dicht(o)
        stap(f"vrij stuk {o['sj_stuk']}: waterdicht", ok, f"slecht {slecht}, volume {vol:.0f}, stappen {list(o.get('sj_fout_stappen', []))}")
        stap(f"vrij stuk {o['sj_stuk']}: groen", o.get("sj_status") == "groen", f"{o.get('sj_status')} wand {o.get('sj_wand_mm')}")
    xs = [v.co.x for v in b.data.vertices]
    stap("vrij: nieuw stuk is alleen het armeinde", min(xs) > 40.0 and max(xs) < 81.0 and
         max(v.co.z for v in b.data.vertices) < 39.0, f"x {min(xs):.1f} tot {max(xs):.1f}")
    stap("vrij: torso blijft heel", min(v.co.x for v in a.data.vertices) < -19.0 and
         max(v.co.z for v in a.data.vertices) > 39.0)
    import json
    nieuw_a = [g for g in json.loads(a["sj_gaten"]) if g.get("vrij")]
    nieuw_b = [g for g in json.loads(b["sj_gaten"]) if g.get("vrij")]
    stap("vrij: gaten aan beide kanten", len(nieuw_a) == len(nieuw_b) and len(nieuw_a) >= 1, f"{len(nieuw_a)} / {len(nieuw_b)}")
    gat_vol = sum(math.pi * g["r_gat"] ** 2 * g["diepte"] for g in nieuw_a + nieuw_b)
    v_na = dicht(a)[2] + dicht(b)[2]
    stap("vrij: volumes tellen op (min gaten en nummers)", v_voor - gat_vol - 400 < v_na < v_voor - gat_vol * 0.9,
         f"voor {v_voor:.0f}, na {v_na:.0f}, gaten {gat_vol:.0f}")
    for naam, o, gs, richting in (("A", a, nieuw_a, -1), ("B", b, nieuw_b, 1)):
        t = boom(o)
        for g in gs:
            p = Vector(g["p"])
            gn = Vector(g["n"])
            stap(f"vrij {naam}: gat langs de normaal van het vlak", abs(abs(gn.dot(n)) - 1.0) < 1e-4, f"{tuple(round(x, 3) for x in gn)}")
            hit = t.ray_cast(p + gn * richting * 0.05, gn * richting)
            d = hit[3] + 0.05 if hit[0] is not None else None
            stap(f"vrij {naam}: gat {g['diepte']:.2f} mm diep", d is not None and abs(d - g["diepte"]) < 0.08,
                 f"gemeten {d}")
    stap("vrij: normaal 15 graden gedraaid", abs(math.degrees(math.atan2(n.y, n.x)) - 15.0) < 0.1, f"{tuple(round(x, 3) for x in n)}")
    lab = [lb for o in (a, b) for lb in json.loads(o["sj_labels"]) if lb.get("vrij")]
    stap("vrij: nummers op beide snijvlakken", sorted(lb["tekst"] for lb in lab) == ["1-2", "2-1"], f"{[lb['tekst'] for lb in lab]}")
    stap("vrij: helften verschillende kleur", tuple(a.color) != tuple(b.color), f"{list(a.color)[:3]} {list(b.color)[:3]}")
    pen = sum(int(p["sj_pennen"]) for p in pen_objecten())
    stap("vrij: pennen gelijk aan gatenparen", pen == len(nieuw_a), f"{pen} pennen")

    # refused: a free cut through the pin hole of piece B (parallel, halfway down the hole). The plane is placed
    # in world space on the hole itself, with the exploded view offset (keuring 24 nov, M2: on x = 52 the plane
    # missed the moved piece and was refused for the wrong reason)
    g = nieuw_b[0]
    gn = Vector(g["n"])
    verschuiving = Vector(b.delta_location)

    def op_gat(diep):
        r, snede = vrije_snede(b, 0.0)
        snede.location = Vector(g["p"]) + gn * diep + verschuiving
        bpy.context.view_layer.update()
        modellen.actief(snede)
        return snede

    op_gat(g["diepte"] / 2.0)
    r = knip()
    stap("vrij: snede door een pengat geweigerd", r == {"CANCELLED"} and len(stukken()) == 2 and
         "pin hole" in LAATSTE[0], f"{r} '{LAATSTE[0][:90]}'")
    weg = [o for o in bpy.context.scene.objects if o.get("sj_vrij")]
    for o in weg:
        bpy.data.objects.remove(o)
    # the 1.2 mm limit itself (keuring K7): 1.0 mm past the bottom is refused, 1.5 mm past it cuts
    op_gat(g["diepte"] + 1.0)
    r = knip()
    stap("vrij: 1,0 mm voorbij het gat nog geweigerd", r == {"CANCELLED"} and len(stukken()) == 2 and
         "pin hole" in LAATSTE[0], f"{r} '{LAATSTE[0][:90]}'")
    for o in [o for o in bpy.context.scene.objects if o.get("sj_vrij")]:
        bpy.data.objects.remove(o)
    op_gat(g["diepte"] + 1.5)
    r = knip()
    stap("vrij: snede net voorbij het gat snijdt wel", r == {"FINISHED"} and len(stukken()) == 3,
         f"{r} {len(stukken())} '{LAATSTE[0][:90]}'")
    if uitmap:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uitmap, "vrij.blend"))


def tekenen(uitmap=None):
    """Draw cut (issue #208): the line a buyer drags in the front view (looking along +Y) across the arm at
    x = 50, from below to above and the other way round. The plane comes from the add-on itself (vlak_uit_lijn
    and zet_vlak, the same calls the modal operator makes after the mouse is released); then Cut piece.
    In the exploded view the piece sits elsewhere: the line is drawn where the piece is seen."""
    import importlib
    vs = importlib.import_module("bl_ext.user_default.click_cuts.vrije_snede")
    for richting, (z1, z2) in (("omhoog", (15.0, 45.0)), ("omlaag", (45.0, 15.0))):
        modellen.mm_scene()
        inst = bpy.context.scene.split_joints
        inst.printer = "A1MINI"
        inst.speling_mm = 0.2
        ob = torso_met_arm()
        modellen.actief(ob)
        bpy.ops.split_joints.plan()
        bpy.ops.split_joints.split()
        lijst = stukken()
        if not stap(f"tekenen {richting}: split geeft 1 stuk", len(lijst) == 1, f"{len(lijst)} stukken"):
            return
        stuk = lijst[0]
        modellen.actief(stuk)
        d = Vector(stuk.matrix_world.translation)
        pts = vs.punten_wereld(stuk)
        kader = vs.vlak_uit_lijn((50.0 + d.x, -60.0 + d.y, z1 + d.z), (50.0 + d.x, -60.0 + d.y, z2 + d.z), (0.0, 1.0, 0.0),
                                 pts, marge=1.0)
        snede = vs.zet_vlak(bpy.context, stuk, *kader)
        bpy.context.view_layer.update()
        n = Vector(snede.matrix_world.to_3x3() @ Vector((0, 0, 1))).normalized()
        stap(f"tekenen {richting}: pijl wijst naar het armeinde", n.x > 0.999, f"{tuple(round(x, 3) for x in n)}")
        stap(f"tekenen {richting}: vlak hoort bij het stuk", snede.get("sj_vrij") == stuk.name)
        modellen.actief(snede)
        r = knip()
        lijst = stukken()
        stap(f"tekenen {richting}: snijden lukt", r == {"FINISHED"} and len(lijst) == 2, f"{r} {len(lijst)} '{LAATSTE[0][:90]}'")
        if len(lijst) != 2:
            continue
        a, b = sorted(lijst, key=lambda o: o["sj_stuk"])
        xs = [v.co.x for v in b.data.vertices]
        stap(f"tekenen {richting}: nieuw stuk is alleen het armeinde", min(xs) > 49.0 and max(xs) < 81.0, f"x {min(xs):.1f} tot {max(xs):.1f}")
        stap(f"tekenen {richting}: torso blijft heel", min(v.co.x for v in a.data.vertices) < -19.0)
        for o in (a, b):
            stap(f"tekenen {richting} stuk {o['sj_stuk']}: groen", o.get("sj_status") == "groen", f"{o.get('sj_status')}")
    if uitmap:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uitmap, "tekenen.blend"))


if __name__ == "__main__":
    try:
        args = sys.argv[sys.argv.index("--") + 1:]
        bpy.ops.extensions.package_install_files(filepath=args[0], repo="user_default", enable_on_install=True)
        alles(args[1] if len(args) > 1 else None)
        tekenen(args[1] if len(args) > 1 else None)
    except Exception:
        traceback.print_exc()
        fouten.append("onverwachte fout")
    log(f"KLAAR {len(fouten)} FOUT {fouten}")
