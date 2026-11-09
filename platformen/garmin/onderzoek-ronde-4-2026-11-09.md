# Ronde 4: beginnen bij wat al verkoopt (9 november 2026, Gijs en een onderzoeker)

Methode: kassa-apps sinds 1 jan 2025 uit de dataset (`platformen/verkenner/data/garmin-niet-wijzerplaten-2026-11-09.json.gz`), gesorteerd op reviews per maand; spellen, tellen met de versnellingsmeter, Bluetooth en alles uit ronde 1 tot 3 weggestreept. Reviews via de winkel-API (let op: `pageSize` hooguit 20 tot 30, 50 geeft "Invalid pageSize!").

## Groot nieuw feit: appfabrieken vullen elke hoek
- **ThijsGer** (niet van ons) heeft 187 apps in de winkel sinds 2 juni 2026: 81 betaald via de kassa (allemaal $1,99) en 106 gratis, van cafeïne en ploegendienst tot sterrenkaart, valkerij en klaverjassen. 83 apps hebben 100+ downloads (79 daarvan betaald), 167 hebben 0 tot 2 reviews (GEZIEN, dataset, nageteld door controleur).
- Andere makers met reeksen: Dialforge, ChanDigital (racketsport), Multipassionate ($8,49 per sport), Strafe (Hero-reeks), VeloroLabs (trainingsdata, $2,25 per glance) (GEZIEN).
- Gevolg: een "lege hoek" bestaat bijna niet meer, en wat vandaag leeg is, heeft over een maand een fabrieksapp. **Winnen kan alleen door in een bewezen hoek duidelijk de beste en mooiste te zijn**, niet door een gat te vinden. De nieuwkomers die 1.000+ halen zijn juist de verzorgde: Multipassionate $8,49 (Hybrid Smash 1.000+, 50 reviews), ROXZONE, Peak Finder Compass van Rampo ($3,49) (GEZIEN). Dat past bij Thijs: bijzonder, mooi, eerlijk.
- Vraag die ik nog niet kan beantwoorden: verdient ThijsGer met 79 betaalde apps op 100+ echt geld (100 tot 999 kopers per app, dus $200 tot $2.000 per app, GOK), of zijn veel downloads van hemzelf of van gratis periodes? Na te kijken.

## Top 3 van de onderzoeker (cijfers GEZIEN tenzij anders vermeld)
1. **Ploegendienst-kalender.** Shift Calendar (VAW.BE): $1,99, 1.000+, 4,4 met 115 reviews sinds sep 2024 (±4,4 per maand), plus een proefversie met 24 reviews. Klachten: "The program will not loop a schedule. Example. 5 week rotation...", "Cannot ... add in 14 days, 14 r&r, 14 nights". Garmin heeft geen ploegenkalender (GOK, niets gevonden). Volledig te testen in de simulator (datumrekenen en een glance). Maar ook hier komen ze bij: Shift van Mellazure ($2,99, sep 2026), ShiftPilot, Shift Calendar van Dialforge en van DMSWatchApps (nog zonder datum, dus net ingediend), plus ShiftPay en Circada van ThijsGer (ander doel). Ik telde zelf 3 echte nieuwe ploegenkalenders sinds aug.
2. **Bergtoppen-kompas.** Peak Finder Compass (Rampo): $3,49, 1.000+, 30 reviews sinds mei 2026. Klacht: "there is no cell signal to pull peak data". Twee nieuwe op 3 nov 2026 (Peak Finder van RAlpha gratis, Peak Horizon $3,99). Rampo is sterk; zie ronde 3.
3. **Vliegtuigradar.** Flight Scanner Pro: $2,99, 1.000+ in 3 maanden, 28 reviews (±9 per maand, het hoogste van alle nuttige apps). Klachten: batterij leeg door ophalen op de achtergrond, "stuck at that location", crasht. Maar 5 nieuwkomers sinds aug (LARA $3,75, Wingwatch $1,99, Overhead, Flight Tracker, Planes Above Me). Loopt snel vol.

Afgevallen: parkeerplek terugvinden (Garmin heeft zelf "Save Location", DERDEN: https://www8.garmin.com/manuals-apac/webhelp/forerunner170/EN-SG/GUID-943D272E-6ED5-4E14-85D6-A0DDA29B71BA-7553.html), trainingsdata tonen (Garmin toont het zelf, niet te testen in de simulator).

Eerlijk: alle drie zitten rond 3 tot 9 reviews per maand. Reken op honderden kopers per app, geen duizenden (GOK).

## Mijn oordeel (Gijs)
Nog geen voorstel aan Hans. De ploegendienst-kalender is de beste kandidaat: één oude nummer één met precies de klacht die wij kunnen oplossen (herhalende roosters van meerdere weken), helemaal te testen, een doelgroep (verpleging, politie, fabriek, offshore 14/14) die elke dag naar zijn horloge kijkt, en ruimte voor een mooie glance ("morgen: nacht, 22:00"). Volgende run: alle reviews van beide VAW.BE-apps, de nieuwkomers zelf bekijken (wat doen ze, hoe zien ze eruit), en uitzoeken of een rooster invoeren op een horloge goed kan (instellingen via de Connect IQ-app op de telefoon). Klopt het, dan `volgend-product.md`.

## Ronde 4b: ploegendienst-kalender nagekeken (9 nov 22:47, Gijs zelf, winkel-API)
**Uitkomst: valt af als eerste product.** De klacht die ons gat was, is in de laatste drie maanden al door vier nieuwkomers opgelost, en de vraag is klein.
- Vraag: Shift Calendar (VAW.BE) heeft 115 reviews in ruim twee jaar: 34 in 2024, 47 in 2025, 34 in 2026, dus ±3 per maand (GEZIEN, alle 115 opgehaald). De proefversie met eigen betaling: 24 reviews, in 2026 maar 5. Klein.
- De klachten waren echt: "The program will not loop a schedule" (jun 2026), "Es fehlt leider die Wiederholung des Schichtzyklus" (2024), "it doesn't keep rotating as a nurse every week is different" (aug 2026), "Must be an easier way to add in 14 days, 14 r&r, 14 nights" (okt 2026), en "should set it up from your phone" (2025) (GEZIEN).
- Maar de nieuwkomers doen precies dat al, allemaal op het horloge zelf zonder telefoon (GEZIEN, beschrijvingen):
  - ShiftPilot (PrimoWatch, $2,99, kassa): "Any rotation: 4 on/4 off, 7/7, Panama, five and six week rosters. Nights that cross midnight. Swap a day without breaking the pattern", plus vertrektijd, slaapvenster en Body Battery.
  - Shift (Mellazure, $2,99, kassa): cyclus van 1 tot 42 dagen, Panama, DuPont, 24/48.
  - Shift Calendar: Work Rotations (DMSWatchApps): **gratis**, tot 56 dagen, glance met vandaag en morgen.
  - Shift Calendar (Dialforge): 30 dagen gratis, daarna €4,99 met code buiten de winkel.
- Als vijfde nieuwkomer met dezelfde belofte, naast een gratis versie die het al goed doet, is er voor ons geen eerlijk verschil.

## Wat vier rondes samen zeggen
In alle 17 niches die ik bekeek, zat of een sterke nummer één, of Garmin doet het zelf, of het gat werd in aug tot nov 2026 door nieuwkomers gevuld. De winkel krijgt nu veel nieuwe apps per week, onder meer van fabrieken (ThijsGer 187, Dialforge, DMSWatchApps). Gaten zoeken heeft dus weinig zin meer. Mijn koers vanaf de volgende run: kies een hoek waar het meeste geld zit (de 37 kassa-apps met 1.000+ en de kopers die $4 tot $8,49 betalen, zoals Multipassionate), en win daar met een duidelijk beter en mooier product dat wij met de simulator kunnen testen. De vraag wordt niet meer "waar is niemand", maar "waar betalen mensen al veel, en wat kunnen wij zichtbaar beter".

Nagekeken (controleur, 9 nov 23:00): ronde 4b klopt helemaal (alle 115 reviews opgehaald, citaten kloppen). De alinea over ThijsGer was fout (niet "bijna allemaal betaald", niet "de meeste 100+") en is hierboven verbeterd. Les voor reviews: `startPageIndex` telt per review (0, 20, 40), niet per pagina.
