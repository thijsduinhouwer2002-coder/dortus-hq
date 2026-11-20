# Garmin: winkelpagina's beter vindbaar en overtuigender (20 nov 2026)

Opdracht van Thijs (20 nov 11:33): Garmin krijgt marketing. Gemaakt door de Garmin-winkelmaker. Alleen gelezen en geschreven: niets in de winkel veranderd, niets gebouwd. Alle winkelcijfers zijn GEZIEN op 20 nov 2026 tussen 10:35 en 10:55 UTC met `curl` op de open API van de winkel (adressen in deel 1). Deze teksten gaan eerst naar een keurder; daarna zet de hoofdchat ze in de winkel.

## Samenvatting (de drie wijzigingen die het meeste opleveren)

1. **Fout gevonden: wie de winkel in het Frans, Spaans, Italiaans, Pools of een andere taal opent, ziet bij Ebb de Duitse titel en tekst** (GEZIEN). De winkel neemt bij een ontbrekende taal de eerste taal uit de lijst, en bij Ebb is dat Duits (bij Calm Engels).
2. **Wijziging 1:** Engels als eerste taal van Ebb zetten, en Frans toevoegen (tekst staat klaar in deel 3). Zo leest elke koper buiten Duitsland en Nederland weer Engels, en Frankrijk zijn eigen taal.
3. **Wijziging 2:** eerste zinnen van Ebb op ons sterkste woord zetten ("breath hold", plek 2) met "one payment, no subscription", plus een link naar de gratis Ebb Calm om eerst te proberen. Calm linkt al naar Ebb (staat live); die zin noemt nu ook box breathing.
4. **Wijziging 3:** extra titelwoorden via de andere talen. De zoeker kijkt in de titels van alle talen tegelijk (GEZIEN), dus "Breathwork" in de Duitse en Nederlandse titel en "respiration" en "souffle" in de Franse geven nieuwe treffers zonder de Engelse titel langer te maken.
5. **Engelse titel van Ebb blijft** "Ebb Breathing & Breath Hold": sinds deze kortere titel (17 nov) steeg Ebb op breathing van 31 naar 18 en op breath hold van 4 naar 2 (GEZIEN).
6. **Waar Ebb nu staat (GEZIEN):** breath hold 2, 478 7, breath training 10, breath 14, breathing 18, breathing exercises 21, breathwork 33, box breathing 41; niet in de eerste 90 bij stress, meditation, freediving, apnea, wim hof.
7. **Beelden:** bij Ebb het beeld "Hold" eerst (past bij de zoekterm), bij Calm een beeld dat naar de volle Ebb wijst in plaats van het pauzescherm.
8. **Prijs:** $2,99 / €3,49 houden. Het is de middenprijs (mediaan $2,99 van 17 betaalde ademapps, GEZIEN); goedkoper verkoopt niet beter, zichtbaarheid en reviews wel.

## 1. Hoe vindt men apps in de Connect IQ-winkel?

**De zoek-API (GEZIEN, ook in de code van de winkelpagina, functie `getAppsByKeywords`):**
`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords?keywords=<woord>&startPageIndex=0&pageSize=30&sortType=mostRelevant`
- Velden die de pagina meestuurt: alleen `keywords`, `startPageIndex`, `pageSize`, `sortType` en `appType`. **Geen taal en geen land:** iedereen krijgt dezelfde volgorde (GEZIEN in de code).
- De zoekpagina opent op `mostRelevant`; andere keuzes zijn `mostPopular`, `highestRated`, `mostRecent`. Links op de pagina kan de bezoeker een soort kiezen (wijzerplaat, app, widget, veld); standaard staat alles door elkaar (GEZIEN in de code).
- Antwoord: `totalCount` en per app onder meer `appLocalizations` (per taal titel en tekst), `downloadCount`, `reviewCount`, `averageRating`, `categoryId`, `typeId`, `paymentModel`. **Geen prijs**; die staat alleen in de details: `.../api/asw/apps/<id>` (veld `pricing.listPrice`).
- `downloadCount` is een klasse: de winkel toont 0, of het getal met een plus (1+, 10+, 100+, 1K+) (GEZIEN in de code).
- "gratis, ontgrendelen buiten winkel" in de tabellen = `paymentModel 1` zonder winkelprijs; dat zijn apps die een code of eigen betaling gebruiken (GOK op de betekenis, zie `onderzoek-winkeltekst-2026-11-10.md`).

**Welke velden tellen (GEZIEN met proeven):**
- **De titel telt het zwaarst.** Calm heeft "Relaxation" in de titel en staat op relaxation op 6; Ebb heeft het woord alleen in de tags en staat niet in de eerste 90.
- **Een korte titel wint.** Bovenaan bij breathing staan titels van twee woorden (Box Breathing, Tactical Breathing, HRV Breathing). Ebb ging van "Ebb: Breathing Exercises, Breath Hold & Calm" naar "Ebb Breathing & Breath Hold" (versie 1.0.1, 17 nov) en steeg op breathing van 31 naar 18 en op breath hold van 4 naar 2; het viel op breathing exercises van 5 naar 21 en op calm van 43 naar 67, omdat die woorden uit de titel gingen (GEZIEN, oude cijfers uit `meting-ebb-calm.md`).
- **De beschrijving telt ook, maar zwak.** Zeldzame woorden uit een tekst vinden de app wel (eerder bewezen met "Huberman" en "predifined", `onderzoek-winkeltekst-2026-11-10.md`); bij gewone woorden komt een teksttreffer zelden in de top 30.
- **Alle talen tellen mee.** "atem" geeft Ebb op 1 (Duitse titel), "ademhaling" geeft Ebb op 1 (Nederlandse titel), "atemübungen" Calm 3 en Ebb 4 (GEZIEN). Een titel in een andere taal is dus een extra titelveld voor de zoeker.
- **Streepjes breken de zoekopdracht.** "4-7-8" geeft 0 treffers. "4 7 8" vindt alleen apps met 4-7-8 in de titel (Breathing Timer op 1), verder wijzerplaten met een 4 of 8. "478" werkt (44 treffers; Calm 3, Ebb 7) (GEZIEN).
- **Downloads en reviews tellen weinig** bij "meest relevant": Box Breathing (10+, 0 reviews) staat op breathing boven WHM breathing (50000+, 1733 reviews) (GEZIEN).
- **Categorie:** Ebb en Calm hebben categorie 254. De web-winkel heeft geen bladerlijst per categorie; de namen van de nummers heb ik niet gevonden (GOK dat de categorie voor zoeken niet telt).
- **Grenzen (GEZIEN, 8679 titels en teksten uit de zoekresultaten):** titel hoogstens 50 tekens (198 titels precies 50, geen enkele erboven), tekst hoogstens 4.000 tekens (geen enkele erboven), hoogstens 5 schermafbeeldingen (771 apps met 5, geen met meer).

**Fout gevonden: welke taal ziet de bezoeker? (GEZIEN)**
De pagina zoekt de taal van de bezoeker in `appLocalizations`; staat die er niet in, dan neemt hij **de eerste uit de lijst** (code van de winkel: `appLocalizations.find(...) || appLocalizations[0]`). De lijst van Ebb is `de, nl, en`; die van Calm en Hat Tower `en, de, nl`. Gemeten met de pagina zelf:

| Taal van de winkel | Ebb toont | Calm toont |
|---|---|---|
| en-US, en-GB | Engels | Engels |
| de-DE, de-AT | Duits | Duits |
| nl-NL | Nederlands | Nederlands |
| fr-FR, es-ES, it-IT, pl-PL | **Duits** ("Ebb Atemübungen & Atem anhalten") | Engels |

Dat geldt voor de titel in de zoeklijst en voor de hele pagina. Een Franse of Spaanse bezoeker ziet dus een Duitse tekst over een Engelstalige app. Hoeveel bezoekers dat zijn: niet bekend (GOK: Frankrijk, Spanje en Italië zijn grote markten voor Garmin). Of de telefoon-app van Garmin dezelfde regel gebruikt: NIET GEZIEN.

## 2. Waar staan wij, en wat doen de toppers anders?

**Plekken van Ebb en Ebb Calm (GEZIEN, eerste 90 resultaten, meest relevant). "-" is niet in de eerste 90.**

| Zoekterm | Treffers | Ebb (alles) | Calm (alles) | Ebb (alleen apps) | Calm (alleen apps) |
|---|---|---|---|---|---|
| breathing | 993 | 18 | 27 | 18 | 25 |
| breath | 994 | 14 | 61 | 12 | 57 |
| breath hold | 996 | **2** | 71 | **2** | 57 |
| breathwork | 996 | 33 | 42 | 29 | 38 |
| box breathing | 996 | 41 | 52 | 31 | 37 |
| 4-7-8 | 0 | - | - | - | - |
| 478 | 44 | 7 | 3 | 4 | 3 |
| 4 7 8 | 998 | - | - | niet gemeten | niet gemeten |
| stress | 998 | - | - | - | - |
| relax | 998 | - | 55 | - | 10 |
| relaxation | 997 | - | 6 | 44 | 4 |
| calm | 998 | 67 | 33 | 4 | **1** |
| meditation | 997 | - | - | - | - |
| freediving | 992 | - | - | niet gemeten | niet gemeten |
| apnea | 162 | - | - | niet gemeten | niet gemeten |
| wim hof | 227 | - | - | niet gemeten | niet gemeten |
| breathing exercises | 997 | 21 | 4 | 21 | 4 |
| breath training | 994 | 10 | - | 9 | - |
| ebb | 97 | 1 | 2 | niet gemeten | niet gemeten |
| atem / atemübungen | 994 / 993 | 1 / 4 | 7 / 3 | niet gemeten | niet gemeten |
| ademhaling / ademhalingsoefeningen | 993 / 996 | 1 / 1 | - / - | niet gemeten | niet gemeten |
| respiration / souffle | 1000 / 507 | - / - | - / - | niet gemeten | niet gemeten |

"Alles" is wat de zoekpagina standaard toont (wijzerplaten, apps, widgets en velden door elkaar). Bij calm, relax en stress staan vooral wijzerplaten bovenaan; filtert iemand op apps, dan staat Calm op calm op 1 en Ebb op 4.

**Freediving, apnea en wim hof laten we bewust liggen:** ons besluit is dat Ebb nooit een freedive- of apneatrainer heet (besluiten, 12 nov), Garmin verbiedt apps voor gevaarlijke activiteiten als vrijduiken (App Review Guidelines 1b), en Wim Hof is een merknaam (Guidelines 3a: "be careful using brand names").

**Wat de toppers anders doen (GEZIEN, details en beelden van de winkel):**
- **Titel:** de toppers hebben het zoekwoord als hoofdwoord in een korte titel ("Breathwork", "Box Breathing", "HRV Breathing") of merk plus dubbele punt plus zoekwoorden ("Breathe: Breathing Exercises", 28 tekens). Ebb doet dat al sinds 1.0.1.
- **Eerste zin:** zegt in één keer wat het is, met het zoekwoord: "Guided breathing exercises on your wrist: 11 patterns, an animated circle, and a vibration cue for every phase..." (Breathe, $2,99, 1000+). Onze eerste zin begint met "Breathwork rounds and calm 4-7-8 breathing", maar noemt "breath hold" (ons beste woord) niet, en de prijsvorm (eenmalig) pas onderaan.
- **Gratis broertje met link:** de twee betaalde ademapps met 1000+ hebben allebei een gratis broertje. WHM breathing+ ($4,99, 1000+, 610 reviews) heeft WHM breathing (gratis, 50000+). Breathe ($2,99, 1000+) en Breathe Free (gratis, 100+) linken in hun tekst met een winkeladres naar elkaar, in beide richtingen. Calm linkt al naar Ebb (staat live sinds 1.0.1); Ebb linkt nog niet naar Calm.
- **Schermafbeeldingen:** Breathe zet onder elk beeld één feit ("11 breathing patterns", "Saves to Garmin Connect", "Sessions up to 60 min"); BreathGym toont het horloge aan een pols met "Breath-hold timer". Onze beelden zijn mooier en hebben koppen, maar zeggen vooral sfeer (zee, dieren); geen beeld zegt in één regel wat je voor je geld krijgt, en geen beeld toont Garmin Connect.
- **Prijs:** zie deel 5. Ebb zit met $2,99 in het midden.
- **Talen:** de best verkopende betaalde ademapps zijn alleen Engels (WHM breathing+, Breathe, HRV Breathing). Veel talen helpt niet vanzelf (BreathGym, 16 talen, 100+). Voor ons telt een taal vooral om de Duitse terugval op te lossen en als extra titelveld.

### Top 10 per zoekterm (GEZIEN, 20 nov ±10:40 UTC, meest relevant, alle soorten)

Prijs uit de details van elke app (dollar). Lange streepjes in namen van anderen zijn vervangen door een gewoon streepje.

**breathing** (993 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Box Breathing | Dialforge.dev | app | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 2 | Tactical Breathing | g1zmo | app | 100+ | gratis | 4 (5.0) |
| 3 | HRV Breathing | Oltek | app | 100+ | $3.99 | 8 (4.9) |
| 4 | Breathing Assistant | Oski3K | app | 10+ | gratis | 1 (5.0) |
| 5 | Breathing Exercises | liamb09 | app | 100+ | gratis | 0 |
| 6 | WHM breathing+ | MobileDriveway | app | 1000+ | $4.99 | 610 (4.9) |
| 7 | WHM breathing | MobileDriveway | app | 50000+ | gratis | 1733 (4.8) |
| 8 | Breathing Exercises | SimonSteinhuber | app | 1000+ | gratis | 7 (3.3) |
| 9 | Kids Breathing - with Resonant Breathing Pet | Oltek | app | 1+ | $4.49 | 1 (5.0) |
| 10 | Box Breathing: Tactical | Oltek | app | 1+ | $2.49 | 0 |

**breath** (994 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Breathbeat: Breathwork & Breath Holds | NeronLLC | app | 1+ | $3.99 | 1 (2.0) |
| 2 | Breath | RiseUp | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |
| 3 | Breath - Guided Breathing, HRV & Breath Holds | wolftronics | app | 10+ | gratis | 0 |
| 4 | Breath Pacer - Paced Breathing Timer | RiversideArt | app | 10+ | gratis | 0 |
| 5 | BreathGym - Breath Hold Trainer | ThijsGer | app | 100+ | $1.99 | 7 (4.4) |
| 6 | Breath Training | Deyve | app | 10+ | $2.99 | 0 |
| 7 | Vytera Breath | VyteraLabs | app | 0 | $4.99 | 0 |
| 8 | Mountain Breath | Madeline | wijzerplaat | 1+ | gratis, ontgrendelen buiten winkel | 0 |
| 9 | Breath Coach | DMSWatchApps | app | 10+ | gratis | 0 |
| 10 | Breath 478 | Driftter | app | 10+ | gratis | 1 (5.0) |

**breath hold** (996 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | BreathGym - Breath Hold Trainer | ThijsGer | app | 100+ | $1.99 | 7 (4.4) |
| 2 | Ebb Breathing & Breath Hold | Dortus | app | 1+ | $2.99 | 0 |
| 3 | Breath Hold Trainer | jonathan.orsel | app | 100+ | gratis | 0 |
| 4 | Breathbeat: Breathwork & Breath Holds | NeronLLC | app | 1+ | $3.99 | 1 (2.0) |
| 5 | StatiQ - Apnea & Breath-Hold Trainer CO2/O2 | Jakub | app | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 6 | Breath - Guided Breathing, HRV & Breath Holds | wolftronics | app | 10+ | gratis | 0 |
| 7 | Breath Hold Coach: Apnea Tables | Dialforge.dev | app | 1+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 8 | Apnea & Breath Hold Trainer by BreakFinder | breakfinder.surf | app | 100+ | gratis | 2 (5.0) |
| 9 | Breath Pacer - Paced Breathing Timer | RiversideArt | app | 10+ | gratis | 0 |
| 10 | Breath | RiseUp | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |

**breathwork** (996 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Breathwork | Kegles | app | 10+ | $1.99 | 0 |
| 2 | Breathwork | No_Try_Hard | app | 1000+ | gratis | 6 (4.3) |
| 3 | BREATHWORK | Sticreations | app | 10+ | $4.49 | 3 (4.3) |
| 4 | Parnayam (Breathwork) | RishiRaj | app | 10+ | gratis | 0 |
| 5 | Easy Breathwork | Ben0713 | app | 1+ | gratis | 0 |
| 6 | Meditation and Breathwork | FlorianGeigl | app | 10000+ | gratis | 150 (4.3) |
| 7 | GroundApp: Breathwork with Bodie | GroundApp | app | 10+ | gratis | 0 |
| 8 | Breathbeat: Breathwork & Breath Holds | NeronLLC | app | 1+ | $3.99 | 1 (2.0) |
| 9 | Stress and HR Graph for Yoga Meditation Breathwork | AccessTech | widget | 100+ | gratis | 0 |
| 10 | ZenBreath | WeAreCollective | app | 100+ | gratis | 2 (5.0) |

**box breathing** (996 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Box Breathing | Dialforge.dev | app | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 2 | Breathe: Box Breathing | scheir.eu | app | 100+ | gratis | 1 (5.0) |
| 3 | Box Breathing: Tactical | Oltek | app | 1+ | $2.49 | 0 |
| 4 | Breathe Free: Box Breathing | FikirLtd | app | 100+ | gratis | 5 (4.4) |
| 5 | Four - Guided Box Breathing | ShayneBoyer | app | 1+ | gratis | 0 |
| 6 | Stirra Boxenschild: Horse Name Plate | breakfinder.surf | wijzerplaat | 1+ | gratis | 0 |
| 7 | Box | NowClockFaces | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |
| 8 | Box to Box | VyteraLabs | app | 1+ | $4.99 | 0 |
| 9 | Breathing Exercises | liamb09 | app | 100+ | gratis | 0 |
| 10 | Breathing Exercises | SimonSteinhuber | app | 1000+ | gratis | 7 (3.3) |

**478** (44 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Breath 478 | Driftter | app | 10+ | gratis | 1 (5.0) |
| 2 | Deep Calm Breathing | Deyve | app | 10+ | $2.75 | 2 (3.0) |
| 3 | Ebb Calm: Breathing Exercises & Relaxation | Dortus | app | 10+ | gratis | 0 |
| 4 | PWF NEXUS-X (Enhance Material) | PWFGarmin | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 2 (5.0) |
| 5 | Isohypse Digital Lite - Topo Mountain Watch Face | Proficode | wijzerplaat | 100+ | gratis | 7 (5.0) |
| 6 | Isohypse Analog Lite - Topo Mountain Watch Face | Proficode | wijzerplaat | 1000+ | gratis | 12 (4.8) |
| 7 | Ebb Breathing & Breath Hold | Dortus | app | 1+ | $2.99 | 0 |
| 8 | Zen | PixelPaceStudios | wijzerplaat | 100+ | $1.99 | 6 (3.7) |
| 9 | PWF Classic Digital (Enhance material & Colors) | PWFGarmin | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 10 | Portal PRO - GB | GreenBlack | wijzerplaat | 1000+ | $4.99 | 206 (4.8) |

**4 7 8** (998 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Breathing Timer: HRV · BOLT · Wim Hof · 4-7-8 | BreathingTimer | app | 1000+ | gratis | 94 (4.5) |
| 2 | DataPro + 4 to 7 Day Weather Forecast! | pstoppani | wijzerplaat | 1000+ | gratis, ontgrendelen buiten winkel | 127 (4.8) |
| 3 | Infogram Analog - 4 to 7 day weather forecast! | pstoppani | wijzerplaat | 1000+ | gratis | 179 (4.8) |
| 4 | Goals 8 | VAW.BE | wijzerplaat | 100000+ | gratis | 20255 (4.8) |
| 5 | Halloween 8 | GreenPoint | wijzerplaat | 1+ | $1.99 | 0 |
| 6 | Halloween 7 | GreenPoint | wijzerplaat | 1+ | $1.99 | 0 |
| 7 | World Time 4 | Dialforge.dev | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 8 | Analogue 7 | GreenPoint | wijzerplaat | 0 | $1.99 | 0 |
| 9 | C 8 | Indrek.V | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 10 | T.Rex Quad 4 | Trudelta | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 7 (4.3) |

**stress** (998 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Average/Delta Stress | Trudelta | widget | 1000+ | gratis, ontgrendelen buiten winkel | 3 (3.7) |
| 2 | Rest: Body Battery & Stress | Dialforge.dev | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 3 | Stress Meter | Trudelta | veld | 1000+ | gratis, ontgrendelen buiten winkel | 5 (4.8) |
| 4 | Heat Stress+ | Trudelta | veld | 1000+ | gratis, ontgrendelen buiten winkel | 17 (4.6) |
| 5 | Stress Analyzer | Edel | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 2 (5.0) |
| 6 | Stress Pulse | AviSnow | wijzerplaat | 1000+ | gratis | 8 (3.3) |
| 7 | Stress PulseOx | TimeFace | wijzerplaat | 100+ | gratis | 1 (5.0) |
| 8 | Stress lite | TimeFace | wijzerplaat | 100+ | gratis | 0 |
| 9 | Stress Tracker | CelestialFire | app | 10+ | $4.25 | 1 (1.0) |
| 10 | Stress stats | Melentina | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |

**relax** (998 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | RELAX | RiseUp | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 2 | Relax | CzG001 | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 1 (3.0) |
| 3 | Relax | Saraswatches | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 2 (4.5) |
| 4 | Relax | Garmin | wijzerplaat | 100000+ | gratis | 96 (4.1) |
| 5 | Bonsai Relax | Poharoba | wijzerplaat | 100+ | gratis | 0 |
| 6 | Mountain Relax | Poharoba | wijzerplaat | 100+ | gratis | 3 (5.0) |
| 7 | RELAX Collection | wgyfrank | wijzerplaat | 100+ | gratis | 2 (4.0) |
| 8 | Snoopy Relax | GreenPoint | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 16 (4.8) |
| 9 | Relax Time | GreenPoint | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 10 | Nature relax | Melentina | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |

**relaxation** (997 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Relaxation | DmClockFaces | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 2 | Relaxation Feedback Aid | Trudelta | app | 100+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 3 | Progressive Muscle Relaxation (PMR) | Artillis | app | 10+ | $3.49 | 4 (4.0) |
| 4 | Relaxation by the lake | LXTHEMES | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 5 | Stress and relaxation cycles | Eloy_VL | app | 1000+ | gratis | 2 (3.0) |
| 6 | Ebb Calm: Breathing Exercises & Relaxation | Dortus | app | 10+ | gratis | 0 |
| 7 | ZenFlow - Guided Breathing | ZenFlow | app | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 8 | Breath Hold Trainer | jonathan.orsel | app | 100+ | gratis | 0 |
| 9 | Vacation Car | Luks28 | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 10 | MeditatorsPeak | SmartWakePro | app | 1000+ | gratis, ontgrendelen buiten winkel | 10 (1.8) |

**calm** (998 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Calm | Melentina | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |
| 2 | Calm | RiseUp | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 3 | Calm | PhoeniXX | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 4 | Keep Calm | La5or | wijzerplaat | 1000+ | gratis | 2 (5.0) |
| 5 | Calm Analog | CalmAnalog | wijzerplaat | 100+ | gratis | 3 (5.0) |
| 6 | Fuji Calm | digitalrerere | wijzerplaat | 1+ | gratis | 0 |
| 7 | Calm Bloom | Digital-Mainspring | wijzerplaat | 0 | $2.99 | 0 |
| 8 | Alpine Calm | Douglas341 | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 9 | Autumn calm | Awooche | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 10 | Water Calm | RoxyWatch | wijzerplaat | 10+ | gratis | 0 |

**meditation** (997 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Meditation | Bash | app | 100+ | gratis, ontgrendelen buiten winkel | 7 (5.0) |
| 2 | Meditation | Impeltech | app | 1+ | gratis | 0 |
| 3 | Meditation | aimonster | app | 1000+ | gratis, ontgrendelen buiten winkel | 8 (4.3) |
| 4 | Meditation | Awooche | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |
| 5 | Meditation | LuxuryThemes | wijzerplaat | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 6 | Meditation and Breathwork | FlorianGeigl | app | 10000+ | gratis | 150 (4.3) |
| 7 | Pulse Meditation | GarPulse | app | 1+ | gratis | 0 |
| 8 | Coherence Meditation | kuboduby | app | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 9 | Meditation App | Illia | app | 1+ | gratis | 0 |
| 10 | Meditation Buddy | AlanSmithee | veld | 1000+ | gratis | 3 (3.0) |

**freediving** (992 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Frontline Freediving Diver | summersdev | wijzerplaat | 100+ | gratis | 3 (5.0) |
| 2 | Frontline Freediving Analog | summersdev | wijzerplaat | 10+ | gratis | 0 |
| 3 | Frontline Freediving Logo | summersdev | wijzerplaat | 10+ | gratis | 0 |
| 4 | Capnia - Freediving & Spearfishing Training | sqidram | app | 10+ | gratis | 0 |
| 5 | Freediving & Apnea Breathing Trainer | udot_artsem | app | 100+ | gratis | 0 |
| 6 | Frontline Freediving Large Numbers | summersdev | wijzerplaat | 10+ | gratis | 0 |
| 7 | Apnea - Freediving & Spearfishing Watch Face | sqidram | wijzerplaat | 1+ | gratis | 0 |
| 8 | Dive Timer - Freediving Surface Coach | DiveTimer | app | 1000+ | gratis | 6 (4.5) |
| 9 | TRITON PRO: Freediving and Apnea Training | Sauli | app | 1+ | gratis | 1 (5.0) |
| 10 | VzMy with Freedivig | BrunaTom | wijzerplaat | 1000+ | gratis | 41 (4.6) |

**apnea** (162 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Apnea Pace | GreeksAPP | app | 1+ | gratis | 0 |
| 2 | Apnea Tables - CO2 and O2 Hold Training | RiversideArt | app | 0 | $2.99 | 0 |
| 3 | Apnea - Freediving & Spearfishing Watch Face | sqidram | wijzerplaat | 1+ | gratis | 0 |
| 4 | BreathGym - Breath Hold Trainer | ThijsGer | app | 100+ | $1.99 | 7 (4.4) |
| 5 | Freediver - Apnea Training | Freediver | app | 100+ | gratis | 8 (5.0) |
| 6 | Freediver & Mermaid Apnea | WarrenWan | app | 10+ | gratis | 0 |
| 7 | Apnea Static Timer | ApnoeMax | app | 1000+ | gratis | 3 (4.3) |
| 8 | JMG-APP Apnea Training | Surfy66 | app | 10000+ | gratis, ontgrendelen buiten winkel | 82 (4.1) |
| 9 | Apnea Sense - Breath Training | duyngo | app | 10+ | gratis | 1 (5.0) |
| 10 | Dynamic/Static Apnea Trainer | FreedivingPH.com | app | 10+ | gratis | 0 |

**wim hof** (227 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Дыхание Wim Hof | VadimRosh | app | 10+ | gratis | 1 (5.0) |
| 2 | DeepBreath - Wim Hof Breathing and Cold | himanshu.skb | app | 1000+ | gratis | 7 (4.1) |
| 3 | Cold Plunge & Sauna+Wim Hof breathing preparation  | kuboduby | app | 100+ | gratis, ontgrendelen buiten winkel | 3 (4.7) |
| 4 | Breathing Timer: HRV · BOLT · Wim Hof · 4-7-8 | BreathingTimer | app | 1000+ | gratis | 94 (4.5) |
| 5 | Breathwork | No_Try_Hard | app | 1000+ | gratis | 6 (4.3) |
| 6 | Oxygenate+ | NirvanaFlow | app | 100+ | gratis, ontgrendelen buiten winkel | 0 |
| 7 | Breathing Exercises | SimonSteinhuber | app | 1000+ | gratis | 7 (3.3) |
| 8 | Prayer Times Wimbledon  | Kamru | app | 100+ | gratis | 2 (5.0) |
| 9 | Breath and Plunge (WHM style) Lite plus Sauna | WhiteBear | app | 100+ | gratis | 6 (4.3) |
| 10 | Breathwork | Kegles | app | 10+ | $1.99 | 0 |

**breathing exercises** (997 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Breathing Exercises | liamb09 | app | 100+ | gratis | 0 |
| 2 | Breathing Exercises | SimonSteinhuber | app | 1000+ | gratis | 7 (3.3) |
| 3 | Breathe: Breathing Exercises | FikirLtd | app | 1000+ | $2.99 | 19 (4.5) |
| 4 | Ebb Calm: Breathing Exercises & Relaxation | Dortus | app | 10+ | gratis | 0 |
| 5 | Box Breathing | Dialforge.dev | app | 10+ | gratis, ontgrendelen buiten winkel | 0 |
| 6 | Breathing Assistant | Oski3K | app | 10+ | gratis | 1 (5.0) |
| 7 | Office Exercises  | SimonSteinhuber | app | 10+ | gratis | 1 (5.0) |
| 8 | HRV Breathing | Oltek | app | 100+ | $3.99 | 8 (4.9) |
| 9 | Tactical Breathing | g1zmo | app | 100+ | gratis | 4 (5.0) |
| 10 | WHM breathing+ | MobileDriveway | app | 1000+ | $4.99 | 610 (4.9) |

**breath training** (994 treffers)

| # | App | Maker | Soort | Downloads | Prijs | Reviews (cijfer) |
|---|---|---|---|---|---|---|
| 1 | Breath Training | Deyve | app | 10+ | $2.99 | 0 |
| 2 | Breathbeat: Breathwork & Breath Holds | NeronLLC | app | 1+ | $3.99 | 1 (2.0) |
| 3 | Apnea Sense - Breath Training | duyngo | app | 10+ | gratis | 1 (5.0) |
| 4 | BreathGym - Breath Hold Trainer | ThijsGer | app | 100+ | $1.99 | 7 (4.4) |
| 5 | Breath Pacer - Paced Breathing Timer | RiversideArt | app | 10+ | gratis | 0 |
| 6 | Breath | RiseUp | wijzerplaat | 100+ | gratis, ontgrendelen buiten winkel | 0 |
| 7 | Breath Training Tool - CO2, O2, Breath & Dry Apnea | Bitochi | app | 1000+ | gratis | 21 (4.9) |
| 8 | Breath - Guided Breathing, HRV & Breath Holds | wolftronics | app | 10+ | gratis | 0 |
| 9 |  BJJ (Brazilian Jiu-Jitsu) | TheBigGoal | app | 100+ | gratis, ontgrendelen buiten winkel | 1 (5.0) |
| 10 | Ebb Breathing & Breath Hold | Dortus | app | 1+ | $2.99 | 0 |

## 3. Voorstel per app

Volgorde voor de hoofdchat: eerst wijziging 1 (taal), dan de teksten, dan de beelden. Of het aanpassen van tekst of beelden zonder nieuwe versie kan en of het opnieuw gekeurd wordt door Garmin: NIET GEZIEN (GOK: tekst bewerken kan zonder nieuw bestand). Zet geen tekst live voordat een keurder hem goedkeurde.

### 3a. Ebb Breathing & Breath Hold (betaald)

**Taal (wijziging 1, het belangrijkste).** Zorg dat Engels de eerste taal in de lijst wordt. Hoe dat in het formulier van Garmin gaat: NIET GEZIEN. Probeer in deze volgorde: (1) kijk of het formulier een standaardtaal of hoofdtaal heeft en zet die op Engels; (2) zo niet: Frans toevoegen (hieronder), en eventueel Duits en Nederlands weghalen en daarna opnieuw toevoegen, zodat Engels vooraan komt (GOK dat de volgorde de volgorde van toevoegen is: bij Calm stond Engels eerst en bleef het eerst). Controle achteraf, zonder inloggen: `curl -s https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/5280653d-1681-452d-8c03-7cbdc7284641` en kijk welke `locale` als eerste in `appLocalizations` staat; of open `https://apps.garmin.com/es-ES/apps/5280653d-1681-452d-8c03-7cbdc7284641` en kijk of de titel Engels is.

**Titel (Engels): blijft**
```
Ebb Breathing & Breath Hold
```
27 tekens. Reden: deze titel bracht Ebb op breathing van 31 naar 18 en op breath hold van 4 naar 2 (GEZIEN). Een extra woord maakt de titel langer en drukt de andere woorden (GEZIEN bij de vorige titel). "Breathing exercises" laten we aan Calm over (plek 4), die naar Ebb linkt.

**Titel Duits (44 tekens) en Nederlands (43 tekens): nieuw, met Breathwork erbij**
```
Ebb: Breathwork, Atemübungen & Atem anhalten
```
```
Ebb: breathwork, ademhaling & adem inhouden
```
Reden: breathwork is een woord waarop betaalde apps staan (Breathwork $1,99, BREATHWORK $4,49) en waar Ebb op 33 staat. De zoeker leest de titels van alle talen, dus dit geeft een titeltreffer zonder de Engelse titel te verlengen. "Breathwork" wordt in het Duits en Nederlands gewoon gebruikt; onze Duitse en Nederlandse tekst noemen al "Breathwork-Runden" en "Breathwork-rondes". Effect op de plek: GOK, meten na 3 dagen.

**Titel Frans (nieuw, 41 tekens)**
```
Ebb : rétention du souffle et respiration
```

**Eerste twee zinnen (Engels)**
```
Breath hold rounds and calm breathing exercises on your Garmin, drawn as a small sea. Breathe in and the water rises, breathe out and it falls, hold your breath and you go under water; every phase has its own vibration, so you can follow with your eyes closed.
```
Daarna in dezelfde alinea: eenmalig betalen, en de veiligheidsregel (alleen op het land, zittend of liggend, nooit in of bij water, nooit tijdens het rijden). Reden: "breath hold" is ons beste woord en staat nu in de eerste woorden; "breathing exercises" en "eyes closed" zijn de zinnen waarmee Breathe opent; "one payment, no subscription" is wat koper en toppers vooraan zetten.

**Volledige beschrijving Engels (3986 tekens, grens 4.000)**
```
Breath hold rounds and calm breathing exercises on your Garmin, drawn as a small sea. Breathe in and the water rises, breathe out and it falls, hold your breath and you go under water; every phase has its own vibration, so you can follow with your eyes closed. One payment, no subscription. For practice on land only: sit or lie down, never in or near water, never while driving. Hold only while it feels easy.

Want to try the sea first? Ebb Calm is free, with 4-7-8 breathing only: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

BREATH HOLD ROUNDS
• Rounds of deep breaths at a steady pace, then breathe out and hold for as long as feels right.
• Press a button to end the hold, then take one big breath in and hold it briefly to recover.
• While you hold, you are under water with a sea animal. The picture stays the same however long you hold. From 3:00 on the watch shows "breathe" at the top. A hold stops by itself after five minutes; the session then ends and saves. That hold is not averaged.
• Before every session Ebb reminds you: sit or lie down.

CALM BREATHING: 4-7-8 AND MY PATTERN
• 4-7-8: breathe in for 4, hold for 7, out for 8, with the sea rising and falling.
• My pattern: set your own seconds in, hold, out and hold in the settings, for example 4-4-4-4 for box breathing or 5-0-5-0 for slow, even breathing.

COLLECT SEA ANIMALS BY SHOWING UP
• 24 sea animals, earned with sessions and weeks in a row, never by holding longer. A small fish swims with you from your first session.
• Your streak counts weeks in which you reach your weekly goal (3 sessions, or set 2 to 7), so rest days never break it.
• A session counts with at least one hold, or one minute of calm breathing. Up to two sessions a day count.
• New animals appear at the end of a session, one at a time, plus one bonus animal to discover. The Sea log shows your animals and exactly how to get the next one.

SEE YOUR PRACTICE
• After rounds: your hold time for every round and your week. After calm breathing: how long you breathed and your breaths.
• Today: the holds of your sessions today as bars. 8 weeks: your sessions per week and your average hold.

BREATHE WITH YOUR EYES CLOSED
• Every phase has its own vibration. The last three breaths before the hold feel different.
• A soft buzz every 30 seconds while you hold, if you like. Vibration can be turned off. One buzz stays on: every 30 s after 3:00 of holding, for your safety.
• While you breathe and hold, the touchscreen does nothing, so a sleeve cannot stop a hold; only the buttons work. Ebb makes no sound.

SAVED IN GARMIN CONNECT
• Each session is saved as a breathing activity with your heart rate. Rounds: one lap per round with its hold time and breaths. For interest only; Ebb gives no score.
• A finished session saves itself. Calm breathing, and a session left paused, save by themselves after 30 minutes. Press back to pause: resume, save or discard.

SETTINGS ON THE WATCH
Breaths per round, pace, rounds, recovery hold, weekly goal, vibration and My pattern. No phone needed.

ONE PAYMENT, NOTHING COLLECTED
• One payment in the Garmin store. No subscription, no unlock code by e-mail, no extra account, no phone app.
• Ebb collects nothing. Your sessions, animals and settings stay on your watch. Only a saved activity goes to Garmin Connect, under Garmin's privacy policy. No analytics, no ads.

SUPPORT AND REFUNDS
Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days. Refunds follow Garmin's Connect IQ Store policy: a 48-hour return window after you buy.

SAFETY
Sit or lie down. Never practise breath holds in or near water, in the bath, or while driving. Feel dizzy or tingly? Stop and breathe normally. Not if pregnant, under 18, or with epilepsy, heart or blood pressure problems. Ebb has no CO2 or O2 tables and is not a medical device.

Tags: breathing exercises, breathing, breath hold, breathwork, box breathing, breath training, 4-7-8, 478, calm, relaxation
```

Wat is er anders dan nu: nieuwe eerste alinea; de link naar de gratis Calm als tweede alinea (zoals Breathe doet); box breathing 4-4-4-4 en 5-0-5-0 als voorbeeld bij My pattern; tags met breathing exercises, box breathing en calm. Weg om ruimte te maken: de patrijspoort, "Pick the one that swims with you", "Found all 24? Your streak of weeks keeps counting." Alle veiligheidszinnen staan er nog, ook "Before every session Ebb reminds you: sit or lie down", "never by holding longer", de stop na vijf minuten en de tril na 3:00.

**Na te lopen door de keurder:** in de code of het menu van Ebb 1.0.1 of My pattern 4 fases heeft, 4 seconden toestaat en een vasthoudfase van 0 (uit `producten/garmin-adem/ontwerp.md`: 1 tot 12 seconden per fase, vast mag 0; de huidige winkeltekst zegt al "set your own seconds in, hold, out and hold"). Klopt 0 niet, haal dan "or 5-0-5-0 for slow, even breathing" weg.

**Duits en Nederlands: vervang alleen de eerste alinea, zet de link eronder, en pas de tags aan.** De rest van de huidige tekst blijft, met één zin erbij bij My pattern. Volledige nieuwe teksten (Duits 3439 tekens, Nederlands 3367 tekens):

Duits:
```
Atem anhalten in Runden und ruhige Atemübungen auf deiner Garmin, gezeichnet als kleines Meer. Beim Einatmen steigt das Wasser, beim Ausatmen sinkt es, beim Anhalten tauchst du unter; jede Phase hat ihre eigene Vibration, sodass du mit geschlossenen Augen folgen kannst. Einmal zahlen, kein Abo. Nur an Land üben: im Sitzen oder Liegen, nie im oder am Wasser, nie beim Autofahren. Halte den Atem nur an, solange es leicht fällt.

Erst das Meer ausprobieren? Ebb Calm ist kostenlos, nur mit 4-7-8-Atmung: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

• Atemrunden: tiefe Atemzüge in festem Tempo, dann ausatmen und halten, solange es sich gut anfühlt. Ab 3:00 zeigt die Uhr oben "breathe". Nach fünf Minuten endet das Anhalten von selbst: die Uhr geht zur Erholung über, beendet dann die Sitzung und speichert sie. Dieses Anhalten zählt nicht im Durchschnitt. Vor jeder Sitzung, auch bei Calm und My pattern, erinnert Ebb: setz oder leg dich hin.
• Sammle 24 Meerestiere durch Dranbleiben (Sitzungen und Wochen in Folge mit deinem Wochenziel, standardmäßig 3 Sitzungen, einstellbar 2 bis 7; Ruhetage unterbrechen die Serie nie), nie durch längeres Halten. Pro Tag zählen bis zu zwei Sitzungen. Neue Tiere kommen am Ende einer Sitzung, dazu ein Bonustier. Alle 24 gefunden: dein Meer ist komplett, deine Wochenserie zählt weiter.
• Calm 4-7-8: 4 ein, 7 halten, 8 aus. My pattern: eigene Sekunden in den Einstellungen, zum Beispiel 4-4-4-4 für Box-Atmung. Eine Sitzung zählt ab einem Anhalten oder einer Minute Calm.
• Nach Atemrunden deine Haltezeit pro Runde, nach Calm deine Dauer und Atemzüge; beim ersten kompletten Meer stattdessen ein Festbild mit allen 24 Tieren. Jederzeit im Menü: heute deine Sitzungen als Balken (bis drei) und über 8 Wochen Sitzungen pro Woche und deine durchschnittliche Haltezeit.
• Eigene Vibration für jede Phase, auch mit geschlossenen Augen; beim Halten auf Wunsch alle 30 Sekunden ein sanftes Vibrieren. Die Vibration lässt sich abschalten. Ein Signal bleibt an: alle 30 Sekunden ab 3:00 Anhalten, zu deiner Sicherheit. Beim Atmen und Halten reagiert der Touchscreen nicht; im Pausenmenü kannst du tippen. Ebb macht keinen Ton.
• Wird als Atemaktivität mit Herzfrequenz in Garmin Connect gespeichert; bei Atemrunden ein Lap pro Runde mit Haltezeit und Atemzügen, nur zur Info, ohne Bewertung. Eine fertige Sitzung speichert sich selbst, Calm und eine pausierte Sitzung nach 30 Minuten ebenfalls; Zurück-Taste für Pause: weiter, speichern oder verwerfen.
• Einmal zahlen. Kein Abo, kein Code per E-Mail, kein zusätzliches Konto, keine Handy-App.
• Datenschutz: Ebb sammelt nichts. Sitzungen, Tiere und Einstellungen bleiben auf der Uhr; nur eine gespeicherte Aktivität geht an Garmin Connect (Datenschutzerklärung von Garmin). Keine Analyse, keine Werbung.
• Support: thijs@dortus.com, mit deinem Uhrenmodell. Wir antworten möglichst innerhalb von 5 Werktagen. Erstattungen folgen den Regeln des Garmin Connect IQ Store: Garmin gibt dir nach dem Kauf 48 Stunden Rückgabefrist.

Die App ist auf Englisch. Keine CO2-Tabellen, kein Medizinprodukt. Sicherheit: im Sitzen oder Liegen. Nie im oder am Wasser, nie in der Badewanne, nie beim Autofahren. Schwindelig oder Kribbeln? Aufhören und normal atmen. Nicht bei Schwangerschaft, unter 18, bei Epilepsie, Herz- oder Blutdruckproblemen.

Tags: Atemübungen, Atemtraining, Atem anhalten, Box-Atmung, 4-7-8, 478, Entspannung, Atmung, breathing
```

Nederlands:
```
Rondes met adem inhouden en rustige ademhalingsoefeningen op je Garmin, getekend als een kleine zee. Adem in en het water stijgt, adem uit en het zakt, houd je adem in en je gaat onder water; elke fase heeft een eigen trilling, zodat je met je ogen dicht kunt volgen. Eén keer betalen, geen abonnement. Alleen op het droge: zittend of liggend, nooit in of bij water, nooit achter het stuur. Houd alleen in zolang het makkelijk gaat.

Eerst de zee proberen? Ebb Calm is gratis, alleen met 4-7-8-ademen: https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

• Ademrondes: diepe ademhalingen in een vast tempo, dan uitademen en inhouden zolang het goed voelt. Vanaf 3:00 toont het horloge bovenaan "breathe". Na vijf minuten stopt het inhouden vanzelf: het horloge gaat door naar herstel, sluit dan de sessie af en slaat hem op. Die inhouding telt niet mee in je gemiddelde. Voor elke sessie, ook Calm en My pattern, zegt Ebb: ga zitten of liggen.
• Verzamel 24 zeedieren door vol te houden (sessies en weken op rij met je weekdoel, standaard 3 sessies, in te stellen van 2 tot 7; rustdagen breken je reeks nooit), nooit door langer in te houden. Per dag tellen hoogstens twee sessies. Nieuwe dieren komen aan het eind van een sessie, plus één bonusdier. Alle 24 gevonden: je zee is compleet en je reeks in weken telt door.
• Calm 4-7-8: 4 in, 7 vasthouden, 8 uit. My pattern: eigen seconden in de instellingen, bijvoorbeeld 4-4-4-4 voor box breathing. Een sessie telt vanaf één inhoud of één minuut Calm.
• Na ademrondes je inhoudtijd per ronde, na Calm je duur en ademhalingen; de eerste keer dat je zee compleet is krijg je in plaats daarvan een feestscherm met alle 24 dieren. Altijd in het menu: vandaag je sessies als staven (tot drie) en over 8 weken sessies per week en je gemiddelde inhoudtijd.
• Eigen trilling per fase, ook met je ogen dicht; tijdens inhouden als je wilt elke 30 seconden een zachte tril. Trillen kun je uitzetten. Eén tril blijft aan: elke 30 seconden na 3:00 inhouden, voor je veiligheid. Tijdens ademen en inhouden doet het aanraakscherm niets; in het pauzemenu kun je tikken. Ebb maakt geen geluid.
• Opgeslagen als ademactiviteit met hartslag in Garmin Connect; bij ademrondes één lap per ronde met inhoudtijd en ademhalingen, alleen ter info, zonder score. Een afgeronde sessie slaat zichzelf op, Calm en een sessie in pauze doen dat na 30 minuten ook; terugknop voor pauze: doorgaan, opslaan of weggooien.
• Eén keer betalen. Geen abonnement, geen code per mail, geen extra account, geen telefoonapp.
• Privacy: Ebb verzamelt niets. Sessies, dieren en instellingen blijven op je horloge; alleen een opgeslagen activiteit gaat naar Garmin Connect (privacybeleid van Garmin). Geen tracking, geen advertenties.
• Support: thijs@dortus.com, met je horlogemodel. We proberen binnen 5 werkdagen te antwoorden. Terugbetalen volgt de regels van de Garmin Connect IQ Store: Garmin geeft je na je aankoop 48 uur om terug te geven.

De app is in het Engels. Geen CO2-tabellen, geen medisch hulpmiddel. Veiligheid: zittend of liggend. Nooit in of bij water, nooit in bad, nooit achter het stuur. Duizelig of tintelingen? Stop en adem gewoon. Niet als je zwanger bent, onder de 18, of bij epilepsie, hart- of bloeddrukproblemen.

Tags: ademhalingsoefeningen, ademhaling, adem inhouden, box breathing, 4-7-8, 478, ontspanning, breathing
```

**Frans (nieuw, 3588 tekens).** Korter dan het Engels, maar met alle functies en alle veiligheidszinnen, en met "L'application est en anglais" (Garmin vraagt beperkingen te noemen; de app zelf is Engels). Laat een Fransman of een keurder met goed Frans er eerst naar kijken.
```
Des cycles de rétention du souffle et des exercices de respiration calmes sur votre Garmin, dessinés comme une petite mer. L'eau monte quand vous inspirez, descend quand vous expirez, et quand vous retenez votre souffle, vous passez sous l'eau ; chaque phase a sa propre vibration, pour suivre les yeux fermés. Un seul paiement, sans abonnement. Uniquement sur la terre ferme : assis ou allongé, jamais dans l'eau ou près de l'eau, jamais en conduisant. Ne retenez votre souffle que tant que c'est facile.

Envie d'essayer la mer d'abord ? Ebb Calm est gratuit, avec seulement la respiration 4-7-8 : https://apps.garmin.com/apps/bcc58192-667b-4bd8-a824-e6fe26794466

L'application est en anglais.

CYCLES DE RÉTENTION
• Des cycles de respirations profondes à un rythme régulier, puis vous expirez et retenez votre souffle aussi longtemps que c'est agréable.
• Un bouton termine la rétention, puis une grande inspiration que vous tenez brièvement pour récupérer.
• Pendant la rétention, vous êtes sous l'eau avec un animal marin. L'image reste la même, quelle que soit la durée. À partir de 3:00, la montre affiche « breathe » en haut. Une rétention s'arrête d'elle-même après cinq minutes ; la séance se termine alors et s'enregistre.
• Avant chaque séance, Ebb vous rappelle : asseyez-vous ou allongez-vous.

RESPIRATION CALME : 4-7-8 ET MY PATTERN
• 4-7-8 : inspirez 4 secondes, retenez 7, expirez 8, avec la mer qui monte et descend.
• My pattern : réglez vous-même les secondes d'inspiration, de pause, d'expiration et de pause, par exemple 4-4-4-4 pour la respiration carrée ou 5-0-5-0 pour une respiration lente et régulière.

DES ANIMAUX MARINS EN REVENANT
• 24 animaux marins, gagnés par vos séances et vos semaines d'affilée, jamais en retenant plus longtemps.
• Votre série compte les semaines où vous atteignez votre objectif (3 séances, ou de 2 à 7) : les jours de repos ne la cassent jamais.
• Le Sea log montre vos animaux et comment obtenir le suivant.

VOTRE PRATIQUE
• Après les cycles : votre temps de rétention par cycle et votre semaine. Today et 8 weeks : vos séances du jour et par semaine.
• Chaque séance est enregistrée dans Garmin Connect comme activité de respiration, avec votre fréquence cardiaque ; un tour par cycle. À titre indicatif, sans score.

LES YEUX FERMÉS
• Chaque phase a sa propre vibration. Les vibrations peuvent être coupées, sauf une : toutes les 30 s après 3:00 de rétention, pour votre sécurité.
• Pendant la séance, l'écran tactile ne fait rien : seuls les boutons fonctionnent. Ebb ne fait aucun son.

UN SEUL PAIEMENT, RIEN N'EST COLLECTÉ
• Un paiement dans la boutique Garmin. Pas d'abonnement, pas de code, pas de compte, pas d'app sur le téléphone.
• Ebb ne collecte rien. Vos données restent sur la montre ; seule une activité enregistrée va vers Garmin Connect, selon la politique de confidentialité de Garmin.

ASSISTANCE ET REMBOURSEMENT
Écrivez à thijs@dortus.com (en anglais) avec le modèle de votre montre. Nous visons une réponse sous 5 jours ouvrés. Remboursements selon la politique du Connect IQ Store de Garmin : 48 heures après l'achat.

SÉCURITÉ
Assis ou allongé. Ne pratiquez jamais la rétention dans l'eau ou près de l'eau, dans le bain, ni en conduisant. Vertiges ou fourmillements ? Arrêtez et respirez normalement. Pas en cas de grossesse, avant 18 ans, ni en cas d'épilepsie, de problèmes cardiaques ou de tension. Ebb n'a pas de tables CO2 ou O2 et n'est pas un dispositif médical.

Tags : respiration, exercices de respiration, rétention du souffle, souffle, respiration carrée, 4-7-8, 478, relaxation, breathing
```

**Schermafbeeldingen: volgorde (alle vijf blijven)**
1. `3`: "Hold. The sea closes over." (hold 1:45). Reden: wie op breath hold zoekt (onze plek 2), ziet meteen inhouden.
2. `1`: "Breathe. Make sea friends." met "One payment, no subscription, no extra account". Reden: sterkste beeld en de prijsvorm.
3. `2`: "Breathe with the sea."
4. `5`: "Fill your sea log."
5. `4`: "Come back. Meet a crab."
(Nummers zijn de huidige volgorde in de winkel. Ebb heeft ook een video; of die vóór de beelden staat: NIET GEZIEN in een browser.)

**Nieuwe beelden die het meest helpen (in volgorde):**
1. **Eén beeld "wat zit erin"** in plaats van `4` (de krab, die overlapt met de sea log): "Breath hold rounds, 4-7-8, My pattern (box 4-4-4-4), 24 sea animals, saved to Garmin Connect, one payment". Reden: de verkoper op $2,99 met 1000+ (Breathe) noemt op elk beeld één feit; onze vijf beelden zeggen sfeer, niet wat je koopt.
2. **Garmin Connect**: een echte activiteit met een ronde per inhouding en de hartslag. Reden: WHM breathing+ verkoopt op de extra gegevens in Garmin Connect. Alleen maken met een echte opname van een echt horloge; zonder echt horloge niet (niet verzinnen).

### 3b. Ebb Calm: Breathing Exercises & Relaxation (gratis)

**Titel Engels: blijft** `Ebb Calm: Breathing Exercises & Relaxation` (42 tekens). Calm staat op breathing exercises op 4, relaxation 6, 478 op 3 en (alleen apps) calm op 1 (GEZIEN). Ik heb overwogen "4-7-8" in de Engelse titel te zetten, maar dat zijn drie woorden erbij (de zoeker knipt op het streepje) en dan zakt Calm waarschijnlijk op zijn beste woorden (GOK, zelfde werking als bij Ebb). Wie "4-7-8" met streepjes typt, krijgt toch 0 treffers.

**Titel Duits: blijft** `Ebb Calm: Atemübungen & Entspannung` (35 tekens).

**Titel Nederlands: nieuw (45 tekens)**
```
Ebb Calm: ademhalingsoefeningen & ontspanning
```
Reden: Calm staat nu niet in de eerste 90 bij ademhaling en ademhalingsoefeningen (Ebb wel op 1); "ademoefeningen" is minder gangbaar (GOK).

**Titel Frans: nieuw (42 tekens)**
```
Ebb Calm : respiration 4-7-8 et relaxation
```
Reden: hier mag 4-7-8 wel in de titel, want het maakt de Engelse titel niet langer; het geeft een titeltreffer op "4 7 8" en op "respiration" (GOK dat een Franse titel even zwaar telt; bij Duits en Nederlands is dat GEZIEN).

**Eerste twee zinnen en de link (Engels).** De link naar Ebb staat al live als tweede alinea. Voorstel: "breathing exercises" in de eerste zin, en box breathing in de linkzin, want wie op box breathing zoekt, vindt Calm (plek 52) maar Calm heeft dat niet; de volle Ebb wel via My pattern.
```
Free 4-7-8 breathing exercises on your Garmin, drawn as a small sea. Breathe in for 4, hold for 7, out for 8: the water rises as you breathe in and falls as you breathe out, and every phase has its own vibration, so you can follow with your eyes closed. A simple breathing exercise for relaxation, to wind down in a calm moment. Sit or lie down while you practise.

Want more? The full Ebb, a separate paid app, adds breath hold rounds, your own breathing pattern (such as box breathing 4-4-4-4) and 24 sea animals to collect: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```

**Volledige beschrijving Engels (2251 tekens)**: de huidige tekst met deze twee alinea's vooraan en deze tags. De alinea "THE FULL EBB" verderop blijft.
```
Free 4-7-8 breathing exercises on your Garmin, drawn as a small sea. Breathe in for 4, hold for 7, out for 8: the water rises as you breathe in and falls as you breathe out, and every phase has its own vibration, so you can follow with your eyes closed. A simple breathing exercise for relaxation, to wind down in a calm moment. Sit or lie down while you practise.

Want more? The full Ebb, a separate paid app, adds breath hold rounds, your own breathing pattern (such as box breathing 4-4-4-4) and 24 sea animals to collect: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641

CALM 4-7-8 BREATHING
• Breathe in for 4 seconds, hold for 7, breathe out for 8. The watch counts every phase down.
• Your round watch face becomes a small sea. The water rises and falls with your breath, and a small fish keeps you company.
• Breathe as long as you like. Press back to pause: resume, save or discard.

BREATHE WITH YOUR EYES CLOSED
• In, hold and out each have their own vibration. Vibration can be turned off in the settings.
• While you breathe, the touchscreen does nothing, so a sleeve cannot stop your session; only the buttons work. Ebb Calm makes no sound.

SAVED IN GARMIN CONNECT
• Save a session and it becomes a breathing activity in Garmin Connect, with your heart rate.
• A session that keeps running saves itself after 30 minutes, and so does a session left paused.

FREE AND PRIVATE
• Free. No account, no subscription, no unlock code, no phone app, no ads.
• Ebb Calm collects nothing. Your settings stay on your watch. Only a saved activity goes to Garmin Connect, under Garmin's privacy policy. No analytics.

THE FULL EBB
Ebb Calm is the calm part of Ebb. The full Ebb, a separate paid app in this store, adds breath hold rounds, your own breathing pattern and 24 sea animals to collect.

SUPPORT
Mail thijs@dortus.com with your watch model. We aim to reply within 5 working days.

SAFETY
Sit or lie down. Never practise in or near water, in the bath, or while driving. Feel dizzy or tingly? Stop and breathe normally. Not if pregnant, under 18, or with epilepsy, heart or blood pressure problems. Ebb Calm is not a medical device.

Tags: breathing exercises, breathing, relaxation, calm, 4-7-8, 478, breathwork, wind down
```

**Duits (2600 tekens) en Nederlands (2360 tekens): alleen de linkzin vervangen** (Nederlands ook de eerste woorden "Gratis 4-7-8-ademhaling" en de tags):
```
Mehr gewünscht? Das ganze Ebb, eine eigene kostenpflichtige App, bietet zusätzlich Runden mit Atemanhalten, dein eigenes Atemmuster (zum Beispiel Box-Atmung 4-4-4-4) und 24 Meerestiere zum Sammeln: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```
```
Meer willen? De volle Ebb, een aparte betaalde app, heeft daarnaast rondes met adem inhouden, je eigen adempatroon (bijvoorbeeld box breathing 4-4-4-4) en 24 zeedieren om te verzamelen: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```
```
Tags: ademhalingsoefeningen, ademhaling, ademen, ontspanning, rustig, 4-7-8, 478, breathing
```

**Frans (nieuw, 2333 tekens)**
```
Respiration 4-7-8 gratuite sur votre Garmin, dessinée comme une petite mer. Inspirez 4 secondes, retenez 7, expirez 8 : l'eau monte quand vous inspirez et descend quand vous expirez, et chaque phase a sa propre vibration, pour suivre les yeux fermés. Un exercice de respiration simple pour se détendre dans un moment calme. Asseyez-vous ou allongez-vous pendant l'exercice.

Envie de plus ? L'Ebb complet, une app payante à part, ajoute des cycles de rétention du souffle, votre propre rythme (par exemple la respiration carrée 4-4-4-4) et 24 animaux marins à collectionner : https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641

L'application est en anglais.

RESPIRATION 4-7-8
• Inspirez 4 secondes, retenez 7, expirez 8. La montre décompte chaque phase.
• L'écran rond devient une petite mer. L'eau monte et descend avec votre souffle, et un petit poisson vous tient compagnie.
• Respirez aussi longtemps que vous voulez. Le bouton retour met en pause : reprendre, enregistrer ou supprimer.

LES YEUX FERMÉS
• Inspiration, pause et expiration ont chacune leur vibration. Les vibrations peuvent être coupées dans les réglages.
• Pendant la séance, l'écran tactile ne fait rien : seuls les boutons fonctionnent. Ebb Calm ne fait aucun son.

ENREGISTRÉ DANS GARMIN CONNECT
• Enregistrez une séance et elle devient une activité de respiration dans Garmin Connect, avec votre fréquence cardiaque.
• Une séance qui continue, ou laissée en pause, s'enregistre d'elle-même après 30 minutes.

GRATUIT ET PRIVÉ
• Gratuit. Pas de compte, pas d'abonnement, pas de code, pas d'app sur le téléphone, pas de publicité.
• Ebb Calm ne collecte rien. Vos réglages restent sur la montre ; seule une activité enregistrée va vers Garmin Connect, selon la politique de confidentialité de Garmin.

ASSISTANCE
Écrivez à thijs@dortus.com (en anglais) avec le modèle de votre montre. Nous visons une réponse sous 5 jours ouvrés.

SÉCURITÉ
Asseyez-vous ou allongez-vous. Ne pratiquez jamais dans l'eau ou près de l'eau, dans le bain, ni en conduisant. Vertiges ou fourmillements ? Arrêtez et respirez normalement. Pas en cas de grossesse, avant 18 ans, ni en cas d'épilepsie, de problèmes cardiaques ou de tension. Ebb Calm n'est pas un dispositif médical.

Tags : respiration, exercices de respiration, relaxation, calme, 4-7-8, 478, breathing
```

**Schermafbeeldingen: volgorde**
1. `1`: "Breathe in. The sea rises." (4-7-8 in één zin).
2. `5`: "Free. One button." Reden: "gratis" is voor een gratis app het sterkste woord en staat nu achteraan.
3. `2`: "Sit down. Close your eyes."
4. `3`: "A few calm minutes." (toont in de app al "The full Ebb adds breath hold rounds and 24 sea animals").
5. Nieuw beeld in plaats van `4` (pauzescherm, het zwakste): "Want more? The full Ebb, a separate paid app: breath hold rounds and 24 sea animals", met het hold-scherm van Ebb. Reden: Calm heeft 10+ downloads en Ebb 1+ (GEZIEN); de beelden van Calm worden vaker gezien dan de tekst onderaan. "Separate paid app" moet erop staan (Garmin: geen "bait-and-switch").

### 3c. Gloop's Hat Tower (gratis)

Live sinds 17 nov, 10+ downloads, 0 reviews, gratis (GEZIEN). Plekken (GEZIEN): gloop 1, one button game 3, stacking game 4, one button 13, hat 31, tower 39, stack 84, game en arcade niet in de eerste 90.
- **Titel blijft** `Gloop's Hat Tower: One-Button Stacking Game` (43 tekens): hij staat al hoog op de twee woorden die precies beschrijven wat het is. Op "game" staan Snake Game ($1,99, 1000+) en Maze Game (50000+); daar winnen we niet met een titel.
- **Tekst en beelden blijven.** Talen staan goed (Engels eerst, GEZIEN).
- Klein idee, weinig waard: een regel "More from Dortus: Ebb Calm, free breathing on your watch" met link. Alleen als de keurder het de moeite vindt; de spelers zoeken een spel, geen ademapp.
- Opvallend (geen voorstel, de prijs is een keuze van Thijs): het best lopende stapelspel, Stack van MangoIQ, kost $1,99 en heeft 10000+ downloads en 86 reviews (GEZIEN). Betaalde spellen verkopen dus wel.

## 4. Doorverwijzen van Ebb Calm (gratis) naar Ebb (betaald)

- **In de winkeltekst mag het, en het staat er al.** De App Review Guidelines van Garmin (laatst bijgewerkt 13 okt 2021, GEZIEN via `developer.garmin.com/connect-iq/articles/app-review-guidelines/Overview.html`) verbieden geen link naar je eigen app. Ze vragen wel: eerlijk beschrijven (4a), zeggen of iets geld kost en geen "bait-and-switch" (4d: niet doen alsof iets gratis is als het dat niet is), en geen spam of reclame die vooral naar een website stuurt (1a). Voorbeeld dat goedgekeurd is: Breathe en Breathe Free linken met een winkeladres naar elkaar (GEZIEN).
- **Calm heeft de link al** (live, tweede alinea, sinds 1.0.1). De winkelpagina maakt adressen in de tekst klikbaar met een linkify-script (GEZIEN in de code van de pagina; niet in een browser gezien).
- **Voorgestelde zin (Engels, vervangt de huidige linkzin):**
```
Want more? The full Ebb, a separate paid app, adds breath hold rounds, your own breathing pattern (such as box breathing 4-4-4-4) and 24 sea animals to collect: https://apps.garmin.com/apps/5280653d-1681-452d-8c03-7cbdc7284641
```
- **De andere kant op is nieuw:** Ebb krijgt een link naar de gratis Calm ("Want to try the sea first?"). Wie twijfelt over $2,99, kan eerst gratis voelen hoe het werkt; Breathe doet hetzelfde.
- **In de app (alleen idee, niet bouwen):**
  - Het eindscherm van Calm zegt al "The full Ebb adds breath hold rounds and 24 sea animals" (GEZIEN op winkelbeeld 3).
  - Een knop die de winkel opent kan niet: met `System.exitTo` kan een app alleen een andere app openen die **al op het horloge staat**; anders volgt `AppNotInstalledException` (Garmin-uitleg "Intents", GEZIEN). Een infoscherm "More: Ebb" in het menu van Calm kan wel; Garmin verbiedt dat niet, mits er staat dat Ebb apart betaald wordt (Guidelines 4d).
  - Reviews vragen kan vanuit de app met `WatchUi.makeReviewTokenRequest()` en `WatchUi.startUserReview()`, vanaf API 4.2.0; de winkel bepaalt of het mag, zodat niemand te vaak gevraagd wordt (Garmin-uitleg "Requesting Reviews", GEZIEN). Ebb en Calm hebben 0 reviews (GEZIEN); voor de koper telt een cijfer naast de prijs (GOK). Idee voor een volgende versie, na een ja van de hoofdchat.

## 5. Prijs

**Betaalde apps over adem, ontspanning en stress (GEZIEN, prijs uit de details, gesorteerd op downloads):**

| App | Maker | Prijs | Downloads | Reviews |
|---|---|---|---|---|
| WHM breathing+ | MobileDriveway | $4,99 | 1000+ | 610 |
| Breathe: Breathing Exercises | FikirLtd | $2,99 | 1000+ | 19 |
| HRV Breathing | Oltek | $3,99 | 100+ | 8 |
| BreathGym - Breath Hold Trainer | ThijsGer | $1,99 | 100+ | 7 |
| Vagal - HRV breathing coach | ThijsGer | $1,99 | 100+ | 4 |
| Progressive Muscle Relaxation (PMR) | Artillis | $3,49 | 10+ | 4 |
| BREATHWORK | Sticreations | $4,49 | 10+ | 3 |
| Deep Calm Breathing | Deyve | $2,75 | 10+ | 2 |
| Stress Tracker | CelestialFire | $4,25 | 10+ | 1 |
| Breath Training | Deyve | $2,99 | 10+ | 0 |
| Breathwork | Kegles | $1,99 | 10+ | 0 |
| Kids Breathing - with Resonant Breathing Pet | Oltek | $4,49 | 1+ | 1 |
| Breathbeat: Breathwork & Breath Holds | NeronLLC | $3,99 | 1+ | 1 |
| **Ebb Breathing & Breath Hold** | **Dortus** | **$2,99** | **1+** | **0** |
| Box Breathing: Tactical | Oltek | $2,49 | 1+ | 0 |
| Vytera Breath | VyteraLabs | $4,99 | 0 | 0 |
| Apnea Tables - CO2 and O2 Hold Training | RiversideArt | $2,99 | 0 | 0 |

Mediaan $2,99 (17 apps, GEZIEN). De europrijs van Ebb is €3,49 (DERDEN: opdracht van Thijs en `status.md`; de API gaf mij alleen dollars).

**Advies: $2,99 / €3,49 houden.** Redenen:
- Het is precies de middenprijs, en dezelfde prijs als Breathe, de enige nieuwe betaalde ademapp met 1000+ (GEZIEN).
- Goedkoper verkoopt niet aantoonbaar beter: de vier apps van $1,99 halen hoogstens 100+, net als HRV Breathing op $3,99 (GEZIEN).
- De twee best verkopende betaalde apps hebben een gratis broertje dat kopers aanvoert en veel reviews (WHM+ 610). Daar zit het verschil, niet in de prijs (GOK op oorzaak, het patroon is GEZIEN).
- Bij 1 koper zegt een prijsproef niets. Eerst de drie wijzigingen, dan meten op 1 dec (besluit 19 nov: begin december meten).
- Later te overwegen, alleen met een ja van Thijs: een korte actie. De API kent een veld `salePrice` naast `listPrice` (GEZIEN); of het formulier van Garmin acties toestaat: NIET GEZIEN.

## 6. Meten na de wijziging

Zelfde manier als hierboven: de zoek-API, eerste 90, meest relevant, alle soorten. Meet 3 dagen na het live zetten de plekken van Ebb en Calm op breathing, breath hold, breathwork, breathing exercises, box breathing, 478, relaxation, calm, atem, ademhaling, ademhalingsoefeningen, respiration en souffle, en de downloads van beide. Zakt Calm op breathing exercises onder 10, of Ebb op breath hold onder 5, zet dan die titel terug.

## Bronnen

- Winkel-API (GEZIEN, 20 nov 2026): zoeken `https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/keywords?...`, details `.../api/asw/apps/<id>`, beelden `.../api/screenshots/<id>`.
- Code van de winkelpagina (GEZIEN): `https://apps.garmin.com/_next/static/chunks/pages/search-b91140ac7e5f0b33.js`, `.../pages/_app-0e2c735a1a779095.js`, `.../pages/apps/%5Baid%5D-cc4f5f4c00c6cb65.js`, `.../761-271330e7b3f2c70f.js` (taalkeuze en downloadklasse), `.../369-3ad784cbf3f9a9f9.js` (linkify).
- Garmin, App Review Guidelines (DERDEN): https://developer.garmin.com/connect-iq/app-review-guidelines/
- Garmin, Intents, Requesting Reviews, Publishing to the Store (DERDEN): https://developer.garmin.com/connect-iq/core-topics/intents/ , https://developer.garmin.com/connect-iq/core-topics/requesting-reviews/ , https://developer.garmin.com/connect-iq/core-topics/publishing-to-the-store/
- Eigen eerdere metingen: `platformen/garmin/meting-ebb-calm.md`, `meting-ebb.md`, `onderzoek-winkeltekst-2026-11-10.md`. Huidige plakteksten: `platformen/garmin/upload/`.
