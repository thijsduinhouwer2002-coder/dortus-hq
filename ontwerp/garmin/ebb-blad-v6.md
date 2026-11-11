# Ebb blad v6 (stand v6.4): alle schermen na de keuring van v5 (Mila, 11 nov, nachtronde)

**Blad:** `ontwerp/garmin/ebb-blad-v6.png` (22 schermen, per scherm links 454 px AMOLED, rechts 260 px MIP op ware grootte).
**Naast elkaar:** `blad6/vier-holds-454.png` en `blad6/vier-holds-260.png` (0:30, 1:45, 2:30, 3:04).
**Dieren:** `ontwerp/garmin/ebb-dieren-v6.png` (alle 25 op 260; boven gevonden op 0000AA, onder als silhouet op zwart).
**Meting:** `blad6/meting-v6.txt` (centreren, rand, lettermaat, MIP) en `blad6/contrast-v6.txt` (tekst en dieren).
**Bron:** `bron/ebb_blad_v6.py`, `bron/ebb_dieren_v6.py`, `bron/meet_contrast_v6.py` (bouwen op v5; alleen wat verandert staat erin).
**Stand:** klaar voor de keuring door de hoofdchat (drie beoordelaars). Nog niet bouwen, nog niet naar Thijs. Mijn eigen frisse keuringen in deze run (v6.0: 7, v6.1: 7, v6.3: 7,3) zijn verwerkt in v6.4; de hoofdchat vroeg daarna geen eigen keuringen meer te doen.

## Afvinklijst

### Besluit 22:53 (Thijs)
- [ja] 1. Dieren alleen voor trouw (sessies en dagen op rij). Inhoudtijd zichtbaar zonder beloning; 6b met dier heeft juist kortere holds dan 6c.
- [ja] 2. Geen meters; de zee wordt donkerder tijdens het inhouden (zes standen, tot 2:30, daarna gelijk).
- [ja] 3. Geen doelring en geen "next 3:00".
- [ja] 4. Nieuw dier alleen op het eindscherm (6b).
- [ja] 5a. Tempo instelbaar: Breathing pace 15 per min (9), 10 tot 20, afgestemd met Gijs (G2).
- [ja] 5b. Trillen bij de laatste 3 ademhalingen: "Buzz before hold" (9b).
- [ja] 5c. Trillen elke 30 s tijdens inhouden, aan of uit: "Buzz in hold" (9).
- [ja] 5d. Alleen trillen: "Sound off" (9b).
- [ja] 5e. Aanraakscherm uit tijdens een sessie: "Touch lock on" (9b).
- [ja, beschreven] 5f. Inhoudtijd per ronde plus hartslag in Garmin Connect: laps met "Hold time" en "Breaths", samenvatting "Rounds 3" en "Hold times 1:20 · 1:45 · 3:04", gewone hartslaggrafiek (staat in Gijs' code).
- [ja] 5g. Live hartslag klein op elk inhoudscherm (3a, 3b, 3d, 3c).
- [ja] 5h. Zacht signaal na 3:00: "time to breathe" met trilteken en buzz (3c).
- [ja] 6. 8 weeks: sessies per week als staven, "avg hold 1:41" als getal.
- [ja] 7. Menu: Rounds en Calm 4-7-8 als twee gelijke pillen, daaronder Sea log en Settings.

### Keuring v4.1 (drie beoordelaars)
- [ja] T1. Je eigen dier zwemt mee (de schildpad uit 8c, "joins your holds"); belletjes per scherm anders.
- [ja, aangepast] T2. De zee wordt echt donkerder, ook op MIP; 3b anders dan 3c. "Na 3:00 iets lichter" is vervangen door het besluit van 00:55: na 2:30 blijft het gelijk.
- [ja] P1. Instellingen in gewone woorden, zonder "tick" of "Pace normal" (9, 9b).
- [ja, beschreven] P2. Connect-resultaat: zie 5f.
- [ja] P3. Hartslag en ronde op elk inhoudscherm.
- [ja] P4. Na 3:00 "time to breathe" in wit, met trilteken, niet in geel.
- [ja] P5. 8 weeks: staven = sessies per week, gemiddelde inhoudtijd alleen als getal (1:41, anders dan today 1:44).
- [ja] P6. Kloppende cijfers: ochtend sessie 8 (1:10, 1:25, 1:40, Starfish, 7 dieren), avond sessie 9 (1:20, 1:45, 3:04, "next: Clownfish, in 1 more session"); herstel "round 2 held 1:45"; today avg 1:44 (624 s / 6).
- [ja] P7. Today laat de hele dag zien (twee sessies, zes staven).
- [ja] P8. Scherm 2: groot "23", klein "of 30 · round 2"; herstel "big breath in, hold" boven "15 s"; eindscherm "3 rounds done" boven de tijden.
- [ja] P9. Gemiste dag: de reeks breekt pas na 2 lege dagen (besluit 00:55); dieren voor dagen op rij tellen met je beste reeks. Schema: tabel onderaan. Waarschuwing: drie bladen bij eerste start en elke 30 dagen, "Seated or lying?" bij elke Rounds-start.
- [ja] V1. Sea log 3 x 3 per blad, drie bladen.
- [ja, vervangen] V2. Silhouetten: zie punt 6 van v5 hieronder.
- [ja] V3. Geen grijs: tekst wit of lichtcyaan.
- [ja] V4. 6b en 6c hetzelfde skelet (kop 0,165, tijden 0,245, dier 0,49, regels 0,69 en 0,772, stippen 0,848).
- [ja, aangepast] V5. Nieuw dier groot en optisch in het midden; door punt 10 van v5 nu 0,145 D (kleiner, onder water).
- [ja] V6. Eén tekenregel (zelfde oog, zelfde opbouw) voor alle dieren.
- [ja] V7. Geen 24 stipjes op 8c.
- [ja] S1. Veiligheid in drie bladen, nu met "Never while standing," en "Not if: pregnant," (v6.4; Gijs past `EbbVeiligTekst` aan).
- [ja] S2. "Seated or lying?" met Start bij elke Rounds-start, met "3 rounds · 30 breaths" erboven.

### Keuring v5 (drie beoordelaars) en besluiten hoofdchat 00:55
- [ja] Besluit zee: elke 30 s donkerder tot 2:30, daarna gelijk; het seintje na 3:00 is tekst, trilteken en buzz.
- [ja] Besluit reeks: breekt pas na 2 lege dagen; zeekomkommer bonus 25. Om 24 van 24 waar te maken vult de Lobster nr. 23 (46 sessies), afgestemd met Gijs.
- [ja] 1. Geen koppeling inhoudtijd en dier: 6b (dier) 1:10 1:25 1:40, 6c (geen dier) 1:20 1:45 3:04.
- [ja] 2. Today: neutrale staande staven in één egale tint, geen "deeper = longer".
- [ja] 3. 3c trilteken (gespiegelde gele boogjes); "press START to breathe" op 3a tot 3c.
- [ja] 4. "breathe in", "3 rounds · 30 breaths", "Sound off"; de "s" is 13 tot 15 px op 260.
- [ja] 5. 0:30, 1:45, 2:30, 3:04 naast elkaar; vanaf 2:00 geen lichtstralen, vanaf 2:30 geen belletjes en alleen 000055 met dunne schuimrand.
- [ja] 6. Niet gevonden: één egaal vlak 000055 met buitenrand 0055AA, zonder ogen of strepen, met het nummer erop; ook op 6c.
- [ja] 7. Contrast dieren: orka met lichte rand van 2 px, manta AAAAAA, reuzeninktvis AA55FF, zeeotter FFAA55, kreeft FF5555 met rand FFAAAA; donkere randen van manta en haai weg (meting onderaan).
- [ja] 8. Herkenbaar op 260: zeehond liggend met flipper en snor, zeeotter op zijn rug met schelp en voeten omhoog, narwal wit met ronde kop en rechte slagtand (geen rugvin) tegenover de blauwe zwaardvis met zeil, walvis blauw met fontein en 1,3 keer groter, reuzeninktvis 1,25 keer en paars, zeekomkommer zonder mutsje, dolfijn met snavel en gebogen rugvin tegenover de haai met spitse kop.
- [ja] 9. 8 weeks: getallen 14 px, alle 8 weken zichtbaar (lege week = stip), grafiek in het midden (was 54 px te laag).
- [ja] 10. Ster 0,145 D (v5: 0,222), helemaal onder water, ±15 px tot de tekst, geen stralenkrans.
- [ja] 11. Optisch centreren: sea log nu met een stip onder het gekozen dier in plaats van een ring, en het raster als geheel op zijn zwaartepunt gezet (8: -1,6 px, 8b: -0,3, 8d: +1,3). 3b schildpad recht, belletjes links en rechts.
- [ja] 12. Menu: twee gelijke pillen, selectie = dikke schuimrand; schildpad helemaal onder de golf.

## Nieuw in v6.4 (naast de punten)
- Dunne zeestrook onderaan op today, 8 weeks, settings en de drie veiligheidsbladen, zoals menu en start: elk scherm hoort bij dezelfde zee.
- 8c: "after 3 days in a row" en "joins your holds".

## Gemeten (Python, op 260 MIP tenzij anders)
- **Optisch zwaartepunt (x):** 1 +0,3; 1b +1,7; 2 +0,3; 3a +1,2; 3b +2,0; 3d +2,0; 3c +0,9; 4 -0,9; 5 -1,7; 6 +0,2; 6b -0,6; 6c -0,4; 7 +3,0; 8 -1,6; 8b -0,3; 8d +1,3; 8c +0,1; 9 -2,0; 9b -1,6; 10 -0,4; 10b -0,9; 10c -0,3. Grootste: 8 weeks +3,0 (eerlijke data van een nieuwe gebruiker, staven rechts); kader daar +0,5.
- **Kader (x):** binnen 0,5 px, behalve sea log 8 (+3,0) en 8d (+5,5): dat is de prijs van optisch centreren.
- **Tekst binnen de veilige cirkel:** alle 22 schermen tot 0,80 van de straal (golfschuim niet meegeteld).
- **Lettermaat:** kleinste letter 20 px op 260 (kapitaal ±14 px).
- **Kleuren:** 0 pixels buiten de 64 MIP-kleuren.
- **Tekstcontrast (eis 4,5:1):** laagste 5,9:1 (lichtcyaan 55FFFF op knop 0055AA, 3a, 3b, 6, 7, 9, 9b); wit op 0055AA 7,3:1; op diep water 10,8 tot 16,3:1. Eén meetregel op scherm 4 (2,1:1) is het golfschuim tegen 00AAFF, geen tekst.
- **Dieren (eis 3:1, deel van de buitenrand):** volledig of bijna (85 tot 100%) op 0000AA: vis, garnaal, schildpad, zeepaardje, zeester, clownvis, kogelvis, octopus, inktvis, zwaardvis, manta, haai, orka, kreeft, walvis. Lager door donkere vinnen, poten of staart aan de rand (het lijf zelf haalt 3:1): kwal 31%, krab 67%, rog 72%, zeehond 64%, dolfijn 69%, zeeotter 56% (op 000055 100%), maanvis 44%, narwal 61%, reuzeninktvis 60%, zeekomkommer 49%. Zie `blad6/contrast-v6.txt`.

## Naast elkaar gelegd en bekeken met Read
- 3a, 3b, 3d, 3c: water stap voor stap donkerder, 3d en 3c gelijk; tijd, dier, "press START" en hartregel op dezelfde plek.
- 6b en 6c: zelfde skelet, alleen dier tegenover silhouet en de tekst wisselen.
- 8, 8b, 8d: kop, raster en paginanummer vast; de stip wandelt mee met de keuze.
- 9, 9b, 10 tot 10c: kop, knop en zeestrook vast.

## Wat Thijs hier als eerste van zegt
Mijn gok: "de zee en het eindscherm kloppen nu." Daarna misschien "de dieren met grote ogen zijn een beetje clipart" (vooral de ster). Het tweede kan ik in v7 oplossen met kleinere ogen, als de keuring het ook ziet.

## Dierenschema v6 (verwacht bij 4 sessies per week)
| nr | dier | wanneer |
|---|---|---|
| 1 | Fish | 1 sessie |
| 2 | Shrimp | 2 sessies |
| 3 | Jellyfish | 2 dagen op rij |
| 4 | Turtle | 3 dagen op rij |
| 5 | Crab | 4 sessies |
| 6 | Seahorse | 6 sessies |
| 7 | Starfish | 4 dagen op rij |
| 8 | Clownfish | 10 sessies |
| 9 | Pufferfish | 5 dagen op rij |
| 10 | Octopus | 12 sessies |
| 11 | Squid | 14 sessies |
| 12 | Ray | 16 sessies |
| 13 | Seal | 6 dagen op rij |
| 14 | Dolphin | 18 sessies |
| 15 | Swordfish | 20 sessies |
| 16 | Sea otter | 22 sessies |
| 17 | Manta | 7 dagen op rij |
| 18 | Shark | 25 sessies |
| 19 | Sunfish | 28 sessies |
| 20 | Orca | 32 sessies |
| 21 | Narwhal | 36 sessies |
| 22 | Giant squid | 42 sessies |
| 23 | Lobster | 46 sessies |
| 24 | Whale | 50 sessies (±12 weken) |
| + | Sea cucumber | bonus: eerste sessie na een pauze; telt niet mee in "x of 24" |

Dagen op rij: een reeks breekt pas na 2 lege dagen; telt met je beste reeks. Hoogstens één nieuw dier per sessie, laagste nummer eerst; sessiedieren hoogstens 2 per dag.
