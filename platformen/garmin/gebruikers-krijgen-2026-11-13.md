# Ebb: hoe komen we aan gebruikers en kopers? (onderzoek, 12 nov 2026, voor 13 nov)

Onderzoeker voor Gijs en de hoofdchat. Werktijd ongeveer 60 minuten. Alles alleen gelezen: nergens ingelogd, niets geplaatst.
Labels: **GEZIEN** = zelf gelezen in de bron (datum erbij). **AFGELEID** = berekend uit wat ik zag. **GOK** = eigen inschatting.
Alle webpagina's gelezen met curl op 12 nov 2026, tenzij anders vermeld. Winkelcijfers komen uit de open winkel-API (`https://apps.garmin.com/api/appsLibraryExternalServices/api/asw/...`) en uit de dataset `platformen/verkenner/data/garmin-nieuw-sinds-jun2025-2026-11-06.json` (opgehaald 6 nov 2026, 27.935 nieuwe apps sinds juni 2025).

## Samenvatting (voor Thijs)

1. **Verwachting, eerlijk:** de eerste maand waarschijnlijk 5 tot 30 kopers ($20 tot $130 netto), na 90 dagen 20 tot 120. Meer dan 100 in de eerste maand is mogelijk maar zeldzaam. Van de nieuwe betaalde horloge-apps van $3,99 en duurder had in de eerste 45 dagen géén enkele 100+ downloads; 20 van de 31 zaten op 1 tot 9 (AFGELEID uit de dataset).
2. **Wat het meest oplevert, nummer 1:** een gratis broertje, "Ebb Free" (versie 1.1). Alle drie de best lopende betaalde ademapps hebben er een (WHM breathing: 50.000+ gratis tegen 1.000+ betaald). Garmin's eigen betaalsysteem kent geen proefperiode, alleen 48 uur geld terug.
3. **Nummer 2:** de eerste 10 tot 25 echte beoordelingen snel binnenhalen, eerlijk. Nieuwe apps met rond de 20 tot 25 beoordelingen staan in de lijsten "Trending" en "Hot & Fresh" (GEZIEN); daar kijken gewone kopers.
4. **Nummer 3:** één eerlijk bericht als maker op r/Garmin (als de regels het toelaten) en een draad in Connect IQ Showcase, op dag 1, met een schermafbeelding.
5. **Prijs:** houd $4,99. Prijs is niet het probleem, gevonden worden wel. Geen lanceringskorting.
6. **Wat Thijs zelf doet:** twee berichten plaatsen (30 min), tien mensen persoonlijk vragen of ze Ebb willen proberen (30 min), elke dag reacties en beoordelingen lezen en kort antwoorden (10 min per dag). Samen ongeveer 4 uur in twee weken (zie het plan).
7. **Wat ik niet kon nagaan:** de regels van de subreddits (Reddit blokkeert), echte verkoopcijfers van ademapps (Garmin toont alleen emmers als 100+ of 1.000+), en hoe de winkel precies rangschikt (Garmin zegt het nergens).

---

## 1. Hoe vinden mensen een app in de winkel?

**De plekken in de winkel (GEZIEN, 12 nov):**
- De winkelpagina en de Connect IQ-app op de telefoon tonen lijsten met de namen `store_category_trending`, `store_category_mostPopular`, `store_category_hotFresh` en `store_category_newAndUpdated` (in de pagina `https://apps.garmin.com/en-US/`, gelezen met curl). De code van de winkel kent de sorteringen `mostRelevant`, `mostRecent`, `highestRated`, `mostPopular`, `trending` en `hotFresh` (bestand `/_next/static/chunks/pages/_app-7923089b5b613838.js`).
- Er zijn ook vaste lijsten (`/api/asw/calculatedCategories`): "Top Paid Watch Faces", **"Top Paid Apps"** en "Disney Digital Watch Faces" (GEZIEN).
- Zoeken: de winkel zoekt in titel en beschrijving, in alle talen tegelijk, vaag (fuzzy). Titeltreffers staan boven teksttreffers, en downloads of beoordelingen tellen bij "meest relevant" weinig (GEZIEN 10 nov, `platformen/garmin/onderzoek-winkeltekst-2026-11-10.md`). Onze titel `Ebb: Breathing, Breath Hold Rounds & 4-7-8` is dus het belangrijkste dat we al goed hebben.
- Bovenaan de startpagina staat een "featured app"-carrousel die Garmin zelf vult uit de hero-afbeelding van apps (GEZIEN, Garmin-bericht van 7 jun 2019, `https://forums.garmin.com/developer/connect-iq/b/news-announcements/posts/we-want-you-to-feel-seen`). Garmin vroeg toen: hero-afbeeldingen met naam en slagzin, liefst vertaald, en "reach out to us through the forums". Of dat in 2026 nog zo werkt: GOK.

**Wat staat er nu in die lijsten? (GEZIEN, API 12 nov, horloge-apps):**
- **Trending:** vooral grote namen (Maps4Garmin, komoot, Google Maps, WhatsApp), maar ook twee apps van deze maand: Atmos Marine Weather (goedgekeurd 3 nov, 100+ downloads, 20 beoordelingen) en Neon Rush (6 nov, 22 beoordelingen).
- **Hot & Fresh:** maar 7 horloge-apps, alle 2 tot 5 maanden oud, met 25 tot 238 beoordelingen (Crossy Road 3D, Atmos Weather, Wallet, CarFinder, Flight Scanner Pro, Tesla Key Pro, ZigZag). Vijf van de zeven zijn betaald.
- **Top Paid Apps:** plaats 1 tot 31 zijn apps met echte verkoop (WHM breathing+ staat op 18 met 1.000+ en 607 beoordelingen; plaats 27 is Tesla Key Pro met maar 100+ en 25 beoordelingen). Vanaf plaats 32 staan alleen nieuwe betaalde apps met 0 of 1 download (GEZIEN). AFGELEID: de drempel om in de bovenste 30 betaalde apps te komen ligt laag, rond een paar honderd kopers in totaal of een paar per dag.
- **Most Recent:** zit vol met apps die net een update kregen, ook oude (GEZIEN; makers klagen er ook over, zie hieronder).

**Wat bepaalt de volgorde? Garmin zegt het nergens.** Wat makers erover schrijven:
- "Where an app is shown within a category depends on different things, like rating, downloads, views. There is no way to 'nominate' an app" en "When searching, you'll only see maybe the first 100-150 apps" (jim_m_58, ervaren maker, draad van ongeveer 28 okt 2026, `https://forums.garmin.com/developer/connect-iq/f/connect-iq-web-store/446898/how-do-apps-get-into-the-connect-iq-store-s-home-page-collections`, GEZIEN).
- Volgens dezelfde maker telt Garmin ook "views" mee (mensen die de pagina bekijken, ook via sociale media) sinds makers klaagden dat alleen grote apps zichtbaar waren. Een andere maker vraagt om bewijs; Garmin heeft het nooit gepubliceerd (zelfde draad, GEZIEN).
- "New and Fresh is meant for new apps. If I recall, apps will only show there for 4 months after they were first published, but rankings are involved" (jim_m_58, ruim 2 jaar geleden, `https://forums.garmin.com/developer/connect-iq/f/discussion/383267/how-to-get-promoted-on-the-connectiq-recommended-section`, GEZIEN). Past bij wat ik in Hot & Fresh zag: alleen apps tot 5 maanden.
- De lijst "Recent" wordt bespeeld met kleine updates; nieuwe apps raken daardoor snel ondergesneeuwd (`https://forums.garmin.com/developer/connect-iq/f/connect-iq-web-store/446033/...`, ongeveer okt 2026, GEZIEN).
- VAW.BE (succesvolle maker) denkt dat hij in Trending kwam door een vermelding in een Garmin-nieuwsbrief, een artikel "Best Garmin watch faces" op Android Authority en betaalde advertenties (Meta, Reddit, Google) (ruim 4 jaar geleden, `https://forums.garmin.com/developer/connect-iq/f/discussion/295143/trending-application-on-connect-iq`, GEZIEN).
- Een maker die uitgelicht werd: "5x more downloads in two weeks than the previous nine months" (GdcSoft, 2020, `https://forums.garmin.com/developer/connect-iq/f/discussion/234215/...`, GEZIEN).

**Wat dit voor ons betekent (AFGELEID/GOK):** zoeken op "breathing" en "breath hold" is onze vaste bron, en die hebben we met de titel goed gedaan. De lijsten Trending en Hot & Fresh zijn de kans op meer; daar lijken nieuwe apps te komen die in korte tijd veel installs, bezoeken en beoordelingen krijgen. Dat bereik je alleen met verkeer van buiten (berichten) en beoordelingen.

## 2. Wat is realistisch voor een nieuwe betaalde app van een onbekende maker?

**Harde cijfers uit de winkel (GEZIEN in de dataset van 6 nov; AFGELEID door mij geteld).** Nieuwe horloge-apps met een winkelprijs, naar leeftijd (downloademmer: "1" betekent 1 tot 9, "10" betekent 10 tot 99, enzovoort):

| Leeftijd | aantal apps | 0 | 1 tot 9 | 10 tot 99 | 100 tot 999 | 1.000+ |
|---|---|---|---|---|---|---|
| 0 tot 45 dagen, alle prijzen | 225 | 65 | 112 | 22 | 26 | 0 |
| 0 tot 45 dagen, $3,99 en duurder | 31 | 9 | 20 | 2 | 0 | 0 |
| 45 tot 120 dagen, $3,99 en duurder | 21 | 1 | 8 | 6 | 6 | 0 |
| 120 tot 600 dagen, $3,99 en duurder | 37 | 1 | 6 | 11 | 14 | 5 |

Daar zitten ook veel snel in elkaar gezette apps tussen (appfabrieken); een verzorgde app doet het waarschijnlijk beter dan de mediaan (GOK). Een eerder onderzoek vond hetzelfde beeld: een nieuwe betaalde app haalt in 1 tot 2 maanden in ongeveer 9% van de gevallen 100+, na 3 tot 6 maanden ongeveer 31% (`platformen/garmin/onderzoek-thijsger-2026-11-10.md`).

**Betaalde ademapps (GEZIEN, API 12 nov):**

| App | Prijs | Sinds | Downloads | Beoordelingen | Beoordelingen per maand |
|---|---|---|---|---|---|
| WHM breathing+ | $4,99 | dec 2024 | 1.000+ | 607 | 18 tot 38, al vanaf januari 2025 (27 in de eerste volle maand) |
| Breathe: Breathing Exercises (FikirLtd) | $2,99 | 17 mrt 2026 | 1.000+ | 18 | mrt 3, apr 5, daarna 1 tot 4 |
| Breath Training System PRO (Bitochi) | $6,25 | 22 apr 2026 | 100+ | 34 | 2 tot 9 |
| HRV Breathing (Oltek) | $3,99 | 20 jan 2026 | 100+ | 8 | ongeveer 1 |
| BreathGym (ThijsGer) | $1,99 | 17 jul 2026 | 100+ | 7 | (appfabriek, niet als bewijs gebruiken) |
| Vytera Breath | $4,99 | 23 okt 2026 | 0 | 0 | 0 |
| ApneaFlow PRO | $5,25 | 26 okt 2026 | 1 tot 9 | 0 | 0 |

Elk van de drie sterkste heeft een gratis broertje: WHM breathing (gratis, 50.000+, 1.730 beoordelingen, met in de tekst "!!! PLUS version of the app !!!" en een link), Breathe Free (Box Breathing, link onderaan de betaalde tekst) en Breath Training Tool van Bitochi (gratis, 1.000+, 21 beoordelingen) (GEZIEN).

**Verhalen van makers (GEZIEN):**
- **Ski Pin** (datapunt, eerst $3,99, later $4,99), forumdraad "I Monetized My Ski App, Here's What Happened", begin 2026: januari 68 verkocht, februari 107, maart 70 ($258,94 uitbetaald), daarna "dropped like a rock" buiten het seizoen. Prijs naar $4,99 in juli: "$3.99 and $4.99 both feel like '5 bucks'", verkoop bleef doorgaan. Zijn les: "don't be afraid to price your app at what it's worth" (`https://forums.garmin.com/developer/connect-iq/f/showcase/430838/i-monetized-my-ski-app-here-s-what-happened`). AFGELEID: Ski Pin stond in de dataset van 9 nov op 100+ met 5 beoordelingen, terwijl hij minstens 245 keer verkocht is. Dus ongeveer **1 beoordeling per 50 kopers**, en de emmer "100+" kan honderden kopers verbergen.
- In dezelfde draad: "I have one paid app, with a unique feature set, and it has zero purchases" (maker van Edge-apps) en "Likely, you'll never get paid enough for your time. Even with paid apps."
- Een oudere maker: "(much) less than a third of people who download the app even start it" en "Charging for an initial release does not attract users!" (draad 234215, zie boven).
- Betalen is een drempel: alleen met een creditcard in Garmin's betaalsysteem; een Nederlandse maker schrijft dat veel Nederlanders hun kaart er niet in krijgen (draad "Connect IQ Monetization System vs own payment system", ongeveer dec 2025, `https://forums.garmin.com/developer/connect-iq/f/discussion/426202/...`). AFGELEID: richt de berichten vooral op Engelstaligen en Duitsers, niet op Nederland.

**Rekensom per koper (GEZIEN, `https://developer.garmin.com/connect-iq/articles/monetization/App_Sales.html`):** Garmin houdt 15% van de prijs zonder btw; Garmin betaalt de kaartkosten. Van $4,99 blijft ongeveer **$4,24** over, min wisselkosten. Uitbetaling op de 1e van de maand, vanaf $10, pas na de 48 uur bedenktijd. Het jaargeld van $100 (genoemd in de Ski Pin-draad) is terug na ongeveer 24 kopers (AFGELEID).

**Drie schattingen voor Ebb** (aanname: Ebb wordt goedgekeurd rond 15 nov, zonder gratis versie in de eerste weken, met twee berichten van Thijs en zonder advertenties):

| | eerste 30 dagen | eerste 90 dagen | aanname |
|---|---|---|---|
| Voorzichtig | 3 tot 8 kopers | 10 tot 25 | berichten slaan niet aan, alleen zoekverkeer; zoals de meeste nieuwe $3,99+-apps (1 tot 9 in 45 dagen) |
| Gewoon | 15 tot 30 | 50 tot 120 | één bericht slaat redelijk aan, 3 tot 6 beoordelingen; tempo tussen HRV Breathing en Breathe in |
| Goed | 60 tot 120 | 200 tot 400 | een bericht gaat rond of we komen in Hot & Fresh of Top Paid; tempo als Ski Pin of Breathe in hun beste maand |

Netto dus voorzichtig $15 tot $35 in een maand, gewoon $65 tot $130, goed $250 tot $500 (AFGELEID, $4,24 per koper). **Eerlijk: de cijfers zijn dun.** Garmin toont alleen emmers, één maker deelde echte verkoop, en de verhouding beoordelingen tot kopers (1 op 20 tot 1 op 50) is een schatting uit twee apps. Ik gok dat "gewoon" het meest waarschijnlijk is, met een flinke kans op "voorzichtig" (GOK).

## 3. Kanalen buiten de winkel

| Kanaal | Regels | Bereik | Hoe makers het doen | Past het? |
|---|---|---|---|---|
| **Connect IQ Showcase** (Garmin-forum) | Zelfpromotie mag alleen hier, plus een link naar je winkelpagina (forumregels, gelezen 10 nov, `lancering.md`). Garmin: "a good place to get [feedback]", support mag maar is openbaar (`https://forums.garmin.com/developer/connect-iq/w/wiki/9/showcase`, GEZIEN 12 nov). | Klein, vooral andere makers (GOK). In de Showcase-draad van Breathing Timer (gratis ademapp, 1.000+) staan alleen berichten van de maker zelf (GEZIEN). | Eén draad per app met uitleg en updates (Breathing Timer, Ski Pin). De Ski Pin-draad met echte cijfers kreeg wel veel reacties. | Ja, kost weinig. Hier ook later een eerlijk verslag met cijfers, dat lezen makers graag. |
| **r/Garmin** | NIET GELEZEN: Reddit gaf een omleiding op `old.reddit.com/.../about/rules.json` en verder lezen werd geblokkeerd. Thijs moet de regels zelf lezen (zijbalk of "About"). | Groot (GOK: honderdduizenden leden). | Berichten als "I coded ... app for my Garmin" bestaan (zoekresultaat, niet gelezen). | Ja, als de regels het toelaten: als maker, eerlijk, één keer. Grootste kans van alle kanalen (GOK). |
| **r/GarminWatches** | Niet gelezen (zelfde reden). | Kleiner (GOK). | Onbekend. | Alleen als r/Garmin niet mag; niet beide op één dag. |
| **r/breathwork** | Niet gelezen. | Middel (GOK). Publiek dat ademrondes doet, maar niet iedereen heeft een Garmin. | Onbekend. | Misschien, als vraag ("doen jullie dit op je horloge?") en alleen als zelfpromotie mag. |
| **r/Meditation** | Niet gelezen. Veel meditatiefora zijn streng tegen apps (GOK). | Groot, maar weinig Garmin. | Onbekend. | Nee: past slecht (Ebb is vooral ademrondes) en de kans op verwijderen is groot. |
| **r/wimhof** | Niet gelezen. | Middel (GOK). | Onbekend. | Voorzichtig nee. We noemen Wim Hof nergens (merk), en dit publiek jaagt vaak op lange inhoudtijden; Ebb beloont dat juist niet. Hooguit later als iemand er zelf naar vraagt. |
| **Facebook-groepen** (per horloge, bv. fenix of Forerunner) | Niet gelezen (inloggen nodig). Een oude maker noemt "face book groups for some devices" als kanaal (draad 234215, GEZIEN). | Onbekend. | Onbekend. | Later, alleen als Thijs zelf al lid is. |
| **YouTube en blogs** (the5krunner, DC Rainmaker, Android Authority, Wareable) | the5krunner heeft een "Top 100 Garmin Connect IQ Apps" (15 jan 2026) en schreef over een kleine maker zonder abonnementen (16 jul 2026), gevonden via zoeken; de pagina zelf kon ik niet lezen (Cloudflare). | Groot. | VAW.BE noemt een Android Authority-lijst als reden voor installs (GEZIEN). | Later (week 3 of 4), één korte mail aan the5krunner met de link, als er al een paar beoordelingen zijn. Geen garantie. |
| **Garmin zelf (uitgelicht, nieuwsbrief)** | Zie onderdeel 1: hero-afbeelding met naam en slagzin, daarna vragen via het forum (2019). | Groot (5x downloads volgens GdcSoft). | Nomineren kan niet volgens jim_m_58 (2026). | Hero-afbeelding klaarzetten kost weinig; vragen mag, verwachten niet. |
| **Betaalde advertenties** | Mag. | Te koop. | VAW.BE doet het. | Nu niet: bij $4,24 per koper is dat bijna zeker verlies (GOK). |

**Waarom r/freediving en alles met apneatraining eruit ligt:** Garmin verbiedt apps die bedoeld zijn voor gebruik bij freediving (`upload-en-keuringsregels-2026-11-11.md`, regel 1). Als wij Ebb op een freedivingforum aanprijzen, maken we er zelf een freedivingapp van, in onze eigen woorden en onder onze naam. Dat kan de app uit de winkel laten halen. Daarnaast willen freedivers tabellen en langere tijden, en Ebb beloont langer inhouden nergens; het publiek past niet en de kans op boze reacties is groot. Sinds winkeltekst v14 staan de woorden freediving en apnea ook niet meer in de tekst. Het oude concept 3 in `lancering.md` vervalt dus.

## 4. Proberen voor kopen

**Wat Garmin's betaalsysteem toelaat (GEZIEN):**
- Geen proefperiode. "The GarminPay system is completely different and only has the 48 hour refund. No trial apps." (jim_m_58, ongeveer jun 2026, draad van de maker van RuckTrack, `https://forums.garmin.com/developer/connect-iq/f/connect-iq-web-store/436796/adding-a-7-day-trial-to-a-garmin-pay-paid-app-what-s-the-official-path`). De maker zelf: "the 48-hour refund window is the closest thing to a trial". Ook Breathe heeft `hasTrialMode: false` (API, GEZIEN).
- Kortingscodes kan je per mail bij Garmin aanvragen: welke app, hoeveel, hoe lang geldig, hoeveel korting; het moet door een keuring en duurt een paar dagen (`https://forums.garmin.com/developer/connect-iq/f/connect-iq-web-store/403209/how-to-generate-promo-codes-for-ciq-store-purchase`, GEZIEN). Garmin noemt codes ook in de eigen uitleg, voor overstappers (`App_Sales.html`, GEZIEN). In de API heeft elke prijs een `salePrice` naast `listPrice` en een lijst `appliedPromotionGuids` (GEZIEN); acties bestaan dus.
- Een eigen betaalsysteem (KiezelPay) heeft wel proeftijd, maar dan staat de app als gratis in de winkel met een betaalmuur, met een code en internet. Dat is precies wat onze tekst belooft níet te doen ("no unlock code by e-mail"). Valt af.

**De opties en wat ze kosten:**

| Optie | Wat het doet | Bouwwerk (GOK) | Oordeel |
|---|---|---|---|
| A. Niets, alleen de 48 uur | Wie twijfelt koopt en kan binnen 48 uur terug | 0 | Dit is versie 1.0. De 48 uur staat al in de tekst. |
| B. **Gratis "Ebb Free"** als aparte app | Bijvoorbeeld Calm 4-7-8 en één ronde per dag, met de eerste paar dieren; in de tekst een link naar de volle Ebb | 1 tot 2 dagen: zelfde code met een bouwvlag, eigen app-id, eigen winkelpagina, tweede keuring | **Doen in 1.1.** Dit is het patroon van alle drie de best lopende betaalde ademapps. De gratis app vangt zoekverkeer van mensen die nooit voor een onbekende app betalen. |
| C. Kortingscodes | Codes voor testers of een actie | Alleen een mail aan Garmin | Ja, een handvol voor de eerste testers (zie onderdeel 5). |

**Advies voor 1.1:** Ebb Free met **Calm 4-7-8 helemaal gratis** en **Breath Hold Rounds beperkt** (bijvoorbeeld 3 rondes per sessie, één sessie per dag) en **alleen de eerste 3 dieren**; het einde van de reis ("8 of 24 found") laat zien wat de volle versie geeft. Geen betaalmuur, geen code: je koopt de volle Ebb gewoon in de winkel. Let op: voortgang gaat niet mee van Free naar de volle app (aparte apps, GOK); zeg dat eerlijk in beide teksten. En: Free moet dezelfde veiligheidszinnen en dezelfde randen hebben (niet langer inhouden belonen, geen duikwoorden). Het nadeel: Free kan de betaalde verkoop opeten. Bij WHM en Bitochi gebeurt dat niet zichtbaar; de betaalde versie loopt juist dankzij de gratis (AFGELEID uit de cijfers hierboven).

## 5. Beoordelingen

**Regels (GEZIEN):**
- Garmin: "You must not perform or encourage any action that creates deceptive reviews or manipulates your app's rating" (`https://forums.garmin.com/developer/connect-iq/b/news-announcements/posts/tips-for-monetizing-your-apps`, 17 dec 2021). In 2020 kondigde Garmin aan alle apps af te wijzen van makers die het beoordelingssysteem bespelen (`.../posts/fake-reviews`, 7 dec 2020).
- Onze eigen keuringsnotitie: geen beoordelingen kopen of om ruil vragen (`upload-en-keuringsregels-2026-11-11.md`, regel 9).
- In de winkeltekst vragen mag in elk geval in de praktijk: Breathe eindigt met "Enjoying Breathe? Please leave a review — it helps other Garmin owners find the app." (GEZIEN, API).
- Garmin heeft geen knop in het horloge om een beoordeling te vragen (GOK). Een zin op het scherm is technisch mogelijk. **Ons eigen besluit is: nooit om een review vragen in de app.** Dat houden we in 1.0.

**Hoe makers aan de eerste beoordelingen komen (GEZIEN, Ski Pin-draad):** "Getting a base of positive reviews is the only defense" tegen negatieve; een andere maker zet in zijn tekst dat mensen met een probleem hem moeten mailen in plaats van een slechte beoordeling te schrijven, "That seems to work to some extent". Antwoorden op een slechte beoordeling: "No one is going to change their review. Your only option is to explain the situation in a reply."

**Plan voor 5 tot 10 eerlijke beoordelingen (AFGELEID/GOK):**
1. Thijs vraagt persoonlijk 10 mensen die een rond Garmin-horloge hebben (vrienden, collega's, sportclub) of ze Ebb een week willen gebruiken. Ze krijgen een kortingscode van Garmin (of kopen hem zelf). Na een week: "Als je wil, schrijf in de winkel wat je echt vindt." **Niet:** vragen om vijf sterren, iets terug geven voor een beoordeling, beoordelingen ruilen met andere makers, of mensen laten beoordelen die de app niet gebruikten.
2. In de berichten (Showcase, Reddit) aan het eind: "Feedback welcome, here or by mail." Geen oproep tot beoordelen op Reddit (daar is dat vaak tegen de regels, GOK).
3. Thijs antwoordt op elke beoordeling, ook de goede, kort en vriendelijk. Kost 2 minuten per stuk.
4. Winkeltekst: één zin "Problem or idea? Mail us first, we answer." staat er in feite al (SUPPORT AND REFUNDS). Een zin "Enjoying Ebb? A review helps other Garmin owners find it." kan erbij, maar de tekst zit op 3.996 van de 4.000 tekens. Pas bij 1.1, als er ruimte gemaakt wordt.
5. Met 1 beoordeling per 20 tot 50 kopers (onderdeel 2) komen er uit de verkoop alleen maar weinig. De eerste tien moeten dus uit de kring van punt 1 komen, anders duurt het maanden.

**Voorstel voor de hoofdchat (geen besluit van mij):** in 1.1 één neutrale zin op het eindscherm, één keer, na de vijfde sessie die telt: "Like Ebb? A store review helps." Zonder beloning, zonder dier. Garmin verbiedt dit niet zover ik zag; het past alleen niet bij ons eigen besluit, dus dat beslist de hoofdchat.

## 6. Prijs

**Wat vergelijkbare apps vragen (GEZIEN, API en dataset):** ademapps $1,99 tot $6,25: WHM breathing+ $4,99 (beste verkoper), Breathe $2,99, HRV Breathing $3,99, Kids Breathing $4,49, BTS PRO $6,25, Vytera $4,99. Van de 632 nieuwe betaalde horloge-apps sinds juni 2025 kost het grootste deel rond $2 (421 apps op afgerond $2), 26 rond $5 (AFGELEID uit de dataset). Bij "Top Paid Apps" staan apps van $1,99 tot $9,49 door elkaar.

**Kortingen bij lancering:** geen enkele van de ademapps had op 12 nov een `salePrice` lager dan `listPrice` (GEZIEN bij Breathe; bij de anderen alleen `listPrice` bekeken). Of Garmin bij een prijswijziging opnieuw keurt: voor de overstap van gratis naar betaald wel ("the app is temporarily removed from the store so it can be reviewed again", `App_Sales.html`, GEZIEN); voor een gewone prijswijziging NIET GEVONDEN.

**Advies: houd $4,99.** Onderbouwing:
- De beste verkoper in ons hoekje vraagt $4,99 en verkoopt al bijna twee jaar (GEZIEN).
- Ski Pin ging van $3,99 naar $4,99 zonder zichtbare terugval; voor kopers voelt het als "5 bucks" (GEZIEN, maar één maker).
- Ons probleem is gevonden worden, niet de prijs. Een lagere prijs geeft per koper minder ($2,54 netto bij $2,99 tegen $4,24 bij $4,99, AFGELEID) en lost het gevonden worden niet op. Om dezelfde opbrengst te halen moet $2,99 ruim 1,7 keer zoveel kopers trekken; daar is geen bewijs voor.
- Een lanceringskorting heeft alleen zin als er al publiek is dat hem ziet. Dat hebben we niet. Bewaar kortingscodes voor testers en voor later (bijvoorbeeld rond nieuwjaar, als mensen goede voornemens hebben; GOK).
- Wat wél helpt tegen de drempel: Ebb Free (onderdeel 4) en de 48 uur geld terug, die al in de tekst staan.
- Wanneer wel zakken: als we na 60 dagen onder het voorzichtige scenario zitten en Ebb Free er al is. Dan $3,99 proberen, één keer, en 30 dagen meten.

---

## Plan voor de eerste twee weken na goedkeuring

Wie: **Thijs** (plaatst en antwoordt zelf), **Gijs** (Garmin-manager, Claude: meet, schrijft concepten, houdt het logboek bij), **hoofdchat** (beslist over 1.1). Dag 1 is de dag dat Garmin goedkeurt.

| Dag | Wie | Wat | Minuten Thijs |
|---|---|---|---|
| Dag 0 (voor goedkeuring) | Gijs | Concepten hieronder naast de echte app leggen; hero-afbeelding (naam plus slagzin "Breathe. Make sea friends.") klaarzetten | 0 |
| Dag 0 | Thijs | Regels van r/Garmin en r/breathwork lezen (zijbalk of "About"). Lijst van 10 mensen met een rond Garmin-horloge maken | 15 |
| Dag 0 | Thijs | Mail aan Garmin voor 10 kortingscodes (concept: Gijs) | 5 |
| Dag 1 | Gijs | Nakijken dat de winkelpagina goed staat (titel, tekst, beelden, prijs, horloges) via de API; link in het logboek | 0 |
| Dag 1 | Thijs | Ebb zelf kopen en op je eigen horloge zetten (bewijs dat kopen werkt, ook met jouw kaart) | 10 |
| Dag 1 | Thijs | De 10 mensen persoonlijk een berichtje sturen, met code als die er is | 30 |
| Dag 2 | Thijs | Showcase-draad plaatsen (concept 1), in eigen woorden | 15 |
| Dag 3 (bij voorkeur di, wo of do, Amerikaanse ochtend, 15:00 tot 17:00 NL; GOK) | Thijs | r/Garmin-bericht, als de regels het toelaten (concept 2). Dat uur erna reacties lezen en kort antwoorden | 45 |
| Dag 3 tot 14 | Gijs | Elke dag via de API: downloademmer, aantal beoordelingen, plek in "breathing", "breath hold", Top Paid, Trending, Hot & Fresh. In `logboek.md` | 0 |
| Dag 3 tot 14 | Thijs | Elke dag 5 tot 10 minuten: beoordelingen en reacties lezen, antwoorden. Bugs doorgeven aan Gijs | 60 tot 100 in totaal |
| Dag 7 | Thijs | Navragen bij de 10 mensen: "Gebruik je hem? Wat mis je? Als je wil, schrijf een eerlijke beoordeling." | 15 |
| Dag 7 | Gijs | Weekverslag: kopers (uit het verkooprapport dat Thijs kan aanvragen onder Merchant account, Documents, of uit de emmer), beoordelingen, vragen. Begin Ebb Free op een proeftak | 0 |
| Dag 8 | Thijs | Alleen als r/Garmin niet mocht of weinig deed: r/breathwork (concept 3) | 20 |
| Dag 10 | Hoofdchat | Besluit over 1.1: Ebb Free, en de zin over beoordelingen | 0 |
| Dag 14 | Gijs | Verslag twee weken: welk scenario (voorzichtig, gewoon, goed), wat werkte; voorstel voor week 3 en 4 (mail aan the5krunner, Ebb Free indienen) | 0 |
| Dag 14 | Thijs | Showcase-draad bijwerken met een korte update (wat er verbeterd is), geen reclame | 10 |

Totaal voor Thijs: ongeveer 4 tot 4,5 uur verspreid over twee weken, waarvan het meeste kort dagelijks lezen en antwoorden.

**Niet doen:** in groepen of fora posten waar zelfpromotie verboden is; hetzelfde bericht op vijf plekken tegelijk; beoordelingen vragen in ruil voor iets; freediving- of apneafora; advertenties kopen.

---

## Nieuwe concepten voor de berichten (kloppen met winkeltekst v19)

Regels voor alle drie: Thijs herschrijft ze in eigen woorden en zet er iets bij dat alleen hij weet (waarom hij het maakte, hoe hij het zelf gebruikt). Nergens de woorden freediving, apnea, Wim Hof, record of "best time". Geen gezondheidsbeloftes (geen stress, slaap, angst). Altijd: alleen op het droge, zitten of liggen. Echte link pas als Ebb in de winkel staat. Lees ze vlak voor het plaatsen naast `producten/garmin-adem/winkeltekst.md`; als de app verandert, verandert de tekst mee.

Wat de app nu doet (uit winkeltekst v19, tak `claude/garmin-2026-11-10b`): het water stijgt als je inademt en zakt als je uitademt; bij inhouden ga je onder water met een zeedier en het beeld blijft gelijk hoe lang je ook inhoudt; een vis zwemt mee vanaf de eerste sessie; 24 zeedieren door sessies en weken op rij, nooit door langer inhouden; hoogstens twee sessies per dag tellen; weekdoel 3 (2 tot 7), rustdagen breken de reeks niet; vanaf 3:00 staat er "breathe" bovenaan en trilt hij elke 30 seconden; na vijf minuten stopt een inhouding vanzelf; elke fase een eigen trilling; opslaan als ademactiviteit in Garmin Connect met hartslag; $4,99 eenmalig, geen abonnement, geen code, geen extra account, geen telefoonapp; 48 uur geld terug via Garmin.

### 1. Connect IQ Showcase (Garmin-forum)

Titel: `Ebb: breathwork rounds and calm 4-7-8 on a round watch, with a sea that fills with animals`

> Hi all. I made Ebb, a breathing app for round Garmin watches. Your watch face becomes a porthole on a small sea: the water rises as you breathe in and falls as you breathe out. When you hold your breath you go under water with a sea animal, and the picture stays the same however long you hold.
>
> Two modes: breath hold rounds (deep breaths at a steady pace, then a hold for as long as feels easy, then a short recovery breath) and calm 4-7-8. You can also set your own pattern. Every phase has its own vibration, so it works with your eyes closed.
>
> A small fish swims with you from the first session. 24 sea animals join as you keep coming back: sessions and weeks in a row, never by holding longer. Rest days don't break the streak.
>
> Sessions save to Garmin Connect as a breathing activity with heart rate. $4.99 once through the Garmin store, no subscription, no code, no extra account. For use on land only: sit or lie down.
>
> Store: <link>
> Questions, bugs and ideas are welcome in this thread or at the support address on the store page.

### 2. r/Garmin (alleen als de regels het toelaten)

Titel: `I made a breathing app for round Garmins where sea animals join you as you keep coming back`

> Maker here, so yes, this is my own app. Ebb does breath hold rounds and calm 4-7-8 breathing. The watch face is a little sea that rises and falls with your breath, and you go under water while you hold. 24 sea animals join over time if you keep showing up (sessions and weeks in a row). Holding longer gets you nothing extra, on purpose, so there's no reason to push.
>
> Every phase has its own buzz, so I mostly do it with my eyes closed. It saves to Connect as a breathing activity. $4.99 once, no subscription or unlock codes. Works on 28 round watches, the store page lists which.
>
> I'd really like to hear what's missing or annoying. <link>

Tip: één schermafbeelding erbij (de poster v5 met de krab, of kaart 2 met de schildpad onder water). Geen video met muziek. Geen oproep tot beoordelen.

### 3. r/breathwork (alleen als zelfpromotie mag; anders niet plaatsen)

Titel: `Do you do your breathwork rounds on a watch? I built one for Garmin and would like honest feedback`

> I do breathing rounds most mornings and wanted to follow them by vibration with my eyes closed, so I built a small app for round Garmin watches. Rounds of deep breaths, a hold for as long as it feels easy, a short recovery breath; and a calm 4-7-8 mode for evenings.
>
> It deliberately doesn't reward longer holds. You collect sea animals by coming back on different days and keeping a weekly streak, rest days included. Land only, sitting or lying down.
>
> Curious what people here would want from a watch for this. Link if you want to look: <link> (it's paid, $4.99 once, I'm the maker).

### Na het plaatsen
- Link en datum per plek in `platformen/garmin/logboek.md` (Gijs, als Thijs het meldt).
- Vragen of bugs uit de draden naar `taken.md`. Antwoorden doet Thijs zelf of laat het; Claude plaatst nooit iets.
- `lancering.md` (de oude concepten) is hiermee vervangen; concept 3 voor r/freediving vervalt.

## Wat ik niet kon nagaan
- De regels van alle subreddits: Reddit gaf een omleiding op `old.reddit.com/r/<naam>/about/rules.json`; verder proberen werd geblokkeerd. Niets over Reddit-regels hierboven is gezien.
- Echte verkoopcijfers van ademapps: Garmin toont alleen emmers. De verhouding beoordelingen tot kopers is geschat uit Ski Pin (één maker).
- Hoe de winkel rangschikt: alleen wat makers vermoeden, niets van Garmin zelf.
- Of de Connect IQ-app op de telefoon andere lijsten toont dan de website (de draad van jpcams noemt "Performance Metrics" en "Training Metrics" op het tabblad Home); niet zelf gezien.
- Facebook-groepen, YouTube en the5krunner (Cloudflare blokkeert curl): bereik onbekend.
- Of een gewone prijswijziging een nieuwe keuring vraagt.
