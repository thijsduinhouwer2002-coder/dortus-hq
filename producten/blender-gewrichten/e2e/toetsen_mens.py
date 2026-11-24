"""Toets (17 nov run 20): Figure from rig op een echte mensfiguur (MakeHuman base.obj, CC0) met Mixamo-rig.

Zelfde figuur en rig als proef_mens.py (run 18), nu met eisen, zodat de figuur van het eindbeeld voor Daan in de CI
blijft werken. Standaard 220 mm hoog (zet CJ_HOOGTE niet zelf; deze toets zet hem).

Eisen in Blender 5.x (gemeten run 18 en 20):
- minstens 6 gewrichten, waaronder beide ellebogen en beide knieën;
- Left knee `from rig` met 0–120, Right knee `mirrored` met 0–120; Left elbow `from rig` 0–140, Right elbow
  `mirrored` 0–140 (het getal is het gemeten bereik, binnen 3 graden);
- elk standaardgewricht dat niet geplaatst is, staat in de melding met een reden tussen haakjes;
- alle delen gesloten en elk deel één stuk;
- handen, voeten en hoofd liggen nog in een deel (geen stil verloren lid).
In Blender 4.2 (alleen de Exact-solver, bekende losse boolean-fout, zie toetsen_rig_armen.py): minstens 3
gewrichten met de ellebogen (gemeten: ellebogen en nek), de rest met reden, en dezelfde eisen voor gesloten, één stuk en niets kwijt.

Gebruik: blender -b --factory-startup --python e2e/toetsen_mens.py -- <betaalde zip> <base.obj>
Uitslag: regels [cj-mens-toets], laatste regel "KLAAR n FOUT".
"""
import importlib
import os
import sys

import bpy

os.environ["CJ_HOOGTE"] = os.environ.get("CJ_TOETS_HOOGTE", "220")
HIER = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HIER, "proef_mens.py"), encoding="utf-8").read().replace("\nmain()\n", "\n")
M = {"__name__": "proef_mens", "__file__": os.path.join(HIER, "proef_mens.py")}
exec(compile(_src, "proef_mens.py", "exec"), M)
A = M["A"]

FOUT = []
DOEL2 = os.environ.get("CJ_HERKANS_LID", "Left shoulder")  # gewricht voor CJ_HERKANS=2


def log(t):
    print(f"[cj-mens-toets] {t}", flush=True)


def check(ok, t):
    log(("OK   " if ok else "FOUT ") + t)
    if not ok:
        FOUT.append(t)


def mod(naam):
    return importlib.import_module("bl_ext.user_default.click_joints." + naam)


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    zip_pad, pad = args[0], args[1]
    A["installeer"](zip_pad)
    inst = bpy.context.scene.click_joints
    A["leeg"]()
    ob, punten = M["laad_mens"](pad)
    st = A["mesh_staat"](ob)
    if st["open_randen"] or st["randen_3plus"]:
        A["actief"](ob)
        bpy.ops.click_joints.maak_gesloten()
        nieuw = bpy.context.view_layer.objects.active
        if nieuw is not ob:
            bpy.data.objects.remove(ob)
            ob = nieuw
    naam = ob.name
    rig = M["maak_rig"](punten)
    ob.modifiers.new("Armature", "ARMATURE").object = rig
    inst.speling_mm, inst.as_bron, inst.uit_elkaar, inst.kogel_auto = 0.2, "CURSOR", False, True
    A["actief"](ob)
    voor = {m.name for m in bpy.data.meshes}
    herkans = os.environ.get("CJ_HERKANS") == "1"
    nep = []
    if herkans:
        # 23 nov (Olaf): in CI gaf het studio-figuur bij de linkerschouder één keer "no watertight parts" (één slechte
        # rand, per machine anders) en dan stopte de knop met zoeken: 8 gewrichten in CI, 9 lokaal. Hier doen we die
        # ene mislukte snede na op de eerste plek van de linkerschouder; de knop moet dan een volgende plek nemen.
        figm = mod("betaald.figuur")
        echt = figm.plaats_gewricht

        def plaats_nep(context, sleutel, naam=None, *a, **k):
            if naam == "Left shoulder" and not nep:
                nep.append(naam)
                return False, ("The cut gave no watertight parts (bad edges: part A 1, part B 0); "
                               "the mesh is unchanged."), []
            return echt(context, sleutel, naam, *a, **k)
        figm.plaats_gewricht = plaats_nep
    herkans2 = os.environ.get("CJ_HERKANS") == "2"
    heup = {"lijst": [], "laatste": None, "nu": None, "op_laatste": False, "geweigerd": 0, "laatste_ok": False}
    if herkans2:
        # 23 nov (Olaf, keuring a3f5e85 kan A5): op de robot van studio-2 gaf de heupsnede in CI (AMD) delen die in
        # rust al vastzaten ("blocked"), lokaal (Intel) niet. De fix is een laatste kandidaat 0,3 mm verder het lid
        # in. Hier doen we die kapotte snede na: op DOEL2 weigert de beweegproef elke plek behalve de
        # laatste. De knop moet dan bij die laatste plek uitkomen en het gewricht toch plaatsen.
        # Gemeten 23 nov 17:40 (lokaal 5.3.0, MakeHuman 220 mm): FAALT op elk lid. Heupen: de plek 0,3 mm verder is
        # "too close" (net als de eerste plek); 400 mm idem; linkerschouder: de plek 0,3 mm verder is "blocked",
        # de eerste plek gaf ±20. De omweg hielp op de robot, maar is geen algemene herkansing. Daarom nog NIET in
        # de e2e; proef voor Bram (keuring a3f5e85, A4: overlap meten direct na de snede).
        rigm2 = mod("betaald.rig")
        figm2 = mod("betaald.figuur")
        echt_schuif, echt_vast, echt_plaats = rigm2.kogel_schuif, rigm2.kogel_vast, figm2.plaats_gewricht

        def schuif_nep(*a, **k):
            uit = echt_schuif(*a, **k)
            heup["kand"] = ([mm for _m, mm in uit], uit[-1][0].to_translation().copy() if uit else None)
            return uit

        def plaats_tel(context, sleutel, naam=None, *a, **k):
            heup["nu"] = naam
            if naam == DOEL2:
                heup["lijst"], heup["laatste"] = heup.get("kand", ([], None))
                c = context.scene.cursor.matrix.to_translation()
                heup["op_laatste"] = heup["laatste"] is not None and (c - heup["laatste"]).length < 1e-5
            r = echt_plaats(context, sleutel, naam, *a, **k)
            if naam == DOEL2:
                log(f"{DOEL2}: laatste plek={heup['op_laatste']} ok={r[0]} melding={r[1]}")
            return r

        def vast_nep(nieuw):
            if heup["nu"] == DOEL2:
                if not heup["op_laatste"]:
                    heup["geweigerd"] += 1
                    return True
                vast = echt_vast(nieuw)
                heup["laatste_ok"] = heup["laatste_ok"] or not vast
                return vast
            return echt_vast(nieuw)
        rigm2.kogel_schuif, rigm2.kogel_vast, figm2.plaats_gewricht = schuif_nep, vast_nep, plaats_tel
    herkans3 = os.environ.get("CJ_HERKANS") == "3"
    verlies = {"nu": None, "kogels": [], "nep": 0}
    if herkans3:
        # 24 nov (keuring Betrouwbaarheid A, M1): het vangnet "lost part of the model" (rig.verloren_stuk, grens 6%)
        # geldt nu ook voor kogels. Hier verliest de eerste snede van de linkerschouder zogenaamd 50%: de knop moet die
        # snede terugdraaien en een volgende plek nemen, en de schouder toch plaatsen (in 5.x).
        rigm3 = mod("betaald.rig")
        figm3 = mod("betaald.figuur")
        echt_verloren, echt_plaats3 = rigm3.verloren_stuk, figm3.plaats_gewricht

        def plaats_tel3(context, sleutel, naam=None, *a, **k):
            verlies["nu"] = (naam, sleutel)
            return echt_plaats3(context, sleutel, naam, *a, **k)

        def verloren_nep(*a, **k):
            naam, sleutel = verlies["nu"] or (None, None)
            if sleutel in ("SHOULDER", "HIP", "NECK"):
                verlies["kogels"].append(naam)
            if naam == "Left shoulder" and not verlies["nep"]:
                verlies["nep"] += 1
                return 0.5
            return echt_verloren(*a, **k)
        rigm3.verloren_stuk, figm3.plaats_gewricht = verloren_nep, plaats_tel3
    try:
        r = bpy.ops.click_joints.figuur_uit_rig()
    except RuntimeError as e:
        r = f"fout {str(e).strip()[:300]}"
    if herkans3:
        rigm3.verloren_stuk, figm3.plaats_gewricht = echt_verloren, echt_plaats3
        log(f"verlies gemeten bij kogels: {verlies['kogels']}")
        check(len(verlies["kogels"]) >= 1, "het vangnet 'lost part of the model' meet ook bij kogelsneden")
        check(verlies["nep"] == 1 and verlies["kogels"].count("Left shoulder") >= 2,
              "na een kogelsnede die te veel verliest neemt de knop een volgende plek (linkerschouder)")
    if herkans:
        figm.plaats_gewricht = echt
        check(nep == ["Left shoulder"], f"mislukte snede nagedaan op de linkerschouder ({nep})")
    if herkans2:
        rigm2.kogel_schuif, rigm2.kogel_vast, figm2.plaats_gewricht = echt_schuif, echt_vast, echt_plaats
        lijst = heup["lijst"]
        log(f"{DOEL2}: kandidaten (mm) {[round(x, 2) for x in lijst]}, geweigerd {heup['geweigerd']}")
        check(len(lijst) >= 2 and abs(lijst[-1] - lijst[0] - 0.3) < 1e-6,
              "laatste heupkandidaat ligt 0,3 mm verder dan de eerste")
        check(heup["geweigerd"] >= 1 and heup["laatste_ok"],
              "na geweigerde heupplekken plaatst de knop de heup op de laatste plek (0,3 mm verder)")
    # 17 nov run 26: eerder bleven hier 172 lege tussenmeshes in het bestand.
    wees = [m.name for m in bpy.data.meshes if m.name not in voor and m.users == 0]
    check(not wees, f"geen lege tussenmeshes achtergebleven ({len(wees)})")
    fig = mod("betaald.figuur")
    ges = mod("gesloten")
    rigm = mod("betaald.rig")
    alle = fig.figuur_gewrichten(bpy.context.scene.objects, naam)
    per = {x["naam"]: x for x in alle}
    delen = [o for o in bpy.context.scene.objects if o.get("cj_figuur") == naam and o.visible_get() and o.type == "MESH"]
    over = next((o.get("cj_rig_overgeslagen") for o in delen if o.get("cj_rig_overgeslagen")), "") or ""
    log(f"uitslag={r} gewrichten={len(alle)}: {[fig.regel(x) for x in alle]}")
    log(f"overgeslagen: {over}")
    oud = bpy.app.version < (4, 5, 0)

    def bereik(n, graden, herkomst):
        x = per.get(n)
        ok = x is not None and x.get("herkomst") == herkomst and x.get("graden") is not None \
            and abs(float(x["graden"]) - graden) <= 3.0
        return ok, (fig.regel(x) if x else "ontbreekt")

    if oud:
        # Gemeten run 20 (4.2.23): ellebogen en nek lukken, knieën, heupen en schouders vallen af met reden
        # (overlap of geen gesloten delen met alleen Exact). Eerlijk in de tekst: "best in Blender 4.5 and newer".
        check(len(alle) >= 3, f"4.2: minstens 3 gewrichten ({len(alle)})")
    else:
        check(len(alle) >= 6, f"minstens 6 gewrichten ({len(alle)})")
        # Run 27: schouders blokkeerden in rechte stand (omhulsel H van een_lid haalde de bolnaad maar half uit deel A,
        # en een kruimel van 0,1 mm bij de elleboog telde als los stuk). Gemeten 5.3.0: beide schouders ±20, heupen ±25.
        for n in ("Left shoulder", "Right shoulder", "Left hip", "Right hip"):
            x = per.get(n)
            g = None if x is None or x.get("graden") is None else float(x["graden"])
            check(g is not None and g >= 15.0, f"{n} geplaatst en beweegt minstens ±15 ({fig.regel(x) if x else 'ontbreekt'})")
        for n, g, h in (("Left knee", 120, "from rig"), ("Right knee", 120, "mirrored")):
            ok, t = bereik(n, g, h)
            check(ok, f"{n}: 0–{g} {h} ({t})")
    for n, g, h in (("Left elbow", 140, "from rig"), ("Right elbow", 140, "mirrored")):
        ok, t = bereik(n, g, h)
        check(ok, f"{n}: 0–{g} {h} ({t})")
    if herkans3 and not oud:
        check("Left shoulder" in per, f"linkerschouder toch geplaatst na de geweigerde snede ({over[:200]})")
    standaard = [f"{k} {w}" for k in ("Left", "Right") for w in ("knee", "elbow", "hip", "shoulder")] + ["Neck"]
    mis = [n for n in standaard if n not in per]
    check(all(f"{n} (" in over for n in mis), f"elk overgeslagen gewricht met reden ({mis})")
    check(all(ges.is_gesloten(o)[0] for o in delen), f"alle {len(delen)} delen gesloten")
    stukken = [A["mesh_staat"](o)["losse_stukken"] for o in delen]
    check(all(s == 1 for s in stukken), f"elk deel één stuk ({stukken})")
    # Run 21: geen speelgoedkogel. Eerst lag de kogel op het bot aan de rand van de dij en koos de automatische maat
    # 2 tot 2,5 mm in een dij van 21 mm (Good fit, maar breekt bij het poseren). Nu in het midden van de doorsnede.
    kogels = {}
    for o in delen:
        if o.get("cj_deel") in ("A", "B") and o.get("cj_soort", "KOGEL") == "KOGEL" and o.get("cj_breedte_mm", -1) > 0:
            kogels[tuple(round(c, 2) for c in o["cj_centrum"])] = (2 * o["cj_kogel_r"], o["cj_breedte_mm"])
    log(f"kogels (diameter, breedte lid): {sorted(kogels.values())}")
    check(all(d >= rigm.KOGEL_MIN_DEEL * b - 1e-6 for d, b in kogels.values()),
          f"elke kogel minstens {rigm.KOGEL_MIN_DEEL} keer de breedte van het lid ({sorted(kogels.values())})")
    if not oud:
        heup = [d for d, b in kogels.values() if b > 15]
        check(len([d for d in heup if d >= 8.0]) >= 2, f"beide heupkogels minstens 8 mm in de dij ({heup})")
        # Run 21: de tweede heup komt er pas zonder de kernregel kogel naast kogel; dan moet elke kogel na alle
        # sneden nog net zo ver bewegen als bij zijn eigen snede (beweegproef opnieuw tegen de delen van nu).
        sc = bpy.context.scene
        heel = [(b.name, rigm.kogel_heel(bpy.context, naam, b)) for b in rigm.kogels_van_figuur(sc, naam)]
        check(heel and all(h for _n, h in heel), f"elke kogel beweegt na alle sneden nog even ver ({heel})")
    dg = bpy.context.evaluated_depsgraph_get()
    for p_naam in ("l-hand", "r-hand", "l-ankle", "r-ankle", "head"):
        p = punten[p_naam]
        binnen = any(rigm._in_kader(o, p) and rigm.binnen(o, p, dg)[0] for o in delen)
        check(binnen, f"{p_naam} {tuple(round(c, 1) for c in p)} ligt nog in een deel")
    log(f"KLAAR {len(FOUT)} FOUT")


main()
