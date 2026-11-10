# Onderzoek winkeltekst ademapps (Connect IQ), 10 nov 2026

Voor: Ebb ($4,99). Vraag: hoe bouwen de best verkopende betaalde ademapps hun titel en tekst op, en hoe zoekt de winkel?
Alles opgehaald op 10 nov 2026 rond 16:00 uit de winkel-API, alleen lezen, met pauzes.

## Bronnen (GEZIEN)

- Zoek-endpoint dat de winkel zelf gebruikt (gevonden in `_app-*.js`, functie `getAppsByKeywords`):
  `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords?keywords=<woord>&startPageIndex=0&pageSize=30&sortType=mostRelevant`
  Sorteringen: `mostRelevant` (standaard op de zoekpagina), `mostPopular`, `highestRated`, `mostRecent`. Optioneel `appType` (watch-app, widget, datafield, watchface).
- Appdetails: `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/<id>`. Alleen de details geven `pricing` (prijs). De zoekresultaten geven geen prijs.
- Let op: `paymentModel` zegt niet of een app betaald is. WHM breathing+ kost $4,99 maar heeft `paymentModel: 0` (prijs zit in `pricing.listPrice`). `paymentModel: 1` hoort bij apps die buiten de winkel ontgrendelen (activeringscode, kpay, proefperiode). (GEZIEN in details; betekenis van 1 is GOK op basis van de teksten.)
- Werkbestanden staan alleen in de kladmap van deze sessie, niet in de repo.

## 1. De vijf best verkopende betaalde ademapps (betaald via de winkel)

Ik heb 131 ademapps (naam of tekst over adem, apneu, freediving, Wim Hof) uit de zoekresultaten gehaald en van elk de details opgevraagd. 23 hebben een winkelprijs. Gesorteerd op downloadklasse en reviews (GEZIEN, details-URL per app hierboven met de id):

| # | App (maker) | Prijs | Downloads | Reviews | Score | Sinds | Talen |
|---|---|---|---|---|---|---|---|
| 1 | WHM breathing+ (MobileDriveway), id 3543ef5f-a9ea-48ed-a0dd-925155e9c7b5 | $4,99 | 1.000+ | 604 | 4,9 | dec 2024 | alleen en |
| 2 | Breathe: Breathing Exercises (FikirLtd), id 93b31a7d-4500-41f8-a2de-9e91c9bcf86f | $2,99 | 1.000+ | 18 | 4,4 | mrt 2026 | alleen en |
| 3 | Breath Training System PRO - CO2, O2 & Dry Apnea (Bitochi, "BTS PRO"), id 12b88972-bc50-40c7-a138-e1e8d6f38068 | $6,25 | 100+ | 34 | 4,7 | apr 2026 | alleen en |
| 4 | Breath for Health (Deyve), id 69a772e3-0b6c-489e-9861-e52d7da09a3f | $2,99 | 100+ | 11 | 4,4 | sep 2025 | en, de |
| 5 | HRV Breathing (Oltek), id 5cc2c150-48e8-4e9f-9a2a-700662edd0b2 | $3,99 | 100+ | 8 | 4,9 | jan 2026 | alleen en |

Buiten de lijst, wel nuttig (GEZIEN):
- JMG-APP Apnea Training (Surfy66): 10.000+ downloads, 82 reviews, maar gratis met betaalde ontgrendeling via code (`paymentModel 1`, geen winkelprijs). Talen fr en en.
- Breath and Plunge (WHM style) PRO plus Sauna (WhiteBear): $2,99, 10+ downloads, 9 reviews, 7 talen (en, es, de, fr, pt_PT, pl, pt_BR).
- BreathGym (ThijsGer): $1,99, 100+, 7 reviews, 16 talen. Veel talen helpt dus niet vanzelf.
- Verder betaald met prijs: Vytera Breath $4,99 (0 downloads), BREATHWORK $4,49, ApneaFlow PRO $5,25, allemaal 10 of minder downloads.
- Categorie: bijna alle ademapps hebben categorie-id 219; BTS PRO en ApneaFlow PRO 212, HRV Breathing 254, JMG-APP 213 (GEZIEN). De namen van die id's heb ik niet in de API gevonden (GOK: 219 is gezondheid/welzijn).

### Titel en eerste zin (GEZIEN, exact)

1. **WHM breathing+** (14 tekens). Eerste zin: "This is tracker app for breathing exercise, similar to the one used by Wim Hof (WHM)."
   Tekst 3.841 tekens, 31 regels, 17 opsommingen met "-", één kopje "INSTRUCTIONS" met een genummerde handleiding van 7 stappen. Begint met wat de betaalde versie extra heeft, dan wat er in Garmin Connect komt (hartslag, stress, eigen grafieken: rondes, ademhalingen, langste inhoudtijd). Taalfouten ("warnig", "predifined"). Verkoopt door de gratis broer WHM breathing (50.000+ downloads, 1.731 reviews), niet door de tekst.
2. **Breathe: Breathing Exercises** (28 tekens, merk + dubbele punt + zoekwoord). Eerste zin: "Guided breathing exercises on your wrist — 11 patterns, an animated circle, and a vibration cue for every phase so you can practise breathwork with your eyes closed."
   Tekst 3.910 tekens, 44 regels, 30 opsommingen. Kopjes in hoofdletters: ELEVEN BREATHING PATTERNS, MAKE IT YOURS, CONTROLS, WHAT'S NEW IN VERSION 13, WORKS ON 68 GARMIN WATCH MODELS. Elk patroon met naam en getallen ("Box Breathing 4-4-4-4", "4-7-8", "Coherent 5-5", "Cyclic Sigh"). Zinnen als "No phone, no account, no internet. One-time purchase: no subscription, no ads." Eindigt met een link naar de gratis versie, een vraag om een review en een regel **"Tags: breathing exercises, breathwork, box breathing, meditation, mindfulness, relaxation, stress relief, calm, sleep, anxiety, pranayama, guided breathing, coherent breathing, deep breathing, HRV."**
3. **Breath Training System PRO - CO2, O2 & Dry Apnea** (48 tekens, naam + streepje + zoekwoorden). Eerste zin: "Breath Training System turns your Garmin into a freediving and apnea coach, not just a timer." Tweede regel: "Stop guessing your apnea training. Let your watch coach it."
   Tekst 2.305 tekens, 43 regels, 32 opsommingen met "•". Zes kopjes in hoofdletters: TRAIN EVERY WAY, IT ADAPTS TO YOU, IT READS YOUR BODY, SEE YOURSELF IMPROVE, SAVED TO GARMIN CONNECT, MADE FOR THE WATCH. Noemt "Wim Hof Power" als patroon, "CO2 and O2 tables", "Static apnea", "Box 4-4-4-4", "Pranayama 4-7-8". Eindigt met een veiligheidsregel (nooit in of bij water zonder buddy).
4. **Breath for Health** (17 tekens; Duits: "Atmen für die Gesundheit"). Eerste zin: "Slow breathing has a number of positive effects on health, such as increasing heart rate variability and reducing stress." Tekst 856 tekens, 3 alinea's, geen kopjes, geen opsomming.
5. **HRV Breathing** (13 tekens). Eerste zin: "Resonant Breathing app for HRV training, designed for night-time use." Tekst 3.469 tekens, 20 opsommingen, kopjes "Features" en "How to Use", noemt "Works on 80+ Garmin watches" en "No data collection".

Extra: WhiteBear PRO begint met drie korte zinnen: "Master your breath. Conquer the cold. Track every second of it." Kopjes als WHERE ARE THE SETTINGS?, TRY BEFORE YOU BUY, NINE PRACTICE PROFILES (GEZIEN).

### Patroon (mijn lezing van de data)
- Titel: kort merk plus het zoekwoord ("Breathe: Breathing Exercises", "HRV Breathing") of merk plus een rij zoekwoorden na een streepje ("... - CO2, O2 & Dry Apnea"). (GEZIEN)
- Eerste zin zegt in één keer wat het is en voor wie, met het hoofdzoekwoord erin. (GEZIEN)
- De nieuwe apps die goed lopen (Breathe, BTS PRO, HRV Breathing) gebruiken 2.300 tot 3.900 tekens, kopjes in HOOFDLETTERS en veel opsommingen; ze noemen "Garmin Connect", "no subscription", "offline", aantal horloges. (GEZIEN)
- Alle vijf de besten hebben alleen Engels (op één Duitse na). (GEZIEN) Of meer talen meer verkoop geeft: GOK, BreathGym met 16 talen haalt ook maar 100+.

## 2. Zoekwoorden: wie staat bovenaan

Top 10 bij `mostRelevant` (zo opent de zoekpagina), GEZIEN via `.../apps/keywords?keywords=<woord>&sortType=mostRelevant`. "betaald" = `paymentModel 1` of winkelprijs; voor apps met winkelprijs (WHM+, Breathe, BTS PRO) staat dat erbij, want de zoek-API toont die als gratis.

- **breathing** (992 treffers): 1 Box Breathing (Dialforge, betaald ext.), 2 Mindful - Meditation & Breathing (Bash, betaald ext.), 3 Breathing Exercises (SimonSteinhuber, gratis), 4 Tactical Breathing (gratis), 5 WHM breathing+ ($4,99), 6 Breathing Assistant, 7 Breathing Exercises (liamb09), 8 WHM breathing (gratis, 1.731 reviews), 9 HRV Breathing (Oltek, $3,99), 10 Kids Breathing (Oltek, $4,49).
- **breath hold** (995): 1 BreathGym (ThijsGer, $1,99), 2 Breath Hold Trainer (gratis), 3 StatiQ Apnea & Breath-Hold Trainer (betaald ext.), 4 Breath – Guided Breathing, HRV & Breath Holds (gratis), 5 Breath Hold Coach: Apnea Tables (Dialforge, betaald ext.), 6 Apnea & Breath Hold Trainer by BreakFinder, 7 Breath (wijzerplaat), 8 Moon Hold (wijzerplaat), 9 Breath Training (Deyve, $2,99), 10 Vytera Breath ($4,99).
- **breathwork** (995): 1 Breathwork (Kegles, $1,99), 2 Breathwork (No_Try_Hard, gratis), 3 BREATHWORK (Sticreations, $4,49), 4 Parnayam (Breathwork), 5 Easy Breathwork, 6 Meditation and Breathwork (gratis, 150 reviews), 7 Stress and HR Graph ... Breathwork (datafield), 8 ZenBreath, 9 Breathe Free: Box Breathing, 10 Sauna Laps.
- **Wim Hof** (204): 1 DeepBreath - Wim Hof Breathing and Cold (gratis), 2 Cold Plunge & Sauna+Wim Hof breathing preparation (betaald ext.), 3 Breathing Timer: HRV · BOLT · Wim Hof · 4-7-8 (gratis, 92 reviews), 4 Breathwork (No_Try_Hard), 5 Oxygenate+ (betaald ext.), 6 Breathing Exercises (SimonSteinhuber), 7 Prayer Times Wimbledon (!), 8 Breath and Plunge (WHM style) Lite, 9 Breathwork (Kegles, $1,99), 10 BTS PRO ($6,25). WHM breathing+ staat hier niet in de top 10 bij relevantie, wel op 5 bij `mostPopular`.
- **freediving** (993): 1 tot 3 en 5 wijzerplaten "Frontline Freediving", 4 Freediving & Apnea Breathing Trainer (gratis), 6 Dive Timer - Freediving Surface Coach, 7 VzMy with Freedivig, 8 Freediver & Mermaid Apnea, 9 ApneaFlow PRO ($5,25), 10 inDepth Dry. Geen sterke betaalde app.
- **apnea** (142): 1 BreathGym ($1,99), 2 JMG-APP Apnea Training (betaald ext., 10.000+), 3 Freediver – Apnea Training, 4 Freediver & Mermaid Apnea, 5 Apnea Static Timer, 6 Dynamic/Static Apnea Trainer, 7 Apnea Sense, 8 Freediving & Apnea Breathing Trainer, 9 Apnea Dynamics Interval Training, 10 Static Apnea Training Tables (50 reviews). Alle gratis behalve 1 en 2.
- **box breathing** (997): 1 Box Breathing (Dialforge), 2 Breathe: Box Breathing (scheir.eu), 3 Breathe Free: Box Breathing (FikirLtd), 4 Four - Guided Box Breathing, 5 Box (wijzerplaat, betaald), 6 Box to Box, 7 Breathing Exercises (liamb09), 8 Breathing Exercises (SimonSteinhuber), 9 Mindful (betaald ext.), 10 Box to Box Free.
- **CO2 table** (983): 1 CO2 Table (gratis), 2 Table (wijzerplaat), 3 GB Grid CO2, 4 CO2 Savings Datafield, 5 table, 6 Apnea Tables - CO2 and O2 Hold Training ($2,99), 7 Table Tennis Go, 8 tot 10 losse "table"-dingen. Bijna leeg: wie "CO2 table" in de titel heeft, staat bovenaan.
- **4-7-8**: 0 treffers. Het streepje breekt de zoekopdracht (GEZIEN). "4 7 8" geeft wel Breathing Timer bovenaan, "478" geeft Breath 478 (Driftter) en Deep Calm Breathing (GEZIEN).
- **relax** (999): bijna alleen wijzerplaten met "Relax" in de naam (RELAX, Relax, Snoopy Relax). Geen ademapp in de top 10. Geen goed woord voor ons.

### Zoekt de winkel ook in de tekst? Ja (GEZIEN)
Test met woorden die alleen in een beschrijving staan:
- "Huberman" staat alleen in de tekst van Breathe (FikirLtd): die staat op 1.
- "mammalian" alleen in de tekst van BTS PRO: op 1.
- "predifined" (tikfout, alleen in de tekst van WHM breathing+): op 1.
- "hyperventilate": Apnea Static Timer en BTS PRO bovenaan (beide in de tekst).
- "Atmen" en "respiración" vinden ademapps via hun Duitse of Spaanse tekst: de winkel zoekt in alle talen tegelijk.

Verder (GEZIEN): de zoeker is vaag (fuzzy). "Wim Hof" vindt ook "Wimbledon", "Huberman" ook "Barman", "box breathing" ook wijzerplaat "Box". Het aantal treffers staat bijna altijd net onder 1.000, dus de rest is opvulling. Titeltreffers staan boven teksttreffers: bij "breathing" komen eerst apps met het woord in de titel (GOK op volgorde, past bij alles wat ik zag). Reviews en downloads tellen bij `mostRelevant` weinig: een app met 0 reviews en 10 downloads (Box Breathing) staat boven WHM breathing+ (GEZIEN).

## 3. Eigen titel en tekst per taal

- Ja. Elke app heeft een lijst `appLocalizations` met per taal `locale`, `name`, `description`, `whatsNew` en `heroImageFileId` (GEZIEN, bijvoorbeeld de details van Breath for Health: en "Breath for Health", de "Atmen für die Gesundheit"; Box Breathing van Dialforge heeft 28 talen: en, pl, de, fr, es, nl, ja, it, zh_CN, ru, pt_BR, cs, pt_PT, ko, sv, da, nb, zh_TW, fi, sk, sl, in, hu, th, el, hr, iw, ms).
- De API geeft altijd alle talen terug; de website kiest zelf de taal van de bezoeker (in de JS wordt elke app met de `locale` van de pagina omgezet). `Accept-Language` is dus niet nodig (GEZIEN in de JS; dat de site terugvalt op de eerste taal als die van de bezoeker ontbreekt is GOK).
- Lengtes over 5.755 taalteksten van 798 apps (GEZIEN):
  - Titel: langste is precies 50 tekens (meerdere apps), niemand komt erboven. Max is dus waarschijnlijk 50 (GOK op grond van die grens).
  - Beschrijving: langste is precies 4.000 tekens, 118 teksten zitten tussen 3.990 en 4.000. Max is 4.000 (GOK, maar zeer waarschijnlijk).
  - "What's new": ook max 4.000.

## 4. Mag "Wim Hof" in onze tekst?

- WHM breathing+ is niet van Wim Hof. De maker is MobileDriveway, die ook weer-apps maakt (Open Weather Widget). De tekst zegt zelf "similar to the one used by Wim Hof (WHM)" (GEZIEN). Geen `trustedDeveloper` (GEZIEN: false).
- Geen enkele app in de winkel lijkt van het officiële Wim Hof-bedrijf (geen maker met die naam in 798 apps, GEZIEN binnen mijn set).
- Drie apps hebben "Wim Hof" in de titel: DeepBreath - Wim Hof Breathing and Cold (1.000+), Cold Plunge & Sauna+Wim Hof breathing preparation, Breathing Timer: HRV · BOLT · Wim Hof · 4-7-8 (1.000+). Vier hebben "WHM" in de titel (WHM breathing, WHM breathing+, Breath and Plunge (WHM style) Lite en PRO). Elf noemen het alleen in de tekst, waaronder WHM+, BTS PRO ("Wim Hof Power") en WhiteBear ("Built for Wim Hof Method practitioners") (GEZIEN).
- Garmin laat het dus toe in titel en tekst (GEZIEN: het staat er). Juridisch: "Wim Hof Method" is een merk van zijn bedrijf (Innerfire) (GOK, niet nagekeken). Veilig advies: niet in de titel, wel één keer beschrijvend in de tekst, bijvoorbeeld "rounds of deep breathing and breath holds, in the style of the Wim Hof method", zonder te doen alsof het officieel is. Dan vindt de zoeker ons op "Wim Hof" (hij zoekt in de tekst) zonder merkrisico in de titel.

## Wat dit betekent voor Ebb (advies, geen feit)

1. Titel van hoogstens 50 tekens met de zoekwoorden erin, bijvoorbeeld "Ebb: Breath Hold & Breathing Trainer" of "Ebb - Breathwork, Breath Hold & Apnea". Alleen "Ebb" wordt op geen enkel zoekwoord gevonden.
2. Eerste zin: wat het is plus hoofdzoekwoord, zoals Breathe en BTS PRO.
3. Tekst 3.000 tot 4.000 tekens met kopjes in hoofdletters en opsommingen. Schrijf de woorden voluit die mensen zoeken: breathing, breath hold, breathwork, apnea, freediving, CO2 table, O2 table, box breathing, "4 7 8" (zonder streepjes, of naast "4-7-8"), HRV, Garmin Connect. Een slotregel "Tags: ..." zoals Breathe werkt omdat de winkel in de tekst zoekt.
4. Vertalingen helpen voor vindbaarheid in die taal (de zoeker leest alle talen), maar de best verkopende apps hebben alleen Engels. Eerst een sterke Engelse tekst; Duits, Frans, Spaans en Nederlands kunnen erbij als het weinig moeite kost.
5. Laag hangend fruit: "CO2 table", "freediving" en "apnea" hebben geen sterke betaalde app bovenaan.
