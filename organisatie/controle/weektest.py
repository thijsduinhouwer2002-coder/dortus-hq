#!/usr/bin/env python3
"""Week-test (roestronde R4), twee delen. Draait in .github/workflows/week-test.yml.

  weektest.py versies
      Kiest de versies voor deze week en schrijft ze naar GITHUB_OUTPUT:
      blender   JSON-lijst: de nieuwste vaste versie uit blender-gewrichten-e2e.yml (de huidige), elke alpha, beta
                of rc van builder.blender.org, en elke nieuwere patch van een vaste versie (bijvoorbeeld 5.2.4-stable).
      idea_build, clion_build
                build van de nieuwste IntelliJ IDEA- en CLion-EAP van een grote versie (2026.3, geen bugfix als
                2026.3.1), alleen als die jonger is dan 28 dagen (zo'n EAP heeft een ingebouwde licentie van 30 dagen
                na de builddatum; een bugfix-EAP vraagt een licentie; anders leeg).
      verifier_extra
                nieuwste IntelliJ IDEA- en CLion-release voor de Plugin Verifier, plus de allernieuwste IntelliJ-EAP
                als build, bijvoorbeeld IU:2026.3,CL:2026.3.0.1,IU/263.8311.30.
      obsidian  JSON-lijst: nieuwste Obsidian met de oudste en met de nieuwste installer. De insider-versie
                (catalyst) vraagt inloggen met een betaald account, die halen we niet.

  weektest.py melden <map met beeldverschil-artefacten> <uitmap>
      Leest de jobs van deze run (API, GH_TOKEN) en de beeldverslagen, en schrijft per eigenaar een bericht
      naar <uitmap>/<naam>.md: welke versie, welke stap rood was, en welke plaatjes sterk veranderden.
"""
import datetime
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

EIGENAREN = [  # (begin van de jobnaam, begin van de artefactnaam, eigenaar, product)
    ("Click Joints", "beeldverschil-blender-gewrichten", "bram", "Click Joints"),
    ("Bison & Flex", "beeldverschil-jetbrains-bison-flex", "chris", "Bison & Flex"),
    ("Rollwright", "beeldverschil-rollwright", "olaf", "Rollwright"),
]
# Welke push-workflow op main hoort bij een job van de week-test (om te zien of het aan de nieuwe versie ligt).
PUSHWORKFLOW = [
    ("Click Joints", "blender-gewrichten-e2e.yml"),
    ("Bison & Flex verifier", "jetbrains-bison-flex-clion.yml"),
    ("Bison & Flex", "jetbrains-bison-flex-e2e.yml"),
    ("Rollwright", "rollwright-e2e.yml"),
]


def laatste_push(repo, token, workflow):
    try:
        d = haal(f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/runs"
                 "?branch=main&event=push&status=completed&per_page=1", token)
        r = d["workflow_runs"][0]
        return f"laatste push-run op main van {workflow}: {r['conclusion']} (run {r['id']}, commit {r['head_sha'][:8]})"
    except Exception as e:  # alleen ter info
        return f"laatste push-run op main van {workflow}: onbekend ({e})"


def haal(url, token=None):
    req = urllib.request.Request(url, headers={"User-Agent": "dortus-week-test", "Accept": "application/json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def uit(**waarden):
    pad = os.environ.get("GITHUB_OUTPUT")
    for k, v in waarden.items():
        print(f"{k}={v}")
        if pad:
            with open(pad, "a", encoding="utf-8") as f:
                f.write(f"{k}={v}\n")


def samenvatting(tekst):
    pad = os.environ.get("GITHUB_STEP_SUMMARY")
    if pad:
        with open(pad, "a", encoding="utf-8") as f:
            f.write(tekst + "\n")


def num(v):
    return tuple(int(x) for x in re.findall(r"\d+", v))


def blender_lijst(vast, builds):
    """vast: vaste versies uit de e2e; builds: de lijst van builder.blender.org."""
    huidig = max(vast, key=num)
    lijst = [huidig]
    reeksen = {".".join(v.split(".")[:2]): v for v in vast}
    hoogste_reeks = max(num(r) for r in reeksen)
    for b in builds:
        if b.get("platform") != "linux" or b.get("architecture") != "x86_64" or b.get("file_extension") != "xz":
            continue
        v, cyc = b["version"], b["release_cycle"]
        reeks = ".".join(v.split(".")[:2])
        if cyc in ("alpha", "beta", "rc", "candidate"):
            lijst.append(f"{v}-{'rc' if cyc == 'candidate' else cyc}")
        elif cyc == "stable":
            if reeks in reeksen and num(v) > num(reeksen[reeks]):
                lijst.append(f"{v}-stable")
            elif reeks not in reeksen and num(reeks) > hoogste_reeks:
                lijst.append(f"{v}-stable")
    return sorted(set(lijst), key=lambda x: (num(x), x))


def eap(code, vandaag, lijst=None):
    """Nieuwste EAP van een grote versie (2026.3, niet 2026.3.1) die jonger is dan 28 dagen.

    Alleen de EAP van een grote versie heeft een ingebouwde licentie. De EAP van een bugfix (2026.3.1, build
    263.8311.30) toont een licentievenster "No subscription" (GEZIEN, run 45101820137, donker-calc-y.png), en
    dat klikt de test niet weg. Zo'n build gaat wel naar de Plugin Verifier (zie verifier_eap).
    """
    if lijst is None:
        lijst = haal(f"https://data.services.jetbrains.com/products/releases?code={code}&type=eap&latest=false").get(code) or []
    if not lijst:
        return "", f"{code}: geen EAP gevonden"
    nieuwste = max(lijst, key=lambda r: r["date"])
    groot = [r for r in lijst if len(num(r.get("version", ""))) <= 2]
    if not groot:
        return "", f"{code}: geen EAP van een grote versie (alleen bugfix-EAP {nieuwste['build']}, vraagt een licentie)"
    rel = max(groot, key=lambda r: r["date"])
    leeftijd = (vandaag - datetime.date.fromisoformat(rel["date"])).days
    if leeftijd > 28:
        return "", (f"{code}: nieuwste EAP van een grote versie {rel['build']} is {leeftijd} dagen oud (licentie verlopen), "
                    f"overgeslagen; nieuwste EAP is {nieuwste['version']} build {nieuwste['build']}")
    return rel["build"], f"{code}: EAP {rel['version']} build {rel['build']} van {rel['date']}"


def verifier_eap(code, lijst=None):
    """Build van de allernieuwste EAP (ook bugfix) voor de Plugin Verifier, als IU/<build>: die vraagt geen licentie."""
    if lijst is None:
        lijst = haal(f"https://data.services.jetbrains.com/products/releases?code={code}&type=eap&latest=true").get(code) or []
    return lijst[0]["build"] if lijst else ""


def release(code):
    r = haal(f"https://data.services.jetbrains.com/products/releases?code={code}&type=release&latest=true")
    return r[code][0]["version"]


def versies():
    wf = Path(".github/workflows/blender-gewrichten-e2e.yml").read_text(encoding="utf-8")
    m = re.search(r"fromJSON\(inputs\.blender \|\| '(\[.*?\])'\)", wf)
    vast = json.loads(m.group(1))
    builds = haal("https://builder.blender.org/download/daily/?format=json&v=1")
    blender = blender_lijst(vast, builds)
    vandaag = datetime.date.today()
    idea, idea_tekst = eap("IIU", vandaag)
    clion, clion_tekst = eap("CL", vandaag)
    extra = f"IU:{release('IIU')},CL:{release('CL')}"
    nieuwste_eap = verifier_eap("IIU")
    if nieuwste_eap:
        extra += f",IU/{nieuwste_eap}"
    obsidian = [{"app": "latest", "installer": "earliest"}, {"app": "latest", "installer": "latest"}]
    uit(blender=json.dumps(blender), idea_build=idea, clion_build=clion, verifier_extra=extra,
        obsidian=json.dumps(obsidian, separators=(",", ":")))
    overzicht = (f"Blender: {', '.join(blender)} (vast bij een push: {', '.join(vast)}). "
                 f"JetBrains: {idea_tekst}; {clion_tekst}; Plugin Verifier ook tegen {extra}. "
                 f"Obsidian: nieuwste app met de oudste en de nieuwste installer.")
    uit(overzicht=overzicht)
    samenvatting("## Week-test: versies\n" + overzicht)


def melden(artmap, uitmap):
    repo, run = os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_RUN_ID"]
    poging = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    token = os.environ.get("GH_TOKEN")
    overzicht = os.environ.get("OVERZICHT", "")
    link = f"https://github.com/{repo}/actions/runs/{run}"
    jobs, pagina = [], 1
    while True:
        d = haal(f"https://api.github.com/repos/{repo}/actions/runs/{run}/attempts/{poging}/jobs?per_page=100&page={pagina}", token)
        jobs += d.get("jobs", [])
        if len(jobs) >= d.get("total_count", 0) or not d.get("jobs"):
            break
        pagina += 1
    regels = {naam: [] for _, _, naam, _ in EIGENAREN}
    for j in jobs:
        if j.get("conclusion") != "failure":
            continue
        stappen = [s["name"] for s in j.get("steps", []) if s.get("conclusion") == "failure"]
        for begin, _, naam, _ in EIGENAREN:
            if j["name"].startswith(begin):
                wf = next(w for b, w in PUSHWORKFLOW if j["name"].startswith(b))
                regels[naam].append(f"- ROOD: {j['name']}, stap: {'; '.join(stappen) or 'onbekend (zie log)'}. "
                                    f"Ter vergelijking, {laatste_push(repo, token, wf)}.")
                break
        else:
            if j["name"] == "versies":
                regels.setdefault("hoofdchat", []).append("- ROOD: de week-test kon de versies niet ophalen (job versies)")
    for d in sorted(Path(artmap).glob("beeldverschil-*")):
        verslag = d / "verslag.md"
        if not verslag.is_file():
            continue
        tekst = verslag.read_text(encoding="utf-8")
        groot = [r for r in tekst.splitlines() if r.endswith("| GROOT |")]
        if not groot:
            continue
        for _, art, naam, _ in EIGENAREN:
            if d.name.startswith(art):
                regels[naam].append(f"- BEELD: {len(groot)} plaatje(s) sterk veranderd sinds de vorige geslaagde week-test "
                                    f"(artefact {d.name}, rood is anders; geen rode test, kijk of het zo bedoeld is):")
                regels[naam] += ["  " + r.strip("| ").replace(" | ", ": ", 1).replace(" | GROOT", "") for r in groot[:8]]
                break
    datum = os.environ.get("DATUM") or datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    Path(uitmap).mkdir(parents=True, exist_ok=True)
    gemeld = []
    for naam, lijst in regels.items():
        if not lijst:
            continue
        product = next((p for _, _, n, p in EIGENAREN if n == naam), "week-test")
        tekst = (f"## {datum} NL, van de week-test (automatisch): {product} tegen de volgende versies\n"
                 f"Run: {link}\n" + "\n".join(lijst) + "\n"
                 f"Geteste versies: {overzicht}\n"
                 "Rood in de week-test blokkeert niets. Kijk of het aan de nieuwe versie ligt (dan aanpassen voor die "
                 "uitkomt) of aan de test.\n")
        (Path(uitmap) / f"{naam}.md").write_text(tekst, encoding="utf-8")
        gemeld.append(naam)
        print(tekst)
    samenvatting("## Week-test: meldingen\n" + (", ".join(gemeld) if gemeld else "alles groen, geen groot beeldverschil"))


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "versies":
        versies()
    elif len(sys.argv) == 4 and sys.argv[1] == "melden":
        melden(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(2)
