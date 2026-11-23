# Keuring logregel shaderwacht in schermen.py, 23-11-2026, automatische keurder
Wat ik keurde: commit a2c4035da, bestand producten/blender-gewrichten/e2e/schermen.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging past alleen twee logtekst-regels aan in het proefscript: "s extra wachten" wordt "pogingen van 1 s extra wachten". De add-on zelf en de gebruikersfuncties blijven gelijk. | Feit | hoog | De diff toont alleen die twee f-strings. |
| 2 | De nieuwe tekst klopt alleen als `shaderwacht` echt het aantal pogingen telt, elk van 1 s. Dat blijkt wel uit de `return 1.0` net boven de gewijzigde regels, maar de teller zelf zie ik niet in de diff. | Vermoeden | midden | Het stuk waar `toestand["shaderwacht"]` wordt opgehoogd, of een run waarin het aantal klopt met de gemeten wachttijd. |
| 3 | De opdracht (kniefout 0.1.1 en 1.0.2) gaat over de add-on. Deze wijziging raakt dat niet en maakt het akkoord van Daan van 16 nov niet ongeldig. | Feit | hoog | Geen bestand in `click_joints/` of de manifesten is gewijzigd. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast om te slagen. Het gaat om een logregel, de voorwaarden `wacht` en `strook_gekleurd()` zijn niet veranderd. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | Het bestand is maar twee regels veranderd. Of het onder ±400 regels blijft, zie ik niet uit de diff. | Vermoeden | laag | Bestanden onder ±400 regels. Een regelaantal van `schermen.py` zou dit bevestigen. |
| 3 | `architectuur.md` is niet bijgewerkt, maar een logtekst in een proefscript vraagt daar geen aanpassing. | Feit | midden | architectuur.md bijgewerkt |
| 4 | Geen persoonsgegevens, sleutels of cijfers zonder label in de wijziging. | Feit | hoog | Geen persoonsgegevens, GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Een gebruiker ziet hier niets van, want het is een logregel in een proefscript. Beeld en speelplezier kan ik uit tekst niet beoordelen. | Niet van toepassing. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer of `shaderwacht` echt in stappen van 1 s optelt, zodat de logtekst klopt (Deel A, punt 2).
- Noem de eenheid in de logtekst één keer in een constante, dan staat hij niet op twee plekken.

---
Automatische keurder, model `claude-sonnet-5-5`, 17372 tokens in, 1264 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
