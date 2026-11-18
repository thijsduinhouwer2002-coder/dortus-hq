#!/usr/bin/env python3
"""Automatische keurder: een losse Claude keurt een wijziging aan een product.

Draait in GitHub Actions (.github/workflows/keurder.yml). Gebruik:
    python3 organisatie/controle/keurder.py <product> <van> <tot>

Hij leest de opdracht van het product (ontwerp.md, architectuur.md), de wijziging
tussen <van> en <tot>, en het formulier uit de skill keuren. Hij bouwt niets.
Uitkomst:
  - platformen/<platform>/keuring/<datum>-auto-<product>-<hash>.md
  - een bericht onderaan berichten/<eigenaar>.md
  (met KEURDER_UIT=<map> komt alles in die map in plaats van in de repo)
  - regel "akkoord=ja|nee" en "bestand=..." in $GITHUB_OUTPUT (als die er is)
Nodig: ANTHROPIC_API_KEY. Model via KEURDER_MODEL (standaard claude-sonnet-5-5).
"""
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone, timedelta

# product: (platform-map, eigenaar). Alleen live producten en Hats.
PRODUCTEN = {
    "blender-gewrichten": ("blender", "bram"),
    "jetbrains-bison-flex": ("jetbrains", "chris"),
    "obsidian-rollwright": ("obsidian", "olaf"),
    "steam-hol": ("steam", "olaf"),
}

MAX_DIFF = 120_000      # tekens wijziging in totaal
MAX_PER_BESTAND = 20_000
MAX_OPDRACHT = 20_000
OVERSLAAN = re.compile(r"\.(png|jpe?g|gif|webp|mp4|webm|wav|ogg|mp3|glb|blend|zip|ttf|otf|woff2?|ico|lock)$|package-lock\.json$|/bewijs-[^/]+/")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def lees(pad, max_tekens):
    try:
        with open(pad, encoding="utf-8") as f:
            tekst = f.read()
    except FileNotFoundError:
        return ""
    if len(tekst) > max_tekens:
        tekst = tekst[:max_tekens] + "\n[... afgekapt ...]"
    return tekst


def wijziging(product, van, tot):
    """Diff per bestand, zonder beelden en gegenereerde bestanden, met een plafond."""
    pad = f"producten/{product}"
    bestanden = [b for b in git("diff", "--name-only", "--no-renames", van, tot, "--", pad).split("\n") if b]
    stukken, overgeslagen, totaal = [], [], 0
    for b in bestanden:
        if OVERSLAAN.search(b):
            overgeslagen.append(b)
            continue
        stuk = git("diff", "--no-color", "--no-renames", "-U3", van, tot, "--", b)
        if len(stuk) > MAX_PER_BESTAND:
            overgeslagen.append(f"{b} (wijziging te groot: {len(stuk)} tekens)")
            continue
        if totaal + len(stuk) > MAX_DIFF:
            overgeslagen.append(f"{b} (plafond bereikt)")
            continue
        stukken.append(stuk)
        totaal += len(stuk)
    return bestanden, "".join(stukken), overgeslagen


def formulier():
    tekst = lees(".claude/skills/keuren/SKILL.md", 10_000)
    return re.sub(r"^---.*?---\s*", "", tekst, flags=re.S)


SYSTEEM = """Je bent de automatische keurder van Dortus. Je hebt dit werk niet gemaakt en je bouwt niets: je schrijft alleen een oordeel.
Je ziet alleen tekst: de opdracht en de wijziging. Je kunt niets draaien, niets spelen en geen beelden zien.
Zeg dus nooit dat iets er goed uitziet of werkt als je dat niet uit de tekst kunt halen: zet het dan als vermoeden, met wat het zou bevestigen.
Oordeel streng maar eerlijk. Alleen echte problemen worden een "moet". Smaak en kleine dingen zijn "kan".
Schrijf in het Nederlands, in gewone woorden, zonder gedachtestreepjes (geen em dash of en dash).
Schrijf nooit persoonsgegevens, sleutels of wachtwoorden over, ook niet als je ze in de wijziging ziet: meld alleen dat ze er staan en in welk bestand.

Gebruik precies het formulier hieronder. De eerste regel is de kop, de tweede "Wat ik keurde:", de derde "Akkoord: ja" of "Akkoord: nee".
Akkoord is nee zodra er minstens één "moet" is.
Hou het kort: hooguit 8 rijen per deel, elke cel hooguit twee zinnen, en denk niet langer na dan nodig. Het hele formulier moet af zijn, met de moet/kan-lijst onderaan.

--- skill keuren ---
{formulier}
"""


def vraag_claude(systeem, bericht):
    sleutel = os.environ["ANTHROPIC_API_KEY"]
    model = os.environ.get("KEURDER_MODEL") or "claude-sonnet-5-5"
    data = json.dumps({
        "model": model,
        "max_tokens": 32000,
        "system": systeem,
        "messages": [{"role": "user", "content": bericht}],
    }).encode()
    verzoek = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=data, method="POST",
        headers={"x-api-key": sleutel, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with urllib.request.urlopen(verzoek, timeout=300) as antwoord:
        uit = json.load(antwoord)
    tekst = "".join(d.get("text", "") for d in uit.get("content", []) if d.get("type") == "text")
    if not tekst.strip():
        soorten = [d.get("type") for d in uit.get("content", [])]
        sys.exit(f"Leeg antwoord van de API (stop_reason {uit.get('stop_reason')}, blokken {soorten}, gebruik {uit.get('usage')}). Geen keuring geschreven.")
    if uit.get("stop_reason") == "max_tokens":
        tekst += "\n\n(Afgekapt: het antwoord was te lang. Lees de moet-punten na in de tabellen hierboven.)"
    return tekst, uit.get("usage", {}), model


def schoon(tekst):
    """Geen gedachtestreepjes in onze repo."""
    return tekst.replace("—", ",").replace("–", "-")


def schrijf_uit(sleutel, waarde):
    pad = os.environ.get("GITHUB_OUTPUT")
    if pad:
        with open(pad, "a", encoding="utf-8") as f:
            f.write(f"{sleutel}={waarde}\n")


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    product, van, tot = sys.argv[1:]
    if product not in PRODUCTEN:
        sys.exit(f"Onbekend product {product}. Bekend: {', '.join(PRODUCTEN)}")
    platform, eigenaar = PRODUCTEN[product]

    bestanden, diff, overgeslagen = wijziging(product, van, tot)
    if not diff.strip():
        print(f"{product}: niets te keuren tussen {van[:7]} en {tot[:7]} (alleen beelden of niets).")
        schrijf_uit("akkoord", "leeg")
        return

    commits = git("log", "--format=- %h %s (%an)", f"{van}..{tot}", "--", f"producten/{product}")
    opdracht = lees(f"producten/{product}/ontwerp.md", MAX_OPDRACHT)
    architectuur = lees(f"producten/{product}/architectuur.md", 10_000)
    changelog = lees(f"producten/{product}/CHANGELOG.md", 5_000)

    nu = datetime.now(timezone(timedelta(hours=1)))
    korte = tot[:7]
    bericht = f"""Keur deze wijziging aan product `{product}` (commits {van[:7]}..{korte}).
Datum: {nu:%d-%m-%Y %H:%M} NL. Keurder: automatische keurder.

## Commits
{commits or '(geen)'}

## Gewijzigde bestanden
{chr(10).join(bestanden)}

## Niet meegestuurd (beelden, gegenereerd of te groot)
{chr(10).join(overgeslagen) or '(niets)'}

## De opdracht: producten/{product}/ontwerp.md
{opdracht or '(geen ontwerp.md gevonden: zeg dat in deel A)'}

## producten/{product}/architectuur.md
{architectuur or '(geen architectuur.md)'}

## CHANGELOG.md (begin)
{changelog or '(geen)'}

## De wijziging
```diff
{diff}
```
"""
    tekst, gebruik, model = vraag_claude(SYSTEEM.format(formulier=formulier()), bericht)
    tekst = schoon(tekst).strip()
    m = re.search(r"Akkoord:\s*\**\s*(ja|nee)", tekst, re.I)
    akkoord = m.group(1).lower() if m else "nee"
    if not m:
        tekst += "\n\n(De keurder gaf geen duidelijk akkoord; daarom telt het als nee.)"

    invoer = gebruik.get("input_tokens", 0)
    uitvoer = gebruik.get("output_tokens", 0)
    voet = (f"\n\n---\nAutomatische keurder, model `{model}`, {invoer} tokens in, {uitvoer} tokens uit (GEZIEN in het antwoord van de API). "
            "Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.\n")
    # KEURDER_UIT: map waar de uitkomst apart komt (de workflow zet die bovenop main).
    uit = os.environ.get("KEURDER_UIT", ".")
    bestand = f"platformen/{platform}/keuring/{nu:%Y-%m-%d}-auto-{product}-{korte}.md"
    os.makedirs(os.path.dirname(os.path.join(uit, bestand)), exist_ok=True)
    os.makedirs(os.path.join(uit, "berichten"), exist_ok=True)
    with open(os.path.join(uit, bestand), "w", encoding="utf-8") as f:
        f.write(tekst + voet)

    moet = ""
    deel = re.split(r"##\s*Moet", tekst, maxsplit=1, flags=re.I)
    if len(deel) == 2:
        moet = " ".join(deel[1].split("\n", 1)[-1].split())[:600]
    maand = "jan feb mrt apr mei jun jul aug sep okt nov dec".split()[nu.month - 1]
    regel = (f"\n## {nu.day} {maand} {nu.year} ±{nu:%H:%M} NL, van de automatische keurder: {product} akkoord {akkoord}\n"
             f"Keuring van {van[:7]}..{korte}: `{bestand}`. "
             + (f"Moet en kan: {moet} " if moet else "")
             + ("Los elk moet-punt op en push opnieuw; de keurder kijkt dan weer. " if akkoord == "nee" else "")
             + "Hij leest alleen tekst, dus beeld en speelplezier blijven bij Daan en Iris.\n"
             "Webpagina's lees je met `curl` in Bash, nooit met WebFetch. WebFetch vraagt Thijs om toestemming en dan staat alles stil.\n")
    with open(os.path.join(uit, "berichten", f"{eigenaar}.md"), "a", encoding="utf-8") as f:
        f.write(schoon(regel))

    print(f"{product}: akkoord {akkoord}, {invoer} in / {uitvoer} uit, {bestand}")
    schrijf_uit("akkoord", akkoord)
    schrijf_uit("bestand", bestand)


if __name__ == "__main__":
    main()
