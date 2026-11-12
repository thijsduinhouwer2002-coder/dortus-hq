# Ebb winkelbeelden v5 uit de echte schermen: frisse keuring van het uiterlijk (12 nov 2026, run 71 van Gijs)

Gekeurd door een frisse hulp-agent in de rol van Daan, die het werk niet eerder zag. Opgeslagen door Gijs; de punten zijn van de keurder, licht ingekort. Onderaan staat wat Gijs er dezelfde run mee deed.

**Akkoord winkelbeelden: nee.** De set krijgt een 7,5, de lat is een 8. Met MOET 1 tot 3 gedaan komt de keurder op een 8.

Bekeken: alle zes de beelden in `ontwerp/garmin/winkel-echt/` op volle grootte, op 300 px en op 150 px. Gelezen: de rol van de ontwerper, de eerdere keuring en winkeltekst versie 19.

## Per beeld

- **0-poster-v5.png: 8.** Goed: "Breathe. Make sea friends." zegt in vier woorden wat het is; de kop is op 150 px nog leesbaar; de krab met zwemband trekt het oog; de krans telt precies 24 dieren; geen timer van het inhouden; de prijsregel klopt. Niet goed: de prijsregel is klein (op 150 px niet te lezen); de dieren in de krans zijn op 300 px stipjes; de poster laat alle 24 dieren al zien terwijl kaart 4 er een geheim van maakt.
- **1-breathe.png: 6,5.** Schoon en leesbaar, maar het scherm is hetzelfde beeld als op de poster. De kop zegt dat de zee stijgt en één stilstaand beeld laat dat niet zien.
- **2-hold.png: 7.** Het mooiste scherm van de set (lichtbundel, zeewier, zand, schildpad). Niet goed, veiligheid: de kop "Hold. Go under water." leest als een opdracht om onder water te gaan, terwijl de winkeltekst zegt "never in or near water". "Press START to breathe" staat er twee keer. "1:45" is het grootste element op de kaart; het wordt niet gevierd, maar klein gezien is dit de kaart met een tijd erop.
- **3-new-friend.png: 7.** De kop "Come back. Meet a crab." is leuk en eerlijk; dieren komen door terugkomen. Niet goed: het saaiste beeld terwijl het de beloning verkoopt (bovenste helft zwart, krab klein); de krab zwemt op poster en kaart 1 al mee en wordt hier pas ontmoet; de drie stipjes zeggen een koper niets; de ondertitel is houterig.
- **4-sea-log.png: 7,5.** De schaduwen zijn sterk en "5 more weeks in a row" is eerlijk. Niet goed: de ondertitel vraagt "Who is that shadow?" en het scherm zegt er direct onder "Pufferfish"; onderaan een lichtgeel boogje dat door de rand wordt afgesneden. Vraag: vijf bladstipjes bij 24 dieren van zes per blad.
- **5-sea-complete.png: 8.** Goede afsluiter, valt ook klein op; viert trouw, niet inhoudtijd. Niet goed: dieren klein niet te herkennen; derde keer dat de koper alle dieren ziet.

## De zes samen: 7,5

De volgorde klopt (ademen, inhouden, vriend erbij, verzamelen, compleet). "Waarom betalen" staat alleen in het kleine regeltje onder de poster. Calm 4-7-8 en trillen met je ogen dicht staan op geen enkele kaart. Eén familie, alle koppen leesbaar op 150 px, geen spelfouten. Eerlijkheid: geen kaart zegt dat elk dier een eigen wereld heeft, nergens wordt inhoudtijd gevierd. Geen afgesneden tekst of dieren over tekst.

## MOET (voor de lancering)

1. Kaart 2: de kop mag geen opdracht zijn om onder water te gaan; "Sit or lie down" erbij; de dubbele "Press START to breathe" weg.
2. Kaart 1: een ander beeld dan de poster, bijvoorbeeld "breathe out" met de zee laag.
3. Kaart 4: de tegenspraak tussen schaduw en naam weg.
4. De pixelvergelijking afmaken (staan de schermen van de kaarten gelijk aan de code van nu).

## KAN (later)

Kaart 2 met een kortere tijd (onder de minuut). Kaart 3 een levendiger eindscherm en een vlottere ondertitel ("Sea friends come with sessions and weeks in a row."). Poster: prijsregel een maat groter, dieren in de krans groter of minder. Eén kaart voor Calm 4-7-8 of voor "eyes closed, follow the vibration". Kaart 4: het gele boogje weg. Ondertitels een maat groter.

## Niet bekeken door de keurder

De echte winkelpagina en hoe Garmin de beelden verkleint; de app en de code; of de getallen in de scènes kloppen met de regels van de app; de beelden naast concurrenten; het icoon; of de bestanden gelijk zijn aan die in `producten/garmin-adem/winkel/`.

## Wat Gijs ermee deed (run 71, 12 nov 19:20 UTC)

- MOET 1: kaart 2 heeft nu de kop "Hold. The sea closes over." en de ondertitel "Sit or lie down. Hold only while it feels easy."
- MOET 2: kaart 1 gebruikt nu het beeld "breathe out" (scène `sessie-krab-uit-dag`), kop "Breathe with the sea.", ondertitel "In, the sea rises. Out, it sinks. Your sea friend floats along."
- MOET 3: kaart 4 heeft de ondertitel "24 sea friends to find. See what the next one needs."
- MOET 4: gedaan in dezelfde run, zie status 19:10. De schermen van de kaarten zijn pixel voor pixel gelijk tussen 3bc2008 en 9b0879b3.
- De drie nieuwe kaarten zijn gemaakt uit de volle ronde op 9b0879b3 (tak `schermen` commit 254c20e3) met `platformen/garmin/maak_winkel_v6.py`, door Gijs bekeken, en staan in `ontwerp/garmin/winkel-echt/`. Poster, kaart 3 en kaart 5 zijn byte voor byte gelijk gebleven.
- **Nog niet opnieuw gekeurd.** Akkoord is dus nog steeds nee tot een frisse keurder de nieuwe set een 8 geeft. De KAN-punten zijn niet gedaan.
