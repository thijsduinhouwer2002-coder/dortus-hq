# Keuring kladblok=smal in steam-hol-winkel.yml, 22 nov 2026, Daan
Wat ik keurde: commit b56513b (Olaf), alleen `.github/workflows/steam-hol-winkel.yml`. Beeld `bureaublad-held-2-b.png` uit run 44961090666 (tak schermen, map `...-scherm1920-smal/bureaublad/`), met de API gehaald en met eigen ogen bekeken.
Akkoord: ja

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| 1 | Standaard `vol` verandert niets: het register wordt alleen gezet bij werkvenster=1 en smal, breedte blijft $wg.Width - $wx - $wr, mapnaam zonder `-smal`. | feit | hoog | diff |
| 2 | Smal: breedte min(vol, 760 maal $sf), dus 1140 bij 1920; letters 110 maal $sf min 5 tienden pt (16 pt bij 1920, 10,5 bij 1280), Consolas; eigen map met `-smal`. | feit | hoog | diff |
| 3 | held-2-b is 1920 x 1080 (PIL). Kladblok loopt van x ±143 tot ±1267, rechts ±650 px donker bureaublad. Tekst groot en goed leesbaar, begroting klopt (rijen tellen op tot de totalen). Recycle Bin vrij, strook met held, troon, Gloop en melding onderaan. | feit | hoog | beeld |
| 4 | Register-instelling blijft niet hangen voor latere runs: elke run is een schone Windows-machine. | vermoeden | middel | GitHub-runner is per job nieuw |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| 1 | Spelcode niet geraakt. Nepbegroting zonder echte namen of persoonsgegevens. Op main gezet vóór keuring met reden (opdrachten draaien alleen op main), standaard ongewijzigd, dus geen risico. | feit | hoog | harde regel 2, 5 |

## Deel C: zou een koper het fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| 1 | Veel beter dan vol: het leest nu als "werk boven, spel onder". Maar de onderste helft van Kladblok (y ±520 tot ±810) is nog leeg wit, het grootste lichte vlak in het beeld trekt het oog weg van het hol. | Kladblok lager maken (bijvoorbeeld hoogte tot net onder de laatste regel, ±560 px bij 1920) zodat er donker bureaublad tussen venster en strook zit, of de begroting een paar regels langer. | klein |
| 2 | De melding rechtsonder ("Trick Lid ready: click the pit") raakt bijna de rechterrand. | Alleen kijken of dat in het spel zo hoort; geen werk voor de opname. | klein |

## Moet (blokkeert akkoord) / Kan (mag later)
Moet: geen.
Kan 1 (Olaf en Sanne): Kladblok minder hoog, zodat er geen leeg wit vlak meer is.
Kan 2: melding rechtsonder bekijken op de rand.
