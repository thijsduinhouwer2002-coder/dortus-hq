# Ebb blad v7 (stand v7.1): dieren, sea log en tekst (Mila, 11 nov run 26 en 27, nachtronde)

**Opdracht:** "Voor Mila" in `ebb-blad-v6-keuring-drie.md` (alleen dieren, sea log en kleine tekstpunten; de schermen zonder dieren bouwt Gijs uit v6).
**Blad:** `ebb-blad-v7.png` (20 schermen, links 454 AMOLED, rechts 260 MIP op ware grootte). Losse beelden: `blad7/ebb-v7-*-260.png` en `-454.png`.
**Dieren:** `ebb-dieren-v7.png` (alle 25 op 260 in hetzelfde vak: boven gevonden op 0000AA, onder niet gevonden op zwart).
**Meting:** `blad7/meting-v7.txt` (centreren, rand, MIP), `blad7/contrast-v7.txt` (tekst en dieren), `blad7/data-v7.txt` (data-controle).
**Data voor Gijs:** `ebb-dieren-v7-data.json` (alle 25 in het formaat van `maak_dieren_data.py`, zie "Voor Gijs").
**Bron:** `bron/ebb_dieren_v7.py`, `bron/ebb_blad_v7.py`, `bron/meet_contrast_v7.py`, `bron/exporteer_dieren_v7.py` (bouwen op v6).
**Stand:** klaar voor keuring. Gijs: de dieren pas bouwen na de keuring; de tekstpunten (settings, start, trilteken) mag je meteen meenemen.

## De haak: de sea log is een stickerboek
Elk gevonden dier heeft dezelfde witte stickerrand (2 px op 260, 3 px op 454), overal waar het verschijnt. Dat is één tekenregel voor alle 24 en het lost het contrast in één keer op: wit op 0000AA is 12:1, dus kwal, maanvis, zeekomkommer en de rest halen nu allemaal 3:1 rondom (in v6 haalden tien dieren dat maar deels). Niet gevonden is het omgekeerde: een donker vlak met een blauwe rand. Je ziet in één oogopslag wat je hebt, en het voelt als plakken.
De grap: de bonus-zeekomkommer slaapt, met "z Z" boven zijn kop. Hij komt als je terug bent na een pauze.

## Afvinklijst (keuring v6, voor Mila)
- [ja] 1. Eén tekenregel: zelfde stickerrand, zelfde passende maat per vak (`maat_voor_vak`: elk dier precies in hetzelfde vak, "groter voor zeldzaam" is weg uit de sea log), zelfde oog (straal volgt het vak). Clownvis met zwart omrande witte banden; orka met grote witte oogvlek en grijs zadel; haai met hoge rugvin; zwaardvis (zeil en zwaard) en narwal (wit, geen vin, slagtand) verschillend. **Squid (11) vervangen door Eel** (murene, geelgroen, golvend lijf, open bek): geen twee inktvissen meer. Otter met grotere kop, garnaal opnieuw als gekrulde C met waaierstaart, bonusdier opnieuw (slapend).
- [ja] 2. Niet gevonden: vlak 000055 met rand 00AAFF (8:1 op zwart, 5:1 op 0000AA), zelfde dikte als de stickerrand, dezelfde vorm als het echte dier, geen nummer meer.
- [ja] 3. Sea log: één vaste kop op alle bladen ("sea log", "8 of 24"); gekozen dier met naam en wat er nog nodig is onder het raster; drie bladstippen in plaats van "1 / 3". **v7.1: optisch gecentreerd op de vorm**: het raster schuift tot het zwaartepunt van alle dieren (gevonden én silhouet, elk even zwaar) in het midden ligt. Gemeten "vorm x": blad 1 -0,1 px, blad 2 +0,3, blad 3 +0,4; kader +2, +3 en -1 px. De oude meting `optisch_x` telt silhouetten niet mee (00AAFF en 000055 staan in de lijst achtergrondkleuren) en geeft op blad 2 -22,6 px omdat daar alleen de octopus in kleur is; daarom staat de nieuwe meting `vorm_x` ernaast.
- [ja] 4. 6c: het volgende dier als silhouet mét zijn kenmerk (de banden van de clownvis in de randkleur, 5:1). Staven van today en 8 weeks in 00AAFF op 260 (8:1 op zwart; was 0055AA, 2,9:1).
- [ja] 5. Eindscherm 6b: nieuw dier 1,6 keer zo groot als in v6, "new friend: Starfish" in geel, stippen met het label "4 days in a row". 6c: "1 rest day is fine" als vaste zin onder de stippen.
- [ja] 6. Settings: "Buzz every 30 s on", "Buzz on last 3 breaths on", "Sound off" weg, vaste regel "Ebb makes no sound".
- [ja] 7. Start "Sit or lie down"; "time to breathe" zonder haakjes, trilteken wit. 8c is een knop: "swim with me" (dikke schuimrand = gekozen) met "START picks" eronder; kies een ander dier door het in de sea log te openen en START te drukken.
- [ja] 8. Nieuw scherm 1c "how it works" bij de eerste Rounds: "30 deep breaths, then hold while the sea gets dark. START: breathe again. BACK stops." Nieuw 6d: eindscherm van Calm, "calm done", "4 min · 12 breaths", "counts as a session" (zoals de code), stippen.
- [ja] 9. Sea log in week 3: 12 sessies, beste reeks 3 dagen, 8 gevonden. Blad 1 kiest de Starfish (reeksdier, nog niet gevonden): "1 more day in a row". Blad 2 Eel: "2 more sessions". Blad 3 Whale: "at 50 sessions" (vanaf 10 of meer te gaan staat "at N sessions", daaronder "N more").

## Voor Gijs
- **Data:** `ebb-dieren-v7-data.json`, per dier `bytes` in jouw formaat ([aantal delen, per deel rol, aantal punten, x, y ...; aantal ogen, x, y]), int8 in 1/90 van de diermaat (jouw SCHAAL 90), al op het zwaartepunt, hoogstens 42 punten per veelhoek, 6148 bytes voor alle 25. De getallen staan met teken (-127 tot 127); `& 0xFF` doe je bij het wegschrijven, zoals in je script. Plus `tint` (lijf, licht, donker), `rand` (wit voor elk dier), `slaperig`, en de silhouetkleuren. Gecontroleerd: uit de data opnieuw getekend wijkt de vorm 1,2 tot 4,7% af van mijn tekening op maat 100 (randpixels door afronden op 1/90), zie `blad7/data-v7.txt`.
- **Of met je eigen script:** `ebb_dieren_v7.py` heeft `delen_v7`, `RAND`, `ALLE` en `dier_beeld` zoals v6. Eén ding erbij: rol 6 = `zz` (de "z Z" van de zeekomkommer, wit, zonder stickerrand). In `ROL` dus `'zz': 6`, en in de randstap rol 6 overslaan.
- `EbbTrouw.DIEREN` nr. 11: "Squid" wordt "Eel" (zelfde drempel, 14 sessies volgens het schema in v6). Vorm in `delen_v7('aal')`.
- Stickerrand: alle delen eerst in wit tekenen, 2 px verschoven in 8 richtingen (op 454: 3 px), daarna het dier in kleur erover. De "z Z" van de zeekomkommer (rol `zz`) krijgt geen rand. Silhouet: hetzelfde in 00AAFF, dan het vlak in 000055.
- Teksten hierboven letterlijk. Today en 8 weeks: staafkleur 00AAFF op MIP.

## Gemeten (260 MIP)
- Tekst binnen 0,83 R op alle schermen, behalve het menu (0,85, ongewijzigd uit v6). Kleinste letter 20 px. 0 pixels buiten de 64 MIP-kleuren.
- Zwaartepunt "vorm x" op alle schermen binnen 1 px behalve 8 weeks (data van een nieuwe gebruiker, staven rechts); zie `blad7/meting-v7.txt`.
- **Tekstcontrast (eis 4,5:1):** laagste 5,9:1 (lichtcyaan op knop 0055AA: 1c, 3b, 9, 9b); wit op knop 7,3:1; op zwart en diep water 10,8 tot 17,1:1. De meetregels van 2,1:1 op 4, 6 en 7 zijn geen tekst: golfschuim (4) en de schuimlijn onder de staven (6, 7) die een staaf in 00AAFF raakt.
- **Dieren (eis 3:1):** gevonden, buitenrand tegen 0000AA en 000055: alle 25 op 100% (krab 99%: één poot raakt de rand). Niet gevonden, rand 00AAFF tegen zwart (8,2:1) en tegen 0000AA (5,2:1): alle 25 op 100%. In v6 haalden tien dieren dat maar voor 31 tot 72%.
- Staven: 00AAFF op zwart 8,2:1 (v6: 0055AA, 2,9:1).

## Bekeken met Read
Alle 25 dieren vergroot op 260 (gevonden en silhouet), de sea log bladen 1 tot 3, 8c, 6b, 6c, 6d en 1c op 260 en vergroot. Gezien: de stickerrand maakt de sea log rustig en rijk tegelijk; in v6 verdwenen kwal en maanvis half in het blauw, nu niet. De Eel is dun in het vak omdat hij lang is; hij leest als aal, niet als slang, door de bek en de vin.
