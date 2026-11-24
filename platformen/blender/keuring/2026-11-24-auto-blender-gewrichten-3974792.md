# Keuring blender-gewrichten, meting tekenpop (meet_rig.py), 24-11-2026, automatische keurder
Wat ik keurde: commit 397479288 (b3a448f..3974792), bestand `producten/blender-gewrichten/e2e/meet_rig.py`
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid (hoog/midden/laag) | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | De wijziging voegt alleen een figuurbouwer `bouw_tekenpop` toe aan het meetscript en zet hem in de lijst `bouwers`. De add-on zelf verandert niet, dus de akkoorden in `ontwerp.md` (0.1.1 en 1.0.2) blijven staan. | Feit | Hoog | De diff raakt alleen `e2e/meet_rig.py`. |
| 2 | Het commitbericht noemt een meting op tekenpop en kleding, 3 versies, 2 keer. De uitkomsten zitten niet in deze wijziging, dus ik kan niets zeggen over wat er gemeten is. | Feit | Hoog | Het uitvoerbestand (json) of het log van de run. |
| 3 | `import figuur_tekenpop` werkt alleen als `commercie/filmpjes/studio/` op het zoekpad staat. Dat staat niet in deze diff. | Vermoeden | Midden | Een groene run met `... meet_rig.py -- <zip> tekenpop <uit.json>` die de regel `MEET tekenpop gewrichten=<n> overgeslagen=<n>` toont. |
| 4 | `laad_tekenpop(220.0)` wordt uitgepakt als drie waarden (`_arm, ob, _p`). Of de functie dat teruggeeft, zie ik niet. | Vermoeden | Midden | Dezelfde run, of de functie in `figuur_tekenpop.py`. |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Er is geen test aangepast of versoepeld. Alleen een meetscript is uitgebreid. | Feit | Hoog | Tests niet aangepast om te slagen |
| 2 | Er komen ongeveer 10 regels bij. De bestandslengte zie ik niet, maar het bestand is minstens ruim 190 regels. Het blijft vermoedelijk onder de ±400. | Vermoeden | Midden | Bestanden onder ±400 regels |
| 3 | `architectuur.md` is niet bijgewerkt. Het gaat om een meetscript in `e2e/`, geen onderdeel van de add-on. Dat is acceptabel. | Feit | Midden | architectuur.md bijgewerkt |
| 4 | Er staan geen persoonsgegevens, sleutels of wachtwoorden in de diff. | Feit | Hoog | Geen persoonsgegevens |
| 5 | Het commitbericht noemt "3 versies, 2 keer" zonder cijfers. Zonder uitkomsten valt er geen GEZIEN/DERDEN/GOK-label te toetsen. | Feit | Hoog | Cijfers met GEZIEN/DERDEN/GOK |
| 6 | De docstring noemt de tekenpop "eigen werk". Dat kan ik niet nagaan. | Vermoeden | Midden | Geen AI-beeld of -geluid op Steam (niet van toepassing: dit is een Blender-product) |

## Deel C: zou een gebruiker het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite (klein/midden/groot) |
|---|---|---|---|
| 1 | Er is niets te zien of te spelen. De wijziging raakt de gebruiker niet. | Niet van toepassing | klein |
| 2 | Het is verstandig dat de meting ook het figuur van de omslag test, want daar kijken kopers naar. Zet de uitkomsten (bijvoorbeeld hoeveel gewrichten er slagen en hoeveel zijn overgeslagen) in een bestand of in `ontwerp.md`. | Uitkomsten vastleggen met een label GEZIEN | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
**Moet:** geen.

**Kan:**
- Zet de meetuitkomsten van deze run (tekenpop en kleding, 3 versies, 2 keer) in de repo, met een label GEZIEN, zodat te zien is wat er is gemeten.
- Laat de run bevestigen dat `figuur_tekenpop` importeerbaar is, of voeg het zoekpad expliciet toe in het script.
- Leg in één regel uit waarom Pro 1.2.3 wordt gemeten terwijl het akkoord in `ontwerp.md` over 1.0.2 gaat.

---
Automatische keurder, model `claude-sonnet-5-5`, 18042 tokens in, 2409 tokens uit (GEZIEN in het antwoord van de API). Deze keurder leest alleen tekst; beeld en speelplezier keuren Daan en Iris nog steeds.
