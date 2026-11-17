# De kern van de reeks: ontwerp (Gijs, run 125, 16 nov 2026)

Volgt `bouwen-in-stappen`. Dit is stap 1 tot 4; er is in deze run nog niets van gebouwd. De proeven 1 tot 3 staan in `ontwerp.md` ernaast en blijven wegwerpcode.

## 1. Wat en voor wie
De kern is het deel dat elke wijzerplaat van de reeks deelt: maten per scherm, vier thema's, drie velden naar keuze, het getal van Body Battery, een slaapstand die binnen de regels van Garmin blijft, en een gratis en een betaalde versie uit dezelfde bron. Voor wie: de drager van een Garmin die in één blik tijd en lijf wil lezen, en voor ons: plaat 2 en verder zijn daarna vooral tekenwerk.

**Af als (alles toetsbaar):**
1. De toetsen in de simulator zijn groen, waaronder: de maten voor 208, 260 en 454 zijn gelijk aan `ontwerp/garmin/reeks/maten-tij-tabel.md` van Mila (elke rij, op de pixel).
2. Het pakket bouwt voor alle horloges in het manifest, gratis en betaald elk met een eigen manifest (`IQ_PROEF ja` twee keer in `uitslag.txt`).
3. Op fenix847mm, venu3s en vivoactive5 (AMOLED) zet het slaapbeeld minder dan 8% van de pixels binnen het scherm aan (marge onder de 10% van Garmin), geteld op de schermafbeelding door een script in de bouwstraat, en twee slaapbeelden na elkaar staan 1 tot 4 px van elkaar.
4. Geheugen na het laden op fr55 en fr245: minstens 40.000 bytes vrij (regel `KERN GEHEUGEN` in `uitslag.txt`).
5. Wakker en slaap op acht horloges als blad bekeken door mij, daarna door Daan.
6. Zonder gegevens (geen Body Battery, geen hartslag, geen geschiedenis) staat er een streepje en stopt de app niet: een toets per geval.

## 2. Code die er is (tak `claude/garmin-reeks-kern`, 2999205)
- `source/KernView.mc` 25 tot 59: lezen en geheugen meten; 74 tot 88: het slaapbeeld van de proef (tijd vol in lichtgrijs: te veel pixels, zie `platformen/garmin/reeks.md`); 90 tot 157: tekenen met vaste proefwaarden ("MON 16", "61").
- `source/Lees.mc` 12 tot 72: geschiedenis van Body Battery en stress, met `has` voor oude horloges; 74: weer per uur. Dit blijft.
- `source/Teken.mc` 9 tot 32: `profiel` (veelhoek uit waarden), 34 tot 45: `golf`. Blijft; de zee van Tij komt hier bij als Daan ja zegt.
- `maak_proefbeelden.py` 24 en 72 tot 77: maakt de vier letters per schermmaat. Wordt de maker van alle maten.
- `.github/workflows/garmin-reeks-kern.yml` 33 tot 80: bouwt, start acht horloges, maakt drie schermafbeeldingen en `uitslag.txt`.
- Voorbeeld van gratis en betaald uit één bron in onze eigen code: Ebb en Ebb Calm (`producten/garmin-adem`), eerst lezen hoe dat daar met de jungle is gedaan voor ik het hier anders doe.

## 3. Open vragen, zelf beantwoord
- **Welke slaapstand?** Tijd als omtrek of dun, grijs, elke minuut verschuiven (regels Garmin, gemeten 13% bij de volle dikke tijd). De vorm kiest Mila (gevraagd 23:05 UTC). Tot dan bouw ik gewicht 300 als extra letter voor de tijd (±600 bytes op nieuwe horloges, proef 3; alleen in de mappen voor AMOLED). Een omtrek vraagt ook een eigen letter, dus wisselen kost later alleen een ander plaatje.
- **Welke velden?** Eerste versie: hartslag, stress, stappen, calorieën, trappen, intensiteitsminuten, afstand, accu van het horloge, weer (temperatuur). Op nieuwe horloges via de kant-en-klare velden van Garmin, op oude rechtstreeks (proef 1: Forerunner 55, 245 en Instinct 2 hebben ze niet). Gratis: drie vaste velden (hartslag, stress, stappen). Betaald: kiezen.
- **Gratis op slot zetten later?** Nee. Besluit in `reeks.md` de kern punt 4: gratis blijft gratis, geen proef, geen code.
- **Wat bij te weinig geheugen?** De kern laadt geen schermvullend plaatje (proef 2: 5.512 bytes over op de Forerunner 245). Alles wordt getekend.
- **Instinct 2?** Niet in de eerste versie van de betaalde (Mila, 23:05 UTC); in de gratis pas met een eigen opmaak. Dus eerst niet in het manifest.
- **Naam en beeld?** Niet nodig om de kern te bouwen. Het manifest krijgt een werknaam; de echte naam komt van Chris.
- **Volgorde van de geschiedenis?** Op de tijd van elke waarde sorteren, niet op de volgorde vertrouwen (proef 1).

## 4. Drie aanpakken voor de maten, en de keuze
1. **Rekenen op het horloge** uit de schermmaat met de verhoudingen van Mila (0,638 S en zo). Klein, één plek. Nadeel: afronden op het horloge kan een pixel afwijken van haar blad, en dat zie je bij een rand van 2 px.
2. **Een tabel in de broncode** met alle acht maten. Precies. Nadeel: elke maat kost geheugen op elk horloge, ook op de Forerunner 55.
3. **Per schermmaat een klein gegevensbestand, gemaakt door hetzelfde script als het blad van Mila.** `maak_proefbeelden.py` leest de getallen uit `maten_blad_tij.py` en schrijft per map (`resources-round-208x208` en verder) de letters en een lijst met maten. Het horloge laadt alleen zijn eigen lijst. Precies gelijk aan het blad, geen dubbele getallen, weinig geheugen. Nadeel: een maakstap erbij, en de toets moet bewaken dat de gemaakte bestanden bij het blad passen.

**Gekozen: 3.** Reden: het blad van Mila is de waarheid en mag niet uit elkaar lopen met de code (zo deed zij het zelf ook: blad en proef uit dezelfde getallen). De toets van punt 1 bij "Af als" bewaakt het.

**Gratis en betaald:** twee manifesten en twee jungles (`gratis.jungle`, `betaald.jungle`) op dezelfde bron, het verschil met een vlag in de bron die de jungle weglaat, zoals bij Ebb en Ebb Calm als dat daar zo werkt (stap 2, nog lezen).

**Volgorde van bouwen (kleine stappen, na elke stap de bouwstraat):** (a) maten uit het script, met de toets; (b) thema's en de drie velden met echte waarden en streepjes; (c) slaapstand met het telscript in de bouwstraat; (d) instellingen in Garmin Connect; (e) gratis en betaald; (f) meer horloges. De zee van Tij komt na het nieuwe ja van Daan (zie `reeks.md`: het idee bestaat al bij Tide Line).

**Keuring (stap 6):** een aparte agent leest de code na (c) en na (e); Daan keurt het beeld.

## Run 128 (17 nov ±02:15 UTC): dunne tijd in de slaapstand en letters voor alle acht ronde maten
- **Wat en voor wie:** op een horloge met een scherm dat kan inbranden (AMOLED) moet in de slaapstand minder dan 8% van het scherm aan staan (regel Garmin: 10%). Af is: `SLAAP_TELLING goed` in de bouwstraat, met elk proefhorloge op de letters van zijn eigen schermmaat, en geen geheugenfout op de Forerunner 245.
- **Drie aanpakken:** (1) de dikke tijd donkerder grijs: telt niet, een pixel die aan staat blijft aan. (2) de tijd als omtrek: ook een eigen letter, en dunne omtrekken worden op 208 tot 260 px rafelig. (3) dezelfde letter in gewicht 300 als eigen letter `TijdSlaap`. **Gekozen: 3.** Rekensom op 390, 416 en 454 px: de dikke tijd alleen zet ±12,3% aan, de dunne ±4,3%. De vorm blijft een keuze van Mila; kiest zij omtrek, dan is het alleen een ander plaatje in `tijdslaap.png`.
- **Geheugen:** `TijdSlaap` wordt alleen geladen als het horloge zegt dat het scherm kan inbranden (`requiresBurnInProtection`). Horloges met een MIP-scherm (zoals de Forerunner 245) laden hem niet en tekenen in de slaapstand de gewone tijd.
- **Letters:** `maak_proefbeelden.py` maakt nu de vijf letters voor 208, 218, 240, 260, 280, 390, 416 en 454 px en stopt als zijn maten niet bij het blad passen. Schermen zonder eigen map (360 px, Venu Sq, Instinct 2) houden de letters van 260 px tot Mila een kolom geeft.
- **Blad van Mila bijgewerkt (17 nov 01:55 UTC):** rand om het BB-getal 1 px tot 359 en 2 px vanaf 360, water bij 100 iets lager; de rij "ruimte-eis" slaat `maak_maten.py` over (toets voor het ontwerp, geen maat voor het horloge).
- **Waarschuwingen van het pakket gelezen (run 129, run 44003040607, GEZIEN in `uitslag.txt`):** twee soorten. (1) 96 keer `Maten.mc:63 Statement is not reachable`: de controle op het soort getal kon nooit waar zijn, want de lijst is al een lijst van hele getallen. Weggehaald; de toets `testMatenVan260` kijkt de lijst na. (2) 64 keer het startpictogram: ons proefplaatje is 40 x 40 en elk horloge wil zijn eigen maat (35 tot 70 px), dus Garmin schaalt het. Voor de proef maakt dat niet uit. Voor de echte plaat: één pictogram per maat (35, 36, 40, 54, 56, 60, 61, 62, 65, 70 px), zoals bij Ebb; Mila tekent het, taak in `platformen/garmin/taken.md`.

## De zee (run 130, 17 nov ±04:10 UTC), na het ja van Daan van 03:50 UTC
- **Wat en voor wie:** de onderkant van de wijzerplaat wordt de zee uit de proef van Mila: vier gekleurde banden die dezelfde waterlijn volgen, de lijn zelf uit het verloop van Body Battery van de laatste vier uur, het bootje op "nu", en het getal met rand en golfje. Voor de drager: in één blik zien hoe de dag liep. **Af als:** (1) de acht nieuwe toetsen `testZee...` groen; (2) op fenix847mm, venu3s, fr255 en fr245 vult de zee de onderkant tot de rand, alle banden volgen één vorm, het bootje staat erop en het getal heeft een golfje (de punten a tot e van Daan), door mij gezien en daarna door Daan; (3) geen geheugenfout op fr55 en fr245; (4) `zee_ms` in `uitslag.txt` gelezen.
- **Code die er is:** `source/KernView.mc` (`tekenBoven`, de oude plek van de zee in `onUpdate`), `source/Teken.mc` (`profiel`, bleef voor het slaapbeeld), `source/Maten.mc` (WATER_TOP tot GOLF_AFSTAND stonden al klaar), `source/Thema.mc`, en het voorbeeld `ontwerp/garmin/reeks/stijl_proef_v3.py` en `stijl_proef_v5.py`.
- **Open vragen, zelf beantwoord:** *Geen Body Battery?* Een vlakke zee halverwege, geen bootje, een streepje als getal: de plaat blijft mooi en liegt niet over een stand. *Eén meting?* Vlakke zee op die hoogte met het bootje. *64 kleuren?* Vaste paletkleuren per thema (voorstel Daan, `Thema.mipBanden`), herkend aan "scherm kan niet inbranden"; Mila kiest de kleuren nog. *Regel 3 uit proef 5 (plafond zakt)?* Zit al in de maat "water bij 100" van het blad, dus niet apart gebouwd.
- **Drie aanpakken:** (1) de oude veelhoek oprekken tot de rand: snel, maar de lagen volgen dan niet dezelfde lijn (punt b van Daan). (2) de zee één keer in een eigen beeldbuffer tekenen en die elke seconde plakken: snelst bij het tekenen, maar een buffer van het halve scherm past niet op de Forerunner 245 (proef 2: 5.512 bytes over). (3) één waterlijn uitrekenen (31 punten) en die vier keer verschoven als vlak vullen, alles rekenwerk in een eigen module `Zee` zonder scherm. **Gekozen: 3.** Past in het geheugen, is na te kijken met toetsen, en volgt het script van Mila regel voor regel. De tijd per beeld meet de bouwstraat (`zee_ms`); is dat op een oud horloge te veel, dan de lijn alleen opnieuw rekenen als de gegevens veranderen.
- **Volgorde op het scherm:** zwart, zee, lijn, bootje, getal met rand en golfje, daarna datum, tijd en velden. Het getal schuift omhoog als water of zeil te dichtbij komt (ruimte minstens 4 px op 208).
- **Niet in deze stap:** het bootje als omtrek in de slaapstand (kan van Mila), de kolom 360 en niet-ronde schermen.
