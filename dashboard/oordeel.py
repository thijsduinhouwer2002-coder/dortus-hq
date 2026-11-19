"""Het nieuwste oordeel uit een keuringsbestand.

Een keuringsbestand kan meer keuringen bevatten: een herkeuring staat soms onderaan, soms bovenaan.
Daarom telt niet de plek in het bestand, maar wanneer de regel "Akkoord:" erin kwam (git blame).
Zijn twee regels even oud (zelfde commit) of is er geen git, dan beslist de kop erboven:
een kop met "herkeuring" gaat voor, dan een latere datum en tijd in de kop, dan de laatste in het bestand.
"""
import re

MAANDEN = {m: i + 1 for i, m in enumerate(["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"])}
AKKOORD = re.compile(r"^\W*akkoord\W*:", re.I)


def _kop_waarde(kop):
    """(herkeuring?, datum en tijd uit de kop) om gelijke regels te ordenen."""
    her = 1 if re.search(r"herkeuring", kop, re.I) else 0
    d = re.search(r"(\d{1,2}) (jan|feb|mrt|apr|mei|jun|jul|aug|sep|okt|nov|dec)\w* (\d{4})", kop, re.I)
    t = re.search(r"(\d{1,2})[:.](\d{2})", kop[d.end():] if d else kop)
    datum = (int(d.group(3)), MAANDEN[d.group(2).lower()], int(d.group(1))) if d else (0, 0, 0)
    tijd = (int(t.group(1)), int(t.group(2))) if t else (0, 0)
    return (her, datum, tijd)


def akkoord_regels(tekst):
    """Lijst van (regelnummer vanaf 1, regel, kop erboven) voor elke regel 'Akkoord:'."""
    uit, kop = [], ""
    for n, r in enumerate(tekst.splitlines(), 1):
        if r.startswith("#"):
            kop = r.lstrip("# ").strip()
        elif AKKOORD.match(r):
            uit.append((n, r, kop))
    return uit


def nieuwste(tekst, tijden=None):
    """De nieuwste (regel, kop) of None. tijden: {regelnummer: unix-tijd} uit git blame (mag leeg)."""
    regels = akkoord_regels(tekst)
    if not regels:
        return None
    tijden = tijden or {}
    beste = max(regels, key=lambda x: (tijden.get(x[0], 0), _kop_waarde(x[2]), x[0]))
    return beste[1], beste[2]


def blame_tijden(blame_porcelain):
    """{regelnummer: author-time} uit de uitvoer van git blame --line-porcelain."""
    tijden, regel = {}, None
    for r in blame_porcelain.splitlines():
        m = re.match(r"^[0-9a-f]{40} \d+ (\d+)", r)
        if m:
            regel = int(m.group(1))
        elif r.startswith("author-time ") and regel is not None:
            tijden[regel] = int(r.split()[1])
    return tijden
