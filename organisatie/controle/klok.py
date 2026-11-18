#!/usr/bin/env python3
"""Klok: is een taak aan de beurt? Want GitHub laat geplande runs (on: schedule) in deze repo vaak vallen.

Roestronde R7, 19 nov 2026. Elke workflow met een schedule start ook bij elke push naar main. Zijn eerste job
draait dit script: niet aan de beurt, dan slaat de werkjob over en duurt de run seconden.

Gebruik in een workflow (job met contents: write en een checkout van deze repo):
  python3 -I organisatie/controle/klok.py <naam> <interval> [--paden a/**,b.py]
Gebruik door een agent:
  python3 organisatie/controle/klok.py stand                 laatste keer van elke taak
  python3 organisatie/controle/klok.py proef <interval> <laatst> <nu>    beslissing nabootsen, schrijft niets

Interval:
  30m, 1h, 7d          aan de beurt als er minstens zo lang verstreken is (min 10%, max 30 minuten speling,
                       zodat een schema dat een paar minuten vroeg komt niet net een beurt mist)
  1d-na-20:00UTC       aan de beurt als de laatste keer van vóór het laatste 20:00 UTC was (één keer per dag,
                       op de eerste start na 20:00 UTC); 7d-na-06:00UTC = één keer per 7 dagen, na 06:00
--paden              een push die een van deze bestanden raakt (glob, ** mag) is altijd aan de beurt;
                       zo blijft het oude paths-filter van de workflow werken
Handmatig gestart (workflow_dispatch) is altijd aan de beurt.

Waar de laatste keer staat: bestand <naam>.txt op de tak `klok` van deze repo (één regel: tijdstip, run, event).
Waarom daar en niet in organisatie/klok/ op main of in de API:
  - op main zou het dashboard alleen al 48 commits per dag geven, en elke bot-push kan botsen met een agent;
  - de API kan een geslaagde run die echt werkte niet onderscheiden van een geslaagde run die de klok oversloeg
    (beide "success"), tenzij je per run de jobs ophaalt: tot tientallen verzoeken per push;
  - op de tak `klok` schrijft alleen deze klok, één bestand per taak. Het zetten is een gewone push (nooit
    geforceerd) bovenop de stand die we net lazen: lukt die niet, dan was een ander net eerder en lezen we
    opnieuw. Zo kan dezelfde beurt nooit twee keer gegeven worden, ook zonder concurrency.
De klok wordt gezet vóór het werk: een mislukte run telt als beurt (geen herhaling bij elke push, wat bij de
keurder API-tegoed zou kosten). Opnieuw proberen = met de hand starten.

Uitvoer: regel beurt=ja of beurt=nee in $GITHUB_OUTPUT. Code 0, of 1 als de klok niet te lezen of te zetten
was (dan beurt=nee, voor de zekerheid niet draaien).
"""
import datetime as dt
import fnmatch
import json
import os
import re
import subprocess
import sys
import time

TAK = "klok"
UTC = dt.timezone.utc


def git(*args, invoer=None, env=None):
    r = subprocess.run(["git", *args], input=invoer, capture_output=True, text=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args[:2])}: {r.stderr.strip()[:300]}")
    return r.stdout.strip()


def lees_tijd(tekst):
    if not tekst:
        return None
    eerste = tekst.split()[0]
    try:
        return dt.datetime.strptime(eerste, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
    except ValueError:
        return None


def beslis(interval, laatst, nu):
    """Geeft (aan de beurt, reden)."""
    m = re.fullmatch(r"(\d+)d-na-(\d\d):(\d\d)UTC", interval)
    if m:
        dagen, uur, minuut = int(m[1]), int(m[2]), int(m[3])
        grens = nu.replace(hour=uur, minute=minuut, second=0, microsecond=0)
        if grens > nu:
            grens -= dt.timedelta(days=1)
        grens -= dt.timedelta(days=dagen - 1)
        if laatst is None:
            return True, "nog nooit gedraaid"
        if laatst < grens:
            return True, f"laatst {laatst:%Y-%m-%d %H:%M} UTC, van voor {grens:%Y-%m-%d %H:%M} UTC"
        return False, f"laatst {laatst:%Y-%m-%d %H:%M} UTC, na {grens:%Y-%m-%d %H:%M} UTC"
    m = re.fullmatch(r"(\d+)([mhd])", interval)
    if not m:
        raise ValueError(f"onbekend interval: {interval} (voorbeelden: 30m, 1h, 7d, 1d-na-20:00UTC)")
    lengte = dt.timedelta(**{{"m": "minutes", "h": "hours", "d": "days"}[m[2]]: int(m[1])})
    speling = min(lengte / 10, dt.timedelta(minutes=30))
    if laatst is None:
        return True, "nog nooit gedraaid"
    verstreken = nu - laatst
    tekst = f"laatst {laatst:%Y-%m-%d %H:%M} UTC, {int(verstreken.total_seconds() // 60)} min geleden"
    if verstreken >= lengte - speling:
        return True, tekst
    return False, tekst + f", beurt na {int((lengte - speling).total_seconds() // 60)} min"


def geraakte_paden(patronen):
    """Bestanden uit de push (GITHUB_EVENT_PATH) die op een patroon lijken."""
    pad = os.environ.get("GITHUB_EVENT_PATH")
    if not patronen or os.environ.get("GITHUB_EVENT_NAME") != "push" or not pad or not os.path.exists(pad):
        return []
    with open(pad, encoding="utf-8") as f:
        event = json.load(f)
    bestanden = set()
    for c in event.get("commits") or []:
        for soort in ("added", "modified", "removed"):
            bestanden.update(c.get(soort) or [])
    pats = [p.strip().replace("**", "*") for p in patronen.split(",") if p.strip()]
    return sorted(b for b in bestanden if any(fnmatch.fnmatchcase(b, p) for p in pats))


def tip_van_klok():
    """Commit van de tak klok (opgehaald), of None als de tak nog niet bestaat."""
    uit = git("ls-remote", "origin", f"refs/heads/{TAK}")
    if not uit:
        return None
    git("fetch", "-q", "--depth=1", "origin", f"refs/heads/{TAK}")
    return uit.split()[0]


def zet(tip, naam, regel):
    """Nieuwe commit op de tak klok met <naam>.txt = regel, bovenop tip. True als de push lukte."""
    blob = git("hash-object", "-w", "--stdin", invoer=regel + "\n")
    rijen = []
    if tip:
        rijen = [r for r in git("ls-tree", tip).splitlines() if r and r.split("\t", 1)[1] != f"{naam}.txt"]
    rijen.append(f"100644 blob {blob}\t{naam}.txt")
    # --missing: de checkout is blobloos (filter blob:none), de bestanden van andere taken staan dan niet lokaal
    boom = git("mktree", "--missing", invoer="\n".join(sorted(rijen, key=lambda r: r.split("\t", 1)[1])) + "\n")
    env = dict(os.environ, GIT_AUTHOR_NAME="dortus-klok", GIT_COMMITTER_NAME="dortus-klok",
               GIT_AUTHOR_EMAIL="41898282+github-actions[bot]@users.noreply.github.com",
               GIT_COMMITTER_EMAIL="41898282+github-actions[bot]@users.noreply.github.com")
    ouder = ["-p", tip] if tip else []
    commit = git("commit-tree", boom, *ouder, "-m", f"Klok {naam}: {regel}", env=env)
    r = subprocess.run(["git", "push", "-q", "origin", f"{commit}:refs/heads/{TAK}"], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  push naar {TAK} lukte niet (een ander was eerder?): {r.stderr.strip()[:200]}")
    return r.returncode == 0


def uitvoer(beurt):
    pad = os.environ.get("GITHUB_OUTPUT")
    if pad:
        with open(pad, "a", encoding="utf-8") as f:
            f.write(f"beurt={'ja' if beurt else 'nee'}\n")


def klok(naam, interval, paden):
    if not re.fullmatch(r"[a-z0-9-]+", naam):
        raise ValueError("naam: alleen kleine letters, cijfers en -")
    beslis(interval, None, dt.datetime.now(UTC))  # interval controleren voor we iets doen
    event = os.environ.get("GITHUB_EVENT_NAME", "lokaal")
    geraakt = geraakte_paden(paden)
    for poging in range(1, 6):
        nu = dt.datetime.now(UTC).replace(microsecond=0)
        tip = tip_van_klok()
        laatst_regel = ""
        if tip:
            try:
                laatst_regel = git("show", f"{tip}:{naam}.txt")
            except RuntimeError:
                laatst_regel = ""
        laatst = lees_tijd(laatst_regel)
        aan_de_beurt, reden = beslis(interval, laatst, nu)
        if event == "workflow_dispatch":
            aan_de_beurt, reden = True, f"met de hand gestart ({reden})"
        elif geraakt:
            aan_de_beurt, reden = True, f"push raakt {', '.join(geraakt[:3])} ({reden})"
        if not aan_de_beurt:
            print(f"Klok {naam} ({interval}): niet aan de beurt: {reden}.")
            return False
        regel = f"{nu:%Y-%m-%dT%H:%M:%SZ} run {os.environ.get('GITHUB_RUN_ID', '-')} ({event})"
        if zet(tip, naam, regel):
            print(f"Klok {naam} ({interval}): aan de beurt: {reden}. Gezet: {regel}")
            return True
        time.sleep(poging * 2)
    raise RuntimeError("klok niet te zetten na 5 pogingen")


def stand():
    try:
        tip = tip_van_klok()
    except RuntimeError as e:
        print(f"Tak {TAK} niet te lezen: {e}")
        return 2
    if not tip:
        print(f"Tak {TAK} bestaat nog niet.")
        return 0
    for rij in git("ls-tree", tip).splitlines():
        bestand = rij.split("\t", 1)[1]
        print(f"{bestand[:-4]:<16} {git('show', f'{tip}:{bestand}')}")
    return 0


def main(argv):
    if argv[:1] == ["stand"]:
        return stand()
    if argv[:1] == ["proef"] and len(argv) == 4:
        laatst = None if argv[2] == "nooit" else lees_tijd(argv[2])
        try:
            ja, reden = beslis(argv[1], laatst, lees_tijd(argv[3]))
        except ValueError as e:
            print(f"FOUT: {e}")
            return 2
        print(f"{'ja ' if ja else 'nee'} {reden}")
        return 0
    if len(argv) not in (2, 4) or (len(argv) == 4 and argv[2] != "--paden"):
        print(__doc__)
        return 2
    try:
        ja = klok(argv[0], argv[1], argv[3] if len(argv) == 4 else "")
    except (RuntimeError, ValueError) as e:
        print(f"Klok {argv[0]}: FOUT: {e}. Voor de zekerheid niet aan de beurt.")
        uitvoer(False)
        return 1
    uitvoer(ja)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
