# Voorstel: spellen voor Android Auto (auto-scherm, alleen als de auto stilstaat)

Noor, 17 nov 2026 ±10:10 UTC. Cijfer **7**. Advies: **ja, met kleine inzet**, samen met de Play-route voor Android XR (één Play-account voor beide).

## Wat is er nieuw
Op 21 sep 2026 haalde Google de categorie spellen voor Android Auto (telefoon aan de auto) en Android Automotive OS (Google ingebouwd in de auto) uit de bèta. Elke maker mag nu spellen via Google Play uitbrengen; daarvoor kon het alleen met toestemming van Google. Spellen werken alleen als de auto stilstaat, bijvoorbeeld bij de laadpaal (GEZIEN, https://android-developers.googleblog.com/2026/09/bring-android-game-to-car-screen.html, gedateerd 21 September 2026).

## De vijf vragen

**1. Groot publiek, groeit het?** Meer dan 250 miljoen auto's kunnen Android Auto aan (DERDEN, cijfer van Google via https://www.auto123.com/en/news/android-auto-updated-2026/73903/). Spellen op Android Auto vragen een telefoon met Android 15 of nieuwer (GEZIEN, blog Google). Welk deel van de Android Auto-gebruikers dat heeft, weet ik niet; een derde tot de helft is een GOK. Elektrische auto's groeien, en laden geeft 15 tot 40 minuten wachttijd (GOK, gangbaar). Publiek is dus ruim boven de 100.000, maar hoeveel mensen echt spelen in de auto is onbekend.

**2. Winkel jong, hoeveel apps?** Open voor iedereen sinds 21 sep 2026, nu 8 weken. Op 22 sep "around 30 games" op Android Auto (DERDEN, https://9to5google.com/2026/09/22/android-auto-rolls-out-game-support-no-longer-in-beta/). Op 23 sep telde Mobilsiden 29 spellen voor Android Auto en 264 voor Android Automotive (DERDEN, https://mobilsiden.dk/nyheder/her-er-alle-spil-til-android-auto-og-android-automotive/, met de volledige lijst). Zelf de twee lijsten van Google Play geopend: de eerste pagina toont telkens 20 spellen (GEZIEN, `promotion_apps_beto__games_on_android_auto__collection`); verder bladeren lukte niet met curl, dus een eigen telling van vandaag heb ik niet.

**3. Kan er betaald worden?** Ja, het is gewoon Google Play: betaalde apps en aankopen in de app. De betaalregel PA-1 in de kwaliteitslijst voor auto's (geen abonnementen afsluiten in de auto) geldt voor navigatie, POI, IOT en weer, niet voor spellen (GEZIEN, https://developer.android.com/docs/quality-guidelines/car-app-quality, "Last updated 2026-09-14"). Of een aankoop in de auto zelf soepel gaat, heb ik niet getest; kopen op de telefoon kan altijd (GOK).

**4. Is er vraag?** Pers schrijft de spellen aan als iets voor de laadpaal (Mobilsiden, 9to5Google, Auto Express). Eigen vraagmeting op forums niet gedaan. Wat ik wel zie: de 29 spellen op Android Auto zijn bijna alle kinderspellen (LetraKid, RV AppStudios, Color Kids), plus King, Rovio, Outfit7 en twee racers (DERDEN, lijst Mobilsiden; de 20 die ik zelf zag zijn van dezelfde soort, GEZIEN).

**5. Is de eerste plek te pakken? Basistaak week 1.** Een volwassene bij de laadpaal zoekt een rustig spelletje voor een kwartier: sudoku, patience (solitaire), kruiswoord of woordzoeker, 2048, schaken. Op Android Automotive bestaan die al (Andoku Sudoku 3, AutoSudoku, Solitaire, Chess, English Crossword Puzzle, 2048 Automotive). **Op Android Auto staat er op 23 sep geen enkel sudoku-, patience-, woord- of schaakspel** (DERDEN, lijst Mobilsiden; ook niet in de 20 die ik vandaag zag, GEZIEN). Dat is de lege hoek: de basistaak voor volwassenen op het grootste van de twee publieken.

## Productidee
"Laadpauze": één app met 3 rustige klassiekers (sudoku, patience, woordzoeker), grote vakken voor een autoscherm, met de vinger of een controller, stand bewaard als de auto gaat rijden. Gratis met een dagpuzzel en één eenmalige aankoop voor alles (geen abonnement). Werkt op Android Auto én Android Automotive, en gewoon op de telefoon. Talen vanaf versie 1 (les Joris verhaal 34).

## Kunnen wij snel live zijn?
- Bouwen: Kotlin en Compose, gewone Android-app met een paar regels in de manifest (`android:appCategory="game"`, categorie voor Android Auto, stoppen met geluid als de auto rijdt) (GEZIEN, blog Google). Een eerste versie binnen een week: ja (GOK, eenvoudige puzzels).
- Testen in de cloud: Android Automotive-emulator kan op een Linux-machine met KVM (GitHub Actions heeft dat); de Desktop Head Unit voor Android Auto wil een telefoon via ADB, met een emulator als telefoon is niet geprobeerd (GOK).
- **De echte rem is Google Play zelf.** Dortus heeft nog geen Play-account. Een nieuw persoonlijk account moet eerst een gesloten test draaien met minstens 12 testers die 14 dagen achter elkaar meedoen, pas daarna mag een app live (GEZIEN, https://support.google.com/googleplay/android-developer/answer/14151465). Een organisatie-account heeft die regel niet, maar vraagt een D-U-N-S-nummer (staat bij Thijs of het kan). Realistisch live: 5 tot 6 weken na het account (testers plus keuring van Google), dus eind december als Thijs deze week een account maakt.

## Controle (hulpagent, 17 nov ±10:15 UTC)
Alle GEZIEN- en DERDEN-cijfers kloppen met de bronnen. De Play-collectie is vandaag in de VS, Nederland, Duitsland en Groot-Brittannië dezelfde 20 spellen als op 23 sep (GEZIEN); geen aankondiging gevonden van een sudoku, patience, woord- of schaakspel voor Android Auto sinds 21 sep (DERDEN). De lege hoek is dus bevestigd voor wat zichtbaar is; voor de laatste 9 van de lijst blijft het een redelijke GOK. Twee dingen die ik miste:
- Google keurt elk autospel apart tegen de kwaliteitslijst voor spellen, bovenop de 14 dagen met 12 testers. Live dus eerder over 5 tot 6 weken dan 4 (GOK).
- Regel DO-2: het spel moet het brede scherm vullen, geen zwarte randen (GEZIEN, https://developer.android.com/training/cars/parked/games). Een vierkant sudokuraster vraagt een zijpaneel. Geen heads-up-meldingen (IN-2), dus geen herinnering voor de dagpuzzel als melding in de auto.
- De collectie in Play is sinds 23 sep niet veranderd: of nieuwe spellen erin komen is een echt risico voor de vindbaarheid.

## Risico
- Niemand speelt in de auto: er zijn geen gebruikscijfers per spel in de auto. Teken dat het stokt: over 4 weken nog steeds ±30 spellen op Android Auto en geen nieuwe artikelen.
- Google zet zelf of een grote maker (bijv. Microsoft Solitaire, NYT) een sudoku of patience neer: dan is de eerste plek weg. Daarom snel zijn.
- Vindbaarheid: mensen vinden autospellen via de collectie in de Play-app op de telefoon. Of Google nieuwe spellen in die collectie zet, weet ik niet (GOK).
- De 12 testers zijn een praktische drempel voor Thijs.

## Waarom 7 en geen 8
Groot publiek, categorie 8 weken open, ±30 spellen, de basistaak voor volwassenen is leeg, betalen werkt: dat is precies de meetlat. Geen 8 omdat er geen enkel cijfer is over hoeveel mensen spelen, en omdat live gaan door de Play-testregel eerder 4 weken duurt dan 1.

## Herhaalmeting
Over 4 weken (15 dec): aantal spellen in de Android Auto-collectie opnieuw tellen (Mobilsiden-lijst of de Play-collectie met een browser) en kijken of er een sudoku of patience bij is gekomen.
