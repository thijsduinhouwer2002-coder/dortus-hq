# Keuring blender-gewrichten, beoordelingsregel na export (issue 100), 25-11-2026, automatische keurder
Wat ik keurde: commits 8a63cef..d3ab39a (fb91ce255 en d3ab39ab2), de bestanden `meld.py`, `toetsen_paneel.py`, `toets_zips.py`, `CHANGELOG.md`, `KAART.md` en `architectuur.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De regel "Happy with it? Leave a rating:" verschijnt in `meld.py` pas bij Good fit, een export (`cj_laatste_export`) en nog niet geklikt. Een klik op een winkel of op het kruisje zet `cj_beoordeeld` op de scène en schrijft het merkje `rating_asked`. | Feit (uit de code) | Hoog | Het is bevestigd door de nieuwe toetsstappen. De uitslag van die run zag ik niet. |
| 2 | Ik zie in de wijziging niet dat `exporteer.py` `cj_laatste_export` zet. Dat bestand staat niet in de gewijzigde bestanden en de toets zet de waarde zelf. Als het niet bestaat, verschijnt de regel in de praktijk nooit. | Vermoeden | Midden | Zoek `cj_laatste_export` in `exporteer.py` (`grep`), of laat de toets echt exporteren via `click_joints.exporteer` en dan de regel controleren. |
| 3 | "Ook in een ander bestand weg" werkt via `bpy.utils.extension_path_user`. Draait de add-on niet als extensie, dan geldt alleen de scène. | Feit | Hoog | De toets slaat die stap over als er geen extensiemap is (alleen een printregel). In het e2e-log moet de regel `[cj-paneel] merkje: <pad>` staan. |
| 4 | De tekst in architectuur en changelog klopt met de code: kruisje met tooltip "Don't ask again", winkels via `click_joints.beoordeel`, geen popup en niets dat vanzelf het netwerk op gaat. | Feit | Hoog | n.v.t. |
| 5 | In `architectuur.md` staat "het merkje wordt één keer per sessie gelezen". Dat klopt alleen als het merkje bestaat. Bestaat het niet, dan doet `al_gevraagd` bij elke hertekening opnieuw `os.path.exists`, zolang de regel in beeld is. | Feit (uit de code) | Hoog | Leesbaar in `al_gevraagd`: `GEVRAAGD` blijft False bij een ontbrekend merkje. Het is goedkoop, maar de beschrijving is niet exact. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toetsen zijn uitgebreid en niet verzwakt. Het gedrag veranderde bewust, dus de stap "wel na Good fit" werd "Good fit telt" plus "wel na Good fit en export". | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | In `toets_zips.py` is alleen de sha256 van `meld.py` bijgewerkt, met een uitleg erbij. Of die hash bij de laatste commit past, kan ik uit tekst niet narekenen. | Vermoeden | Midden | Tests niet aangepast om te slagen |
| 3 | `KAART.md` noemt e2e 45684750503 op bcbef51, een hash die niet in deze commitlijst staat. Op d3ab39a zelf zie ik geen run. 4.2.23 was eerst rood op `knight_yellow` en werd groen na een herstart, met de aanduiding "buiten deze wijziging" zonder bewijs. | Vermoeden | Midden | Cijfers met GEZIEN/DERDEN/GOK |
| 4 | De bestanden blijven ruim onder de 400 regels. `architectuur.md` en `KAART.md` zijn bijgewerkt. Er staan geen persoonsgegevens, sleutels of wachtwoorden in. Het merkje bevat alleen "1". | Feit | Hoog | Bestandsgrootte, architectuur.md, geen persoonsgegevens |
| 5 | In `KAART.md` staat dat note `pro-1.2.9.md` is aangepast, maar dat bestand zit niet in deze wijziging. | Vermoeden | Laag | Een aanpassing hoort bij de wijziging te staan, of je moet haar in een eerdere commit kunnen aanwijzen. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De regel is rustig en dwingt niets af. Je kunt hem permanent wegklikken en hij komt niet terug. Dat is prettig. | n.v.t. | n.v.t. |
| 2 | In Pro staan Superhive, Gumroad en het kruisje op één rij in een smalle zijbalk. Ik vermoed dat de knoptekst afgekapt wordt en het kruisje klein is. Ik zie geen scherm. | Een schermafbeelding van de zijbalk op smalle breedte bekijken. Zo nodig de winkels op twee rijen zetten. | Klein |
| 3 | De vraag komt direct na de export, dus vóór de print er is. De speler weet dan nog niet of het gewricht klikt. | Overweeg de regel pas te tonen een tijd na de export of na de tweede export. Dat levert waarschijnlijk betere beoordelingen op. | Klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeken (link naar het beste voorbeeld van een concurrent) |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | geen cijfer | Ik zie alleen tekst en geen beeld, en kan dit niet vergelijken. Dit is een kleine regel in het paneel en geen hoofdbeeld, dus de blinde test geldt niet. |
| Zou ik het zelf kopen of bekijken op basis van dit? | geen cijfer | Dit is geen koopbeslissing. Het is een detail in het paneel. |
| Zou Thijs er trots op zijn? | geen cijfer | Dat kan alleen met een zichtbaar scherm. Daan of Iris keuren het. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Controleer dat `exporteer.py` `cj_laatste_export` echt zet (Deel A, 2). Anders is de regel dood. Laat de toets één echte export doen.
2. Draai e2e op exact d3ab39a en noteer de run. Dan staat er geen onbekende hash in de KAART, en is de hash van `meld.py` in `toets_zips.py` bevestigd.
3. Maak de herstart op 4.2.23 (`knight_yellow`) een eigen issue als hij vaker rood wordt, in plaats van "buiten deze wijziging".
4. Pas "één keer per sessie" in `architectuur.md` aan of cache ook het ontbreken van het merkje.
5. Laat Daan of Iris het paneel op smalle breedte bekijken (Deel C, 2).
6. Laat de toets de stap met het merkje niet stilletjes overslaan buiten een extensie.

---
Automatische keurder, model `claude-sonnet-5-5`, 28305 tokens in, 7812 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
