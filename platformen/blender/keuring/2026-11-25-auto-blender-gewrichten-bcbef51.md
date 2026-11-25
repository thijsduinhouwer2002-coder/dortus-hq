# Keuring blender-gewrichten (Click Joints) issue 100, 25-11-2026, automatische keurder
Wat ik keurde: commit bcbef51ea (e893f68..bcbef51), alleen als tekst gelezen
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De code voegt het kruisje "Don't ask again" toe. Het is dezelfde operator met een lege `url`, opent niets en onthoudt de keuze. Dit past bij de CHANGELOG-regel en bij issue 100. | Feit (uit de diff) | Hoog | Een groene e2e-run met de nieuwe toets "kruisje werkt". |
| 2 | De regel verschijnt alleen na een export en een Good fit, en verdwijnt na een klik op een winkel of het kruisje, ook in een ander bestand. De code en de toets in `toetsen_paneel.py` doen dat. | Feit (code), vermoeden (uitvoering) | Midden | E2e-log in 4.2, 5.2 en 5.3 met de regels "beoordelen: ...". |
| 3 | Het commentaar zegt dat het merkje "één keer per sessie" wordt gelezen. `GEVRAAGD` wordt alleen `True` gezet. Zolang er nog niet is geklikt, kijkt `al_gevraagd` bij elke hertekening opnieuw naar het bestand, maar pas na een export en een Good fit. | Feit (uit de code) | Hoog | Lezen van `al_gevraagd`. Het gaat om een goedkope `os.path.exists`, dus het is klein. |
| 4 | `merkbestand()` maakt de map niet meer aan bij elke hertekening (`create=maak`). Dat is een verbetering. | Feit | Hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is uitgebreid, niet verzwakt: kruisje als echte operator, een `schoon()`-hulp, en een nieuwe sessie nagebootst via `GEVRAAGD`. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | In `toets_zips.py` is alleen de vastgezette hash van `meld.py` vervangen. De andere hashes zijn gelijk gebleven. Ik kan niet narekenen of de nieuwe hash klopt met de nieuwe `meld.py`. | Vermoeden | Midden | Tests / zip-controle; een groene run zou het bevestigen |
| 3 | `architectuur.md` is bijgewerkt (kruisje, `GEVRAAGD`, toets). `KAART.md` en `CHANGELOG.md` ook. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | De KAART noemt winkellinks "alle drie 200, GEZIEN" met curl op 25 nov 20:30. Ik kan dat uit de tekst niet narekenen. | Vermoeden | Laag | Een curl-uitvoer bij de bron |
| 5 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. `meld.py` is kort. De gratis build noemt de betaalde versie niet. | Feit | Hoog | Regels 3.3, 3.10, 6.1 van extensions.blender.org |
| 6 | Er zit geen e2e-uitslag bij de wijziging. De KAART zegt dat de uitslag en de keuring van Daan "in #100" staan. | Feit | Hoog | Run-id van de e2e op deze commit |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Het kruisje staat zonder rand in een rij met knoppen mét rand. Of dat er in Blender netjes uitziet, kan ik niet zien. | Een schermafbeelding in 4.2 en 5.2 bekijken. | Klein |
| 2 | Wie op het kruisje klikt, krijgt de vraag nooit meer terug, in geen enkel bestand. Er is geen manier om dat terug te draaien behalve het merkje wissen. | Eventueel een regel in de README of de Preferences, maar niet nodig. | Klein |
| 3 | Het kruisje heeft alleen een tooltip. Het is dus een bewuste keuze dat het kruisje niet voor zichzelf spreekt. | Controleer op het scherm of het duidelijk genoeg leest. | Klein |

## Deel C: is het goed genoeg?
Dit is een klein paneeldetail, geen hoofdbeeld, omslag of thumbnail, dus de blinde test is niet nodig. Ik kan geen beeld zien, dus ik geef geen cijfers 1 tot 10. De keuring van Daan op uiterlijk staat volgens de KAART nog open in #100. De uitgave is ingepland niet vóór 30 nov.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Draai de e2e en zie dat de nieuwe hash van `meld.py` klopt. Dat bevestigt B2. Zonder groene run staat hij nog open voor uitbrengen.
2. Pas het commentaar "één keer per sessie" aan, of cache ook het `False`-geval (A3).
3. Laat Daan de schermafbeelding van het kruisje in de rij zien (C1, C3).
4. Zet het run-id van de e2e en de curl-uitvoer bij de KAART (B4, B6).

---
Automatische keurder, model `claude-sonnet-5-5`, 27368 tokens in, 4519 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
