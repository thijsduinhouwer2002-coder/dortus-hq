# Keuring blender-gewrichten, 19-11-2026, automatische keurder
Wat ik keurde: commit a753e11a (b7b6ed6..a753e11), drie proefscripts onder producten/blender-gewrichten/e2e/
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging raakt alleen proefscripts. De add-on, de beloften in ontwerp.md en de gratis en betaalde zip blijven gelijk. | Feit (lijst gewijzigde bestanden) | hoog | Een `git diff --stat` dat niets onder `click_joints/` toont. |
| 2 | De nieuwe verwachting in de toets, "8 joints · 1 rig · 1 mirror · 6 preset", klopt met het figuur. Het zijn 8 gewrichten: 1 elleboog uit de rig, 1 gespiegeld, 6 preset (2 knieën, 2 heupen, 2 schouders). | Feit (uit de docstring en de assert) | midden | De groene run van `toetsen_rig_armen.py` laat de samenvatting van de add-on dezelfde tekst geven. |
| 3 | De add-on moet die samenvatting al zo tonen (Daan 18 nov, moet 1). Dat staat niet in deze commit. | Vermoeden | midden | Een eerdere commit die het paneel veranderde, of de samenvattingsregel in de paneelcode. |
| 4 | `zijbalk_omlaag` scrolt de zijbalk met `view2d.scroll_down`, zodat plaatje 19 het onderste deel van het paneel toont. Of dat nu werkt, valt uit de tekst niet te halen. | Vermoeden | laag | Plaatje `19-mens.png` met het paneel onderaan, en in het log de regel "MENS zijbalk omlaag: True". |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is aangepast, maar op één dingvergelijking: de verwachte tekst volgt een bewuste paneelwijziging. Dat past bij "tests niet aangepast om te slagen", mits de add-on echt eerst veranderde. | Vermoeden | midden | Tests niet aanpassen om te slagen |
| 2 | De streng-check blijft precies: de volledige tekst moet gelijk zijn, er is niets versoepeld of weggehaald. | Feit | hoog | Tests niet aangepast om te slagen |
| 3 | De wijziging is klein, dus de bestandsgrens van ±400 regels komt niet in beeld. De omvang van `scherm_mens.py` zelf kan ik niet zien. | Vermoeden | laag | Bestanden onder ±400 regels |
| 4 | De toevoeging is een testhulp. `architectuur.md` hoeft niet bij te werken. Er staan geen persoonsgegevens of sleutels in de wijziging. | Feit | hoog | architectuur.md, geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Ik kan geen beeld zien. Of plaatje 19 nu de onderkant van het paneel toont, moeten Daan of Iris kijken. | Plaatje 19 nakijken op de tak `schermen` nadat de run klaar is. | klein |
| 2 | De commitregel noemt een onderschrift ("Daan moets 1 en 2, kan 3"). In deze diff staat geen onderschrift of tekst voor een plaatje. | Controleren of het onderschrift in een andere commit staat en niet is vergeten. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Kijk na in de volgende run of het log "MENS zijbalk omlaag: True" toont en plaatje 19 het onderste paneel laat zien.
- Zet de oude xdotool-scrolllus (25 klikken) weg als `view2d.scroll_down` werkt. Nu draaien beide naast elkaar.
- Controleer dat de samenvattingstekst in de add-on al "1 rig · 1 mirror · 6 preset" is (Daan 18 nov, moet 1), zodat de toets het gedrag volgt en niet andersom.
- Zoek het onderschrift uit de commitregel op, want het staat niet in deze wijziging.

---
Automatische keurder, model `claude-sonnet-5-5`, 19233 tokens in, 2723 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
