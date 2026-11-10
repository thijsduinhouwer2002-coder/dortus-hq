# Ebb blad v4: alle schermen na besluit 22:53 (Mila, 10 nov run 21)

**Blad: `ontwerp/garmin/ebb-blad-v4.png`.** Per scherm links 454 px (AMOLED), rechts 260 px (MIP), op ware grootte. Losse beelden en meting in `ontwerp/garmin/blad4/` (`meting-v4.txt`), bron `ontwerp/garmin/bron/ebb_blad_v4.py` (bouwt op `ebb_blad_v3.py`). **Dieren: `ontwerp/garmin/ebb-dieren-v4.png`**, losse beelden in `ontwerp/garmin/dieren4/`, bron `bron/ebb_dieren_v4.py`. Vervangt blad v3. Gaat eerst naar Thijs via de hoofdchat; Gijs bouwt de schermen pas na zijn ja (de functies zonder schermen zijn al af).

## Het idee in één zin
Ebb is een zee die je elke dag een beetje beter leert kennen: je zit niet te jagen op langer inhouden, je komt terug, en wie terugkomt krijgt bezoek. De haak zit nu in trouw, en de grap in de zeekomkommer (zie dier 10).

## Wat er veranderde, per punt van het besluit
1. **Dieren voor trouw:** 24 dieren, gekregen op sessies en dagen op rij (lijst hieronder). Inhoudtijd staat er nog, zonder beloning: geen goud, geen "new best".
2. **Geen meters:** op het duikscherm staat "hold" boven de tijd. De zee wordt donkerder naarmate je langer inhoudt (3: 0:48 licht, 3b: 2:34 donker).
3. **Geen doelring en geen "next":** de oranje ring is weg. Op zijn plek, onder het dier: **live hartslag klein** (rood hartje plus getal, samen gecentreerd).
4. **Nieuw dier pas aan het eind:** scherm 6b komt na today, als de sessie is opgeslagen. Op het duikscherm zwemt je laatste dier mee als maatje (scherm 3: de kwal). Dat is gezelschap, geen beloning: het verandert niet door hoe lang je inhoudt.
5. **Zacht signaal na 3 min (3c):** "breathe when ready" in geel op de plek van de hartslag, de tijd loopt gewoon door. Rustig en zonder alarm, maar wel duidelijk.
6. **8 weeks:** acht kolommen water, hoogte is je **gemiddelde per sessie** in die week, onder elke kolom het **aantal dagen** dat je ademde. Deze week heeft een witte top en een wit cijfer. Onderaan "avg 1:44" en "5 days this week". Geen meters, geen doelring, geen record.
7. **Menu:** twee gelijke pillen, "Rounds 3 x 30" en "Calm 4-7-8", even groot; de gekozen is gevuld, de andere omlijnd. Daaronder "Sea log · Settings". De walvis blijft in het lage tij onderaan.
8. **Today:** de drie trechters blijven, tijden in wit, onder "avg 1:44" in grijs. Geen goud meer.
9. **Settings:** Breaths 30, **Pace normal** (gekozen, met pijltjes), Hold tick on, Rounds 3. "Buzz" staat er niet meer: Ebb trilt alleen (Gijs, logboek), dus een keuze "alleen trillen" zou niets doen.
10. **Sea log (8, 8b):** bovenaan 24 stippen in twee rijen (gevonden is schuim, nog niet is een open ring), daaronder één dier groot met naam en **hoe je het kreeg** ("3 days in a row"), onderaan "7 of 24". Omhoog en omlaag bladert. Een dier dat je nog niet hebt, staat er als silhouet met "?" en eerlijk wat ervoor nodig is ("50 sessions"). Geen raadsel, want verrassing zit in het moment van krijgen, niet in het zoeken.
11. **Veiligheid:** ongewijzigd (v3), bij de eerste start en elke 30 dagen (Gijs).

## De 24 dieren en wanneer je ze krijgt
Tellers van Gijs (`EbbTrouw`, 4fa11ef): sessies (rondes en rustig ademen tellen allebei) en beste reeks dagen op rij. Eén extra: "terug na een pauze". Regels: hoogstens één nieuw dier per sessie; halen twee tegelijk hun drempel, dan wacht het tweede tot de volgende sessie. Beste reeks telt, dus een gemiste dag pakt niets af. Bij ±4 sessies per week heb je de walvis na ±3 maanden.

| nr | dier | wanneer | getekend |
|---|---|---|---|
| 1 | Fish | 1e sessie | ja |
| 2 | Jellyfish | 2 sessies | ja |
| 3 | Crab | 2 days in a row | ja (nieuw) |
| 4 | Turtle | 3 days in a row | ja |
| 5 | Seahorse | 5 sessions | ja (nieuw) |
| 6 | Starfish | 7 sessions | ja (nieuw) |
| 7 | Octopus | 5 days in a row | ja (nieuw) |
| 8 | Pufferfish | 10 sessions | ja (nieuw) |
| 9 | Clownfish | 12 sessions | ja (nieuw) |
| 10 | Sea cucumber | back after a break (eerste sessie na 7 of meer dagen zonder) | ja (nieuw) |
| 11 | Ray | 15 sessions | ja (nieuw) |
| 12 | Dolphin | 7 days in a row | ja (nieuw) |
| 13 | Seal | 18 sessions | ja (nieuw) |
| 14 | Squid | 21 sessions | ja (nieuw) |
| 15 | Lobster | 10 days in a row | ja (nieuw) |
| 16 | Otter | 25 sessions | ja (nieuw) |
| 17 | Anglerfish | 28 sessions | volgende run |
| 18 | Manatee | 14 days in a row | volgende run |
| 19 | Shark | 32 sessions | volgende run |
| 20 | Swordfish | 36 sessions | volgende run |
| 21 | Manta | 21 days in a row | volgende run |
| 22 | Orca | 42 sessions | volgende run |
| 23 | Narwhal | 30 days in a row | volgende run |
| 24 | Whale | 50 sessions | ja |

**De grap, dier 10:** wie een week wegblijft, krijgt bij terugkomst de zeekomkommer, met halfdichte slaperige ogen: "Sea cucumber · back after a break". Geen schuldgevoel en geen verloren reeks, maar een knipoog. Dat vertellen mensen door.

Tekst op 6b: naam groot, eronder de reden in geel ("3 days in a row" / "10 sessions" / "back after a break"). Bij een reeks staan er zeven dagstippen onder (zoveel gevuld als de reeks, tot 7); bij sessies niet.

## Dieren v4 (`ebb-dieren-v4.png`)
Dertien nieuwe in dezelfde stijl als v3 (gevulde vlakken in MIP-kleuren, lijf, licht deel, donker deel, hetzelfde oog met glans): krab (oranje, nu vrij omdat de ring weg is), zeepaardje (geel), octopus (paars), zeester, kogelvis (geel met stekels), zeekomkommer (slaperig), clownvis, rog, dolfijn, zeehond, inktvis, kreeft en zeeotter (op zijn rug met een schelp). Daarmee staan er 17 van de 24; de nummers op het blad zijn die uit de tabel. Elk dier heeft een eigen kleur, zodat je de 24 op de sea log uit elkaar houdt. Gemeten: 0 pixels buiten MIP op 260 voor alle tien. Bekeken met Read op 454 en vergroot. Zwakste: de otter (leest pas als otter als je weet dat hij op zijn rug ligt) en het zeepaardje (wat hoekig). De zeekomkommer leest als een worstje, maar dat is hier de bedoeling.

Voor Gijs: dezelfde vorm als nu in `Teken.mc` (polygonen in eenheden van de diermaat, punten staan in `bron/ebb_dieren_v4.py`, functie `nieuwe_delen`). Volgende run teken ik de laatste zeven (Anglerfish, Manatee, Shark, Swordfish, Manta, Orca, Narwhal) en maak ik otter en zeepaardje beter.

## Gemeten (`blad4/meting-v4.txt`) en bekeken
- Kader van alles wat getekend is: binnen 0,5 px van het midden op alle 28 beelden.
- Optisch midden op 260: binnen 2,3 px op alle schermen (sea log -2,3 door het schildpadkopje links).
- Kleinste letter op 260: 20 px. 0 pixels buiten MIP op alle 14 schermen.
- Blad, dieren en de 260-beelden van menu, duiken, sea log en settings zelf met Read bekeken op ware grootte.

## Bouwbaar (voor Gijs)
- Hartslag: `Sensor.getInfo().heartRate`, hartje uit twee `fillCircle` en een `fillPolygon`; `null` = streepje "--".
- Zee donkerder: dezelfde `duik_zee` als v3, maar de stand volgt de tijd (0:00 licht, 3:00 donkerst) in plaats van meters; AMOLED kan met de drie vaste PNG's van v3.
- 8 weeks: `fillRoundedRectangle` per kolom met de waterbanden via `setClip`, cijfers met de gewone letter.
- Sea log: stippen `fillCircle` / `drawCircle`, één dier per pagina, omhoog en omlaag.
