# Garmin: broncode van concurrenten, wat Ebb ervan leert (25 nov 2026)

Gemaakt door een onderzoeksagent voor de hoofdchat. Alleen gelezen: 15 repo's met `git clone --depth 1` in `/tmp`, niets uitgevoerd, niets gebouwd, niets in de winkel veranderd. Winkelcijfers en reviews GEZIEN op 25 nov ±23:00 UTC met `curl` op de open API van de winkel (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>` en `.../<id>/reviews`). Code van Ebb: tak `claude/garmin-ebb-11` (1.1.0, 57 horloges); live staat 1.0.1 (GEZIEN). Zoek elke plek terug met `git grep -n "<woord>" origin/claude/garmin-ebb-11 -- producten/garmin-adem/source`.

## De 5 dingen die Ebb het meest beter maken voor kopers (op volgorde van geld)

1. **Nieuw hoofdbeeld in de winkel zoals de winnaar:** echt horloge met een gewoon ademscherm (in, tellen, hartslag), de patronen in woorden ("4-7-8 · BOX · BREATH HOLD · MY PATTERN") en een rij van 4 pictogrammen (eyes closed, saves to Garmin Connect, one payment, no account). Schildpad klein of weg. Issue #27.
2. **Box breathing terug als eigen knop in het startmenu** (nu alleen via My pattern in de instellingen, `Start.mc` regel 18 en 40) en als woord in het hoofdbeeld; patronen is het meest geprezen punt in reviews van concurrenten. Issue #28.
3. **Hartslag en stress van het horloge voor en na op het eindscherm en in Garmin Connect** (techniek van Meditate, MIT); geeft een beeld met cijfers voor de winkel. Geen medische claim: "your watch's stress score before and after". Issue #28.
4. **Trillen dat op elke Forerunner werkt:** losse tikken met lange pauzes in plaats van korte reeksen; een maker zag op een echte Forerunner 165 dat reeksen samenvallen tot één lange tril, en reviews van Meditate klagen over trillen op Forerunner 245 en 255. Beschermt onze kernbelofte "eyes closed". Issue #28.
5. **Instellingen ook in de Connect IQ-app op de telefoon, met een keuze "dim screen"**: Ebb heeft nu op geen enkel horloge telefooninstellingen (GEZIEN), en klachten over instellingen op het horloge en een te fel scherm in het donker komen bij vier concurrenten terug. Nog geen issue: na #28.

## Wat ik zocht en vond

Zoekopdrachten (`gh api search/repositories`): connect iq breathing, garmin breathe, garmin breathing, monkey c breathing, box breathing garmin, connectiq breath, garmin meditation, garmin wim hof, connectiq game, garmin watch game, connect iq animation, garmin hrv, garmin apnea. "monkey c breathing" en "connectiq relax" gaven 0. Een filter op taal Monkey C werkt niet in de zoek-API (GEZIEN: geeft gewone treffers). De lijst met repo's van github.com/garmin is in deze sessie dicht (403); `garmin/connectiq-apps` heb ik wel gekloond.

Sterren en licentie: GEZIEN in de zoek-API en in het LICENSE-bestand van de kloon. **Overnemen mag alleen bij MIT en Apache-2.0, met naamsvermelding** (de regel "Copyright (c) ..." en de licentietekst in ons pakket, bijvoorbeeld in `producten/garmin-adem/bron/LICENSES-derden.txt`). GPL-3.0 niet: dat zou Ebb (betaald, gesloten) onder GPL dwingen. Geen licentie betekent alle rechten voorbehouden: alleen het idee, eigen code schrijven.

| Repo | Sterren | Licentie (GEZIEN) | Laatste push | Overnemen? |
|---|---|---|---|---|
| [garmin/connectiq-apps](https://github.com/garmin/connectiq-apps) | 597 | Apache-2.0 | 2025-01-08 | ja, met vermelding |
| [vtrifonov-esfiddle/Meditate](https://github.com/vtrifonov-esfiddle/Meditate) | 54 | MIT, (c) 2017 vtrifonov-esfiddle | 2022-11-15 | ja, met vermelding |
| [vtrifonov-esfiddle/TestHrv](https://github.com/vtrifonov-esfiddle/TestHrv) | 53 | MIT, (c) 2018 vtrifonov-esfiddle | 2021-01-13 | ja, met vermelding |
| [dliedke/Meditate](https://github.com/dliedke/Meditate) (fork) | 4 | MIT, (c) 2017 vtrifonov-esfiddle | 2026-05-19 | ja, met vermelding |
| [nradov/BreatheFree](https://github.com/nradov/BreatheFree) | 0 | MIT, (c) 2026 BreatheFree contributors | 2026-11-18 | ja, met vermelding |
| [SirLocke/garmin-wimhofBreathing](https://github.com/SirLocke/garmin-wimhofBreathing) | 0 | MIT, (c) 2026 SirLocke | 2026-11-21 | ja, met vermelding |
| [lgruen/wim-hof-garmin](https://github.com/lgruen/wim-hof-garmin) | 0 | MIT, (c) 2025 Leonhard Gruenschloss | 2025-06-15 | ja, met vermelding |
| [farmisen/watch-invaders](https://github.com/farmisen/watch-invaders) | 3 | MIT, (c) 2025 Fabrice | 2025-08-16 | ja, met vermelding |
| [massimocolella/simple-breath](https://github.com/massimocolella/simple-breath) | 0 | GPL-3.0 | 2026-07-18 | nee, alleen idee |
| [8ctopus/garmin-static-apnea](https://github.com/8ctopus/garmin-static-apnea) | 1 | GPL-3.0 | 2023-07-17 | nee, alleen idee |
| [tomaspolak82-commits/garmin-breathing](https://github.com/tomaspolak82-commits/garmin-breathing) | 0 | geen | 2026-10-30 | nee, alleen idee |
| [Driftter-jv/Breath478](https://github.com/Driftter-jv/Breath478) | 0 | geen | 2026-10-24 | nee, alleen idee |
| [henrikkorsgaard/mindful-garmin](https://github.com/henrikkorsgaard/mindful-garmin) | 0 | geen | 2026-03-30 | nee, alleen idee |
| [kzibart/Garmin_FlappyWatch](https://github.com/kzibart/Garmin_FlappyWatch) | 2 | geen | 2024-12-02 | nee, alleen idee |
| [black-square/BrickGame](https://github.com/black-square/BrickGame) | 2 | geen | 2025-05-08 | nee, alleen idee |

Geen van de best verkopende ademapps in de winkel (WHM breathing+, Breathing Timer, Breathe van FikirLtd, BTS PRO) heeft open broncode die ik vond. Wel open: Meditate (twee winkelvermeldingen met elk 10.000+ downloads en 136 en 138 reviews, GEZIEN).

## Per repo: wat ze slim doen en wat wij ermee doen

### vtrifonov-esfiddle/Meditate en de fork dliedke/Meditate (MIT)
Winkel (GEZIEN): Meditate `1cc98099-...` 10.000+ downloads, 136 reviews, 4,5; de fork `c5fc5ea5-...` 10.000+, 138 reviews, 4,6.
- **Stress voor en na de sessie** uit de geschiedenis van het horloge: `dliedke_Meditate/Meditate/source/summaryScreen/SummaryModel.mc` regels 42-110. `SensorHistory.getStressHistory(null)` (met `has`-controle, regel 100-110), het nieuwste monster is "na", het oudste monster binnen de sessietijd is "voor". De fork schrijft zelf: werkt pas bij sessies van 5 minuten of langer (README, DERDEN).
- **Laagste, gemiddelde en hoogste hartslag** in een eigen FIT-veld op de sessie: `vtrifonov-esfiddle_Meditate/HrvAlgorithms/sources/activity/HrActivity.mc` regels 37-83 (elke seconde `Activity.getActivityInfo().currentHeartRate`, min bijhouden, gemiddeld en max van het horloge).
- **HRV (RMSSD) uit slag-tot-slag-tijden**: `HrvAlgorithms/sources/activity/HeartbeatIntervalsSensor.mc` regels 19-42 (`Sensor.registerSensorDataListener` met `:heartBeatIntervals`), berekening in `hrv/HrvRmssd.mc`. Let op: reviews klagen vaak dat HRV blijft hangen op "waiting" (zie klachten), dus niet beloven.
- **Trilpatronen met lange pauzes** (1000 ms aan, 1000 ms uit): `Meditate/source/activity/Vibe.mc` regels 50-85. Toch klagen kopers dat trillen op Forerunner 245 en 255 niet werkt (reviews 2019-12, 2022-08, 2023-02, GEZIEN).
- **Opslaan als ademwerk**: `HrvAlgorithms/sources/activity/FitSessionSpec.mc` regel 6 en 16-21, subsport 62. Ebb doet dit al (`Opname.mc` regel 53-57).
- **Klachten van gebruikers (GEZIEN, reviews van 3 sterren of minder):** "Wish the screen could be turned off, it almost burned into the display" (2026-09), "not keep the display backlit for the entire time" (2022-07), timer niet in te stellen, trillen werkt niet op Forerunner 245, "stuck on waiting HRV" op Forerunner 255 en Venu 3.
- **Bij Ebb:** stress en hartslag voor en na in `EindScherm.mc` (functie `teken`, regel 15) en als FIT-velden in `Opname.mc` (regel 58-63, naast `inhoud` en `tijden`). Overnemen mag (MIT), met de regel "Copyright (c) 2017 vtrifonov-esfiddle" en de licentietekst. Ik raad eigen code aan: het is 30 regels en wij hebben eigen namen en toetsen.

### nradov/BreatheFree (MIT)
- **Ademhalingen per minuut en stress live** van het horloge: `source/ActivityModel.mc` regels 130-155 (`ActivityMonitor.Info has :respirationRate`, API 3.3.0; `stressScore`, API 5.0.0, met `--` als het er niet is). Samenvatting na opslaan: tijd, gemiddeld ademtempo, gemiddelde en hoogste hartslag, laps.
- Subsport 62 "same as the built-in Breathwork activity" (regel 28).
- Klachten: geen winkelreviews gevonden (geen winkellink in de README).
- **Bij Ebb:** `stressScore` is de goedkoopste weg naar "stress voor en na" (één waarde bij start en één bij einde, Ebb draait op API 5.0.0, `manifest.xml` `minApiLevel="5.0.0"`, GEZIEN). Ademtempo niet tonen tijdens geleide ademhaling: de fork van Meditate schrijft dat het bij subsport ademwerk slecht werkt door een fout in Connect IQ (README, DERDEN).

### tomaspolak82-commits/garmin-breathing (geen licentie, alleen idee)
- **Gevonden op een echte Forerunner 165 Music: "Forerunners voegen trilpatronen samen tot één lange trilling, daarom gebruikt de app alleen losse trillingen"** en "een trilling van 15 ms is voelbaar maar stoort niet" (README regel 24-25, DERDEN, Tsjechisch). In de code: één `VibeProfile` per fase (`source/BreathSession.mc` regel 176-187).
- Begeleiding alleen het eerste deel (10, 30 of 50%), daarna zelf ademen; naam van de activiteit zegt het patroon ("Koherence 5/5", regel 149-159). Slaat op als `SPORT_MEDITATION` met subsport ademwerk (regel 53, API 4.1.6).
- **Bij Ebb:** `Trillen.mc` regels 23-37 maakt reeksen met pauzes van 90 tot 300 ms (`M_INHOUDEN`, `M_HERSTEL`, `M_VAST`, `M_LAATSTE`, `M_DRIE_MIN`), en Ebb staat op 16 Forerunner-varianten (fr70, fr165, fr170, fr255, fr265, fr570, fr955, fr965, fr970 met hun varianten, GEZIEN in `manifest.xml` van 1.1.0). GOK dat onze korte pauzes op Forerunners samenvallen; niet gemeten, de simulator voelt niet. Oplossing: per moment losse tikken via een `Timer` met minstens 300 ms ertussen, of verschil in lengte in plaats van in aantal. Eigen code (geen licentie).

### massimocolella/simple-breath (GPL-3.0, alleen idee)
- **Instellingen in de telefoonapp**: `resources/settings/settings.xml` en `properties.xml` (in- en uitademen, kleur, trillen, geluid), gelezen met `Properties.getValue` (`source/RespiroView.mc` regel 101-124).
- **Scherm aan houden met grenzen**: `Attention.backlight(true)` elke zoveel seconden, in een `try`, en stoppen als het horloge weigert ("Some AMOLED devices limit prolonged backlight requests", regel 237-241 en 446-456).
- Uitademen in dezelfde kleur op 55% helderheid (regel 15); een gloed als zachte rand op schermen met veel kleuren en een dunne ring op 8 kleuren (regel 388-400).
- **Noodopslag** als het systeem de app sluit tijdens een sessie (README; `source/RespiroApp.mc` regel 23). Ebb gooit de sessie dan weg (`EbbApp.mc` regel 19-26).
- **Bij Ebb:** telefooninstellingen voor trillen, tik30, laatste3, weekdoel en My pattern naast de opslag van `Instellingen.mc` (regel 18-33); winkel toont nu bij elk horloge "settings: false" (GEZIEN, veld `settingsAvailabilityInfo`). Noodopslag in `EbbApp.onStop` overwegen (opslaan in plaats van weggooien, als de sessie langer dan 1 minuut liep). Eigen code (GPL).

### henrikkorsgaard/mindful-garmin (geen licentie, alleen idee)
- **Herinnering die de app opent**: achtergronddienst met `Background.registerForTemporalEvent` (`source/GarminBreatheApp.mc` regel 171) en `Background.requestApplicationWake("Time to breathe")` (`source/BackgroundServiceDelegate.mc` regel 12-15), toestemming `Background` in `manifest.xml`.
- Klacht die dit raakt: "needs to have ability to set daily reminders ... The apple watch has this function" (review van Breathe van Hemanth1984, 2018, GEZIEN).
- **Bij Ebb:** een dagelijkse herinnering op een gekozen uur, alleen als het weekdoel (`Instellingen.mc` `WEEKDOEL`) nog niet gehaald is. Helpt de reeks en dus reviews; geen geld binnen weken (GOK), daarom niet in de top 5. Eigen code.

### lgruen/wim-hof-garmin (MIT)
- Ogen-dicht-taal: 3 snelle tikken in, één lange zachte uit, **sterke puls elke 10 ademhalingen**, extra tik bij de laatste 5, roffel op de laatste (README; `source/WimHofBreathingView.mc` regel 184-262, met een losse `Timer` voor een tik na een korte wacht, regel 255).
- **Bij Ebb:** een zachte mijlpaal elke 10 ademhalingen in de rondes (30 tellen zonder te kijken), naast `M_LAATSTE`. Mag overgenomen worden met "Copyright (c) 2025 Leonhard Gruenschloss"; het is één regel logica, eigen code is eenvoudiger.

### SirLocke/garmin-wimhofBreathing (MIT)
- Valt netjes terug als het horloge geen subsport ademwerk kent: `source/WimHofView.mc` regel 140-146 (`Activity has :SUB_SPORT_BREATHING`, anders algemeen). Ebb draait vanaf API 5.0.0, dus niet nodig. Duidelijke veiligheidstekst in de README, zoals bij ons.

### vtrifonov-esfiddle/TestHrv (MIT)
- Losse HRV-meting van een paar minuten met dezelfde bibliotheek als Meditate. Voor Ebb niet nu: HRV is onbetrouwbaar in reviews (zie klachten), en "HRV" vraagt uitleg die snel medisch klinkt.

### Driftter-jv/Breath478 (geen licentie)
- Alleen 4-7-8 en box, sessie 1 tot 60 minuten, Engels en Spaans, "buy me a coffee". Laat zien dat **4-7-8 en box samen** het basispakket zijn. Ebb heeft box uit het menu gehaald (`Start.mc` regel 18: "Box weg (besluit 2)").

### garmin/connectiq-apps (Apache-2.0)
- `watchfaces/DanceDanceGarmin/source/DanceDanceAnimationController.mc` regels 12-77: `WatchUi.AnimationLayer` speelt een vooraf gemaakte animatie (Monkey Motion) af met een tekstlaag erboven. Zuiniger dan elke 100 ms alles tekenen (GOK, niet gemeten). Ebb tekent de zee zelf met een timer van 100 ms (`EbbView.mc` regel 55, `RustigView.mc` regel 38). Alleen interessant als de batterij een klacht wordt; nu geen.
- `device-apps/namaste`: eenvoudig voorbeeld van een activiteit met eigen FIT-velden. Ebb doet dat al.

### Spellen: farmisen/watch-invaders (MIT), black-square/BrickGame en kzibart/Garmin_FlappyWatch (geen licentie)
- watch-invaders: bediening met knoppen, vegen en tikken links of rechts tegelijk (`source/WatchInvadersDelegate.mc` regel 21-54), spellus met een timer van 200 ms (`WatchInvadersView.mc` regel 35-36).
- BrickGame: het vaste speelveld één keer in een `BufferedBitmap` tekenen en elke beurt alleen dat plaatje plus de score (`source/FallingBricksView.mc` regel 95-115 en 160-180).
- **Bij Gloop's Hat Tower (gratis):** geen geld binnen weken, dus wacht. Ebb gebruikt de buffer al voor dieren (`DierPlaatje.mc` regel 44).

## Klachten in de winkel (GEZIEN, reviews van 3 sterren of minder met tekst)

Gelezen: 11 ademapps, tot 300 reviews per app. Telling met trefwoorden; een review kan in meer groepen vallen.

| App | Reviews | Laag met tekst | Wat terugkomt |
|---|---|---|---|
| JMG Relax HR Coherence | 138 | 32 | patroon/tempo 7, crash 6, instellingen 5, trillen 4 ("Vibration stops working when the screen turns off") |
| Meditation and Breathwork | 150 | 25 | stress/HRV 7, crash 6, opslaan 5; "turns up the brightness ... painful for my eyes" (2025-12), "blank screen option on Amoled" (2026-10) |
| Meditate (vtrifonov) | 136 | 16 | opslaan 4, trillen 3 (Forerunner 245), scherm aan of inbranden |
| Meditate (dliedke) | 138 | 10 | crash 4, stress/HRV 3, trillen en geluid werken niet op Forerunner 255 |
| Breathing Timer (winnaar blinde test) | 96 | 13 | crash 4, instellingen 3 ("Venu 4 ... no menu button, no settings"), "cant turn off the auto backlight ... to save battery" (2026-05), Forerunner 55 "I choose 4:4:4, but it is 8:8:8" |
| Breathe (FikirLtd, $2,99) | 19 | 2 | "could have been a great app if there was an option to turn on vibration", timer niet in te stellen |
| Breathe (Hemanth1984) | 24 | 10 | crash 4, opslaan als activiteit 3, dagelijkse herinnering |
| WHM breathing+ ($4,99) | 300 | 1 | "harassed to provide feedback" (vraagt steeds om een review) |

Wat kopers prijzen (zelfde telling, 4 en 5 sterren): patronen en tempo (4 tot 22 per app), stress, HRV en hartslag (tot 24 van 101 bij Meditation and Breathwork), opslaan in Garmin Connect (21 van 93 bij Meditate), instellingen op de telefoon (12 tot 18).

## Waarom deze volgorde (geld)

- **1 en 2 raken de winkel**: Ebb heeft 1 download (GEZIEN, 25 nov) en Calm 10. Het hoofdbeeld haalde plek 2 tot 3 van 4 in de blinde test; beide rechters vroegen om "patterns like box/4-7-8/custom on the first image" en "a straightforward watch screenshot highlighting inhale/hold/exhale guidance and metrics" (`organisatie/blindtest/uitslag/ebb-garmin-hoofdbeeld-2026-11-24-2304.md`, GEZIEN). Het winnende beeld (Breathing Timer, zelf bekeken) toont precies dat: horloge, "HRV · BOLT · BOX · 4-7-8 · BUTEYKO", in-tellen met hartslag, en vijf pictogrammen onderaan ("Record & Analyze (FIT Activities)", "100% Private"). Ebb toont nu inhouden onder water met een schildpad.
- **3 geeft het beeld de "metrics"** en een reden om te kopen die de gratis WHM breathing niet zo toont. GOK hoeveel extra.
- **4 en 5 voorkomen slechte reviews en terugbetalingen** (Garmin kent 48 uur terugbetalen, `concurrenten-2026-11-13.md`). Met 0 reviews weegt de eerste slechte zwaar (GOK).
- Prijs ($2,99) en titel blijven: eerder gemeten in `winkel-vindbaar-2026-11-20.md`.

## Wat niet gezien is

- Geen enkele techniek is in Ebb gebouwd of op een echt horloge geprobeerd. Of onze trilreeksen op een Forerunner samenvallen: NIET GEZIEN (GOK op basis van één maker en vier reviews).
- Of `stressScore` tijdens een sessie van 2 tot 4 minuten verandert: NIET GEZIEN; de fork van Meditate zegt 5 minuten (DERDEN).
- Reviews van WHM breathing hebben bijna geen tekst (11 van 300), dus daar weinig klachten te lezen.
