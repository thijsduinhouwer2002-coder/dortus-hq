#!/usr/bin/env python3
"""Dortus-dashboard: verzamelt de stand van de ploeg en de producten in data.json en index.html.

Draait elk half uur in GitHub Actions (geen Claude, geen tokens). Leest alleen de repo en een
paar openbare adressen. Gebruik: python3 dashboard/bouw.py <uitvoermap>
"""
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dashboard", "uit")
REPO = "thijsduinhouwer2002-coder/dortus-hq"
NU = dt.datetime.now(dt.timezone.utc)
AMS = dt.timezone(dt.timedelta(hours=1))  # wintertijd; zomertijd is +2, klein verschil voor een dashboard


def lees(pad):
    try:
        with open(os.path.join(ROOT, pad), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def haal(url, json_=True, token=False):
    req = urllib.request.Request(url, headers={"User-Agent": "dortus-dashboard"})
    if token and os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
            return (json.loads(data) if json_ else r.status)
    except urllib.error.HTTPError as e:
        return None if json_ else e.code
    except Exception:
        return None


def schoon(tekst, max_len=220):
    t = re.sub(r"\*\*|`|~~", "", tekst)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip(" -")
    return t if len(t) <= max_len else t[: max_len - 1].rsplit(" ", 1)[0] + "…"


def tijd_ams(t):
    return t.astimezone(AMS).strftime("%H:%M")


def geleden(t):
    m = int((NU - t).total_seconds() // 60)
    if m < 60:
        return f"{m} min geleden"
    if m < 60 * 24:
        return f"{m // 60} uur geleden"
    return f"{m // 1440} dagen geleden"


# ---------- commits ----------
log = subprocess.run(
    ["git", "-C", ROOT, "log", "--since=36 hours ago", "--format=%H|%ct|%an|%s"],
    capture_output=True, text=True,
).stdout.strip().splitlines()
commits = []
for regel in log:
    try:
        h, ts, auteur, onderwerp = regel.split("|", 3)
    except ValueError:
        continue
    commits.append({"hash": h[:7], "tijd": dt.datetime.fromtimestamp(int(ts), dt.timezone.utc),
                    "auteur": auteur, "onderwerp": onderwerp})

config = json.loads(lees("dashboard/ploeg.json"))


def van_wie(c):
    s = c["onderwerp"].lower()
    for p in config["mensen"]:
        for k in p["sleutels"]:
            if s.startswith(k.lower()):
                return p["naam"]
    if c["auteur"] == "Dortus":
        return "Hoofdchat"
    return None


for c in commits:
    c["wie"] = van_wie(c)

vandaag_start = NU.astimezone(AMS).replace(hour=0, minute=0, second=0, microsecond=0).astimezone(dt.timezone.utc)
ploeg = []
for p in config["mensen"]:
    eigen = [c for c in commits if c["wie"] == p["naam"]]
    laatste = eigen[0] if eigen else None
    ploeg.append({
        "naam": p["naam"], "rol": p["rol"], "team": p["team"], "schema": p["schema"], "actief": p["actief"],
        "vandaag": sum(1 for c in eigen if c["tijd"] >= vandaag_start),
        "laatst": geleden(laatste["tijd"]) if laatste else "langer dan 36 uur",
        "laatst_min": int((NU - laatste["tijd"]).total_seconds() // 60) if laatste else 99999,
        "wat": schoon(laatste["onderwerp"].split(":", 1)[-1], 140) if laatste else "",
    })

feed = [{"tijd": tijd_ams(c["tijd"]), "wie": c["wie"] or "Ploeg", "wat": schoon(c["onderwerp"].split(":", 1)[-1] if c["wie"] else c["onderwerp"], 160)}
        for c in commits[:25]]

# ---------- wacht op Thijs ----------
lijst = lees("organisatie/lijst-thijs.md").splitlines()
wacht = []
for r in lijst:
    if r.startswith("- **") and not r.startswith("- ~~"):
        kop = re.match(r"- \*\*(.+?)\*\*", r)
        titel = schoon(kop.group(1) if kop else r, 160)
        rest = schoon(r[kop.end():] if kop else "", 220)
        ter_info = bool(re.search(r"ter info|niets te doen|niet nu|LATER|later, niet|niet dringend|mag ook later|niets nodig|GEÜPLOAD|INGEDIEND|staat online|staat live|^- \*\*[^*]*:\*\*\s*$", r, re.I))
        wacht.append({"titel": titel, "uitleg": rest, "ter_info": ter_info})

# ---------- besluiten ----------
besluiten = []
for r in lees("organisatie/besluiten.md").splitlines():
    if r.startswith("- ") and "|" in r:
        delen = [d.strip() for d in r[2:].split("|")]
        if len(delen) >= 3:
            besluiten.append({"wanneer": schoon(delen[0], 40), "wie": schoon(delen[1], 20), "wat": schoon(delen[2], 200)})
    if len(besluiten) >= 6:
        break

# ---------- producten ----------
def eerste_stand(pad):
    for r in lees(pad).splitlines():
        if r.startswith("- "):
            return schoon(r, 260)
    return ""


cijfers = {}
stats = haal("https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json")
if isinstance(stats, dict) and "rollwright" in stats:
    cijfers["obsidian"] = {"hoofd": f"{stats['rollwright'].get('downloads', 0)}", "label": "downloads", "staat": "live, geparkeerd"}
jb = haal("https://plugins.jetbrains.com/api/plugins/35901")
if isinstance(jb, dict):
    cijfers["jetbrains"] = {"hoofd": str(jb.get("downloads", 0)), "label": "downloads",
                            "staat": "goedgekeurd" if jb.get("approve") else "in keuring"}
cj = haal("https://extensions.blender.org/add-ons/click-joints/", json_=False)
issues = haal(f"https://api.github.com/repos/thijsduinhouwer2002-coder/click-joints/issues?state=open", token=True)
cijfers["blender"] = {"hoofd": "live" if cj == 200 else "keuring", "label": "extensions.blender.org",
                      "staat": ("goedgekeurd" if cj == 200 else "Awaiting Review") + (f", {len(issues)} meldingen" if isinstance(issues, list) else "")}
cijfers["steam"] = {"hoofd": "bouwen", "label": "prototype", "staat": "nog niet betaald of gepubliceerd"}
cijfers["tiktok"] = {"hoofd": "bouwen", "label": "eerst Moneybird", "staat": "uitbrengen na KvK"}
cijfers["garmin"] = {"hoofd": "start", "label": "product kiezen", "staat": "nog niets gebouwd"}

producten = []
for p in config["producten"]:
    c = cijfers.get(p["soort"], {})
    producten.append({"naam": p["naam"], "platform": p["platform"], "hoofd": c.get("hoofd", "?"),
                      "label": c.get("label", ""), "staat": c.get("staat", ""), "stand": eerste_stand(p["status"])})

# ---------- tests (GitHub Actions) ----------
runs = haal(f"https://api.github.com/repos/{REPO}/actions/runs?per_page=60&branch=main", token=True)
tests = []
if isinstance(runs, dict):
    gezien = set()
    for r in runs.get("workflow_runs", []):
        naam = r.get("name", "")
        if naam in gezien or naam.lower().startswith("dashboard"):
            continue
        gezien.add(naam)
        tests.append({"naam": naam, "uitkomst": r.get("conclusion") or r.get("status"),
                      "wanneer": geleden(dt.datetime.fromisoformat(r["created_at"].replace("Z", "+00:00")))})

actief = [p for p in ploeg if p["actief"]]
data = {
    "gebouwd": NU.isoformat(timespec="minutes"),
    "gebouwd_ams": NU.astimezone(AMS).strftime("%d-%m %H:%M"),
    "samenvatting": {
        "actief": len(actief),
        "commits_vandaag": sum(1 for c in commits if c["tijd"] >= vandaag_start),
        "wacht_op_thijs": sum(1 for w in wacht if not w["ter_info"]),
        "stil": [p["naam"] for p in actief if p["laatst_min"] > 150 and p["schema"] == "elk uur"],
    },
    "ploeg": ploeg, "feed": feed, "wacht_op_thijs": wacht, "besluiten": besluiten,
    "producten": producten, "tests": tests[:12],
}

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

sjabloon = lees("dashboard/sjabloon.html")
pagina = sjabloon.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(pagina)
print(f"dashboard gebouwd: {len(ploeg)} mensen, {len(commits)} commits, {len(wacht)} lijstpunten")
