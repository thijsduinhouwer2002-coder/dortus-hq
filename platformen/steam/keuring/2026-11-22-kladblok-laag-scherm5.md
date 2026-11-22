# Keuring kladblok=laag in steam-hol-winkel.yml, 22 nov 2026, Daan
Wat ik keurde: commit e2e969d (Olaf), alleen `.github/workflows/steam-hol-winkel.yml`. Beeld `bureaublad-held-2-b.png` uit run 44970504844 (tak schermen, map `steam-hol/winkel-1920-week-160-zaad1795340417-run44970504844-werkvenster-run44970504844-scherm1920/bureaublad/`), met de API gehaald en met eigen ogen bekeken.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | `vol` en `smal` blijven gelijk: laag neemt de breedte en letters van smal over (`-in @('smal','laag')`) en zet alleen de hoogte op min(oud, 375 maal $sf), dus 562 bij 1920. | feit | hoog | diff |
| 2 | held-2-b is 1920 x 1080 (PIL). Kladblok van y ±25 tot ±578, de laatste regel "ask about the printer contract" staat er net boven, geen regel valt weg. Tussen venster en strook ±290 px donker bureaublad. Recycle Bin vrij. | feit | hoog | beeld |
| 3 | Begroting klopt: kolommen 2.800, 2.705, 3.190 en rijtotalen tellen op tot 8.695 (zelf nagerekend). | feit | hoog | beeld |
| 4 | De map van laag krijgt geen eigen achtervoegsel (alleen `smal` krijgt `-smal`, regel 436). Een laag-map ziet er dus uit als een vol-map. Overschrijven gebeurt niet, want het run-nummer staat in de naam. | feit | hoog | regel 436 |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Spelcode niet geraakt (spel bevroren). Nepbegroting zonder namen of persoonsgegevens. Op main vóór keuring met reden (opdrachten draaien alleen op main); standaard ongewijzigd. | feit | hoog | harde regel 2, 5 |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Beter dan smal: er is geen groot wit vlak meer, het oog zakt via het donkere bureaublad naar de kleurige strook. Het beeld zegt nu in één blik "je werkt boven, je hol leeft onder". Mijn keus voor scherm 5: laag. | Sanne kiest; ik raad laag aan. | geen |
| 2 | Onderin Kladblok staat een lege horizontale schuifbalk; klein, maar het is het enige rommelige stukje. | Word Wrap aan of venster 10 px breder; alleen als het gratis kan. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.
Kan 1 (Olaf): map van laag `-laag` geven, net als `-smal`, zodat je het beeld later terugvindt.
Kan 2 (Olaf): horizontale schuifbalk in Kladblok weg (Word Wrap), alleen als het klein is.
