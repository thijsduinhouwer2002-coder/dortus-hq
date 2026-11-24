"""Click Cuts: cuts a model that is too big for the printer into pieces with pins that fit."""
from . import eigenschappen, exporteer, gesloten, in_een_klik, paneel, passingproef, schaal, snedes, splitsen, vrije_snede

MODULES = (eigenschappen, gesloten, schaal, snedes, splitsen, vrije_snede, in_een_klik, exporteer, passingproef, paneel)


def register():
    import bpy
    for m in MODULES:
        for k in m.KLASSEN:
            bpy.utils.register_class(k)
    eigenschappen.koppel()
    passingproef.koppel()


def unregister():
    import bpy
    passingproef.ontkoppel()
    eigenschappen.ontkoppel()
    for m in reversed(MODULES):
        for k in reversed(m.KLASSEN):
            bpy.utils.unregister_class(k)
