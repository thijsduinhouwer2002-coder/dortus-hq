# Keuring Hats licht en klein leven in het hol, 25 nov 2026, Daan
Wat ik keurde: commit 71145c5 (issue #97, keurvraag #106), `producten/steam-hol/bewijs-mooi/` (film 30 s ware grootte, voor-en-na, beeldvellen). Zelf beelden uit de film gehaald op 2,4 s, 12,4 s en 25,4 s op 1024 x 120 en bekeken met Read.
Akkoord: nee (licht ja, klein leven nee)

## Deel A: doet het wat beloofd is?
| # | Bevinding | Feit of vermoeden | Zekerheid | Wat het zou bevestigen of weerleggen |
|---|---|---|---|---|
| A1 | Licht: gang donkerder naar rechts, gangen donkerder dan aarde, schatkamer warm. Werkt en geeft diepte op 120 px. | feit (GEZIEN) | hoog | |
| A2 | Warme gloed om de fakkel bij de ingang: op ware grootte zie ik geen plas licht om de vlam, alleen dat de linkerkant van de gang iets lichter is dan rechts. De gloed om het goud zie je wel. | feit (GEZIEN, frame 2,4 s) | hoog | Een beeld met en zonder alleen de fakkelgloed |
| A3 | Klein leven komt om de 5 tot 15 s, nooit twee tegelijk (toets: 44 in 10 min, gaten 5,1 tot 14,8 s). | feit volgens toets | hoog | |
| A4 | Windows-run 45699029288 en duurtest 45699117410 liepen nog tijdens mijn keuring (in_progress). | feit | hoog | Groene uitslag van beide |

## Deel B: houdt het zich aan onze regels?
| # | Bevinding | Feit of vermoeden | Zekerheid | Regel |
|---|---|---|---|---|
| B1 | CPU +1 procent over twee paren, met methode en grens 10 erbij (GEZIEN door Olaf). Gebakken kaart in het vaste beeld: goede keuze. | feit volgens bestand | midden | |
| B2 | `hol_lagen.gd` afgesplitst zodat `strook.gd` onder 400 regels blijft. Geen tekst voor spelers, geen geluid, geen AI-beeld. | feit | hoog | |

## Deel C: zou een speler het leuk en fijn vinden?
| # | Bevinding | Wat het beter maakt | Moeite |
|---|---|---|---|
| C1 | **Worm en mot passen niet bij de rest.** De worm is een plat roze blokje met een zwart streepje, de mot een wit streepje van 2 px. Al het andere (Gloop, helden, kristal, laars) is rond, met schaduw en rand. Op ware grootte lezen ze als een kapotte pixel, niet als een beestje. Dit is precies het "goedkope" gevoel waar Gemini over viel. | Worm en mot tekenen in de huisstijl: ronde vorm, één tint donkerder voor schaduw, donkere rand zoals bij Gloop, minstens 5 tot 6 px hoog op 120 px, en de worm met een oogje. De kunst van Hats is van Mila: laat haar de twee figuurtjes tekenen, Olaf zet ze erin. | midden |
| C2 | Kruimels: op ware grootte niet te zien, op 4x een paar puntjes voor het kristal. | Weg, of groter met een klein stofwolkje op de vloer. Liever weg: drie goede dingen zijn beter dan vier waarvan één niemand ziet. | klein |
| C3 | Stofjes in het fakkellicht: werkt, rustig en warm. | | |
| C4 | Jouw vraag 1, kristal, putten en laars fel in de donkere gang: dat leest als opvallen, niet als geplakt. Ze zijn dingen om te pakken of te vermijden, dus ze mogen eruit springen. Houden. | | |
| C5 | Jouw vraag 3, donker op 120 px: de zwaarte is goed. Wat mist is contrast: de lichte plek om de fakkel. Nu is het van links naar rechts een egale verloop in plaats van "warm eiland in het donker" zoals bij Rusty's Retirement (lat `hats-tempo.md`). | Rond de fakkel een zachte ronde lichtplas van ±2 tegels straal, duidelijk lichter en warmer dan de gang 3 tegels verder. | klein |

## Deel C: is het goed genoeg?
| Vraag | Cijfer | Waarom, en waarmee vergeleken |
|---|---|---|
| Ziet het er top uit, op het niveau van de beste in de winkel? | 7 | Het licht maakt het hol beter dan het was (voor en na naast elkaar). Naast Rusty's Retirement (https://store.steampowered.com/app/2666510/, warme lichtplekken, alle beestjes in één stijl) vallen worm en mot uit de toon en mist de fakkel zijn lichtplas. |
| Zou ik het zelf kopen of bekijken op basis van dit? | 7 | Het licht ja; de streepjes zou ik als fout lezen. |
| Zou Thijs er trots op zijn? | 7 | Op het licht wel. Op een roze blokje dat een worm moet zijn niet. |

## Moet (blokkeert akkoord)
1. **Worm en mot in de huisstijl** (C1): rond, schaduw, rand, minstens 5 tot 6 px hoog op 120 px. Tekening van Mila. Lukt dat niet in de volgende run: zet worm en mot uit en laat alleen stofjes en (als ze zichtbaar zijn) kruimels draaien, dan keur ik het licht los.
2. **Kruimels weg of zichtbaar** (C2).
3. **Lichtplas om de fakkel** die je op ware grootte ziet (A2, C5).
4. Windows-run en duurtest groen (A4).

## Kan (mag later)
1. Een kleine eigen vlam of kaars in de schatkamer, zodat de mot ook daar kan fladderen.

Nakeuring: alleen deze vier punten, met een nieuw beeldvel op ware grootte en op 4x.
