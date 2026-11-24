# Keuring blender-gewrichten gids 5 (downloaded STL), 24-11-2026, automatische keurder
Wat ik keurde: commit e0a0b5c37 (65219c0..e0a0b5c), de bestanden `e2e/gids_stl_bron.py` en `e2e/scherm_gids_stl.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
De opdracht is hier geen release maar een schermscript voor een gidspagina. De add-on zelf is niet veranderd, dus het akkoord van 16 nov voor 0.1.1 en 1.0.2 blijft staan.

| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De commitbericht zegt zelf dat het middel van het figuur door de armen snijdt en dat er een ander model nodig is. De constante `MIDDEL` staat nog op dat punt, dus de plaatjes `s2-joint` en `s3-export` zijn zo niet bruikbaar voor de gids. | Feit (uit het bericht), vermoeden dat het zo in beeld komt | midden | Een log met `GIDS plaats:` en een bekeken `s2-joint.png` zonder doorsneden armen. |
| 2 | De opmerking bij `MIDDEL` zegt "daar is de wand groen". Dat staat haaks op het commitbericht en klopt waarschijnlijk niet voor dit model. | Vermoeden | midden | Het veld `cj_passing` in de regel `GIDS plaats:` van het log. |
| 3 | Het script volgt de stappen van de gids: standaardkubus weg, STL laden, Check mesh, Convert to mm, Make watertight indien nodig, Place joint, export 3MF. Het gebruikt alleen de gratis zip, dus geen betaalde functies in beeld. | Feit (uit de code) | hoog | Niet nodig. |
| 4 | Of de drie plaatjes echt zijn ontstaan en er goed uitzien, kan ik uit tekst niet halen. Er zit geen beeld of log bij de wijziging. | Vermoeden | laag | De regels `GIDS OK s1-import.png`, `s2-joint.png` en `s3-export.png` in het log, en iemand die de plaatjes bekijkt. |

## Deel B: houdt het zich aan onze regels?

| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast. Beide bestanden zijn nieuw en veel korter dan 400 regels. | Feit | hoog | Tests niet aanpassen om te slagen, bestandsgrootte. |
| 2 | In `gids_stl_bron.py` staan vaste paden onder `/home/claude/g5` (`knight.glb`, `bones.json`, `figure.stl`). Die invoer zit niet in de repo en is op een andere machine niet na te maken. Dit zijn geen persoonsgegevens. | Feit | hoog | Reproduceerbaar maken (geen regel geschonden). |
| 3 | De bron is CC0 van Quaternius ("quaternius-showcase"). Er staat geen link of naam van de download in de repo. De licentie is dus nergens vastgelegd. | Feit | hoog | Herkomst van beeldmateriaal vastleggen. |
| 4 | Er is geen AI-beeld of AI-geluid, en geen persoonsgegevens of sleutels. De export gaat naar een tijdelijke map, zodat geen machinepad in beeld komt. | Feit | hoog | Geen AI-beeld op Steam, geen persoonsgegevens. |
| 5 | `architectuur.md` is niet bijgewerkt. Het gaat om proefscripts onder `e2e/` en niet om de add-on, dus dit is geen blokkade. | Feit | midden | architectuur.md bijgewerkt. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan geen beelden zien. Dit is dus alleen wat uit het script volgt.

| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een gids voor mensen die alleen een STL downloaden, is pas overtuigend als het eerste gewricht op een plek zit die iedereen snapt (elleboog, knie, nek). Een snede door het middel met armen ernaast leest als een fout. | Kies een ander model, of zet de cursor op een arm of been en toon dat. | klein |
| 2 | De kijkhoek (Euler 1.30, 0, 0.55) en de afstand zijn vast. Dan is het plaatje voor elk model even statisch. | Richt de camera op het gekozen gewricht, zodat de gloed en het opengewerkte beeld goed te zien zijn. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet de tekst van de bouwer ("middel snijdt door armen") en het eigen oordeel in de repo, zodat de plaatjes niet zonder nieuwe run op dortus.com komen. De gidspagina publiceren mag pas na een keuring van de echte plaatjes door Daan of Iris.
- Pas de opmerking bij `MIDDEL` aan, of kies een gewricht op een plek waar de wand echt groen is.
- Leg de bron van het figuur vast: downloadlink en CC0-vermelding, bijvoorbeeld in de docstring of een README in `e2e/`.
- Maak de paden in `gids_stl_bron.py` instelbaar (argumenten of een map in de repo), of voeg `figure.stl` of een downloadstap toe.
- Controleer in `scherm_gids_stl.py` dat `delen[0]` het goede deel is. De volgorde van `bpy.data.objects` is niet gegarandeerd. Kies liever het deel met `cj_deel == "A"`, als die eigenschap bestaat.
- Vul na een nieuwe run het log (`GIDS OK ...` en `GIDS plaats: ... passing=`) in bij de volgende keuring, als bewijs voor de plaatjes.

---
Automatische keurder, model `claude-sonnet-5-5`, 20658 tokens in, 3770 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
