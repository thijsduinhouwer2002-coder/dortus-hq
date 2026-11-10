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

## Keuring 2 (10 nov 2026, ±16:25 UTC, handmatige run van de hoofdchat, "alle zeilen bij Ebb"): ja op voorwaarde

Bekeken: Mila's icoon, poster en zes kaarten (f012bcd, nog dezelfde als keuring 1, met Read ook op winkelformaat), de winkeltekst versie 2 van Gijs (88adb3f, alle drie de talen) tegen de code op de tak (f287bab plus 88adb3f), en de drie best verkopende betaalde ademapps live uit de winkel-API (10 nov, GEZIEN): WHM breathing+ ($4,99, 4,9, 604 reviews, 1.000+), Breath Training System PRO ($6,25, 4,7, 34 reviews, 100+), Breathe: Breathing Exercises ($2,99, 4,4, 18 reviews, 1.000+).

**Akkoord voor indienen: ja op voorwaarde** van de punten hieronder. Allemaal klein: Gijs één run (dieren, testgegevens, drie zinnen), daarna Mila één run (script opnieuw draaien). Ingediend wordt alleen met de nieuwe beelden en tekst; ik kijk ze na op alleen deze punten.

### Valt Ebb op in een rij zoekresultaten?
Ja. Zelf nagebootst op winkelformaat (icoon 150 px met naam, maker, prijs), licht en donker: `ontwerp/garmin/winkel/ebb-zoekrij-top3-licht.png` en `-donker.png`. De drie toppers zijn een foto van een persoon, een tekstbanner met horloge en een horloge met groene ring, alle drie donker en koel. Ebb is het enige getekende figuur en het enige warme vlak (koraal); de patrijspoort met bouten is in één oogopslag een eigen vorm. De titel zet de zoekwoorden vooraan ("Breath Hold, Breathwork") en wordt in de rij na twee regels afgekapt, maar het belangrijke staat voor de knip. Ook prijs gelijk aan de leider klopt: wij bieden meer (voortgang, eigen patroon, het uiterlijk).

### Winkeltekst: moet (Gijs)
- **T1. "Pause stops the clock; at the end you choose save or discard" klopt niet.** Een afgeronde rondesessie slaat zichzelf op (`EbbApp.mc` ±245); kiezen kan alleen in het pauzemenu onder de terug-knop. Wordt: "A finished session saves itself. Press back to pause: resume, save or discard." Ook in "Nagekeken".
- **T2. "One lap per round" en "hold time per lap" gelden alleen voor de rondes.** Rustig ademen slaat ook een ademactiviteit op (via Save in het pauzemenu), maar zonder laps en inhoudtijd (`RustigView.mc`). Wordt: "Breath hold sessions: one lap per round, with your hold time." Zelfde in DE ("eine Runde pro Lap") en NL ("een ronde per lap").
- **T3. "The water gets deeper every 15 seconds" belooft te veel.** Er zijn vier tinten, na 45 s wordt het niet donkerder (`EbbApp.mc` ±313); wat doorloopt is de diepte in meters. Wordt: "The hold is a dive: the water darkens, bubbles rise and the depth counts up." Mila: de ondertitel van kaart 1 "Deeper every 15 seconds" moet dan ook anders, bijvoorbeeld "The water darkens. Bubbles rise."

### Winkeltekst: kan
- Namen uit de app aanhouden: "4-7-8" en "Calm (5.5 in, 5.5 out)" in plaats van "4 7 8 breathing" en "Slow breathing".
- Bij de getijdenlijn "after each session" erbij, want je ziet hem na een sessie met omhoog en omlaag, niet vanuit het menu.

De rest klopt (controleur ging elke zin na met bestand en regel): stoppen met elke knop of tik, herstel, dieren op 60, 90, 120 en 180 s, Sea log, de patronen en het eigen patroon, duikprofiel met diepste stip, record in koraal, trillen per fase en uit te zetten, de instellingen, alleen de permissies Fit en FitContributor (dus geen data van het horloge), de negen horloges gelijk aan het manifest, geen review-vraag. Veiligheid en "wat Ebb niet is" staan er duidelijk in: goed.

### Winkelbeelden: moet (Gijs bron, Mila beelden)
De vijf punten van keuring 1 blijven, nu als B1 tot B5:
- **B1.** Eén verhaal in de testgegevens: beste tijd 3:0x op de getijdenlijn, duikprofiel met 3 rondes rond 1:40 tot 3:05 (nu 0:05 en "best 2:05" naast een ontmoete walvis).
- **B2.** Nieuwe walvis en schildpad in de app (Mila moet 3 en 4), daarna poster, kaart 1 tot 3 en de walvis in het icoon gelijk aan de app.
- **B3.** Kaart 6 op de fenix 8, een rustige stand (4-7-8 of Calm), getal boven de golf.
- **B4.** Geen belletje over het cijfer (frame uit de build met belletjes achter het cijfer kiezen).
- **B5.** Kaart 2: het dier groter of de walvis.
Plus de ondertitel van kaart 1 (zie T3).

### Kan (beelden)
Halve belletjes onderin naar binnen; donker nachtblauw boven het water in het icoon.

Waarom ja op voorwaarde en geen nee: de app is goed en eigen, de tekst is eerlijk op drie zinnen na, en de opbouw van de beelden is het sterkste in de rij. Wat overblijft is een tegenspraak in testgegevens, de walvis die de poster belooft, en drie zinnen. Dat zijn geen nieuwe ontwerpkeuzes.

Controleur (agent): ging elke bewering van de tekst na in de code; vond T2 en T3 en bevestigde T1. Overgenomen.

## Keuring 3 (10 nov 2026, 18:45 UTC): nakijkronde v2, nee door de walvis

Bekeken met Read: Mila's v2 op tak `claude/garmin-2026-11-10b` (dd460d0: icoon, poster, kaart 1, 2 en 6, rij `ontwerp/garmin/winkel/ebb-winkel-v2-rij.png`), de winkeltekst versie 3 (T1 tot T3 en beide kan-punten) en de tekencode van de dieren (`Teken.mc` walvis en schildpad, `EbbApp.mc` ±359). Daarbij het oordeel van Thijs zelf (19:33 NL, `berichten/daan.md`): de walvis is "niet mooi en heel makkelijk" en "staat niet in het midden".

**Akkoord voor indienen: nee.** Niet indienen met release `ebb-v1.0.0`: de walvis zit in de app zelf, dus er komt een nieuwe build en release.

**Ja, klaar en vast (niet meer aan zitten):**
- Winkeltekst versie 3: T1, T2, T3 en de kan-punten kloppen (regel 26, 39, 47, 48 en de patroonnamen in alle drie de talen).
- B1, B3, B4 en de ondertitel van kaart 1: gedaan. Kaart 6 (fenix 8, 4-7-8, getal boven de golf) is goed.
- Opbouw, koppen, icoonvorm met bouten, nachtblauw boven het water: blijft.

**Thijs heeft gelijk, en ik had dit zelf moeten tegenhouden.** In keuring 1 en 2 keurde ik de vorm van de walvis ("V-staart, spuitje, platte buik") op lijstje af in plaats van te vragen of hij mooi is. Naast elkaar op de poster: een vlakke rode veelhoek, de onderkaak is een losse spleet, geen buik, geen vin, het oog is een gat. Zo ziet clipart eruit, en de walvis is precies wat de poster verkoopt ("Meet the whale").

**Moet (op volgorde), geldt voor app, icoon, poster en kaarten:**
- **W1. Een walvis met karakter en diepte** (Mila tekent, Gijs bouwt in `Teken.mc`). Bolle kop die vloeiend naar de staartsteel loopt (geen knik), buik in de lichte tint `0xFFAAAA` met drie keelgroeven, een ronde borstvin die naar achteren hangt, een oog met een witte glans (stip van 40%), een bek als zachte lijn met de mondhoek omhoog (vriendelijk, geen spleet), het spuitje mag blijven. Alleen MIP-kleuren, geen verloop. Richting (geen eindontwerp, Mila is de baas over de stijl): `ontwerp/garmin/winkel/walvis-richting-daan.png`, bron `ontwerp/garmin/bron/walvis_richting_daan.py`, links in de patrijspoort, midden op 454 px, rechts op 260 px. Eén gesloten vorm: nu staat op de poster een lichte naad tussen buik en vin. Toets: op 260 px zie je nog buik, oog en vin.
- **W2. Het midden van de tekening is het midden van het dier.** Nu loopt de walvis van -11 tot +14,5 rond cx, dus hij staat altijd 1,75 eenheid rechts van waar de code denkt. Verticaal zit hij er nog verder naast: van -9,2 (spuitje) tot +3,4 (vin), dus 2,9 eenheden boven cy. Zet de punten zo dat het kader van het hele dier (met spuitje) rond (0,0) ligt, en haal dan het lapmiddel `yd = yDier + 0.06` (`EbbApp.mc` ±362) weg.
- **W3. Op het horloge in het midden onder de klok.** De dieren zwemmen nu in één beweging van rechts naar links door het beeld (`(1.1 - 1.2 * p) * d`), dus elk stilstaand frame vangt ze ergens onderweg. Beter voor beeld en gevoel: het dier zwemt in, blijft ±2 s rustig in het midden onder het getal hangen (heel licht op en neer), en zwemt dan door. Winkelbeelden kiezen een frame uit dat stuk.
- **W4. De patrijspoort-loep netjes gecentreerd.** Nu valt de kop links tegen de rand en de staart rechts eraf: het dier past niet in de loep. Het hele dier (met spuitje en staart) binnen ±78% van de binnenmaat, met het midden van het kader op het midden van de loep. Alleen het waterbeeld in de loep: nu vergroot de loep onderaan een zwarte boog en streepjes van de wijzerplaat mee. Geldt voor poster en kaart 2.
- **W5. De schildpad dezelfde ronde.** Zelfde probleem: het schild met losse kruislijnen leest als een gebroken bord, de pootjes als losse plakjes. Schild met een lichte rand of plaatjes in `0xFFAAAA`, kop met oog en glans, peddels als één vloeiende vorm. Vis en kwal kijken we mee na; ze zijn klein en kort in beeld, maar moeten bij dezelfde familie horen.
- **W6. Het icoon gelijk aan de nieuwe walvis**, ook gecentreerd in de patrijspoort.

**Volgorde:** Mila tekent W1, W5 en W6 (bron in `ontwerp/garmin/bron/`), Gijs bouwt W1 tot W3 en W5 in de app, groene test op de negen horloges, release `ebb-v1.0.1`; Mila draait haar script opnieuw met W4. Daarna kijk ik alleen W1 tot W6 na, op winkelformaat én op het echte formaat van het horloge. Tekst en de rest van de beelden zijn al ja.

**De vraag die ik nu bij elk dier stel:** zou een koper de poster stilzetten om naar de walvis te kijken? Bij v2 is het antwoord nee.

Controleur (agent): W1 tot W6 kloppen met de plaatjes en de code. Vond erbij: de walvis zit ook verticaal 2,9 eenheden scheef, de loep vergroot de rand van het horloge mee, en een naad tussen buik en vin; overgenomen in W1, W2 en W4. Over mijn richting-schets: beter, maar de keelgroeven zijn op dit formaat bijna onzichtbaar, de snelheidsstreepjes achter de staart botsen met W3 (stil in het midden) en trekken het kader scheef, er staat geen getal in om "onder de klok" te toetsen, en het oog met glans haalt 260 px maar net. Daarom is het een richting, geen eindontwerp: Mila laat de streepjes weg of alleen tijdens het in- en wegzwemmen, en maakt oog en groeven groot genoeg voor 260 px.
