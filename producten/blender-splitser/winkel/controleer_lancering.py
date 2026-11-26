"""Kijkt lancering.md na: elk pad bestaat, en elke regel in een plakblok staat letterlijk in een gekeurde bron.

Draaien vanuit de root van de repo: python3 producten/blender-splitser/winkel/controleer_lancering.py
Waarom: de lanceerbundel mag geen eigen tekst hebben; zo zie je meteen als een bron later verandert.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HIER = Path(__file__).resolve().parent
BUNDEL = HIER / "lancering.md"
BRONNEN = [
    ROOT / "producten/blender-splitser/galerij.md",
    ROOT / "platformen/blender/superhive/click-cuts-winkeltekst.md",
]
ZOEKMAPPEN = [ROOT, ROOT / "organisatie/blindtest/uitslag", ROOT / "ontwerp/cuts-galerij/beelden",
              ROOT / "ontwerp/cuts-hoofdbeeld/beelden", HIER]


def schoon(regel):
    """Regel zonder citaat-teken, opsommingsteken en vet, zodat bron en bundel vergelijkbaar zijn."""
    r = regel.strip()
    r = re.sub(r"^>\s*", "", r)
    r = re.sub(r"^-\s*", "", r)
    return r.replace("**", "").replace("`", "").strip()


def main():
    tekst = BUNDEL.read_text()
    bron = "\n".join(schoon(r) for b in BRONNEN for r in b.read_text().splitlines())
    fouten, regels, paden = [], 0, 0

    for blok in re.findall(r"```\n(.*?)```", tekst, flags=re.S):
        for r in blok.splitlines():
            s = schoon(r)
            if not s:
                continue
            regels += 1
            if s not in bron:
                fouten.append(f"niet in een gekeurde bron: {s[:80]}")

    for p in sorted(set(re.findall(r"`([^`\s]+\.(?:md|jpg|png|py|toml|yml))`", tekst))):
        paden += 1
        naam = p.split("/")[-1]
        if not any((m / p).exists() or (m / naam).exists() for m in ZOEKMAPPEN) and not list(ROOT.glob(f"**/{naam}")):
            fouten.append(f"pad bestaat niet: {p}")

    # de oude zin uit de lange tekst mag er niet in (Daan M1 #12: geen "every cut face")
    if "every cut face" in tekst.replace("a number on every cut face", ""):
        fouten.append('"every cut face" staat erin (Daan M1 #12)')
    # Daan M1 #189: magneetgat alleen "where it fits"; M2 #189: geen $24 na 14 dec (niet besloten)
    if "both sides of every cut" in tekst:
        fouten.append('"both sides of every cut" staat erin (Daan M1 #189: "each cut where it fits")')
    if "daarna $24" in tekst:
        fouten.append('"daarna $24" staat erin (Daan M2 #189: vaste prijs op basis van verkoop)')
    if "click-cuts-winkeltekst-lang.md" in tekst and "niet gebruiken" not in tekst:
        fouten.append("lange tekst genoemd zonder 'niet gebruiken'")

    print(f"{regels} plakregels en {paden} paden nagekeken.")
    for f in fouten:
        print("FOUT:", f)
    print("OK" if not fouten else f"{len(fouten)} fouten")
    return 1 if fouten else 0


if __name__ == "__main__":
    sys.exit(main())
