"""Extra bronnen voor scorebord.py: Gumroad, Kit, Discord en YouTube. Roestronde R6, 18 nov 2026.

Regels:
- Sleutels komen alleen uit de omgeving (GitHub-secrets GUMROAD_ACCESS_TOKEN, KIT_API_KEY) en staan altijd in een kop of worden nooit geprint. Foutregels noemen alleen
  de bron en de foutcode, nooit een adres met een sleutel erin.
- Alleen lezen. Alleen aantallen opslaan: nooit namen, mailadressen of andere gegevens van kopers
  of abonnees. De Gumroad-productlijst en de Kit-teltellers geven geen kopers of abonnees terug;
  waar de Kit-API wel abonnees teruggeeft (terugval: tellen per pagina) tellen we alleen len().
- Zonder sleutel slaat een bron zichzelf over met een melding.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (Dortus scorebord; 1 keer per dag)"

# YouTube @Dortusapps: kanaal-id staat openbaar op de kanaalpagina (GEZIEN 18 nov, "externalId").
YOUTUBE_KANAAL = "UCTspMNCOwnBkGT2LZ7tB2dg"
YOUTUBE_NAAM = "YouTube @Dortusapps"

# Discord van Hats of the Fallen: de uitnodigingscode is openbaar bedoeld (komt op de Steampagina).
# De hoofdchat vult hem hier in (alleen de code, bijv. "abcDEF12"), of zet de GitHub-variabele
# HATS_DISCORD_INVITE. Leeg: dan probeert het script de code via de webhook en de widget van de server.
HATS_DISCORD_INVITE = ""
DISCORD_NAAM = "Hats of the Fallen"


def _get(url, koppen=None, json_=True, pogingen=3):
    """Geeft (inhoud, foutcode). Print nooit het adres (daar kan een sleutel in zitten)."""
    code = None
    for p in range(pogingen):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*", **(koppen or {})})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                body = r.read().decode("utf-8", "replace")
            return (json.loads(body) if json_ else body), None
        except urllib.error.HTTPError as e:
            code = e.code
            if code in (400, 401, 403, 404):
                break
            time.sleep(10 * (p + 1) if code == 429 else 3)
        except Exception as e:  # noqa: BLE001
            code = type(e).__name__
            time.sleep(3)
    return None, code


# ---------------------------------------------------------------- Gumroad

def gumroad(meet, noten):
    sleutel = os.environ.get("GUMROAD_ACCESS_TOKEN", "").strip()
    if not sleutel:
        noten.append("Gumroad: geen GUMROAD_ACCESS_TOKEN in de omgeving, overgeslagen.")
        meet("Gumroad (alle)", "Gumroad", "verkopen", None, "geen leessleutel in deze run")
        return
    d, code = _get("https://api.gumroad.com/v2/products", {"Authorization": f"Bearer {sleutel}"})
    if code == 401:  # de docs noemen access_token als parameter; het adres wordt nergens geprint
        d, code = _get("https://api.gumroad.com/v2/products?" + urllib.parse.urlencode({"access_token": sleutel}))
    if not isinstance(d, dict) or not d.get("success"):
        noten.append(f"Gumroad: productlijst niet leesbaar ({code}).")
        meet("Gumroad (alle)", "Gumroad", "verkopen", None, f"API niet leesbaar ({code})")
        return
    producten = [p for p in d.get("products", []) if not p.get("deleted")]
    if not producten:
        noten.append("Gumroad: geen producten in de lijst.")
    for p in producten:
        naam = (p.get("name") or "?").strip()
        stand = ("gepubliceerd" if p.get("published") else "niet gepubliceerd") + f", {p.get('formatted_price', '')}".rstrip(", ")
        meet(naam, "Gumroad", "verkopen", p.get("sales_count"), stand)
        cent = p.get("sales_usd_cents")
        meet(naam, "Gumroad", "omzet USD", None if cent is None else f"{int(cent) / 100:.2f}",
             "bruto, vóór kosten van Gumroad")
        for k in ("views_count", "views", "view_count"):  # staat niet in de API-docs; als hij er ooit is, meten we hem
            if isinstance(p.get(k), int):
                meet(naam, "Gumroad", "bezoekers", p[k], "uit de productlijst")
                break


# ---------------------------------------------------------------- Kit

def _kit_v4_totaal(pad, sleutel, sleutel_in_kop):
    """Aantal actieve abonnees achter een v4-lijst. Eerst include_total_count, anders tellen per pagina."""
    basis = f"https://api.kit.com/v4{pad}"
    d, code = _get(f"{basis}?per_page=1&include_total_count=true", sleutel_in_kop)
    if not isinstance(d, dict):
        return None, code
    tot = (d.get("pagination") or {}).get("total_count")
    if isinstance(tot, int):
        return tot, None
    # terugval: tellen, zonder iets te bewaren behalve het aantal
    n, na, rondes = 0, None, 0
    while rondes < 50:
        q = {"per_page": 1000}
        if na:
            q["after"] = na
        d, code = _get(f"{basis}?{urllib.parse.urlencode(q)}", sleutel_in_kop)
        if not isinstance(d, dict):
            return None, code
        n += len(d.get("subscribers") or [])
        pag = d.get("pagination") or {}
        if not pag.get("has_next_page"):
            return n, None
        na, rondes = pag.get("end_cursor"), rondes + 1
    return None, "te veel pagina's"


def kit(meet, noten):
    sleutel = os.environ.get("KIT_API_KEY", "").strip()
    if not sleutel:
        noten.append("Kit: geen KIT_API_KEY in de omgeving, overgeslagen.")
        meet("Kit (alle)", "Kit", "abonnees", None, "geen leessleutel in deze run")
        return
    kop = {"X-Kit-Api-Key": sleutel}
    tags, code = _get("https://api.kit.com/v4/tags?per_page=1000", kop)
    if isinstance(tags, dict):
        totaal, c = _kit_v4_totaal("/subscribers", sleutel, kop)
        meet("Kit (alle)", "Kit", "abonnees", totaal, "actief, alle tags samen" if totaal is not None else f"niet leesbaar ({c})")
        lijst = tags.get("tags") or []
        if not lijst:
            noten.append("Kit: nog geen tags aangemaakt, alleen het totaal gemeten.")
        for t in lijst:
            n, c = _kit_v4_totaal(f"/tags/{t.get('id')}/subscribers", sleutel, kop)
            meet(f"Kit tag {t.get('name', '?')}", "Kit", "abonnees", n, "actief" if n is not None else f"niet leesbaar ({c})")
        return
    if code != 401:
        noten.append(f"Kit: v4-API niet leesbaar ({code}).")
        meet("Kit (alle)", "Kit", "abonnees", None, f"API niet leesbaar ({code})")
        return
    # Oudere sleutel (v3 api_secret): die moet in het adres. Het adres wordt nergens geprint.
    q = urllib.parse.urlencode({"api_secret": sleutel})
    d, c = _get(f"https://api.convertkit.com/v3/subscribers?{q}")
    if not isinstance(d, dict):
        noten.append(f"Kit: sleutel werkt niet op v4 (401) en niet op v3 ({c}).")
        meet("Kit (alle)", "Kit", "abonnees", None, "sleutel geweigerd")
        return
    meet("Kit (alle)", "Kit", "abonnees", d.get("total_subscribers"), "actief, alle tags samen (API v3)")
    tags, c = _get(f"https://api.convertkit.com/v3/tags?{q}")
    for t in (tags or {}).get("tags", []) if isinstance(tags, dict) else []:
        s, c2 = _get(f"https://api.convertkit.com/v3/tags/{t.get('id')}/subscriptions?{q}")
        n = s.get("total_subscriptions") if isinstance(s, dict) else None
        meet(f"Kit tag {t.get('name', '?')}", "Kit", "abonnees", n, "API v3" if n is not None else f"niet leesbaar ({c2})")


# ---------------------------------------------------------------- Discord

def discord(meet, noten):
    code_ = (os.environ.get("HATS_DISCORD_INVITE") or HATS_DISCORD_INVITE).strip().rstrip("/").rsplit("/", 1)[-1]
    # Alleen de openbare uitnodigingscode; de webhook (kan posten) hoort hier niet (keuring R6, 19 nov).
    if not code_:
        meet(DISCORD_NAAM, "Discord", "leden", None, "uitnodigingscode ontbreekt (vraag staat bij de hoofdchat)")
        noten.append("Discord: geen uitnodigingscode. Zet de code in HATS_DISCORD_INVITE in scorebord_bronnen.py.")
        return
    if not re.fullmatch(r"[A-Za-z0-9-]{2,40}", code_):
        noten.append("Discord: uitnodigingscode heeft een vreemde vorm, overgeslagen.")
        return
    d, c = _get(f"https://discord.com/api/v9/invites/{code_}?with_counts=true")
    if not isinstance(d, dict) or "approximate_member_count" not in d:
        meet(DISCORD_NAAM, "Discord", "leden", None, f"uitnodiging niet leesbaar ({c}), misschien verlopen")
        return
    meet(DISCORD_NAAM, "Discord", "leden", d.get("approximate_member_count"), f"server {d.get('guild', {}).get('name', '?')}")
    meet(DISCORD_NAAM, "Discord", "online", d.get("approximate_presence_count"), "op het moment van meten")


# ---------------------------------------------------------------- YouTube

def youtube(meet, noten):
    xml, code = _get(f"https://www.youtube.com/feeds/videos.xml?channel_id={YOUTUBE_KANAAL}", json_=False)
    if not xml:
        meet(YOUTUBE_NAAM, "YouTube", "weergaven (RSS)", None, f"RSS niet leesbaar ({code})")
        return
    ns = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
          "m": "http://search.yahoo.com/mrss/"}
    try:
        boom = ET.fromstring(xml)
    except ET.ParseError:
        meet(YOUTUBE_NAAM, "YouTube", "weergaven (RSS)", None, "RSS niet te lezen als XML")
        return
    totaal, n = 0, 0
    for e in boom.findall("a:entry", ns):
        vid = e.findtext("yt:videoId", default="?", namespaces=ns)
        titel = (e.findtext("a:title", default="", namespaces=ns) or "").replace("|", "/")[:60]
        stat = e.find("m:group/m:community/m:statistics", ns)
        views = int(stat.get("views")) if stat is not None and str(stat.get("views", "")).isdigit() else None
        datum = (e.findtext("a:published", default="", namespaces=ns) or "")[:10]
        meet(YOUTUBE_NAAM, "YouTube", f"weergaven {vid}", views, f"{datum} {titel}".strip())
        totaal += views or 0
        n += 1
    meet(YOUTUBE_NAAM, "YouTube", "weergaven (RSS)", totaal if n else 0,
         f"{n} filmpjes in de RSS (alleen de nieuwste openbare, max 15)")
