# Ebb: zichtbaarheid van alle 25 dieren, gemeten op echte schermbeelden (Gijs, run 74, 12 nov 2026)

Nachtlijst punt 1 (besluit Thijs, hoofdchat 12 nov 22:20 en 22:40 NL). Geen frisse keurder; gemeten, en daarna zelf alle 25 dieren bekeken.

**Uitkomst in het kort.** Op de bladen zijn alle 25 dieren bij dag en bij nacht te zien, op de FR255 en op de fenix 8. De meting geeft in 191 van de 200 vakjes 65 of meer. In 9 vakjes meet hij lager. Die negen heb ik stuk voor stuk bekeken: het dier is er te zien, en in acht van de negen ligt het aan de meting, niet aan het dier (uitleg onderaan). De norm is dus NIET voor alle 25 dieren met het getal alleen gehaald; het bewijs is getal plus eigen oog. De code is niet veranderd na nachtregel v1.4.

## Welke code en welke beelden

- Code: nachtregel v1.4 van proef73 5680d2a7 (gelijk aan de bouwtak e40269e1 op de kijkproef na).
- Vijf proeftakken met elk andere dieren op de plekken van de sessiescènes, alleen `Scenes.mc` (de rij `wie`) en `proef-scenes.txt` verschillen: `claude/garmin-2026-11-12-proef74a` tot `proef74e`. Plaatjesruns 43315472109 (a), 43315475655 (b), 43315480366 (c), 43315483088 (d), 43315487820 (e), alle vijf `success`.
- Per dier vier scènes: inademen en inhouden, bij dag en bij nacht. Twee horloges: FR255 (MIP, 260 px) en fenix 8 47 mm (AMOLED, 454 px). Samen 200 beelden.
- Ronde b kwam niet op de tak `schermen` (vijf runs schreven tegelijk naar dezelfde map en de vijfde verloor); die beelden komen uit de artefacten van run 43315475655.

## Bladen (zelf kijken)

`ontwerp/garmin/ebb-alle25-run74-fr255-nacht.png`, `-fr255-dag.png`, `-fenix847mm-nacht.png`, `-fenix847mm-dag.png`. Per dier links inademen, rechts inhouden. De twee nachtbladen heb ik helemaal bekeken; van de dagbladen alleen de vakjes die laag maten.

## De meting

Script: `platformen/garmin/meet_dieren_beeld.py` (uitleg bovenin). Getallen: `meting-dieren-run74-fr255.csv` en `-fenix847mm.csv`.

Het getal is: **welk deel van het dier (procent van zijn oppervlak) steekt duidelijk af tegen de achtergrond eromheen** (kleurverschil 20 of meer in Lab, op een 3x3 vervaagd beeld). Het silhouet van het dier komt uit het dag- en het nachtbeeld samen, zodat een lijf dat bij nacht wegvalt wel meetelt.

**Norm: 65.** Zo gekozen: ik heb dezelfde meting losgelaten op de oude nachtbeelden van run 72 (c6761f19, plaatjesrun 43295837436), waar de keurder zei dat de orka en de narwal wegvielen. Die maten daar 43 tot 64 (orka 49, 64, 43, 60; narwal 55, 46). Met v1.4 meten dezelfde scènes 66 tot 90. Alles wat als "valt weg" beoordeeld was zat dus onder 65. Eerlijk: de norm is achteraf gekozen op die oude gevallen, en de zwaardvis, die de keurder van run 72 ook zwak vond, mat toen al 78 tot 83. De meting vangt dus niet alles wat een mens zwak vindt.

## Tabel (procent van het dier dat afsteekt; vet is onder 65)

| nr | dier | FR255 dag in | FR255 dag hold | FR255 nacht in | FR255 nacht hold | fenix 8 dag in | fenix 8 dag hold | fenix 8 nacht in | fenix 8 nacht hold | laagste |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Fish | 97 | 77 | 97 | 95 | 98 | 78 | 88 | 89 | 77 |
| 1 | Shrimp | 93 | 95 | 96 | 91 | 98 | 97 | 84 | 84 | 84 |
| 2 | Jellyfish | 97 | 95 | 96 | 92 | 96 | 95 | 84 | 89 | 84 |
| 3 | Turtle | 89 | 92 | 87 | 91 | 96 | 89 | 82 | 88 | 82 |
| 4 | Crab | 75 | 72 | 69 | 62 | 91 | 83 | 80 | 69 | **62** |
| 5 | Seahorse | 94 | 94 | 96 | 92 | 98 | 90 | 85 | 93 | 85 |
| 6 | Starfish | 90 | 74 | 94 | 93 | 96 | 75 | 87 | 85 | 74 |
| 7 | Clownfish | 90 | 96 | 90 | 94 | 98 | 98 | 82 | 85 | 82 |
| 8 | Pufferfish | 96 | 85 | 94 | 92 | 98 | 83 | 86 | 96 | 83 |
| 9 | Octopus | 96 | 92 | 96 | 95 | 94 | 95 | 89 | 89 | 89 |
| 10 | Eel | 96 | 94 | 95 | 90 | 98 | 96 | 80 | 82 | 80 |
| 11 | Ray | 92 | 85 | 93 | 87 | 97 | 77 | 87 | 29 | **29** |
| 12 | Seal | 88 | 94 | 80 | 88 | 96 | 95 | 61 | 81 | **61** |
| 13 | Dolphin | 74 | 85 | 97 | 91 | 69 | 96 | 88 | 84 | 69 |
| 14 | Swordfish | 87 | 91 | 89 | 90 | 93 | 97 | 80 | 80 | 80 |
| 15 | Sea otter | 94 | 91 | 94 | 94 | 97 | 90 | 83 | 85 | 83 |
| 16 | Manta | 89 | 94 | 64 | 91 | 91 | 96 | 46 | 89 | **46** |
| 17 | Shark | 96 | 94 | 94 | 89 | 95 | 94 | 83 | 87 | 83 |
| 18 | Sunfish | 81 | 88 | 93 | 93 | 43 | 96 | 91 | 91 | **43** |
| 19 | Orca | 92 | 94 | 82 | 95 | 94 | 93 | 68 | 91 | 68 |
| 20 | Narwhal | 59 | 60 | 88 | 94 | 30 | 96 | 90 | 86 | **30** |
| 21 | Giant squid | 94 | 84 | 96 | 94 | 96 | 95 | 89 | 88 | 84 |
| 22 | Lobster | 96 | 93 | 93 | 85 | 97 | 97 | 75 | 85 | 75 |
| 23 | Whale | 83 | 94 | 96 | 94 | 82 | 96 | 85 | 86 | 82 |
| 24 | Sea cucumber | 96 | 95 | 94 | 93 | 98 | 97 | 85 | 87 | 85 |

## De negen vakjes onder 65, elk bekeken

| dier | vakje | getal | wat ik zie | oorzaak |
|---|---|---|---|---|
| Ray | fenix 8, nacht, inhouden | 29 | goed te zien, zandkleurig lijf tegen donker water | de meting neemt het zand onderin het venster als achtergrond, en de rog heeft de kleur van het zand; hij zwemt er boven, niet ertegen |
| Narwhal | fenix 8, dag, inademen | 30 | goed te zien, paarsblauw lijf met stippen | witte buik en witte stickerrand tegen het witte schuim van de golf; het silhouet pakt ook een stuk schuim mee |
| Narwhal | FR255, dag, inademen en inhouden | 59 en 60 | goed te zien, zwarte omtrek | witte buik tegen de lichte luchtband (inademen) en tegen het lichte zand (inhouden); de buik is een derde van het dier |
| Sunfish | fenix 8, dag, inademen | 43 | te zien, met witte rand; het lila lijf lijkt wel op de lila lucht erachter | dit is deels echt: lijf AAAAFF tegen een lila lucht. Geen wegvallen. Naar lijst-1.1 |
| Manta | fenix 8 en FR255, nacht, inademen | 46 en 64 | goed te zien, lichtgrijs tegen de donkere lucht | de grijze golfrand loopt door het venster en telt als achtergrond; de manta heeft bijna die kleur |
| Seal | fenix 8, nacht, inademen | 61 | goed te zien | zelfde als de manta: grijs lijf, grijze golfrand |
| Crab | FR255, nacht, inhouden | 62 | goed te zien, rood | de krab heeft in zijn eigen wereld een reddingsboei en een anemoon; het silhouet pakt die mee en raakt de rand van het venster |

De orka, waar de keurders van run 73 over vielen, meet 82 en 95 op de FR255 bij nacht en 68 en 91 op de fenix 8 bij nacht. 68 (inademen, fenix 8) is het laagste echte getal van een dier dat eerder wegviel. Hij is klein, maar hij is er.

## Wat deze meting niet bewijst (eerlijk)

- Het silhouet vindt bij inademen niet het hele dier: wat onder water zit en dunne delen (zwaard, staartpunten) vallen er soms af. Het getal gaat dan over het deel boven water.
- De achtergrond is geschat uit de rand van het venster. Bij een golfrand, schuim of zand in het venster valt dat verkeerd uit voor dieren met die kleur (zie de tabel hierboven). Altijd naar de strenge kant: het getal wordt lager, niet hoger.
- Herkenbaarheid (lijkt het op een orka) meet dit niet. Alleen of het dier afsteekt.
- Alleen FR255 en fenix 8 47 mm. De venu 3s is wel gebouwd in deze rondes maar niet gemeten en niet bekeken.
- Uitademen is niet in beeld gebracht (het dier staat dan tussen de plek van inademen en inhouden).

## Besluit

Geen wijziging aan de dieren of de nachtregel. Waarom: op de echte beelden valt geen van de 25 dieren weg, bij dag niet en bij nacht niet; de lage getallen zijn op één na fouten van het meetscript. De maanvis bij dag op de fenix 8 en de wensen voor de orka (groter, meer wit) staan op `platformen/garmin/lijst-1.1.md`. Is de hoofdchat het niet eens met "getal plus eigen oog": de twee nachtbladen zijn het snelst te beoordelen.
