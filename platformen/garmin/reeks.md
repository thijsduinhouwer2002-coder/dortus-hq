# Reeks sportieve datawijzerplaten: plan voor de eerste twee (Gijs, 16 nov 2026, run 122)

Opdracht: hoofdchat 16 nov 20:10 NL (Thijs koos Garmin optie 2). Een reeks van 4 tot 10 wijzerplaten per jaar, één herkenbare stijl en naam, steeds een gratis versie en een betaalde. Bron voor de markt: `platformen/verkenner/garmin-wijzerplaten-2026-11.md` (Vera). Dit bestand is een **plan, nog geen keuze**: de stijl is van Daan en Mila, de naam van Chris. Alles is GEZIEN (winkel-API, 16 nov ±20:00 UTC) tenzij er GOK of NIET GEZIEN staat.

## Kort
1. **Elk los idee bestaat al.** Body Battery met stress, een dag in één oogopslag, het weer per uur rond de rand, een zonnewijzer van 24 uur: van alles vond ik er minstens één, en drie daarvan kwamen in de laatste vijf weken uit. Wie op "een functie die niemand heeft" mikt, verliest.
2. **Wat wel verkoopt is zichtbaar:** een sterke eigen stijl, grote leesbare cijfers, veel horloges, een gratis broertje en eerlijk kopen. Bewijs: *Tactix8 Amoled PRO* ($4,99, 1.000+, 200 reviews, 4,9) en *Noctis PRO* ($3,99, 100+ in 10 maanden) van GreenBlack hebben allebei een gratis broertje (dat van Noctis staat op 1.000+, 52 reviews; dat van Tactix8 heb ik niet gemeten); *Fenix 9 CAMO Rich data* ($4,99, 1.000+, 395 reviews).
3. **Eerst de kern, dan de platen.** De kern is het deel dat elke plaat deelt: velden kiezen, kleuren, slaapstand, aanraken, gratis en betaald uit één bron, 100+ horloges. Die bouwen we één keer. Plaat 1 en 2 zijn dan vooral tekenwerk.
4. **Voorstel plaat 1: grote tijd met velden die hun richting tonen** (werknaam Koers). **Plaat 2 is nog open.** Mijn eerste idee (de dag als ring, werknaam Dagboog) trek ik zelf in: in dezelfde run vond ik op het forum van Connect IQ twee wijzerplaten van één maker van deze week die het al doen, *Two Suns* (ring van 24 uur met Body Battery) en *DayArc* (zelfde naam als mijn werknaam), elk met een gratis en een betaalde versie. Met *Daylight Left* erbij zijn dat er drie in vier dagen. Zie plaat 2 hieronder.
5. **Eerlijk over de opbrengst:** in mijn steekproef van vandaag halen 12 van de 82 betaalde wijzerplaten 100+ (15%), 2 de 1.000+. Vera: mediaan ±$25 per wijzerplaat in de eerste maanden bij kleine makers, een kwart haalt ±$190 of meer. Een reeks is een optelsom van kleine bedragen met een kleine kans op een uitschieter.

## Hoe gemeten
Zoekbalk van de winkel, alleen wijzerplaten, eerste 30 per woord, gesorteerd op "meest relevant": body battery, training readiness, data rich, sleep score, big digits, large digits, no glasses, hrv, 24h, hourly forecast, timeline. Samen 330 rijen, 318 verschillende wijzerplaten: `reeks-zoekwoorden-2026-11-16.csv`. Van 15 daarvan de hele winkeltekst gelezen. **Niet gedaan:** de schermbeelden bekijken (dat doet Mila, zie stappen), meer dan de eerste 30 reviews van vijf wijzerplaten lezen, en zoeken buiten de winkel (zie "Wat eraan komt").

| Groep (318 wijzerplaten) | Aantal | 10+ | 100+ | 1.000+ | Mediaan horloges |
|---|---|---|---|---|---|
| Betaald via Garmin | 82 | 25 | 12 | 2 | 90 |
| Gratis in de winkel | 236 | 204 | 122 | 45 | 89 |

Betaald naar aantal horloges: tot 60 horloges 3 van 20 op 100+, 61 tot 120 2 van 43, 121 en meer 7 van 19. De leeftijd van de wijzerplaten is hierin niet gelijk getrokken, dus lees het als richting; het past bij wat Joris mat (verhaal 19).

**Let op bij "gratis":** een deel is niet gratis. *Rest: Body Battery & Stress* (Dialforge), *Health Dashboard* (Trudelta), *Weathergraph* en *Daylight Left* staan als gratis in de winkel en verkopen een code of PRO buiten Garmin om (eigen site, PayPal, KiezelPay); Daylight Left vraagt na 2 dagen om geld. Garmin ziet dat geld niet en de koper moet een horloge-ID overtypen. Wij doen dat niet: het mag niet van onze eigen regels (geen eigen betaling, geen server) en het is juist iets om ons mee te onderscheiden.

## Wat kopers schrijven (eerste 30 reviews van vijf sterke datawijzerplaten, GEZIEN 16 nov ±20:08 UTC)
Fenix 9 CAMO, Tactix8 Amoled PRO, Noctis PRO, Noctis (gratis) en Health Dashboard: 118 reviews gelezen, 104 met vijf sterren. Wat er naast de lof staat:
- **Leesbaarheid:** "can't get the font large enough to read" en "the camo doesn't show up unless the brightness is way up" (3 sterren, Tactix8 PRO). Zelfde klacht als bij de figuur-wijzerplaten van run 112.
- **Slaapstand:** "Amazing, but missing a better AoD mode" (Fenix 9 CAMO).
- **Meer velden:** tijd tot zonsondergang, trend van de luchtdruk, weekafstand in plaats van de laatste 7 dagen.
- **Kopen met een code gaat mis:** "I payed for pro-version, but not sent code for unlocked" (1 ster, Health Dashboard). Dat steunt de keuze voor kopen via Garmin.
- "Paid for pro to get the segment time font" (Noctis): een mooier lettertype voor de tijd is voor iemand reden genoeg om te betalen.
Lees dit als voorbeelden, niet als telling: 30 reviews per wijzerplaat, vooral tevreden kopers.

## Wat een wijzerplaat mag tonen
GEZIEN in de uitleg van Garmin (`https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html`, 16 nov): er bestaan kant-en-klare velden voor Body Battery, stress, slaapscore, hersteltijd, trainingsstatus, VO2max, hartslag, stappen, trappen, calorieën, intensiteitsminuten, ademhaling, zuurstof, meldingen, agenda, weer nu, temperatuur hoog en laag, verwachting 1 tot 3 dagen, zonsopgang en zonsondergang, hoogte, luchtdruk, weekafstand hardlopen en fietsen, wedstrijdvoorspelling. Training readiness en HRV-status staan **niet** in die lijst.
Stond open tot run 123 (uitslag hieronder): of de geschiedenis van Body Battery en stress (voor een lijntje) op elk horloge te lezen is, het weer per uur, hoeveel geheugen een wijzerplaat per horloge krijgt, en de regels voor de slaapstand op AMOLED (hoeveel pixels aan mogen).

### Uitslag van de proef (run 123, 16 nov ±21:15 UTC): de geschiedenis is er, het geheugen is krap
Proef: tak `claude/garmin-reeks-kern` (26399a6), map `producten/garmin-reeks-kern`, run 43956535066 groen (3 toetsen, pakket met 63 horloges bouwt). Een kale wijzerplaat die leest en tekent, niet voor de winkel. Alle regels staan in `uitslag.txt` op de tak `schermen`, map `garmin-reeks-kern/claude-garmin-reeks-kern/`.

**GEZIEN in het log van de simulator, op 8 horloges** (Forerunner 255, fēnix 8 47 mm, Venu 3S, vívoactive 5, Venu Sq 2 en de oude Forerunner 55, Forerunner 245 en Instinct 2):
- **Geschiedenis van Body Battery en van stress: op alle 8 te lezen** (`has ja`, 80 waarden elk, geen lege).
- **Weer per uur: 12 uur vooruit, op alle 8.**
- **Kant-en-klare velden van Garmin (Complications):** ja op de 5 nieuwere, nee op Forerunner 55, 245 en Instinct 2. Op oude horloges lezen we velden dus op de oude manier (stappen, hartslag en zo rechtstreeks).
- **Beeld (GEZIEN met Read, blad van fr255, fenix847mm, instinct2, venusq2 en fr55, ±420 px hoog):** de tijd, de blauwe heuvellijn van Body Battery, de oranje van stress en de groene golf staan er op alle vijf; onderaan `BB80 ST80 W12`. Op de Instinct 2 is alles zwart-wit en valt de laatste cijfer van de tijd achter het ronde venstertje rechtsboven: dat horloge vraagt een eigen opmaak.
- **Tekenen:** tijd, twee heuvellijnen van 40 punten en een golf van 24 punten samen 1 tot 2 ms op de schermen met weinig kleuren, 7 tot 15 ms op AMOLED (fēnix 8: 9 tot 15 ms). Dat is de simulator op een server, geen horloge.
- **Geheugen voor een wijzerplaat** (uit de bestanden van de SDK, alle 63 regels geteld in `uitslag.txt`): 131.072 bytes op 56 van de 63, ook op de nieuwste (Venu 4, Forerunner 970, vívoactive 6). 98.304 op Forerunner 55, 245, 945 en Venu Sq; 114.688 op fēnix 6; 65.536 op Instinct 2; 524.288 op vívoactive 4. De kale proef gebruikt ±9.000 bytes. Een spel krijgt 786.432 bytes, een wijzerplaat dus een zesde.

**GEZIEN in de uitleg van Garmin** (`https://developer.garmin.com/connect-iq/api-docs/Toybox/SensorHistory.html`, opgehaald met curl, 16 nov ±21:00 UTC): de lijst "Supported Devices" bij de geschiedenis van Body Battery telt 113 regels, bij stress 116. Erin: alle Forerunners vanaf de 55 en 245, fēnix 6 tot 9, epix, Enduro, Instinct 2 en 3, Venu (alle), vívoactive 4 tot 6, MARQ, Descent, Approach S50, S70 en S72, D2. Er niet in voor Body Battery: fēnix 5 Plus en D2 Air.

**Antwoord op de voorwaarde van Daan (16 nov ±21:05 UTC):** ja, de heuvellijn van Body Battery of stress kan op het grootste deel van de 100+ horloges. Volgens de lijst van Garmin op 113 soorten, in de simulator gezien op 8 waaronder de drie oudste die we zouden meenemen.

**NIET GEZIEN, en dat telt:**
- Hoeveel uur geschiedenis een echt horloge geeft. De simulator geeft op elk horloge dezelfde 80 nepwaarden (laagste 5, hoogste 93), één per minuut, dus 79 minuten, ook al vroeg ik 4 uur. Garmin schrijft zelf dat de tijd tussen twee waarden per horloge verschilt. Pas een echt horloge zegt of de lijn 4 uur of een hele dag kan tonen.
- De volgorde: ik vroeg "oudste eerst" en kreeg de nieuwste eerst (de tijd liep 4.740 seconden terug). Bij het bouwen de tijd van elke waarde gebruiken en niet de volgorde vertrouwen.
- Het kleurverloop als vast plaatje per thema (vraag van Mila): niet geprobeerd. Met 131.072 bytes voor alles is een schermvullend plaatje per thema de eerste zorg; op nieuwere horloges tellen plaatjes mogelijk niet mee in dat geheugen (GOK, eerst meten).
- De slaapstand op AMOLED en instellingen in Garmin Connect.

### Uitslag van proef 2 (run 124, 16 nov ±22:10 UTC): plaatjes en letters kosten op nieuwe horloges bijna niets, op oude veel
Proef: zelfde tak, commit bc72807, run 43965812334 groen (toetsen, pakket voor 63 horloges, 8 horloges in de simulator). De proef laadt een eigen cijferletter op twee maten (Poppins, 56 en 110 px, alleen `0123456789:`) en één schermvullend kleurverloop, en print het geheugen ervoor en erna. Ontwerp van de proef: `producten/garmin-reeks-kern/ontwerp.md` op de tak.

**GEZIEN in `uitslag.txt` (simulator, bytes van het geheugen van de app):**

| Horloge | Scherm | Geheugen totaal | Kale proef | Letter 56 px | Letter 110 px | Schermvullend plaatje | Vrij daarna |
|---|---|---|---|---|---|---|---|
| Forerunner 255 | 260 | 126.792 | 10.632 | 568 | 320 | 1.192 | 113.984 |
| fēnix 8 47 mm | 454 | 126.792 | 10.768 | 568 | 320 | 1.296 | 113.744 |
| Venu 3S, vívoactive 5 | 390 | 126.792 | 10.704 | 568 | 320 | 1.296 (plaatje van 260) | 113.808 |
| Venu Sq 2 | 320x360 | 126.792 | 10.656 | 568 | 320 | 1.168 (plaatje van 260) | 113.984 |
| Forerunner 55 | 208 | 94.024 | 11.792 | 2.120 | 4.208 | 22.576 | 53.248 |
| Forerunner 245 | 240 | 94.024 | 11.784 | 2.776 | 5.328 | 68.544 (plaatje van 260) | 5.512 |
| Instinct 2 | 176 | 61.256 | 11.808 | 2.120 | 4.208 | 18.624 (plaatje van 260) | 24.416 |

- **Nieuwe horloges (de vijf met `pool=ja`):** een plaatje of een letter telt bijna niet mee in het geheugen van de app, ±1.300 bytes voor een heel scherm. Het beeld zelf staat in een apart geheugen van het horloge. Hoe groot dat aparte geheugen op een echt horloge is: NIET GEZIEN, de simulator klaagt niet.
- **Oude horloges (Forerunner 55, 245, Instinct 2, `pool=nee`):** het plaatje telt volledig mee. Op de Forerunner 245 blijft na één schermvullend plaatje 5.512 bytes over: dat past dus niet naast een echte wijzerplaat. Letters kosten daar 2.000 tot 5.500 bytes per stuk, dat kan.
- **Tekenen op de fēnix 8:** het schermvullende plaatje 9 tot 12 ms, de tijd in de eigen letter 2 tot 3 ms, alles samen 13 tot 17 ms. Op de schermen met weinig kleuren 0 tot 1 ms.
- **Inbranden:** `inbrand=true` op fēnix 8, Venu 3S, vívoactive 5 en Venu Sq 2; `false` op Forerunner 255, 55, 245 en Instinct 2. Op de eerste groep gelden dus de regels van Garmin voor de slaapstand.
- **Beeld (GEZIEN met Read, blad van 8 beelden, ±390 px breed):** de eigen letter staat er op alle horloges. Het kleurverloop is glad op AMOLED, korrelig op de Forerunner 255 en 245 en grof gestippeld op de Forerunner 55 (8 kleuren). Op Venu 3S vult het plaatje van 260 het scherm van 390 niet: per schermmaat is een eigen plaatje nodig.
- **NIET GEZIEN:** het slaapbeeld. De proef tekende het pas na 14 s en de laatste schermafbeelding was toen al gemaakt (`KERN SLAAPBEELD` staat wel in het log, `echt=false`: de simulator zet de slaapstand niet zelf aan). Hersteld in 2999205 (na 6 s); die run liep nog toen ik stopte.

**Antwoord voor Tij (Mila):** getekende banden in plaats van een plaatje is de goede keuze, want dat werkt ook op de oude horloges en op elk scherm. De vier letters kunnen overal. Proef 3 (commits a216c39 en 2999205, zelfde tak) meet haar echte letters: Big Shoulders Display, tijd 78 en 136 px, BB-getal 29 en 50, veldgetal 17 en 30, datum 17 en 30, en op 208 px alles maal 0,8. Uitslag: volgende run.

**Wat dit betekent voor het ontwerp:** weinig plaatjes, veel tekenen met lijnen en vlakken; een eigen cijferletter voor de tijd kost geheugen en moet gemeten worden voor Mila hem uitwerkt; de golf en de heuvellijn als veelhoek zijn goedkoop genoeg om elke seconde te tekenen als het horloge wakker is.

## De kern (één keer bouwen, in elke plaat)
1. **Velden kiezen** uit de lijst hierboven, in Garmin Connect en waar het kan op het horloge zelf. Bij de wijzerplaten met 100+ noemt 85% dit (Vera).
2. **Kleuren:** een handvol thema's per plaat, door Mila gekozen en op contrast gemeten (zoals bij de dieren van Ebb), geen vrije kleurkiezer met 64 lelijke uitkomsten.
3. **Slaapstand** op AMOLED en **aanraken**: tik op een veld en de bijbehorende weergave van Garmin gaat open.
4. **Gratis en betaald uit één bron.** Gratis: vaste velden, één thema, blijft altijd werken. Betaald ($3,00; $2,99 bestaat niet bij Garmin, de stappen zijn $2,75 en $3,00): alles kiezen. Geen proef die omslaat, geen code, geen eigen site. Zin voor de winkel: "Pay once in the Connect IQ Store. The free version stays free."
5. **100+ horloges vanaf de eerste dag.** Het venster "nieuw" duurt 14 dagen en komt niet terug (Joris). De mediaan van een betaalde app is 84 van de 107 soorten horloges waar betaald op kan.
6. **Winkelpagina:** filmpje (Chris), 5 beelden (Mila), tekst in Engels, Duits en Nederlands, zoekwoord in de naam.
7. **Meten:** elke plaat krijgt een regel in een meetbestand op dag 0, 7, 14 en 30.
8. **Het gratis broertje (Joris, 16 nov ±21:50 UTC, verhaal 22 in `platformen/succes/verhalen-groei.md`, 452 paren gemeten):** de betaalde haalt mediaan een tiende van zijn gratis broertje. Daarom: (a) in de eerste regels van de gratis winkeltekst één zin met link naar de betaalde ("The full version adds ...: <link>"); (b) de gratis op alle horloges waar hij draait, ook waar de betaalde niet kan (oude horloges zonder betalen via Garmin); (c) meetlat: de gratis op 1.000 is het doel, de betaalde volgt met ±een tiende. Gratis blijft gratis, geen proef en geen code: dat klopt met wat Joris mat.

De wijzerplaat met Gloop (tak `claude/garmin-wijzerplaat-gloop-2026-11-16`) wordt plaat 3 of later: de hoedentoren groeit echt met je stappen, maar hij krijgt eerst de kern eronder. Een figuur zonder velden haalt half zo vaak 100+ (Vera).

## Plaat 1, werknaam Koers: grote tijd, en elk veld laat zien waar het heen gaat
**Wat het is:** tijd zo groot als het scherm toelaat, daaronder vier velden naar keuze. Elk veld toont het getal met een klein lijntje van de laatste uren of een pijl (Body Battery zakt, stress loopt op, hartslag in rust daalt). Voor wie voor het trainen wil weten: ga ik omhoog of omlaag?
**Waarom deze eerst:** hij bouwt de hele kern, en Body Battery, weer en zelf velden kiezen zijn de kenmerken die het sterkst samengaan met 100+ (Vera: 45,9% tegen 27,7%, 46,3% tegen 23,1%, 42,7% tegen 20,3%).

| De 5 dichtstbijzijnde | Prijs | Downloads, reviews | Horloges | Wat het doet (winkeltekst) | Wat wij hebben dat zij niet hebben |
|---|---|---|---|---|---|
| Noctis PRO, GreenBlack (jan 2026) | $3,99 | 100+, 18 (4,9); gratis broertje 1.000+, 52 | 15 | "Extra-large, bold digits", sportvelden, weer | Bijna alles behalve 15 horloges: wij 100+. En de richting per veld |
| VoltGrid, dvpdesign.pro (aug 2026) | $1,99 | 100+, 3 (5,0) | 179 | Zeven velden naar keuze, "cyber-HUD", grafiekjes, AOD | Rust: vier velden in plaats van zeven, geen neon. Zwak verschil als hun grafiekjes hetzelfde doen (NIET GEZIEN, beelden bekijken) |
| Clean Rings, Bash (9 nov 2026) | $1,99 | 100+, 5 (4,2) | 59 | Drie ringen naar keuze, grote tijd, veld vasthouden opent Garmin-weergave | Meer soorten gegevens (stress, slaap, herstel, weer) en de richting |
| Astra Vital Pro, astra-dev (sep 2026) | $4,99 | 10+, 2 (5,0) | 74 | Stress en Body Battery met geschiedenis, thema's, gratis versie die blijft, eenmalig kopen | Prijs ($2,99) en stijl; inhoudelijk zit deze het dichtst op ons plan |
| Daybook, AyetelKursi (okt 2026) | $2,99 | 1+, 3 (4,7) | 86 | Training, herstel, slaap, weer en een dagcurve sinds middernacht (Body Battery, hartslag of stress, met zonsopgang en zonsondergang), met gratis versie | Eerlijk: weinig. Daybook doet veel van wat wij willen en staat na een maand op 1. Dat is de waarschuwing dat functies alleen niet verkopen |

**Mijn antwoord op "wat hebben wij":** niet één functie, wel de combinatie die geen van de vijf heeft: leesbaar als Noctis, op 100+ horloges als VoltGrid, eerlijk te kopen als Astra, en getekend in één eigen stijl. Dat is een dun antwoord zolang de stijl er niet is. Daarom is stap 1 hieronder een stijlblad en geen code.

## Plaat 2: ingetrokken idee (de dag als ring), nog geen nieuwe keuze
**Stand 16 nov ±20:10 UTC: dit idee gaat niet door.** Na het schrijven van de tabel hieronder las ik de showcase van het forum van Connect IQ (`https://forums.garmin.com/developer/connect-iq/f/showcase`, GEZIEN met curl). Daar staan van de maker Verden: *Two Suns* (2 dagen oud: ring van 24 uur met het daglicht, Body Battery onder de tijd, de betaalde Pro met de curve van Body Battery over 24 uur) en *DayArc* (1 dag oud: 's ochtends het weer, 's middags stress, 's avonds Body Battery; gratis en Pro). Samen met *Daylight Left* (13 nov) doen drie wijzerplaten van deze week wat ik wilde. Op de vraag "wat hebben wij dat zij niet hebben" heb ik dan geen antwoord, en de regel zegt: geen antwoord, geen keuze. De tabel blijft staan als bewijs.
**Gemeten 16 nov ±20:09 UTC (maker Verden.watch, 3 talen):** Two Suns gratis 10+ en Pro $2,49 1+ (97 en 96 horloges); DayArc gratis 100+ na één tot twee dagen en Pro $2,49 1+. Dit is precies onze opzet (gratis broertje, betaalde Pro via Garmin, ±100 horloges), dus een goede meetlat: over 14 dagen kijken waar hun Pro's staan voor wij iets beloven.
**Wat dit leert:** het forum is de plek waar makers hun wijzerplaat aankondigen, vaak een dag na de goedkeuring. Die lezen we voortaan bij elke concurrentiecheck. Reddit is van hieruit niet te lezen (curl geeft 403; niet omzeild).
**Kandidaten voor een nieuwe plaat 2, nog zonder check:** een analoge sportplaat met dezelfde kern (wijzers, velden met richting), of de wijzerplaat met Gloop op de kern. Kiezen na het stijlblad, met een eigen tabel van vijf.

Het oude voorstel:
**Wat het is:** een ring van 24 uur om de tijd. Het stuk dat achter je ligt toont wat je lijf deed (Body Battery als lijn), het stuk dat komt toont het weer per uur en de zonsondergang. Eén blik: hoeveel energie heb ik, en wanneer is het droog en licht?

| De 5 dichtstbijzijnde | Prijs | Downloads, reviews | Horloges | Wat het doet | Wat wij hebben dat zij niet hebben |
|---|---|---|---|---|---|
| Daylight Left, MarioZ (13 nov 2026) | gratis in de winkel; na 2 dagen $1,99 via KiezelPay met een code | 10+ | 118 | Zonnewijzer van 24 uur met Body Battery ernaast, hartslaggrafiek van 4 uur | Verleden en toekomst in dezelfde ring; kopen via Garmin |
| Ringcast, OkaLabs (12 nov 2026) | gratis | 100+, 1 | 93 | 12 uur weer rond de wijzerplaat, vier velden naar keuze | De helft van de ring voor je lijf |
| Weather Dial, WatchFaceKit (jun 2026) | $1,99 | 100+, 5 (5,0) | 47 | Negen uur weer op de rand | Body Battery, meer horloges |
| Just Ring Forecast, Eduard_Design (okt 2026) | $3,99 | 10+, 1 | 69 | Weergrafiek van 12 uur, acht velden | Eenvoud |
| Weathergraph, tomas.kafka (2017) | gratis, PRO op eigen site | 10.000+, 278 (4,4) | 151 | Het weer per uur, veruit de bekendste | Wij zijn geen weer-app en moeten dat ook niet willen zijn; *Forecast* van VAW.BE (gratis, 10.000+, 414 reviews) zit er ook |

**Mijn antwoord:** het idee "achter je je lijf, voor je het weer" vond ik bij niemand in één ring, maar twee van de vijf zijn vier dagen oud en het weer is in handen van twee gratis toppers. Dit is dus de zwakkere van de twee. (Ingetrokken, zie boven.)

## Wat eraan komt
De winkel heeft geen lijst "binnenkort". Wat ik zag: 4 van de 15 gelezen wijzerplaten zijn van de laatste 5 weken (Clean Rings 9 nov, Ringcast 12 nov, Daylight Left 13 nov, Rest 28 okt), en Vera telde 1.171 nieuwe betaalde wijzerplaten in de eerste 16 dagen van november. Het forum van Connect IQ (showcase, eerste pagina, 25 onderwerpen van de laatste 3 dagen) gelezen: daar vond ik Two Suns en DayArc, zie plaat 2. Voor plaat 1 stond er niets dat dichterbij komt dan de vijf in de tabel (wel *Slab*, "all time, no clutter", en *Still*, een rustige weerplaat op 91 horloges met gratis en Pro). **Nog te doen:** de nieuwste 60 op "body battery" en "big digits" en de showcase nog eens bekijken op de dag dat we beginnen met bouwen. Reddit (r/Garmin, r/GarminWatches) is van hieruit niet te lezen.

## Stappen
1. **Mila en Daan (eerst):** de winkelbeelden van de tien wijzerplaten hierboven bekijken, alleen om te leren, en één stijlblad voor de reeks maken: lettertype voor de tijd, vier thema's, hoe een veld met richting eruitziet op 260 MIP en op 454 AMOLED. Daan zegt per plaat het verschil in één zin, of zegt nee.
2. **Gijs, tegelijk:** proef in de simulator op een tak `claude/garmin-reeks-kern`: velden lezen via de kant-en-klare velden van Garmin, geschiedenis van Body Battery, weer per uur, instellingen, geheugen per horloge. Uitslag in dit bestand onder "Wat een wijzerplaat mag tonen".
3. **Chris:** naam van de reeks en van plaat 1, met zoekwoorden gemeten zoals bij Ebb.
4. **Bouwen** van plaat 1 pas na 1 tot 3. Gratis en betaald samen indienen, met 100+ horloges.
5. **Meetpunt:** 30 nov tellen we de downloads van alles op Garmin (hoofdchat). Plaat 1 staat er dan nog niet; het meetpunt gaat over Ebb 1.0.1 en Hat Tower.

## Wat dit omgooit
- Blijkt in de proef dat de geschiedenis van Body Battery of het weer per uur op de helft van de horloges niet te lezen is: dan vervalt de richting per veld of de ring, en kiezen we opnieuw.
- Staat plaat 1 met kern, filmpje en 100+ horloges na 30 dagen onder de 10 downloads: dan ligt het aan de drukte en niet aan ons product, en bouwen we geen plaat 3 zonder ander kanaal (Vera schreef hetzelfde over Gloop).
