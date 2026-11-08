"""Ronde e (punten van Daan, 8 nov 05:28): automatische kogelmaat (punt 9) en geen selectie na Place joint.
Alle maten in mm."""
import bpy

import figuren
from hulp import addon, delen, gesloten_delen, log, plaats, stap, toets_stl, weg


def alles(arm):
    inst = bpy.context.scene.click_joints
    # Zelf een diameter typen zet Auto uit.
    inst.kogel_auto = True
    inst.kogel_mm = 4.0
    stap("diameter typen zet Auto uit", not inst.kogel_auto)

    # Auto aan: de diameter volgt de dikte van de arm op de snede (arm 10 mm dik, golf +-3%).
    inst.kogel_auto = True
    inst.speling_mm, inst.soort, inst.as_bron = 0.2, "KOGEL", "CURSOR"
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    figuren.maak_actief(arm)
    uitslag = bpy.ops.click_joints.plaats()
    lijst = delen()
    d = inst.kogel_mm
    a = next((o for o in lijst if o.get("cj_deel") == "A"), None)
    breedte = a.get("cj_breedte_mm") if a else None
    passing = a.get("cj_passing") if a else None
    log(f"AUTO: uitslag={uitslag} breedte_op_snede={breedte}mm diameter={d}mm ({d / 10.0:.2f} x armdikte 10 mm) "
        f"passing={passing} wand={a.get('cj_wand_mm') if a else None}mm auto_na={inst.kogel_auto}")
    stap("auto: Auto blijft aan na Place joint", inst.kogel_auto)
    stap(f"auto: breedte gemeten 9,4 tot 10,4 mm ({breedte})", breedte is not None and 9.4 <= breedte <= 10.4)
    stap(f"auto: diameter 0,6 x breedte afgerond op 0,5 mm ({d})",
         breedte is not None and abs(d - round(0.6 * breedte * 2) / 2) < 1e-6)
    stap(f"auto: diameter 55 tot 65% van de armdikte ({d})", 5.5 <= d <= 6.5)
    stap(f"auto: kogel in de delen is {d} mm", a is not None and abs(2 * a["cj_kogel_r"] - d) < 1e-6)
    stap(f"auto: passing Good fit of Tight ({passing})", passing in ("groen", "oranje"))
    gesloten_delen("auto", lijst)

    # Geen selectie na Place joint (punt 2): geen oranje rand naast de passingkleur; export werkt toch.
    gekozen = [o.name for o in bpy.context.view_layer.objects if o.select_get()]
    actief = bpy.context.view_layer.objects.active
    log(f"SELECTIE na plaatsen: geselecteerd={gekozen} actief={actief.name if actief else None}")
    stap("na plaatsen: niets geselecteerd", not gekozen)
    stap("na plaatsen: deel A actief (paneel toont de passing)", actief is a)
    if len(lijst) == 2:
        toets_stl(lijst, "STL zonder selectie")
        gekozen = [o.name for o in bpy.context.view_layer.objects if o.select_get()]
        stap(f"na export: nog steeds niets geselecteerd ({gekozen})", not gekozen)
        inst.uit_elkaar = False
        bpy.context.view_layer.update()
        b = next(o for o in lijst if o["cj_deel"] == "B")
        stap("Exploded view uit zonder selectie: deel B op de echte plek", b.delta_location.length < 1e-9)
        inst.uit_elkaar = True
        bpy.context.view_layer.update()
        stap("Exploded view aan zonder selectie: deel B verschoven", b.delta_location.length > 0)
    weg(lijst)
    arm.hide_set(True)
    grootste_goede()
    geen_breedte()
    teksten()


def _auto_op(ob, punt):
    inst = bpy.context.scene.click_joints
    inst.kogel_auto = True
    inst.speling_mm, inst.soort, inst.as_bron = 0.2, "KOGEL", "CURSOR"
    figuren.zet_cursor(punt, (1, 0, 0))
    figuren.maak_actief(ob)
    uitslag = bpy.ops.click_joints.plaats()
    lijst = delen()
    a = next((o for o in lijst if o.get("cj_deel") == "A"), None)
    return uitslag, lijst, a


def _rode_tekens_weg():
    weg([o for o in bpy.context.scene.objects if o.get("cj_passing") == "rood" and not o.get("cj_deel")])


def grootste_goede():
    """Tussenreactie 2 van Daan, punt 2: Auto kiest de grootste kogel met Good fit (wand minstens 1,5 mm),
    niet een krappe. Staaf van 7 mm dik: groen. Staaf van 5 mm: groen kan niet, dan Tight of rood met keuze."""
    regel = addon("passing")
    staaf = figuren.staaf("staaf_7mm", 3.5)
    uitslag, lijst, a = _auto_op(staaf, (0, 0, 0))
    d = bpy.context.scene.click_joints.kogel_mm
    breedte = a.get("cj_breedte_mm") if a else None
    boven = regel.auto_diameter(breedte) if breedte else None
    log(f"AUTO GOED: staaf 7 mm uitslag={uitslag} breedte={breedte}mm bovengrens={boven}mm diameter={d}mm "
        f"passing={a.get('cj_passing') if a else None} wand={a.get('cj_wand_mm') if a else None}mm "
        f"keuze={a.get('cj_auto_keuze') if a else None}")
    stap("auto staaf 7 mm: twee delen", len(lijst) == 2)
    stap("auto staaf 7 mm: passing Good fit", a is not None and a.get("cj_passing") == "groen")
    stap("auto staaf 7 mm: wand minstens 1,5 mm", a is not None and a.get("cj_wand_mm", 0) >= 1.5)
    stap("auto staaf 7 mm: keuze goed", a is not None and a.get("cj_auto_keuze") == "goed")
    stap(f"auto staaf 7 mm: diameter {d} niet boven 0,6-regel {boven}", boven is not None and d <= boven + 1e-6)
    weg(lijst)
    if boven is not None and d + 0.5 <= boven + 1e-6:
        # Grootste: een halve mm groter mag geen Good fit meer zijn.
        groter = plaats("staaf 7 mm, auto + 0,5", staaf, (0, 0, 0), (1, 0, 0), kogel=d + 0.5)
        kleur = groter[0].get("cj_passing") if groter else next(
            (o.get("cj_passing") for o in bpy.context.scene.objects if o.get("cj_passing") == "rood"), None)
        log(f"AUTO GROTER: diameter {d + 0.5} mm passing={kleur}")
        stap(f"auto staaf 7 mm: {d + 0.5} mm is geen Good fit meer ({kleur})", kleur in ("oranje", "rood"))
        weg(groter)
        _rode_tekens_weg()

    dun = figuren.staaf("staaf_5mm", 2.5)
    uitslag, lijst, a = _auto_op(dun, (0, 0, 0))
    teken = next((o for o in bpy.context.scene.objects if o.get("cj_passing") == "rood" and not o.get("cj_deel")), None)
    bron = a or teken
    keuze = bron.get("cj_auto_keuze") if bron else None
    kleur = bron.get("cj_passing") if bron else None
    log(f"AUTO DUN: staaf 5 mm uitslag={uitslag} diameter={bpy.context.scene.click_joints.kogel_mm}mm "
        f"passing={kleur} wand={bron.get('cj_wand_mm') if bron else None}mm keuze={keuze}")
    stap(f"auto staaf 5 mm: geen Good fit mogelijk, keuze krap of regel ({keuze})", keuze in ("krap", "regel"))
    stap(f"auto staaf 5 mm: keuze past bij passing ({keuze}, {kleur})",
         (keuze, kleur) in (("krap", "oranje"), ("regel", "rood")))
    weg(lijst)
    _rode_tekens_weg()
    weg([staaf, dun])


def geen_breedte():
    """Cursor buiten het figuur: Auto vindt geen breedte, de oude maat blijft en Auto blijft aan."""
    inst = bpy.context.scene.click_joints
    staaf = figuren.staaf("staaf_buiten", 3.5)
    inst.kogel_mm = 4.0
    uitslag, lijst, a = _auto_op(staaf, (0, 30, 0))
    teken = next((o for o in bpy.context.scene.objects if o.get("cj_passing") == "rood" and not o.get("cj_deel")), None)
    log(f"AUTO BUITEN: uitslag={uitslag} delen={len(lijst)} diameter={inst.kogel_mm}mm auto={inst.kogel_auto} "
        f"breedte={teken.get('cj_breedte_mm') if teken else None}")
    stap("auto buiten figuur: diameter blijft 4,0 mm", abs(inst.kogel_mm - 4.0) < 1e-6)
    stap("auto buiten figuur: Auto blijft aan", inst.kogel_auto)
    stap("auto buiten figuur: niet gesneden, rood teken zonder breedte",
         not lijst and teken is not None and teken.get("cj_breedte_mm") == -1.0)
    weg(lijst)
    _rode_tekens_weg()
    weg([staaf])


def teksten():
    """passing.fit_tekst: Engelse tekst met de oorzaak, twee decimalen, geen haakjes in haakjes."""
    p = addon("passing")
    verwacht = {("groen", 1.62): "Good fit",
                ("oranje", 0.894): "Tight: wall 0.89 mm (aim for 1.5 mm or more)",
                ("rood", -1.0): "Too thin: joint sticks out of the mesh",
                ("rood", 0.456): "Too thin: wall 0.46 mm (minimum 0.8 mm)"}
    for (kleur, wand), tekst in verwacht.items():
        echt = p.fit_tekst(kleur, wand)
        stap(f"fit_tekst {kleur} {wand}: {echt!r}", echt == tekst and echt.count("(") <= 1)
