# Ebb blad v4.1: alle schermen na besluit 22:53 (Mila, 10 nov run 21 en 22)

**Blad: `ontwerp/garmin/ebb-blad-v4.png`.** Per scherm links 454 px (AMOLED, verloop en gloed zoals v3), rechts 260 px (MIP, strak), op ware grootte. Losse beelden en meting: `ontwerp/garmin/blad4/` (`meting-v4.txt`), bron `ontwerp/garmin/bron/ebb_blad_v4.py` (bouwt op `ebb_blad_v3.py`).
**Alle 24 dieren: `ontwerp/garmin/ebb-dieren-v4.png`**, losse beelden in `ontwerp/garmin/dieren4/`, punten in `bron/ebb_dieren_v4.py` (`nieuwe_delen`, eenheden van de diermaat, zelfde vorm als `dier_delen()`).
Vervangt blad v3. Gaat eerst naar Thijs via de hoofdchat; Gijs bouwt de schermen pas na zijn ja (de logica bouwt hij al). Run 21 maakte v4, run 22 (nachtronde hoofdchat 23:01 NL) maakte v4.1: sea log als verzamelboek, eindscherm met rondes, dier en reeks, trilinstellingen, dierenlijst gelijk aan Gijs' code.

## Het idee in één zin
Ebb is een zee die je beter leert kennen door terug te komen: je jaagt niet op langer inhouden, en wie terugkomt krijgt bezoek. De haak zit in trouw en in het verzamelboek; de grap is de slaperige zeekomkommer voor wie na een pauze terugkomt.

## Per scherm: wat en hoe in Connect IQ (één zin)
1. **Menu:** twee gelijke pillen "Rounds 3 x 30" (gevuld als gekozen) en "Calm 4-7-8" (omlijnd), daaronder "Sea log · Settings", walvis in het lage tij. *Bouw:* eigen `View` met `fillRoundedRectangle` en `drawRoundedRectangle` van dezelfde maat, omhoog en omlaag wisselt wat gevuld is, de onderste regel is een derde en vierde keuze.
2. **Ademen:** ongewijzigd uit v3. *Bouw:* zoals nu.
3. **Duiken (0:48 en 2:34):** "hold" boven de tijd, geen meters en geen ring, de zee wordt donkerder met de tijd, je hoogste dier zwemt mee, live hartslag klein onderaan (rood hartje plus getal). *Bouw:* zee-stand uit de tijd (0:00 licht, 3:00 donkerst; AMOLED via de drie vaste PNG's van v3), hartje uit twee `fillCircle` en een `fillPolygon`, getal uit `Activity.getActivityInfo().currentHeartRate` (`null` wordt "--").
3c. **Na 3 min:** "breathe when ready" in geel op de plek van de hartslag, de tijd loopt door. *Bouw:* bij jouw zachte signaal de regel wisselen.
4. **Boven** en 5. **Rustig:** ongewijzigd uit v3.
6. **Today:** drie trechters, tijden in wit, "avg 1:44" in grijs; geen goud, geen "new best". *Bouw:* zoals v3, alleen tekstkleur en onderregel.
6b. **Eindscherm met nieuw dier:** "session done", de rondes ("1:20 · 1:45 · 2:08"), het dier groot, "new friend: Turtle", de reden in geel ("3 days in a row") en zeven dagstippen voor de reeks. *Bouw:* na het opslaan, alleen als `EbbTrouw` een nieuw dier geeft; stippen met `fillCircle` / `drawCircle` (tot 7 gevuld).
6c. **Eindscherm zonder dier (de meeste sessies):** "session done", rondes, "4 days in a row" met stippen, en het volgende dier als silhouet met "Clownfish in 2 sessions" (of "... in 2 days"). Dat is een doel op trouw, niet op inhoudtijd. *Bouw:* silhouet = hetzelfde dier in een vlakke kleur met een rand in schuim (vier keer verschoven getekend), tekst uit de drempel min je teller.
7. **8 weeks:** acht waterkolommen, hoogte is het **gemiddelde per sessie** in die week, onder elke kolom het **aantal sessies** die week, deze week wit; onderaan "avg 1:44" en "5 sessions this week". *Bouw:* `fillRoundedRectangle` per kolom met de waterbanden via `setClip`; jouw rekenwerk geeft nu dagen per week, graag sessies per week (besluit punt 6).
8. en 8b. **Sea log als verzamelboek:** 12 dieren per blad in 3 rijen van 4, twee bladen; gevonden in kleur, nog niet als donkerblauw silhouet; ring in schuim om het gekozen dier; "7 of 24" en "1 / 2". Leest op 260 (dieren ±30 px breed, GEZIEN). *Bouw:* omhoog en omlaag verplaatst de ring, aan het eind van een blad naar het volgende; elk dier op zijn zwaartepunt in het vak.
8c. **Sea log, één dier:** START op een dier: groot, met naam, hoe je het kreeg ("4 days in a row") en "7 of 24", bovenaan 24 stippen. Bij een silhouet staat er wat ervoor nodig is ("10 sessions"). *Bouw:* zelfde dierfunctie op een grotere maat.
9. **Settings:** Breaths 30, **Pace normal** (gekozen), Hold tick on, Last 3 buzz on; Rounds staat erboven bij scrollen. Geen "Buzz only": Ebb trilt alleen. *Bouw:* eigen `View` zoals v3, vier regels zichtbaar.
10. **Veiligheid:** ongewijzigd uit v3, bij de eerste start en elke 30 dagen.

## De 24 dieren (gelijk aan `EbbTrouw.DIEREN` van Gijs, 65bb1ee, met één wissel)
Hoogstens één nieuw dier per sessie, alleen op het eindscherm. Dagen op rij tellen met de beste reeks.

| nr | dier | wanneer |
|---|---|---|
| 1 | Fish | 1 sessie |
| 2 | Shrimp | 2 sessies |
| 3 | Jellyfish | 2 dagen op rij |
| 4 | Turtle | 3 dagen op rij |
| 5 | Crab | 5 sessies |
| 6 | Seahorse | 8 sessies |
| 7 | Starfish | 4 dagen op rij |
| 8 | Clownfish | 10 sessies |
| 9 | Pufferfish | 5 dagen op rij |
| 10 | Octopus | 12 sessies |
| 11 | Squid | 6 dagen op rij |
| 12 | Ray | 15 sessies |
| 13 | Seal | 7 dagen op rij |
| 14 | Dolphin | 18 sessies |
| 15 | Swordfish | 10 dagen op rij |
| 16 | Sea otter | 21 sessies |
| 17 | Manta | 14 dagen op rij |
| 18 | Shark | 25 sessies |
| 19 | Sunfish | 30 sessies |
| 20 | Orca | 21 dagen op rij |
| 21 | Narwhal | 40 sessies |
| 22 | Giant squid | 30 dagen op rij |
| 23 | **Sea cucumber** | **back after a break**: eerste sessie na 7 of meer dagen zonder (was Sea turtle elder) |
| 24 | Whale | 60 sessies (jouw 60 is beter dan mijn 50; naam "Whale", want hij is koraalrood, geen blauwe vinvis) |

Waarom de wissel: de "oude zeeschildpad" is een tweede schildpad en dus geen nieuw dier. De zeekomkommer met halfdichte ogen maakt van een gemiste week een knipoog in plaats van schuld; dat vertellen mensen door. Hij kan op elk moment komen, ook vroeg; op de sea log staat hij op plek 23.

## Dieren v4
Alle 24 getekend in de stijl van v3 (gevulde vlakken, alleen MIP-kleuren, lijf, licht deel, donker deel, hetzelfde oog met glans), elk een eigen kleur, zodat je ze op het verzamelboek uit elkaar houdt. Gemeten: 0 pixels buiten MIP op 260 voor alle 24. Bekeken op 454, vergroot en op 260. Zwakste: de zeeotter (op zijn rug met een schelp; leest pas als je het weet) en het zeepaardje (wat hoekig). De kreeft staat als reserve in de bron. Giant squid is de inktvis in donkerrood met twee lange armen, Manta is de rog in zwart met hoorntjes.

## Gemeten (`blad4/meting-v4.txt`) en bekeken
- Kader van alles wat getekend is: binnen 2,0 px van het midden op alle 32 beelden (de sea log-bladen 1 tot 2 px door de vorm van de dieren aan de rand).
- Optisch midden op 260: binnen 2,7 px (8c door het kopje van de zeester links; 6c 1,9 px).
- Kleinste letter op 260: 20 px (14 px kapitaalhoogte), eis 13 px. 0 pixels buiten MIP op alle 16 schermen.
- Blad, alle dieren en de 260-beelden van menu, duiken, eindschermen, sea log en settings zelf met Read bekeken.
