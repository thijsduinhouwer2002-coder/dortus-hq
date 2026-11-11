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

## Blad v7.1 van Mila, alleen fouten en leesbaarheid (11 nov ±02:05 UTC)
De hoofdchat keurt v7 met drie beoordelaars; dit zijn alleen de fouten die ik zag, zodat ze niet in de bouw komen.
- **L1. 1c "how it works":** de pil "Next" ligt op de zeestrook en raakt "BACK stops" erboven (454 en 260). Zelfde regel als B5: 0,02 D lucht boven en onder de pil.
- **L2. 6c einde zonder dier:** onderaan staan drie regels plus stippen op elkaar ("next: Clownfish, 1 more", stippen, "4 days in a row", "1 rest day is fine"); op 454 raken de laatste twee regels elkaar bijna, op 260 is het een propje tegen de rand. Eén regel minder (bijvoorbeeld "4 days in a row · rest day ok" of de rustdag-zin alleen tonen als je gisteren rustte).
- Verder geen lees- of rekenfouten gezien; stickerrand maakt de dieren op 260 goed leesbaar.

## Bouwkeuring 2, 11 nov 2026, ±02:10 UTC (handmatige run hoofdchat: bouw zonder dieren, scherm voor scherm)

**Bekeken:** plaatjes run 42940068457 (1bc3d89, 16 scènes op fenix 8, FR265, vivoactive 5, FR255), e2e run 42940068326 (1bc3d89, alle negen horloges: fenix 7, fenix 8, epix 2 pro, FR255, FR265, FR965, Venu 2, Venu 3, vivoactive 5), naast blad v6. Ook de keuring door drie van de hoofdchat (`ebb-bouw-1-keuring-drie.md`) gelezen; ik ben het met alle twaalf punten eens. Gijs' commits van na 1bc3d89 (521493a herstelkop, e4b1e8a uitlegzin en dubbel opslaan) staan nog niet in beeld, die keur ik op de volgende beelden.

**Akkoord: nee** voor de bouw zonder dieren.

### Scherm voor scherm tegen blad v6
| Blad | In testbeeld? | Letter | Kleur en zee | Opmaak en centreren (gemeten) | Oordeel |
|---|---|---|---|---|---|
| 1 menu | ja (e2e `-m`, plaatjes 10, Venu `-veeg`) | systeem | strook vlak, zonder lichte kam; **rode vis** in plaats van je eigen dier | pillen en tekst in het midden (dx 0 tot +2 px) | nee: eigen dier, kam |
| 1b start | ja (`-s`, 12) | systeem | goed | in het midden; Start raakt de strook op vivoactive 5 | bijna |
| 1c uitleg | ja (`-u`, 11) | systeem | goed | tot 0,87 R op fenix 8 (grens 0,80); oude zin "while the sea gets dark" in beeld (e4b1e8a nog niet gezien) | nee |
| 2 ademen in | ja (`demo-b`, 9) | systeem | **turkoois vlak** (`0x00AAAA`) i.p.v. blauwe zee | cijfer zakt door de golf op alle horloges | nee |
| 2 ademen uit | **ontbreekt** | | | | |
| 3a/3b/3d/3c inhouden | alleen plaatjes 0 tot 3, **niet in de e2e** | systeem | zee wordt per stap donkerder: ja, goed te zien; op AMOLED rechte banden i.p.v. verloop | dier links of rechts naast de tijd (FR255 3:04 +6 px), vis raakt "0:30"; hart "--" | nee |
| 4 herstel | alleen plaatjes 8 | systeem | goed (zon, lichte zee) | kop tot 0,94 R, letters afgesneden op vivoactive 5 (521493a nog niet gezien) | nee |
| 5 rustig 4-7-8 | e2e `-r`, plaatjes 7 | systeem | **oud turkoois vlak** over het hele scherm (wit op teal 2,9:1), "4-7-8" op de schuimlijn | blad: zwart, zee onderaan, groot cijfer met s, "Calm 4-7-8" in het water | nee |
| 6 today | ja (`demo-c`, 5) | systeem | goed | kader dx +1 px | ja |
| 6 today, 6 rondes / 3 sessies | **ontbreekt** | | | | |
| 6b einde met dier | **ontbreekt** (wacht op dieren) | | | | |
| 6c einde zonder dier | **ontbreekt** (Gijs bezig) | | | | |
| 6d einde Calm (v7) | **ontbreekt** | | | | |
| 7 8 weeks | ja (`demo-d`, 6) | systeem | goed | kader dx +1 px, staven rechts is echte data | ja |
| 8, 8b, 8d sea log | **nee**: lijst van 4 i.p.v. raster 3 x 3 | | | lijst hangt +14 px rechts | nee (wacht op v7-data) |
| 8c sea log dier | **ontbreekt** | | | | |
| 9, 9b settings | **ontbreekt** (07e7ca3 nog niet in beeld) | | | | |
| 10, 10b, 10c veiligheid | ja (`-a`, `-a2`, `-a3`, 13 tot 15) | systeem | goed | tekst in het midden (dx 0 tot +2), binnen 0,74 R; OK raakt de strook op fenix 8 | bijna |
| pauzemenu | **ontbreekt** | | | | |

**Grijs:** `demo-a` is op **alle negen** horloges een leeg grijs vlak (epix 2 pro, fenix 7, fenix 8, FR255, FR265, FR965, Venu 2, Venu 3, vivoactive 5). Epix 2 pro, FR965, Venu 2 en Venu 3 hebben verder alleen `demo-b` tot `demo-d` (en Venu `-veeg`); de plaatjesbouw draait alleen op vier horloges.

### Moet-punten voor de bouw zonder dieren (D1 tot D9)
Dezelfde volgorde als de keuring door drie, met mijn maat erbij.
- **D1. Letter Barlow Condensed** (OFL) als eigen font, mijn kan-punt K1 wordt moet: het blad leunt erop en het lost de randproblemen (B4) op. Drie maten per schermmaat: groot cijfer (alleen 0 tot 9, : en s, dat houdt het klein), kop, regel. Meet het geheugen eerst op fenix 7 en FR255; past het groot cijfer niet, dan daar de systeemletter voor het cijfer en Barlow voor de rest.
- **D2. Eén zee.** `DIEPTE[0]` naar `0x00AAFF`. Ademen: blauwe zee met lichte kam zoals blad 2; rustig: zoals blad 5 (zwart, zee onderaan, "7 s" groot, "Calm 4-7-8" in het water), geen teal vlak meer.
- **D3. AMOLED verloop** (fenix 8, epix, FR265, FR965, Venu, vivoactive 5): zee met verloop en lichte kam, geen rechte banden achter de cijfers. Op MIP vaste tinten met golvende randen.
- **D4. Tekst nooit in de golf:** minstens 0,03 D tussen tekst en de hoogste golftop (ademen "2" en "23", rustig "4-7-8", herstel "15" en zon).
- **D5. Alles binnen 0,80 R:** herstelkop, uitleg (meet op de tekstregels zelf, niet op het kader met de schuimlijn).
- **D6. Knoppen los van de zee:** 0,02 D lucht onder Start, OK en Next.
- **D7. Dier op het inhoudscherm en in het menu:** je eigen dier (niet de rode vis), in rust in het midden onder de tijd, lucht erboven en eronder; in de plaatjes in rustpositie. Tot de dieren van Mila er zijn mag het de schildpad zijn.
- **D8. Testbeelden compleet, met vaste namen:** elk scherm uit de tabel hierboven dat ontbreekt (ademen uit, inhouden in de e2e, 6c, 6d, today 6 rondes en 3 sessies, settings 1 en 2, pauzemenu, sea log 1/2/3 en dier zodra gebouwd), op 454, 416, 390 en 260; `demo-a` repareren; plaatjes ook op Venu 2, Venu 3, epix 2 pro en FR965. Hartslag in de plaatjes nagebootst (bijvoorbeeld 61).
- **D9. Settings in Ebb-stijl** zoals blad v7 9 en 9b (zwart, gekozen regel als blauwe pil, woorden van v7).

Wanneer ja: als D1 tot D9 in beeld staan op de vier maten en alles gemeten binnen de grenzen valt (centreren 2 px, 0,80 R, 0,03 D vrij van de golf). Sea log en eindscherm met dier keur ik apart na Mila's dieren v8.
