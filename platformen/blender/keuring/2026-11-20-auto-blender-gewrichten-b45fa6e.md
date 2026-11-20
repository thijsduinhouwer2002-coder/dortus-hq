# Keuring blender-gewrichten README Pro-trechter, 20-11-2026, automatische keurder
Wat ik keurde: commit b45fa6ea5, bestand producten/blender-gewrichten/repo-click-joints/README.md (alleen de tekstwijziging, gelezen)
Akkoord: nee

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De README noemt $19 (persoonlijk) en $59 (studio). In de opdracht staat alleen $12 (lanceerprijs $9) en studio $45. Het commit zegt "juiste prijs", maar in de meegestuurde tekst staat geen besluit of winkelpagina die $19 en $59 bevestigt. | Feit (verschil), vermoeden (welke prijs klopt) | hoog | Een besluit van Thijs of de live prijs op Gumroad en Superhive. |
| 2 | De Pro-lijst belooft nieuwe functies: Figure from rig, Limit Rotation 30° tot 150°, herkenning van acht rig-namen, zes lichaamsdeel-presets en een gradenboog met jointlijst. De opdracht heeft alleen een akkoord voor Pro 1.0.2 (scharnier, pose-schuif, afstandscontrole). Voor 1.1 is in de tekst geen keuring of akkoord te zien. | Feit | hoog | Een keuring van Pro 1.1 en een bewijs dat de zip met deze functies bestaat. |
| 3 | Het commit zegt dat er een nieuwe Short-beschrijving "ter keuring" bij zit. In de diff staat alleen de README. | Feit | hoog | Het ontbrekende bestand of de tekst alsnog meesturen. |
| 4 | De link naar Superhive (`/products/click-joints-pro`) en de ankerlink `#pro-in-addition-to-everything-above` zijn niet bekeken. Het anker past wel bij de kop. | Vermoeden | midden | `curl` op de Superhive-pagina; de gerenderde README bekijken. |
| 5 | De regel "Measured in Blender, not print tested by us yet" past bij het ontwerp, want de handmatige printproef staat nog open. | Feit | hoog | n.v.t. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Bovenaan de README van de gratis versie staat nu een opvallende Pro-reclame. Het ontwerp eist een volledig werkende gratis versie zonder verwijzing naar de betaalde. De Pro-sectie stond er al, dus nieuw is vooral de opvallende plek. Het is niet te zien of extensions.blender.org deze README toont. | Vermoeden | midden | Regels 3.3, 3.10, 6.1 en ToS 6.2 van extensions.blender.org |
| 2 | Getallen en claims (30° tot 150°, acht herkende rigs, "200 mm of taller") hebben geen label GEZIEN, DERDEN of GOK en geen bron in de wijziging. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 3 | Geen persoonsgegevens, sleutels of wachtwoorden gezien. De Gumroad-link was er al. | Feit | hoog | Geen persoonsgegevens |
| 4 | Er zijn geen tests aangepast en het bestand is ruim onder 400 regels. De architectuur- en changelog-bestanden hoefden niet mee te veranderen, want alleen de README veranderde. | Feit | hoog | Tests, bestandsgrootte, architectuur.md |

## Deel C: zou een gebruiker het leuk en fijn vinden? (alles wat je kunt zien of spelen)
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | De Pro-lijst is concreter dan de oude: "one button reads your armature" zegt meteen wat je krijgt. De zin "$19 once" is duidelijk. | Niets nodig. | klein |
| 2 | De README bestaat alleen uit tekst. Het is mijn vermoeden dat een bezoeker de gradenboog of het scharnier sneller snapt met een plaatje of korte gif bovenaan. | Eén afbeelding van een rig-figuur met de gradenbogen erbij. | midden |
| 3 | De Pro-reclame staat vóór de gratis lijst. Dat kan wantrouwen wekken bij wie de gratis add-on komt bekijken. | De Pro-regel naar onder de Free-lijst verplaatsen. | klein |
| 4 | "Works best on figures of about 200 mm or taller" is eerlijk, maar staat los van de gratis grenzen van 5 tot 500 mm. | Eén zin die het verschil uitlegt. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet**
1. Prijs: README zegt $19 en $59, de opdracht zegt $12 en $45. Laat zien dat de nieuwe prijs besloten of live is, of zet de oude prijs terug (A1).
2. Pro 1.1: de beloofde functies hebben geen keuring of akkoord in de opdracht. Zet de README niet live voordat Pro 1.1 gekeurd is en de zip bestaat (A2).

**Kan**
- Stuur de nieuwe Short-beschrijving alsnog mee, want die ontbreekt in de diff (A3).
- Controleer de Superhive-link en het anker met `curl` en de gerenderde README (A4).
- Geef de getallen bij de rig-functies een label GEZIEN, DERDEN of GOK (B2).
- Controleer of extensions.blender.org deze README toont. Zo ja, haal de promo bovenaan weg of maak hem klein (B1).
- Plaatje bovenaan, Pro-regel lager en één zin over de 200 mm (C2 tot C4).

---
Automatische keurder, model `claude-sonnet-5-5`, 18056 tokens in, 4400 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
