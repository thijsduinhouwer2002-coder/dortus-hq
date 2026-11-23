# Keuring blender-gewrichten (CI-meting heup), 23-11-2026 16:32 NL, automatische keurder
Wat ik keurde: commit fae434cef (reeks 8e07654..fae434c), bestand `producten/blender-gewrichten/proeven/ci-verschil/diag-beweeg.patch`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging is één nieuw patchbestand onder `proeven/ci-verschil/`. Er is geen bestand in `click_joints/` gewijzigd, dus de goedgekeurde add-on (0.1.1 en 1.0.2) blijft zoals hij was. | Feit (lijst gewijzigde bestanden) | hoog | Een `git diff` tegen 1d0c54c die alleen deze map toont. |
| 2 | De patch voegt alleen `print`-regels en een lijst `DIAG` toe aan de beweegproef. De enige logica die verandert is dat bij `hit` het teken en de afstand `dd` worden bewaard. De terugkeer `True` bij `dd < -1e-9` is gelijk aan het origineel. | Feit (diff gelezen) | midden | Een run met de patch toegepast waarin `bereik` en `buig_graden` gelijk blijven aan een run zonder. |
| 3 | De patch noemt geen doelbestand en heeft geen contextregels (gewoon `diff`-formaat met regelnummers). Uit de tekst kan ik niet zien op welk bestand hij hoort en of hij schoon past. | Vermoeden (waarschijnlijk `beweeg.py`) | laag | Een proefrun in CI die laat zien dat de patch past en de DIAG-regels in het log komen. |
| 4 | De commit zegt "CI 8 tegen lokaal 9", maar de meetuitkomst staat niet in de wijziging. Het is dus een instrument zonder uitslag. | Feit | hoog | Het CI-log met de regels DIAGMESH, DIAGBEWEEG en DIAGGROOT. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Geen testbestand aangepast. Er is niets dat een test laat slagen. | Feit | hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is 27 regels, ver onder ±400. | Feit | hoog | Bestandsgrootte |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft ook niet, want de add-on is niet veranderd. | Feit | hoog | architectuur.md bijgewerkt |
| 4 | In het patchbestand staan geen persoonsgegevens, sleutels of wachtwoorden. | Feit | hoog | Geen persoonsgegevens |
| 5 | De uitspraak "CI 8 tegen lokaal 9" in de commitbericht heeft geen label (GEZIEN, DERDEN of GOK). Het is een meting door de maker, dus waarschijnlijk GEZIEN, maar de bron (runnummer) ontbreekt. | Feit | midden | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De patch staat in `proeven/` en niet in de add-onmap. Dat de patch niet in de zip komt, is een vermoeden: `toets_zips.py` is niet getoond. | Vermoeden | midden | Gratis zip byte voor byte gelijk (toets_zips) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Niets te zien of te spelen. Voor de gebruiker verandert niets. | Niet van toepassing. | klein |
| 2 | Als het verschil CI 8 tegen lokaal 9 door de patch een echte oorzaak krijgt, kan een gebruiker op een andere machine een ander bereik zien. Dat zou het vertrouwen in "Bends ±N°" raken. | De oorzaak vinden en vastleggen, daarna in een aparte commit oplossen met een test. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet in de commit of in een README naast de patch op welk bestand en welke versie de patch hoort (bijvoorbeeld `beweeg.py` op 1d0c54c). Zet er ook bij hoe je hem toepast.
- Leg de uitslag vast (runnummer en de DIAG-regels), met label GEZIEN, zodat "CI 8 tegen lokaal 9" naspeurbaar is.
- Controleer dat `proeven/` buiten de gratis en betaalde zip blijft (`toets_zips`).
- Voeg de diagnose pas toe aan de add-on als de oorzaak bekend is. Voeg dan ook een test toe die het verschil tussen CI en lokaal dekt.

---
Automatische keurder, model `claude-sonnet-5-5`, 18011 tokens in, 2407 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
