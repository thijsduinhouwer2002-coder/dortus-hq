"""Vaste regels van de repo-radar: zoektermen, wat we uit een README halen, wat ruis is en de score.

Alles hier is zonder internet, zodat test_radar.py het kan testen. radar.py doet het ophalen.
"""
import re

# (zoekterm, ook in de README zoeken?) Algemene woorden zoals "startup" of "pricing" alleen in naam,
# beschrijving en topics: in een README staan ze ook in zinnen als "runs on startup" (veel ruis).
ZOEKTERMEN = [
    ("saas", False),
    ('"side project"', True),
    ('"indie hacker"', True),
    ("indiehacker", False),
    ("monetize", True),
    ("monetization", False),
    ("pricing", False),
    ("subscription", False),
    ("mrr", False),
    ("revenue", False),
    ("gumroad", True),
    ("stripe", False),
    ('"lemon squeezy"', True),
    ("lemonsqueezy", True),
    ('"paddle billing"', True),
    ('"business plan"', True),
    ('"go-to-market"', True),
    ('"app idea"', True),
    ("startup", False),
    ('"landing page"', False),
    ("waitlist", True),
    ('"pro version"', True),
    ("freemium", True),
    ('"premium features"', True),
]

# Platformen die wij kennen (CLAUDE.md, opdracht Thijs 19 nov). Eigen winkel = 2 punten, web = 1 punt
# (web is breed en vol; in een winkel van ons hebben we al een account en een route naar kopers).
PLATFORMEN = [
    ("Blender", 2, r"blender add-?on|blender plugin|\bbpy\b|blender extension"),
    ("Obsidian", 2, r"obsidian plugin|obsidian\.md|obsidian community"),
    ("JetBrains", 2, r"jetbrains plugin|intellij (idea )?plugin|jetbrains marketplace"),
    ("Garmin", 2, r"\bgarmin\b|connect ?iq|monkey ?c\b"),
    ("Steam", 2, r"\bon steam\b|steam (page|store|game|deck)|steamworks|wishlist on steam|\bgodot\b"),
    ("Chrome", 2, r"chrome[ -]extension|browser[ -]extension|manifest v3|chrome web store"),
    ("web", 1, r"\bsaas\b|web ?app|\bnext\.?js\b|\bnuxt\b|\bsvelte ?kit\b|landing page|\bsupabase\b|\bvercel\b"),
    ("Gumroad", 2, r"\bgumroad\b"),  # laatst: "verkocht via Gumroad" zegt niets over waar het draait
]
# Platformen die wij (nog) niet bedienen: wel noemen, geen punten.
ANDERE_PLATFORMEN = [
    ("iOS", r"\bios\b|\bswift ?ui\b|app store"),
    ("Android", r"\bandroid\b|google play|\bkotlin\b"),
    ("Shopify", r"\bshopify\b"),
    ("WordPress", r"\bwordpress\b|\bwoocommerce\b"),
    ("Telegram", r"\btelegram\b"),
    ("Discord", r"\bdiscord bot\b"),
    ("VS Code", r"vs ?code extension|visual studio code"),
]

# Verdienmodel: label in gewone woorden, patroon.
VERDIENMODELLEN = [
    ("abonnement", r"subscription|per month|/ ?mo(nth)?\b|monthly plan|\bmrr\b|recurring|per user per|annual plan|/ ?year\b"),
    ("eenmalige koop", r"one[- ]time (payment|purchase|fee)|lifetime (deal|access|license)|pay once|\bbuy (it )?now\b"),
    ("gratis met betaalde pro-versie", r"freemium|free tier|pro version|premium (version|features|plan|tier)|upgrade to pro|\bpro plan\b|paid plan"),
    ("per gebruik betalen", r"pay[- ]as[- ]you[- ]go|credits? (system|pack)|usage[- ]based|per (request|credit|generation)"),
    ("commissie of transactiekosten", r"commission|transaction fee|platform fee|take rate|marketplace fee"),
    ("advertenties", r"\badsense\b|advertis(ing|ement)s? revenue|ad[- ]supported|display ads"),
    ("affiliate", r"\baffiliate\b"),
    ("donaties", r"buy ?me ?a ?coffee|ko-fi\.com|github sponsors|patreon|donat(e|ion)"),
]
STERKE_MODELLEN = {"abonnement", "eenmalige koop", "gratis met betaalde pro-versie", "per gebruik betalen",
                   "commissie of transactiekosten"}

# Betaalpagina's en wachtlijsten (tractie: iemand kan al betalen of zich aanmelden).
BETAALLINKS = [
    ("Stripe", r"buy\.stripe\.com|checkout\.stripe\.com|stripe\.com/(payment|checkout)"),
    ("Gumroad", r"gumroad\.com/l/|\w+\.gumroad\.com"),
    ("Lemon Squeezy", r"lemonsqueezy\.com/(checkout|buy)|\w+\.lemonsqueezy\.com"),
    ("Paddle", r"paddle\.com/checkout|buy\.paddle\.com|pay\.paddle\.io"),
    ("Polar", r"polar\.sh/[\w-]+"),
    ("Ko-fi of Buy Me a Coffee", r"ko-fi\.com/|buymeacoffee\.com/"),
]
WACHTLIJST = r"join (the|our) wait ?list|wait ?list|getwaitlist\.com|launchlist|tally\.so|typeform\.com|early access sign ?up"

# Voor wie: herkende groep in de tekst, in gewone woorden.
DOELGROEPEN = [
    ("ontwikkelaars", r"\bdevelopers?\b|\bdevs\b|\bprogrammers?\b|\bengineers?\b"),
    ("freelancers", r"\bfreelancers?\b"),
    ("kleine bedrijven", r"small business(es)?|\bsmbs?\b|\bsmes?\b|local business(es)?"),
    ("makers en creators", r"\bcreators?\b|influencers?|youtubers?|streamers?"),
    ("studenten", r"\bstudents?\b"),
    ("docenten", r"\bteachers?\b|\btutors?\b|educators?"),
    ("webwinkels", r"e-?commerce|online stores?|shopify (merchants|stores)|\bsellers?\b"),
    ("marketeers", r"\bmarketers?\b|marketing teams?"),
    ("ontwerpers", r"\bdesigners?\b"),
    ("schrijvers", r"\bwriters?\b|\bauthors?\b|bloggers?"),
    ("gamers", r"\bgamers?\b|\bgaming\b"),
    ("bureaus", r"\bagenc(y|ies)\b"),
    ("startups", r"\bstartups?\b|founders?"),
    ("zorg", r"\bclinics?\b|\bdoctors?\b|\bpatients?\b|healthcare"),
    ("vastgoed", r"real estate|landlords?|property managers?"),
    ("restaurants", r"\brestaurants?\b|\bcafes?\b"),
    ("recruiters", r"recruiters?|hiring managers?|job seekers?"),
    ("teams", r"\bteams\b"),
]

# Ruis: (reden in gewone woorden, patroon). Volgorde = welke reden telt als er meer passen.
RUIS_NAAM = [  # op naam, beschrijving en topics
    ("sjabloon of boilerplate", r"\btemplates?\b|boilerplate|starter(-| )?kit|\bstarter\b|scaffold|\bsaas[- ]kit\b"),
    ("huiswerk of oefening", r"homework|assignment|bootcamp|\bcs50\b|tutorial|\bexercises?\b|learning project|\bclone\b|final[- ]project|\blab\d+\b|\buniversity\b"),
    ("crypto-pump", r"memecoin|meme coin|pump\.?fun|airdrop|presale|token sale|\bico\b|sniper|rug ?pull|\b100x\b|to the moon"),
    ("spam of illegaal", r"\bcrack(ed)?\b|keygen|mod apk|free download|\bhack(s|ed)?\b.*\bfree\b|cheat engine|serial key|patched build|\bnulled\b|premium unlocked|unlocked premium|activation bypass|license bypass|game cheats?|\bcheat (menu|tool)s?\b|aimbot|wallhack|game trainer|\w+ trainer \+\d+"),
    ("lijst, geen product", r"^awesome[- ]|\bawesome list\b|curated list"),
]
RUIS_README = [  # op de README zelf
    ("spam of illegaal", r"patched build|\bnulled\b|premium unlocked|unlocked premium|activation bypass|license bypass|\bkeygen\b|cracked version"),
    ("sjabloon of boilerplate", r"use this template|this (is a )?(template|boilerplate)|starter (kit|template)|boilerplate for|clone this (repo|template) to start"),
    ("huiswerk of oefening", r"\bhomework\b|\bassignment\b|course project|for learning purposes|learning project|practice project|bootcamp|\bcs50\b|as part of (a|the|my) (course|class|program)|university project|school project|this tutorial"),
    ("crypto-pump", r"memecoin|meme coin|pump\.fun|presale|airdrop|token launch|sniper bot|\b100x\b"),
]

# Kopjes die laten zien dat het plan is uitgeschreven (niet alleen code).
PLANKOPPEN = r"^#{1,4}\s*(?:the )?(problem|solution|target (audience|users|market|customers)|who is (it|this) for|business model|monetization|revenue model|go[- ]to[- ]market|market|competitors|competition|roadmap|why now|value proposition|mvp)\b"

GELDWOORDEN = r"pricing|\bprice\b|\bpaid\b|\bpay\b|revenue|monetiz|subscription|\bplans?\b|checkout|\bstripe\b|\bbilling\b|customers?|\bsell\b|\bsales\b"

PRIJS = re.compile(
    r"(?:[$€£]\s?\d{1,4}(?:[.,]\d{1,2})?(?![\d.,]*\d)|\d{1,4}(?:[.,]\d{1,2})?\s?(?:usd|eur|euro|dollars?)\b)"
    r"(?:\s?(?:/|per|a)\s?(?:mo(?:nth)?|maand|yr|year|jaar|user|seat|week|lifetime)\b|\s(?:lifetime|one[- ]time)\b)?",
    re.I,
)
EENHEID = [(r"mo(nth)?|maand", "/maand"), (r"yr|year|jaar", "/jaar"), (r"user|seat", "/gebruiker"),
           (r"week", "/week"), (r"lifetime|one[- ]time", " eenmalig")]

MAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
TELEFOON = re.compile(r"\+?\d[\d\s().-]{8,}\d")
URL = re.compile(r"https?://\S+|www\.\S+")


def _zoek(patroon, tekst):
    return re.search(patroon, tekst, re.I | re.M) is not None


def schoon(tekst, maxlen=160):
    """Eén regel platte tekst: geen markdown, links, mailadressen of telefoonnummers; geen gedachtestreepjes."""
    t = re.sub(r"<[^>]+>", " ", tekst or "")
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)          # plaatjes
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)        # links: alleen de tekst
    t = MAIL.sub("[mail]", t)
    t = URL.sub("", t)
    t = TELEFOON.sub("", t)
    t = re.sub(r"[`*_#>|]+", " ", t)
    t = t.replace("\u2014", ",").replace("\u2013", "-")
    t = re.sub(r"\s+", " ", t).strip(" -:,")
    if len(t) > maxlen:
        t = t[: maxlen - 3].rsplit(" ", 1)[0] + "..."
    return t


def proza(readme):
    """De lopende tekst van een README: zonder codeblokken, koppen, tabellen, plaatjes en badges."""
    t = re.sub(r"```.*?```", " ", readme or "", flags=re.S)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    regels = []
    for r in t.splitlines():
        s = r.strip()
        if not s or s.startswith(("#", "|", "    ", "\t", "![", "[![", "<img", "<p align", "$ ", "npm ", "pip ")):
            continue
        regels.append(s)
    return "\n".join(regels)


def eerste_alinea(readme):
    for alinea in re.split(r"\n\s*\n", proza(readme)):
        s = schoon(alinea, 400)
        if len(s.split()) >= 6:
            return s
    return ""


def prijzen(tekst):
    gevonden = []
    for m in PRIJS.finditer(tekst):
        p = m.group(0).strip()
        bedrag = re.search(r"\d+(?:[.,]\d+)?", p).group(0)
        if float(bedrag.replace(",", ".")) < 0.99:  # gratis of centbedragen per API-aanroep: geen productprijs
            continue
        munt = "$" if ("$" in p or re.search(r"usd|dollar", p, re.I)) else "€" if re.search(r"€|eur", p, re.I) else "£"
        eenheid = ""
        staart = p[p.find(bedrag) + len(bedrag):]
        for pat, naam in EENHEID:
            if re.search(r"(/|per|a|\s)\s?(" + pat + r")\b", staart, re.I):
                eenheid = naam
                break
        netjes = f"{munt}{bedrag}{eenheid}"
        if netjes not in gevonden:
            gevonden.append(netjes)
        if len(gevonden) == 3:
            break
    return gevonden


def labels(lijst, tekst, maxn=3):
    uit = []
    for item in lijst:
        if _zoek(item[-1], tekst) and item[0] not in uit:
            uit.append(item[0])
        if len(uit) == maxn:
            break
    return uit


def ruis_op_naam(repo):
    """Reden om een repo al vóór het lezen van de README eruit te gooien, of None."""
    if repo.get("fork"):
        return "fork"
    if repo.get("is_template"):
        return "sjabloon of boilerplate"
    if repo.get("archived"):
        return "gearchiveerd"
    tekst = " ".join([repo.get("name", ""), repo.get("description") or "", " ".join(repo.get("topics") or [])])
    tekst = tekst.replace("-", " ").replace("_", " ") + " " + repo.get("name", "")
    for reden, pat in RUIS_NAAM:
        if _zoek(pat, tekst):
            return reden
    return None


def lees_plan(repo, readme):
    """Haal het plan uit naam, beschrijving, topics en README. Geeft een dict met velden in gewone woorden.

    Platform en doelgroep alleen uit de kop en het begin van de README (verderop staan lijsten met koppelingen
    die anders alles laten lijken op een Blender- of Garmin-project); verdienmodel, prijs en betaallinks uit
    de hele README (de prijzen staan vaak onderaan).
    """
    beschrijving = repo.get("description") or ""
    topics = " ".join(repo.get("topics") or [])
    kop = " ".join([repo.get("name", "").replace("-", " "), beschrijving, topics])
    begin = kop + "\n" + (readme or "")[:3000]
    heel = kop + "\n" + (readme or "")
    homepage = (repo.get("homepage") or "").strip()
    return {
        "naam": repo["full_name"],
        "link": repo["html_url"],
        "wat": schoon(beschrijving) if len(beschrijving.strip()) >= 15 else schoon(eerste_alinea(readme)),
        "voor_wie": labels(DOELGROEPEN, begin, 2),
        "verdienmodel": labels(VERDIENMODELLEN, heel, 2),
        "prijs": prijzen(heel),
        "platform": labels(PLATFORMEN, begin, 2),
        "ander_platform": labels(ANDERE_PLATFORMEN, begin, 2),
        "betaallinks": labels(BETAALLINKS, readme or "", 3),
        "wachtlijst": _zoek(WACHTLIJST, heel),
        "prijskop": _zoek(r"^#{1,4}\s*(pricing|plans|prijzen|tarieven)\b", readme or ""),
        "plankoppen": len(set(m.group(1).lower() for m in re.finditer(PLANKOPPEN, readme or "", re.I | re.M))),
        "geldwoorden": len(set(m.group(0).lower() for m in re.finditer(GELDWOORDEN, heel, re.I))),
        "site": bool(homepage) and "github.com" not in homepage,  # alleen ja/nee, de link zelf bewaren we niet
        "sterren": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "aangemaakt": (repo.get("created_at") or "")[:10],
        "laatste_push": (repo.get("pushed_at") or "")[:10],
        "taal": repo.get("language") or "",
    }


def spamnetwerk(repos, min_groep=3):
    """Namen van repo's die bij een kopie-netwerk horen: dezelfde beschrijving bij 3+ repo's van verschillende
    eigenaren, of 5+ eigenaren waarvan de naam met dezelfde 7 tekens begint (zoals apimart1, apimart2, ...)."""
    per_tekst, per_begin = {}, {}
    for r in repos:
        eigenaar = r["full_name"].split("/")[0].lower()
        tekst = re.sub(r"\W+", " ", (r.get("description") or "").lower()).strip()[:80]
        if len(tekst) >= 25:
            per_tekst.setdefault(tekst, set()).add(r["full_name"])
        if len(eigenaar) >= 8:
            per_begin.setdefault(eigenaar[:7], {}).setdefault(eigenaar, set()).add(r["full_name"])
    spam = set()
    for namen in per_tekst.values():
        if len({n.split("/")[0] for n in namen}) >= min_groep:
            spam |= namen
    for eigenaars in per_begin.values():
        if len(eigenaars) >= 5:
            for namen in eigenaars.values():
                spam |= namen
    return spam


def ruis_op_readme(plan, readme):
    """Reden om een repo na het lezen eruit te gooien, of None."""
    if readme is None:
        return "geen README"
    p = proza(readme)
    woorden = len(re.findall(r"[A-Za-z\u00C0-\u024F]{2,}", p))
    if len(readme.strip()) < 200:
        return "lege README"
    for reden, pat in RUIS_README:
        if _zoek(pat, readme[:6000]):
            return reden
    if woorden < 40:
        # veel tekst maar weinig lopende zinnen: codeblokken, commando's of tabellen zonder uitleg
        heeft_code = "```" in readme or len(readme.strip()) - len(p) > 300
        return "alleen code, geen uitleg" if heeft_code else "lege README"
    if not plan["verdienmodel"] and not plan["prijs"] and not plan["betaallinks"] and plan["geldwoorden"] < 2:
        return "geen verdienplan in de tekst"
    return None


def score(plan):
    """Voorselectie 0 tot 10 met vaste regels. Geeft (score, uitleg)."""
    punten = []
    sterk = [m for m in plan["verdienmodel"] if m in STERKE_MODELLEN]
    if sterk:
        punten.append((2, "verdienmodel"))
    elif plan["verdienmodel"]:
        punten.append((1, "zwak verdienmodel"))
    if plan["prijskop"]:
        punten.append((1, "kopje prijzen"))
    if plan["plankoppen"] >= 2:
        punten.append((1, "plan uitgeschreven"))
    if plan["prijs"]:
        punten.append((2, "prijs"))
    plat = max([p[1] for p in PLATFORMEN if p[0] in plan["platform"]], default=0)
    if plat:
        punten.append((plat, "platform van ons" if plat == 2 else "web"))
    if plan["sterren"] >= 50:
        punten.append((2, "50+ sterren"))
    elif plan["sterren"] >= 10:
        punten.append((1, "10+ sterren"))
    if plan["betaallinks"] or plan["wachtlijst"]:
        punten.append((1, "betaalpagina of wachtlijst"))
    if plan["site"]:
        punten.append((1, "eigen site"))
    totaal = min(10, sum(p[0] for p in punten))
    return totaal, ", ".join(f"{u} +{p}" for p, u in punten)
