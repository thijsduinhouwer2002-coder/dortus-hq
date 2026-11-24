# Keuring blender-gewrichten rig.py commentaar A3, 24-11-2026, automatische keurder
Wat ik keurde: commit 8b012bb5f (reeks 2496476..8b012bb), bestand producten/blender-gewrichten/click_joints/betaald/rig.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging splitst één commentaarregel in twee regels. Er verandert geen code, dus het gedrag van Pro 1.2.6 (robot-enkels) blijft gelijk. | Feit (uit de diff) | hoog | Een groene e2e-run op deze commit in 4.2.23, 5.2.3 en 5.3.0 zou het ook in de echte Blender bevestigen. |
| 2 | Het commentaar noemt "toets A3 in e2e/toetsen_robot_meer.py" en de cijfers 0% en 32 tot 35%. Of die toets en cijfers kloppen kan ik uit deze diff niet nagaan. | Vermoeden | midden | De toets in dat bestand en het log van de run van 24 nov (45384569641) zouden dat laten zien. |
| 3 | Het akkoord van Daan (24 nov, tak 6dc287f) geldt voor een eerdere stand. Het enige verschil sindsdien is hier een commentaar. | Feit voor deze diff, vermoeden voor de rest van de reeks | midden | `git diff 6dc287f..8b012bb` mag alleen commentaarregels tonen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er zijn geen tests aangepast, alleen een commentaarregel is verplaatst. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | De bestandsgrootte van rig.py zie ik niet. Een commentaar op twee regels maakt het bestand één regel langer. | Vermoeden | laag | Bestanden onder ±400 regels (het regelaantal vraagt een telling) |
| 3 | architectuur.md is niet bijgewerkt. Bij een puur commentaar is dat niet nodig. | Feit | hoog | architectuur.md bijgewerkt |
| 4 | Er zijn geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. Het commentaar noemt alleen "Olaf" als voornaam in de context van de robot van de studio. | Feit | hoog | Geen persoonsgegevens |
| 5 | De cijfers in het commentaar zijn als "gemeten" aangeduid en staan niet als GEZIEN, DERDEN of GOK gelabeld. Dat is gebruikelijk bij code-commentaar. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK (kleine opmerking) |
| 6 | Het is geen spelerstekst en er is geen AI-beeld of -geluid. | Feit | hoog | Hats-tekst als CONCEPT, geen AI-beeld op Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen. De wijziging raakt alleen een commentaar, dus voor de gebruiker verandert niets. | Niets te doen. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- De commentaarregels in dit blok zijn lang. Je zou het hele blok over A3 korter of als losse regels kunnen schrijven, dat is smaak.
- Zet bij "Gemeten op de robot" een label of verwijs naar de run, bijvoorbeeld "GEZIEN, run 45384569641", als dat klopt.
- Controleer met een telling dat rig.py onder ±400 regels blijft. Dat kan ik uit de diff niet zien.

---
Automatische keurder, model `claude-sonnet-5-5`, 17611 tokens in, 1517 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
