"""Betaalde functies van Click Joints (alleen in de betaalde build, zie e2e/maak_zip.sh).

Het scharnier met eindstop (ontwerp betaald v1.1 in ontwerp.md): vorm in scharnier_vorm.py, operator en
paneelknoppen in scharnier.py. Ook de
weigering als de gratis versie uit een andere repository ook aan staat: zelfde id, dus anders botsen
operators, panelen en scene.click_joints."""
import addon_utils
import bpy

from .. import gewricht, uit_elkaar
from . import afstand, scharnier, scharnier_beweeg, scharnier_boog

ACTIEF = True
KLASSEN = scharnier.KLASSEN
MELDING = "Disable the free Click Joints first. Your settings stay in the .blend file."
MELDING_UIT = "Click Joints Pro was turned off. Disable the free Click Joints first, then enable Pro again."


def andere_versies(namen, eigen):
    """Modules van andere Click Joints-installaties (zelfde id, andere repository) die aan staan."""
    return [n for n in namen if n != eigen and (n == "click_joints" or n.endswith(".click_joints"))]


def weiger_dubbel(eigen):
    namen = [a.module for a in bpy.context.preferences.addons]
    if andere_versies(namen, eigen):
        raise RuntimeError(MELDING)


LAATSTE_MELDING = [None]  # voor de e2e: de laatste keer dat de betaalde opzij ging voor de gratis
_oude_enable = [None]


def _meld(melding=MELDING_UIT):
    """Melding in de console en (met scherm) als venstertje bij de muis."""
    LAATSTE_MELDING[0] = melding
    print(f"Click Joints: {melding}")
    if bpy.app.background:
        return
    try:
        bpy.context.window_manager.popup_menu(
            lambda self, _ctx: self.layout.label(text=melding), title="Click Joints", icon='ERROR')
    except Exception:
        pass


def _enable_met_wacht(eigen):
    """Tweede volgorde van eis 7: de betaalde staat aan en daarna wordt de gratis aangezet.

    De gratis code mag niet veranderen, dus de betaalde moet het merken. Gekozen: zolang de betaalde aan staat
    is addon_utils.enable omhuld. Elke weg om een add-on aan te zetten komt daar langs (het vinkje in de
    voorkeuren via preferences.addon_enable, installeren met "enable on install", het opstarten via
    addon_utils.reset_all, scripts). Wordt een andere Click Joints aangezet, dan zet de betaalde eerst
    zichzelf netjes uit (addon_utils.disable, dus zijn eigen unregister) en geeft de melding; pas daarna
    registreert de gratis zijn klassen.

    Waarom niet een timer of handler die achteraf kijkt: dan heeft de gratis zich al geregistreerd met
    dezelfde namen (operators, paneel, scene.click_joints). Zet de betaalde zich daarna uit, dan haalt zijn
    unregister juist scene.click_joints en klassen van de gratis weg, en de gratis is kapot. Vooraf opzij
    gaan heeft dat probleem niet, kost niets bij gewoon gebruik (geen timer die blijft lopen, alleen één
    naamvergelijking als er een add-on wordt aangezet) en bij uitzetten zet unregister de oude functie terug."""
    oud = _oude_enable[0]

    def enable(module_name, *args, **kwargs):
        if andere_versies([module_name], eigen) and eigen in {a.module for a in bpy.context.preferences.addons}:
            # default_set van de aanroep volgen (kan-punt controleur eis 7); het vinkje in de voorkeuren geeft True.
            addon_utils.disable(eigen, default_set=bool(kwargs.get("default_set", False)))
            _meld()
        return oud(module_name, *args, **kwargs)

    enable.__wrapped__ = oud
    enable._actief = True  # alleen terugzetten als addon_utils.enable nog ons omhulsel is
    return enable


_oude_afstand = [None]


def _afstand(ob):
    """Eis 6: Exploded view schuift deel B van een scharnier 1,5 keer de wangdiameter (3 Rn = 3 cj_naad_r) langs
    de lidas; de tong reikt tot R onder H en de wangen van A tot Rn - s/2 erboven, dus de tong komt helemaal uit
    de vork. Anders (kogel) de functie van het gratis deel, dat zelf niet verandert."""
    if ob.get("cj_soort") == "SCHARNIER":
        return uit_elkaar.FACTOR * 2.0 * float(ob.get("cj_naad_r", 0.0))
    return _oude_afstand[0](ob)


_oude_zet = [None]


def _zet(ob, aan):
    """Weergave van deel B: bij een scharnier de eigen pose om H (scharnier_beweeg.zet_scharnier), anders de
    functie van het gratis deel. Zonder dit zou Exploded view aan of uit de kogelpose op een scharnier zetten."""
    if ob.get("cj_soort") == "SCHARNIER" and ob.get("cj_deel") == "B" and "cj_scharnier_punt" in ob:
        scharnier_beweeg.zet_scharnier(ob, aan)
        return
    _oude_zet[0](ob, aan)


def _scharnier_recht():
    """Bij uitzetten van Pro: deel B van elk scharnier weer recht in beeld (pose 0, delta's op nul), anders zou
    het gratis deel bij Exploded view de kogelpose op een scharnier zetten (kan-punt controleur eis 8)."""
    try:
        delen = [o for o in bpy.data.objects if o.get("cj_soort") == "SCHARNIER" and o.get("cj_deel") == "B"]
    except (AttributeError, TypeError):  # bpy.data is bij opstarten soms afgeschermd
        return
    for o in delen:
        o["cj_pose_graden"] = 0.0
        o.delta_location = (0.0, 0.0, 0.0)
        o.delta_rotation_euler = (0.0, 0.0, 0.0)
        o.delta_rotation_quaternion = (1.0, 0.0, 0.0, 0.0)


def register(eigen=None):
    for k in KLASSEN:
        bpy.utils.register_class(k)
    # Keuze voor de knoppen in het paneel (niet in de .blend, zoals een knop in een werkbalk).
    bpy.types.WindowManager.cj_flip_bend = bpy.props.BoolProperty(
        name="Flip bend", default=False, description="Bend the other way: the end stop moves to the other side")
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.append(scharnier.teken_knop)
    scharnier_boog.register()  # eis 8: gradenboog en pose-schuif van het scharnier
    # Omhullen pas als alles staat (kan-punt controleur eis 7), zodat een fout hierboven geen omhulsel achterlaat.
    # uit_elkaar.zet (en via zet_alle ook bij_wissel) zoekt afstand en zet op in de module.
    if _oude_afstand[0] is None:
        _oude_afstand[0] = uit_elkaar.afstand
        uit_elkaar.afstand = _afstand
    if _oude_zet[0] is None:
        _oude_zet[0] = uit_elkaar.zet
        uit_elkaar.zet = _zet
    afstand.register(gewricht)  # kogel naast scharnier: gewricht.te_dicht en gewricht.markeer (zie afstand.py)
    if _oude_enable[0] is None and eigen:
        _oude_enable[0] = addon_utils.enable
        addon_utils.enable = _enable_met_wacht(eigen)


def unregister():
    scharnier_boog.unregister()
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.remove(scharnier.teken_knop)
    if hasattr(bpy.types.WindowManager, "cj_flip_bend"):
        del bpy.types.WindowManager.cj_flip_bend
    for k in reversed(KLASSEN):
        bpy.utils.unregister_class(k)
    _scharnier_recht()
    if _oude_afstand[0] is not None:
        if uit_elkaar.afstand is _afstand:  # alleen terugzetten als het nog ons omhulsel is
            uit_elkaar.afstand = _oude_afstand[0]
        _oude_afstand[0] = None
    if _oude_zet[0] is not None:
        if uit_elkaar.zet is _zet:
            uit_elkaar.zet = _oude_zet[0]
        _oude_zet[0] = None
    afstand.unregister(gewricht)
    if _oude_enable[0] is not None:
        if getattr(addon_utils.enable, "_actief", False):  # iemand anders omhulde daarna: niet overschrijven
            addon_utils.enable = _oude_enable[0]
        _oude_enable[0] = None
