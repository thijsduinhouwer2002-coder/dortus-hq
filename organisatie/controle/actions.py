#!/usr/bin/env python3
"""Uitslag van GitHub Actions lezen, zonder sleutel (de repo is openbaar; ±60 verzoeken per uur).

Gebruik:
  python3 organisatie/controle/actions.py <run_id>                  status, jobs en stappen van een run
  python3 organisatie/controle/actions.py <workflow.yml>            de laatste run van die workflow
  python3 organisatie/controle/actions.py <opdrachtbestand.json>    de run die bij die opdracht hoort
  python3 organisatie/controle/actions.py lijst                     de laatste 15 runs van alle workflows
Opties:
  --log     laatste regels van de mislukte stap (uit organisatie/actions-logs/, anders rechtstreeks)
  --wacht   wacht tot de run klaar is (één keer per minuut, max 60 min)
  --tak X   bij een workflow: alleen runs op tak X

Bij een opdrachtbestand: eerst `git pull --rebase`, want het runnummer zet de workflow opdracht.yml erin.
Code 0 = geslaagd of nog bezig, 1 = mislukt, 2 = niet gevonden of fout bij het lezen.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

REPO = "thijsduinhouwer2002-coder/dortus-hq"
API = f"https://api.github.com/repos/{REPO}"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
RAW_LOGS = f"https://raw.githubusercontent.com/{REPO}/actions-logs/"  # logs sinds 26 nov op eigen tak
HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.dirname(os.path.dirname(HIER))
TEKEN = {"success": "OK  ", "failure": "FOUT", "cancelled": "STOP", "skipped": "--  ", None: "..  "}


def haal(url, ruw=False):
    # Bewust zonder sleutel: de GH_TOKEN in agentsessies is ongeldig en geeft 401.
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "dortus-actions"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read().decode(errors="replace")
    except urllib.error.HTTPError as e:
        if e.code in (403, 429) and e.headers.get("X-RateLimit-Remaining") == "0":
            herstel = int(e.headers.get("X-RateLimit-Reset", "0")) - int(time.time())
            raise SystemExit(f"Te veel verzoeken zonder sleutel; weer mogelijk over ±{max(herstel, 0) // 60 + 1} min.")
        raise
    return data if ruw else json.loads(data)


def run_van_workflow(wf, tak=None):
    url = f"{API}/actions/workflows/{wf}/runs?per_page=1" + (f"&branch={tak}" if tak else "")
    runs = haal(url).get("workflow_runs", [])
    if not runs:
        raise SystemExit(f"Geen runs gevonden voor {wf}.")
    return runs[0]["id"]


def run_van_opdracht(pad):
    o = json.load(open(pad, encoding="utf-8"))
    if o.get("fout"):
        raise SystemExit(f"Opdracht niet gestart: {o['fout']}")
    rid = (o.get("uitslag") or {}).get("run_id")
    if not rid:
        if "uitslag" in o:
            raise SystemExit(f"Opdracht gestart maar zonder runnummer; kijk met: actions.py {o.get('workflow')}")
        raise SystemExit("Nog geen uitslag in het bestand. Wacht ±1 minuut, doe `git pull --rebase` en probeer opnieuw.")
    return rid


def toon(rid):
    r = haal(f"{API}/actions/runs/{rid}")
    jobs = haal(f"{API}/actions/runs/{rid}/jobs?per_page=100").get("jobs", [])
    print(f"{r['name']}  (run {rid}, poging {r.get('run_attempt', 1)})")
    print(f"  {r['html_url']}")
    print(f"  status: {r['status']}, uitslag: {r.get('conclusion') or 'nog bezig'}")
    print(f"  gestart: {r.get('run_started_at')} door {r.get('event')}, tak {r.get('head_branch')}, commit {r['head_sha'][:8]}")
    mislukt = []
    for j in jobs:
        print(f"  [{TEKEN.get(j.get('conclusion'), j.get('conclusion'))}] job: {j['name']}")
        for s in j.get("steps", []):
            c = s.get("conclusion") or ("bezig" if s.get("status") == "in_progress" else None)
            print(f"      [{TEKEN.get(c, c)}] {s['number']}. {s['name']}")
            if c == "failure":
                mislukt.append(f"{j['name']}: stap {s['number']} {s['name']}")
    if mislukt:
        print("  MISLUKT: " + "; ".join(mislukt))
    return r, jobs


def logbestand(r):
    stam = os.path.splitext(os.path.basename(r["path"].split("@")[0]))[0]
    return f"organisatie/actions-logs/{stam}-{r['id']}.txt"


def toon_log(r, jobs):
    if r.get("conclusion") != "failure":
        print("\nGeen log: de run is niet mislukt.")
        return
    pad = logbestand(r)
    lokaal = os.path.join(WORTEL, pad)
    tekst = None
    if os.path.isfile(lokaal):
        tekst = open(lokaal, encoding="utf-8", errors="replace").read()
    else:
        for basis in (RAW_LOGS, RAW):
            try:
                tekst = haal(basis + pad, ruw=True)
                break
            except urllib.error.HTTPError:
                pass
    if tekst:
        print(f"\n--- {pad} ---\n{tekst}")
        return
    # Rechtstreeks proberen (lukt alleen als deze sessie toch bij logs mag).
    for j in jobs:
        if j.get("conclusion") == "failure":
            try:
                regels = haal(f"{API}/actions/jobs/{j['id']}/logs", ruw=True).splitlines()
                print(f"\n--- log van job {j['name']} (rechtstreeks, laatste 200 regels) ---")
                print("\n".join(regels[-200:]))
                return
            except urllib.error.HTTPError:
                break
    print(f"\nNog geen logbestand ({pad}). De workflow actions-log.yml zet het er neer: ±1 minuut na de run als"
          " die door een push startte, anders bij de veegronde (elk kwartier). Sneller: een opdrachtbestand met"
          f' {{"workflow": "actions-log.yml", "invoer": {{"run": "{r["id"]}"}}}}. Daarna `git pull --rebase` en opnieuw.')


def lijst():
    # Lege "overgeslagen" runs van Actions-log (één na elke workflow) laten we weg.
    runs = [r for r in haal(f"{API}/actions/runs?per_page=40").get("workflow_runs", [])
            if not (r["name"].startswith("Actions-log (") and r.get("conclusion") == "skipped")]
    for r in runs[:15]:
        print(f"[{TEKEN.get(r.get('conclusion'), r.get('conclusion'))}] {r['id']}  {r['created_at']}  {r['name']}")


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    if args[0] == "lijst":
        lijst()
        return 0
    tak = args[args.index("--tak") + 1] if "--tak" in args else None
    doel = args[0]
    try:
        if doel.isdigit():
            rid = int(doel)
        elif doel.endswith(".json"):
            rid = run_van_opdracht(doel)
        else:
            rid = run_van_workflow(os.path.basename(doel), tak)
        r, jobs = toon(rid)
        if "--wacht" in args:
            # Eén verzoek per minuut, zodat je onder de grens van ±60 per uur blijft.
            eind = time.time() + 3600
            while r["status"] != "completed" and time.time() < eind:
                time.sleep(60)
                r = haal(f"{API}/actions/runs/{rid}")
                print(f"(wachten... {r['status']})", flush=True)
            print()
            r, jobs = toon(rid)
        if "--log" in args:
            toon_log(r, jobs)
    except urllib.error.HTTPError as e:
        print(f"GitHub zei {e.code} ({e.reason}). Klopt het nummer of de naam?")
        return 2
    return 1 if r.get("conclusion") == "failure" else 0


if __name__ == "__main__":
    sys.exit(main())
