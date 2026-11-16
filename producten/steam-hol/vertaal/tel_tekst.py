#!/usr/bin/env python3
"""Lijst van tekst die spelers kunnen zien, als voorbereiding op de vertaaltabel (bericht hoofdchat 16 nov 00:05).

Gebruik:  python3 -I producten/steam-hol/vertaal/tel_tekst.py [uit.csv]
Leest alle .gd onder producten/steam-hol/godot behalve toetsen/, en schrijft per tekst: bestand, regel, tekst.
Telt als tekst: een string met letters en een spatie (of een hoofdletter vooraan), zonder pad, logregel of sleutel.
Het is een ruwe lijst: wat nooit getoond wordt (dode kroniekregels, zie taken.md 16 nov 05:35) staat er ook in.
"""
import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "godot"
STR = re.compile(r'"((?:[^"\\]|\\.)*)"')
LOG = re.compile(r'\b(print|prints|printerr|push_error|push_warning|_log|assert)\s*\(')


def tekst(s: str) -> bool:
    if not re.search(r"[A-Za-z]", s) or s.startswith(("res://", "user://", "HOL ", "%")):
        return False
    if re.fullmatch(r"[a-z0-9_./:-]+", s):  # sleutels, namen van soorten, paden
        return False
    return " " in s.strip() or bool(re.match(r"[A-Z][a-z]", s))


def main() -> None:
    rijen = []
    for p in sorted(ROOT.rglob("*.gd")):
        if "toetsen" in p.parts:
            continue
        for nr, regel in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if regel.lstrip().startswith("#"):
                continue
            code = regel.split(" # ", 1)[0]
            if LOG.search(code):
                continue
            for m in STR.finditer(code):
                if tekst(m.group(1)):
                    rijen.append((str(p.relative_to(ROOT)), nr, m.group(1)))
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([("bestand", "regel", "tekst")] + rijen)
    per = {}
    for b, _, t in rijen:
        per.setdefault(b, [0, 0])
        per[b][0] += 1
        per[b][1] += len(re.findall(r"[A-Za-z']+", t))
    for b, (n, w) in sorted(per.items(), key=lambda x: -x[1][0]):
        print(f"{n:4d} {w:5d}  {b}")
    print(f"{len(rijen):4d} {sum(w for _, w in per.values()):5d}  totaal (teksten, woorden)")


if __name__ == "__main__":
    main()
