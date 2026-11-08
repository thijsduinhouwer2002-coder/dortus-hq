"""Click Joints: snijdt een figuur in twee printbare delen met een kogel- of pengewricht."""
import bpy

from . import eigenschappen, exporteer, gesloten, gewricht, paneel

MODULES = (eigenschappen, gesloten, gewricht, exporteer, paneel)


def register():
    for m in MODULES:
        for k in m.KLASSEN:
            bpy.utils.register_class(k)
    eigenschappen.koppel()


def unregister():
    eigenschappen.ontkoppel()
    for m in reversed(MODULES):
        for k in reversed(m.KLASSEN):
            bpy.utils.unregister_class(k)
