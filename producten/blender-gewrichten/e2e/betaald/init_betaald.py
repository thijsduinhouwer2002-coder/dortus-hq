

# Alleen in de betaalde build: maak_zip.sh zet dit achter __init__.py (ontwerp betaald v1.1).
from . import betaald as _betaald  # noqa: E402

_register_kern, _unregister_kern = register, unregister  # noqa: F821  (fragment achter __init__.py)


def register():  # noqa: F811
    _betaald.weiger_dubbel(__package__)
    _register_kern()
    _betaald.register(__package__)


def unregister():  # noqa: F811
    _betaald.unregister()
    _unregister_kern()
