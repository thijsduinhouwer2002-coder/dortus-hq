# Ebb: keuring van de echte bouw (Daan)

## Bouwkeuring 1, 11 nov 2026, 02:00 UTC

**Bekeken (met Read, op ware grootte en ingezoomd):**
- Plaatjesbouw run 42940068457 op commit 1bc3d89 (tak `claude/garmin-2026-11-10b`), alle 16 scènes op fenix 8 (454), FR265 (416), vivoactive 5 (390) en FR255 (260). Map `garmin-adem/plaatjes/` op tak `schermen`.
- e2e run 42938098428 op b8918fe (menu, uitleg, startcheck, drie veiligheidsbladen, rustig) op fenix 8 en FR255.
- Naast blad v6 (`ontwerp/garmin/ebb-blad-v6.png`) gelegd, scherm voor scherm.
- Gemeten in Python (kader van de tekst tegen het schermmidden, afstand tot de rand als deel van de straal).

Beelden van deze keuring: `ontwerp/garmin/bouw/keuring1-zes-punten-454.jpg` (de zes probleemschermen ingezoomd), `keuring1-alle-454.jpg` en `keuring1-alle-260.jpg` (alle 16 scènes).

**Oordeel: `Akkoord: nee` voor de bouw, maar een grote stap.** Wat goed is: de app ziet er nu uit als één geheel. Menu met twee gelijke pillen, de zee die per 30 s donkerder wordt (0:30, 1:45, 2:30 en 3:04 zijn duidelijk anders), "time to breathe" in wit met trilteken, today met staven, 8 weeks met sessies per week, veiligheidsbladen letterlijk als het blad, en per horloge de juiste knop ("top button to breathe" op vivoactive 5). Centreren van de tekstblokken klopt op 1 tot 3 px op bijna alle schermen. Wat nog niet klopt zijn botsingen tussen tekst en water, één verkeerde waterkleur, het dier op het inhoudscherm en tekst die buiten de veilige cirkel valt. Allemaal klein werk in de code, geen nieuw ontwerp.

### Moet (voor ik ja zeg)
- **B1. Eén zee: de bovenste watertint is fout.** `EbbTeken.DIEPTE[0]` is `0x00AAAA` (groenblauw, turkoois). Het blad gebruikt `0x00AAFF` (W0, helder zeeblauw). Daardoor zijn ademen (scène 9) en rustig 4-7-8 (scène 7) turkoois en de rest blauw: het lijken twee apps. Zet `DIEPTE[0]` op `0x00AAFF` (MIP-kleur, mag op alle horloges). Controleer daarna dat het woord in het water (`of 30 · round 2`, `4-7-8`) nog minstens 4,5:1 haalt; zo niet, wit of `0x000055`.
- **B2. Het getal staat in de golf.** Ademen: de onderkant van "23" zakt door de schuimlijn (alle vier horloges). Rustig: de schuimlijn loopt dwars door "4-7-8" (alle vier). Herstel: de zon raakt bijna "15". Regel voor elk scherm: tekst raakt nooit de schuimlijn, minstens 0,03 D vrij boven de hoogste golftop (golftop = peil + amplitude). Dus het peil lager, of het getal hoger, of bij 4-7-8 het label helemaal onder de golf in het water zoals op het blad (scherm 5: "Calm 4-7-8" ruim in het water).
- **B3. Dier op het inhoudscherm in het midden.** Op 1:45 en 3:04 staat de schildpad rechts van de tijd (FR255 3:04: kader +6 px), op 0:30 en 2:30 links, en op 0:30 raakt de vis met zijn belletjes de onderkant van "0:30" (fenix 8, vivoactive 5). Regel van Thijs (20:20): alles in het midden. Het dier rust in het midden onder de tijd (zoals blad v6 scherm 3a tot 3c), met minstens 0,02 D lucht onder het getal en boven de hartregel. Zwemmen mag, maar dan een kleine slinger rond het midden (hoogstens 0,04 D opzij), niet van rand tot rand. De stilgezette plaatjes moeten het dier in de rustpositie tonen.
- **B4. Tekst binnen de veilige cirkel.** "big breath in, hold" (herstel) loopt tot 0,94 R op fenix 8 en 0,89 R op FR255, en op vivoactive 5 snijdt de ronde rand de "b" en de "d" af. "how it works" met zijn regels loopt tot 0,87 R op fenix 8. Grens is 0,80 R. Oplossing: kleiner lettertype voor die kop, of twee regels ("big breath in," / "hold"). Meet het na met de meting die ik hieronder geef, niet alleen het kader.
- **B5. Knop los van de zee.** OK, Next en Start (uitleg, veiligheid, startcheck) liggen op of tegen de bovenrand van de zeestrook (fenix 8 scène 15: OK zakt in de golf; vivoactive 5 Start raakt hem). Minstens 0,02 D tussen onderkant pil en hoogste golftop; anders de strook lager.
- **B6. Op 454 en 416 (AMOLED) geen strepen als een vlag.** Op het inhoudscherm zijn de lagen water rechte horizontale banden met een harde rand dwars achter de cijfers (fenix 8 0:30 en 1:45 het duidelijkst). Het blad en het besluit van 23:38 zeggen: op 454 een verloop, op 260 vaste tinten. Op AMOLED dus een zacht verloop (bijvoorbeeld 12 tot 16 smalle stroken die in kleur weinig verschillen, of een bitmap van het verloop per zeestand), op MIP mogen de banden blijven maar dan met een golvende rand zoals de bovenste golf, niet recht.
- **B7. Testbeelden compleet.** `demo-a` in de e2e is een grijs vlak (niet vastgelegd) op fenix 8 en FR255. Nog niet in de plaatjesbouw: settings (9 en 9b), eindschermen 6b en 6c, sea log volgens v7. Die keur ik zodra ze er zijn; zonder die schermen geen ja.

### Kan (beter, niet blokkerend voor de bouw)
- **K1. Lettertype.** Het blad leunt op Barlow Condensed; de bouw gebruikt de systeemletter. Op FR255 (smalle vette systeemletter) oogt dat prima, op fenix 8 en Venu breder en gewoner, en het is de oorzaak van B4. Een eigen bitmapfont (Barlow Condensed, OFL-licentie, drie maten: getal, kop, regel) maakt Ebb meteen herkenbaar en lost B4 voor altijd op. Advies aan Gijs: doen na B1 tot B7 als het geheugen het toelaat (fenix 7 en FR255 eerst meten).
- **K2. Hartregel in de plaatjes.** "♥ --" in alle stilgezette beelden. Voor winkelbeelden en mijn keuring een nagebootste hartslag (bijvoorbeeld 61) zodat je ziet hoe het eruitziet als het werkt. De afstand rond de stip is ongelijk ("-- ·  round"): gelijk maken.
- **K3. Sea log (scène 4)** is nu een lijstje dat links hangt (fenix 8 kader +14 px) en lijkt nog niet op het blad. Wacht op dieren v7 van Mila; niet nu ombouwen, wel straks het raster van v7 letterlijk volgen.
- **K4. Titel "in" bij rustig** in `0x55AAAA` is net zwakker dan de andere koppen in `0x55FFFF`. Liever overal dezelfde koptint.

### Meting die ik gebruikte
Midden van het scherm uit een zwart scherm (scène 13) per horloge, daarna per scène het kader van alle tekstpixels (wit, geel, koraal, schuimkleur) binnen R min 3 px. Let op: de schuimlijn telt als tekst mee, dus voor de rand-toets alleen de tekstregels zelf nemen (rijen boven de golf). Uitkomst kader dx op fenix 8: +0,5 tot +3,5 px op alle schermen behalve sea log (+14). FR255: -1,5 tot +3,5, behalve 3:04 (+6, schildpad rechts).

### Volgende keer
Zodra B1 tot B7 op de tak staan en de plaatjesbouw groen is, keur ik in één ronde alle scènes opnieuw op dezelfde vier horloges, plus settings, eindschermen en sea log. Daarna pas winkelbeelden uit de echte bouw.
