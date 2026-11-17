"""Draait met: python3 e2e/toets_zips.py <gratis zip> <betaalde zip>   (geen Blender nodig)
Twee builds uit één bron (ontwerp betaald v1.1, eis 7): de gratis zip bevat niets uit betaald/ en
noemt de betaalde versie nergens (hele woorden, zodat "Properties" niet telt); de gratis zip is precies
de map click_joints/ zonder betaald/ en __pycache__ en gelijk aan een vaste sha256-lijst van de gekeurde stand;
de betaalde zip heeft betaald/ en de registratie."""
import hashlib
import os
import re
import sys
import zipfile

gratis, betaald = sys.argv[1], sys.argv[2]
hier = os.path.dirname(os.path.abspath(__file__))
bron = os.path.join(hier, "..", "click_joints")
fout = 0


def stap(naam, ok, extra=""):
    global fout
    print(f"[cj-zips] {'OK' if ok else 'FOUT'} {naam} {extra}".rstrip())
    fout += 0 if ok else 1


zg = zipfile.ZipFile(gratis)
namen = sorted(n for n in zg.namelist() if not n.endswith("/"))
stap("gratis zip zonder betaald/", not any(n.startswith("betaald/") for n in namen))
woorden = re.compile(r"\b(hinge|pro|superhive|betaald)\b", re.I)
# Zelftoets van de regex: losse woorden tellen, delen van langere woorden niet.
moet = ["Click Joints Pro", "Pro.", "(Pro)", "'Pro'", "Get Pro now", "Hinge joint", "on Superhive", "PRO", "HINGE"]
niet = ["Properties", "Project", "bpy.props", "Prothese", "Hinged", "Hinges", "ProFile", "Pro_mode", "superhives"]
stap("regex vangt het hele woord", all(woorden.search(z) for z in moet), str([z for z in moet if not woorden.search(z)]))
stap("regex negeert delen van woorden", not any(woorden.search(z) for z in niet),
     str([z for z in niet if woorden.search(z)]))
treffers = []
for n in namen:
    tekst = zg.read(n).decode("utf-8", "replace")
    treffers += [f"{n}: {m.group(0)}" for m in woorden.finditer(tekst)]
stap("gratis code noemt de betaalde versie niet", not treffers, "; ".join(treffers[:5]))

verwacht = []
for wortel, mappen, bestanden in os.walk(bron):
    mappen[:] = [m for m in mappen if m not in ("__pycache__", "betaald")] if wortel == bron else \
        [m for m in mappen if m != "__pycache__"]
    for b in bestanden:
        verwacht.append(os.path.relpath(os.path.join(wortel, b), bron).replace(os.sep, "/"))
stap("gratis zip is precies de bronmap", namen == sorted(verwacht), f"{len(namen)} bestanden")
for n in namen:
    with open(os.path.join(bron, n), "rb") as f:
        if f.read() != zg.read(n):
            stap(f"gratis zip gelijk aan bron: {n}", False)

# Controleur eis 6: het gratis deel is gekeurd op 014172e; elke verandering moet opvallen (lijst dan bewust bijwerken).
# Bewust bijgewerkt 16 nov (Bram): 0.1.1, een_lid.py nieuw, gewricht.py en manifest veranderd (kniefout).
# Opnieuw 16 nov ±02:20 (Bram): een_lid.py ronde 2 (H = omhulsel rond het vlak plus het lid zelf; Meshy man_backpack).
# Opnieuw 16 nov ±20:30 (Ruben): een_lid.py voetfout (UNION liet het lid weg, zool los in B; Chris army_man). Gaat mee in gratis 0.1.2.
# Opnieuw 17 nov (Ruben, run 30): gratis 0.1.2: manifest (versie, tagline van Joris), meldingen met het belangrijkste
# vooraan (kan-punt Daan) in een_lid.py, gesloten.py en gewricht.py. Geen andere verandering.
# Opnieuw 19 nov (roestagent R5): meld.py nieuw (knop Report a problem, zonder enige verwijzing naar de betaalde versie) en __init__.py registreert meld.
GEKEURD = {
    "__init__.py": "526d677349cf407344d268dc15dbcb1bb68116dcdff387ceb221f6e80d88861e",
    "beweeg.py": "f7d9f2f26d2e780984b3b94e4e21ec983557f79e6d54f6f406b1ff83517219c6",
    "blender_manifest.toml": "2089bd52ad616af3789d3a681730fd03ed97fb59876057322218df9b05b09dd6",
    "drie_mf.py": "2cf1603e681bb5c4d1fb9a3f6fb46d73b7c264800ee6adf566a65d0f73f4f1f3",
    "eigenschappen.py": "677238f80391b6ddc7db3831ed074ea663b9a918100da1110d95414ec0117101",
    "exporteer.py": "d0e8b467db37c190b4173cbb8ce7bb075f2520b53a0b59325a8c233f7e3bd03f",
    "gesloten.py": "1a5c56fee836ebad205af30352fb34e57bb0cd0e5544424f421dc676b5bdd9ca",
    "een_lid.py": "6bd56557f8f099aba1181d888f0d63838fb08249173f20384c7327ca302f6bb9",
    "gewricht.py": "d51355f47f9079d6cdb1720c5ec5db1c58b7f1215ff72b44ebe7edd3043afd4b",
    "gradenboog.py": "159a503b3621da1073c8c29ee026454c9146a9b46a90d0028fec97096612e251",
    "kleur.py": "9f98ca165bfbe06d5c5737185bd4eee973accb8818563dbec0c794c2e5c9e1c4",
    "maat.py": "db5be6fea8bf18b478ba699a5cf68f564aeb7f33e7923f226b4cff108d2c9a9f",
    "meld.py": "77ca1508acd1b3f98eca2749462e37fbb80bb6da14789df7b395eb626dacd7b4",
    "paneel.py": "f3ed14701ac2db96e071c9f372b4a850b69133b4b25305c8817ed87f20b3f6ea",
    "passing.py": "26d843fc8fd39a519b82539811365cfe46d8115072ddafd85e9ca61889ea3aa9",
    "schaal.py": "bfcd37332fd8edd4e751cf4b44d03925ff66436b66e70c75e32670d735ac6c85",
    "uit_elkaar.py": "164a8308dc78c10bfb03def8da4f1d6e03ec3577b03fb671a42933a619a142ea",
    "vormen.py": "5517142f7f3572a9805f34abfb23fc45e983f684338831e8d896a3112ff29bd7",
    "waaier.py": "a08c0456fdfe5077f866a3652fb4d0608f6db9c3565963d41c10917d9a380c77",
}
anders = sorted(set(namen) ^ set(GEKEURD))
anders += [n for n in namen if n in GEKEURD and hashlib.sha256(zg.read(n)).hexdigest() != GEKEURD[n]]
stap("gratis zip gelijk aan de gekeurde stand 014172e (sha256 per bestand)", not anders, "; ".join(anders))
man_g = zg.read("blender_manifest.toml").decode()
tag_g = [r.split('"')[1] for r in man_g.splitlines() if r.startswith("tagline")]
stap("gratis manifest: versie 0.1.2, naam Click Joints", 'version = "0.1.2"' in man_g and 'name = "Click Joints"' in man_g)
stap("gratis tagline hooguit 64 tekens, zonder punt, met poseable", len(tag_g) == 1 and len(tag_g[0]) <= 64
     and not tag_g[0].endswith(".") and "poseable" in tag_g[0], str(tag_g))
# Kan-punt Daan (0.1.2): de statusbalk knipt lange zinnen af, dus wat je moet doen staat in de eerste 40 tekens.
lid = zg.read("een_lid.py").decode()
gew = zg.read("gewricht.py").decode() + zg.read("gesloten.py").decode()
vooraan = [re.search(r'MELD_VAST = \("Pick a spot', lid), re.search(r'MELD_DICHT = \("Pick another spot', lid),
           re.search(r'"Click Make watertight first:', gew), re.search(r'"Not watertight, use Make watertight:', gew),
           re.search(r'"Click Place joint in the 3D viewport:', gew),
           re.search(r'Joint placed\. \{passing\.fit_tekst\(kleur, wand\)\}\.\{auto_noot\}', gew)]
stap("meldingen: wat je moet doen vooraan", all(vooraan), str([i for i, v in enumerate(vooraan) if not v]))

zb = zipfile.ZipFile(betaald)
nb = zb.namelist()
stap("betaalde zip heeft betaald/__init__.py", "betaald/__init__.py" in nb)
init_b = zb.read("__init__.py").decode()
stap("betaalde __init__ registreert betaald", "from . import betaald as _betaald" in init_b)
stap("betaalde __init__ begint met de gratis __init__", init_b.startswith(zg.read("__init__.py").decode()))
stap("betaalde zip zonder __pycache__", not any("__pycache__" in n for n in nb))
man_b = zb.read("blender_manifest.toml").decode()
pro_versie = os.environ.get("PRO_VERSIE", "1.0.0")
stap(f"betaalde manifest: naam Click Joints Pro, versie {pro_versie}, id gelijk",
     'name = "Click Joints Pro"' in man_b and re.search(r'^version = "' + re.escape(pro_versie) + '"$', man_b, re.M) is not None and 'id = "click_joints"' in man_b)
stap("betaalde tagline hooguit 64 tekens zonder punt aan het eind",
     all(len(r.split('"')[1]) <= 64 and not r.split('"')[1].endswith(".") for r in man_b.splitlines() if r.startswith("tagline")))
print(f"[cj-zips] klaar: {fout} FOUT")
sys.exit(1 if fout else 0)
