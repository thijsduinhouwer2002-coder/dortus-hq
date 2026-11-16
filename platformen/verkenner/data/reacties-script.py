#!/usr/bin/env python3
"""Reacties op onze geplaatste berichten bijhouden (Vera, 16 nov 2026).

Leest platformen/verkenner/data/geplaatst.csv (een regel per geplaatst bericht)
en meet per bericht wat openbaar te zien is, zonder inlog:
- Discourse-fora (forum.obsidian.md, blenderartists.org, platform.jetbrains.com, devtalk.blender.org):
  views, antwoorden, likes via <draad>.json
- Garmin-forum (forums.garmin.com): views, antwoorden en volgers uit de pagina
- Hacker News: punten en reacties via de open Algolia-API
- Reddit: niet leesbaar met curl (403, niet omzeilen). De hoofdchat vult de kolom
  "hand" in geplaatst.csv zelf in (upvotes, reacties, zichtbaar uitgelogd ja/nee).
Daarnaast de downloads van het product uit organisatie/scorebord-data.csv:
de laatste meting op of voor de plaatsdatum en de nieuwste.

Gebruik (vanuit de hoofdmap van de repo):
    python3 -I platformen/verkenner/data/reacties-script.py
Schrijft platformen/verkenner/verspreiden-reacties.md en vult
platformen/verkenner/data/reacties-geschiedenis.csv aan. 1 verzoek per 2 s.
"""
import csv, datetime, json, os, re, subprocess, sys, time

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
GEPLAATST = os.path.join(HIER, "geplaatst.csv")
GESCH = os.path.join(HIER, "reacties-geschiedenis.csv")
UIT = os.path.join(REPO, "platformen", "verkenner", "verspreiden-reacties.md")
SCORE = os.path.join(REPO, "organisatie", "scorebord-data.csv")
DISCOURSE = ("forum.obsidian.md", "blenderartists.org", "platform.jetbrains.com", "devtalk.blender.org")


def curl(url):
    r = subprocess.run(["curl", "-sL", "-m", "30", "-A", "Mozilla/5.0", url], capture_output=True, text=True)
    time.sleep(2)
    return r.stdout


def meet(url):
    """Geeft (views, antwoorden, likes_of_punten, opmerking)."""
    host = re.sub(r"^https?://", "", url).split("/")[0]
    try:
        if host in DISCOURSE:
            m = re.search(r"/t/(?:[^/]+/)?(\d+)", url)
            d = json.loads(curl(f"https://{host}/t/{m.group(1)}.json"))
            return d.get("views"), d.get("posts_count", 1) - 1, d.get("like_count"), ""
        if host == "forums.garmin.com":
            t = curl(url)
            v = re.search(r"([\d,]+) views", t)
            a = re.search(r"([\d,]+) repl(?:y|ies)", t)
            s = re.search(r"([\d,]+) subscribers", t)
            f = lambda x: int(x.group(1).replace(",", "")) if x else None
            return f(v), f(a), None, f"volgers {f(s)}" if s else ""
        if host == "news.ycombinator.com":
            i = re.search(r"id=(\d+)", url).group(1)
            d = json.loads(curl(f"https://hn.algolia.com/api/v1/items/{i}"))
            n = sum(1 for _ in _kinderen(d)) - 1
            return None, n, d.get("points"), "punten"
        if "reddit.com" in host:
            return None, None, None, "Reddit niet leesbaar met curl: zie kolom hand"
        return None, None, None, "onbekende plek, met de hand meten"
    except Exception as e:  # een kapotte bron mag de rest niet stoppen
        return None, None, None, f"fout bij lezen ({type(e).__name__})"


def _kinderen(d):
    yield d
    for k in d.get("children") or []:
        yield from _kinderen(k)


def downloads(product):
    """[(datum, waarde)] voor downloads van dit product, oud naar nieuw."""
    if not os.path.exists(SCORE):
        return []
    rij = [(r["datum"], r["waarde"]) for r in csv.DictReader(open(SCORE))
           if r["product"] == product and r["maat"] == "downloads"]
    return sorted(rij)


def main():
    if not os.path.exists(GEPLAATST):
        sys.exit("geplaatst.csv ontbreekt")
    nu = datetime.datetime.now(datetime.timezone.utc)
    posts = list(csv.DictReader(open(GEPLAATST)))
    regels, gesch = [], []
    for p in posts:
        v, a, l, opm = meet(p["url"])
        dl = downloads(p["product"])
        voor = [w for d, w in dl if d <= p["geplaatst_utc"][:10]]
        dl_txt = f"{voor[-1] if voor else '?'} naar {dl[-1][1] if dl else '?'}"
        dagen = (nu - datetime.datetime.fromisoformat(p["geplaatst_utc"].replace("Z", "+00:00"))).days
        s = lambda x: "" if x is None else str(x)
        regels.append(f"| {p['product']} | {p['plek']} | {p['geplaatst_utc'][:10]} ({dagen} d) | {s(v)} | {s(a)} | {s(l)} | {p.get('hand', '')} | {dl_txt} | {opm} |")
        gesch.append([nu.strftime("%Y-%m-%d %H:%M"), p["product"], p["plek"], p["url"], s(v), s(a), s(l)])
    nieuw = not os.path.exists(GESCH)
    with open(GESCH, "a", newline="") as f:
        w = csv.writer(f)
        if nieuw:
            w.writerow(["gemeten_utc", "product", "plek", "url", "views", "antwoorden", "likes_of_punten"])
        w.writerows(gesch)
    kop = (f"# Reacties op onze berichten\n\nGemeten op {nu:%Y-%m-%d %H:%M} UTC met "
           "`platformen/verkenner/data/reacties-script.py` (GEZIEN, openbaar, zonder inlog). "
           "Lijst van berichten: `platformen/verkenner/data/geplaatst.csv`; geschiedenis: "
           "`data/reacties-geschiedenis.csv`. Wat normaal is per plek: `verspreiden-2026-11.md`.\n\n"
           "| Product | Plek | Geplaatst | Views | Antwoorden | Likes of punten | Hand (Reddit) | Downloads (bij plaatsen naar nu) | Opmerking |\n"
           "|---|---|---|---|---|---|---|---|---|\n")
    open(UIT, "w").write(kop + "\n".join(regels) + "\n")
    print("\n".join(regels))


if __name__ == "__main__":
    main()
