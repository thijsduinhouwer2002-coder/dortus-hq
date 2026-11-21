

# Alleen in de direct-zip: maak_zip.sh direct zet dit achter __init__.py (Pro-knoppen op slot, Afkijker 21 nov).
from . import direct as _direct  # noqa: E402

_register_kern, _unregister_kern = register, unregister  # noqa: F821  (fragment achter __init__.py)


def register():  # noqa: F811
    _register_kern()
    _direct.register()


def unregister():  # noqa: F811
    _direct.unregister()
    _unregister_kern()
