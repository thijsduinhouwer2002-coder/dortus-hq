"""Blinde test: ons beeld tussen 3 concurrenten, zonder namen, beoordeeld door Gemini en ChatGPT.

Besluit Thijs 24 nov 2026 20:19. Per kandidaat-beeld van ons: 2 rondes met een andere volgorde,
elk model kiest welk product het als klant het eerst zou kopen. Geslaagd = bij elk model gemiddeld
plek 2 of beter. Sleutels komen uit GEMINI_API_KEY en OPENAI_API_KEY (GitHub-geheimen), nooit printen.

Gebruik: python3 blindtest.py sets/<naam>.json uitslag/<bestand>.md
"""
import base64, hashlib, io, json, os, random, sys, time, urllib.request, urllib.error

RONDES = 2
LETTERS = "ABCD"
GEMINI_MODELLEN = os.environ.get("GEMINI_MODELLEN", "gemini-2.5-pro,gemini-2.5-flash").split(",")
OPENAI_MODELLEN = os.environ.get("OPENAI_MODELLEN", "gpt-5,gpt-4.1,gpt-4o").split(",")

VRAAG = """{rol}

Below are four product images, labeled A, B, C and D. Judge ONLY from what you see.
Be honest and critical, not polite: you are spending your own money.
Which product would you click and buy first, second, third, fourth?

Answer with JSON only:
{{"ranking": ["?","?","?","?"],
  "reasons": {{"A": "one sentence", "B": "...", "C": "...", "D": "..."}},
  "improve": {{"A": "the one change that would most make you buy it", "B": "...", "C": "...", "D": "..."}}}}"""


def haal(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 dortus-blindtest"})
            return urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:  # netwerk hapert soms
            if i == tries - 1:
                raise RuntimeError(f"kon {url} niet ophalen: {e}")
            time.sleep(3)


def als_jpeg(data, breed=1024):
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert("RGB")
    if im.width > breed:
        im = im.resize((breed, round(im.height * breed / im.width)))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=88)
    return base64.b64encode(buf.getvalue()).decode()


def volgorde(items, zaad):
    rnd = random.Random(int(hashlib.sha256(zaad.encode()).hexdigest(), 16))
    lijst = list(items)
    rnd.shuffle(lijst)
    return lijst


def lees_antwoord(tekst):
    """Haalt de JSON uit een antwoord en controleert de ranglijst."""
    tekst = tekst.strip()
    if tekst.startswith("```"):
        tekst = tekst.strip("`")
        tekst = tekst[tekst.find("{"):]
    data = json.loads(tekst[tekst.find("{"): tekst.rfind("}") + 1])
    rang = [str(x).strip().upper()[:1] for x in data.get("ranking", [])]
    if sorted(rang) != list(LETTERS):
        raise ValueError(f"ongeldige ranglijst: {data.get('ranking')}")
    data["ranking"] = rang
    return data


def plek_van(rang, letter):
    return rang.index(letter) + 1


def post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json", **headers})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=180).read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read()[:300].decode(errors='replace')}")


def vraag_gemini(prompt, beelden, model):
    parts = [{"text": prompt}]
    for letter, b64 in beelden:
        parts += [{"text": f"Image {letter}:"}, {"inline_data": {"mime_type": "image/jpeg", "data": b64}}]
    r = post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
             {"contents": [{"parts": parts}], "generationConfig": {"responseMimeType": "application/json"}},
             {"x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    return r["candidates"][0]["content"]["parts"][0]["text"]


def vraag_openai(prompt, beelden, model):
    content = [{"type": "text", "text": prompt}]
    for letter, b64 in beelden:
        content += [{"type": "text", "text": f"Image {letter}:"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}]
    r = post("https://api.openai.com/v1/chat/completions",
             {"model": model, "messages": [{"role": "user", "content": content}], "response_format": {"type": "json_object"}},
             {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    return r["choices"][0]["message"]["content"]


def vraag(naam, modellen, functie, prompt, beelden, gekozen):
    """Probeert modellen op volgorde; onthoudt welk model werkte."""
    fouten = []
    for m in ([gekozen[naam]] if naam in gekozen else modellen):
        try:
            data = lees_antwoord(functie(prompt, beelden, m.strip()))
            gekozen[naam] = m.strip()
            return data
        except Exception as e:
            fouten.append(f"{m}: {e}")
    raise RuntimeError(f"{naam} gaf geen bruikbaar antwoord: " + " | ".join(fouten))


def main(setpad, uitpad):
    s = json.load(open(setpad))
    rechters = []
    if os.environ.get("GEMINI_API_KEY"):
        rechters.append(("Gemini", GEMINI_MODELLEN, vraag_gemini))
    if os.environ.get("OPENAI_API_KEY"):
        rechters.append(("ChatGPT", OPENAI_MODELLEN, vraag_openai))
    if not rechters:
        print("Geen sleutels (GEMINI_API_KEY, OPENAI_API_KEY): niets getest.")
        return 0
    prompt = VRAAG.format(rol=s["rol"])
    plaatjes = {i["naam"]: als_jpeg(haal(i["url"])) for i in s["ons"] + s["concurrenten"]}
    gekozen, regels, alles_goed = {}, [], True
    regels += [f"# Blinde test: {s['titel']}", "", f"Rol voor de rechters: {s['rol']}", "",
               "Concurrenten: " + ", ".join(f"[{c['naam']}]({c['url']})" for c in s["concurrenten"]), "",
               "Geslaagd = bij elke rechter gemiddeld plek 2 of beter (van 4), over "
               f"{RONDES} rondes met een andere volgorde.", ""]
    for kand in s["ons"]:
        plekken = {r[0]: [] for r in rechters}
        uitleg = []
        for ronde in range(RONDES):
            rij = volgorde([kand] + s["concurrenten"], f"{s['titel']}|{kand['naam']}|{ronde}")
            letter_van = {item["naam"]: LETTERS[i] for i, item in enumerate(rij)}
            beelden = [(LETTERS[i], plaatjes[item["naam"]]) for i, item in enumerate(rij)]
            ons = letter_van[kand["naam"]]
            for naam, modellen, functie in rechters:
                data = vraag(naam, modellen, functie, prompt, beelden, gekozen)
                plekken[naam].append(plek_van(data["ranking"], ons))
                winnaar = next(i["naam"] for i in rij if letter_van[i["naam"]] == data["ranking"][0])
                uitleg.append(f"- Ronde {ronde + 1}, {naam}: wij plek {plek_van(data['ranking'], ons)}, "
                              f"eerste keus {winnaar}. Over ons: {data.get('reasons', {}).get(ons, '?')} "
                              f"Beter maken: {data.get('improve', {}).get(ons, '?')}")
        gem = {n: sum(p) / len(p) for n, p in plekken.items()}
        goed = all(g <= 2 for g in gem.values())
        alles_goed &= goed
        regels += [f"## {kand['naam']}: {'GESLAAGD' if goed else 'NIET GESLAAGD'}", "",
                   f"Beeld: {kand['url']}", "",
                   "Gemiddelde plek: " + ", ".join(f"{n} {g:.1f}" for n, g in gem.items()), ""] + uitleg + [""]
    regels += ["Modellen: " + ", ".join(f"{n} = {m}" for n, m in gekozen.items()),
               "Alles is GEZIEN: letterlijke antwoorden van de modellen, ingekort tot één zin per punt."]
    os.makedirs(os.path.dirname(uitpad) or ".", exist_ok=True)
    open(uitpad, "w").write("\n".join(regels) + "\n")
    print("\n".join(regels))
    return 0 if alles_goed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
