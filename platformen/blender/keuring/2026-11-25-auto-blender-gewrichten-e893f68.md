# Keuring beoordelingsregel pas na export (issue 100), 25-11-2026 20:11 NL, automatische keurder
Wat ik keurde: commit e893f68da (bbdd604..e893f68), bestanden `meld.py`, `architectuur.md`, `e2e/toets_zips.py`, `e2e/toetsen_paneel.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
(Opdracht: issue 100 uit de commit: beoordeling pas na een export, niet meer na een klik op een winkel. Ik zie alleen de diff, geen testuitslag.)
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De regel "Happy with it?" verschijnt nu alleen bij Good fit, een export (`cj_laatste_export` op de scène) en nog geen klik. `vraag_beoordeling` doet precies dat. | Feit (uit de code) | hoog | Een groene e2e-run met de nieuwe stappen in `toetsen_paneel.py`. |
| 2 | Een winkelknop gaat nu via `click_joints.beoordeel`. Die opent de winkel en onthoudt de klik in de scène en in een merkje in de extensiemap, dus ook in andere bestanden. | Feit (uit de code) | hoog | Handmatig in Blender: klik, open een ander .blend, en de regel blijft weg. |
| 3 | Het diff-bewijs dat `exporteer.py` `cj_laatste_export` zet ontbreekt: dat bestand is niet gewijzigd en de test zet de sleutel zelf. Zet het bestaande code die sleutel niet echt, dan verschijnt de regel nooit. | Vermoeden | midden | `grep cj_laatste_export click_joints/exporteer.py`, of een e2e-stap die echt exporteert en dan `vraag_beoordeling` controleert. |
| 4 | Het nieuwe `meld.py` gebruikt `os` en `bpy.utils.extension_path_user`. De imports bovenin staan niet in de diff. Ontbreekt `import os`, dan vangt `except Exception` de fout stil af en onthoudt de add-on niets over bestanden heen. | Vermoeden | laag | De kop van `meld.py` en de e2e-stap "ook in een ander bestand weg" met een harde eis dat het merkpad bestaat. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Tests zijn uitgebreid, niet versoepeld: nieuwe stappen voor "nog niet vóór export", "winkelknop via beoordeel", "na klik weg" en "ander bestand". | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | De cross-bestand-stap staat achter `if merk:`. Is `merk` leeg (add-on draait niet als extensie), dan wordt die stap stil overgeslagen en lijkt de test groen. | Feit (uit de code), gevolg is vermoeden | midden | Tests moeten echt iets toetsen |
| 3 | De pinhash van `meld.py` in `toets_zips.py` (GEKEURD) is bijgewerkt met een uitleg. Of de nieuwe hash klopt met het bestand kan ik niet narekenen. De nieuwe code noemt nergens de betaalde versie. | Feit (uitleg), hash onbekend | midden | Gratis zip zonder verwijzing naar betaald; `toets_zips` bewaakt dit |
| 4 | `architectuur.md` beschrijft de nieuwe werking (issue 100, operator, merkje, toets). | Feit | hoog | architectuur.md bijgewerkt |
| 5 | `CHANGELOG.md` (gratis, Unreleased) zegt nog "After a Good fit, one small line ... links to the reviews". Dat klopt niet meer en die tekst gaat naar de release notes. | Feit | hoog | Changelog vanuit de gebruiker, klopt met de uitgave |
| 6 | Bestandsgrootte, persoonsgegevens: `meld.py` is ongeveer 145 regels en het merkje bevat alleen "1". De winkellink is volgens de commit met curl nagekeken (200), dat is GEZIEN door de bouwer. Er staan geen sleutels of persoonsgegevens in de diff. | Feit | hoog | Bestanden onder ±400 regels, geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Vragen na een export is een beter moment dan na het plaatsen: de gebruiker heeft dan iets om te printen. Dat oordeel komt alleen uit de tekst. | Niets nodig. | klein |
| 2 | Wie nooit klikt, ziet de regel na elke export in elk nieuw bestand, tot in het oneindige. | Een kleine "Not now" die het merkje zet, of de regel hooguit enkele keren tonen. | klein |
| 3 | Het merkje wordt bij elke hertekening van het paneel gecontroleerd en aangemaakt (`create=True`). Dat gebeurt alleen na een export, maar bestandstoegang in `draw` is onrustig. | Het merkje eenmalig lezen en in een variabele bewaren. | klein |

## Deel C: is het goed genoeg?
Er is geen beeld, geen blinde test en geen speelbare versie. Cijfers kan ik niet geven en ik verzin ze niet. Daan of Iris moeten het paneel zien (regel na export, regel weg na klik) voor het uitkomt.
| Vraag | Cijfer 1 tot 10 | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | niet te geven | Alleen tekst gezien, geen scherm. |
| Zou ik het zelf kopen of bekijken op basis van dit? | niet te geven | Kleine paneelwijziging, geen winkelbeeld. |
| Zou Thijs er trots op zijn? | niet te geven | Zie hierboven. |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
1. Zet in de e2e-test een harde eis dat `meld.merkbestand()` niet `None` is (of sla de stap uitdrukkelijk als "overgeslagen" over in het log), zodat een stille mislukking niet groen lijkt.
2. Controleer dat `exporteer.py` `cj_laatste_export` echt zet, met een e2e-stap die exporteert en dan `vraag_beoordeling` toetst (Deel A 3).
3. Controleer dat `import os` bovenin `meld.py` staat (Deel A 4).
4. Pas de Unreleased-regel in `CHANGELOG.md` aan naar "After a Good fit and an export" voor de uitgave.
5. Eis voor het uitbrengen een groene e2e-run (4.2, 5.2, 5.3) op deze commit. Het akkoord hierboven hangt daaraan, want ik zie geen runuitslag.
6. Voeg een "Not now" toe en lees het merkje niet bij elke hertekening (Deel C 2 en 3).

---
Automatische keurder, model `claude-sonnet-5-5`, 26329 tokens in, 6113 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
