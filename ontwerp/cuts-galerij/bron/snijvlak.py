"""Galerijbeeld Click Cuts "Numbered for assembly" (Beeldmaker, 25 nov 2026, issue #39).

blender -b --factory-startup --python snijvlak.py -- <hoofdbeeld.py> <click_cuts.zip> <modelmap> <uit.png> <json> [samples] [schaal%]

Hetzelfde paard als het hoofdbeeld (Horse Statue 01, Poly Haven, CC0, https://polyhaven.com/a/horse_statue_01),
gesneden door de echte knop Split to fit van Click Cuts. Dan van dichtbij: één stuk met zijn snijvlak naar de
camera, de pengaten en het gegraveerde nummer die de add-on maakte, en gouden pennen in de gaten (één gat leeg).
Daarachter zweeft het buurstuk met zijn eigen nummer. Het beeld is een render, geen foto van een print.
Omgeving: SV_STUK en SV_BUUR (kies het snijvlak zelf), SV_DRAAI, SV_HOOG (camera), SV_LEEG (gaten zonder pen).
"""
import json
import math
import os
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

a = sys.argv[sys.argv.index("--") + 1:]
HB = a[0]
UIT_PNG, META_JSON = a[3], a[4]
SAMPLES = int(a[5]) if len(a) > 5 else 64
SCHAAL = int(a[6]) if len(a) > 6 else 100
# hoofdbeeld.py leest zijn eigen argumenten: geef hem zip, model, uit en json
sys.argv = [sys.argv[0], "--"] + a[1:]
bron = open(HB).read().rsplit("\nmain()", 1)[0]
_bewaar = (UIT_PNG, META_JSON, SAMPLES, SCHAAL)
exec(compile(bron, HB, "exec"))  # noqa: S102  laad(), splits(), plastic(), goud(), gloed(), punten() ...



UIT_PNG, META_JSON, SAMPLES, SCHAAL = _bewaar


def snijvlakken(stukken):
    """Elk snijvlak (stuk, buur) met zijn gaten en het nummer, uit wat de add-on op de stukken zette."""
    per = {s["sj_stuk"]: s for s in stukken}
    uit = []
    for s in stukken:
        gaten = json.loads(s.get("sj_gaten", "[]"))
        labels = json.loads(s.get("sj_labels", "[]"))
        buren = {}
        for g in gaten:
            buren.setdefault(g["buur"], []).append(g)
        for buur, gs in buren.items():
            tekst = f"{s['sj_stuk']}-{buur}"
            lb = [x for x in labels if x["tekst"] == tekst]
            if not lb or buur not in per:
                continue
            as_, tk, c = gs[0]["as"], gs[0]["teken"], gs[0]["snede"]
            opp = sum(p.area for p in s.data.polygons
                      if abs(p.normal[as_] - tk) < 0.02 and abs(p.center[as_] - c) < 1.0)
            uit.append({"stuk": s, "buur": per[buur], "gaten": gs, "label": lb[0], "as": as_,
                        "teken": tk, "opp": opp})
    return uit


def main():
    ob, dims = laad()
    voor, stukken, bak = splits(ob)
    for b in bak:
        bpy.data.objects.remove(b)
    bpy.data.objects.remove(voor)
    vlakken = snijvlakken(stukken)
    if os.environ.get("SV_ALLEEN_LIJST"):
        log("vlakken", [(x["stuk"]["sj_stuk"], x["buur"]["sj_stuk"], x["as"], x["teken"], len(x["gaten"]),
                         round(x["opp"])) for x in vlakken])
        return
    kies = os.environ.get("SV_STUK")
    if kies:
        v = next(x for x in vlakken if x["stuk"]["sj_stuk"] == int(kies) and x["buur"]["sj_stuk"] == int(os.environ["SV_BUUR"]))
    else:
        # het grootste nummer met de meeste gaten, liefst een horizontaal vlak dat naar boven kijkt
        v = max(vlakken, key=lambda x: x["opp"] * (1.3 if x["as"] == 2 and x["teken"] == 1 else 1.0))
    st, bu = v["stuk"], v["buur"]
    log("snijvlak", [(x["stuk"]["sj_stuk"], x["buur"]["sj_stuk"], x["as"], x["teken"], len(x["gaten"]),
                      round(x["opp"])) for x in vlakken])
    log("gekozen", st["sj_stuk"], bu["sj_stuk"], v["as"], v["teken"], len(v["gaten"]))
    for o in stukken:
        if o not in (st, bu):
            bpy.data.objects.remove(o)
    for o in (st, bu):
        o.delta_location = (0, 0, 0)
        o.location = (0, 0, 0)
        m = plastic(f"m_{o.name}", tuple(o.color), rough=0.45, coat=0.15)
        o.data.materials.clear()
        o.data.materials.append(m)
        for p in o.data.polygons:
            p.material_index = 0
            # snijvlakken plat, de rest glad (een glad snijvlak geeft vegen over de lange driehoeken)
            p.use_smooth = max(abs(c) for c in p.normal) < 0.999
    n = Vector((0, 0, 0))
    n[v["as"]] = v["teken"]
    # het buurstuk zweeft weg langs de normaal
    gat_mm = float(os.environ.get("SV_GAT", "150"))
    bu.location = n * gat_mm
    # pennen: half in de gaten van het stuk, één gat leeg
    mat = goud()
    leeg = int(os.environ.get("SV_LEEG", "1"))
    gs = sorted(v["gaten"], key=lambda g: -Vector(g["p"]).dot(Vector((1, -1, 0))))
    pens = []
    for i, g in enumerate(gs):
        if i < leeg:
            continue
        lengte = 2 * g["diepte"]
        bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=g["pen_d"] / 2, depth=lengte)
        pen = bpy.context.active_object
        bv = pen.modifiers.new("afschuin", "BEVEL")
        bv.width, bv.segments = 0.5, 3
        pen.data.materials.append(mat)
        for p in pen.data.polygons:
            p.use_smooth = True
        rot = {0: (0, math.pi / 2, 0), 1: (math.pi / 2, 0, 0), 2: (0, 0, 0)}[g["as"]]
        pen.rotation_euler = rot
        pen.location = Vector(g["p"]) + n * (lengte * 0.5 - g["diepte"] + 0.0)
        pen["hb_pen"] = 1
        pens.append(pen)
    # draai alles zodat het snijvlak naar de camera kijkt (de studiowand staat aan de +Y-kant)
    from mathutils import Matrix
    midden0 = Vector(v["label"]["p"])
    R = Matrix.Rotation(math.radians(float(os.environ.get("SV_ZDRAAI", "0"))), 4, "Z")
    if v["as"] != 2:
        hoek = math.atan2(n.x, -n.y)
        R = Matrix.Rotation(-hoek, 4, "Z")
    if True:
        bpy.context.view_layer.update()
        for o in [st, bu] + pens:
            o.matrix_world = R @ o.matrix_world
        n = (R.to_3x3() @ n).normalized()
        midden0 = R @ midden0
    bpy.context.view_layer.update()
    log("normaal na draaien", [round(c, 3) for c in n])
    # studio rond het snijvlak
    pts = punten([st])
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    maat = (hi - lo).length
    s = bpy.context.scene
    # verschuif alles zodat het stuk op de vloer staat
    for o in [st, bu] + pens:
        o.location.z -= lo.z
    bpy.context.view_layer.update()
    studio(maat * 1.1)
    # strijklicht over het vlak zodat de gravure leest
    midden = midden0 - Vector((0, 0, lo.z))
    ld = bpy.data.lights.new("strijk", "AREA")
    ld.shape, ld.size, ld.energy = "DISK", maat * 0.25, float(os.environ.get("SV_STRIJK", "1.2e6")) * (maat / 300) ** 2
    ld.color = srgb("FFF0DA")[:3]
    sl = bpy.data.objects.new("strijk", ld)
    s.collection.objects.link(sl)
    zij = Vector((1, 0, 0)) if v["as"] != 0 else Vector((0, 1, 0))
    sl.location = midden + zij * maat * 0.9 + n * maat * 0.18 + Vector((0, -maat * 0.4, 0))
    sl.rotation_euler = (midden - sl.location).to_track_quat("-Z", "Y").to_euler()

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
    zichtbaar = {st, bu, *pens} | {o for o in s.objects if o.name == "wand"}
    for o in s.objects:
        if o.type == "MESH":
            o.hide_render = o not in zichtbaar
    # camera: schuin boven het snijvlak, het vlak in de rechterhelft van het beeld
    if v["as"] == 2:
        boven, opzij = Vector((0, -1, 0)), Vector((1, 0, 0))
    else:
        boven, opzij = Vector((0, 0, 1)), n.cross(Vector((0, 0, 1)))
    richting = (n + boven * float(os.environ.get("SV_HOOG", "0.55"))
                + opzij * float(os.environ.get("SV_DRAAI", "0.35")))
    met_buur = os.environ.get("SV_BUUR_IN_BEELD", "0") == "1"
    bu.hide_render = not met_buur
    # kader: het snijvlak zelf (de vlakken van het stuk in het snijvlak) plus de pennen
    # macro: het nummer en de twee gaten die er het dichtst bij liggen
    gat_w = sorted((Vector(pp.matrix_world.translation) for pp in pens), key=lambda q: (q - midden).length)
    leeg_w = [R @ Vector(g["p"]) - Vector((0, 0, lo.z)) for g in gs[:leeg]]
    dicht = sorted(gat_w + leeg_w, key=lambda q: (q - midden).length)[:int(os.environ.get("SV_N_GAT", "2"))]
    r = float(os.environ.get("SV_RAND", "18"))
    vl = []
    for q in dicht + [midden]:
        for dx in (-r, r):
            for dz in (-r, r):
                vl.append(q + Vector((dx, 0, dz)))
                if met_buur:
                    vl.append(q + Vector((dx, 0, dz)) + n * gat_mm * float(os.environ.get("SV_BUUR_KADER", "0.8")))
    kader = bpy.data.objects.new("kader", bpy.data.meshes.new("kader"))
    kader.data.from_pydata([tuple(c) for c in vl], [], [])
    s.collection.objects.link(kader)
    kader.hide_render = True
    bpy.context.view_layer.update()
    objs = [st] if os.environ.get("SV_KADER") == "stuk" else [kader] + pens
    xb = (float(os.environ.get("SV_X0", "0.44")), 0.97)
    cam = camera(objs, richting, xb, (float(os.environ.get("SV_Y0", "0.06")), 0.96),
                 lens=float(os.environ.get("SV_LENS", "85")))
    cam.data.dof.use_dof = True
    cam.data.dof.focus_object = None
    cam.data.dof.focus_distance = (cam.location - midden).length
    cam.data.dof.aperture_fstop = float(os.environ.get("SV_F", "8"))
    bpy.context.view_layer.update()

    def vak(lijst):
        uv = [world_to_camera_view(s, cam, p) for p in punten(lijst)]
        return [min(q.x for q in uv), max(q.x for q in uv), 1 - max(q.y for q in uv), 1 - min(q.y for q in uv)]

    lp = world_to_camera_view(s, cam, midden)
    meta = {"model": "Horse Statue 01, Poly Haven, CC0", "printer": PRINTER, "stukken": len(stukken),
            "stuk": st["sj_stuk"], "buur": bu["sj_stuk"], "label": v["label"]["tekst"],
            "label_hoogte_mm": round(v["label"]["h"], 1), "label_diepte_mm": st.get("sj_label_diepte_mm"),
            "gaten_op_vlak": len(v["gaten"]), "pen_d_mm": v["gaten"][0]["pen_d"],
            "speling_mm": round(v["gaten"][0]["r_gat"] - v["gaten"][0]["pen_d"] / 2, 2),
            "status": [st.get("sj_status"), bu.get("sj_status")],
            "label_beeld": [lp.x, 1 - lp.y], "vak_stuk": vak([st]), "vak_buur": vak([bu])}
    with open(META_JSON, "w") as f:
        json.dump(meta, f, indent=1)
    log("meta", json.dumps(meta))
    s.render.filepath = UIT_PNG
    bpy.ops.render.render(write_still=True)
    log("klaar", UIT_PNG)


main()
