"""Toetsen voor de teksten die de gebruiker ziet (kan-punt controleur ronde j): "Bends ±N°" in het paneel,
"Too thin here ..." en "Too close ..." als melding. De verwachte teksten staan hier letterlijk, los van de add-on.

Een melding van een operator (self.report) schrijft Blender in een script naar de uitvoer als "Warning: ...".
Daarom vangt `vang` de uitvoer op, zowel van Python (sys.stdout) als op bestandsniveau (fd 1), en zet hem daarna
gewoon weer in het log, zodat er niets uit het bewijs verdwijnt. Alle maten in mm."""
import contextlib
import ctypes
import io
import os
import sys
import tempfile

import bpy

import figuren
from hulp import addon, delen, log, plaats, stap, weg

TE_DUN = "Too thin here for a ball joint. Try a thicker spot."


@contextlib.contextmanager
def vang(uit):
    """Vangt alles wat er tijdens het blok naar de uitvoer gaat in de lijst `uit` (één tekst)."""
    libc = ctypes.CDLL(None)  # libc van het proces zelf; werkt op Linux (CI) en macOS, niet op Windows
    sys.stdout.flush()
    libc.fflush(None)
    oud = os.dup(1)
    buf = io.StringIO()
    with tempfile.TemporaryFile() as f:
        os.dup2(f.fileno(), 1)
        try:
            with contextlib.redirect_stdout(buf):
                yield
        finally:
            sys.stdout.flush()
            libc.fflush(None)
            os.dup2(oud, 1)
            os.close(oud)
            f.seek(0)
            tekst = buf.getvalue() + f.read().decode("utf-8", "replace")
            uit.append(tekst)
            print(tekst, end="", flush=True)  # terug in het log


def bends():
    """Staaf 10 mm met kogel 5 mm: stand 25, gemeten ±25,4 (toetsen_beweeg). Paneel moet precies "Bends ±25°" tonen."""
    st = figuren.staaf("staaf_tekst", 5.0, lengte=40.0)
    lijst = plaats("TEKST staaf", st, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    stap("TEKST staaf: twee delen", len(lijst) == 2)
    if len(lijst) != 2:
        weg([st])
        return
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    tekst = addon("paneel").buig_tekst(a)
    log(f"TEKST paneel: {tekst!r} (stand {a.get('cj_hoek')}, gemeten {list(a.get('cj_buig_graden', []))})")
    stap(f"TEKST paneel toont precies 'Bends ±25°' (kreeg {tekst!r})", tekst == "Bends ±25°")
    te_dicht(b)
    weg(lijst)
    st.hide_set(True)


def te_dicht(b):
    """Tweede gewricht 8 mm verder op deel B: te dicht. Afstand zelf gerekend (controleur): bolnaad nieuw
    straal 5 + marge 0,5 + speling 0,2 = 5,7, plus nek 0,4r = 1,0 is 6,7; kom oud r + s = 2,7; samen 9,4,
    naar boven afgerond 10 mm."""
    inst = bpy.context.scene.click_joints
    inst.uit_elkaar = False
    inst.speling_mm, inst.kogel_mm, inst.soort, inst.as_bron, inst.kogel_auto = 0.2, 5.0, "KOGEL", "CURSOR", False
    figuren.zet_cursor((8, 0, 0), (1, 0, 0))
    figuren.maak_actief(b)
    uit = []
    try:
        with vang(uit):
            try:
                uitslag = bpy.ops.click_joints.plaats()
            except RuntimeError as fout:
                uitslag = {"FOUT: " + str(fout)}
        nodig = b.get("cj_te_dicht_mm")
        nieuw = [d for d in delen() if d.get("cj_bron") == b.name]
        verwacht = "Too close to another joint (keep 10 mm apart)."
        log(f"TEKST te dicht: uitslag={uitslag}, cj_te_dicht_mm={nodig}, nieuwe delen={len(nieuw)}")
        stap(f"TEKST te dicht: geweigerd met afstand 10 mm (kreeg {nodig})",
             uitslag == {"CANCELLED"} and nodig == 10 and not nieuw)
        stap(f"TEKST te dicht: melding precies '{verwacht}'", f"Warning: {verwacht}" in uit[0])
        weg(nieuw)
    finally:
        inst.uit_elkaar = True


def te_dun():
    """Staaf van 3,1 mm straal met kogel 5 mm: rood, niet gesneden, melding TE_DUN; paneel toont dan geen Bends."""
    st = figuren.staaf("staaf_tekst_dun", 3.1)
    uit = []
    with vang(uit):
        lijst = plaats("TEKST dun", st, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    rood = [o for o in bpy.context.scene.objects if o.get("cj_passing") == "rood" and o.get("cj_bron") == st.name]
    stap(f"TEKST dun: niet gesneden, rood teken ({len(lijst)} delen, {len(rood)} rood)", not lijst and len(rood) == 1)
    stap(f"TEKST dun: melding precies '{TE_DUN}'", f"Warning: {TE_DUN}" in uit[0])
    if rood:
        tekst = addon("paneel").buig_tekst(rood[0])
        stap(f"TEKST dun: paneel toont geen Bends bij rood (kreeg {tekst!r})", tekst is None)
    weg(lijst + rood)
    weg([st])


def alles():
    bends()
    te_dun()
