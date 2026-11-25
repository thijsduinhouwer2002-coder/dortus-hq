"""Knop "Report a problem" onder het paneel (roestronde R5): opent een nieuwe melding op GitHub met de naam en versie
van de add-on, de Blender-versie en het systeem al ingevuld.

Alleen een link die de gebruiker zelf opent (wm.url_open), niets gaat vanzelf het netwerk op. Naam en versie komen uit
blender_manifest.toml naast dit bestand, zodat elke build zijn eigen naam en versie meestuurt zonder dat de code ze
noemt. Bewust geen template= in de URL: zolang het meldformulier nog niet in de loketrepo staat, werkt de link dan ook
(gewone melding met de body ingevuld). De velden version, blender en os hebben dezelfde id als in het formulier."""
import os
import platform
import tomllib
from urllib.parse import quote

import bpy

LOKET = "https://github.com/thijsduinhouwer2002-coder/click-joints"


def manifest():
    """(naam, versie) uit blender_manifest.toml van deze add-on."""
    try:
        with open(os.path.join(os.path.dirname(__file__), "blender_manifest.toml"), "rb") as f:
            m = tomllib.load(f)
        return m.get("name", "Click Joints"), m.get("version", "unknown")
    except (OSError, tomllib.TOMLDecodeError):
        return "Click Joints", "unknown"


def systeem():
    """Besturingssysteem zonder gebruikersnaam of paden, bijvoorbeeld "Linux 6.8.0 (x86_64)"."""
    return f"{platform.system()} {platform.release()} ({platform.machine()})"


def body(naam, versie, blender, os_tekst):
    return ("**What happened?**\n\n\n"
            "**What did you expect?**\n\n\n"
            "**Steps to reproduce** (a screenshot of the panel or a small .blend helps a lot)\n\n\n"
            "---\n"
            f"Add-on: {naam} {versie}\n"
            f"Blender: {blender}\n"
            f"OS: {os_tekst}")


def url(naam, versie, blender, os_tekst):
    velden = (("version", f"{naam} {versie}"), ("blender", blender), ("os", os_tekst),
              ("body", body(naam, versie, blender, os_tekst)))
    return f"{LOKET}/issues/new?" + "&".join(f"{k}={quote(v, safe='')}" for k, v in velden)


def url_hier():
    naam, versie = manifest()
    return url(naam, versie, bpy.app.version_string, systeem())


# Beoordelen (issue 70, gat 3 in de lat: Cleave, Split 3D Print en JointLab hebben er elk 3, wij 0). Eén rustige regel
# onder het paneel, geen popup, niets in ruil. Issue 100: pas na een Good fit én een export (eerder heeft de gebruiker
# nog niets om te printen), en weg na een klik op een winkel, ook in een ander bestand. Link nagekeken met curl op
# 25 nov (200). Een andere build zet hier zijn eigen winkels in (en zet bij uitzetten deze terug).
BEOORDEEL_GRATIS = (("Blender Extensions", "https://extensions.blender.org/add-ons/click-joints/reviews/"),)
BEOORDEEL = list(BEOORDEEL_GRATIS)
MERK = "rating_asked"


def goed_resultaat(objecten):
    """True zodra er in de scène een gewricht met "Good fit" (groen) staat."""
    return any(ob.get("cj_passing") == "groen" for ob in objecten)


def merkbestand():
    """Pad van het merkje in de gebruikersmap van deze extensie (blijft over bestanden heen), of None als de add-on
    niet als extensie draait (dan alleen de scène)."""
    try:
        return os.path.join(bpy.utils.extension_path_user(__package__, create=True), MERK)
    except Exception:
        return None


def al_gevraagd(scene):
    pad = merkbestand()
    return bool(scene.get("cj_beoordeeld")) or bool(pad and os.path.exists(pad))


def onthoud(scene):
    """Na een klik op een winkel: niet meer vragen, in deze scène en (als het kan) in elk bestand."""
    scene["cj_beoordeeld"] = True
    pad = merkbestand()
    if pad:
        try:
            with open(pad, "w", encoding="utf-8") as f:
                f.write("1")
        except OSError:
            pass


def vraag_beoordeling(scene):
    """Regel tonen: Good fit, er is geëxporteerd (exporteer.py zet cj_laatste_export) en nog niet geklikt."""
    return "cj_laatste_export" in scene and goed_resultaat(scene.objects) and not al_gevraagd(scene)


class CLICK_JOINTS_OT_beoordeel(bpy.types.Operator):
    bl_idname = "click_joints.beoordeel"
    bl_label = "Leave a rating"
    bl_description = "Open the store page to leave a rating"
    bl_options = {"INTERNAL"}

    url: bpy.props.StringProperty(options={"SKIP_SAVE"})

    def execute(self, context):
        bpy.ops.wm.url_open(url=self.url)
        onthoud(context.scene)
        return {"FINISHED"}


class CLICK_JOINTS_OT_meld(bpy.types.Operator):
    bl_idname = "click_joints.meld"
    bl_label = "Report a problem"
    bl_description = "Open a bug report on GitHub with the add-on, Blender and system versions filled in"

    def execute(self, context):
        bpy.ops.wm.url_open(url=url_hier())
        return {"FINISHED"}


class CLICK_JOINTS_PT_meld(bpy.types.Panel):
    """Subpaneel zonder kop onderaan het hoofdpaneel, zodat paneel.py gelijk blijft en de knop altijd als laatste
    staat, ook onder knoppen die andere code aan het hoofdpaneel hangt (een los paneel zonder kop zet Blender
    juist bovenaan, GEZIEN in Blender 4.2)."""
    bl_label = "Report a problem"
    bl_idname = "CLICK_JOINTS_PT_meld"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Click Joints"
    bl_parent_id = "CLICK_JOINTS_PT_paneel"
    bl_options = {"HIDE_HEADER"}

    def draw(self, context):
        if vraag_beoordeling(context.scene):
            kol = self.layout.column(align=True)
            kol.label(text="Happy with it? Leave a rating:", icon="SOLO_OFF")  # past in een smalle zijbalk
            rij = kol.row(align=True)
            for winkel, link in BEOORDEEL:
                rij.operator(CLICK_JOINTS_OT_beoordeel.bl_idname, text=winkel, icon="URL").url = link
        self.layout.operator(CLICK_JOINTS_OT_meld.bl_idname, icon="URL", emboss=False)


KLASSEN = (CLICK_JOINTS_OT_meld, CLICK_JOINTS_OT_beoordeel, CLICK_JOINTS_PT_meld)
