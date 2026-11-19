#!/usr/bin/env python3
"""Maakt het dagrapport van de repo-radar uit kandidaten.json.

Gebruik: python3 rapport.py <kandidaten.json>   (print markdown)
"""
import collections
import json
import sys

TOP = 25


def top(data, n=TOP):
    """De beste n plannen die niet op een eerdere dag al in de top stonden."""
    return [p for p in data["plannen"] if not p.get("eerder_gemeld")][:n]


def _lijst(x, leeg):
    return ", ".join(x) if x else leeg


def soort(p):
    """Wat het is, in gewone woorden: platform plus doelgroep."""
    plat = [x for x in p["platform"] if x != "Gumroad"] + p.get("ander_platform", [])
    if not plat:
        wat = "project"
    elif plat[0] == "web":
        wat = "web-app"
    elif plat[0] == "Chrome":
        wat = "browserextensie"
    elif plat[0] in ("Blender", "Obsidian", "JetBrains"):
        wat = f"{plat[0]}-plugin"
    elif plat[0] == "Steam":
        wat = "spel"
    else:
        wat = f"{plat[0]}-app"
    if p["voor_wie"]:
        wat += " voor " + " en ".join(p["voor_wie"])
    if "Gumroad" in p["platform"]:
        wat += ", verkocht via Gumroad"
    return wat


def regel(i, p):
    tractie = [f"{p['sterren']} sterren"]
    if p["forks"]:
        tractie.append(f"{p['forks']} forks")
    if p["betaallinks"]:
        tractie.append("betaalpagina (" + ", ".join(p["betaallinks"]) + ")")
    if p["wachtlijst"]:
        tractie.append("wachtlijst")
    if p["site"]:
        tractie.append("eigen site")
    wat = f' "{p["wat"]}"' if p["wat"] else ""
    return (f"{i}. **{p['score']}** [{p['naam']}]({p['link']}): {soort(p)}.{wat} "
            f"Verdienmodel: {_lijst(p['verdienmodel'], 'niet genoemd')}. Prijs: {_lijst(p['prijs'], 'geen')}. "
            f"Tractie: {', '.join(tractie)}. Sinds {p['aangemaakt']}.")


def maak(data):
    t = top(data)
    ruis = data["ruis"]
    per_reden = collections.Counter(r["reden"] for r in ruis)
    voorbeeld = collections.defaultdict(list)
    for r in ruis:
        if len(voorbeeld[r["reden"]]) < 3:
            voorbeeld[r["reden"]].append(r["naam"])
    eerder = sum(1 for p in data["plannen"] if p.get("eerder_gemeld"))
    uit = [
        f"# Repo-radar {data['datum']}",
        "",
        f"Gemaakt {data['gemaakt']} door de workflow ideeen-radar. Alle cijfers GEZIEN via de zoek-API van GitHub "
        "op die tijd. De score is een voorselectie met vaste regels (zie onderaan), geen oordeel: dat doet de "
        "beoordelaar met de ideeëntest.",
        "",
        f"- Zoekvragen: {data['zoekvragen']} ({data['zoekvragen_mislukt']} mislukt)",
        f"- Gevonden: {data['gevonden']} verschillende repo's; README gelezen: {data['gelezen']}; "
        f"niet gelezen (limiet): {data['niet_gelezen']}",
        f"- Ruis eruit: {len(ruis)}; over met een plan: {len(data['plannen'])}"
        + (f" (waarvan {eerder} al eerder in de top)" if eerder else ""),
        "",
        f"## Top {len(t)}",
        "",
        "Score, repo, wat het is, de beschrijving van de maker (oorspronkelijke taal), verdienmodel, prijs, tractie.",
        "",
    ]
    uit += [regel(i + 1, p) for i, p in enumerate(t)] or ["Vandaag niets met een plan gevonden."]
    uit += ["", "## Ruis: wat eruit ging en waarom", ""]
    uitleg = {
        "fork": "een kopie van andermans repo, geen eigen plan",
        "gearchiveerd": "de maker is gestopt",
        "sjabloon of boilerplate": "een startpunt om zelf iets mee te bouwen, geen product",
        "huiswerk of oefening": "school, cursus, tutorial of een kloon om te leren",
        "crypto-pump": "munten, airdrops en snipers: geen product, vaak oplichterij",
        "spam of illegaal": "cracks, mod-apk's, lokrepo's en kopie-netwerken (dezelfde tekst bij veel accounts)",
        "lijst, geen product": "een verzamellijst (awesome-lijst)",
        "geen README": "niets te lezen",
        "lege README": "te weinig tekst om een plan uit te halen",
        "alleen code, geen uitleg": "wel code, geen uitleg wat het is of voor wie",
        "geen verdienplan in de tekst": "geen verdienmodel, prijs, betaalpagina of geldwoorden in de tekst",
    }
    for reden, n in per_reden.most_common():
        uit.append(f"- {reden}: {n} ({uitleg.get(reden, '')}). Bijvoorbeeld: {', '.join(voorbeeld[reden])}")
    uit += [
        "",
        "## Hoe de score werkt (max 10)",
        "",
        "- verdienmodel genoemd: +2 (abonnement, eenmalige koop, pro-versie, per gebruik, commissie), +1 als het "
        "alleen advertenties, affiliate of donaties is; kopje met prijzen in de README: +1; plan uitgeschreven "
        "(2+ kopjes zoals probleem, doelgroep, verdienmodel, concurrentie, roadmap): +1",
        "- prijs gevonden: +2",
        "- platform dat wij kennen: Blender, Obsidian, JetBrains, Garmin, Steam, Chrome of Gumroad +2, web +1",
        "- tractie: 10+ sterren +1, 50+ sterren +2; betaalpagina of wachtlijst +1; eigen site +1",
        "",
        "Volledige gegevens per repo: kandidaten.json in dezelfde map.",
        "",
    ]
    return "\n".join(uit)


if __name__ == "__main__":
    print(maak(json.load(open(sys.argv[1]))))
