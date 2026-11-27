"""Kijkt na of de hulppagina dortus.com/click-cuts/ dezelfde gekeurde zinnen heeft als winkel/docs.md en winkel/faq.md.

Gebruik: python3 controleer_hulppagina.py <pad naar click-cuts/index.html>
Elke zin (gesplitst op . ? !) uit de codeblokken van docs.md en faq.md moet in de paginatekst staan.
Alleen de koppen van de Docs-tab en de regels die naar "the store" of "the FAQ" wijzen mogen anders.
"""
import html, re, sys
from pathlib import Path

HIER = Path(__file__).parent


def blok(pad):
    t = (HIER / pad).read_text(encoding="utf-8")
    return re.search(r"```\n(.*?)```", t, re.S).group(1)


def normaal(s):
    s = html.unescape(s).replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def pagina_tekst(pad):
    t = Path(pad).read_text(encoding="utf-8")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = normaal(t)
    return re.sub(r"\s+([.,:;?!)])(?=\s|$)", r"\1", t)


def zinnen(tekst):
    uit = []
    for regel in tekst.splitlines():
        regel = regel.strip()
        if not regel:
            continue
        regel = re.sub(r"^\d+ (Printer|Cuts|Joints and numbers|Check and export): ", "", regel)
        regel = re.sub(r"^\d+\. ", "", regel)
        for z in re.split(r"(?<=[.?!])\s+", regel):
            z = normaal(z)
            if len(z) > 3:
                uit.append(z)
    return uit


def main():
    pagina = pagina_tekst(sys.argv[1])
    toegestaan = {"See the FAQ.", "Getting started", "Your first split:", "Print the fit test first",
                  "Magnets instead of pins", "Choose where it cuts: Free cut", "Choose where it cuts: Draw cut", "Lay parts flat",
                  "The panel, step by step", "Big models", "Support"}
    mist = []
    for naam in ("docs.md", "faq.md"):
        for z in zinnen(blok(naam)):
            if z in toegestaan:
                continue
            # de pagina zet een kop of label los voor de zin; vergelijk dan het deel na de dubbele punt
            stuk = z.split(": ", 1)[1] if z.split(": ", 1)[0] in ("Install", "Open the panel", "Where the files go", "Your original model is kept", "Clearance with magnets", "Gluing the magnets") else z
            if stuk not in pagina and stuk[:1].upper() + stuk[1:] not in pagina:
                mist.append((naam, z))
    for naam, z in mist:
        print(f"MIST ({naam}): {z}")
    print("OK" if not mist else f"{len(mist)} zinnen missen")
    sys.exit(1 if mist else 0)


main()
