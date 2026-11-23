# Keuring Betrouwbaarheid A, M1 (vangnet verlies bij kogelsneden), 23-11-2026 23:45 NL, automatische keurder
Wat ik keurde: commit 1945f46c0 (5aa27a8..1945f46), alleen de tekst van de wijziging in architectuur.md, redenen.py, rig.py, meet_diag.py en toetsen_mens.py
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | In `rig.py` geldt het vangnet "lost part of the model" (grens `VERLOREN_MAX` 6%) nu voor elke soort snede, niet meer alleen voor `HINGE`. Dat is wat de commitregel zegt. | Feit (uit de diff) | hoog | Niet nodig. |
| 2 | De nieuwe toets `CJ_HERKANS=3` laat de eerste snede van de linkerschouder zogenaamd 50% verliezen. Hij eist dat de knop een volgende plek neemt en de schouder toch plaatst (alleen in 5.x). De toets is logisch opgezet. | Vermoeden dat hij slaagt | midden | Een groene run van `CJ_HERKANS=3` in 5.2.3 en 5.3.0. Die staat niet in de aangeleverde tekst. |
| 3 | In de diff is geen workflow en geen runnerscript aangepast. De toets draait dus alleen als de e2e `CJ_HERKANS=3` al ergens meegeeft. architectuur.md zegt "in de e2e na `CJ_HERKANS=1`". | Vermoeden | midden | De workflow of het script dat `CJ_HERKANS=1` zet. Daar moet ook een regel met `=3` staan. |
| 4 | Een grens van 6% ligt dicht bij wat echte figuren verliezen. Eerder gemeten: Meshy-knight 5,6% met Exact-vereniging, 8 tot 9% met het voxel-omhulsel. Meer kogelgewrichten kunnen daardoor in "Skipped" belanden. | Vermoeden | laag | Een meetrun met `verloren_diag` (nieuw in `meet_diag.py`) op alle zeven figuren, vergeleken met de vorige run. |
| 5 | De tekst in `redenen.py` is eerlijker geworden. 4.5 wordt niet meer genoemd omdat het niet gemeten is; 5.2 wel. "The cut failed" heeft een eigen zin, en bij "blocked" staat geen versietip meer. | Feit (uit de tekst) | hoog | Niet nodig. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is een toets toegevoegd en geen bestaande toets versoepeld. De bestaande checks blijven staan. | Feit | hoog | Tests niet aangepast om te slagen: ok. |
| 2 | architectuur.md beschrijft de wijziging: vangnet voor kogels, toets `CJ_HERKANS=3`, nieuwe zinnen. | Feit | hoog | architectuur.md bijgewerkt: ok. |
| 3 | `redenen.py` zet "the cut failed" nu op een eigen zin en haalt de oude kern "no watertight parts" daaruit weg. architectuur.md zegt "toetsen zoeken erop". Een toets die op die kern zoekt bij een mislukte snede zou nu falen. In de diff is geen toets aangepast. | Vermoeden | midden | Oude kern van de zin blijft: de toetsen die `leesbaar` of "Skipped" lezen, in een run. |
| 4 | `rig.py` is veel langer dan ±400 regels (de wijziging staat rond regel 746). Het was al zo, de diff voegt er maar 4 regels aan toe. | Feit | hoog | Bestanden onder ±400 regels: bestaande schuld, niet nieuw. |
| 5 | Geen persoonsgegevens of sleutels gezien. Geen spelerstekst of beeld of geluid. | Feit | hoog | Persoonsgegevens, Steam: ok. |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | De lijst "Skipped" geeft nu per gewricht een zin met wat de koper kan doen. Dat is duidelijker dan een technische melding. Of het in Blender goed leest, zie ik niet. | Een schermafbeelding van de lijst met meerdere redenen onder elkaar, om te kijken of ze niet te veel op elkaar lijken. | klein |
| 2 | "Place it by hand a few mm along the bone" staat bij bijna elke reden. Na een paar keer is dat herhalend. | Eén keer boven de lijst uitleggen hoe je met de hand plaatst, en per gewricht alleen de reden noemen. | klein |
| 3 | Een gewricht dat om verlies wordt overgeslagen, laat de koper zonder schouder zitten. | Eerst automatisch een paar mm opschuiven proberen, zoals de knop al voor andere fouten doet. | midden |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Laat de groene run van `CJ_HERKANS=3` zien in 5.2.3 en 5.3.0, en bevestig dat de workflow hem aanroept (Deel A 2 en 3).
- Controleer dat geen bestaande toets meer zoekt op "no watertight parts" bij "the cut failed" (Deel B 3).
- Meet met `verloren_diag` of de grens van 6% op echte figuren niet te veel kogels overslaat (Deel A 4).
- Splits `rig.py` op als er een kans is (Deel B 4).
- Deel C 1 tot 3: bekijk de lijst "Skipped" met Daan of Iris en overweeg de verbeteringen.

---
Automatische keurder, model `claude-sonnet-5-5`, 26465 tokens in, 3970 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
