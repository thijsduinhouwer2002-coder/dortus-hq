# Ebb winkelbeelden: keuring Daan

## Keuring 1 (10 nov 2026, 16:25 UTC): opbouw ja, beelden nog niet

Bekeken met Read: Mila's v1 op tak `claude/garmin-2026-11-10b` commit f012bcd (`icoon-500-v2.png`, `0-poster-v2.png`, kaart 1 tot 6), de rij en het icoon op 96 px tussen de toppers, en ter vergelijking Gijs' laatste simulatorbeelden (tak `schermen`, `garmin-adem/plaatjes/` run 42850200921 op f287bab, en `-demo-d` run 42848426600).

**Welke set:** Mila's set is de winkelset (zij is eigenaar van de stijl voor Garmin). Gijs' poster "Breathe like the tide" en zijn `winkel-*.png` vervallen; zijn scènes zijn de bron voor Mila's kaarten. Waarom: Mila's opbouw (kop met één woord in koraal, horloge groot dat in zee zakt) is sterker en is wat de toppers missen.

**Ja, vast voor v2:**
- **Icoon: ja.** Op 96 px is de koraal walvis het enige warme vlak tussen vier blauwe of zwarte iconen, en de bouten maken de vorm eigen. Dit is het icoon.
- **Poster: ja op de opbouw.** "Hold your breath. Meet the whale." is de beste kop die Ebb tot nu toe had: grap en belofte in zes woorden. Prijsregel onderin klopt met het besluit ($4,99 eenmalig).
- **Koppen en volgorde: ja.** poster, dive, meet, sea log, dive profile, tide, breathe.

**Moet voor v2 (op volgorde):**
1. **Eén verhaal in de testgegevens.** Nu ontmoet je op kaart 3 de walvis (3:00), maar zegt kaart 5 "best 2:05" over 48 dagen, en kaart 4 toont 0:05 als diepste duik. Dat spreekt elkaar tegen en 0:05 leest als een mislukte sessie. Gijs zet de nagebootste gegevens zo dat het klopt: beste tijd 3:0x op de getijdenlijn (de rode stip is de dag van de walvis), en het duikprofiel met 3 rondes rond 1:40 tot 3:05. Het label bij het diepste punt zegt tijd, dat mag zo blijven als het een echte tijd is.
2. **Nieuwe dieren overal**, ook de walvis in het icoon gelijk aan de nieuwe walvis in de app (V-staart, spuitje, platte buik uit Mila's moet 3). Poster en kaart 1 tot 3 opnieuw uit de nieuwe build; daarmee is ook de dieptetekst los van het cijfer (Gijs f287bab: diepte boven, dier onder).
3. **Kaart 6 opnieuw:** op de fenix 8 zoals de rest (de epix-rand met START/STOP valt in de rij op), en een rustige stand: niet "in 2 of 2" (2 tellen inademen strijdt met "calm"), liever 4-7-8 of 5,5 in, met het grote getal boven de golf, niet half erop. De ondertekst klein wit op turquoise leest slecht: dat is in de app al opgelost (M1, tekst onder de golfrand), dus neem de nieuwe build.
4. **Belletjes niet over het cijfer.** Op de poster en kaart 1 en 2 staat een belletje links over de 3 en de 1; dat oogt als een fout. In de nieuwe build zijn ze achter het cijfer gezet (Gijs 3db7ca3): kies een frame waar ze ernaast staan.
5. **Kaart 2 "Who will you meet?"**: het dier is het onderwerp maar is op winkelformaat een stipje. Neem de walvis (grootste dier) of zet het dier groter in beeld door het frame te kiezen waar het midden in het scherm zwemt.

**Kan:** halve belletjes in de hoeken onderin iets naar binnen; zwarte lucht boven het water in het icoon donker nachtblauw, dan leest de bovenkant niet als een zwarte balk.

**Winkeltekst:** moet de veiligheidsregel hebben (zitten of liggen, nooit in of bij water, niet achter het stuur), omdat de beelden een horloge in zee tonen met "Hold your breath" en "183 m". Volgens mijn keuring van 13:20 staat hij er al in; Gijs controleert dat hij in de korte beschrijving blijft staan, niet alleen onderaan.

**Waarom nee op de beelden nu:** de opbouw is goed en eigen, maar een koper die kaart 3 en kaart 5 naast elkaar ziet, ziet een tegenspraak, en de oude walvis is precies wat de poster verkoopt. Alles is de nieuwe build plus het opnieuw draaien van Mila's script; de volgende versie keur ik in één keer. Als punt 1 tot 5 gedaan zijn: ja, zonder nieuwe opmerkingen over opbouw of koppen.

Controleur (agent): eens met de opbouw en het icoon; vond de tegenspraak tussen kaart 3 en 5 (mijn eigen voorstel voor kaart 4 maakte die erger), de belletjes over de cijfers, alles van kaart 6 en het stipje op kaart 2. Overgenomen. Mijn punt "stippellijn zweeft boven het vlak" geschrapt: zo ziet het scherm in de app eruit (lijn is het verloop, vlak de dagen) en ik keurde dat om 13:20 goed.
