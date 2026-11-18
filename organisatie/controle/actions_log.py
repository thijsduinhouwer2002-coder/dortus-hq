#!/usr/bin/env python3
"""Zet het log van een mislukte run als tekstbestand in de repo (draait in .github/workflows/actions-log.yml).

Agents kunnen logs niet zonder sleutel downloaden; deze workflow wel. Per mislukte job de laatste 200 regels
van de mislukte stap, met persoonsgegevens en sleutels weggehaald (zelfde patronen als check.py).

Gebruik in de workflow:
  python3 organisatie/controle/actions_log.py maak <run_id> <uitmap>   nodig: GH_TOKEN, GITHUB_REPOSITORY
  python3 organisatie/controle/actions_log.py zoek <uitmap>            alle mislukte runs van de laatste 24 uur zonder logbestand
  python3 organisatie/controle/actions_log.py opruimen                 haalt logs ouder dan 7 dagen weg (git rm)
"zoek" is nodig omdat workflow_run niet afgaat voor runs die met de workflow-sleutel zijn gestart
(zoals runs uit een opdrachtbestand, GEZIEN 18 nov bij run 44415897839).
"""
import datetime
import glob
import json
import os
import re
import subprocess
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import REGELS  # noqa: E402

MAP = "organisatie/actions-logs"
REGELS_PER_JOB = 200
MAX_JOBS = 4
BEWAAR_DAGEN = 7
TIJD = re.compile(r"^\d{4}-\d\d-\d\dT[\d:.]+Z ")


def api(pad, ruw=False):
    req = urllib.request.Request("https://api.github.com" + pad, headers={
        "Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read().decode(errors="replace")
    return data if ruw else json.loads(data)


def schoon(regel):
    """Tijdstempel eraf, persoonsgegevens en sleutels eruit."""
    regel = TIJD.sub("", regel.rstrip("\n"))
    for naam, patroon, _ in REGELS:
        regel = patroon.sub("-" if naam == "gedachtestreepje" else f"[weggehaald: {naam}]", regel)
    return regel


def via_gh(repo, run):
    """gh run view --log-failed: regels 'job<TAB>stap<TAB>tekst'. Geeft {job: [regels]}."""
    p = subprocess.run(["gh", "run", "view", str(run), "--log-failed", "-R", repo],
                       capture_output=True, text=True, errors="replace")
    per_job = {}
    for regel in p.stdout.splitlines():
        delen = regel.split("\t", 2)
        if len(delen) == 3:
            per_job.setdefault(f"{delen[0]} / {delen[1]}", []).append(delen[2])
    return per_job


def via_api(repo, run, jobs):
    """Terugval: het hele joblog, afgekapt na de laatste foutregel."""
    per_job = {}
    for j in jobs:
        if j.get("conclusion") != "failure":
            continue
        try:
            regels = api(f"/repos/{repo}/actions/jobs/{j['id']}/logs", ruw=True).splitlines()
        except Exception as e:  # log weg of verlopen
            regels = [f"(log niet op te halen: {e})"]
        fout = [i for i, r in enumerate(regels) if "##[error]" in r]
        if fout:
            regels = regels[: fout[-1] + 3]
        stap = next((s["name"] for s in j.get("steps", []) if s.get("conclusion") == "failure"), "?")
        per_job[f"{j['name']} / {stap}"] = regels
    return per_job


def stam_van(r):
    return os.path.splitext(os.path.basename(r.get("path", "onbekend.yml").split("@")[0]))[0]


def zoek(uit):
    repo = os.environ["GITHUB_REPOSITORY"]
    sinds = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
    runs = api(f"/repos/{repo}/actions/runs?status=failure&per_page=50&created=%3E{sinds}").get("workflow_runs", [])
    nieuw = [r for r in runs if not r.get("name", "").startswith("Actions-log ")
             and not os.path.exists(f"{MAP}/{stam_van(r)}-{r['id']}.txt")]
    print(f"{len(runs)} mislukte run(s) in 24 uur, {len(nieuw)} zonder logbestand.")
    for r in nieuw[:10]:
        try:
            maak(r["id"], uit, r)
        except Exception as e:  # één kapotte run mag de rest niet tegenhouden
            print(f"Run {r['id']}: log maken lukte niet ({e})")


def maak(run, uit, r=None):
    repo = os.environ["GITHUB_REPOSITORY"]
    r = r or api(f"/repos/{repo}/actions/runs/{run}")
    jobs = api(f"/repos/{repo}/actions/runs/{run}/jobs?per_page=100").get("jobs", [])
    per_job = via_gh(repo, run) or via_api(repo, run, jobs)
    stam = stam_van(r)
    nu = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    mislukt = [f"{j['name']}: {s['name']}" for j in jobs if j.get("conclusion") == "failure"
               for s in j.get("steps", []) if s.get("conclusion") == "failure"]
    uitvoer = [
        f"# gemaakt: {nu}",
        f"# workflow: {r.get('name')} ({r.get('path')})",
        f"# run: {run} {r.get('html_url')}",
        f"# commit: {r.get('head_sha', '')[:8]} tak {r.get('head_branch')} gestart door {r.get('event')}",
        "# mislukte stappen: " + ("; ".join(mislukt) or "geen stap gemarkeerd (zie de run)"),
        f"# per mislukte job de laatste {REGELS_PER_JOB} regels; persoonsgegevens en sleutels weggehaald.",
        "# wordt na 7 dagen vanzelf opgeruimd.",
    ]
    if not per_job:
        uitvoer.append("\n(geen log gevonden; misschien faalde de run voor er een stap draaide, bijvoorbeeld een fout in de yml)")
    for naam, regels in list(per_job.items())[:MAX_JOBS]:
        uitvoer.append(f"\n===== {naam} (laatste {min(len(regels), REGELS_PER_JOB)} van {len(regels)} regels) =====")
        uitvoer += [schoon(x) for x in regels[-REGELS_PER_JOB:]]
    doel = os.path.join(uit, MAP, f"{stam}-{run}.txt")
    os.makedirs(os.path.dirname(doel), exist_ok=True)
    with open(doel, "w", encoding="utf-8") as f:
        f.write("\n".join(uitvoer) + "\n")
    print(f"Log klaar: {MAP}/{stam}-{run}.txt ({len(per_job)} job(s))")


def opruimen():
    grens = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=BEWAAR_DAGEN)
    for pad in glob.glob(f"{MAP}/*.txt"):
        with open(pad, encoding="utf-8", errors="replace") as f:
            m = re.match(r"# gemaakt: (\S+)", f.readline())
        if m and datetime.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc) < grens:
            subprocess.run(["git", "rm", "-q", pad], check=False)
            print(f"Opgeruimd: {pad}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["maak"]:
        maak(sys.argv[2], sys.argv[3])
    elif sys.argv[1:2] == ["zoek"]:
        zoek(sys.argv[2])
    elif sys.argv[1:2] == ["opruimen"]:
        opruimen()
    else:
        print(__doc__)
        sys.exit(2)
