"""Buitenblik: Gemini en ChatGPT als strenge buitenstaanders over hoe een product meer verkoopt.

Idee van Thijs (25 nov 2026): hij vroeg Google AI "hoe market ik dit", vroeg twee keer door ("nog meer,
maar alleen echte dingen") en vond zo twee gaten die wij misten. Dit script doet dat elke week vanzelf,
met onze echte pagina's erbij zodat de modellen niet hoeven te gokken, en met zoeken op internet aan.

python3 buitenblik.py <product.json> <uitslag.md>
product.json: naam, feiten (wat wij zeker weten), pagina's (url's die we met curl ophalen), doelgroep.
Uitslag: de letterlijke antwoorden. De hoofdmanager checkt elk punt met curl voor er een issue van komt.
"""
import html
import json
import os
import re
import sys
import urllib.request

GEMINI = os.environ.get("GEMINI_MODEL", "gemini-3.1-pro-preview")
OPENAI = os.environ.get("OPENAI_MODEL", "gpt-5")


def haal_tekst(url, maxlen=6000):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (buitenblik Dortus)"})
        ruw = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        return f"(kon {url} niet ophalen: {e})"
    ruw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", ruw)
    t = html.unescape(re.sub(r"<[^>]+>", " ", ruw))
    return re.sub(r"\s+", " ", t).strip()[:maxlen]


def post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", **headers})
    return json.loads(urllib.request.urlopen(req, timeout=300).read())


def gemini(beurten):
    """beurten: lijst teksten, om en om gebruiker en model. Met Google Search aan."""
    contents = [{"role": "user" if i % 2 == 0 else "model", "parts": [{"text": t}]} for i, t in enumerate(beurten)]
    r = post(f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI}:generateContent",
             {"contents": contents, "tools": [{"google_search": {}}]},
             {"x-goog-api-key": os.environ["GEMINI_API_KEY"].strip()})
    c = r["candidates"][0]
    tekst = "".join(p.get("text", "") for p in c["content"]["parts"])
    bronnen = [g["web"]["uri"] for g in c.get("groundingMetadata", {}).get("groundingChunks", []) if "web" in g]
    return tekst, bronnen


def openai(prompt, vorige=None):
    body = {"model": OPENAI, "input": prompt, "tools": [{"type": "web_search"}]}
    if vorige:
        body["previous_response_id"] = vorige
    r = post("https://api.openai.com/v1/responses", body,
             {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"].strip()})
    tekst, bronnen = "", []
    for item in r.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content", []):
                if c.get("type") == "output_text":
                    tekst += c.get("text", "")
                    bronnen += [a.get("url") for a in c.get("annotations", []) if a.get("url")]
    return tekst, bronnen, r.get("id")


VRAAG1 = """You are a blunt, experienced advisor for indie sellers of Blender add-ons (Superhive, Gumroad, extensions.blender.org).
Do not be nice; do not agree to please. Search the web to see what the best sellers in this niche actually do.

PRODUCT: {naam}
AUDIENCE: {doelgroep}
FACTS WE KNOW FOR SURE (trust these over anything you find):
{feiten}

OUR LIVE PAGES (plain text, fetched just now):
{paginas}

Question: what are the 7 changes that would bring the most extra SALES within 2 weeks?
For each: (1) exactly what to change or do, (2) why, with evidence: a quote from our pages above or a link you found,
(3) expected effect (say if it is a guess), (4) effort: small, medium or large.
Rules: no generic marketing tips that would fit any product; nothing we already do according to the pages above
(quote it if you think we do it badly); say "unsure" when you are. Number the points."""

VRAAG2 = """Now be critical of your own list. Which points are generic, wrong given our pages, or things we already do?
Drop them and say why in one line each. Then give up to 4 new points that are specific to this product and this
audience (people who 3D print figures), with the same format and evidence. End with the single change you would do first."""


def main(prodpad, uitpad):
    p = json.load(open(prodpad, encoding="utf-8"))
    paginas = "\n\n".join(f"--- {u} ---\n{haal_tekst(u)}" for u in p["paginas"])
    v1 = VRAAG1.format(naam=p["naam"], doelgroep=p["doelgroep"], feiten="\n".join("- " + f for f in p["feiten"]),
                       paginas=paginas)
    regels = [f"# Buitenblik: {p['naam']}", "",
              "Letterlijke antwoorden van Gemini en ChatGPT (met zoeken op internet), twee beurten zoals Thijs deed: "
              "eerst de vraag, dan doorvragen naar alleen echte punten. NIET GECONTROLEERD: de hoofdmanager checkt elk punt "
              "met curl tegen onze pagina's voordat er een issue van komt.", ""]
    if os.environ.get("GEMINI_API_KEY", "").strip():
        try:
            a1, b1 = gemini([v1])
            a2, b2 = gemini([v1, a1, VRAAG2])
            regels += [f"## Gemini ({GEMINI})", "", "### Beurt 1", "", a1, "", "### Beurt 2 (doorgevraagd)", "", a2, "",
                       "Bronnen: " + ", ".join(sorted(set(b1 + b2))[:20]), ""]
        except Exception as e:  # noqa: BLE001
            regels += [f"## Gemini: fout {e}", ""]
    if os.environ.get("OPENAI_API_KEY", "").strip():
        try:
            a1, b1, rid = openai(v1)
            a2, b2, _ = openai(VRAAG2, rid)
            regels += [f"## ChatGPT ({OPENAI})", "", "### Beurt 1", "", a1, "", "### Beurt 2 (doorgevraagd)", "", a2, "",
                       "Bronnen: " + ", ".join(sorted(set(b1 + b2))[:20]), ""]
        except Exception as e:  # noqa: BLE001
            regels += [f"## ChatGPT: fout {e}", ""]
    os.makedirs(os.path.dirname(uitpad), exist_ok=True)
    open(uitpad, "w", encoding="utf-8").write("\n".join(regels) + "\n")
    print(uitpad)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
