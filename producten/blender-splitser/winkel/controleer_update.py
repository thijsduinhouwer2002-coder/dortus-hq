"""Kijkt update-1.1.md na tegen de tak: changelog, versie, woorden in de code, startspeling en de plek in de beschrijving.

Draaien vanuit de root van de repo: python3 producten/blender-splitser/winkel/controleer_update.py
Waarom (#248): de winkeltekst van 1.1 mag niets beloven wat niet in de zip zit.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROD = ROOT / "producten/blender-splitser"
HIER = Path(__file__).resolve().parent


def main():
    tekst = (HIER / "update-1.1.md").read_text()
    blokken = re.findall(r"```\n(.*?)```", tekst, flags=re.S)
    fouten = []

    # 1. versie in het manifest
    man = (PROD / "split_joints/blender_manifest.toml").read_text()
    if 'version = "1.1.0"' not in man:
        fouten.append("manifest is niet 1.1.0")

    # 2. releasenote = kop 1.1.0 van de changelog, regel voor regel, hooguit 5 regels
    log = (PROD / "CHANGELOG.md").read_text()
    m = re.search(r"## 1\.1\.0[^\n]*\n(.*?)\n## ", log, flags=re.S)
    if not m:
        fouten.append("geen kop 1.1.0 in CHANGELOG.md")
    else:
        uit_log = [r for r in m.group(1).splitlines() if r.strip()]
        note = [r for r in blokken[0].splitlines()[1:] if r.strip()]
        if uit_log != note:
            fouten.append("releasenote wijkt af van CHANGELOG.md 1.1.0")
        if len(uit_log) > 5:
            fouten.append(f"changelog 1.1.0 heeft {len(uit_log)} regels (hooguit 5)")

    # 3. elke knopnaam en melding die de tekst noemt, staat in de code
    code = "\n".join(p.read_text() for p in (PROD / "split_joints").glob("*.py"))
    for woord in ["Draw cut", "Flip side", "comes off", "Add free cut", "Cut piece", "Split to fit",
                  "Clearance changed: press"]:
        if woord in tekst or woord in log:
            if woord not in code:
                fouten.append(f"niet in de code: {woord}")

    # 4. startspeling per materiaal gelijk aan passing.py
    sp = re.search(r"STARTSPELING = \{(.*?)\}", (PROD / "split_joints/passing.py").read_text()).group(1)
    waarden = {k: float(v) for k, v in re.findall(r'"(\w+)": ([0-9.]+)', sp)}
    verwacht = {"RESIN": 0.10, "PLA": 0.20, "PETG": 0.25, "ABS": 0.25, "TPU": 0.30}
    for k, v in verwacht.items():
        if abs(waarden.get(k, -1) - v) > 1e-9:
            fouten.append(f"startspeling {k} is {waarden.get(k)} in de code, tekst zegt {v}")

    # 5. de twee regels die vervangen worden, staan zo in de beschrijving van lancering.md
    lan = (HIER / "lancering.md").read_text()
    for kop in ["- **Free cut:**", "- **Fit test:**"]:
        if lan.count(kop) != 1:
            fouten.append(f"regel {kop} staat niet precies één keer in lancering.md")

    # 6. uitgave-workflow niet meer vast op 1.0.0
    wf = (ROOT / ".github/workflows/click-cuts-uitgave.yml").read_text()
    if 'VERSIE: "1.0.0"' in wf:
        fouten.append("click-cuts-uitgave.yml staat nog vast op 1.0.0")

    # 7. geen beweringen die niet mogen
    for zin in ["print tested", "not print tested", "AI", "clicks together"]:
        if re.search(rf"\b{re.escape(zin)}\b", "\n".join(blokken)):
            fouten.append(f"verboden in een plakblok: {zin}")

    print(f"{len(blokken)} plakblokken nagekeken.")
    for f in fouten:
        print("FOUT:", f)
    print("OK" if not fouten else f"{len(fouten)} fouten")
    return 1 if fouten else 0


if __name__ == "__main__":
    sys.exit(main())
