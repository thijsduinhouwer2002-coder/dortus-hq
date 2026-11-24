"""Slotzin naar de koopknop en geen "not print tested" meer (Regisseur run 25, 24 nov 2026).

Waarom: opdracht hoofdchat 24 nov 16:05 (elke Short eindigt met "Click Joints Pro, on Gumroad", ja Thijs 15:59)
en besluit Thijs 24 nov 15:32 (nergens meer "not print tested by us yet"). Alleen het scenebestand verandert,
dus de workflow hergebruikt de ruwe opname en monteert alleen opnieuw.

Gebruik: python3 slotzin.py <scenes.json> <soort>   soort: tip | pro | gratis | cc | es
Schrijft het json-bestand terug en zet de voorleestekst (<naam>-stem.txt) opnieuw neer.
"""
import json
import sys
from pathlib import Path

PRINT_EN = "Every printer is different: print a test joint first."
PRINT_CC = "Every printer is different: print the fit test first."
PRINT_TIP = "Every printer is different: print a small test first."
PRINT_ES = "Cada impresora es distinta: imprime antes una prueba."

SLOT = {
    "tip": ("Make your prints poseable: Click Joints Pro, on Gumroad.", "Make your 3D prints poseable."),
    "pro": ("Click Joints Pro, on Gumroad.", "Elbows and knees stop where your rig stops."),
    "gratis": ("Click Joints is free. Want more? Click Joints Pro, on Gumroad.", "Make your 3D prints poseable."),
    "es": ("¿Quieres más? Click Joints Pro, en Gumroad.", "Figuras articuladas en Blender."),
}


def eerlijk(tekst, soort):
    """Vervang de oude eerlijkheidszin; laat de tweede zin (Save this ..., Print ... first) staan."""
    oud = ["Measured in Blender, not print tested by us yet.", "Not print tested by us yet.",
           "Medido en Blender; todavía no lo hemos impreso."]
    for o in oud:
        if tekst.startswith(o):
            rest = tekst[len(o):].strip()
            if soort == "es":
                return "Cada impresora es distinta. " + (rest or "Imprime antes una prueba.")
            if soort == "cc":
                return "Every printer is different. " + (rest or "Print the fit test first.")
            if rest.lower().startswith("print a test joint first") or rest.lower().startswith("print the fit test"):
                return "Every printer is different. " + rest
            return "Every printer is different, so print a small test first. " + rest
    return tekst


def main():
    pad, soort = Path(sys.argv[1]), sys.argv[2]
    j = json.loads(pad.read_text())
    j["printzin"] = {"cc": PRINT_CC, "es": PRINT_ES, "tip": PRINT_TIP}.get(soort, PRINT_EN)
    for sc in j["scenes"]:
        nieuw = eerlijk(sc["tekst"], soort)
        if nieuw != sc["tekst"]:
            sc["tekst"] = nieuw
            sc.pop("uitspraak", None)
            if sc.get("label") in ("HONEST", "HONESTO"):
                sc["label"] = "PRINT FIRST" if soort != "es" else "PRIMERO"
    if soort in SLOT:
        zin, onder = SLOT[soort]
        laatste = j["scenes"][-1]
        assert laatste["beeld"].get("eindkaart"), "laatste scene is geen eindkaart"
        laatste["tekst"] = zin
        laatste["uitspraak"] = zin.replace("3D", "three D")
        laatste["label"] = "CLICK JOINTS PRO"
        laatste["kleur"] = "groen"
        j["eind"]["titel"] = "Click Joints Pro"
        j["eind"]["zin"] = onder
        j["eind"]["adres"] = "en Gumroad" if soort == "es" else "on Gumroad"
        j["eind"].pop("icoon", None)
    tekst = json.dumps(j, ensure_ascii=False, indent=1)
    assert "print tested" not in tekst and "lo hemos impreso" not in tekst, "oude zin staat er nog"
    pad.write_text(tekst + "\n")
    stem = pad.with_name(pad.stem + "-stem.txt")
    kop = [r for r in (stem.read_text().splitlines() if stem.exists() else []) if r.startswith("#")]
    kop.append("# Bijgewerkt Regisseur run 25 (24 nov): slotzin naar Gumroad, geen 'not print tested' meer.")
    zinnen = [sc.get("uitspraak") or sc["tekst"] for sc in j["scenes"]]
    stem.write_text("\n".join(kop) + "\n\n" + "\n".join(zinnen) + "\n")
    print(pad, "OK", len(zinnen), "zinnen")


if __name__ == "__main__":
    main()
