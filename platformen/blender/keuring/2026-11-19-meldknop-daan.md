# Keuring meldknop "Report a problem" Click Joints (gratis en Pro), 19 nov 2026, Daan

Wat ik keurde: `producten/blender-gewrichten/click_joints/meld.py` op main, en de schermen `1-paneel-x.png` en `10-winkel-paneel-x.png` van Blender 4.2.23 en 5.3.0 uit de tak `schermen` (run 44426983769, commit e133d25). Gevraagd door Bram: ja of nee op plek en tekst.

## Deel A: werkt en ziet het er goed uit?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De knop staat als laatste regel onder stap 3 (Export), los van de drie stappen, zonder knoprand, met een klein wereldbol-icoon. Hij valt niet op tussen de echte werkknoppen en duwt niets weg. In 4.2.23 en 5.3.0 gelijk. | feit (GEZIEN) | hoog | |
| 2 | Ook in het volle paneel (plaatje 10: Good fit, bend range, richtingen) blijft hij onderaan onder Export STL. | feit (GEZIEN) | hoog | |
| 3 | Tekst "Report a problem" is kort, gewoon Engels, zegt wat er gebeurt. De tooltip zegt eerlijk dat er een melding op GitHub opengaat met versies ingevuld. | feit | hoog | |
| 4 | De link bevat alleen naam en versie van de add-on, Blender-versie en systeem (bijv. "Windows 11 (AMD64)"), geen gebruikersnaam of paden. Niets gaat vanzelf het net op; de gebruiker opent de link zelf. URL ±490 tekens, ruim binnen de grens. | feit (code gelezen, URL zelf nagebouwd) | hoog | |
| 5 | Of de repo click-joints meldingen aan heeft staan kon ik niet nakijken (deze run mag die repo niet lezen). Staan issues uit, dan geeft de knop een 404. | vermoeden | midden | de link eenmaal openen vóór 0.1.2 |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen persoonsgegevens van Thijs of van de gebruiker in code of link. | feit | hoog | harde regel 2 |
| 2 | Pro meldt in hetzelfde openbare loket als gratis; de naam in de melding zegt welke het is. Geen probleem. | feit | hoog | |

## Moet (blokkeert akkoord)
Geen.

## Kan (mag later)
1. Vóór 0.1.2 één keer de link openen en zien dat het formulier op click-joints opengaat (punt A5).
2. Winkelbeeld 10 laat de knop nu ook zien. Mag blijven: klein en eerlijk. Wil je een strakker winkelbeeld, snij dan net boven de knop af.

**Akkoord: ja** op plek en tekst. Mag mee in 0.1.2.
