#!/usr/bin/env python3
"""Drift-controle (afgekeken bij Twenty): verwijzen CLAUDE.md, de skills en de regels nog naar
bestanden en mappen die echt bestaan? Een verouderde verwijzing stuurt agents de verkeerde kant op.

Gebruik: python3 organisatie/controle/wegwijzer.py   (code 1 bij dode verwijzingen)
"""
import glob
import os
import re
import sys

BRONNEN = ["CLAUDE.md", "START.md"] + glob.glob(".claude/skills/*/SKILL.md") + glob.glob("organisatie/regels/*.md") \
    + ["organisatie/regels.md", "organisatie/toegang.md", "organisatie/sjablonen/agent-opdracht.md"] \
    + glob.glob("organisatie/rollen/*.md")
PAD = re.compile(r"`([A-Za-z0-9_.\-/]+)`")
VOORVOEGSELS = ("organisatie/", "platformen/", "producten/", "commercie/", "berichten/", ".claude/", ".github/",
                "ontwerp/", "strategie/", "rapporten/")


def main():
    dood = []
    for bron in BRONNEN:
        if not os.path.isfile(bron):
            continue
        basis = os.path.dirname(bron)
        for nr, regel in enumerate(open(bron, encoding="utf-8"), 1):
            for p in PAD.findall(regel):
                if "<" in p or "*" in p or p.startswith(("http", "-")):
                    continue
                if not (p.startswith(VOORVOEGSELS) or p.endswith((".md", ".yml", ".yaml", ".py", ".sh"))):
                    continue
                kandidaten = [p, os.path.join(basis, p), os.path.join("organisatie", p), os.path.join(".github/workflows", p)]
                if not any(os.path.exists(k.rstrip("/")) for k in kandidaten):
                    if "/" not in p and not os.path.exists(p):
                        # losse bestandsnaam zonder map: alleen melden als hij nergens in de repo staat
                        if glob.glob("**/" + p, recursive=True):
                            continue
                    dood.append(f"{bron}:{nr}: `{p}` bestaat niet")
    if dood:
        print("Wegwijzer: dode verwijzingen (pas de verwijzing aan of zet het bestand terug):")
        for d in dood:
            print("  " + d)
        return 1
    print("Wegwijzer: alle verwijzingen kloppen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
