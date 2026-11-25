# Keuring blender-gewrichten toets Hinge placed, 25-11-2026, automatische keurder
Wat ik keurde: commit c393c55a9, bestand `producten/blender-gewrichten/e2e/toetsen_paneel.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De commit zegt dat een Blender-object geen `update()` heeft. De wijziging vervangt `d.update({...})` door een lus met `d[k] = v`. Dat zet dezelfde zeven eigenschappen. | Feit (uit de diff) | Hoog | Niet nodig. |
| 2 | Dat een ID-object (`bpy.types.Object`) geen `update()` heeft, klopt volgens mijn kennis van de Blender-API. Alleen het IDPropertyGroup-object of een gewone dict heeft die methode. | Vermoeden | Midden | Een groene e2e-run van de toets met "Hinge placed" in het log. |
| 3 | De wijziging raakt alleen het testbestand, dus de add-on en wat de gebruiker ziet blijven gelijk. De opdracht (ontwerp.md) gaat niet over deze toets. De titel "Pro 1.2.9 (issue 70)" past bij de architectuur, die de paneellijsten sinds 1.2.9 noemt. | Feit | Hoog | Niet nodig. |
| 4 | De commit noemt een nieuw versienummer, maar de diff bevat geen versiewijziging. Een uitgave volgt dus niet uit deze commit. | Feit | Midden | Het manifest op de tak: staat daar al 1.2.9? |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | De toets is niet verzwakt om te slagen. De waarden en de latere controles (`plek(log, "label", "Hinge placed")`) blijven gelijk. De wijziging herstelt een fout in de opzet van de testdata. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Het bestand is maar een paar regels veranderd. De totale lengte kan ik niet zien, want het bestand is niet meegestuurd. | Vermoeden | Laag | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Dat hoeft ook niet, want het gedrag verandert niet. | Feit | Hoog | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of cijfers zonder label in de wijziging. Er is geen spelerstekst, beeld of geluid. | Feit | Hoog | Persoonsgegevens, cijfers, Steam |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Niet te beoordelen. De wijziging zit alleen in een test en raakt niets wat een gebruiker ziet of speelt. | Niet van toepassing | klein |

## Deel C: is het goed genoeg?
Niet van toepassing. Er is geen beeld, winkeltekst, spel of site veranderd, dus de cijfers en de blinde test gelden hier niet.

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Controleer in de e2e-run dat de toets "Hinge placed" nu groen wordt. Dat kan ik uit de tekst niet zien. De diff zelf ziet er goed uit.
- Zet de regel in de lus op meerdere regels. De opmerking staat nu aan het eind van een lange regel, wat slecht leest.
- Als `toetsen_paneel.py` richting 400 regels gaat, splits het dan.

---
Automatische keurder, model `claude-sonnet-5-5`, 18086 tokens in, 1463 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
