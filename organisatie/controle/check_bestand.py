#!/usr/bin/env python3
"""Controle direct na elke bewerking (PostToolUse-hook in .claude/settings.json).

Leest de hook-invoer (JSON op stdin), pakt het bewerkte bestand en controleert alleen de
regels die nieuw zijn ten opzichte van de laatste commit (of het hele bestand als het nieuw is).
Vindt hij persoonsgegevens, sleutels of een gedachtestreepje, dan stopt hij met code 2:
Claude Code geeft de melding dan meteen terug aan de agent, die het kan herstellen
voordat het ooit in een commit komt. Zelfde regels als check.py.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import REGELS, TEKST, ZELF  # noqa: E402


def nieuwe_regels(pad):
    r = subprocess.run(["git", "ls-files", "--error-unmatch", pad], capture_output=True)
    if r.returncode != 0:
        try:
            return list(enumerate(open(pad, encoding="utf-8", errors="replace").read().splitlines(), 1))
        except OSError:
            return []
    d = subprocess.run(["git", "-c", "core.quotePath=false", "diff", "--unified=0", "--no-color", "HEAD", "--", pad],
                       capture_output=True, text=True, errors="replace").stdout
    uit, nr = [], 0
    for regel in d.splitlines():
        if regel.startswith("@@"):
            import re
            m = re.search(r"\+(\d+)", regel)
            nr = int(m.group(1)) if m else 0
        elif regel.startswith("+") and not regel.startswith("+++"):
            uit.append((nr, regel[1:]))
            nr += 1
    return uit


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    pad = (data.get("tool_input") or {}).get("file_path") or ""
    if not pad or not os.path.isfile(pad):
        return 0
    try:
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                             cwd=os.path.dirname(pad)).stdout.strip()
    except Exception:
        return 0
    if not top:
        return 0
    rel = os.path.relpath(pad, top)
    if rel == ZELF:
        return 0
    os.chdir(top)
    fouten = []
    for nr, tekst in nieuwe_regels(rel):
        for naam, patroon, alleen_tekst in REGELS:
            if alleen_tekst and not rel.endswith(TEKST):
                continue
            if patroon.search(tekst):
                fouten.append(f"{rel}:{nr}: {naam}")
    if fouten:
        print("Controle openbare repo: haal dit meteen weg (persoonsgegevens: schrijf 'staat bij Thijs'):", file=sys.stderr)
        for f in fouten[:20]:
            print("  " + f, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
