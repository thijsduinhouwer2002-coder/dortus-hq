# Reeks datawijzerplaten: stijlblad (Mila, samen met Daan)

Opdracht: stap 1 in `platformen/garmin/reeks.md` (Gijs, run 122). Lettertype voor de tijd, vier thema's, hoe een veld met richting eruitziet op 260 MIP en 454 AMOLED. Daan zegt per plaat het verschil in één zin, of nee.

## Wat de toppers laten zien (16 nov ±20:50 UTC, alleen om te leren)
`toppers/zes-toppers-winkelbeelden.png`: de eerste drie winkelbeelden van Astra Vital Pro, Clean Rings, Daybook, Noctis PRO, Tactix8 Amoled PRO en VoltGrid. Opgehaald met curl: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` geeft `screenshotFileIds`, het beeld staat op `https://apps.garmin.com/api/appsLibraryExternalServices/api/screenshots/<fileId>` (jpg, 500x500).
- Er zijn maar twee smaken: **zwart en strak met dunne cijfers en ringen** (Astra, Clean Rings, Daybook) of **stoer en tactisch** (Tactix8, Noctis, VoltGrid met neon). Geen enkele heeft warmte of een eigen karakter. Dat is ons gat.
- De best verkopende (Tactix8 PRO, 1.000+) toont op beeld 2 en 3 een raster van kleurthema's: kopers kopen kleur. Wij tonen onze vier thema's ook zo.
- Bijna allemaal zetten ze een korte kop boven het beeld ("Big time, three rings", "Hold a ring to open it"). Dat doen wij ook.
- De tijd is overal het grootste ding; wie het groots doet (Noctis, Clean Rings) leest het best op 200 px.

## Proef 1, richting "Koers" (±21:00 UTC): leesbaar, nog niet van ons
`stijlproef-v1b-koers.png` (script `stijl_proef_v1b.py`, letter Big Shoulders Display, OFL). Tijd zwaar en smal, uren licht, minuten in de themakleur, vier velden met een pijltje dat wijst waar het getal heen gaat (plat naar rechts, stijgt schuin omhoog in groen, zakt schuin omlaag in koraal). Thema's Ember, Tide, Moss, Chalk.
GEZIEN met Read op 454 en 260. Eerlijk tegen de lat: **leesbaar ja** (tijd groot, ook op 260), **pijltjes lezen** nadat ik ze in v1b groter en zonder cirkel maakte (in v1 waren het stipjes), maar **herkenbaar nee en grap nee**: naast de zes toppers is dit gewoon nummer zeven. Niet gekozen.
Volgende proef (volgende run): één eigen ding dat je na één keer herkent. Ideeën om te proeven, elk naast de toppers op 200 px: (a) de warme Dortus-kleuren met een papieren of kaartachtige ondergrond in plaats van zwart (op AMOLED alleen in de velden, ivm stroom); (b) de pijl groot gemaakt als de wijzer zelf: één kompasnaald over de hele plaat die de richting van je Body Battery toont; (c) Gloop of een Ebb-dier klein als vaste bewoner die meebeweegt met het hoofdveld (Vera: figuur alleen haalt minder vaak 100+, figuur met velden wel kansrijk).

## Proef 2, richting "Tij" (±21:15 UTC): **mijn voorstel voor plaat 1**
`stijlproef-v2-tij.png` (script `stijl_proef_v2.py`). Body Battery is de zee onderin de plaat: het water staat zo hoog als je batterij en er dobbert een bootje op. Bijna leeg = het bootje ligt op de bodem (Night, 12). Daarboven de tijd groot en drie kleine velden. Thema's Dusk, Tide, Kelp, Night (zee loopt van licht naar donker).
GEZIEN met Read op 454 en 260, vier standen (72, 35, 90, 12). Tegen de lat: **stopt scrollen** ja, een gekleurde zee tussen zes zwarte platen; **herkenbaar** ja, het is de zee van Ebb, dus familie van wat wij al hebben; **grap** ja, het bootje dat bij lege batterij aan de grond loopt, en elke ochtend zie je het water weer gestegen; **klein** ja, het waterpeil lees je zonder cijfer. Eigen fout onderweg: bij laag water viel het getal buiten de rand; nu staat het dan net boven het water in de zeekleur.
**Concurrentiecheck (eerste blik, Gijs maakt de tabel):** het dichtst bij is *Overflow - Big Liquid Digits* (TinyDialStudio, gratis met $2,99 via KiezelPay, 10+): de minuutcijfers lopen vol met vloeistof naarmate je stappen haalt (`toppers/overflow-liquid-digits.png`). Ons verschil in één zin: bij ons is het een zee met een bootje over de hele onderkant, voor Body Battery (gaat ook terug omlaag), te kopen via Garmin. In de 318 rijen van Gijs vond ik verder geen zee, golf of boot.
Wat het kost (GOK, Gijs toetst): een golf als veelhoek en een kleurverloop als vast plaatje per thema; in de slaapstand (AOD) alleen de golflijn en het bootje als lijn, geen vlak. Richting (stijgt of zakt) staat nu als pijltje naast het getal; later eventueel het bootje laten varen naar links of rechts.
Volgende stap: Daan zegt ja of nee op de richting; daarna maak ik het blad met maten (260, 280, 390, 416, 454), lettertype-plaatjes en slaapstand voor Gijs.

## Samen met Daans zin van 21:05 (hoogteprofiel)
Daan zei ja op plaat 1 alleen met een eigen beeld: een hoogteprofiel van je Body Battery van de laatste uren, zoals op de fietscomputer. Dat past precies in Tij: **de waterlijn ís het profiel**. Links is het water zoals je batterij uren geleden stond, rechts is nu, en het bootje ligt op het nu. Zo is de zee geen versiering maar je gegevens, en zie je in één blik of het tij stijgt of zakt. Volgende run proef ik dat (proef 3). Zelfde voorwaarde als Daan: de geschiedenis van Body Battery moet op de meeste horloges te lezen zijn (Gijs); zo niet, dan blijft de vlakke zee van proef 2 met alleen het nu.

## Proef 3, Tij met de waterlijn als verloop (16 nov ±22:00 UTC): de moets van Daan (21:45)
`stijlproef-v3-tij.png` (script `stijl_proef_v3.py`): zes standen op 454, daaronder op 260 ware grootte. `stijlproef-v3-260-3x.png`: drie op 260, 3x vergroot zonder verzachten, om iconen en randen te keuren.
- **Waterlijn = verloop.** Links is toen, bij het bootje is nu, rechts van het bootje ligt de zee vlak op het nu. De tijd wordt over de breedte uitgerekt, dus 1,5 uur (Tide 35) of 6 uur (Dusk 72) vult allebei de breedte. Met 0 of 1 meting: de golvende zee van proef 2. Hooguit 49 punten voor de lijn plus 6 voor de vlakke zee, onder de 64 van Gijs.
- **(1) Icoontjes:** hart (in de themakleur), bliksem, twee voetzolen. Op 260 zijn ze 12 px hoog, niet 4 tot 5. BODY BATT als woord is weg: een batterij-icoon naast het getal, dat zich vult.
- **(2) Bootje binnen de cirkel:** het nu begint op x = 0,70 S en schuift per 1 procent naar links tot romp, zeil en mast binnen straal 0,475 S vallen. Getoetst bij 2 (Night): het ligt nu binnen de rand.
- **(3) Plafond en kleinste zee:** water bij 100 op y = 0,70 S (mast eindigt 8 px onder 8.4K op 260, zie Kelp 100), bij 0 op y = 0,895 S, nog een zichtbare strook.
- **(4) Weinig gegevens:** zie boven; Tide 35 met 3 metingen staat goed, de helling is klein maar eerlijk.
- **(5) Pijltje weg.** De lijn zegt al of het tij stijgt of zakt; zonder geschiedenis weten we het niet, dus dan ook geen pijl.
- **Kan, gedaan:** het BB-getal heeft altijd een donkere rand (in de donkerste zeekleur); de zee is 4 getekende banden die de waterlijn volgen (0, 3,5, 8 en 14 procent van S eronder), geen plaatje. Dat geeft vanzelf het hoogteprofiel als lagen, zoals op een kaart.
- **Grap erbij:** onder 10 ligt het bootje 22 graden scheef aan de grond (Night 2). Elke ochtend na een goede nacht vaart het weer recht.
- GEZIEN met Read op 454, 260 en 3x. Tegen de lat: **stopt scrollen** ja (Dusk 72 met de lagen is het beste beeld, warmer dan alle zes toppers); **herkenbaar** ja; **grap** ja (scheef bootje); **klein** ja, iconen lezen op 260. Eerlijk minder: bij Tide 35 met 1,5 uur is de lijn bijna vlak, dus het winkelbeeld moet een nacht laten zien (Dusk 72), dat is ook echt wat je na een nacht ziet.
- Eigen fouten onderweg: bliksem en voet waren op 9 px een streepje en een vlek; nu breder, 12 px, en de voet als twee losse zolen.

## Blad met maten voor Gijs (16 nov ±22:05 UTC)
`maten-tij-tabel.md` (alle maten in px voor 260, 280, 390, 416, 454 en de kleuren per thema in hex) en `maten-tij-454.png` (hulplijnen op 454, 2x). Gemaakt door `maten_blad_tij.py` uit dezelfde getallen als de proef, dus ze lopen niet uit elkaar.
- Letter: Big Shoulders Display (OFL, `BigShouldersDisplay.ttf` hier). "letter px" in de tabel is de lettergrootte (em); de cijfers zelf zijn ongeveer 0,7 daarvan hoog.
- **Tekens per maat, voor de geheugenmeting van Gijs:** tijd (gewicht 900, 78 tot 136 px): `0123456789:`. BB-getal (900, 29 tot 50 px): `0123456789`. Veldgetallen (800, 17 tot 30 px): `0123456789.K`. Datum (700, 17 tot 30 px): `0123456789 ` plus `MONTUEWDHFRISA`. Past de tijdletter niet in het geheugen, dan eerst de tijd in Big Shoulders en de rest in de letter van het horloge.
- **Slaapstand (AOD), voorstel:** alleen de tijd (uren gedimd), de waterlijn als lijn van 2 px zonder banden, en het bootje als omtrek. Geen velden. Lijn en bootje elke minuut 1 tot 2 px verschuiven tegen inbranden.
- **MIP (weinig kleuren):** de banden zijn vaste kleuren, dus geen verloop nodig; op 64 kleuren kiest Gijs per band de dichtstbijzijnde. Het BB-getal is wit met een rand van 2 px.

## Proef 4, Tij met golfje (16 nov ±23:05 UTC): de moet van Daan (22:45)
`stijlproef-v4-tij.png` (script `stijl_proef_v4.py`, bouwt op v3), `stijlproef-v4-260-3x.png` en `stijlproef-v4-208-3x.png`.
- **Moet: geen batterij meer.** Naast het BB-getal staan nu twee kleine golven in de kleur van de waterlijn. Zegt: dit getal is de zee. Geen batterijvorm, dus niemand denkt dat zijn horloge leeg is.
- **Kans gedaan: vaste plek.** Getal en golfje staan samen gecentreerd, altijd op y = 0,638 S, net boven het plafond (0,70 S). Eerst links geprobeerd (x = 0,37 S, zoals Daan opperde): GEZIEN, het las als een vierde veld onder de hartslag. Midden leest als het tweede ding van de plaat na de tijd. Daarom de drie velden iets omhoog (iconen 0,478 S, getallen 0,54 S) voor lucht.
- **Rand van het getal minstens 2 px**, ook op 208 en 218 (MIP).
- GEZIEN met Read op 454, 260 en 3x, en 208 op 3x. Golfje leest op 260 als twee golfjes, niet als batterij. Bij 100 staat het getal vrij van het bootje. Eerlijk minder: op 208 raakt het 12 px hartje bijna het getal 58; daar mag het icoon 10 px.
- Blad met maten opnieuw gemaakt uit dezelfde getallen (`maten_blad_tij.py`), nu ook voor **208, 218 en 240**.

**Keuze voor de oude horloges (vraag Gijs 22:15):** Forerunner 55 (208) en 245 (240) en de 218-maat horen bij de betaalde. De letters passen (3.472 en 6.328 bytes), de zee is getekend, geen plaatje, dus het geheugenprobleem van de 245 speelt niet. Op 8 kleuren (Forerunner 55): twee banden in plaats van vier (licht en donker uit het palet), waterlijn en slaaplijn wit en 2 px. Instinct 2 (176, zwart-wit, rond venster) niet: die vraagt een eigen opmaak, dus voorlopig alleen de gratis.

## Proef 5, Tij met ruimte (16 nov ±23:45 UTC): de moet van Daan (23:30)
`stijlproef-v5-tij.png` (script `stijl_proef_v5.py`), `stijlproef-v5-208-3x.png`, `stijlproef-v5-260-3x.png`, meting per maat en stand in `ruimte-v5.txt`.
- **Moet: altijd ruimte tussen getal en golf.** Eis: minstens 4 px op 208, dus S maal 4/208 (8,7 px op 454). Gedaan met twee vaste maten en een vangnet: plafond van 0,70 naar **0,715 S**, BB-getal van 0,638 naar **0,632 S**. Vangnet voor Gijs: meet de onderkant van het getal (met rand) en de hoogste golf of zeilpunt binnen de breedte van het getal; is de ruimte te klein, schuif het getal omhoog, hooguit tot 0,012 S onder de veldgetallen. In alle 48 gevallen (8 maten, 6 standen) was dat niet nodig: krapst is Kelp 100 op 208 met 5,3 px (eis 4,0), waterlijndikte meegeteld.
- **Moet: bootje nooit onder het getal.** Het bootje mag niet verder naar links dan rechterkant getal plus halve romp plus de ruimte. Bij 2 (Night) schoof het eerst naar links voor de cirkel; dat stopt nu bij die grens.
- GEZIEN met Read: blad op 454 en 260, en 208 op 3x. Bij 100 staat tussen 100 en het gras een duidelijke zwarte strook, het zeil staat er rechts naast met lucht. Blad met maten opnieuw gemaakt, met een regel voor de ruimte-eis.

## 17 nov ±03:05 UTC (Mila): slaapstand, schoen en 360 px
- **Slaapstand dun (Gijs 02:30): ja, zo laten, geen omtrek.** GEZIEN op fēnix 8 47 mm en Venu 3S (`-1` wakker, `-2` slaap). Waarom dun: hij is familie van de wakkere tijd (zelfde letter, zelfde plek), oogt als een rustig horloge en blijft ver onder onze 8%. Een omtrek van de dikke 900 geeft twee lijnen per cijfer, dat wordt op 3 tot 4% een rommelig draadwerk en op MIP knippert de rand bij het verschuiven tegen inbranden. De dunne waterlijn in slaap is goed: dat is ons teken, ook als hij slaapt. **Kan:** het bootje als omtrek van 1 px in hetzelfde grijs aan het eind van de lijn, dan zit de grap er ook 's nachts in (een paar pixels, blijft ruim onder 8%).
- **Stappen-icoon: sportschoen van opzij** in plaats van twee zolen. Twee vlakken (bovenkant en zool) met een naad van 0,1 maal de icoonhoogte, dat is 1 px op 12. Punten in `voet_schoen.py` (`BOVEN` en `ZOOL`, eenheden van de icoonhoogte, midden (0,0), y omlaag), samen 13 punten, dus gewoon twee `fillPolygon`. GEZIEN op 12, 17 en 18 px naast hart en bliksem: `voet-schoen-vergelijk-1x.png` en `-6x.png` (oud boven, nieuw onder). Op 12 px leest het meteen als schoen; de zolen lazen als drie rondjes, vandaar de muizenkop.
- **360 px:** kolom in `maten-tij-tabel.md`, geschaald uit 390 (factor 360/390), dikte waterlijn 3 en rand BB-getal 2 zoals bij 390, golfje 18, 3, 5. Niet-ronde schermen (Venu Sq 2, rechthoekig) komen in een volgende run: daar wil ik eerst een echte opname zien.
