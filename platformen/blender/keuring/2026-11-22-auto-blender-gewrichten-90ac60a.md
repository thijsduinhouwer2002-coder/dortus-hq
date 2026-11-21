# Keuring Pro-link in direct-zip, 22-11-2026, automatische keurder
Wat ik keurde: commit d8980241e (producten/blender-gewrichten/e2e/direct/direct.py en e2e/test_direct.py), gevraagd bereik 3d5b537..90ac60a
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `URL` in direct.py is nu `https://dortus.com/click-joints/?from=addon#pro`, zoals de commit zegt. | Feit | hoog | Staat zo in de diff. |
| 2 | De knop opent de link alleen via `wm.url_open` na een klik van de gebruiker. Dat staat in de kop van het bestand en de wijziging raakt dat niet. | Feit | midden | Alleen de URL-regel is gewijzigd. De rest van het bestand zag ik niet. |
| 3 | De commit zegt dat de uitgave de direct-zip weigert en dat indienen.md twee zips beschrijft. Beide bestanden zitten niet in deze diff. | Vermoeden | laag | De workflow `click-joints-uitgave.yml` en indienen.md in de rest van het bereik, of een test die de weigering laat falen. |
| 4 | Of het anker `#pro` op dortus.com/click-joints/ bestaat, kan ik niet zien. | Vermoeden | laag | `curl` op de pagina en zoeken naar `id="pro"`, of Playwright die naar het anker scrolt. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De test is aangepast aan de nieuwe URL. De URL is bewust veranderd en test en code zeggen nu hetzelfde, dus de test is niet aangepast om te slagen. | Feit | hoog | Tests niet aanpassen om te slagen |
| 2 | Twee kleine wijzigingen, geen bestand dicht bij 400 regels. | Feit | midden | Bestandsgrootte |
| 3 | architectuur.md is niet bijgewerkt. Het deel dat ik zag noemt de direct-build niet, dus dat hoeft hier misschien ook niet. | Vermoeden | laag | architectuur.md bijgewerkt |
| 4 | De direct-zip met Pro-link mag niet op extensions.blender.org (regels 3.3, 3.10, 6.1 uit het ontwerp). Dat de uitgave hem weigert, zit niet in deze diff (zie A3). | Vermoeden | midden | Gratis versie zonder verwijzing naar betaald |
| 5 | Geen persoonsgegevens, sleutels of wachtwoorden. `?from=addon` bevat alleen een bronnaam. | Feit | hoog | Geen persoonsgegevens |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Een klik op de knop brengt de koper nu bij de Pro-kop in plaats van bovenaan de pagina. Dat is fijner, mits het anker werkt. | Controleer op de live pagina, ook op de telefoon, dat `#pro` goed scrolt en de kop niet achter een vaste balk valt. | klein |
| 2 | Ik kan het venster en de knop niet zien. Hoe het voelt in Blender beoordeel ik niet. | Iris of Daan bekijkt een schermafbeelding van het slotvenster. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer dat `#pro` op de productpagina bestaat (A4, C1).
- Laat de test van de uitgave-weigering (A3, B4) zien in een van de andere commits. Zo ja, dan is het punt weg. Zo nee, dan is het een moet bij de volgende keuring.
- Het bereik 3d5b537..90ac60a noemt alleen commit d8980241e. Als er meer commits in zitten, heb ik die niet gezien.

---
Automatische keurder, model `claude-sonnet-5-5`, 17810 tokens in, 2362 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
