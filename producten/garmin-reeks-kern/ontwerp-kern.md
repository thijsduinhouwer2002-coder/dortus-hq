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
