#!/usr/bin/env python3
"""Repo-radar: zoekt elke dag nieuwe GitHub-repo's met een geldplan, leest de README en geeft een voorselectie.

Gebruik:
  python3 radar.py --uit <map> [--gezien gezien.json] [--max-readmes 2000] [--dagen 2]
Schrijft <map>/kandidaten.json en <map>/rapport.md. Nodig (in de workflow): GH_TOKEN, anders zonder sleutel.

Limieten van GitHub: zoeken 30 keer per minuut (wij wachten 2,2 s tussen zoekvragen en wachten bij een 403/429
tot de teller weer vol is). README's halen we bij raw.githubusercontent.com: dat telt niet mee voor de
API-limiet van 1000 per uur die alle workflows van deze repo samen delen.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regels  # noqa: E402
import rapport  # noqa: E402

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
README_NAMEN = ["README.md", "readme.md", "Readme.md", "README.MD", "README", "README.rst", "README.txt"]
WACHT_ZOEK = 2.2
MAX_README_BYTES = 200_000
MAX_API_README = 200  # README via de API (als raw niets gaf): telt mee voor de 1000 per uur van de hele repo
_api_teller = {"n": 0}
_api_slot = threading.Lock()


def _kop(api=True):
    k = {"User-Agent": "dortus-repo-radar"}
    if api:
        k["Accept"] = "application/vnd.github+json"
        k["X-GitHub-Api-Version"] = "2022-11-28"
    if os.environ.get("GH_TOKEN") and api:
        k["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    return k


def zoek(q, sort=None, pogingen=4):
    """Eén zoekvraag (max 100 uitkomsten). Geeft (items, totaal) of ([], -1) bij een blijvende fout."""
    par = {"q": q, "per_page": 100}
    if sort:
        par.update(sort=sort, order="desc")
    url = API + "/search/repositories?" + urllib.parse.urlencode(par)
    for poging in range(pogingen):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=_kop()), timeout=40) as r:
                d = json.load(r)
                return d.get("items", []), d.get("total_count", 0)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                wacht = e.headers.get("Retry-After")
                if not wacht and e.headers.get("X-RateLimit-Reset"):
                    wacht = int(e.headers["X-RateLimit-Reset"]) - int(time.time()) + 2
                wacht = min(max(int(wacht or 30), 5), 70)
                print(f"  limiet bereikt, {wacht} s wachten", flush=True)
                time.sleep(wacht)
                continue
            if e.code == 422:  # zoekvraag niet geldig: niet opnieuw proberen
                print(f"  zoekvraag geweigerd (422): {q}", flush=True)
                return [], -1
            time.sleep(5 * (poging + 1))
        except Exception as e:  # netwerk: even wachten en opnieuw
            print(f"  netwerkfout {type(e).__name__}, opnieuw", flush=True)
            time.sleep(5 * (poging + 1))
    return [], -1


def lees_readme(repo):
    """README als tekst, of None. Eerst raw.githubusercontent.com (gratis), daarna één keer de API."""
    tak = repo.get("default_branch") or "main"
    for naam in README_NAMEN:
        url = f"{RAW}/{repo['full_name']}/{urllib.parse.quote(tak)}/{naam}"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=_kop(api=False)), timeout=20) as r:
                return r.read(MAX_README_BYTES).decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code != 404:
                break
        except Exception:
            break
    with _api_slot:
        if _api_teller["n"] >= MAX_API_README:
            return None
        _api_teller["n"] += 1
    try:
        kop = _kop()
        kop["Accept"] = "application/vnd.github.raw"
        req = urllib.request.Request(f"{API}/repos/{repo['full_name']}/readme", headers=kop)
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read(MAX_README_BYTES).decode("utf-8", "replace")
    except Exception:
        return None


def zoekvragen(vandaag, dagen):
    """Twee soorten per zoekterm: nieuw (aangemaakt in de laatste <dagen> dagen) en actief (jonger dan 90 dagen,
    gisteren of vandaag gepusht, minstens 5 sterren: een benadering van 'flink bijgewerkt')."""
    nieuw = (vandaag - dt.timedelta(days=dagen)).isoformat()
    gisteren = (vandaag - dt.timedelta(days=1)).isoformat()
    kwartaal = (vandaag - dt.timedelta(days=90)).isoformat()
    vragen = []
    for term, readme in regels.ZOEKTERMEN:
        waar = "in:name,description,topics" + (",readme" if readme else "")
        vragen.append(("nieuw", f"{term} {waar} created:>={nieuw}", None))
        vragen.append(("actief", f"{term} {waar} created:{kwartaal}..{nieuw} pushed:>={gisteren} stars:>=5", "stars"))
    return vragen


def verzamel(vandaag, dagen, log=print):
    repos, treffers, fouten = {}, {}, 0
    vragen = zoekvragen(vandaag, dagen)
    for i, (soort, q, sort) in enumerate(vragen):
        items, totaal = zoek(q, sort)
        if totaal < 0:
            fouten += 1
        log(f"[{i + 1}/{len(vragen)}] {soort}: {q} -> {len(items)} van {totaal}")
        for it in items:
            repos.setdefault(it["full_name"], it)
            treffers.setdefault(it["full_name"], set()).add(q.split(" in:")[0].strip('"'))
        time.sleep(WACHT_ZOEK)
    return repos, treffers, len(vragen), fouten


def run(uit, gezien_pad=None, max_readmes=2000, dagen=2, vandaag=None, log=print):
    vandaag = vandaag or dt.datetime.now(dt.timezone.utc).date()
    gezien = {}
    if gezien_pad and os.path.exists(gezien_pad):
        try:
            with open(gezien_pad) as f:
                gezien = json.load(f)
        except Exception:
            gezien = {}
    repos, treffers, n_vragen, n_fout = verzamel(vandaag, dagen, log)
    log(f"{len(repos)} verschillende repo's gevonden")

    kandidaten, ruis = [], []
    spam = regels.spamnetwerk(repos.values())
    for naam, repo in repos.items():
        reden = "spam of illegaal" if naam in spam else regels.ruis_op_naam(repo)
        if reden:
            ruis.append({"naam": naam, "link": repo["html_url"], "reden": reden, "fase": "naam"})
        else:
            kandidaten.append(repo)
    # Volgorde van lezen: eerst nieuw (Thijs wil nieuwe plannen), dan meer geldtermen, dan sterren.
    # Wat buiten de limiet valt lezen we niet; dat is geen ruis en staat apart in het rapport.
    grens = (vandaag - dt.timedelta(days=dagen)).isoformat()
    kandidaten.sort(key=lambda r: ((r.get("created_at") or "")[:10] >= grens, len(treffers[r["full_name"]]),
                                   r.get("stargazers_count", 0)), reverse=True)
    te_lezen, niet_gelezen = kandidaten[:max_readmes], kandidaten[max_readmes:]
    log(f"{len(ruis)} ruis op naam, {len(te_lezen)} README's lezen, {len(niet_gelezen)} niet gelezen (limiet)")

    with cf.ThreadPoolExecutor(8) as pool:
        readmes = dict(zip([r["full_name"] for r in te_lezen], pool.map(lees_readme, te_lezen)))

    plannen = []
    for repo in te_lezen:
        readme = readmes[repo["full_name"]]
        plan = regels.lees_plan(repo, readme)
        reden = regels.ruis_op_readme(plan, readme)
        if reden:
            ruis.append({"naam": plan["naam"], "link": plan["link"], "reden": reden, "fase": "readme"})
            continue
        plan["score"], plan["waarom_score"] = regels.score(plan)
        plan["zoektermen"] = sorted(treffers[repo["full_name"]])
        eerder = gezien.get(plan["naam"])
        plan["eerder_gemeld"] = eerder if eerder and eerder < vandaag.isoformat() else None
        plannen.append(plan)
    # bij gelijke score: eerst nieuw, dan sterren
    plannen.sort(key=lambda p: (p["score"], p["aangemaakt"] >= grens, p["sterren"], len(p["zoektermen"])), reverse=True)

    data = {
        "datum": vandaag.isoformat(),
        "gemaakt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "zoekvragen": n_vragen,
        "zoekvragen_mislukt": n_fout,
        "gevonden": len(repos),
        "gelezen": len(te_lezen),
        "niet_gelezen": len(niet_gelezen),
        "plannen": plannen,
        "ruis": ruis,
    }
    os.makedirs(uit, exist_ok=True)
    with open(os.path.join(uit, "kandidaten.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    tekst = rapport.maak(data)
    with open(os.path.join(uit, "rapport.md"), "w") as f:
        f.write(tekst)
    # bijwerken wat we gemeld hebben (alleen de top van vandaag), voor de volgende dagen
    if gezien_pad:
        for p in rapport.top(data):
            gezien.setdefault(p["naam"], vandaag.isoformat())
        with open(gezien_pad, "w") as f:
            json.dump(gezien, f, ensure_ascii=False, indent=0, sort_keys=True)
    return data


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--uit", required=True)
    a.add_argument("--gezien")
    a.add_argument("--max-readmes", type=int, default=2000)
    a.add_argument("--dagen", type=int, default=2)
    args = a.parse_args()
    data = run(args.uit, args.gezien, args.max_readmes, args.dagen, log=lambda s: print(s, flush=True))
    print(f"klaar: {len(data['plannen'])} plannen, {len(data['ruis'])} ruis, {data['zoekvragen_mislukt']} zoekvragen mislukt")
    if data["zoekvragen_mislukt"] > data["zoekvragen"] // 2:
        sys.exit(1)


if __name__ == "__main__":
    main()
