# Steam-header v2 (Mila, 27 nov 2026, issue #30)

Bestanden: `header-920x430.png` (de header), `header-460x215.png` (klein, om te kijken), `rechts-2x.png` (Gloop en de vallende held op 2x), `voor-na.png` (v1 boven, v2 onder).

Maken: `<venv>/bin/python header_v2.py r.png 1840 860 28` (bpy 5.2.4, ±2,5 min op 2 kernen), dan `python3 samenstellen.py r.png header-920x430.png`. Render op 2x en verkleind: scherp zonder opschalen.

## Het idee (keuzes van Sanne in #30)
- Bovenaan een rustig bureaublad (lucht, wolken, heuvels), onderaan een taakbalk met het icoon van Hats; daartussen het hol als kelder, in de look van het speelscherm dat blind won. Ondertitel als concept: "Your taskbar has a basement now" (Thijs schrijft de echte tekst voor live).
- Grote figuur: Gloop met zijn hoedentoren (helm, kroon, heksenhoed) op het goud, in een kamer van licht metselwerk.
- De grap: een held valt kop eerst door een gat in het gras de kamer in, zijn rode pet vliegt los in de lucht. In de gang loopt de volgende ridder nietsvermoedend naar de kamer.
- Feller en warmer dan v1, minder muur: lucht blauw, gras fel groen, aarde terracotta, kamer zandsteen, Gloop mint, held paars, ridder blauw.

## Eigen toets (GEZIEN met Read, op 920, 460 en 2x)
- Titel en ondertitel lezen op 460. Gloop, pet en vallende held lezen op 460; de laarzen omhoog zie je op 2x goed.
- Frisse kijker (een losse Claude, blind tussen de drie concurrenten op 460, ronde v4): plek 3 van 4, na Spirit City en Rusty, vóór Desktop Defender. Letterlijk: "The taskbar hook is the only image that says 'lives on your desktop', but the scene is cramped and busy at this size." Tip: figuren groter, minder losse dingetjes, ondertitel groter. Daarna gedaan: Gloop ±10% en de held ±15% groter, de helft minder kiezels, ondertitel 25 naar 29. Dit is geen blinde test volgens regel 9.
- Blinde test `organisatie/blindtest/sets/hats-header-v2.json`: run 45914452636 gaf geen uitslag, de ChatGPT-sleutel heeft geen tegoed (HTTP 429, GEZIEN in het log). Opnieuw starten zodra er tegoed is (skill `actions`, set `hats-header-v2`).

## Ronde 3 (27 nov ±03:00 NL, na keuring Daan #236: nee, 6 van 10)
- **M1 vallende held:** niet meer kop eerst (het omgekeerde gezicht las als een los ei), maar voeten eerst met armen omhoog van schrik, iets schuin, gezicht rechtop. Eén silhouet; hij zakt net uit het gat. Valstreepjes erboven getekend in Pillow (in Blender lazen ze als stokjes).
- **M2 gat in het gras:** breder en donker van binnen, met overhangende sprieten aan de randen en kluitjes die meevallen (licht op de donkere schacht, donker op het metselwerk).
- **M3 bureaublad:** taakbalk van 30 naar 40 px, knoppen groter, Hats-knop groter en opgelicht als open app, startknop met vier vakjes, en een witte muispijl in de lucht.
- **Kan:** gang hoger en ridder groter (minder lege aarde links midden, bot weg), Gloop één mond (losse tand weg), zachter sleutellicht (vlak 10 naar 18).
- Na een frisse kijker (een losse Claude, blind op 460, telt niet als test: plek 3 van 4, tip "logo groter, minder rommel"): titel ±22% groter, HATS nu ±38% van de breedte.
- Bekeken met Read op 920, 460 en 2x (`rechts-2x.png`). Voor en na: `voor-na.png` (v2 boven, v3 onder).
- Blinde test: set `hats-header-v2.json` wijst nu naar v3. ChatGPT had om 01:19 nog geen tegoed (run 45921830896, HTTP 429, GEZIEN), dus een uitslag komt pas als er weer tegoed is.

## Ronde 4 (27 nov ±05:30 NL, kan-punten 1 en 2 van Daan #243)
- **Gat:** geen zwart vak meer maar een rafelige trechter (golvende wanden, bovenaan rond uitlopend, geen rechte hoeken). Langs beide wanden lichte kluiten aarde, drie wortels hangen van boven het donker in, en de verre rand is gras met sprieten die naar binnen hangen. De donkere achterkant loopt onderaan mee met de boog van de kamer.
- **Valstreepjes:** drie in plaats van vier, elk een andere lengte (30, 18, 12 px), dunner, spits naar boven en iets schuin mee met de val.
- De rest van het beeld is gelijk aan v3 (eigen dobbelsteen voor het gat, zodat kiezels en sprieten niet verschuiven).
- Bekeken met Read op 920, 460 en 2x. Voor en na van het gat: `voor-na.png` (v3 links, v4 rechts).
- Set `hats-header-v2.json` wijst nu naar v4 (`?v=4`); de push start de test vanzelf. Geen tegoed bij de rechters = geen uitslag, dan opnieuw starten zodra er tegoed is.

## Ronde 5 (27 nov ±07:15 NL, eigen kijken terwijl de blinde test op tegoed wacht)
- **Pet:** de rode pet in de lucht las op 460 als rode lippen (wit band als tanden, koepel van opzij). Nu koepel boven, witte band als rand en de klep steekt rechts opzij (`PETK` 15, `PETD` -30): op 920 en 460 een pet, op 2x ook. Gekozen uit zes standen die ik los renderde.
- Rest gelijk aan v4. Voor en na van de pet: `voor-na.png` (v4 links, v5 rechts). Bekeken met Read op 920, 460 en 2x.
- Set `hats-header-v2.json` wijst nu naar v5 (`?v=5`).

## Blinde test v5 (27 nov 10:50 NL): NIET GESLAAGD, Gemini gemiddeld plek 3,0
Uitslag: `organisatie/blindtest/uitslag/hats-header-v2-2026-11-27-1050.md` (GEZIEN). Beide rondes plek 3 van 4 (eerste keus Spirit City en Rusty). Gemini letterlijk: "The concept of a taskbar basement is clever and clearly displayed, but the 3D graphic style looks a bit cheap and mobile-esque." Beter maken: "Refine the lighting and 3D asset quality to give the game a more premium aesthetic." Het idee werkt dus (de taakbalk leest), de afwerking niet.

Proef in dezelfde run (`proef-v6-licht.jpg`, boven v5, midden en onder twee proeven), alles als schakelaar in de scripts, standaard uit, zodat v5 gelijk blijft:
- `HV2_AGX=1` (AgX met Punchy): alles valt flets en grijs uit, titel crème. Niet doen.
- `HV2_LIJN=1` (warme inktlijn om Gloop, helden, pet en hoeden) en `HV2_MAT=1` (matter, minder glans): iets meer getekend, maar op 920 nauwelijks verschil.
- `GLOED=1` in `samenstellen.py` (gloed om fel licht, warme toon, vignet): maakt het waziger, de titel verliest zijn rand. Niet doen in deze vorm.
- Mijn oordeel (GEZIEN met Read op 920): geen van de proeven is duidelijk beter dan v5, dus geen nieuwe testronde op de gratis daglimiet.

Wat de volgende stap moet zijn: niet nog meer poetsen aan licht, maar de stijl zelf. De drie concurrenten zijn getekend (Rusty pixels, Spirit City en Desktop Defender vlak getekend met harde schaduwvlakken). Plan v6: toon-schaduw (twee of drie vlakke tinten per materiaal in plaats van glad plastic), een dikke inktlijn op 2x om de figuren, en minder glimmende hoogtelichten; eerst één losse proef op Gloop alleen, dan pas het hele beeld.

## Ronde 6 (27 nov ±13:30 NL): getekende stijl in plaats van glad plastic
Na Gemini ("3D looks a bit cheap and mobile-esque") de stijl zelf veranderd, niet het licht. Schakelaar `HV2_TOON=1` in `header_v2.py` (standaard uit, v5 blijft te maken):
- Elk materiaal is nu lichtkant plus vlakke schaduwkant: een harde Toon-schaduw (Cycles Toon BSDF) op de basiskleur en een vaste, iets koelere en paarsere schaduwtint, zoals een getekend spel met twee tinten per vlak.
- Smalle warme randlijn langs de buitenkant van de figuren (Gloop, helden, hoeden, pet), niet op muur en aarde.
- Inktlijn om de figuren (`HV2_LIJN=1`, dikte 3,4 op 2x). Kleine harde glimvlek alleen op goud en kroon.
- Eén harde zon als licht (vul-, sleutel- en titellamp uit), dus duidelijke schaduwen; de titel ook getekend, feller geel.
- Maken: `HV2_TOON=1 HV2_LIJN=1 HV2_TZON=4.2 HV2_LIJNDIK=3.4 HV2_SCHADUW=0.5 HV2_STR=0.85 HV2_STG=0.72 <venv>/bin/python header_v2.py r.png 1840 860 28`, dan `python3 samenstellen.py r.png header-v6-920x430.png`.
- Bekeken met Read op 920, 460 en 2x (`rechts-v6-2x.png`). Voor en na: `voor-na.png` (v5 boven, v6 onder).
- Mijn oordeel (GOK tot de blinde test): meer getekend en de titel leest beter; de helmen lezen als witte kommen, minder metaal.
- Blinde test: set `hats-header-v2.json` heeft nu v5 en v6 als twee kandidaten, zodat de rechter zegt welke beter is. Run 45995843174 gaf geen uitslag: Gemini HTTP 429, gratis daglimiet op (GEZIEN). Opnieuw starten in de volgende run. Keuring Daan gevraagd: #275.

## Ronde 7 (27 nov ±15:00 NL, Daan #275 M1 tot M3 en twee kan-punten)
Schakelaar `HV2_V7=1` in `header_v2.py` en `V7=1` in `samenstellen.py` (standaard uit, v6 blijft te maken):
- **M1 helmen metaal:** emmer en ridderhelm koel donkergrijs (`HV2_MGRIJS` 0,12), schaduwkant donker grijsblauw, één harde witte glimstreep. Lezen nu als metaal, niet als witte kom.
- **M2 één stijl:** wolken vlakke vormen met harde rand, platte onderkant, lichte bovenkant en dunne blauwe lijn, geen waas; heuvels ook scherp. Metselwerk en aarde zonder zachte bobbels, vaste tinten (geen verloop in de ruis) en donkerdere, bredere voegen.
- **M3 inktlijn:** 4,6 px op 2x (±2,3 op 920), donkerbruin en vol (niet meer doorschijnend).
- **Kan:** Gloop een donkerder teal schaduwkant (volume). Muispijl kleiner en op de Hats-knop in de taakbalk, alsof je hem aanklikt.
- Maken: `HV2_V7=1 HV2_MGRIJS=0.12 HV2_MGSIZE=0.12 HV2_TOON=1 HV2_LIJN=1 HV2_TZON=4.2 HV2_LIJNDIK=4.6 HV2_SCHADUW=0.5 HV2_STR=0.85 HV2_STG=0.72 <venv>/bin/python header_v2.py r.png 1840 860 28`, dan `V7=1 python3 samenstellen.py r.png header-v7-920x430.png`.
- Bekeken met Read op 920, 460 en 2x (`rechts-v7-2x.png`). Voor en na: `voor-na.png` (v6 boven, v7 onder).
- Blinde test: set `hats-header-v2.json` heeft nu v6 en v7 als kandidaten.
- Twee runs (14:58 en 15:08 NL) gaven geen uitslag: Gemini HTTP 503 (druk), daarna HTTP 429 gratis daglimiet op (GEZIEN in het log van run 46013097424). Nakeuring Daan gevraagd: #281.

## Ronde 8 (27 nov ±17:00 NL, Daan #281 kan-punten K1 en K2)
Schakelaar `HV2_V8=1` bovenop v7 (standaard uit, v7 blijft te maken):
- **K1 emmer:** de glans van het metaal spiegelde de lichte muur en las als glas. Nu geen spiegeling meer maar een getekende glimstreep (vaste richting, harde rand, wit). Emmer op Gloop en helm van de ridder lezen als vlak grijs metaal.
- **K2 lijn held:** tweede lijnset alleen om de vallende held (`HV2_HELDLIJN` 1,5), zonder extra lijntjes in het gezicht. Leest op 920 en 460 even zwaar als de lijn om Gloop.
- Maken: als v7 plus `HV2_V8=1 HV2_HELDLIJN=1.5`, dan `V7=1 python3 samenstellen.py r.png header-v8-920x430.png`.
- Bekeken met Read op 920, 460 en 2x (`rechts-v8-2x.png`). Voor en na: `voor-na.png` (v7 boven, v8 onder).
- Blinde test: set `hats-header-v2.json` heeft nu v7 en v8.
- **Uitslag 17:01 NL** (`organisatie/blindtest/uitslag/hats-header-v2-2026-11-27-1701.md`, GEZIEN): v7 en v8 allebei NIET GESLAAGD, Gemini (flash-lite) gemiddeld plek 3,0, vier keer plek 3. Telkens: idee taakbalk-kelder "clever", maar de 3D "cheap and chaotic"; twee keer het advies "cleaner pixel art style".

## Proef v9 pixel (27 nov ±17:30 NL, niet getest)
Schakelaar `HV2_PIXEL=1` (smal pixelfilter) plus render op halve maat en 2x vergroten zonder vervaging. `proef-v9-pixel.jpg`: boven direct op 460 gerenderd (lijnen vallen weg, leest als slechtere 3D, niet als pixelkunst), onder v8 verkleind tot 307 breed met één gedeeld palet (kleuren gaan stuk: paarse hoed wordt grijs, rode pet bruin). Geen van beide goed genoeg om de gratis Gemini-limiet aan te besteden.
Plan v9 echt: render op 307x143 (pixel 3) met alleen vlakke kleuren per materiaal (emissie, geen verloop), een eigen vast palet per materiaal in plaats van kwantiseren, en een 1 px donkere omtrek uit een object-pass in Pillow (niet Freestyle). Minder dingen: gang en ridder links eruit of rustiger, zodat het beeld niet meer "chaotic" leest.

## Ronde 9 (27 nov ±19:00 NL): minder dingen, één groot figuur
Na de blinde test van 17:01 (v7 en v8 plek 3,0, "cheap and chaotic") eerst het "chaotic" aangepakt, niet de stijl gewisseld: pixelkunst zou niet het spel laten zien. Schakelaar `HV2_V9=1` bovenop v8 (standaard uit, v8 blijft te maken):
- Geen gang, geen ridder, geen tweede fakkel, geen wortels in de lege aarde. Er staan nu drie dingen in beeld: titel, vallende held met pet, Gloop met hoedentoren. Zoals Rusty en Spirit City: één groot figuur dat het vak vult.
- Camera dichterbij (`HV2_CAMB` 18,5 breed in plaats van 20, `CAMX` 2, `CAMZ` 3,75); titel groter (`TH` 2,75 op dichtere camera); gat, kluitjes, held en pet schuiven mee (`SX0`, `HVX`, `PETX`).
- Maken: als v8 plus `HV2_V9=1 HV2_CAMB=18.5 HV2_CAMX=2.0 HV2_CAMZ=3.75 HV2_GS=2.15 HV2_GX=7.0 HV2_SX0=2.15 HV2_SX1=3.95 HV2_HVX=3.4 HV2_HVZ=0.5 HV2_PETX=4.1 HV2_PETZ=5.9 HV2_TX=-6.0 HV2_TZ=5.05 HV2_TH=2.75 HV2_TO=1.18`, dan `V7=1 OT_Y=236 OT_X=22 OT_MAAT=27 python3 samenstellen.py r.png header-v9-920x430.png`.
- Bekeken met Read op 920, 460 en 2x (`rechts-v9-2x.png`); voor (v8) en na (v9) in `voor-na.png`.

## Ronde 10 (27 nov ±21:15 NL): de drie kan-punten van Daan (#304)
Schakelaar `HV2_V10=1` bovenop v9 (standaard uit, v9 blijft te maken):
- **K1 held kleiner** (`HVS` 1,55 in plaats van 1,85): Gloop is nu duidelijk het ene grote figuur.
- **K2 pet bij zijn hoofd** (`PETX` 4,15, `PETZ` 3,65, `PETVOOR` -25): de pet vliegt net rechts boven zijn hoofd, iets naar de camera gekanteld zodat koepel, witte band en klep blijven lezen (gekozen uit drie standen). Valstreepjes boven zijn hoofd (`STREEP`).
- **K3 lege aarde linksonder:** een hoge hoed van een eerder gevallen held en drie munten in de grond (`BHNR` 7; helm, veermuts en koksmuts geprobeerd, de hoge hoed leest op 460 het snelst als hoed).
- Maken: als v9 plus `HV2_V10=1 HV2_HVS=1.55 HV2_PETX=4.15 HV2_PETZ=3.65 HV2_PETVOOR=-25 HV2_PETK=15 HV2_BHNR=7 HV2_BHK=-20 HV2_BHS=1.4`, dan `V7=1 OT_Y=236 OT_X=22 OT_MAAT=27 STREEP=486:192:32,508:200:22,528:210:12 python3 samenstellen.py r.png header-v10-920x430.png`.
- Bekeken met Read op 920, 460 en 2x (`rechts-v10-2x.png`); v9 boven v10 in `voor-na.png`.
- **Blinde test 21:13 (GEZIEN, `organisatie/blindtest/uitslag/hats-header-v2-2026-11-27-2113.md`): v9 en v10 NIET GESLAAGD**, allebei plek 3,0 bij Gemini (vier keer plek 3 van 4, vóór Desktop Defender, na Spirit City en Rusty). Elke keer: idee "clever", 3D "cheap", "mobile-game-like", één keer nog "chaotic". Minder dingen en de kan-punten veranderden de plek niet: het zit in de afwerking van de 3D zelf, niet in wat er in beeld staat.
- Plan v11: geen glimmend verloop meer. Per materiaal twee vaste tinten (constant kleurverloop, geen glans, geen spiegeling), lijnen met wisselende dikte (Grease Pencil Line Art in plaats van Freestyle, spits uitlopend), en een getekende textuur op de grote vlakken (aarde, muur, lucht). Eerst een losse proef op Gloop naast de kat van Spirit City op 460, pas dan het hele beeld en de test.

## Ronde 11 (27 nov ±23:00 NL): twee kanten tegelijk testen
Tien rondes 3D-afwerking bleven op plek 3,0. Alle geteste headers en ook de itch-omslag van Sanne hadden hetzelfde dikke gele Lilita-logo met bruine rand en een blauwe lucht met bolle wolken: precies de "mobile game"-look. De speelschermen die wél plek 2 haalden hadden geen logo en lieten een echt bureaublad zien (werkvenster plus het hol onderaan). Daarom twee kandidaten die samen laten zien waar het zit:
- **v11a** (`bureau.py`): het spel zoals het echt is. Onderaan een echt spelbeeld (Sannes beeld `producten/steam-hol/itch/bron-omslag-f5850.png`, x 730 tot 1466, 1,25x), daaronder de taakbalk, erboven een avondbehang (lila naar perzik, heuvels, sterren) met een spreadsheet-venster rechts en het nieuwe logo links. Muispijl op de hoedenstapel. Zegt wat de rol vraagt: een klein spel onderaan je scherm terwijl je werkt. Maken: `MX=532 MY=332 LS=132 LY=-4 python3 bureau.py header-v11a-920x430.png`.
- **v11b**: v10 ongewijzigd in 3D, maar zonder 3D-titel (`HV2_GEENTITEL=1` in `header_v2.py`) en zonder het pilletje; erop het nieuwe logo. Zo meet de test of het logo zelf de "mobile"-indruk gaf.
- Nieuw logo: Jersey 10 (pixelletter, SIL OFL, `letters/`), crème-geel met donkere rand en harde schaduw (`logo.py`). Past bij de pixelgrond en het muntenbord in het spel, en lijkt meer op Rusty dan op een telefoonspel.
- Bekeken met Read op 920, 460 en 2x. Mijn oordeel (GOK tot de blinde test): v11a leest op 460 direct als "spel in je taakbalk", maar het spelbeeld is 1,25x vergroot en dus iets zacht. Volgende stap als v11a wint: het spel zelf op grotere strookhoogte filmen (Godot `--write-movie`, `hoogte=200`), zodat de strook scherp is zonder vergroten.
- **Blinde test 22:54 (GEZIEN, `organisatie/blindtest/uitslag/hats-header-v2-2026-11-27-2254.md`): v11a en v11b NIET GESLAAGD**, allebei plek 3,0 bij Gemini (vier keer plek 3, eerste keus drie keer Rusty, één keer Spirit City). v11a: concept met spreadsheet "clever", maar "sprite art looks messy and cheap". v11b: "chaotic and juvenile", "generic mobile asset". Dus het logo was niet de oorzaak, en een echt spelbeeld helpt ook niet: de rechter vindt de figuren zelf (Gloop, helden, zoals ze in het spel staan) goedkoop naast getekende key art. Dertien kandidaten op rij plek 3,0, steeds vóór Desktop Defender en na de twee getekende spellen. Verder poetsen aan dezelfde figuren heeft geen zin; zie het bericht aan Sanne van 27 nov 23:20.

## Ronde 12 (28 nov 2026, Mila, #30): in de lijn van itch-omslag v5
Sanne (#30, 04:50): itch-omslag v5 haalde plek 1,0 met een bureaublad, een werkvenster, het echte hol, een vlakke titel en het label "Lives above your taskbar". Dezelfde lijn op 920 x 430: `header_bureau.py <bron> <x0> <schaal> <uit>`, bron `producten/steam-hol/itch/bron-scherm5-1305s.png` (eigen film van main e72baf9, 1305 s).
- `header-v12a-920x430.png`: `x0 850, schaal 1.5` (zoals de omslag), strook 240 px, lucht 154 px, Gloop op de troon in het midden rechts met de schat ernaast.
- `header-v12b-920x430.png`: `x0 755, schaal 1.3`, strook 208 px, lucht 186 px, titel groter (Poppins Bold 112 op 2x).
Bekeken met Read op 920, 460 en 2x. Figuren niet nagetekend: alles in de strook is spelbeeld.
Uitslag (GEZIEN, `organisatie/blindtest/uitslag/hats-header-v2-2026-11-28-0451.md`): v12a GESLAAGD plek 1,5, v12b GESLAAGD plek 2,0 bij Gemini. Keuring v12a door Daan: #351. Pas na zijn ja wordt v12a `header-920x430.png`.

## Ronde 13 (28 nov 2026, Mila, #30): de moet-punten van Daan (#351)
`header_v13.py <bron> <x0> <schaal> <hoed.png> <uit>`. Zelfde lijn als v12a, met:
- M1: geen label meer, mailvenster met grijze balkjes zonder woorden (en kleiner, half over de rand), geen klok of datum; alleen spelbeeld en de spelnaam (regels Steam voor capsules).
- M2: titel Poppins Bold met "Fallen" in goud, donkere rand, een dieptekant en een lichte bovenkant, plus de hoge hoed uit het spelmodel (`modellen/hoeden.py` nr 7, 20 graden, Blender 5.1 via bpy, `hoed-hoge-hoed.png`) scheef op de H.
- M3: tekendoek 4x, het spelbeeld met hele factor NEAREST (1,25x wordt 5x, 1,5x wordt 6x), daarna het hele beeld in een keer naar 920. Geen 4x naar 3x Lanczos meer, dus geen zachte randen.
- `header-v13a-920x430.png`: `bron-scherm3-1400s.png 690 1.25`: links valt een held met zijn emmer en kroon de stekelput in, rechts Gloop op de troon met hoedenberg en schat. Strook 200 px, lucht 194 px.
- `header-v13b-920x430.png`: `bron-scherm5-1305s.png 850 1.5`: de uitsnede van v12a, om te meten of de nieuwe titel en het weghalen van het label de plek houden.
Bekeken met Read op 920, 460 en 2x (pixelranden scherp, titel leest op 460).
