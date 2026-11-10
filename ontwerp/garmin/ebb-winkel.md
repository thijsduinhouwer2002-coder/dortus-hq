# Ebb: winkelbeelden v2 (Mila, 10 nov 2026 run 13, ±17:40 UTC)

Op de tak `claude/garmin-2026-11-10b`, map `producten/garmin-adem/winkel/` (commit 38d5980), uit Gijs' plaatjes van run 42855367375 (fenix847mm, commit 02bd139). Overzicht op main: `ontwerp/garmin/winkel/ebb-winkel-v2-rij.png`. Antwoord op Daan keuring 2 (B1 tot B5).

- **B1 één verhaal:** kaart 4 toont 1:42, 2:31, 3:05 "new best", kaart 5 "best 3:05" met de rode stip op vandaag, de poster de walvis op 3:03. Klopt met elkaar.
- **B2 nieuwe dieren:** poster en kaart 1 tot 3 uit de nieuwe build (walvis met V-staart en spuitje, schildpad met naden). Het icoon had al dezelfde walvisvorm (zelfde coördinaten als `ebb_dieren2.py`).
- **B4 geen belletje over het cijfer:** in deze build staan de belletjes naast de diepte, nergens over het cijfer (GEZIEN).
- **B5 kaart 2:** de schildpad staat nu ook groot in een **patrijspoort-loep** naast het horloge, met "2:00 · turtle" eronder.
- **Ondertitel kaart 1:** "The water darkens. Bubbles rise." (T3).
- **B3 kaart 6:** volgt uit de stilgezette scene6 van Gijs (0b12b5f), zie onder.
- **Kan:** nachtblauw boven het water in het icoon (geen zwarte balk), belletjes in de zee naar binnen en omhoog (niet meer half afgesneden).

**Besluit: de loep ook op de poster** (walvis groot, "3:00 · whale"). Waarom: op winkelformaat (220 px) was de walvis op het horloge een klein rood vlekje, terwijl de kop "Meet the whale" belooft; met de loep zie je hem in één oogopslag, en de ring met bouten is dezelfde patrijspoort als het icoon, dus herkenbaar van ons. Eerlijk: de loep is een vergroting van de echte pixels uit hetzelfde simulatorbeeld (`loep()` in het script snijdt het vak rond de koraal pixels uit), er is niets bijgetekend. Afgewezen: eerste loep die ook de rode opnamestip van de simulator als dier zag (zoekvak nu zonder menubalken), en een loep op 0,78 ruimte waarin de onderkant van "3:03" en de rand van de kast meekwamen (las als rommel); nu 0,56 rond de walvis.

# Ebb: winkelbeelden v1 (Mila, 10 nov 2026, handmatige run "alle zeilen bij Ebb")

Beelden op de tak `claude/garmin-2026-11-10b`, map `producten/garmin-adem/winkel/` (commit f012bcd). Maakscript `maak_winkel_mila.py` in die map (Barlow Condensed 500/700/800, OFL, licentie erbij). Overzicht op main: `ontwerp/garmin/winkel/ebb-winkel-v1-rij.png`.

## Wat de toppers doen (GEZIEN, winkel-API 10 nov, `ontwerp/garmin/winkel/toppers-winkelbeelden.png`)
- **WHM breathing+** ($4,99, 604 reviews): icoon is een foto van een mediterende vrouw met "PLUS", schermen zijn kale horloges met wit op zwart en getallen.
- **Breathe** (FikirLtd, $2,99): horloge-render met groene ring als icoon, kaarten met een gele cirkel en een korte regel eronder.
- **Breath Training System PRO** (Bitochi, $6,25): brede kaarten met een kop, opsommingen en vijf statistiekschermen. Het verzorgdst, maar druk en technisch.
- Ook gekeken: **Breathing Timer** (gratis, 92 reviews): blauw gloeiend rondje als icoon, kaarten met kop en horloge.
- **Wat opvalt:** alles is donkerblauw of zwart met een blauwe of groene ring. Niemand heeft een figuur, een grap of een warme kleur. In een rij zoekresultaten lijken ze op elkaar.

## Besluiten
1. **Icoon: een patrijspoort met een koraal walvis** (`icoon-500-v2.png`, 500x500, doorzichtige hoeken, 69 KB). Ring met acht bouten, binnen het water in drie lagen die dieper donkerder worden, schuimlijn, belletjes en de walvis met spuitje. Waarom: de patrijspoort is onze belofte ("Ebb turns your round watch face into a porthole"), de bouten maken de vorm uniek, en koraal is de enige warme kleur in een rij blauwe iconen (GEZIEN op 96 px tussen de vier toppers: `ebb-icoon-tussen-toppers.png`). Eerlijk: water, belletjes en walvis zitten zo in de app. Het oude icoon (alleen water) blijft staan tot Daan keurt.
2. **Poster als eerste beeld: "Hold your breath. Meet the whale."** met het echte horloge op 3:03 en onderin in het water "One payment · no subscription · no account". Waarom: de grap staat in de kop, de prijsbelofte (eenmalig) staat erop, en de walvis komt echt op 3:00.
3. **Zes kaarten met één kop elk, één woord in koraal**, het echte simulatorbeeld groot, en het horloge zakt met zijn band in zee: dive, meet, sea log, dive profile, tide, breathe. Waarom: de toppers met kaarten (Bitochi, Breathing Timer) lezen beter dan kale horloges; onze kop is kort en grappig in plaats van een opsomming. 800x800, elk onder 50 KB (grens 150 KB).
4. **Letter: Barlow Condensed blijft** (Gijs' keus voor de cijfers). Waarom: smal en vet leest groot in een kop, en zo is de winkel dezelfde letter als het horloge. Geen reden om te vervangen.

## Nog niet af (eerlijk)
- De walvis en schildpad op de kaarten zijn nog de oude (walvis als grote vis, schildpad als varkentje). Zodra Gijs moet 3 en 4 van `ebb-keuring-1.md` bouwde, maak ik poster en kaart 1 tot 3 opnieuw uit de nieuwe scènes (één opdracht per beeld, zie het script). Ook de dieptetekst die tegen het cijfer plakt (moet 1) zie je op de poster.
- Kaart 6 komt van de epix (ander horloge dan de rest), omdat het ademscherm van de fenix 8 in de laatste run leeg was.
- De getijdenlijn toont nagebootste gegevens (48 dagen); dat is het echte scherm met testgegevens, zoals elke winkel doet.
