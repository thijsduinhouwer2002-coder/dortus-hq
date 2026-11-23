# Push-Up Hero (Strafe) en de Goals-wijzerplaten van VAW.BE: een app die zichzelf op de grootste wijzerplaat van de winkel krijgt (23 nov 2026)

Afkijker, run 23 nov ±18:30 NL. Alles gelezen met `curl` (winkel-API van Garmin, Reddit-archief arctic-shift, vaw.be, uitleg van Garmin). Niets geplaatst, niemand benaderd.

## Wat we letterlijk kunnen nadoen

1. **Ebb publiceert een "complication" (een getal dat wijzerplaten kunnen tonen): ademminuten vandaag en deze week.** Push-Up Hero doet dat met push-ups, Atmos Air Quality (plek 2 Top Paid) zegt letterlijk "This app publishes complications for use in watch faces". Wie: Dortus (een Garmin-bouwer, de hoofdchat wijst aan). Kosten $0. Kan vanaf API 4.2.0.
2. **Vraag Wim Van Aerschot (VAW.BE) om Ebb op te nemen in zijn Goals-wijzerplaten**, zoals hij Push-Up Hero, Hydration PRO, Time To Pray, Tides en CGM Connect noemt met "requires external app" en "More coming with every update". Goals: 100.000+ downloads en 32.535 reviews, Goals 8: 100.000+ en 20.318. Wie: Chris schrijft de tekst, Daan keurt, verstuurd via het Contact Developer-formulier van het ontwikkelaarsaccount van Thijs (dus zijn ja). Kosten $0.
3. **Eén regel in de winkeltekst van Ebb:** "Shows your breathing minutes on compatible watch faces", met de namen erbij zodra een wijzerplaat het toont. Wie: Chris, Daan keurt, de hoofdchat plakt. $0.
4. **Klaar vóór ±15 december.** Push-Up Hero kreeg in december en januari 90 en 93 reviews, tegen 33 tot 80 (meestal 50 tot 60) in de andere maanden van 2026 (GEZIEN, tabel hieronder): nieuwe horloges onder de kerstboom en goede voornemens.
5. **Verwacht effect (GOK):** als Goals Ebb noemt, zien elke maand duizenden Goals-gebruikers de naam Ebb in een lijst met "requires external app"; bij 1 op 1.000 die het koopt zijn dat 10 tot 30 kopers per maand à $2,99 (GOK op de verhouding, niet gemeten). Zonder ja van Wim blijft punt 1 alleen nuttig voor wijzerplaten waar de gebruiker zelf velden kiest (klein effect, GOK).

**Niet doen:** een klassement op adem inhouden (wie houdt het langst vol). Dat is de kern van Push-Up Hero, maar bij adem inhouden is het gevaarlijk, en Garmin verbiedt freediving en het woord apnea (keuring Daan 22 nov). Een klassement op ademminuten of reeksen kan later, als een eigen bouwstap met een server; nu niet.

---

## Bewijs

### Push-Up Hero, de app (GEZIEN, winkel-API, https://apps.garmin.com/apps/787e795f-2426-4e41-b172-9a197d5f0f68)
- Maker "Strafe" (geen trustedDeveloper). $1,99, geen proef (`hasTrialMode false`), **10.000+ downloads, 969 reviews, 4,3 sterren**, versie v1.7.4, 176 horlogetypes, 14 talen (en, fr, cs, de, es, nl, pt_BR, nb, sv, pl, it, ru, zh_CN, zh_TW). Plek 4 in Top Paid Apps (GEZIEN, https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/apps/calculatedCategories/topPaidApps?startPageIndex=0&pageSize=30).
- Eerste zin: "Push-Up challenges! Track your progress and compete with friends." Klassement wereldwijd, of een besloten groep: je kiest een naam en deelt die met vrienden.
- In de tekst: "Use compatiable watch faces to see push-up complication data (streaks, weekly totals, etc.) on your watch face. See several of Wim's watchfaces such as Stride II" met link. Stride II is van VAW.BE (GEZIEN, `/apps/898c1596-5e4f-4e02-a25a-6150ac010230`, 1.000+, 412 reviews). Het werkt dus twee kanten op: Strafe stuurt naar Wim, Wim noemt Strafe.
- Wat er nieuw is per versie staat volledig in "What's new" (v1.1.0 tot v1.7.4); v1.4.0 "Adds reminders, streaks, custom goals, and complications!", v1.7.0 voegde 13 talen toe.

### Reviews per maand (GEZIEN, alle 969 via `/apps/787e795f-.../reviews?startPageIndex=N&pageSize=30`)
| maand | reviews | maand | reviews |
|---|---|---|---|
| 2025-03 | 10 (eerste: 9 mrt, v1.1.0) | 2026-01 | **93** |
| 2025-04 | 11 | 2026-02 | 50 |
| 2025-05 | 22 | 2026-03 | 52 |
| 2025-06 | 19 | 2026-04 | 55 |
| 2025-07 | 50 | 2026-05 | 67 |
| 2025-08 | 37 | 2026-06 | 80 |
| 2025-09 | 26 | 2026-07 | 48 |
| 2025-10 | 33 | 2026-08 | 58 |
| 2025-11 | 56 | 2026-09 | 53 |
| 2025-12 | **90** | 2026-10 | 33 |
|  |  | 2026-11 (tot 23e) | 26 |

- Sterren: 658 keer 5, 121 keer 4, 76 keer 3, 37 keer 2, 77 keer 1. 781 van de 969 zonder tekst (normaal in deze winkel: bij Atmos, WHM breathing+ en Plank Hero 26 tot 28 van de nieuwste 30 ook zonder tekst, GEZIEN), dus dit wijst niet op een reviewknop in de app.
- **De maker antwoordt op 40 reviews, bijna allemaal op 1 tot 3 sterren, in de taal van de schrijver** (Pools, Duits, Arabisch, Koreaans), met een concrete oplossing ("try calibrating your stance in the settings menu") en "contact the developer". Bij één review ging de koper terug naar 5 sterren na een fix ("Rating back to five stars now that the weekly and monthly league tables have reset properly - thanks dev").
- Waar de klachten over gaan: tellen ("count" 62 keer, "accura" 28 keer). Over het klassement 5 keer.

### De reeks van dezelfde maker (GEZIEN, `/apps/developer/788e10b4-7ecf-4aec-9d24-30cf4abecbfe`)
31 apps. Na Push-Up Hero dezelfde app voor andere oefeningen, elk $1,99: Sit-Up Hero 1.000+ (46 reviews), Plank Hero 1.000+ (55), Pull-Up Hero 1.000+ (45), Squat Hero 100+ (30). Verder spellen: Chess! - Free 10.000+ (934), Checkers! 10.000+ (652, gratis), Chess! $3,99 1.000+ (63), en EasyUV gratis 1.000+ (440).

### Goals van VAW.BE noemt de apps van anderen (GEZIEN)
- Goals (`/apps/c4d24b8d-ecc2-4436-b14e-ce75b462e425`): $1,99, **100.000+ downloads, 32.535 reviews**. In de tekst: "Hydration tracking via Hydration PRO", "Rain", "Air Quality (AQI)", "Continuous Glucose Monitoring ... via CGM Connect", "Electricity Spot Price", "Hourly Steps", "Time To Pray", "Push Up Hero: Push Ups today, this week", "Tides", telkens met "requires external app", en dan "... More coming with every update". Daarna: "If you have any questions, don't hesitate to ask ... Just use the Contact Developer form to reach me. I'll try to respond within 24 hours!"
- Goals 8 (`/apps/62451616-8744-48ee-a972-8e2f4a604279`): 100.000+, 20.318 reviews, noemt alle vijf Hero-apps. Goals Pro 10.000+ (917), Goals Pro with trial 1.000+ (788), Goals 9 1.000+ (418): allemaal Push-Up Hero erin.
- Hydration PRO, Rain en Goals zijn van Wim zelf; Push-Up Hero, CGM Connect, Time To Pray en Tides lijken van anderen (Push-Up Hero GEZIEN van Strafe; de rest GOK, niet nagekeken).
- vaw.be: "I'm Wim Van Aerschot and this is my hobby project! I create apps and clocks for Fitbit, Garmin & Pebble" (GEZIEN, https://vaw.be/watch/?brand=garmin&app=goals). Dus één maker, net als wij.
- Atmos Air Quality (plek 2 Top Paid, 10.000+, 1.089 reviews): "-- This app publishes complications for use in watch faces" (GEZIEN, `/apps/b9a3f779-5272-4b44-bc21-7ba1c65fa5e9`).

### Garmin zelf
- Complications bestaan sinds API Level 4.2.0 (GEZIEN, https://developer.garmin.com/connect-iq/api-docs/Toybox/Complications.html). Onze eigen notitie: kant-en-klare velden op de nieuwere horloges, niet op Forerunner 55, 245 en Instinct 2 (`platformen/garmin/reeks.md`).

### Reddit
- r/Garmin, 19 nov 2025: "Who is PNN on Garmin's pushup hero?", een zoon die met zijn vader het klassement volgt (GEZIEN, https://arctic-shift.photon-reddit.com/api/posts/ids?ids=1p10kwm, score 0, 1 reactie). Klein, maar laat zien dat het klassement gesprek geeft. Geen posts van de maker zelf gevonden; geen YouTube, geen site in de winkelpagina.

### Tijdlijn: hoe kwam hij aan zijn eerste kopers (deels GOK)
1. Mrt 2025: Push-Up Hero live, 10 tot 22 reviews per maand (GEZIEN).
2. Jul 2025: sprong naar 50 reviews (v1.3.x). Oorzaak niet te zien; GOK: opgenomen in Top Paid of in Goals.
3. v1.4.0 (najaar 2025, GOK op de datum): complications, reeksen, herinneringen. Daarna staat hij in Goals en Goals 8 (wanneer precies niet te zien).
4. Dec 2025 en jan 2026: 90 en 93 reviews, het hoogste (GEZIEN).
5. Daarna de reeks (Sit-Up, Plank, Pull-Up, Squat), die ook in Goals 8 kwam.
Hoe hij aan de eerste 100 kwam is niet openbaar: geen forumdraad, geen Reddit-post, geen video gevonden. Wat wel te zien is: de winkel zelf (Top Paid) en de wijzerplaten van Wim.

### Wat Ebb al heeft
Ebb houdt sessies bij met de schermen Today en 8 weeks (`producten/garmin-adem/ontwerp.md`), dus "minuten vandaag" en "sessies deze week" bestaan al in de app. Het getal hoeft alleen naar buiten.
