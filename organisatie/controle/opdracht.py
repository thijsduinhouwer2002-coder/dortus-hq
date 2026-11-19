#!/usr/bin/env python3
"""Start workflows uit opdrachtbestanden (draait in .github/workflows/opdracht.yml, niet zelf draaien).

Een agent pusht `organisatie/opdrachten/<datum>-<naam>.json`:
  {"workflow": "wegwijzer.yml", "invoer": {}, "van": "<naam>", "waarom": "<een zin>"}
Dit script start elke opdracht zonder "uitslag" of "fout", als de workflow op de lijst TOEGESTAAN staat,
en schrijft het runnummer terug in hetzelfde bestand (veld "uitslag"), of de reden in "fout".

Gebruik: python3 organisatie/controle/opdracht.py <uitmap>
  Schrijft de bijgewerkte bestanden onder <uitmap>/organisatie/opdrachten/. Nodig: GH_TOKEN, GITHUB_REPOSITORY.
"""
import datetime
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

MAP = "organisatie/opdrachten"

# Alleen deze workflows mogen via een opdrachtbestand starten: tests, proeven, renders, meten.
# Bewust NIET: alles wat naar een winkel uploadt of in een (openbare) GitHub-release schrijft (die gaan via de
# tag-route in de skill uitbrengen; daarom ook niet jetbrains-bison-flex-zip.yml en filmpjes-geluid.yml), en
# workflows die geld kosten (keurder.yml gebruikt het API-tegoed van Thijs).
# Een workflow toevoegen: alleen als hij niets naar buiten zet en niets kost, met een reden erachter, en
# zonder invoer met ${{ }} rechtstreeks in een run-stap (invoer via env:, zie roestronde R2).
# "schermen" = de tak schermen in deze repo, waar testbeelden staan; "artefact" = bestand bij de run zelf.
TOEGESTAAN = {
    "wegwijzer.yml",                   # leest alleen de repo, schrijft niets
    "actions-log.yml",                 # schrijft alleen logbestanden in organisatie/actions-logs/
    "dashboard.yml",                   # bouwt het dashboard uit de repo, schrijft alleen in de repo
    "scorebord.yml",                   # leest openbare cijfers en tellers (alleen-lezen sleutels), schrijft in de repo
    "blender-gewrichten-e2e.yml",      # test in echte Blender, beelden naar schermen
    "blender-gewrichten-proef.yml",    # bouwproef in echte Blender, schrijft niets
    "blender-chris-figuur.yml",        # figuur maken, alleen artefact
    "click-joints-render.yml",         # render, beelden naar schermen en artefact
    "click-joints-pro-film.yml",       # demofilm renderen, alleen artefact (geen release)
    "click-joints-film-plak.yml",      # film plakken uit een eerdere run, naar schermen
    "garmin-proef.yml",                # simulator-test, beelden naar schermen
    "jetbrains-bison-flex-clion.yml",  # unittests en Plugin Verifier, alleen artefact
    "jetbrains-bison-flex-e2e.yml",    # test in de echte IDE, beelden naar schermen
    "jetbrains-bison-flex-film.yml",   # beelden in de echte IDE, naar schermen
    "rollwright-e2e.yml",              # test in echte Obsidian, beelden naar schermen
    "rollwright-ontwerp.yml",          # ontwerptest, beelden naar schermen
    "steam-hol.yml",                   # Godot-test op Windows, beelden naar schermen
    "steam-hol-exe.yml",               # .exe bouwen als artefact, geen upload naar Steam
    "steam-hol-duur.yml",              # duurtest, uitslag naar schermen
    "steam-hol-clips.yml",             # clips maken, naar schermen
    "steam-hol-modellen.yml",          # 3D-modellen renderen, schrijft in de repo en artefact
    "steam-hol-winkel.yml",            # winkelbeelden maken (niet uploaden), naar schermen
    "steam-proef.yml",                 # Godot-proef, beelden naar schermen
    "steam-fest-meting.yml",           # leest openbare spelertallen, schrijft in de repo
    "loket-meldingen.yml",             # R5: leest openbare issues van de loketrepo's, schrijft in berichten/hoofdchat.md
    "schaduwbot.yml",                  # ai-handel: korte proef, leest alleen openbare marktdata, schrijft op tak ai-handel-data
    "scanner.yml",                     # ai-handel: proefrun koersverschil-scanner, leest openbare koersen, schrijft op tak ai-handel-data (map scanner/)
    "driehoek.yml",                    # ai-handel: proefrun driehoek-meter, leest openbare orderboeken, schrijft op tak ai-handel-data (map driehoek/)
    "radar.yml",                       # ai-handel: proefrun kansenradar, leest openbare lijsten, funding en orderboeken, schrijft op tak ai-handel-data (map radar/)
}

# Invoer komt in workflows terecht; alleen gewone tekens, zodat er nooit een commando in kan sluipen.
INVOER_TEKENS = re.compile(r"[A-Za-z0-9._,/ -]*")
INVOER_MAX = 200
SLEUTEL_TEKENS = re.compile(r"[A-Za-z0-9_-]{1,50}")


def nu():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def api(methode, pad, data=None):
    req = urllib.request.Request(
        "https://api.github.com" + pad,
        method=methode,
        data=json.dumps(data).encode() if data is not None else None,
        headers={
            "Authorization": "Bearer " + os.environ["GH_TOKEN"],
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            tekst = r.read().decode()
            return r.status, json.loads(tekst) if tekst else {}
    except urllib.error.HTTPError as e:
        return e.code, {"message": e.read().decode(errors="replace")[:300]}


def controleer(o):
    if not isinstance(o, dict):
        return "het bestand is geen JSON-object"
    wf = o.get("workflow")
    if not isinstance(wf, str) or wf not in TOEGESTAAN:
        return f"workflow {wf!r} staat niet op de lijst in organisatie/controle/opdracht.py"
    if not os.path.isfile(f".github/workflows/{wf}"):
        return f".github/workflows/{wf} bestaat niet (verplaatst of uitgezet?)"
    invoer = o.get("invoer", {})
    if not isinstance(invoer, dict) or not all(isinstance(k, str) and isinstance(v, (str, int, float, bool)) for k, v in invoer.items()):
        return '"invoer" moet een object zijn met alleen tekst, getallen of ja/nee'
    if len(invoer) > 25:
        return "te veel invoervelden (max 25)"
    for k, v in invoer.items():
        if not SLEUTEL_TEKENS.fullmatch(k):
            return f"invoerveld {k[:50]!r}: alleen letters, cijfers, _ en - in de naam"
        w = str(v)
        if len(w) > INVOER_MAX:
            return f"invoer {k}: langer dan {INVOER_MAX} tekens"
        if not INVOER_TEKENS.fullmatch(w):
            return f"invoer {k}: alleen letters, cijfers, spatie en . _ , / - toegestaan"
        if w.lstrip().startswith("-"):
            return f"invoer {k}: mag niet met - beginnen (zou als optie gelezen kunnen worden)"
    # Alleen main: op een andere tak kan een workflow met dezelfde naam iets anders doen dan op de lijst bedoeld is.
    if o.get("tak", "main") != "main":
        return 'alleen "tak": "main" mag (laat het veld weg)'
    return None


def zoek_run(repo, wf, sinds):
    """Terugval als de API geen runnummer teruggeeft: de nieuwste dispatch-run sinds het starten."""
    for _ in range(10):
        time.sleep(3)
        s, d = api("GET", f"/repos/{repo}/actions/workflows/{wf}/runs?event=workflow_dispatch&per_page=5")
        for r in d.get("workflow_runs", []) if s == 200 else []:
            if r.get("created_at", "") >= sinds:
                return r["id"], r["html_url"]
    return None, None


def start(repo, o):
    wf, tak = o["workflow"], "main"
    invoer = {k: (str(v).lower() if isinstance(v, bool) else str(v)) for k, v in o.get("invoer", {}).items()}
    sinds = nu()
    s, d = api("POST", f"/repos/{repo}/actions/workflows/{wf}/dispatches",
               {"ref": tak, "inputs": invoer, "return_run_details": True})
    if s == 200 and d.get("workflow_run_id"):
        return {"run_id": d["workflow_run_id"], "url": d.get("html_url"), "gestart": sinds}, None
    if s == 204:
        rid, url = zoek_run(repo, wf, sinds)
        if rid:
            return {"run_id": rid, "url": url, "gestart": sinds}, None
        return {"run_id": None, "gestart": sinds, "let_op": "gestart, maar runnummer niet gevonden; kijk met actions.py " + wf}, None
    return None, f"GitHub zei {s}: {d.get('message', '')}"


def main():
    uit = sys.argv[1]
    repo = os.environ["GITHUB_REPOSITORY"]
    gedaan = 0
    for pad in sorted(glob.glob(f"{MAP}/*.json")):
        try:
            o = json.load(open(pad, encoding="utf-8"))
        except (ValueError, OSError) as e:
            o, fout = {}, f"geen geldige JSON: {e}"
        else:
            if isinstance(o, dict) and ("uitslag" in o or "fout" in o):
                continue
            fout = controleer(o)
        if not isinstance(o, dict):
            o = {"inhoud": o}
        if not fout:
            uitslag, fout = start(repo, o)
            if uitslag:
                o["uitslag"] = uitslag
        if fout:
            o["fout"] = fout
            o["fout_tijd"] = nu()
        doel = os.path.join(uit, pad)
        os.makedirs(os.path.dirname(doel), exist_ok=True)
        with open(doel, "w", encoding="utf-8") as f:
            json.dump(o, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"{pad}: " + (f"FOUT {fout}" if fout else f"gestart, run {o['uitslag'].get('run_id')} {o['uitslag'].get('url', '')}"))
        gedaan += 1
    print(f"{gedaan} opdracht(en) verwerkt.")


if __name__ == "__main__":
    main()
