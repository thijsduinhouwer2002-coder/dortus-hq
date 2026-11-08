#!/usr/bin/env python3
"""Meet de openbare appgids van het Reddit Developer Platform (Devvit).

Haalt alle pagina's van https://developers.reddit.com/apps op (installs per app),
en per app de detailpagina (aanmaakdatum, categorieen, maker).
Schrijft data/devvit-apps-<datum>.json en voegt een regel toe aan data/devvit-apps.csv.
Rustig: drie verzoeken tegelijk, 0,3 seconde pauze na elk. Gebruik: python3 devvit-apps-meet.py [--snel]
(--snel slaat de detailpagina's over en telt alleen apps en installs.)
"""
import concurrent.futures, csv, datetime, html, json, os, re, statistics, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Dortus meetscript)"}
HIER = os.path.dirname(os.path.abspath(__file__))


def haal(url):
    for poging in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
        except Exception:
            time.sleep(2 + poging * 3)
    return ""


def lijst():
    apps, pagina, totaal = [], 1, 1
    while pagina <= totaal:
        t = haal(f"https://developers.reddit.com/apps?page={pagina}")
        m = re.search(r'totalPages="(\d+)"', t)
        if m:
            totaal = int(m.group(1))
        for kaart in re.findall(r"<devvit-app-card ([^>]*)>", t):
            a = dict(re.findall(r'([\w-]+)="([^"]*)"', kaart))
            apps.append({
                "naam": html.unescape(a.get("name", "")),
                "omschrijving": html.unescape(a.get("description", "")),
                "installs": int(a.get("installation-count", "0") or 0),
                "slug": a.get("app-url", "").replace("/apps/", ""),
            })
        pagina += 1
        time.sleep(0.3)
    return apps


def detail(app):
    t = html.unescape(haal(f"https://developers.reddit.com/apps/{app['slug']}"))
    m = re.search(r'appInfo="(\{.*?\})" ', t)
    info = {}
    if m:
        try:
            info = json.loads(m.group(1))
        except Exception:
            info = {}
    if not info:
        c = re.search(r'"createdAt":"([^"]+)"', t)
        info = {"createdAt": c.group(1) if c else ""}
    app["aangemaakt"] = (info.get("createdAt") or "")[:10]
    app["maker"] = (info.get("owner") or {}).get("displayName", "")
    cats = info.get("categoriesV2") or info.get("categories") or []
    app["categorieen"] = [c.get("name", str(c)) if isinstance(c, dict) else c for c in cats]
    return app


def main():
    snel = "--snel" in sys.argv
    vandaag = datetime.date.today().isoformat()
    apps = lijst()
    if not snel:
        def veilig(a):
            try:
                detail(a)
            except Exception as fout:
                a["fout"] = str(fout)
            time.sleep(0.3)
        # drie tegelijk, elk met een pauze: rustig maar binnen ±8 minuten klaar
        with concurrent.futures.ThreadPoolExecutor(3) as pool:
            list(pool.map(veilig, apps))
        with open(os.path.join(HIER, f"devvit-apps-{vandaag}.json"), "w") as f:
            json.dump(apps, f, ensure_ascii=False, indent=0)
    inst = [a["installs"] for a in apps]
    rij = {
        "datum": vandaag,
        "apps": len(apps),
        "installs_totaal": sum(inst),
        "mediaan": statistics.median(inst) if inst else 0,
        "apps_1000plus": sum(1 for x in inst if x >= 1000),
        "apps_100plus": sum(1 for x in inst if x >= 100),
        "top1": max(inst) if inst else 0,
    }
    pad = os.path.join(HIER, "devvit-apps.csv")
    nieuw = not os.path.exists(pad)
    with open(pad, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rij))
        if nieuw:
            w.writeheader()
        w.writerow(rij)
    print(json.dumps(rij))


if __name__ == "__main__":
    main()
