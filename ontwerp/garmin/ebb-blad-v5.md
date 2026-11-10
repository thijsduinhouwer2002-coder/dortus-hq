# Ebb blad v5 (stand v5.3): alle schermen na de keuring van v4.1 (Mila, 11 nov 00:00 tot 00:35 NL)

**Blad: `ontwerp/garmin/ebb-blad-v5.png`** (21 schermen, per scherm links 454 px AMOLED, rechts 260 px MIP op ware grootte).
**Naast elkaar:** `blad5/drie-holds-454.png` (0:30, 1:45, 3:04) en `blad5/zee-standen-260.png` (alle zeven zee-standen).
**Dieren:** `ontwerp/garmin/ebb-dieren-v5.png`. Losse beelden en meting in `blad5/` (`meting-v5.txt`). Bron: `bron/ebb_blad_v5.py` en `bron/ebb_dieren_v5.py`. Gijs zet de dieren met zijn script al om naar `DierenData.mc`.
**Stand:** vervangt v4.1. Twee frisse keuringen in deze run, v5.0 en v5.1, gaven allebei een 6 (`ebb-blad-v5-frisse-keuring.md`). De punten daaruit zitten in v5.2 en v5.3. Nog niet bouwen en nog niet naar Thijs: eerst een frisse keuring op v5.3 met minstens een 8.

## Afvinklijst
**Besluit 22:53**
- [ja] 1. Dieren alleen voor trouw (sessies en dagen op rij). Inhoudtijd blijft zichtbaar, zonder beloning.
- [ja] 2. Geen meters. De zee wordt donkerder naarmate je langer inhoudt, in 6 standen.
- [ja] 3. Geen doelring en geen "next 3:00".
- [ja] 4. Een nieuw dier komt alleen op het eindscherm (6b).
- [ja] 5a. Ademtempo is instelbaar: Breathing pace, 10 per min (9).
- [ja] 5b. Trillen bij de laatste 3 ademhalingen: Buzz last 3 breaths (9b).
- [ja] 5c. Trillen elke 30 s tijdens inhouden, aan of uit: Buzz every 30 s (9).
- [ja] 5d. Alleen trillen: Buzz only, on (no sound) (9b).
- [ja] 5e. Aanraakscherm uit tijdens een sessie: Touch lock (9b).
- [ja, beschreven] 5f. Inhoudtijd per ronde plus hartslag in Garmin Connect: zie P2.
- [ja] 5g. Live hartslag klein op elk inhoudscherm (3a, 3b, 3c).
- [ja] 5h. Zacht signaal na 3:00: "time to breathe" plus trilling (3c).
- [ja] 6. 8 weeks toont sessies per week als staven en het gemiddelde als getal.
- [ja] 7. Menu: Rounds en Calm zijn twee even grote pillen, daaronder Sea log en Settings.

**Keuring v4.1 (drie beoordelaars)**
- [ja] T1 eigen dier
- [ja] T2 zee echt donkerder, 3b anders dan 3c, na 3:00 iets lichter
- [ja] P1, [ja, beschreven] P2, [ja] P3 tot en met P9
- [ja] V1 tot en met V7
- [ja] S1, S2

**Frisse keuring v5.0**
- [ja] M1 tot en met M8

**Frisse keuring v5.1**
- [ja] N1 tot en met N6
- Kan-punten: [ja] grijze "s" weg, [ja] today met meer ruimte tussen de sessies. OK op 10c staat al op dezelfde hoogte als Next (0,79 van D, nagemeten).

## Per punt wat ik deed
**Van Thijs**
- **T1:** op 3a, 3b en 3c zwemt de schildpad mee die je in de sea log koos (8c, "swims with you: on"). Zonder keuze is het je laatst gevonden dier. Het dier kantelt per scherm anders en de belletjes staan elke keer ergens anders. Op het menu ligt ook je eigen dier (M8).
- **T2:** de zee gaat elke 30 s een stap donkerder (`ZEE_STAND`, standen 0 tot 5). Op 260 schuiven de lichte banden omhoog en vallen weg. Op 454 gebeurt hetzelfde, en het hele water wordt per stap ook 10% donkerder. Vanaf 3:00 springt het terug naar stand 4, dus iets lichter. Gemeten lichtsterkte van het water: 3a 0,042, 3b 0,015, 3c 0,0085 (tweede beoordelaar).

**Product**
- **P1:** 9 toont Rounds 3, Breathing pace 10 per min, Breaths 30 en Buzz every 30 s on. 9b toont Buzz last 3 breaths on, Buzz only on (no sound), Touch lock on en Safety info.
- **P2, Garmin Connect:** activiteit Breathwork, met per ronde een lap. FIT-velden: per lap "Hold time" en "Breaths", in de samenvatting "Rounds 3" en "Longest hold 3:04". Daarbij de gewone hartslaggrafiek van Garmin; daarop zie je per ronde het hart zakken. Er staat nergens "best" of "record".
- **P3:** op elk inhoudscherm onderaan een hartje, bpm en "· round N". Die regel staat op 3a, 3b en 3c op dezelfde hoogte.
- **P4:** na 3:00 staat bovenaan "time to breathe" in wit op de plek van "hold", met een trilling. Geen geel.
- **P5:** de staven zijn sessies per week en de getallen eronder ook. Daaronder "avg hold 1:41" over alle sessies; dat is iets anders dan today (1:49, alleen vandaag).
- **P6, één verhaal:** een nieuwe gebruiker met 9 sessies.
  - Ochtend 7:40: 1:20, 1:45, 3:04. Dat zijn de schermen 3a, 3b, 3c en 6b. Op 6b krijg je de Starfish voor 4 dagen op rij, en daarmee heb je 7 dieren.
  - Avond 21:15: 1:15, 1:38, 1:52. Op 6c staat dan "Pufferfish tomorrow", want die komt bij 5 dagen op rij.
  - Today: zes holds, avg 1:49 (nagerekend).
  - 8 weeks: 0 0 0 0 0 0 3 6, samen 9 sessies.
  - Sea log: "7 of 24", en de octopus vraagt "3 more sessions" (12 min 9).
  - Herstel: "round 2 held 1:45".
- **P7:** today laat de hele dag zien (twee sessies, zes trechters) en niet de drie tijden van het eindscherm.
- **P8:** scherm 2 heeft groot "23" en klein "of 30 · round 2". Scherm 4 heeft "big breath in, hold" boven "15 s". Het eindscherm heeft "3 rounds" boven de drie tijden.
- **P9, regels:**
  - **Gemiste dag:** de reeks op het eindscherm begint opnieuw. Dieren voor dagen op rij tellen met je beste reeks, dus een gemiste dag pakt nooit een dier af. Na 7 of meer dagen zonder sessie komt de zeekomkommer, en die gaat dan voor op andere dieren.
  - **Schema:** hoogstens één nieuw dier per sessie, en sessiedieren tellen hoogstens 2 sessies per dag mee. Bij ongeveer 4 sessies per week krijg je er in week 1 vier à vijf, in week 2 en 3 elke 3 à 4 dagen een, en daarna ongeveer één per week. Narwhal, Giant squid en Whale komen in maand 3 en 4.
  - **Waarschuwing:** de drie veiligheidsbladen bij de eerste start en elke 30 dagen opnieuw. "Seated or lying?" bij elke Rounds-start. Op 3:00 een trilling met "time to breathe".

**Visueel**
- **V1:** sea log 3 x 3 per blad, drie bladen. Het kleinste dier is 30 px op 260 en 52 px op 454 (gemeten).
- **V2:** een dier dat je nog niet hebt is een spook: het dier in drie donkere blauwen, zodat vinnen, banden, buik en een klein licht oog te zien blijven, met een lichtcyaan rand van 2 px. De rand haalt 18,5:1 op zwart en 6,4:1 op 0055AA. Bovenaan staat wat het gekozen spook vraagt ("Octopus · 3 more sessions"). De zeekomkommer blijft een verrassing ("comes after a break").
- **V3:** nergens nog grijs. Tekst is wit (7,3:1 op 0055AA) of lichtcyaan AAFFFF (6,4:1).
- **V4:** 6b en 6c hebben hetzelfde skelet: kop op 0,14, "3 rounds" op 0,21, tijden op 0,27, dier op 0,535 tot 0,55, regel op 0,73, regel op 0,80, 7 stippen op 0,86. Het spook zit helemaal onder water.
- **V5:** de zeester op 6b is ongeveer 37% breed. Daarachter een lichtkrans van 12 stralen, alleen onder water; op het horloge draait die langzaam. Dan "new friend!" in geel op een eigen regel en meer belletjes.
- **V6:** dieren v5. Opnieuw getekend: zeekomkommer met slaapmuts, zeeotter op zijn rug, zeehond met vlekjes. Rog is een kleine ruit met stippen, manta breed met hoorntjes. Haai, zwaardvis, orka en manta zijn lichter of hebben een rand. Alle 24 hebben hetzelfde oog.
- **V7:** 8c heeft geen 24 stipjes meer, wel een groot dier, de naam, "found: 3 days in a row" en een knop met toestand.

**Veiligheid**
- **S1:** drie bladen. De tekst letterlijk voor de code:
  - "Sit or lie down. / Never standing, / never in or near water, / never while driving." [Next]
  - "You can faint / without warning. / Never force a hold. / Stop if dizzy." [Next]
  - "Not if pregnant, / under 18, epilepsy, / heart or blood / pressure problems." In geel: "Not a medical device." [OK]
- **S2:** scherm 1b "Seated or lying?" met de knop Start, bij elke Rounds-start.

## Gemeten (`blad5/meting-v5.txt`, Python)
- **Centreren:** het kader van alles wat getekend is zit op 260 en 454 binnen 0,5 px van het midden, het optische midden binnen 2,7 px. Uitzondering is de sea log (8, 8b, 8d): 4,5 tot 9 px door de ring om het gekozen dier en de halve laatste rij op blad 3. Het raster zelf staat in het midden.
- **Lettermaat:** de kleinste letter is 20 px op 260 (hoofdletter ongeveer 14 px).
- **Kleuren:** 0 pixels buiten de 64 MIP-kleuren op 260, ook voor alle 24 dieren.
- **Contrast:** wit op 0055AA 7,3:1, lichtcyaan op 0055AA 6,4:1, geel op 0000AA 12,7:1, schuim op 000055 15,1:1, spookrand op zwart 18,5:1.
- **Tekst binnen de rand:** zonder water blijft de tekst binnen 0,70 tot 0,79 van de straal. De sea log haalt tot 0,92, dat zijn de onderste dieren. Op schermen met water meet de kolom "verst" het schuim van de golf.

## Naast elkaar gelegd en bekeken met Read
- **2, 3a, 3b, 3c:** het water wordt donkerder en het dier en de belletjes bewegen. Kop, groot getal en hartregel blijven op hun plek.
- **6b en 6c:** hetzelfde skelet; het dier tegenover het spook, en "new friend!" tegenover "Pufferfish tomorrow".
- **8, 8b, 8d:** kop, raster en paginanummer blijven vast. Alleen de regel bovenaan wisselt tussen "7 of 24" en de eis van het gekozen spook.
- **9 en 9b, 10, 10b en 10c:** kop en knop staan vast.

## Wat Thijs hier als eerste van zegt
Mijn gok: "het water en het nieuwe dier zijn nu goed." Wat hij nog kan zeggen: today blijft een rij trechters zonder uitleg, en de otter blijft het zwakste dier. Allebei staat het op mijn lijst voor na de volgende keuring.
