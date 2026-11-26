"""Galerijbeeld Click Cuts "Numbered for assembly", nu met het hele paard (Beeldmaker, 26 nov 2026, issue #105).

blender -b --factory-startup --python nummer_paard.py -- <hoofdbeeld.py> <click_cuts.zip> <modelmap> <uit.png> <json> [samples] [schaal%]

Thijs zag bij het vorige beeld een los oranje stuk en vroeg "wat moet het voorstellen?". Daarom hier het hele paard
(Horse Statue 01, Poly Haven, CC0, https://polyhaven.com/a/horse_statue_01), gesneden door de echte knop Split to fit
van Click Cuts, uit elkaar in de kleuren per stuk die de add-on geeft, met gouden pennen op elk gatenpaar. In <json>
staat waar de naad tussen NP_STUK en NP_BUUR (standaard 7 en 11) in het beeld ligt, zodat de tekstlaag er een lijn
naar het kaartje met de close-up (snijvlak.py) kan trekken. Het beeld is een render, geen foto van een print.
Omgeving: NP_STUK, NP_BUUR, NP_X0, NP_X1, NP_Y0, NP_Y1 (vak in het beeld), plus HB_UIT, HB_UIT_Z, HB_DRAAI, HB_KANTEL.
"""
import json
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
sys.argv = [sys.argv[0], "--"] + a[1:]
bron = open(HB).read().rsplit("\nmain()", 1)[0]
_bewaar = (UIT_PNG, META_JSON, SAMPLES, SCHAAL)
exec(compile(bron, HB, "exec"))  # noqa: S102  laad(), splits(), uit_elkaar(), pennen(), studio(), camera() ...
UIT_PNG, META_JSON, SAMPLES, SCHAAL = _bewaar


def main():
    ob, dims = laad()
    h = dims.z
    voor, stukken, bak = splits(ob)
    for b in bak:
        bpy.data.objects.remove(b)
    bpy.data.objects.remove(voor)
    kleur_stukken(stukken)
    plek = Vector((0, 0, 0))
    d = uit_elkaar(stukken, plek)
    n_pen = pennen(stukken, d, plek, goud())
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
    zichtbaar = set(stukken) | {o for o in s.objects if o.get("hb_pen") or o.name == "wand"}
    for o in s.objects:
        if o.type == "MESH":
            o.hide_render = o not in zichtbaar
    xb = (float(os.environ.get("NP_X0", "0.40")), float(os.environ.get("NP_X1", "0.74")))
    yb = (float(os.environ.get("NP_Y0", "0.12")), float(os.environ.get("NP_Y1", "0.94")))
    cam = camera(stukken, Vector((float(os.environ.get("HB_DRAAI", "0.35")), -1.0,
                                  float(os.environ.get("HB_KANTEL", "0.22")))), xb, yb, lens=70)

    def vak(lijst):
        uv = [world_to_camera_view(s, cam, p) for p in punten(lijst)]
        return [min(q.x for q in uv), max(q.x for q in uv), 1 - max(q.y for q in uv), 1 - min(q.y for q in uv)]

    per = {o["sj_stuk"]: o for o in stukken}
    nst, nbu = int(os.environ.get("NP_STUK", "7")), int(os.environ.get("NP_BUUR", "11"))
    naad = None
    if nst in per and nbu in per:
        lb = [x for x in json.loads(per[nst].get("sj_labels", "[]")) if x["tekst"] == f"{nst}-{nbu}"]
        if lb:
            w = Vector(lb[0]["p"]) + plek + (d[nst] + d[nbu]) / 2
            q = world_to_camera_view(s, cam, w)
            naad = [q.x, 1 - q.y]
    labels = {o["sj_stuk"]: [x["tekst"] for x in json.loads(o.get("sj_labels", "[]"))] for o in stukken}
    maten = [sorted(round(v, 1) for v in o.dimensions) for o in stukken]
    meta = {"model": "Horse Statue 01, Poly Haven, CC0", "hoogte_mm": round(h, 1), "printer": PRINTER,
            "bed_mm": BED, "stukken": len(stukken), "pennen": n_pen,
            "status": [o.get("sj_status") for o in stukken], "alle_passen": all(m[2] <= BED for m in maten),
            "labels": labels, "vakken": {o["sj_stuk"]: [round(v, 3) for v in vak([o])] for o in stukken},
            "kleuren": {o["sj_stuk"]: [round(c, 2) for c in o.color[:3]] for o in stukken}, "stuk": nst, "buur": nbu, "naad_beeld": naad,
            "vak_na": vak(stukken), "vak_stuk": vak([per[nst]]) if nst in per else None,
            "vak_buur": vak([per[nbu]]) if nbu in per else None}
    with open(META_JSON, "w") as f:
        json.dump(meta, f, indent=1)
    log("meta", json.dumps(meta))
    if os.environ.get("NP_ALLEEN_META"):
        return
    s.render.filepath = UIT_PNG
    bpy.ops.render.render(write_still=True)
    log("klaar", UIT_PNG)


main()
