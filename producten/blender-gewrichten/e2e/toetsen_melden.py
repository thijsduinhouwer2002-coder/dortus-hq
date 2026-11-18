"""Roestronde R5: de knop "Report a problem" (click_joints/meld.py). Draait vanuit test_achtergrond.py, voor de gratis
en de betaalde zip. Toetst: operator en paneel bestaan, het paneel is een subpaneel van het hoofdpaneel (dus onderaan, ook onder de knoppen
van de betaalde build; GEZIEN op een scherm in Blender 4.2), en de link heeft de naam
en versie uit de manifest van de geïnstalleerde zip (dus "Click Joints Pro" in de betaalde build en "Click Joints" in
de gratis, zonder dat de code die naam noemt), de Blender-versie en het systeem. De browser openen wordt niet getoetst
(wm.url_open zonder scherm), wel dat de operator precies die link doorgeeft."""
import tomllib
import zipfile
from urllib.parse import parse_qs, urlsplit

import bpy

from hulp import addon, log, stap


def alles(zip_pad):
    with zipfile.ZipFile(zip_pad) as z:
        m = tomllib.loads(z.read("blender_manifest.toml").decode("utf-8"))
    naam, versie = m["name"], m["version"]
    meld = addon("meld")

    stap("melden: operator click_joints.meld bestaat", "meld" in dir(bpy.ops.click_joints))
    stap("melden: paneel CLICK_JOINTS_PT_meld geregistreerd", hasattr(bpy.types, "CLICK_JOINTS_PT_meld"))
    ouder = getattr(bpy.types.CLICK_JOINTS_PT_meld, "bl_parent_id", "")
    stap(f"melden: subpaneel onderaan het hoofdpaneel (bl_parent_id {ouder})", ouder == "CLICK_JOINTS_PT_paneel")
    stap("melden: knoptekst", meld.CLICK_JOINTS_OT_meld.bl_label == "Report a problem")

    url = meld.url_hier()
    log(f"MELDEN url ({len(url)} tekens): {url}")
    delen = urlsplit(url)
    stap("melden: loketrepo click-joints",
         f"{delen.scheme}://{delen.netloc}{delen.path}" == "https://github.com/thijsduinhouwer2002-coder/click-joints/issues/new")
    stap("melden: geen template (werkt ook zonder formulier)", "template" not in parse_qs(delen.query))
    v = {k: w[0] for k, w in parse_qs(delen.query).items()}
    stap(f"melden: versie uit de manifest ({naam} {versie})", v.get("version") == f"{naam} {versie}")
    stap("melden: Blender-versie", v.get("blender") == bpy.app.version_string)
    stap("melden: systeem", v.get("os") == meld.systeem() and len(v.get("os", "")) > 3)
    body = v.get("body", "")
    stap("melden: body met dezelfde gegevens",
         f"Add-on: {naam} {versie}" in body and f"Blender: {bpy.app.version_string}" in body and "OS: " in body)
    stap("melden: link ver onder de grens van GitHub", len(url) < 2000)

    # De operator geeft precies deze link aan wm.url_open (vervangen door een nep, er gaat geen browser open).
    gekregen = []
    echt = meld.bpy

    class NepOps:
        class wm:
            @staticmethod
            def url_open(url):
                gekregen.append(url)
                return {"FINISHED"}

    class NepBpy:
        ops = NepOps
        app = echt.app

    meld.bpy = NepBpy
    try:
        uit = meld.CLICK_JOINTS_OT_meld.execute(None, bpy.context)
    finally:
        meld.bpy = echt
    stap("melden: operator opent de link", uit == {"FINISHED"} and gekregen == [url])
