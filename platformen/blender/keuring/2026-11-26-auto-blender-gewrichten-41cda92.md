# Keuring blender-gewrichten changelog 0.1.2, 26-11-2026, automatische keurder
Wat ik keurde: commit 41cda9244 (reeks 544cb47..41cda92), alleen `producten/blender-gewrichten/CHANGELOG.md`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De enige wijziging is één regel in de changelog van 0.1.2: "Click a store or the X" wordt "Click the link or the X". Dat past bij de gratis build, die maar één winkelknop heeft (Blender Extensions) plus een kruisje. | Feit | Hoog | Architectuur beschrijft de gratis `BEOORDEEL` met alleen Blender Extensions en het kruisje met lege `url`. |
| 2 | De regel klopt met het gedrag: een klik op de link of het kruisje zet `cj_beoordeeld` en het merkje `rating_asked`, en daarna vraagt hij niet meer. | Feit | Hoog | Architectuur, onderdeel `meld.py`. De toets in `toetsen_paneel.py` zou dit in het log bevestigen. |
| 3 | De commitmelding zegt dat `click-joints-uitgave.yml` naar 0.1.2 is gezet, maar dat bestand staat niet in deze wijziging. | Vermoeden | Midden | Het zit waarschijnlijk in een eerdere commit. Dat blijkt uit `git log` op dat bestand of uit de versie in `blender_manifest.toml`. |
| 4 | De beweringen "Daan ja #127" en "e2e groen" kan ik uit de tekst niet nagaan. | Vermoeden | Laag | Het ja van Daan bovenaan `ontwerp.md` voor 0.1.2 en een groene run op de commit. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast. Er is alleen een changelogregel veranderd. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Versie 0.1.2 heeft 3 regels, binnen de grens van 5. De sectie is naar schatting ruim onder de 1024 tekens (±550), dus de uitgave-workflow kapt niets af. | Feit | Midden | Changelogregels: maximaal 5 regels en 1024 tekens |
| 3 | De tekst noemt geen betaalde functies of de betaalde versie. | Feit | Hoog | extensions.blender.org 3.3, 3.10, 6.1 en ToS 6.2 |
| 4 | Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | Hoog | Geen persoonsgegevens |
| 5 | `architectuur.md` hoeft niet bij: er verandert geen code of gedrag. | Feit | Hoog | architectuur.md bijgewerkt |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De nieuwe zin is duidelijker voor de gebruiker, want er is in de gratis build maar één link. Ik kan hier niets spelen of zien. | Niets nodig. | klein |
| 2 | Of "No popups" na het inklikken van de beoordelingsregel ook zo voelt, kan ik niet beoordelen. Dat moet Iris of Daan in Blender bekijken. | Een schermafbeelding van de regel onderin het paneel naast de tekst. | klein |

## Deel C: is het goed genoeg?
Niet van toepassing: dit is één regel tekst in een changelog, geen hoofdbeeld, omslag of thumbnail. Er is geen blinde test nodig en ik geef geen cijfers.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer dat `click-joints-uitgave.yml` echt op 0.1.2 staat. Dat bestand zit niet in deze wijziging, dus het blijft een vermoeden tot iemand het ziet.
- Controleer vóór het uitbrengen dat het ja van Daan (#127) en de groene e2e-run echt bij deze commit horen.

---
Automatische keurder, model `claude-sonnet-5-5`, 18046 tokens in, 2674 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
