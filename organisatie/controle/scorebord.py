#!/usr/bin/env python3
"""Scorebord van Dortus: per product in één blik hoe het gaat, alleen met openbare bronnen.

Vera, 16 nov 2026, opdracht hoofdchat 16 nov 17:05.

Gebruik:
  python3 organisatie/controle/scorebord.py            # meet, werkt de geschiedenis bij, schrijft scorebord.md
  python3 organisatie/controle/scorebord.py --droog    # meet en laat zien, schrijft niets

Wat het meet (alles openbaar, niet inloggen):
- Blender: alle extensies van maker Thijs-Dortus op extensions.blender.org (API voor de lijst,
  de openbare productpagina voor Downloads en het aantal beoordelingen).
- Superhive: de verkoopklasse ("Sales 10+" enzovoort) en beoordelingen van Click Joints Pro.
  Superhive weigert soms verkeer van buiten GitHub; dan staat er "niet leesbaar".
- Garmin: alle openbare apps van maker Dortus in de winkel-API (downloads, beoordelingen, prijs).
  Het makernummer wordt bij elke run uit het antwoord van Ebb gelezen en nergens opgeschreven.
- Obsidian: downloads van Rollwright uit community-plugin-stats.json.
- JetBrains: downloads, keuring en beoordeling van Bison & Flex.
- Gumroad (sinds 18 nov, R6): verkopen en omzet per product uit de API met GUMROAD_ACCESS_TOKEN (alleen lezen).
- Kit (R6): actieve abonnees in totaal en per tag met KIT_API_KEY (alleen aantallen).
- Discord (R6): leden en online van de Hats-server via de openbare invite-API (code in scorebord_bronnen.py).
- YouTube (R6): weergaven per filmpje van @Dortusapps uit de openbare RSS, zonder sleutel.
  Zie scorebord_bronnen.py.
- dortus.com (sinds 16 nov 20:35): bezoekers per dag uit Amami, totaal en per productpagina; sinds 24 nov (Meter) ook per verwijzende site.
  Met sleutel: AMAMI_API_KEY als GitHub-secret, alleen gelezen uit de
  omgeving, nooit geprint of opgeslagen. Zonder sleutel slaat het script dit deel over. Het
  website-id wordt elke run uit de html van dortus.com gelezen. Amami bewaart cijfers 7 dagen,
  dus het script haalt elke run de afgelopen 6 hele dagen (Amsterdamse tijd, vanaf 16 nov) die nog
  niet in de geschiedenis staan, plus vandaag tot nu (alleen in scorebord.md). Gratis plan:
  10 verzoeken per minuut, daarom 7 seconden tussen verzoeken.

Geschiedenis: organisatie/scorebord-data.csv (datum, product, maat, waarde). Een tweede run op
dezelfde dag vervangt de cijfers van die dag. Uitvoer: organisatie/scorebord.md.
"""
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scorebord_amami as amami  # noqa: E402
import scorebord_bronnen as bronnen  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
ORG = os.path.dirname(HIER)
DATA = os.path.join(ORG, "scorebord-data.csv")
UIT = os.path.join(ORG, "scorebord.md")
UA = "Mozilla/5.0 (Dortus scorebord; openbare cijfers, 1 keer per dag)"

EBB_WINKEL_ID = "5280653d-1681-452d-8c03-7cbdc7284641"
BLENDER_MAKER = "Thijs-Dortus"
SUPERHIVE = {"Click Joints Pro": "https://superhivemarket.com/products/click-joints-pro"}
OBSIDIAN = {"Rollwright": "rollwright"}
JETBRAINS = {"Bison & Flex": 35901}
GARMIN_NAMEN = {EBB_WINKEL_ID: "Ebb"}  # vaste naam per winkel-id, zodat de geschiedenis niet breekt bij een nieuwe titel
VERWACHT_GARMIN = ["Ebb Calm"]  # staat hij er nog niet, dan een regel "nog niet in de winkel"
GARMIN_API = "https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps"


def haal(url, json_=True, pogingen=3):
    for p in range(pogingen):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=40) as r:
                body = r.read().decode("utf-8", "replace")
            return json.loads(body) if json_ else body
        except Exception as e:  # noqa: BLE001
            fout = e
            time.sleep(2 * (p + 1))
    print(f"  niet gelukt: {url} ({fout})", file=sys.stderr)
    return None


def haal_curl(url):
    """Superhive weigert urllib maar liet curl op GitHub Actions toe (meting 15 nov, 2.296 pagina's)."""
    import subprocess
    for p in range(3):
        r = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", "Mozilla/5.0 (dortus-verkenner; alleen lezen)",
                            "-w", "\n%{http_code}", url], capture_output=True, text=True, errors="replace")
        body, _, code = r.stdout.rpartition("\n")
        if code == "200":
            return body
        time.sleep(3 * (p + 1))
    print(f"  niet gelukt: {url} (curl {code})", file=sys.stderr)
    return None


def getal(s):
    try:
        return int(str(s).replace(",", "").replace(".", "").strip())
    except ValueError:
        return None


# Elke meting: (product, platform, maat, waarde, toelichting)
METINGEN = []
NOTEN = []


def meet(product, platform, maat, waarde, toel=""):
    METINGEN.append((product, platform, maat, waarde, toel))


def blender():
    lijst = haal("https://extensions.blender.org/api/v1/extensions/")
    if not isinstance(lijst, dict):
        NOTEN.append("Blender: lijst van extensions.blender.org niet leesbaar.")
        return
    eigen = [x for x in lijst.get("data", []) if x.get("maintainer") == BLENDER_MAKER]
    if not eigen:
        NOTEN.append("Blender: geen extensie van Thijs-Dortus in de openbare lijst.")
    for x in eigen:
        naam, site = x.get("name", x.get("id")), x.get("website", "")
        pagina = haal(site, json_=False) if site.startswith("https://extensions.blender.org/") else None
        toel = f"versie {x.get('version')}"
        if not pagina:
            meet(naam, "Blender", "downloads", None, toel + ", pagina niet leesbaar")
            continue
        tekst = re.sub(r"\s+", " ", pagina)
        m = re.search(r"<dt>\s*Downloads\s*</dt>\s*<dd>\s*([\d,.]+)\s*</dd>", tekst)
        meet(naam, "Blender", "downloads", getal(m.group(1)) if m else None, toel)
        # het getal tussen haakjes na <dt>Rating</dt>, bijv. "(65)"; zonder review staat er "Leave a review"
        blok = re.search(r"<dt>\s*Rating\s*</dt>(.{0,1500}?)</dd>", tekst)
        m = re.search(r"\(\s*([\d,]+)\s*\)", blok.group(1)) if blok else None
        meet(naam, "Blender", "beoordelingen", getal(m.group(1)) if m else (0 if blok else None), "")


def superhive():
    for naam, url in SUPERHIVE.items():
        t = haal_curl(url)
        if not t:
            meet(naam, "Superhive", "verkoopklasse", None, "niet leesbaar (Superhive weigert dit adres soms)")
            continue
        s = re.sub(r"\s+", " ", re.sub("<[^>]+>", "|", t))
        # zelfde manier als onderzoek/verkenner/data/superhive-6mnd-script.py (nu in release archief-beelden-2026-11-22) (15 nov, 2.296 pagina's goed gelezen)
        m = re.search(r"\|\s*Sales\s*\|[| ]*([^|]{1,15})", s)
        klasse = m.group(1).strip() if m else "geen verkoopblok (onder 10 of nog niet zichtbaar)"
        m = re.search(r'"reviewCount"\s*:\s*"?(\d+)', t)
        meet(naam, "Superhive", "verkoopklasse", klasse, "Superhive toont alleen klassen")
        meet(naam, "Superhive", "beoordelingen", int(m.group(1)) if m else 0, "")


def garmin():
    ebb = haal(f"{GARMIN_API}/{EBB_WINKEL_ID}")
    if not isinstance(ebb, dict):
        NOTEN.append("Garmin: winkel-API niet leesbaar.")
        return
    apps = haal(f"{GARMIN_API}/developer/{ebb.get('developerId')}?startPageIndex=0&pageSize=30")
    if isinstance(apps, dict):
        apps = apps.get("apps") or apps.get("data") or apps.get("items") or []
    if not isinstance(apps, list) or not apps:
        apps = [ebb]
    namen = []
    for a in apps:
        d = haal(f"{GARMIN_API}/{a.get('id')}") if a.get("id") != EBB_WINKEL_ID else ebb
        d = d if isinstance(d, dict) else a
        loc = {l.get("locale"): l.get("name") for l in d.get("appLocalizations") or []}
        naam = GARMIN_NAMEN.get(d.get("id")) or (loc.get("en") or next(iter(loc.values()), None) or d.get("id", "?")[:8]).split(":")[0].strip()
        namen.append(naam)
        prijs = ((d.get("pricing") or {}).get("salePrice") or {}).get("formattedPrice", "gratis")
        soort = {"1": "wijzerplaat", "2": "app", "3": "widget", "4": "dataveld", "5": "muziek"}.get(str(d.get("typeId")), "")
        toel = f"{soort}, {prijs}, versie {d.get('latestExternalVersion')}".strip(", ")
        meet(naam, "Garmin", "downloads", d.get("downloadCount"), toel)
        meet(naam, "Garmin", "beoordelingen", d.get("reviewCount"),
             f"gemiddeld {d.get('averageRating')}" if d.get("reviewCount") else "")
    for verwacht in VERWACHT_GARMIN:
        if not any(verwacht.lower() in n.lower() for n in namen):
            meet(verwacht, "Garmin", "downloads", "nog niet in de winkel", "niet in de openbare lijst van maker Dortus")


def obsidian():
    stats = haal("https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json")
    for naam, pid in OBSIDIAN.items():
        s = stats.get(pid) if isinstance(stats, dict) else None
        meet(naam, "Obsidian", "downloads", s.get("downloads") if s else None, "community-plugin-stats.json")


def jetbrains():
    for naam, pid in JETBRAINS.items():
        d = haal(f"https://plugins.jetbrains.com/api/plugins/{pid}")
        r = haal(f"https://plugins.jetbrains.com/api/plugins/{pid}/rating")
        if not isinstance(d, dict):
            meet(naam, "JetBrains", "downloads", None, "niet leesbaar")
            continue
        stemmen = sum((r or {}).get("votes", {}).values()) if isinstance(r, dict) else 0
        meet(naam, "JetBrains", "downloads", d.get("downloads"),
             ("goedgekeurd" if d.get("approve") else "in keuring") + f", {d.get('pricingModel', '').lower()}")
        meet(naam, "JetBrains", "beoordelingen", stemmen, "")


def gumroad():
    bronnen.gumroad(meet, NOTEN)


def kit():
    bronnen.kit(meet, NOTEN)


def discord():
    bronnen.discord(meet, NOTEN)


def youtube():
    bronnen.youtube(meet, NOTEN)


def tiktok():
    teksten = []
    for pad in TIKTOK_LOGBOEKEN:
        try:
            with open(os.path.join(os.path.dirname(ORG), pad), encoding="utf-8") as f:
                teksten.append(f.read())
        except OSError:
            pass
    bronnen.tiktok(meet, NOTEN, teksten)


# Herkomst (Meter, 23 nov 2026): verkopen per bron en één regel per bron per dag
METEN = os.path.join(ORG, "meten")
VERKOPEN = os.path.join(METEN, "verkopen.csv")
DAG = os.path.join(METEN, "dag.csv")
TIKTOK_LOGBOEKEN = ["commercie/geplaatst.md", "marketing/dagrapport.md", "organisatie/meten/tiktok.md"]
PRO = "Click Joints Pro"


def soort_bron(r):
    """Waar kwam deze verkoop vandaan, in één woord of twee."""
    code = r.get("kortingscode", "")
    if code.upper().startswith("CJP"):
        return f"maker ({code})"
    if code:
        return f"code {code}"
    if r.get("utm_source"):
        return f"utm {r['utm_source']}"
    if r.get("affiliate") == "ja":
        return "affiliate"
    return r.get("bron") or "onbekend"


def herkomst_tabel(rijen):
    if rijen is None:
        return ["", "## Herkomst Gumroad-verkopen", "", "Niet gemeten deze run (zie meldingen)."]
    uit = ["", "## Herkomst Gumroad-verkopen", "",
           f"Per verkoop, zonder persoonsgegevens, uit Gumroad API v2 /sales (GEZIEN, leessleutel). Volledige lijst in `organisatie/meten/verkopen.csv`.", "",
           "| Datum | Product | Bedrag | Bron (referrer) | utm | Kortingscode | Herkomst |", "|---|---|---|---|---|---|---|"]
    for r in rijen:
        utm = "/".join(x for x in (r["utm_source"], r["utm_medium"], r["utm_campaign"]) if x)
        uit.append(f"| {r['datum']} | {r['product']} | {r['bedrag']} {r['munt']} | {r['bron']} | {utm} | {r['kortingscode']} | {soort_bron(r)} |")
    if not rijen:
        uit.append("| | geen verkopen | | | | | |")
    return uit


def codes_tabel(rijen):
    kop = ["", "## Kortingscodes Gumroad", ""]
    if rijen is None:
        return kop + ["Niet gemeten deze run (zie meldingen)."]
    uit = kop + ["Per product uit Gumroad API v2 /products/:id/offer_codes (GEZIEN, leessleutel, alleen lezen). "
                 "Codes met 100% korting staan er niet voluit in.", "",
                 "| Product | Code | Korting | Keer gebruikt | Max | Alle producten |", "|---|---|---|---|---|---|"]
    for r in rijen:
        uit.append(f"| {r['product']} | {r['code']} | {r['korting']} | {r['gebruikt']} | {r['max']} | {r['alle_producten']} |")
    if not rijen:
        uit.append("| | geen kortingscodes | | | | |")
    return uit


def schrijf_verkopen(rijen):
    os.makedirs(METEN, exist_ok=True)
    with open(VERKOPEN, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=bronnen.VERKOOP_KOLOMMEN + ["herkomst"])
        w.writeheader()
        for r in rijen:
            w.writerow({**r, "herkomst": soort_bron(r)})


def dag_rijen(dag, metingen, bezoek, verkopen):
    """Eén regel per bron per maat voor deze dag (kolommen datum, bron, maat, waarde, gezien_bron)."""
    uit = []
    for p, pl, m, w, _ in metingen:
        if w in (None, ""):
            continue
        uit.append({"datum": dag, "bron": f"{pl} {p}", "maat": m, "waarde": w, "gezien_bron": BRON.get(pl, "GEZIEN")})
    for d, p, m, w in bezoek:
        uit.append({"datum": d, "bron": f"dortus.com {p}", "maat": m, "waarde": w,
                    "gezien_bron": "GEZIEN, Amami (Umami-API, leessleutel)"})
    if verkopen is not None:
        tel = {}
        for r in verkopen:
            if r["datum"] == dag and r["terug"] == "nee":
                k = (r["product"], soort_bron(r))
                tel[k] = tel.get(k, 0) + 1
        for (prod, herk), n in sorted(tel.items()):
            uit.append({"datum": dag, "bron": f"Gumroad {prod} via {herk}", "maat": "verkopen", "waarde": n,
                        "gezien_bron": "GEZIEN, Gumroad API v2 /sales (leessleutel)"})
    return uit


def schrijf_dag(nieuw):
    os.makedirs(METEN, exist_ok=True)
    kol = ["datum", "bron", "maat", "waarde", "gezien_bron"]
    oud = []
    if os.path.exists(DAG):
        with open(DAG, newline="", encoding="utf-8") as f:
            oud = list(csv.DictReader(f))
    sleutels = {(r["datum"], r["bron"], r["maat"]) for r in nieuw}
    alles = [r for r in oud if (r["datum"], r["bron"], r["maat"]) not in sleutels] + nieuw
    with open(DAG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kol)
        w.writeheader()
        for r in sorted(alles, key=lambda r: (r["datum"], r["bron"], r["maat"])):
            w.writerow({k: r.get(k, "") for k in kol})


# Waar elk cijfer vandaan komt (alles GEZIEN: het script leest het zelf, elke run)
BRON = {
    "Blender": "GEZIEN, extensions.blender.org (API en productpagina)",
    "Superhive": "GEZIEN, superhivemarket.com productpagina",
    "Garmin": "GEZIEN, apps.garmin.com winkel-API",
    "Obsidian": "GEZIEN, obsidian-releases community-plugin-stats.json",
    "JetBrains": "GEZIEN, plugins.jetbrains.com API",
    "Gumroad": "GEZIEN, Gumroad API v2 /products (leessleutel)",
    "Kit": "GEZIEN, Kit API (leessleutel), alleen aantallen",
    "Discord": "GEZIEN, discord.com invite-API (with_counts)",
    "YouTube": "GEZIEN, youtube.com/feeds/videos.xml (RSS)",
    "TikTok": "GEZIEN, tiktok.com videopagina (playCount)",
}


def lees_geschiedenis():
    if not os.path.exists(DATA):
        return []
    with open(DATA, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def waarde_op(rijen, product, maat, dag):
    """Laatste meting op of vóór die dag, met de datum erbij."""
    best = None
    for r in rijen:
        if r["product"] == product and r["maat"] == maat and r["datum"] <= dag and r["waarde"] != "":
            if best is None or r["datum"] > best["datum"]:
                best = r
    return (best["waarde"], best["datum"]) if best else (None, None)


def tekst(w):
    return "?" if w in (None, "") else str(w)


def verschil(nu, oud):
    a, b = getal(nu), getal(oud)
    if a is None or b is None or not str(nu).isdigit() or not str(oud).isdigit():
        return ""
    d = a - b
    return f"+{d}" if d > 0 else str(d)


def main():
    droog = "--droog" in sys.argv
    vandaag = dt.datetime.now(dt.timezone.utc).date()
    for stap in (blender, superhive, garmin, obsidian, jetbrains, gumroad, kit, discord, youtube, tiktok):
        try:
            stap()
        except Exception as e:  # noqa: BLE001
            NOTEN.append(f"{stap.__name__}: fout tijdens meten ({type(e).__name__}).")

    try:
        verkopen = bronnen.gumroad_verkopen(NOTEN)
    except Exception as e:  # noqa: BLE001
        verkopen = None
        NOTEN.append(f"herkomst: fout tijdens meten ({type(e).__name__}).")

    try:
        codes = bronnen.gumroad_codes(NOTEN)
    except Exception as e:  # noqa: BLE001
        codes = None
        NOTEN.append(f"kortingscodes: fout tijdens meten ({type(e).__name__}).")

    geschiedenis = lees_geschiedenis()
    # een dag geldt als gemeten als er een totaal en een verwijzerregel is (verwijzers sinds 24 nov, dus oudere dagen één keer opnieuw)
    met_verw = {r["datum"] for r in geschiedenis if r["platform"] == "dortus.com" and str(r["product"]).startswith("verwijzer ")}
    totaal_al = {r["datum"] for r in geschiedenis if r["platform"] == "dortus.com" and r["product"] == "dortus.com"}
    al = totaal_al & met_verw
    try:
        amami.dortus_bezoek(al, haal, NOTEN, zonder_verw=totaal_al - met_verw)
        amami.dortus_detail(haal, NOTEN)
    except Exception as e:  # noqa: BLE001
        NOTEN.append(f"dortus_bezoek: fout tijdens meten ({type(e).__name__}).")
    # bezoekrijen hebben de bezoekdag als datum; ze blijven staan, behalve een dag die opnieuw gehaald is
    oud = [r for r in geschiedenis
           if (r["platform"] == "dortus.com" and r["datum"] not in amami.BEZOEK_DAGEN)
           or (r["platform"] != "dortus.com" and r["datum"] != vandaag.isoformat())]
    bezoek_nieuw = [{"datum": d, "product": p, "platform": "dortus.com", "maat": m, "waarde": w} for d, p, m, w in amami.BEZOEK]
    nieuw = [{"datum": vandaag.isoformat(), "product": p, "platform": pl, "maat": m, "waarde": "" if w is None else w}
             for p, pl, m, w, _ in METINGEN]
    alles = oud + nieuw + bezoek_nieuw

    gister = (vandaag - dt.timedelta(days=1)).isoformat()
    week = (vandaag - dt.timedelta(days=7)).isoformat()
    regels = [
        "# Scorebord Dortus",
        "",
        f"Gemeten op {vandaag.isoformat()} om {dt.datetime.now(dt.timezone.utc):%H:%M} UTC met `organisatie/controle/scorebord.py`, "
        "openbare bronnen, plus Gumroad, Kit en bezoekers van dortus.com (Amami) met leessleutels. Elk cijfer is GEZIEN: het script leest het zelf; de bron staat per regel. Draait elke dag om 06:41 UTC (workflow \"Scorebord\"). "
        "Gisteren en 7 dagen terug: de laatste meting op of vóór die dag; staat er een datum tussen haakjes, "
        "dan is dat een oudere meting. Geschiedenis in `organisatie/scorebord-data.csv`.",
        "",
        "| Product | Platform | Maat | Vandaag | Gisteren | 7 dagen terug | Erbij in 7 dagen | Stand | Bron |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for p, pl, m, w, toel in METINGEN:
        g, gd = waarde_op([r for r in oud if r["platform"] != "dortus.com"], p, m, gister)
        k, kd = waarde_op(oud, p, m, week)
        gt = tekst(g) + (f" ({gd})" if gd and gd != gister else "") if g is not None else "geen meting"
        kt = tekst(k) + (f" ({kd})" if kd and kd != week else "") if k is not None else "geen meting"
        regels.append(f"| {p} | {pl} | {m} | {tekst(w)} | {gt} | {kt} | {verschil(w, k)} | {toel} | {BRON.get(pl, 'GEZIEN')} |")
    regels += herkomst_tabel(verkopen)
    regels += codes_tabel(codes)
    regels += amami.bezoek_tabel(alles)
    regels += amami.verwijzer_tabel(alles)
    regels += amami.detail_tabel()
    regels += ["", "## Wat niet te zien is", "",
               "- Gumroad-bezoekers staan niet in de Gumroad API v2 (verkopen per product, en sinds 23 nov per verkoop de bron via /sales); bezoekers van de productpagina's op dortus.com staan hierboven (Amami).",
               "- YouTube: de RSS toont alleen de nieuwste openbare filmpjes (max 15); oudere filmpjes en abonnees vragen de YouTube Data API (sleutel ontbreekt nog, zie toegang.md).",
               "- Kit en Gumroad: alleen aantallen, nooit namen of mailadressen van kopers of abonnees.",
               "- Superhive toont alleen een verkoopklasse (0, 10+, 100+ ...), geen precies aantal.",
               "- Garmin telt downloads per app; bij een betaalde app is dat ongeveer het aantal kopers, inclusief terugbetalingen binnen 48 uur (GOK).",
               "- Steam (Hats of the Fallen) is nog niet in de winkel; volgers zijn pas te meten als de pagina openbaar is."]
    if NOTEN:
        regels += ["", "## Meldingen van deze run", ""] + [f"- {n}" for n in NOTEN]
    md = "\n".join(regels) + "\n"

    print(md)
    gemeten = [w for _, _, _, w, _ in METINGEN if w not in (None, "")]
    if len(gemeten) < 3:
        print("Bijna alle bronnen mislukt, niets opgeslagen.", file=sys.stderr)
        return 1
    if droog:
        return 0
    with open(DATA, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["datum", "product", "platform", "maat", "waarde"])
        w.writeheader()
        for r in sorted(alles, key=lambda r: (r["datum"], r["platform"], r["product"], r["maat"])):
            w.writerow({k: r.get(k, "") for k in ["datum", "product", "platform", "maat", "waarde"]})
    with open(UIT, "w", encoding="utf-8") as f:
        f.write(md)
    if verkopen is not None:
        schrijf_verkopen(verkopen)
    schrijf_dag(dag_rijen(vandaag.isoformat(), METINGEN, amami.BEZOEK, verkopen))
    return 0


if __name__ == "__main__":
    sys.exit(main())
