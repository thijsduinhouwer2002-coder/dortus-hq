"""Eén Meshy-figuur met knie en elleboog uit Pro 1.0.2, voor de render van Chris (hoofdchat 16 nov 16:40).

Leent laad, lussen en installeer uit proef_ai_model.py (zonder zijn main). Anders dan die proef bepaalt dit script
eerst hoe de figuur staat: links-rechts is de richting waarin de schouders het breedst zijn, voor is de kant waar
de schoen het verst voorbij de scheen steekt (de tenen). Dan: Pro-scharnier met eindstop 115 in één knie (buigt naar
achter) en in de elleboog aan dezelfde kant (buigt naar voor), scharnieras links-rechts. Lidas omhoog: deel B is het
bovenste deel en kantelt naar cj_buigkant; dan draait het onderste deel ten opzichte van B andersom, en een punt
onder het scharnier (voet, hand) komt ook aan de buigkant uit (Chris 16 nov 20:00, klopt). Een knie krijgt dus
buigkant achter, een elleboog buigkant voor.
Na elke snede: deel A en B moeten elk één gesloten stuk zijn. Is dat niet zo (in 1.0.2 liet de snede op army_man bij
40,5 mm de zool van de schoen als los stuk in B, zie ontwerp-1.1.md run 12), dan opnieuw vanaf het model op de
volgende hoogte. Bewaart <uit>/<naam>-knie-elleboog.blend.
Gebruik: blender -b --factory-startup --python e2e/maak_chris_figuur.py -- <betaalde zip> <uitmap> <model.glb>
"""
import os
import sys

import bpy
from mathutils import Matrix, Vector

HIER = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HIER, "proef_ai_model.py"), encoding="utf-8").read()
src = src[:src.rstrip().rfind("main()")]
g = {"__name__": "proef_ai_model", "__file__": os.path.join(HIER, "proef_ai_model.py")}
exec(compile(src, "proef_ai_model.py", "exec"), g)
H = g["HOOGTE_MM"]


def log(t):
    print(f"[cj-chris] {t}", flush=True)


def zichtbaar():
    return [o for o in bpy.context.scene.objects if o.type == "MESH" and o.visible_get()]


def punten(ob):
    return [ob.matrix_world @ v.co for v in ob.data.vertices]


def stand_van(ob):
    """(zij, voor): eenheidsvectoren in het grondvlak."""
    ps = punten(ob)
    sch = [p for p in ps if 0.66 * H < p.z < 0.72 * H]
    bx = max(p.x for p in sch) - min(p.x for p in sch)
    by = max(p.y for p in sch) - min(p.y for p in sch)
    zij = Vector((0, 1, 0)) if by > bx else Vector((1, 0, 0))
    vr = Vector((1, 0, 0)) if by > bx else Vector((0, 1, 0))
    # 16 nov run 12: eerst zool tegen enkel (zool z < 2%, enkel 5 tot 8%), maar bij army_man zit de enkelhoogte nog
    # in de schoen en lag het verschil verkeerd om. Nu: één been (de kant +zij), hoe ver steekt de schoen (z < 6%)
    # aan elke kant voorbij de scheen (13 tot 20%)? De tenen zitten aan de kant waar dat het meest is.
    been = [p for p in ps if p.dot(zij) > 3.0]
    voet = [p.dot(vr) for p in been if p.z < 0.06 * H]
    scheen = [p.dot(vr) for p in been if 0.13 * H < p.z < 0.20 * H]
    d = (max(voet) - max(scheen)) - (min(scheen) - min(voet))
    return zij, (vr if d > 0 else -vr)


def zet_cursor(c, as_, buig):
    h = buig.cross(as_)  # zelfde handigheid als in proef_ai_model: H = buigkant x lidas
    m = Matrix.Identity(4)
    for i, v in enumerate((h, buig, as_)):
        m.col[i][:3] = v
    m.col[3][:3] = c
    cur = bpy.context.scene.cursor
    cur.rotation_mode = "QUATERNION"
    cur.matrix = m


def lid_lus(zij, z, kant, max_breed=30.0):
    """Lus van een been of arm op hoogte z aan de kant `kant` (+1/-1 langs zij), het verst naar buiten."""
    beste = None
    for o in zichtbaar():
        for c, bx, by in g["lussen"](o, z):
            s = c.dot(zij) * kant
            if s > 3.0 and max(bx, by) < max_breed * H / 150.0 and (beste is None or s > beste[1]):
                beste = (o, s, c)
    return beste


def scharnier(doel, c, as_, buig, wat):
    zet_cursor(c, as_, buig)
    inst = bpy.context.scene.click_joints
    inst.as_bron, inst.uit_elkaar = "CURSOR", False
    g["actief"](doel)
    voor = set(o.name for o in bpy.context.scene.objects)
    try:
        r = bpy.ops.click_joints.plaats_scharnier(stand="115")
    except RuntimeError as e:
        r = f"fout {str(e)[:150]}"
    nieuw = [o for o in bpy.context.scene.objects if o.name not in voor and o.get("cj_deel")]
    log(f"{wat} op ({c.x:.1f}, {c.y:.1f}, {c.z:.1f}): {r}, delen {[(o.name, o.get('cj_bereik_graden')) for o in nieuw]}, "
        f"melding {next((o.get('cj_melding') for o in nieuw if o.get('cj_melding')), None)}")
    return bool(nieuw)


def een_poging(pad, pct_knie):
    """Model laden, dicht maken, knie op pct_knie. (gelukt, naam, zij, voor); gelukt alleen bij twee hele delen."""
    g["leeg"]()
    ob = g["laad"](pad)
    st = g["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        g["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        ob = bpy.context.view_layer.objects.active
    zij, voor = stand_van(ob)
    l = lid_lus(zij, pct_knie / 100 * H, 1)
    # Knie: scheen en voet naar achter, dus buigkant achter (-voor). 16 nov run 11 stond hier +voor met een
    # omgekeerde tenen-test; uitkomst gelijk, nu om de goede reden.
    if not (l and scharnier(l[0], l[2], Vector((0, 0, 1)), -voor, "KNIE")):
        return False, ob.name, zij, voor
    heel = all(stukken(o) == 1 for o in zichtbaar() if o.get("cj_deel"))
    if not heel:
        log(f"KNIE op {pct_knie}%: delen niet heel ({[(o.name, stukken(o)) for o in zichtbaar() if o.get('cj_deel')]}), "
            "opnieuw op de volgende hoogte")
    return heel, ob.name, zij, voor


def stukken(ob):
    """Aantal losse stukken (via randen verbonden punten)."""
    me = ob.data
    ouder = list(range(len(me.vertices)))

    def zoek(a):
        while ouder[a] != a:
            ouder[a] = ouder[ouder[a]]
            a = ouder[a]
        return a
    for e in me.edges:
        a, b = zoek(e.vertices[0]), zoek(e.vertices[1])
        if a != b:
            ouder[a] = b
    return len({zoek(i) for i in range(len(me.vertices))})


if __name__ == "__main__":
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, uit, pad = args[0], args[1], args[2]
    os.makedirs(uit, exist_ok=True)
    g["installeer"](zip_pad)
    gelukt = []
    naam, zij, voor = None, None, None
    for pct in (27, 25, 29, 24, 31):
        ok, naam, zij, voor = een_poging(pad, pct)
        if ok:
            gelukt.append("knie")
            break
    log(f"zij {tuple(zij)}, voor {tuple(round(x, 2) for x in voor)}")
    if not gelukt:  # niets heel gelukt: model leeg terug, zodat er geen half resultaat in de .blend staat
        g["leeg"]()
        g["laad"](pad)
    for pct in (59, 57, 61, 55, 63, 53):
        l = lid_lus(zij, pct / 100 * H, 1, 22.0)
        # Elleboog: onderarm en hand naar voor, dus buigkant voor.
        if l and scharnier(l[0], l[2], Vector((0, 0, 1)), voor, "ELLEBOOG"):
            gelukt.append("elleboog")
            break
    for o in zichtbaar():
        log(f"deel {o.name} stand={o.get('cj_stand')} bereik={o.get('cj_bereik_graden')} passing={o.get('cj_passing')} "
            f"stukken={stukken(o)}")
    log(f"gelukt: {gelukt}")
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(uit, f"{naam}-knie-elleboog.blend"), compress=True)
    log("KLAAR")
