# Broncode: Crystal (Garmin-wijzerplaat, gratis, open) en Crystal Reborn (betaald)

Uitgeplozen door de Afkijker op do 26 nov 2026 (±12:30 NL), voor issue #20. Code gelezen uit `git clone --depth 1` van https://github.com/warmsound/crystal-face (laatste commit bcc3404, 15 apr 2025; niets uitgevoerd). Winkelcijfers, beschrijvingen en reviews met curl uit de open winkel-API (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` en `/reviews`).

## Waarom dit project
- **Crystal: 1.000.000+ downloads, 4.005 reviews, 4,4 sterren, 209 horlogetypen, gratis, in de winkel sinds 12 mrt 2018** (GEZIEN, app `9fd04d09-8c80-4c81-9257-17cfa0f0081b`, maker PixelPathos, websiteUrl wijst naar deze repo). Het is de bekendste open Connect IQ-app.
- **De maker verdient nu met een betaalde opvolger, Crystal Reborn** (sinds 18 jul 2025): Garmin Pay-versie $2,99, 1.000+ downloads, 55 reviews, 4,6, 93 horlogetypen (GEZIEN, `f3c3d2d3-6efa-49da-bdab-329cdf37b70f`); en een KiezelPay-versie met 24 uur proef en een code, 1.000+, 18 reviews, 3,9, 158 horlogetypen (GEZIEN, `111ed5fc-c61f-47ec-b05d-aac856024d06`).
- Licentie: GPL-3 (GEZIEN, `LICENSE.txt`). Code overnemen zou Ebb ook GPL maken; we lenen dus alleen ideeën.
- Ebb ter vergelijking (GEZIEN 26 nov, zelfde API): Ebb $2,99, emmer "1+" downloads, 0 reviews, 74 horlogetypen; Ebb Calm gratis, emmer "10+", 0 reviews, 75 horlogetypen.

## Wat ze slim doen (bestand en regels)
1. **Het gratis ding is de etalage van het betaalde ding, en dat staat op regel 1.** De beschrijving van Crystal begint met "A new version of Crystal is out! Check out **Crystal Reborn** here:" plus link, nog vóór de uitleg (GEZIEN, winkelbeschrijving). Reborn begint op zijn beurt met een link naar de andere betaalversie en naar zijn nieuwe wijzerplaat Orbula. Elke pagina stuurt dus door naar de volgende verkoop. Bij Ebb Calm staat de link naar Ebb pas in de tweede alinea ("Want more? The full Ebb...", GEZIEN in en, de, nl, fr).
2. **Per schermmaat eigen letters en maten, via de jungle in plaats van via code.** `monkey.jungle` hangt per groep horloges een extra map aan: `resources-small-time` voor 218 en 208 px, `resources-small-icons` voor de kleinste, `resources-no_floors` voor horloges zonder trappen (r. 8 tot 25). Er zijn 15 mappen per schermmaat (`resources-round-218x218` tot `resources-round-454x454`), elk met een eigen `layout.xml`. De code blijft één en dezelfde.
3. **Annotaties knippen code weg voor oude horloges.** `base.excludeAnnotations = unbuffered;object_store;...` en per oud horloge het omgekeerde (`monkey.jungle` r. 6 en 36 tot 40). Functies met `(:buffered)` bestaan dan alleen op horloges die het kunnen (`source/GoalMeter.mc` r. 272). Zo draait één app op 209 typen.
4. **Weinig geheugen door buffers met maar 2 of 3 kleuren.** De meters worden één keer in een `BufferedBitmap` met `:palette => [achtergrond, vulkleur]` getekend en daarna alleen geplakt (`source/GoalMeter.mc` r. 271 tot 287, `source/MoveBar.mc` r. 136 tot 143). Dat spaart batterij en geheugen.
5. **Altijd-aan-scherm in een eigen, uitgeklede tekening die elke minuut verschuift** (inbrandbescherming), met per schermmaat eigen verschuivingen: `burnInYOffsets [-54, -27, 27, 54]` op 360 px (`resources-round-360x360/layouts/layout.xml` r. 67, `always-on-source/AlwaysOnDisplay.mc` r. 9 tot 12). Bij het wisselen geeft hij het geheugen van de gewone tekening vrij (`source/CrystalView.mc` r. 305 tot 310).
6. **Versienummer zichtbaar in de instellingen**, alleen lezen (`resources/settings/settings.xml` r. 3 tot 5, `properties.xml` r. 3). Wie klaagt, kan zeggen welke versie hij heeft.
7. **Echte tests in de app** voor de lastigste rekensom (schaal van de meterblokjes), met `(:test)` (`source/GoalMeterTests.mc`, 102 regels). Ebb doet dit al (`InstellingenTest.mc`, `OpslagTest.mc`, enz.).

## Wat gebruikers klagen (reviews, GEZIEN 26 nov via de API)
Crystal, 120 nieuwste reviews: 86 keer 5, 13 keer 4, 13 keer 3, 3 keer 2, 5 keer 1.
- **Vastlopen op één model:** "Model: FR55 Does not work. Keeps showing the (IQ!) error", "works great for 10 seconds then crashes", "lately I have to delete & re-install it EVERY time I charge my watch".
- **Batterij:** "it drained my battery so fast it was not worth it"; "the dot blinking every heart rate update is extremely annoying".
- **Instellingen niet gevonden:** "Why fahrenheit and not celsius?", "is there a way to turn the time into 24 hour clock", "baixei e não sei como instalar". Daarom staat "FAQs, including how to change watch face settings" bovenaan de beschrijving.
Crystal Reborn:
- **Garmin Pay-versie, 30 reviews: niets onder de 3.** De enige klacht die terugkomt: **letters te klein op kleine horloges** ("the indicator and data fonts are too small on a smaller watches like the vivoactive", 21 jan 2026; "size of fonts should be bigger", 31 jan 2026; "font size. Can't make it bigger", 1 sep 2026).
- **KiezelPay-versie, 18 reviews: 4 onder de 3, en twee gaan over de code:** "After a day then screen is filled with text asked me to go to website and enter code. Avoid" (11 dec 2025), "Also nix mit 24 Stunden Trial" (3 feb 2026); en "waited 5 hours for it to start working" (24 sep 2026). Dit bevestigt onze keuze voor Garmin Pay zonder ontgrendelcode (`platformen/garmin/concurrenten-2026-11-13.md` r. 14).
- Issues op GitHub kon ik niet lezen: buiten onze repo's geeft de API 403.

## Welk product wordt er beter van: Ebb en Ebb Calm
1. **Horloges die Crystal Reborn (betaald) wel heeft en Ebb niet** (GEZIEN, verschil van `compatibleDeviceTypeIds`, namen uit `/api/asw/deviceTypes`): Descent MK3 43 mm en MK3i 51 mm, Venu X1, fēnix 9 Pro 51 mm, Enduro 4, MARQ Adventurer Gen 3, Approach S70 (42 en 47 mm) en S50, Venu Sq 2 en Sq 2 Music, Enduro 3 en Instinct 3 AMOLED (staan al op de proeftakken voor 1.1), en de fēnix 6-reeks (die kan Ebb niet: minApiLevel 5.0.0). Descent is een duikhorloge: precies de mensen die adem inhouden oefenen. Meer horloges is meer kopers zonder nieuwe functie. Nagekeken in `manifest.xml` van tak `claude/garmin-ebb-11` (3dae428, 57 horloges): fēnix 9 Pro 43 en 47 mm staan er al in; Descent MK3, Venu X1, Enduro 4, fēnix 9 Pro 51 mm, MARQ Gen 3, Approach en Venu Sq 2 niet. Of de SDK ze allemaal kent en of ze minApiLevel 5.0.0 halen: niet nagekeken (GOK: de nieuwe wel, Venu Sq 2 en Approach S50 twijfel).
2. **Link naar Ebb op regel 1 van Ebb Calm**, vet, vóór de uitleg, zoals Crystal (nu tweede alinea).
3. **Kleine schermen:** Daan noemde "Calm 4-7-8" op 218 px al "krap maar leesbaar" (`producten/garmin-adem/keuring-daan`, 17 nov). De enige terugkerende klacht over Reborn is precies dat. Bij de kerstronde de 218 en 208 px nog eens met de ogen nalopen; een eigen `resources-small` map in de jungle zoals Crystal is de nette weg.
4. **Versie zichtbaar** op het instellingenscherm van Ebb, voor als er ooit een klacht komt.

Bestanden bij ons: `producten/garmin-adem/monkey.jungle` en `manifest.xml` (horloges), winkelteksten in `platformen/garmin/` (regel 1 van Calm).
