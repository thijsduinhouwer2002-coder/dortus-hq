# Onderzoek 5 kandidaat-niches voor een betaalde Connect IQ app (9 nov 2026)

Onderzoeker voor Gijs. Werktijd ongeveer 18 minuten.

Labels: **GEZIEN** = zelf gelezen in de dataset `garmin-niet-wijzerplaten-2026-11-09.json.gz`, in de open Garmin API (appdetails of reviews) of op de site van de maker. **DERDEN** = uit een bron van iemand anders. **GOK** = eigen kennis of schatting, niet nagekeken in deze ronde.

Belangrijke kanttekeningen vooraf:
- Zoeken op het web via curl werkte niet (DuckDuckGo blokkeert, Bing negeert zoekopdrachten, Garmin-handleidingen en de Connect IQ-docs worden met JavaScript geladen). Daardoor zijn de punten c) en d) **GOK** (eigen kennis), aangevuld met wat gebruikers zelf in reviews schrijven (GEZIEN). Dit moet iemand met een browser nog nakijken.
- De reviews-API gebruikt `startPageIndex` als *beginpositie* (offset), niet als paginanummer. Wie de API later gebruikt: 0, 30, 60 enzovoort.
- "Betaald" in de dataset (veld `pay`/`paymentModel`) betekent niet altijd dat je meteen betaalt. Bijna alle betaalde apps werken met proefperiode en een code via de site van de maker.
- Reviews 2025-2026 zijn volledig opgehaald, behalve bij Sauna Timer (alleen de nieuwste 150, terug tot 20-08-2026).

---

## 1. Sauna en ijsbad

### a) Top apps
| App | Maker | Emmer | Cijfer | Reviews | Betaald | Prijs | Eerste goedkeuring |
|---|---|---|---|---|---|---|---|
| Sauna Timer | peterdedecker | 10.000+ | 4,8 | 592 | nee | gratis | 2024-11-12 |
| Plunge & Sauna | aimonster | 10.000+ | 3,7 | 204 | ja | $3,49 eenmalig na 14 dagen proef (GEZIEN, beschrijving); reviews noemen nu een jaarbedrag (GEZIEN, review 2026-08-10) | 2023-02-24 |
| Sauna tracker PRO | Stanislav.Bures | 10.000+ | 3,7 | 125 | nee in winkel | onbekend | 2023-01-23 |
| GoPolar | TheWellnessCompany | 1.000+ | 4,2 | 122 | nee in winkel | horloge-app gratis, extra's via betaalde telefoonapp (GEZIEN, reviews) | 2025-02-21 |
| Sauna Session PRO | Dialforge.dev | 100+ | 4,8 | 62 | ja | €6,49 eenmalig na 30 dagen proef (GEZIEN, dialforge.dev/apps/saunapro) | 2026-09-21 |

Alle cijfers in de tabel: GEZIEN (dataset), prijzen zoals aangegeven.

### b) Reviews 2025-2026
- **Plunge & Sauna (betaald nr. 1):** 78 reviews, 13 keer 1 ster, 3 keer 2 sterren, gemiddeld 4,0 (GEZIEN).
  1. Opnieuw moeten betalen of licentie kwijt: "Says lifetime when i purchased now after 6 months its prompting to pay again."
  2. Te duur voor alleen een timer: "$4.22 for an app that just tells you how long you are in the icebath ... a bit overpriced"
  3. Sauna en ijsbad niet in één sessie, en kleine gebreken (max 99 graden, Strava toont "Workout"): "Needs the option to have sauna & ice bath in the one activity"
- **Sauna Timer (grootste gratis):** van de nieuwste 150 reviews 1 keer 1 ster en 3 keer 2 sterren, gemiddeld 4,77 (GEZIEN). Klachten: batterij blijft leeglopen na de sessie ("continue draining my battery after the session"), activiteit wordt niet opgeslagen, horloge blokkeert daarna.
- GoPolar: 12 keer 1 ster, 8 keer 2 sterren op 122 (GEZIEN). Klachten: alleen een timer zonder abonnement, crashes, kleine letters met natte handen, geen wisselen tussen sauna en koude in één activiteit, en een waarschuwing dat horloges maar tot ongeveer 45 graden gemaakt zijn.

### c) Doet Garmin dit zelf?
Geen eigen sauna- of ijsbadactiviteit bekend op Garmin-horloges (GOK). Gebruikers loggen nu als "yoga" of "cardio" (GEZIEN, review Plunge & Sauna 2025-01-19). Let op het hitterisico: een review waarschuwt dat horloges tot ongeveer 45 graden gemaakt zijn (GEZIEN, review GoPolar).

### d) Simulator
Goed te testen: het is een timer met hartslag en eventueel temperatuur. De simulator kan hartslag en sensordata nabootsen (GOK). Alleen de echte batterij en de hitte kun je niet testen.

### e) Oordeel
De betaalde nummer één is zwak in vertrouwen (licentie kwijt, prijs verhoogd naar een jaarbedrag) en mist een sessie waarin je sauna en koude afwisselt. Er is ruimte voor een mooi product (rondes sauna/koude/rust in één activiteit, grote cijfers, goede Connect-velden, Strava-naam), maar de gratis Sauna Timer is sterk (4,8) en Dialforge zit er net met €6,49, dus het moet echt beter zijn dan "een timer".

---

## 2. Alcohol- en cafeïne-logboek

### a) Top apps
| App | Maker | Emmer | Cijfer | Reviews | Betaald | Prijs | Eerste goedkeuring |
|---|---|---|---|---|---|---|---|
| Caffeine Tracker | OndrejBozek | 10.000+ | 4,6 | 111 | ja (freemium) | gratis, eenmalige Premium, bedrag niet in beschrijving | 2025-12-01 |
| AlcoTracker [LEGACY] | RoboleoApps | 1.000+ | 4,8 | 107 | ja | alleen voor kopers van voor 2025 | 2022-12-05 |
| BeerWatch | necc | 10.000+ | 3,2 | 53 | nee | gratis (datapunt, bier verbrand tijdens sport) | 2025-06-03 |
| AlcoTracker | RoboleoApps | 1.000+ | 4,2 | 48 | nee in winkel | reviews zeggen dat ze betaald hebben (GEZIEN) | 2024-12-30 |
| Alcogram | OndrejBozek | 1.000+ | 3,8 | 23 | ja (freemium) | Premium unlock, bedrag niet gevonden | 2026-06-02 |

Alle cijfers GEZIEN (dataset en beschrijving).

### b) Reviews 2025-2026
- **Caffeine Tracker (betaald nr. 1):** 111 reviews, 2 keer 1 ster, 1 keer 2 sterren, gemiddeld 4,65 (GEZIEN). Klachten zijn er weinig:
  1. Ingewikkeld: "Way too complicated and not intuitive at all."
  2. Betalen via code is gedoe: "I really have to type the device code from my watch to buy premium? Immediately lost interest"
  3. Traag en tekst valt weg: "extremly unresponsive. For every click, there's a second delay on F8 Pro."
- **BeerWatch (grootste gratis):** 53 reviews, 19 keer 1 ster, 1 keer 2 sterren (GEZIEN). Bijna alles is "werkt niet op mijn horloge": "Just shows a iq logo when trying to use on 255". Het is een ander soort app (datapunt).
- AlcoTracker: vaste Amerikaanse maten in oz, geen ml: "needs the ability to change the units from US to other stuff such as ml!" (GEZIEN).

### c) Doet Garmin dit zelf?
Garmin Connect heeft "Lifestyle Logging" in de telefoonapp, waarin je o.a. alcohol en cafeïne per dag kunt aanvinken en naast slaap en HRV ziet (GOK, eigen kennis, nakijken op support.garmin.com). Dat is op de telefoon, niet als teller met milligram op het horloge. Hydratatie loggen kan Garmin wel zelf (GOK).

### d) Simulator
Volledig te testen: alleen invoer, rekenen en een glance. Geen sensor nodig (GOK).

### e) Oordeel
Caffeine Tracker is níet zwak (4,65, weinig klachten, zelfde maker als Alcogram), dus cafeïne is bezet. Bij alcohol zijn de spelers rommelig (oz-only, codes die niet werken), maar het is een gevoelig onderwerp met een klein publiek; geen goede plek voor een duur, opvallend product.

---

## 3. CrossFit / WOD / HIIT

### a) Top apps
| App | Maker | Emmer | Cijfer | Reviews | Betaald | Prijs | Eerste goedkeuring |
|---|---|---|---|---|---|---|---|
| Tabata | Efflon | 100.000+ | 4,3 | 147 | nee | gratis, donatie | 2016-05-18 |
| HIIT Tracker | werkkrew | 50.000+ | 3,4 | 216 | nee | gratis, open source | 2017-06-09 |
| HIIT Timer (App) | GDCSoft | 10.000+ | 4,5 | 46 | ja | $2,49 eenmalig, eerste training gratis (GEZIEN) | 2020-04-21 |
| WodBuddy: Crossfit & Hyrox | wodbuddy.app | 1.000+ | 3,6 | 39 | extern abonnement | bedrag niet gevonden | 2025-05-05 |
| HIIT & WOD Timer (EMOM) | PenguinCode | 1.000+ | 4,4 | 14 | freemium | AMRAP en For Time gratis, Premium eenmalig (GEZIEN), bedrag niet gevonden | 2025-12-29 |

Ter info: ROXZONE (Hyrox, ChanDigital, betaald, 10.000+, 4,7, 312 reviews, 2026-03-19) is in deze buurt de echte winnaar (GEZIEN). Let op: WodBuddy is in de winkel niet "betaald" maar vraagt een extern abonnement (GEZIEN, extsub).

### b) Reviews 2025-2026
- **WodBuddy (betaalde/abonnement nr. 1 voor CrossFit):** 39 reviews, 9 keer 1 ster, 1 keer 2 sterren (GEZIEN).
  1. Koppelen telefoon en horloge lukt niet: "my watch doesn't sync with the app also if is a compatible model (Garmin Venu2)"
  2. Inloggen werkt niet: "Makes problems while signing in. Doesn't work"
  3. Stopt of scherm wordt zwart, reps tellen werkt niet: "the rep count doesn't work at all"
- HIIT Timer (App) (betaald in de winkel): maar 6 reviews in 2025-2026, 0 keer 1 ster, 1 keer 2 sterren (GEZIEN); de app is weinig in beeld.
- **Tabata (grootste gratis):** 11 reviews, 2 keer 1 ster, 1 keer 2 sterren (GEZIEN). Klachten: crasht op Fenix 8, rekent totale tijd fout, minimum rust 2 seconden.

### c) Doet Garmin dit zelf?
**Ja, en goed.** Nieuwere Garmin-horloges (fenix 7 en later, Forerunner 255/265/955/965/970, Venu 3 en later, epix) hebben een eigen HIIT-activiteit met de vormen AMRAP, EMOM, Tabata, Custom en vrij, plus HIIT-trainingen met oefeningen in de Garmin Connect app (GOK, eigen kennis, nakijken in de handleiding van de fenix 8 of Forerunner 965, hoofdstuk "HIIT"). Een gewone timer-app verliest daarvan.

### d) Simulator
Timers zijn goed te testen in de simulator. Herhalingen tellen via de versnellingsmeter niet echt (GOK).

### e) Oordeel
De nummer één (WodBuddy) is zwak, maar Garmin doet de timers zelf al goed en Hyrox is al in handen van ROXZONE (4,7). Alleen een app die echt de WOD van de box binnenhaalt, zou kans maken, en dat vraagt een server en een telefoonapp; niet geschikt als snel, mooi product.

---

## 4. Springtouw

### a) Top apps
| App | Maker | Emmer | Cijfer | Reviews | Betaald | Prijs | Eerste goedkeuring |
|---|---|---|---|---|---|---|---|
| Jump Rope | **Garmin** | 100.000+ | 2,7 | 365 | nee | gratis | 2022-06-05 |
| JumpJump Pro | li2niu | 1.000+ | 3,6 | 51 | ja | $5 eenmalig (GEZIEN, beschrijving); 2 proeftrainingen (GEZIEN, review) | 2022-03-09 |
| JumpJump Pro (CIQ Store versie) | li2niu | 100+ | 3,0 | 2 | nee in lijst | onbekend | 2025-02-03 |
| Jump Rope Coach Pro | KeepFit | 10+ | 5,0 | 2 | nee | onbekend | onbekend |

Alle cijfers GEZIEN (dataset). Er is dus nauwelijks concurrentie buiten Garmin zelf.

### b) Reviews 2025-2026
- **JumpJump Pro (betaald nr. 1):** 14 reviews, 7 keer 1 ster, 1 keer 2 sterren, gemiddeld 2,36 (GEZIEN).
  1. Licentie komt niet of gaat niet mee naar nieuw horloge: "I purchased on March 1st, paid via PayPal and still don't have the activation key."
  2. Telt verkeerd: "I count 100 and watches count 84."
  3. Geen antwoord van de maker: "Still waiting for developer to move licence for me."
- **Jump Rope van Garmin (grootste gratis):** 107 reviews, 33 keer 1 ster, 18 keer 2 sterren, gemiddeld 2,87 (GEZIEN).
  1. Slaat op als "Cardio" in plaats van "Springtouw", data weg en geen badges: "the app is incorrectly saving the activity as cardio instead of jump rope"
  2. Tellen onnauwkeurig: "You jump 50 times, the app says 27."
  3. Geen rondes met tijd en rust: "if it had timed rounds it would be better. Example: 2 minute round with 1 minute rest."
  Plus crashes/herstarten na een update in feb 2025.

### c) Doet Garmin dit zelf?
Deels. Garmin maakt zelf de gratis app "Jump Rope" (GEZIEN, maker Garmin) en die is slecht beoordeeld. Een gebruiker schrijft dat een Venu 3 springtouw wel als eigen activiteit kan opslaan (GEZIEN, review 2025-04-11), dus op sommige nieuwe modellen zit een eigen springtouwactiviteit met tellen (GOK, nakijken in de Venu 3/vivoactive 6 handleiding). Ook via een HIIT-training met oefening "springtouw" (GEZIEN, review 2026-04-18).

### d) Simulator
Dit is het zwakke punt. Springtouw tellen vraagt ruwe versnellingsmeterdata (Toybox.Sensor, registerSensorDataListener, 25 tot 100 Hz). De simulator kan die niet realistisch nabootsen; je hebt een echt horloge nodig om het tellen af te stellen (GOK). Een Connect IQ-app kan ook geen activiteit als "springtouw" opslaan als het horloge dat sporttype niet kent (GOK), dus het "cardio"-probleem los je niet zomaar op.

### e) Oordeel
De markt is zwak (Garmin 2,87 en JumpJump 2,36, beide met boze reviews) en er is veel vraag (100.000+). Maar goed tellen kun je zonder echt horloge niet bouwen of testen, dus dit kan alleen als Thijs een horloge en een touw inzet; dan is $4 tot $6 met rondes, betrouwbaar tellen en reps in Connect best haalbaar.

---

## 5. Bloeddruk-logboek

### a) Top apps
| App | Maker | Emmer | Cijfer | Reviews | Betaald | Prijs | Eerste goedkeuring |
|---|---|---|---|---|---|---|---|
| BP Ready | ElmarBraun | 1.000+ | 3,8 | 12 | nee in winkel, wel betaald | $3,49 (GEZIEN, review 2026-07-30) | 2026-07-20 |
| Blood Pressure Journal | TheBigGoal | 1.000+ | 3,4 | 5 | ja | $3,99 eenmalig na 7 dagen proef (GEZIEN) | 2026-05-28 |
| Blood Pressure Log | Dialforge.dev | 100+ | 4,0 | 4 | ja | €4,99 eenmalig na 30 dagen (GEZIEN) | 2026-10-14 |
| BP Diary Lite / BP Diary | Salgarm | 100+ / 10+ | 5,0 / 3,0 | 2 / 2 | nee | onbekend | 2026-10-14 |

Alle cijfers GEZIEN. Opvallend: alle apps zijn van 2026 en er zijn er al 6, ook van Dialforge en drie dezelfde dag.

### b) Reviews 2025-2026
- **Blood Pressure Journal (betaald nr. 1):** 5 reviews, 1 keer 1 ster, 0 keer 2 sterren (GEZIEN). Klacht: geen koppeling met Garmin Connect: "It's strange that the data isn't syncing with Garmin Connect. It has its own blood pressure recording system there."
- **BP Ready (grootste, in winkel gratis):** 12 reviews, 3 keer 1 ster, 1 keer 2 sterren (GEZIEN).
  1. Invoer onhandig, standaard 120/80 per ongeluk opgeslagen: "Ehe man sich versieht hat man den Standartwert 120/80 gespeichert"
  2. Betaald maar werkt niet: "I paid for it, but it doesn't work"
  3. Mensen denken dat het horloge bloeddruk meet: "No mide la presión arterial"

### c) Doet Garmin dit zelf?
Ja, op de telefoon: Garmin Connect heeft een eigen bloeddrukregistratie (handmatig of via de Index BPM-meter) (GEZIEN, review die dat zegt; GOK verder). Een Connect IQ-app kan daar niet in schrijven (GOK), en dat is precies de grootste klacht.

### d) Simulator
Volledig te testen, alleen invoer en grafiek (GOK).

### e) Oordeel
De nummer één is zwak, maar het publiek is klein (hooguit 1.000+), het veld raakt in 2026 snel vol en het kernprobleem (geen koppeling met Garmin Connect) kun je als app niet oplossen. Geen plek voor een duur, uniek product.

---

## Samenvatting en rangorde (oordeel onderzoeker)
1. **Sauna en ijsbad:** beste mix van vraag (twee apps 10.000+), zwakke betaalde leider, Garmin doet het zelf niet, volledig te testen in de simulator. Risico: sterke gratis Sauna Timer en Dialforge (€6,49) zit er net.
2. **Springtouw:** zwakste concurrentie en meeste vraag, maar niet te bouwen zonder echt horloge.
3. **CrossFit/WOD:** Garmin doet de timers zelf goed; afraden.
4. **Bloeddruk:** klein en snel vol; afraden.
5. **Cafeïne/alcohol:** cafeïne is goed bezet (4,65); afraden.

Ruwe data staat in de kladmap van deze sessie (niet in de repo).
