# Keuring blender-gewrichten testkaartplaatjes, 19-11-2026, automatische keurder
Wat ik keurde: commit 8bce0692a (d78a128..8bce069), bestand `producten/blender-gewrichten/e2e/scherm_testkaart.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Plaatje 20: camera van 1,6 naar 1,45 keer de grootste maat, dus iets dichterbij. Dat is wat de commit en het commentaar noemen ("Daan herkeuring 20, kan"). | Feit (diff) | hoog | n.v.t. |
| 2 | Plaatje 20h: hoek van 8 naar 38 graden, dus 30 graden gedraaid, zoals het commentaar zegt. | Feit (diff) | hoog | n.v.t. |
| 3 | Of de platte kant van tong en pengat nu echt in beeld staat en niets wordt afgesneden, kan ik uit tekst niet zien. | Vermoeden | laag | De nieuwe `20-testkaart.png` en `20h-testkaart-scharnier.png` bekijken met de Read-tool. |
| 4 | De docstring zegt nu "alle drie plaatjes bestaan". Dat klopt met de drie `render`-aanroepen (20, 20d, 20h). De eis "KAART BEELD OK" is niet veranderd. | Feit (diff) | hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Alleen camerawaarden en een docstring zijn aangepast. Er is geen test aangepast om te slagen en de controle op 10 + 10 delen en vijf getallen per set is gelijk gebleven. | Feit (diff) | hoog | Tests niet aangepast om te slagen |
| 2 | Er staan geen persoonsgegevens, sleutels of cijfers zonder label in de wijziging. | Feit (diff) | hoog | Geen persoonsgegevens, GEZIEN/DERDEN/GOK |
| 3 | De plaatjes komen uit Workbench-renders van eigen geometrie, niet van een AI-generator. | Feit (docstring) | midden | Geen AI-beeld op Steam |
| 4 | De bestandslengte zie ik niet in de diff. De wijziging maakt het bestand niet langer. | Vermoeden | midden | Bestanden onder ±400 regels (`wc -l` zou het bevestigen) |
| 5 | `architectuur.md` is niet bijgewerkt. Dat is hier niet nodig, want de wijziging raakt alleen de weergave in een testscript. | Feit | hoog | architectuur.md bijgewerkt |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Dichterbij en een gedraaide hoek maken het plaatje waarschijnlijk duidelijker. Ik kan het niet zien. Het risico is dat de rand of het onderschrift "Shown pulled apart" nu wordt afgesneden. | Bekijk de drie plaatjes na de run en zet bij afsnijden de factor terug naar ±1,5. | klein |
| 2 | Plaatje 20d is niet aangepast. | Alleen aanpassen als Daan er iets van vindt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** niets.

**Kan:**
- De drie plaatjes van deze run bekijken (Daan of Iris) op afsnijden en leesbaarheid van het onderschrift.
- Controleren dat het bestand onder ±400 regels blijft.

---
Automatische keurder, model `claude-sonnet-5-5`, 17937 tokens in, 1931 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
