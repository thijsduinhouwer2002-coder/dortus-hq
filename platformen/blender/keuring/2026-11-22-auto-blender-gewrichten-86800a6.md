# Keuring blender-gewrichten (Click Joints Pro, rig.py), 22-11-2026, automatische keurder
Wat ik keurde: commit 86800a638 (2e86648..86800a6), alleen `producten/blender-gewrichten/click_joints/betaald/rig.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De nieuwe functie `gedraaid` draait de assen goed. (h, buig, lid) wordt (buig, -h, lid) of (-buig, h, lid), en het uitproduct blijft het lid. Een rechtshandig stelsel blijft dus rechtshandig. | Feit (uit de tekst gerekend) | hoog | Een kleine test op een matrix: determinant 1 en kolom 2 ongewijzigd. |
| 2 | De bewering dat de Yeti 16% van de punten kwijtraakt en dat gedraaid dit oplost, staat als GEZIEN in een commentaar. In de wijziging zit geen log, test of run die dat toont. | Vermoeden | midden | Een run op de Yeti en een andere Quaternius-rig met uitkomst vóór en na, en het aantal punten per deel. |
| 3 | Het vangnet komt pas aan de beurt na de bestaande kandidaten, dus rigs waar het al lukte veranderen niet. Dat klopt alleen als de lus na de eerste geslaagde plek stopt. Die lus staat niet in de wijziging. | Vermoeden | midden | De lus rond `kandidaten` in `rig.py` lezen, of een run op een rig die al werkte met dezelfde uitkomst. |
| 4 | `kandidaten[0]` wordt zonder controle gebruikt. Geeft `scharnier_plekken` een lege lijst, dan volgt een IndexError in plaats van de nette melding van voorheen. | Vermoeden | midden | Een test met een lid zonder bruikbare plek: geeft hij een melding of een foutmelding in de console? |
| 5 | Het vangnet staat in de tak voor alle scharnieren, niet alleen voor de elleboog. Bij een knie zou 90 graden draaien sideways buigen betekenen. Het commentaar noemt alleen de elleboog. | Vermoeden | midden | Controleren of die tak ook de knie bedient, en een beeld of meting van de gekozen buigrichting bij een knie. |
| 6 | Dit is Pro 1.1 en wordt in het commentaar zo genoemd. Het ontwerp en het akkoord van Daan gaan over Pro 1.0.2. Voor 1.1 staat er geen eis of akkoord in `ontwerp.md`. | Feit | hoog | Een regel in `ontwerp.md` voor Quaternius-rigs en de versie 1.1 vóór het uitbrengen. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test of beweegproef toegevoegd voor `gedraaid` of het vangnet. Alleen `rig.py` veranderde. | Feit | hoog | Nieuw gedrag moet toetsbaar zijn in de echte Blender op Actions. |
| 2 | `architectuur.md` is niet bijgewerkt, terwijl er een nieuw gedrag in het rigpad bij is. | Feit | hoog | architectuur.md bijgewerkt |
| 3 | `rig.py` is veel langer dan ±400 regels: de diff laat regelnummers rond 650 en 670 zien. Deze wijziging maakt het bestand nog 22 regels groter. | Feit | hoog | Bestanden onder ±400 regels |
| 4 | Er staan geen tests aangepast en geen persoonsgegevens, sleutels of wachtwoorden in de wijziging. | Feit | hoog | Tests niet aangepast om te slagen, geen persoonsgegevens |
| 5 | De cijfers in het commentaar (Yeti 150 mm, 16%, z 126 mm) dragen het label GEZIEN. Het bewijs zit niet in deze wijziging. | Vermoeden | laag | Cijfers met GEZIEN/DERDEN/GOK |

## Deel C: zou een gebruiker het leuk en fijn vinden?
Ik kan niets zien of spelen, dit is alleen uit de tekst gehaald.
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De gebruiker merkt niet dat de add-on zelf het scharnier heeft gedraaid. Een elleboog die plots horizontaal buigt, kan verrassen. | Een korte melding "hinge turned 90°, because the first cut lost part of the figure" en een knop om terug te wisselen. | klein |
| 2 | De voorkeur voor naar voren buigen (-Y) past bij een elleboog. Voor een knie is dat anatomisch onhandig. | De voorkeur per gewrichtssoort laten verschillen, of de knie uit het vangnet laten. | klein |
| 3 | Bij Quaternius-monsters en andere rigs met een onverwachte T-houding is dit precies waar kopers last van hebben. Een Yeti en een tweede rig als voorbeeld en plaatje in de Pro-uitleg zou het vertrouwen vergroten. | Een proefplaatje van twee game-rigs, alleen voor Pro-pagina's (niet voor extensions.blender.org). | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet een controle op een lege `kandidaten` vóór `kandidaten[0]` (A4).
- Controleer of het vangnet ook voor de knie geldt en beperk het tot de elleboog als dat zo is (A5, C2).
- Voeg een test toe met de Yeti (en een tweede Quaternius-rig) die laat zien dat de snede geen punten verliest, plus een matrixtest van `gedraaid` (A2, B1).
- Werk `architectuur.md` bij met het vangnet (B2).
- Splits `rig.py` op, want het bestand is ruim boven ±400 regels (B3).
- Leg Pro 1.1 en Quaternius-rigs vast in `ontwerp.md` en laat Daan het zien vóór uitbrengen (A6).
- Meld aan de gebruiker dat het scharnier is gedraaid (C1).

---
Automatische keurder, model `claude-sonnet-5-5`, 18123 tokens in, 5471 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
