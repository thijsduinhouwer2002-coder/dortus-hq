#!/usr/bin/env python3
"""Controle voor de openbare repo: geen persoonsgegevens, geen sleutels, geen gedachtestreepjes.

Gebruik:
  python3 organisatie/controle/check.py                 # wat jij nog niet gepusht hebt (tegen origin/main)
  python3 organisatie/controle/check.py <van> <tot>     # alleen de regels die tussen twee commits zijn toegevoegd

Kijkt alleen naar toegevoegde regels, zodat oude bestanden geen ruis geven.
Vindt hij iets, dan stopt hij met code 1 en zegt waar. Haal het weg en commit opnieuw.
"""
import re
import subprocess
import sys

ZELF = "organisatie/controle/check.py"

# (naam, patroon, alleen in tekstbestanden zoals .md)
REGELS = [
    ("IBAN of rekeningnummer", re.compile(r"\b[A-Z]{2}\d{2}[ ]?[A-Z]{4}[ ]?\d{4}[ ]?\d{4}[ ]?\d{2}\b"), False),
    ("telefoonnummer", re.compile(r"(?<![\w.])(?:\+31|0031)[\s-]?6[\s-]?\d{8}\b|(?<![\w.])06[\s-]?\d{8}\b"), False),
    ("prive-mailadres", re.compile(r"[\w.+-]+@(?:gmail|googlemail|hotmail|outlook|live|icloud|me|yahoo|ziggo|kpnmail|xs4all|planet)\.(?:com|nl)\b", re.I), False),
    ("GitHub-sleutel", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}"), False),
    ("API-sleutel", re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_-]{20,}"), False),
    ("AWS-sleutel", re.compile(r"\bAKIA[0-9A-Z]{16}\b"), False),
    ("privesleutel", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), False),
    ("gedachtestreepje", re.compile("—"), True),
]

TEKST = (".md", ".txt")

# Omvang (opschonen 24 nov 2026, Thijs: "zodat ze dit echt heilig doen"). Alleen als jij het bestand
# in deze push verandert, zodat wie het te groot maakt het ook kleiner maakt.
GRENZEN = {"CLAUDE.md": 12000, "organisatie/besluiten.md": 25000}
GRENS_BERICHTEN = 60000  # berichten/<naam>.md; oud werk naar berichten/archief/


def omvang(van, tot):
    cmd = ["git", "-c", "core.quotePath=false", "diff", "--name-only", "--diff-filter=AM", van] + ([tot] if tot else [])
    namen = subprocess.run(cmd, capture_output=True, text=True, errors="replace").stdout.split()
    fouten = []
    for n in namen:
        grens = GRENZEN.get(n)
        if grens is None and n.startswith("berichten/") and n.count("/") == 1 and n.endswith(".md"):
            grens = GRENS_BERICHTEN
        if grens is None:
            continue
        try:
            if tot:
                data = subprocess.run(["git", "show", f"{tot}:{n}"], capture_output=True).stdout
            else:
                data = open(n, "rb").read()
        except OSError:
            continue
        if len(data) > grens:
            fouten.append(f"{n}: {len(data)} tekens, grens {grens}. Maak het korter (oud naar het archief) en commit opnieuw.")
    return fouten


def diff(van, tot):
    # quotePath=false: ook bestanden met een naam als "ideeën/" worden gecontroleerd.
    # --no-renames: een hernoemd bestand telt als nieuw, dus de hele inhoud wordt gecontroleerd.
    basis = ["git", "-c", "core.quotePath=false", "diff", "--unified=0", "--no-color", "--no-renames", "--diff-filter=AM"]
    cmd = basis + [van, tot] if tot else basis + [van]
    uit = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    # Faalt git diff (bijv. blob:none kan een oud bestand niet ophalen), dan is er niets gecontroleerd:
    # dat is rood, nooit stil groen (keuring R1, 19 nov).
    if uit.returncode != 0:
        print("Controle openbare repo: NIET OK. git diff faalde, dus er is niets gecontroleerd:")
        print("  " + (uit.stderr.strip().splitlines() or ["(geen foutmelding)"])[-1][:300])
        sys.exit(2)
    return uit.stdout


def main():
    args = sys.argv[1:]
    if len(args) == 2:
        van, tot = args
    else:
        subprocess.run(["git", "fetch", "-q", "origin", "main"], capture_output=True)
        van, tot = "origin/main", None
    bestand, regelnr, fouten = None, 0, []
    for regel in diff(van, tot).splitlines():
        if regel.startswith("+++ "):
            pad = regel[4:].strip().strip('"')
            bestand = pad[2:] if pad.startswith("b/") else None
            continue
        if regel.startswith("@@"):
            m = re.search(r"\+(\d+)", regel)
            regelnr = int(m.group(1)) if m else 0
            continue
        if not regel.startswith("+") or bestand is None or bestand == ZELF:
            continue
        tekst = regel[1:]
        for naam, patroon, alleen_tekst in REGELS:
            if alleen_tekst and not bestand.endswith(TEKST):
                continue
            if patroon.search(tekst):
                fouten.append(f"{bestand}:{regelnr}: {naam}")
        regelnr += 1
    te_groot = omvang(van, tot)
    if te_groot:
        print("Controle omvang: NIET OK.")
        for f in te_groot:
            print("  " + f)
        sys.exit(1)
    if fouten:
        print("Controle openbare repo: NIET OK. Haal dit weg (persoonsgegevens: schrijf 'staat bij Thijs'):")
        for f in fouten[:50]:
            print("  " + f)
        sys.exit(1)
    print("Controle openbare repo: OK")


if __name__ == "__main__":
    main()
