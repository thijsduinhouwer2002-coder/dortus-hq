"""Alleen in de direct-zip (gratis download van dortus.com en GitHub, NIET op extensions.blender.org).

Onder de gratis knoppen drie Pro-functies met een slotje. Een klik geeft een klein venster "This is in Click Joints
Pro" met één knop naar de Pro-pagina. Onderaan één regel "Upgrade to Pro" met dezelfde link. Geen prijs in Blender
(die verandert). Voorbeeld: TrailPrint3D (Afkijker 21 nov). maak_zip.sh direct zet dit bestand als direct.py in de zip
en het fragment init_direct.py achter __init__.py; de extensions-zip blijft byte voor byte gelijk.

Alleen een link die de gebruiker zelf opent (wm.url_open), niets gaat vanzelf het netwerk op."""
import bpy

ACTIEF = True
URL = "https://dortus.com/click-joints/?from=addon#pro"
FUNCTIES = ("Figure from rig", "Hinge with end stop", "Body-part presets")
VENSTER = "This is in Click Joints Pro"
KNOP = "See Click Joints Pro"
ONDERAAN = "Upgrade to Pro"


class CLICK_JOINTS_OT_pro_slot(bpy.types.Operator):
    bl_idname = "click_joints.pro_slot"
    bl_label = "Click Joints Pro"
    bl_description = "This is in Click Joints Pro"
    bl_options = {"INTERNAL"}

    functie: bpy.props.StringProperty(default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=260)

    def draw(self, context):
        kol = self.layout.column()
        if self.functie:
            kol.label(text=self.functie, icon="LOCKED")
        kol.label(text=VENSTER)
        kol.operator("wm.url_open", text=KNOP, icon="URL").url = URL

    def execute(self, context):
        return {"FINISHED"}


def teken(self, context):
    """Hangt onder het hoofdpaneel van de kern (CLICK_JOINTS_PT_paneel.append), boven "Report a problem"."""
    vak = self.layout.box()
    kol = vak.column(align=True)
    for f in FUNCTIES:
        kol.operator(CLICK_JOINTS_OT_pro_slot.bl_idname, text=f, icon="LOCKED").functie = f
    self.layout.operator("wm.url_open", text=ONDERAAN, icon="URL").url = URL


KLASSEN = (CLICK_JOINTS_OT_pro_slot,)


def register():
    for k in KLASSEN:
        bpy.utils.register_class(k)
    bpy.types.CLICK_JOINTS_PT_paneel.append(teken)


def unregister():
    paneel = getattr(bpy.types, "CLICK_JOINTS_PT_paneel", None)
    if paneel is not None:
        paneel.remove(teken)
    for k in reversed(KLASSEN):
        bpy.utils.unregister_class(k)
